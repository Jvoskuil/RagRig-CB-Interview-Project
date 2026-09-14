# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on a process event from your shift — I'll ask you to walk me through what happened and how you made a few of the calls along the way. Nothing here goes into your personnel file, it's for improving our SPC response process. Sound okay? Participant: Sure, no problem. Happy to walk through it. Interviewer: Great. Can you start by telling me what your role was that day and what first drew your attention to the control chart? Participant: I'm the QA analyst covering statistical process control for the turning cell that makes the automotive shafts. I was watching the Xbar-R chart for outer diameter like normal, two subgroups an hour from the automated gauge. I noticed three subgroup means in a row creeping downward, and the most recent one landed in the warning zone — inside two sigma, not over the LCL yet. Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average. Interviewer: What was going through your mind at that point? Participant: Honestly, at 62% through the shift's quota, my first instinct was not to panic. A single warning-zone point isn't automatically an assignable cause under the Western Electric rules — you need a pattern. But three downward-trending points is a pattern worth respecting. Nothing had been logged yet, no maintenance, no material change, so I didn't have an obvious explanation. Interviewer: Walk me through what happened next, chronologically. Participant: I tightened up sampling instead of pulling the trigger on a full stop. I figured if it was real, the next subgroup would confirm it, and if it was noise, extra samples would show it settling back down. Sure enough, the next subgroup crossed the LCL outright. I did a manual spot check with a hand micrometer to rule out a gauge artifact, and it matched the automated reading, so I knew it was real. Interviewer: At that first decision point, what alternatives did you weigh, and why did you choose to increase sampling rather than halt immediately? Participant: I could have shut it down right there, or just logged it and kept going. Stopping the line on one warning-zone point felt premature — that costs us 45 minutes of changeover time we might not need, and we're still trying to hit quota. Ignoring it felt reckless given the trend. Increasing sampling was the middle path — get more data fast without committing to downtime. Interviewer: Once you confirmed the out-of-control signal, what did you look at to figure out the cause? Participant: I pulled up everything I had access to in real time. The shop floor temperature log showed about a three-degree rise over the same two-hour window as the drift. The material lot traveler — which lags real time by about an hour — showed a new lot had been loaded roughly ninety minutes before the drift started. I hadn't checked the tool wear sensor yet at that point. I also asked our process engineer if he'd seen anything like this before, and he said no, actually — this was the first time he'd seen a pattern like this line up with a temperature swing on this particular machine. Interviewer: Given the engineer didn't have a precedent for you, what made you still lean toward temperature as the explanation? Participant: The timing just lined up so cleanly on its own — the temperature started climbing and almost immediately the dimension started walking. I didn't have history to lean on this time, but the correlation itself felt tight enough to run with. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and the temperature story felt like it explained things well enough that I didn't prioritize that test at the time. Interviewer: Did you do anything to directly check the lot hypothesis before moving forward? Participant: Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption. Interviewer: Let's move to the next stretch of the shift. What came in after that? Participant: The tool wear sensor data finally came through. It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine. Interviewer: How did that sensor reading change your thinking about the tool? Participant: It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment. I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one. Interviewer: So what did you decide to do? Participant: I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away. Interviewer: Looking back, what alternatives did you consider there, and why didn't the offset feel like enough given what the sensor showed? Participant: I considered halting for a tool change outright, and I considered just running it out unchanged since the tool was 'recently serviced.' The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet. Interviewer: What happened after that adjustment? Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding. Then shift changeover happened, and the incoming night operator mentioned the tool had sounded different in the last hour — a cue I obviously didn't have access to until after the handoff. Interviewer: Bring me to the end of the shift. What did the final data show, and what did you decide? Participant: By the end, several parts were near or slightly under the lower spec limit. The wear sensor was up to 91%. Cpk for the last two hours had dropped from 1.42 to 1.05, which is a real capability hit. At that point I recommended an immediate tool change, a temporary update to the control chart center line, and I filed a deviation report covering the affected parts. Interviewer: What tipped you fully toward that recommendation? Participant: The Cpk drop was the clincher, honestly, combined with the wear number climbing another thirteen points in a short window. That's not marginal anymore, that's a tool that's clearly done. And with parts sitting near spec limits, a deviation report was required regardless of what I concluded about the cause. Interviewer: What happened after the tool change? Participant: It resolved it. The next shift's dimensions went right back to the historical baseline. And when the lab result on that new material lot finally came back, the hardness was within spec after all — so that wasn't a factor. Interviewer: If the engineer had told you this machine had a history of temperature-linked drift, do you think you would have felt any more confident in the temperature explanation than you already did? Participant: Maybe a little more confident, but honestly the timing alone did most of the convincing for me. Having a precedent would have made it feel more settled, but I don't think it would have changed what I actually did — I was already comfortable running with it based on how closely the two things tracked. Interviewer: And if the lot hardness test had come back out of spec instead? Participant: Then I'd have had two live explanations instead of one, and I probably would have had to test them against each other more directly instead of settling on temperature early. Interviewer: Looking back, is there anything about how you weighed the temperature information against the lot information that you'd do differently, especially without a precedent to lean on? Participant: In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote. Not having the engineer's backup actually should have made me want more direct evidence, not less, but in the moment the timing was persuasive enough on its own. Interviewer: How much did the approaching shift changeover and time pressure shape your decisions overall? Participant: Quite a bit, especially at the tool wear point. Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in. Interviewer: That's really helpful, thank you for walking through all of that in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.05s · gen 78.20s · total 82.9s_

**Retrieved** (ranked by store ranker):
1. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0273 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
2. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0261 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0260 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0257 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0252 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0241 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0240 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0236 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Hallihan_etal_DTM_12.pdf** — 0.0233 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
10. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0224 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0220 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0217 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0208 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0208 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0205 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
17. **Lyell Automation bias and verification complexity.pdf** — 0.0200 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0179 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
22. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0176 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
25. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0166 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
26. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0166 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
28. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
29. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0162 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0158 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
32. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
33. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0156 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
36. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0149 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
39. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0147 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration more often than th_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0147 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0145 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
46. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0144 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
47. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0143 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
48. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0143 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
49. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0141 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "The analysis is restricted to the participant's contemporaneous reasoning and decisions during the SPC process event. Hypothetical questions and retrospective reflections were used only when they clarified the mechanisms operating at the time."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "selective hypothesis testing",
        "positive test strategy",
        "belief-consistent information processing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and emphasize evidence in ways that support a favored hypothesis while giving insufficient attention to evidence or tests that could disconfirm it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Cause attribution after out-of-control signal",
      "decision_point_description": "Choosing between temperature and material-lot hypotheses and deciding whether to directly test the new material lot before acting on the temperature explanation.",
      "affected_reasoning_operation": "Evidence weighting, hypothesis generation, and causal inference",
      "bias_specific_mechanism": "After observing a close temporal correlation between temperature rise and dimensional drift, the participant formed a preferred temperature hypothesis. He then used the timing correlation as sufficient confirmatory evidence, sought additional documentation for the temperature account, and deferred direct testing of the alternative material-lot hypothesis. The absence of prior engineer precedent did not lead him to test the temperature account more rigorously; instead, he continued under the favored explanation.",
      "manifestation_in_interview": "The participant explicitly stated that the timing correlation felt tight enough to run with, that the temperature story explained things well enough, and that he did not prioritize the lot hardness test at the time. He kept the lot hypothesis as a secondary footnote while monitoring under the temperature assumption.",
      "effect_on_reasoning_or_decision": "The participant did not pull a hardness sample on the new material lot when the alternative was available, which left the lot explanation unexamined and channeled his investigative attention toward the temperature hypothesis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The timing just lined up so cleanly on its own — the temperature started climbing and almost immediately the dimension started walking. I didn't have history to lean on this time, but the correlation itself felt tight enough to run with. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.",
          "evidence_explanation": "This quote demonstrates selective hypothesis acceptance: a temporal correlation was treated as sufficiently persuasive even without precedent, and an available test of an alternative hypothesis was deprioritized because the favored explanation already felt adequate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption.",
          "evidence_explanation": "This quote shows the participant directed evidence-documentation and monitoring toward the favored temperature hypothesis while preserving the lot hypothesis only as a secondary, unexamined note."
        }
      ],
      "correction_or_counterevidence": "The participant did log the material lot as a secondary possibility, and later lab results ruled the lot explanation out. However, that later result does not neutralize the earlier biased weighting: at the time, he chose not to directly test the alternative and instead continued under the temperature assumption.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Cook and Smallman source supports the general confirmation-bias mechanism of selectively selecting and prioritizing evidence consistent with a hypothesis during investigation.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human Factors of the Confirmation Bias in Intelligence Analysis: Decision Support from Graphical Evidence",
          "authors": "Cook & Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at assessment but a strong and pervasive confirmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "The source documents confirmation bias as a strong and pervasive tendency to select and prioritize evidence consistent with a hypothesis during investigation.",
          "relevance_to_this_occurrence": "The participant selected and prioritized temperature-timing evidence consistent with his favored explanation while failing to directly test the alternative material-lot hypothesis."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "insufficient adjustment",
        "belief perseverance"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information or prior belief and to make insufficient adjustments when new evidence arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Tool wear sensor interpretation and intervention decision",
      "decision_point_description": "Deciding whether to initiate a full tool change or continue running with a smaller offset after receiving the tool wear sensor reading.",
      "affected_reasoning_operation": "Causal inference and risk updating under prior beliefs",
      "bias_specific_mechanism": "The participant anchored on the prior mental model that the tool had been recently serviced and therefore should not be a major factor. When the wear sensor showed 78% of rated tool life, he treated the reading as surprising but still adjusted only partially, choosing a small in-process offset rather than a full tool change. The prior anchor made the striking sensor data feel insufficient to justify a large intervention.",
      "manifestation_in_interview": "The participant explicitly stated that the mental model of the tool as recently serviced was hard to shake and that stopping for a full tool change felt like too large a move to make from one sensor reading, even a striking one.",
      "effect_on_reasoning_or_decision": "He chose a small offset adjustment and continued running rather than halting for a tool change. The offset did not hold, and subsequent data showed continued drift toward the lower spec limit and rising tool wear.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment.",
          "evidence_explanation": "This explicitly identifies a prior anchor and the difficulty adjusting away from it when the wear sensor data arrived."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one.",
          "evidence_explanation": "This shows the sensor reading was acknowledged as striking but still insufficiently weighted relative to the anchored belief that the tool was recently serviced."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered halting for a tool change outright, and I considered just running it out unchanged since the tool was 'recently serviced.' The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet.",
          "evidence_explanation": "The participant framed the tool as 'recently serviced' and selected a partial adjustment rather than the more diagnostic intervention, consistent with anchoring and insufficient adjustment."
        }
      ],
      "correction_or_counterevidence": "Time pressure, quota concerns, and impending changeover were real constraints, and the participant did take an intermediate control action rather than ignoring the sensor reading. However, his own description shows the prior recently-serviced belief anchored that intermediate response, and the later rapid climb in wear and Cpk loss eventually overcame the anchor.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Rastogi et al. source supports the anchoring-and-adjustment mechanism in decision-making under time constraints.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoring and adjustment. ... participants' likelihood of sufficiently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoring-and-adjustment heuristic is a resource-rational tradeoff between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source describes anchoring-and-adjustment as a heuristic in which people adjust insufficiently from an initial anchor, especially under limited time.",
          "relevance_to_this_occurrence": "The participant remained anchored to the recently-serviced tool assumption and made only a partial offset adjustment despite the 78% wear sensor data."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": [
        "get-there-itis",
        "continuation bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Tool-wear sensor and impending shift changeover",
      "supporting_interview_quote": "Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in.",
      "plausible_mechanism": "The participant may have continued the current production plan despite incoming evidence of tool wear because the proximity of shift changeover and production goals made stopping increasingly aversive, which resembles plan continuation bias.",
      "why_not_identified": "The behavior is substantially confounded by legitimate time and production constraints, and the participant still took an intermediate control action and increased monitoring. A distinct plan-continuation distortion is therefore not sufficiently separable from resource-rational decision-making under schedule pressure."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a retrospective self-report, so some reasoning may be reconstructed rather than concurrent.",
    "Retrieved corpus passages are limited and partially OCR-degraded, so corpus metadata and quotations may be incomplete.",
    "Findings are based on a single interview and are not necessarily representative of the participant's typical decision-making."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on a process event from your shift — I'll ask you to walk me through what happened and how you made a few of the calls along the way. Nothing here goes into your personnel file, it's for improving our SPC response process. Sound okay? Participant: Sure, no problem. Happy to walk through it. Interviewer: Great. Can you start by telling me what your role was that day and what first drew your attention to the control chart? Participant: I'm the QA analyst covering statistical process control for the turning cell that makes the automotive shafts. I was watching the Xbar-R chart for outer diameter like normal, two subgroups an hour from the automated gauge. I noticed three subgroup means in a row creeping downward, and the most recent one landed in the warning zone — inside two sigma, not over the LCL yet. Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average. Interviewer: What was going through your mind at that point? Participant: Honestly, at 62% through the shift's quota, my first instinct was not to panic. A single warning-zone point isn't automatically an assignable cause under the Western Electric rules — you need a pattern. But three downward-trending points is a pattern worth respecting. Nothing had been logged yet, no maintenance, no material change, so I didn't have an obvious explanation. Interviewer: Walk me through what happened next, chronologically. Participant: I tightened up sampling instead of pulling the trigger on a full stop. I figured if it was real, the next subgroup would confirm it, and if it was noise, extra samples would show it settling back down. Sure enough, the next subgroup crossed the LCL outright. I did a manual spot check with a hand micrometer to rule out a gauge artifact, and it matched the automated reading, so I knew it was real. Interviewer: At that first decision point, what alternatives did you weigh, and why did you choose to increase sampling rather than halt immediately? Participant: I could have shut it down right there, or just logged it and kept going. Stopping the line on one warning-zone point felt premature — that costs us 45 minutes of changeover time we might not need, and we're still trying to hit quota. Ignoring it felt reckless given the trend. Increasing sampling was the middle path — get more data fast without committing to downtime. Interviewer: Once you confirmed the out-of-control signal, what did you look at to figure out the cause? Participant: I pulled up everything I had access to in real time. The shop floor temperature log showed about a three-degree rise over the same two-hour window as the drift. The material lot traveler — which lags real time by about an hour — showed a new lot had been loaded roughly ninety minutes before the drift started. I hadn't checked the tool wear sensor yet at that point. I also asked our process engineer if he'd seen anything like this before, and he said no, actually — this was the first time he'd seen a pattern like this line up with a temperature swing on this particular machine. Interviewer: Given the engineer didn't have a precedent for you, what made you still lean toward temperature as the explanation? Participant: The timing just lined up so cleanly on its own — the temperature started climbing and almost immediately the dimension started walking. I didn't have history to lean on this time, but the correlation itself felt tight enough to run with. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and the temperature story felt like it explained things well enough that I didn't prioritize that test at the time. Interviewer: Did you do anything to directly check the lot hypothesis before moving forward? Participant: Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption. Interviewer: Let's move to the next stretch of the shift. What came in after that? Participant: The tool wear sensor data finally came through. It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine. Interviewer: How did that sensor reading change your thinking about the tool? Participant: It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment. I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one. Interviewer: So what did you decide to do? Participant: I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away. Interviewer: Looking back, what alternatives did you consider there, and why didn't the offset feel like enough given what the sensor showed? Participant: I considered halting for a tool change outright, and I considered just running it out unchanged since the tool was 'recently serviced.' The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet. Interviewer: What happened after that adjustment? Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding. Then shift changeover happened, and the incoming night operator mentioned the tool had sounded different in the last hour — a cue I obviously didn't have access to until after the handoff. Interviewer: Bring me to the end of the shift. What did the final data show, and what did you decide? Participant: By the end, several parts were near or slightly under the lower spec limit. The wear sensor was up to 91%. Cpk for the last two hours had dropped from 1.42 to 1.05, which is a real capability hit. At that point I recommended an immediate tool change, a temporary update to the control chart center line, and I filed a deviation report covering the affected parts. Interviewer: What tipped you fully toward that recommendation? Participant: The Cpk drop was the clincher, honestly, combined with the wear number climbing another thirteen points in a short window. That's not marginal anymore, that's a tool that's clearly done. And with parts sitting near spec limits, a deviation report was required regardless of what I concluded about the cause. Interviewer: What happened after the tool change? Participant: It resolved it. The next shift's dimensions went right back to the historical baseline. And when the lab result on that new material lot finally came back, the hardness was within spec after all — so that wasn't a factor. Interviewer: If the engineer had told you this machine had a history of temperature-linked drift, do you think you would have felt any more confident in the temperature explanation than you already did? Participant: Maybe a little more confident, but honestly the timing alone did most of the convincing for me. Having a precedent would have made it feel more settled, but I don't think it would have changed what I actually did — I was already comfortable running with it based on how closely the two things tracked. Interviewer: And if the lot hardness test had come back out of spec instead? Participant: Then I'd have had two live explanations instead of one, and I probably would have had to test them against each other more directly instead of settling on temperature early. Interviewer: Looking back, is there anything about how you weighed the temperature information against the lot information that you'd do differently, especially without a precedent to lean on? Participant: In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote. Not having the engineer's backup actually should have made me want more direct evidence, not less, but in the moment the timing was persuasive enough on its own. Interviewer: How much did the approaching shift changeover and time pressure shape your decisions overall? Participant: Quite a bit, especially at the tool wear point. Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in. Interviewer: That's really helpful, thank you for walking through all of that in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.17s · gen 103.96s · total 108.6s_

**Retrieved** (ranked by store ranker):
1. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0273 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
2. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0261 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0260 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0257 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0252 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0241 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0240 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0236 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Hallihan_etal_DTM_12.pdf** — 0.0233 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
10. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0224 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0220 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0217 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0208 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0208 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0205 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
17. **Lyell Automation bias and verification complexity.pdf** — 0.0200 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0179 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
22. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0176 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
25. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0166 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
26. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0166 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
28. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
29. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0162 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0158 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
32. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
33. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0156 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
36. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0149 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
39. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0147 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration more often than th_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0147 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0145 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
46. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0144 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
47. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0143 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
48. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0143 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
49. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0141 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis covers the participant's reported statistical process control reasoning and decisions across three episodes: early causal attribution of the diameter drift, evidence seeking for competing cause hypotheses, and response to tool-wear sensor information."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "illusory correlation",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "illusory correlation",
      "alternative_labels": [
        "false cause",
        "post hoc ergo propter hoc",
        "illusory covariation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The perception of a causal relationship between events or variables based primarily on their co-occurrence or temporal sequence, without sufficient evidence of a true association.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Causal attribution of the diameter drift to temperature increase",
      "decision_point_description": "Participant adopted temperature as the working cause before directly testing the material-lot alternative.",
      "affected_reasoning_operation": "causal attribution",
      "bias_specific_mechanism": "Treating temporal contiguity or correlated movement as sufficiently diagnostic of a causal link; the participant used the co-occurrence of a shop-floor temperature rise and a dimension drift to infer that temperature was the cause, even without precedent or direct testing.",
      "manifestation_in_interview": "The participant stated that the timing correlation was persuasive on its own and that the timing, rather than precedent, did most of the convincing.",
      "effect_on_reasoning_or_decision": "The inference made temperature the working explanation, so the material-lot hypothesis was not directly tested and tool wear was not prioritized until later.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The timing just lined up so cleanly on its own — the temperature started climbing and almost immediately the dimension started walking. I didn't have history to lean on this time, but the correlation itself felt tight enough to run with.",
          "evidence_explanation": "This directly shows the participant treating the temporal relationship between temperature rise and dimension drift as sufficient to infer a causal explanation, despite lacking history or direct experimental evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Maybe a little more confident, but honestly the timing alone did most of the convincing for me.",
          "evidence_explanation": "The participant explicitly says the timing/correlation, rather than additional diagnostic evidence, was the main persuasive factor in the causal judgment."
        }
      ],
      "correction_or_counterevidence": "The participant did identify the material lot as a secondary possibility and later acknowledged that a direct hardness test would have closed off one hypothesis. The final lab result showed lot hardness was within spec. Temporal correlation is also a legitimate initial cue in process troubleshooting, and resource constraints favored triage.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage provided support for illusory correlation; the label was applied from general cognitive-science knowledge because retrieved support was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "hypothesis-confirming bias",
        "positive test strategy"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, favor, and prioritize information that confirms an existing hypothesis or belief while underweighting or failing to test alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Choosing what cause to pursue after temperature and material-lot hypotheses emerged",
      "decision_point_description": "Participant chose to continue monitoring under the temperature assumption without directly testing the material-lot alternative.",
      "affected_reasoning_operation": "evidence seeking and hypothesis testing",
      "bias_specific_mechanism": "Selective prioritization of evidence consistent with the favored temperature hypothesis: the participant documented the temperature correlation and monitored under that assumption while deferring a low-cost opportunity to test the material-lot alternative.",
      "manifestation_in_interview": "The participant described the temperature story as feeling like it explained things well enough and did not prioritize the lot hardness test at the time; he logged the lot as secondary but continued under the temperature assumption.",
      "effect_on_reasoning_or_decision": "Reduced willingness to directly test a live alternative hypothesis, delayed the hardness sample, and allowed the temperature explanation to remain the working cause without direct support.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.",
          "evidence_explanation": "This shows the participant favoring the hypothesis-consistent temperature explanation while not testing the alternative lot hypothesis, which is selective evidence prioritization consistent with confirmation bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption.",
          "evidence_explanation": "The participant explicitly describes continuing under the preferred hypothesis while leaving the alternative as an unexamined secondary possibility."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote.",
          "evidence_explanation": "This retrospective statement supports the occurrence by showing the participant now recognizes that a cheap disconfirming test was available and was not used."
        }
      ],
      "correction_or_counterevidence": "The participant did identify the material lot as a secondary possibility and did not completely dismiss it. He was also operating under time constraints and did eventually recommend a deviation report and tool change after stronger evidence emerged.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and mechanism supported by the retrieved Cook and Smallman passage on confirmation bias in selecting and prioritizing evidence during hypothesis analysis.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": "Cook and Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at as-sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias as a strong and pervasive bias in selecting and prioritizing evidence during hypothesis analysis.",
          "relevance_to_this_occurrence": "The participant's decision to prioritize temperature-correlation evidence while deferring testing of the material lot is an example of biased evidence selection and prioritization consistent with this source."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value or belief and to adjust insufficiently from that anchor when new evidence becomes available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting tool-wear sensor and responding to continuing drift",
      "decision_point_description": "After seeing the tool-wear sensor at 78%, participant chose a small offset adjustment rather than an immediate tool change.",
      "affected_reasoning_operation": "belief updating and operational risk decision",
      "bias_specific_mechanism": "Anchoring to the initial belief that the tool was recently serviced and should not be a major factor; the participant under-adjusted from that anchor when the 78% wear sensor arrived, treating the contradictory reading as insufficient to warrant immediate tool change.",
      "manifestation_in_interview": "The participant described the initial mental model as hard to shake and chose a middle-ground offset rather than fully updating to the possibility that the tool was the cause.",
      "effect_on_reasoning_or_decision": "Delayed the tool change; subsequent drift continued and process capability degraded until the participant recommended immediate tool change at shift end.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was.",
          "evidence_explanation": "This establishes the initial anchor: the tool was recently serviced and therefore should not be worn."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment.",
          "evidence_explanation": "This directly describes anchoring to the prior belief and difficulty updating from it when contrary sensor evidence appeared."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet.",
          "evidence_explanation": "This shows insufficient adjustment from the prior belief: the participant partially responded to the new information but did not fully update to the tool-wear explanation."
        }
      ],
      "correction_or_counterevidence": "The participant did not completely ignore the sensor; he made an offset and planned to monitor closely. Time pressure and imminent changeover also contributed to avoiding a full stop. At shift end, after Cpk dropped and wear increased, he recommended immediate tool change, showing eventual full updating.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and anchoring-and-adjustment mechanism supported by the retrieved Rastogi et al. passage on anchoring-and-adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Anchoring-and-adjustment heuristic: people adjust insufficiently away from an initial anchor, with adjustment influenced by available time and resources.",
          "relevance_to_this_occurrence": "The participant anchored to the initial 'recently serviced' tool belief and under-adjusted after receiving the 78% wear sensor. The source's emphasis on anchoring and limited adjustment, especially under time constraints, fits this reasoning pattern."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective self-report interview and cannot directly observe the participant's real-time cognitive processing.",
    "Some decisions were also shaped by legitimate time pressure, production-quota concerns, and incomplete information, which are not themselves biases.",
    "The retrieved corpus passages are sparse and contain OCR noise; support for illusions of causality was not available in the retrieved set.",
    "The findings are probabilistic classifications of reasoning patterns, not proof of counterfactual error causation.",
    "The participant's later self-corrective actions may understate the lasting effect of the identified biases."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on a process event from your shift — I'll ask you to walk me through what happened and how you made a few of the calls along the way. Nothing here goes into your personnel file, it's for improving our SPC response process. Sound okay? Participant: Sure, no problem. Happy to walk through it. Interviewer: Great. Can you start by telling me what your role was that day and what first drew your attention to the control chart? Participant: I'm the QA analyst covering statistical process control for the turning cell that makes the automotive shafts. I was watching the Xbar-R chart for outer diameter like normal, two subgroups an hour from the automated gauge. I noticed three subgroup means in a row creeping downward, and the most recent one landed in the warning zone — inside two sigma, not over the LCL yet. Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average. Interviewer: What was going through your mind at that point? Participant: Honestly, at 62% through the shift's quota, my first instinct was not to panic. A single warning-zone point isn't automatically an assignable cause under the Western Electric rules — you need a pattern. But three downward-trending points is a pattern worth respecting. Nothing had been logged yet, no maintenance, no material change, so I didn't have an obvious explanation. Interviewer: Walk me through what happened next, chronologically. Participant: I tightened up sampling instead of pulling the trigger on a full stop. I figured if it was real, the next subgroup would confirm it, and if it was noise, extra samples would show it settling back down. Sure enough, the next subgroup crossed the LCL outright. I did a manual spot check with a hand micrometer to rule out a gauge artifact, and it matched the automated reading, so I knew it was real. Interviewer: At that first decision point, what alternatives did you weigh, and why did you choose to increase sampling rather than halt immediately? Participant: I could have shut it down right there, or just logged it and kept going. Stopping the line on one warning-zone point felt premature — that costs us 45 minutes of changeover time we might not need, and we're still trying to hit quota. Ignoring it felt reckless given the trend. Increasing sampling was the middle path — get more data fast without committing to downtime. Interviewer: Once you confirmed the out-of-control signal, what did you look at to figure out the cause? Participant: I pulled up everything I had access to in real time. The shop floor temperature log showed about a three-degree rise over the same two-hour window as the drift. The material lot traveler — which lags real time by about an hour — showed a new lot had been loaded roughly ninety minutes before the drift started. I hadn't checked the tool wear sensor yet at that point. I also asked our process engineer if he'd seen anything like this before, and he said no, actually — this was the first time he'd seen a pattern like this line up with a temperature swing on this particular machine. Interviewer: Given the engineer didn't have a precedent for you, what made you still lean toward temperature as the explanation? Participant: The timing just lined up so cleanly on its own — the temperature started climbing and almost immediately the dimension started walking. I didn't have history to lean on this time, but the correlation itself felt tight enough to run with. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and the temperature story felt like it explained things well enough that I didn't prioritize that test at the time. Interviewer: Did you do anything to directly check the lot hypothesis before moving forward? Participant: Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption. Interviewer: Let's move to the next stretch of the shift. What came in after that? Participant: The tool wear sensor data finally came through. It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine. Interviewer: How did that sensor reading change your thinking about the tool? Participant: It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment. I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one. Interviewer: So what did you decide to do? Participant: I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away. Interviewer: Looking back, what alternatives did you consider there, and why didn't the offset feel like enough given what the sensor showed? Participant: I considered halting for a tool change outright, and I considered just running it out unchanged since the tool was 'recently serviced.' The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet. Interviewer: What happened after that adjustment? Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding. Then shift changeover happened, and the incoming night operator mentioned the tool had sounded different in the last hour — a cue I obviously didn't have access to until after the handoff. Interviewer: Bring me to the end of the shift. What did the final data show, and what did you decide? Participant: By the end, several parts were near or slightly under the lower spec limit. The wear sensor was up to 91%. Cpk for the last two hours had dropped from 1.42 to 1.05, which is a real capability hit. At that point I recommended an immediate tool change, a temporary update to the control chart center line, and I filed a deviation report covering the affected parts. Interviewer: What tipped you fully toward that recommendation? Participant: The Cpk drop was the clincher, honestly, combined with the wear number climbing another thirteen points in a short window. That's not marginal anymore, that's a tool that's clearly done. And with parts sitting near spec limits, a deviation report was required regardless of what I concluded about the cause. Interviewer: What happened after the tool change? Participant: It resolved it. The next shift's dimensions went right back to the historical baseline. And when the lab result on that new material lot finally came back, the hardness was within spec after all — so that wasn't a factor. Interviewer: If the engineer had told you this machine had a history of temperature-linked drift, do you think you would have felt any more confident in the temperature explanation than you already did? Participant: Maybe a little more confident, but honestly the timing alone did most of the convincing for me. Having a precedent would have made it feel more settled, but I don't think it would have changed what I actually did — I was already comfortable running with it based on how closely the two things tracked. Interviewer: And if the lot hardness test had come back out of spec instead? Participant: Then I'd have had two live explanations instead of one, and I probably would have had to test them against each other more directly instead of settling on temperature early. Interviewer: Looking back, is there anything about how you weighed the temperature information against the lot information that you'd do differently, especially without a precedent to lean on? Participant: In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote. Not having the engineer's backup actually should have made me want more direct evidence, not less, but in the moment the timing was persuasive enough on its own. Interviewer: How much did the approaching shift changeover and time pressure shape your decisions overall? Participant: Quite a bit, especially at the tool wear point. Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in. Interviewer: That's really helpful, thank you for walking through all of that in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.99s · gen 98.83s · total 103.3s_

**Retrieved** (ranked by store ranker):
1. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0273 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
2. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0261 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0260 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0257 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0252 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0241 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0240 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0236 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Hallihan_etal_DTM_12.pdf** — 0.0233 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
10. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0224 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0220 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0217 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0208 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0208 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0205 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
17. **Lyell Automation bias and verification complexity.pdf** — 0.0200 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0179 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
22. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0176 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
25. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0166 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
26. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0166 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
28. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
29. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0162 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0158 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
32. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
33. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0156 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
36. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0149 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
39. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0147 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration more often than th_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0147 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0145 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
46. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0144 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
47. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0143 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
48. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0143 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
49. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0141 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first analysis; structural constraints such as time pressure, lab delay, and SPC rules are treated as context rather than bias unless a separate bias-specific mechanism is affirmatively evidenced."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Selective hypothesis testing"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or hypotheses while giving disproportionately less consideration to alternative possibilities.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial causal attribution after out-of-control signal",
      "decision_point_description": "After the out-of-control signal, selecting temperature as the primary cause and deferring the material-lot hardness test, despite no historical precedent and an alternative lot hypothesis with similar timing.",
      "affected_reasoning_operation": "Causal hypothesis generation and testing / information search",
      "bias_specific_mechanism": "Once the participant formed a temperature hypothesis from a salient temporal correlation, he treated that hypothesis as sufficient and directed attention toward documenting the temperature correlation, while leaving the competing material-lot hypothesis as an unexamined secondary possibility. He explicitly did not prioritize direct testing of the lot hypothesis even though doing so could have closed off an alternative cause.",
      "manifestation_in_interview": "The participant reported that the temporal correlation between temperature rise and dimensional drift 'felt tight enough to run with' and that he did not prioritize a hardness sample because the temperature explanation felt sufficient. He logged the material lot as a secondary possibility but continued monitoring under the temperature assumption.",
      "effect_on_reasoning_or_decision": "The participant committed to the temperature explanation and delayed direct testing of the material-lot hypothesis. The later lab result showed the lot hardness was within spec, meaning the untested alternative was not the cause, and the actual tool-wear cause was not pursued as early as it might otherwise have been.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The timing just lined up so cleanly on its own — the temperature started climbing and almost immediately the dimension started walking. I didn't have history to lean on this time, but the correlation itself felt tight enough to run with.",
          "evidence_explanation": "Shows acceptance of a causal explanation based on temporal correlation without historical precedent, illustrating early commitment to the temperature hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.",
          "evidence_explanation": "Directly demonstrates that the favored temperature hypothesis was treated as sufficient and that the competing lot hypothesis was not directly tested."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption.",
          "evidence_explanation": "Shows selective attention to the favored hypothesis while the alternative remained an unexamined footnote."
        }
      ],
      "correction_or_counterevidence": "The participant did log the material lot as a secondary possibility and asked the process engineer whether the pattern had a precedent. He also stated in hindsight that he could have pulled the lot sample earlier. These are reflective or partial safeguards rather than contemporaneous correction, and the earlier reasoning was still materially shaped by the untreated temperature hypothesis.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support provides a conceptual description of confirmation bias in processing sampled information; it is used only to support classification, not as evidence that the bias occurred.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "an explanation in terms of confirmation bias in processing the sampled information",
          "mechanism_supported_by_source": "The source describes confirmation bias as a processing tendency affecting how sampled information is handled, consistent with selective processing of the temperature hypothesis while the lot hypothesis remained untested.",
          "relevance_to_this_occurrence": "This supports the conceptual classification of the participant's selective information search and processing as confirmation bias; it does not establish that the bias occurred in this interview."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment", "Insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information or prior belief when making subsequent judgments, with insufficient adjustment away from that anchor in light of new evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Tool wear sensor interpretation and offset adjustment",
      "decision_point_description": "After receiving the tool wear sensor reading at 78% of rated life and learning that the drift direction was a classic tool wear signature, deciding whether to change the tool immediately or make a small offset adjustment and continue running.",
      "affected_reasoning_operation": "Diagnostic inference and corrective action selection",
      "bias_specific_mechanism": "The participant anchored on the prior mental model that the insert was essentially new because it had been swapped two days earlier. When the wear sensor showed 78% of rated life and the drift direction matched a classic tool wear signature, he adjusted only partially, making an offset adjustment rather than fully revising the prior belief and stopping for a tool change. He explicitly described the prior model as difficult to shake in the moment.",
      "manifestation_in_interview": "The participant reported surprise at the 78% reading because he had been thinking of the tool as basically new, stated that the prior mental model was hard to fully shake, and chose a middle-ground offset adjustment rather than an immediate tool change despite calling the sensor reading striking and the drift direction a classic tool wear signature.",
      "effect_on_reasoning_or_decision": "The participant made only an offset adjustment instead of replacing the tool. The drift continued, the wear sensor later climbed to 91%, Cpk dropped from 1.42 to 1.05, and the eventual tool change resolved the problem, indicating that the adjustment away from the initial anchor was insufficient.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine.",
          "evidence_explanation": "Demonstrates that new evidence conflicted with the participant's prior anchor that the tool was recently serviced and unlikely to be the cause."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment.",
          "evidence_explanation": "Explicitly describes anchoring on the prior mental model even though new evidence was recognized as important."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away.",
          "evidence_explanation": "Shows insufficient adjustment away from the anchor: the participant took a limited action rather than the stronger action implied by the sensor evidence."
        }
      ],
      "correction_or_counterevidence": "The participant did not entirely dismiss the sensor reading and described the offset as a middle-ground action. There was also real time pressure and proximity to shift changeover. His later recommendation for an immediate tool change after further evidence, including the 91% wear reading and Cpk drop, shows eventual correction once additional evidence became overwhelming.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Rastogi et al. (2022) conceptually grounds the anchoring-and-adjustment heuristic; it is used only to support classification, not as evidence that the bias occurred.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source treats anchoring-and-adjustment as a heuristic involving insufficient adjustment away from an initial anchor, with resource and time tradeoffs, consistent with the participant's partial adjustment from the recently-serviced-tool anchor.",
          "relevance_to_this_occurrence": "This supports the conceptual classification of the participant's insufficient adjustment from a prior anchor when new tool-wear evidence appeared; it does not establish that the bias occurred in this interview."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages are sparse and OCR-noisy; support is used at a conceptual level rather than as direct evidence that a bias occurred.",
    "The analysis relies on participant self-report in a debrief interview; contemporaneous behavior was not directly observed.",
    "Some decisions occurred under genuine time and production pressure, which is treated as contextual and competing explanation where relevant."
  ]
}

