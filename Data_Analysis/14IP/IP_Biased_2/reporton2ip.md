# RAG Benchmark — 2026-09-13

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on a process event from your shift — I'll ask you to walk me through what happened and how you made a few of the calls along the way. Nothing here goes into your personnel file, it's for improving our SPC response process. Sound okay? Participant: Sure, no problem. Happy to walk through it. Interviewer: Great. Can you start by telling me what your role was that day and what first drew your attention to the control chart? Participant: I'm the QA analyst covering statistical process control for the turning cell that makes the automotive shafts. I was watching the Xbar-R chart for outer diameter like normal, two subgroups an hour from the automated gauge. I noticed three subgroup means in a row creeping downward, and the most recent one landed in the warning zone — inside two sigma, not over the LCL yet. Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average. Interviewer: What was going through your mind at that point? Participant: Honestly, at 62% through the shift's quota, my first instinct was not to panic. A single warning-zone point isn't automatically an assignable cause under the Western Electric rules — you need a pattern. But three downward-trending points is a pattern worth respecting. Nothing had been logged yet, no maintenance, no material change, so I didn't have an obvious explanation. Interviewer: Walk me through what happened next, chronologically. Participant: I tightened up sampling instead of pulling the trigger on a full stop. I figured if it was real, the next subgroup would confirm it, and if it was noise, extra samples would show it settling back down. Sure enough, the next subgroup crossed the LCL outright. I did a manual spot check with a hand micrometer to rule out a gauge artifact, and it matched the automated reading, so I knew it was real. Interviewer: At that first decision point, what alternatives did you weigh, and why did you choose to increase sampling rather than halt immediately? Participant: I could have shut it down right there, or just logged it and kept going. Stopping the line on one warning-zone point felt premature — that costs us 45 minutes of changeover time we might not need, and we're still trying to hit quota. Ignoring it felt reckless given the trend. Increasing sampling was the middle path — get more data fast without committing to downtime. Interviewer: Once you confirmed the out-of-control signal, what did you look at to figure out the cause? Participant: I pulled up everything I had access to in real time. The shop floor temperature log showed about a three-degree rise over the same two-hour window as the drift. The material lot traveler — which lags real time by about an hour — showed a new lot had been loaded roughly ninety minutes before the drift started. I hadn't checked the tool wear sensor yet at that point. I also mentioned to our process engineer what I was seeing, and he said temperature swings had caused drift on that machine before. Interviewer: Given both the temperature rise and the new lot were roughly time-aligned with the drift, what made you lean toward temperature as the explanation? Participant: The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking. And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and honestly the temperature story felt like it explained things well enough that I didn't prioritize that test at the time. Interviewer: Did you do anything to directly check the lot hypothesis before moving forward? Participant: Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption. Interviewer: Let's move to the next stretch of the shift. What came in after that? Participant: The tool wear sensor data finally came through. It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine. Interviewer: How did that sensor reading change your thinking about the tool? Participant: It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment. I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one. Interviewer: So what did you decide to do? Participant: I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away. Interviewer: Looking back, what alternatives did you consider there, and why didn't the offset feel like enough given what the sensor showed? Participant: I considered halting for a tool change outright, and I considered just running it out unchanged since the tool was 'recently serviced.' The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet. Interviewer: What happened after that adjustment? Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding. Then shift changeover happened, and the incoming night operator mentioned the tool had sounded different in the last hour — a cue I obviously didn't have access to until after the handoff. Interviewer: Bring me to the end of the shift. What did the final data show, and what did you decide? Participant: By the end, several parts were near or slightly under the lower spec limit. The wear sensor was up to 91%. Cpk for the last two hours had dropped from 1.42 to 1.05, which is a real capability hit. At that point I recommended an immediate tool change, a temporary update to the control chart center line, and I filed a deviation report covering the affected parts. Interviewer: What tipped you fully toward that recommendation? Participant: The Cpk drop was the clincher, honestly, combined with the wear number climbing another thirteen points in a short window. That's not marginal anymore, that's a tool that's clearly done. And with parts sitting near spec limits, a deviation report was required regardless of what I concluded about the cause. Interviewer: What happened after the tool change? Participant: It resolved it. The next shift's dimensions went right back to the historical baseline. And when the lab result on that new material lot finally came back, the hardness was within spec after all — so that wasn't a factor. Interviewer: If the tool wear data had been available an hour earlier, do you think it would have changed your call at the offset-adjustment point? Participant: Possibly. If I'd seen 78% that much earlier with more of the shift left, I might have leaned toward the tool change sooner rather than the offset. The compressed time at the end made a bigger intervention feel less appealing. Interviewer: And if the lot hardness test had come back out of spec instead? Participant: Then I'd have had two live explanations instead of one, and I probably would have had to test them against each other more directly instead of settling on temperature early. Interviewer: Anything you'd do differently in how you weighed the temperature information against the lot information? Participant: In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote. Interviewer: Last one — how much did the approaching shift changeover and time pressure shape your decisions overall? Participant: Quite a bit, especially at the tool wear point. Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in. Interviewer: That's really helpful, thank you for walking through all of that in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.14s · gen 93.73s · total 98.5s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0278 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0274 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0272 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0266 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
5. **Hallihan_etal_DTM_12.pdf** — 0.0258 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0250 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0250 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0235 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0235 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0226 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0213 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0211 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0209 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0207 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
15. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0206 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
17. **Lyell Automation bias and verification complexity.pdf** — 0.0200 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0186 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0186 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0184 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
21. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0183 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
23. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0179 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
24. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0177 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
27. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0164 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
30. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0162 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0150 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0150 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration more often than th_
39. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0148 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
42. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0148 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
43. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0147 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
44. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0143 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
45. **Pinto (2023). Methodological and Cognitive biases in Science issues for current research and ways to counteract them.pdf** — 0.0142 (rrf) — _Test (IAT). The conclusion of the study states: argumentqualitytoin extent of message processing_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0137 (rrf) — _## Evolut ionary Cognitive Psychology | mals in Pleistocene caves, for instance, demonstrate one_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0137 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0136 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "The evaluation considered only the participant's reported reasoning and decisions during the process event, using the retrieved corpus for terminology and mechanism validation."
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
      "confidence": "low",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "hypothesis-confirmation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, favor, and prioritize information that supports an existing hypothesis while under-weighting, avoiding, or failing to directly test plausible alternative hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Cause attribution after out-of-control signal",
      "decision_point_description": "Choosing whether to directly test the new material lot versus proceeding with temperature as the working explanation.",
      "affected_reasoning_operation": "Causal attribution and hypothesis testing / evidence prioritization",
      "bias_specific_mechanism": "After identifying two time-aligned possible causes, temperature rise and a new material lot, the participant selected the temperature hypothesis based on temporal correlation and an engineer's prior-experience comment. He logged the lot hypothesis as a secondary possibility but did not directly test or seek disconfirming evidence for it, describing the temperature story as sufficiently explanatory. This reflects selective prioritization of a favored hypothesis and premature closure rather than active disconfirmation.",
      "manifestation_in_interview": "The participant reported that the timing of the temperature rise 'lined up so cleanly' and that the engineer's comment reinforced the temperature explanation, while explicitly not prioritizing a lab test of the new lot because the temperature story 'felt like it explained things well enough.'",
      "effect_on_reasoning_or_decision": "The participant did not collect a hardness sample or otherwise directly test the new material lot at that point. He continued monitoring and documenting under the temperature assumption, leaving the alternative hypothesis unexamined until later evidence showed the lot was in-spec and tool wear was the actual cause.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking. And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and honestly the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.",
          "evidence_explanation": "This quote shows favoritism toward the temperature hypothesis and the explicit decision not to test the alternative, despite the alternative being known. The phrase 'felt like it explained things well enough' indicates premature closure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption.",
          "evidence_explanation": "Confirms that the lot hypothesis was not directly checked and remained secondary while the participant focused on documentation supporting the temperature correlation."
        }
      ],
      "correction_or_counterevidence": "There were legitimate operational considerations: a lot hardness sample required lab time, and the temperature hypothesis was supported by temporal correlation and an engineer's prior experience with the same machine. The participant later acknowledged the sample 'wouldn't have cost much time' and could have closed off the alternative, which weakens the resource explanation. The eventual in-spec lab result does not retroactively impute bias but does show the untested alternative was non-causal.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages describe confirmation bias in evidence selection, prioritization, and hypothesis testing; they support the label but do not describe this specific industrial QA episode.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human Factors of the Confirmation Bias in Intelligence Analysis: Decision Support from Graphical Evidence",
          "authors": "Cook & Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at as-sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias can operate by selecting and prioritizing evidence in a way that supports an existing investigative hypothesis.",
          "relevance_to_this_occurrence": "The participant prioritized evidence and documentation supporting the temperature hypothesis and did not directly test the lot alternative, consistent with confirmatory evidence prioritization."
        },
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "discounting of contradictory information. In  addition, an explanation in terms of confirmation bias in processing the sampled information  or difficulties of comprehension is also unlikely,  given that the participants were very well  trained and that the system parameter always  contradicted the aid’s diagnosis in an unequivocal way.",
          "mechanism_supported_by_source": "Confirmation bias can involve discounting contradictory information or processing information in a hypothesis-consistent manner.",
          "relevance_to_this_occurrence": "The participant did not actively sample or test the contradictory lot hypothesis, leaving it as a footnote while pursuing the favored temperature explanation."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial reference point or belief and to make insufficient adjustments away from that anchor when new evidence arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to tool wear sensor data",
      "decision_point_description": "Deciding whether to stop for a tool change or make a smaller offset adjustment after seeing 78% cumulative cutting distance.",
      "affected_reasoning_operation": "Belief updating and diagnostic inference from new evidence",
      "bias_specific_mechanism": "The participant anchored on the initial representation of the cutting tool as 'basically new' because it had been swapped two days earlier. When the sensor showed 78% of rated tool life and a classic tool wear signature, he acknowledged the new data but made only incremental mental adjustment, interpreting the reading as not yet sufficient to justify a full tool change and choosing a small offset adjustment instead.",
      "manifestation_in_interview": "The participant explicitly stated that his prior mental model of the tool as recently serviced was 'a hard thing to fully shake in the moment.' He then chose a small in-process offset adjustment rather than pulling the tool, despite the sensor reading and the classic wear signature.",
      "effect_on_reasoning_or_decision": "The initial belief about the tool's recent service led the participant to under-react to objective wear data, delaying the tool change until further drift and Cpk degradation made the evidence overwhelming.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine.",
          "evidence_explanation": "This establishes the objective data contradicting the initial belief and the participant's acknowledgment that the initial anchor, 'basically new,' shaped his expectation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment.",
          "evidence_explanation": "This is direct testimony that the prior belief resisted updating in the face of new evidence, which is the core mechanism of anchoring or insufficient adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away.",
          "evidence_explanation": "The behavioral consequence shows an incremental adjustment rather than full updating to the new wear information, consistent with anchoring."
        }
      ],
      "correction_or_counterevidence": "The choice of an offset adjustment was also influenced by time pressure and proximity to shift changeover, which is a plausible non-bias operational consideration. However, the participant explicitly described the residual prior model as hard to shake, and the sensor evidence objectively contradicted that prior model, supporting a distinct cognitive distortion beyond resource constraints.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passage from Rastogi et al. supports the anchoring-and-adjustment mechanism in a time-pressured decision context.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Insufficient adjustment away from an initial anchor is a resource-rational trade-off; under time pressure, adjustments are often insufficient.",
          "relevance_to_this_occurrence": "The participant exhibited insufficient adjustment away from the initial 'recently serviced tool' anchor under time pressure, choosing a smaller correction rather than a full tool change."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved passages contain extraction artifacts and are used only for terminology and mechanism validation, not as evidence of whether the biases occurred.",
    "Confidence ratings reflect transcript evidence only; low-confidence findings remain valid positive identifications under the task definition.",
    "Production pressure, time constraints, and shift-changeover considerations may partially overlap with or resemble cognitive bias mechanisms, making exact causal separation difficult.",
    "The analysis is limited to the participant's self-reported reasoning and decisions during the interview."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on a process event from your shift — I'll ask you to walk me through what happened and how you made a few of the calls along the way. Nothing here goes into your personnel file, it's for improving our SPC response process. Sound okay? Participant: Sure, no problem. Happy to walk through it. Interviewer: Great. Can you start by telling me what your role was that day and what first drew your attention to the control chart? Participant: I'm the QA analyst covering statistical process control for the turning cell that makes the automotive shafts. I was watching the Xbar-R chart for outer diameter like normal, two subgroups an hour from the automated gauge. I noticed three subgroup means in a row creeping downward, and the most recent one landed in the warning zone — inside two sigma, not over the LCL yet. Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average. Interviewer: What was going through your mind at that point? Participant: Honestly, at 62% through the shift's quota, my first instinct was not to panic. A single warning-zone point isn't automatically an assignable cause under the Western Electric rules — you need a pattern. But three downward-trending points is a pattern worth respecting. Nothing had been logged yet, no maintenance, no material change, so I didn't have an obvious explanation. Interviewer: Walk me through what happened next, chronologically. Participant: I tightened up sampling instead of pulling the trigger on a full stop. I figured if it was real, the next subgroup would confirm it, and if it was noise, extra samples would show it settling back down. Sure enough, the next subgroup crossed the LCL outright. I did a manual spot check with a hand micrometer to rule out a gauge artifact, and it matched the automated reading, so I knew it was real. Interviewer: At that first decision point, what alternatives did you weigh, and why did you choose to increase sampling rather than halt immediately? Participant: I could have shut it down right there, or just logged it and kept going. Stopping the line on one warning-zone point felt premature — that costs us 45 minutes of changeover time we might not need, and we're still trying to hit quota. Ignoring it felt reckless given the trend. Increasing sampling was the middle path — get more data fast without committing to downtime. Interviewer: Once you confirmed the out-of-control signal, what did you look at to figure out the cause? Participant: I pulled up everything I had access to in real time. The shop floor temperature log showed about a three-degree rise over the same two-hour window as the drift. The material lot traveler — which lags real time by about an hour — showed a new lot had been loaded roughly ninety minutes before the drift started. I hadn't checked the tool wear sensor yet at that point. I also mentioned to our process engineer what I was seeing, and he said temperature swings had caused drift on that machine before. Interviewer: Given both the temperature rise and the new lot were roughly time-aligned with the drift, what made you lean toward temperature as the explanation? Participant: The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking. And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and honestly the temperature story felt like it explained things well enough that I didn't prioritize that test at the time. Interviewer: Did you do anything to directly check the lot hypothesis before moving forward? Participant: Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption. Interviewer: Let's move to the next stretch of the shift. What came in after that? Participant: The tool wear sensor data finally came through. It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine. Interviewer: How did that sensor reading change your thinking about the tool? Participant: It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment. I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one. Interviewer: So what did you decide to do? Participant: I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away. Interviewer: Looking back, what alternatives did you consider there, and why didn't the offset feel like enough given what the sensor showed? Participant: I considered halting for a tool change outright, and I considered just running it out unchanged since the tool was 'recently serviced.' The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet. Interviewer: What happened after that adjustment? Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding. Then shift changeover happened, and the incoming night operator mentioned the tool had sounded different in the last hour — a cue I obviously didn't have access to until after the handoff. Interviewer: Bring me to the end of the shift. What did the final data show, and what did you decide? Participant: By the end, several parts were near or slightly under the lower spec limit. The wear sensor was up to 91%. Cpk for the last two hours had dropped from 1.42 to 1.05, which is a real capability hit. At that point I recommended an immediate tool change, a temporary update to the control chart center line, and I filed a deviation report covering the affected parts. Interviewer: What tipped you fully toward that recommendation? Participant: The Cpk drop was the clincher, honestly, combined with the wear number climbing another thirteen points in a short window. That's not marginal anymore, that's a tool that's clearly done. And with parts sitting near spec limits, a deviation report was required regardless of what I concluded about the cause. Interviewer: What happened after the tool change? Participant: It resolved it. The next shift's dimensions went right back to the historical baseline. And when the lab result on that new material lot finally came back, the hardness was within spec after all — so that wasn't a factor. Interviewer: If the tool wear data had been available an hour earlier, do you think it would have changed your call at the offset-adjustment point? Participant: Possibly. If I'd seen 78% that much earlier with more of the shift left, I might have leaned toward the tool change sooner rather than the offset. The compressed time at the end made a bigger intervention feel less appealing. Interviewer: And if the lot hardness test had come back out of spec instead? Participant: Then I'd have had two live explanations instead of one, and I probably would have had to test them against each other more directly instead of settling on temperature early. Interviewer: Anything you'd do differently in how you weighed the temperature information against the lot information? Participant: In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote. Interviewer: Last one — how much did the approaching shift changeover and time pressure shape your decisions overall? Participant: Quite a bit, especially at the tool wear point. Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in. Interviewer: That's really helpful, thank you for walking through all of that in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.28s · gen 100.83s · total 105.6s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0278 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0274 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0272 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0266 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
5. **Hallihan_etal_DTM_12.pdf** — 0.0258 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0250 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0250 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0235 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0235 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0226 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0213 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0211 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0209 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0207 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
15. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0206 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
17. **Lyell Automation bias and verification complexity.pdf** — 0.0200 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0186 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0186 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0184 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
21. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0183 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
23. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0179 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
24. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0177 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
27. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0164 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
30. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0162 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0150 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0150 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration more often than th_
39. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0148 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
42. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0148 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
43. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0147 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
44. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0143 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
45. **Pinto (2023). Methodological and Cognitive biases in Science issues for current research and ways to counteract them.pdf** — 0.0142 (rrf) — _Test (IAT). The conclusion of the study states: argumentqualitytoin extent of message processing_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0137 (rrf) — _## Evolut ionary Cognitive Psychology | mals in Pleistocene caves, for instance, demonstrate one_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0137 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0136 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed a single process-event debrief interview for cognitive bias mechanisms, using retrieved corpus passages on confirmation bias and anchoring."
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
      "confidence": "low",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Selective information seeking", "Hypothesis confirmation"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to seek, interpret, or prioritize information in ways that support an existing hypothesis or belief while undervaluing alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Causal attribution after out-of-control signal",
      "decision_point_description": "Choosing whether to immediately investigate the material-lot hypothesis or continue under the temperature hypothesis after the control chart confirmed drift.",
      "affected_reasoning_operation": "Hypothesis testing / causal attribution",
      "bias_specific_mechanism": "The participant favored the temperature hypothesis after it produced a coherent story and an engineer's confirming remark; he then documented that story and did not prioritize a direct test of the alternative material-lot hypothesis.",
      "manifestation_in_interview": "The participant described the temperature story as feeling like it explained things well enough, left the material lot as an unexamined footnote, and later acknowledged he could have pulled the lot sample earlier.",
      "effect_on_reasoning_or_decision": "The decision to continue under the temperature assumption delayed testing the material-lot hypothesis; the later lab result showed lot hardness was in spec, meaning tool wear—not temperature or material—was the actual cause.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking. And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine.",
          "evidence_explanation": "Shows that a salient temporal correlation and an engineer's prior-experience statement strengthened the favored temperature hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and honestly the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.",
          "evidence_explanation": "Directly links subjective sufficiency of the favored explanation to withholding a test that could have disconfirmed the alternative material-lot hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption.",
          "evidence_explanation": "Shows selective prioritization of confirmatory evidence while the alternative remained untested."
        }
      ],
      "correction_or_counterevidence": "The participant did record the material lot as a secondary possibility and later acknowledged he could have pulled the sample earlier; practical constraints, including lab turnaround delay, also plausibly influenced the decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and mechanism supported by a retrieved passage on confirmation bias in evidence selection and prioritization.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at assessment but a strong and pervasive confirmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "The source documents a confirmation bias in how people select and prioritize evidence consistent with a favored hypothesis.",
          "relevance_to_this_occurrence": "The participant selected and prioritized temperature-related evidence and did not directly test the alternative material-lot hypothesis, consistent with confirmation-biased evidence prioritization."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment", "Belief perseverance"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to rely too heavily on an initial value or belief and to adjust insufficiently when new evidence arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Tool wear sensor interpretation and intervention choice",
      "decision_point_description": "Deciding whether to stop for a full tool change or make a smaller offset adjustment after receiving 78% tool-wear sensor data.",
      "affected_reasoning_operation": "Interpretation of diagnostic sensor data and treatment decision",
      "bias_specific_mechanism": "The initial mental model that the tool was recently serviced and therefore not a major factor served as an anchor; the participant made only a small offset adjustment despite a striking wear-sensor reading and classic tool-wear signature.",
      "manifestation_in_interview": "The participant explicitly said the recently-serviced-tool mental model was hard to shake and chose a middle-path offset rather than pulling the tool.",
      "effect_on_reasoning_or_decision": "The insufficient adjustment from the prior belief deferred a likely necessary tool change; the offset did not hold, wear increased, and Cpk fell before the shift ended.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The tool wear sensor data finally came through. It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine.",
          "evidence_explanation": "Shows new diagnostic evidence that conflicted with the prior 'recently serviced' model and was initially located as surprising rather than decisive."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment.",
          "evidence_explanation": "Direct statement that the initial mental model exerted continuing influence on interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away.",
          "evidence_explanation": "Demonstrates a small adjustment away from the prior position rather than a decision to address the structurally indicated cause."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the wear reading and considered a full tool change; time pressure and approaching changeover were realistic operational constraints. The later tool change resolved the issue, confirming the sensor was informative.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and mechanism supported by a retrieved passage on the anchoring-and-adjustment heuristic.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source treats anchoring-and-adjustment as a heuristic involving insufficient adjustment from an anchor, particularly under time constraints.",
          "relevance_to_this_occurrence": "The participant remained anchored to the recently serviced tool mental model and made only a small offset adjustment despite new wear data, with time pressure explicitly present."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on retrospective self-report rather than direct observation of internal mental states.",
    "Time pressure, changeover proximity, and normal operational rules may provide non-bias explanations for some decisions.",
    "The interview does not include real-time verification of which evidence the participant actually sampled or prioritized beyond his account."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on a process event from your shift — I'll ask you to walk me through what happened and how you made a few of the calls along the way. Nothing here goes into your personnel file, it's for improving our SPC response process. Sound okay? Participant: Sure, no problem. Happy to walk through it. Interviewer: Great. Can you start by telling me what your role was that day and what first drew your attention to the control chart? Participant: I'm the QA analyst covering statistical process control for the turning cell that makes the automotive shafts. I was watching the Xbar-R chart for outer diameter like normal, two subgroups an hour from the automated gauge. I noticed three subgroup means in a row creeping downward, and the most recent one landed in the warning zone — inside two sigma, not over the LCL yet. Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average. Interviewer: What was going through your mind at that point? Participant: Honestly, at 62% through the shift's quota, my first instinct was not to panic. A single warning-zone point isn't automatically an assignable cause under the Western Electric rules — you need a pattern. But three downward-trending points is a pattern worth respecting. Nothing had been logged yet, no maintenance, no material change, so I didn't have an obvious explanation. Interviewer: Walk me through what happened next, chronologically. Participant: I tightened up sampling instead of pulling the trigger on a full stop. I figured if it was real, the next subgroup would confirm it, and if it was noise, extra samples would show it settling back down. Sure enough, the next subgroup crossed the LCL outright. I did a manual spot check with a hand micrometer to rule out a gauge artifact, and it matched the automated reading, so I knew it was real. Interviewer: At that first decision point, what alternatives did you weigh, and why did you choose to increase sampling rather than halt immediately? Participant: I could have shut it down right there, or just logged it and kept going. Stopping the line on one warning-zone point felt premature — that costs us 45 minutes of changeover time we might not need, and we're still trying to hit quota. Ignoring it felt reckless given the trend. Increasing sampling was the middle path — get more data fast without committing to downtime. Interviewer: Once you confirmed the out-of-control signal, what did you look at to figure out the cause? Participant: I pulled up everything I had access to in real time. The shop floor temperature log showed about a three-degree rise over the same two-hour window as the drift. The material lot traveler — which lags real time by about an hour — showed a new lot had been loaded roughly ninety minutes before the drift started. I hadn't checked the tool wear sensor yet at that point. I also mentioned to our process engineer what I was seeing, and he said temperature swings had caused drift on that machine before. Interviewer: Given both the temperature rise and the new lot were roughly time-aligned with the drift, what made you lean toward temperature as the explanation? Participant: The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking. And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and honestly the temperature story felt like it explained things well enough that I didn't prioritize that test at the time. Interviewer: Did you do anything to directly check the lot hypothesis before moving forward? Participant: Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption. Interviewer: Let's move to the next stretch of the shift. What came in after that? Participant: The tool wear sensor data finally came through. It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine. Interviewer: How did that sensor reading change your thinking about the tool? Participant: It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment. I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one. Interviewer: So what did you decide to do? Participant: I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away. Interviewer: Looking back, what alternatives did you consider there, and why didn't the offset feel like enough given what the sensor showed? Participant: I considered halting for a tool change outright, and I considered just running it out unchanged since the tool was 'recently serviced.' The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet. Interviewer: What happened after that adjustment? Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding. Then shift changeover happened, and the incoming night operator mentioned the tool had sounded different in the last hour — a cue I obviously didn't have access to until after the handoff. Interviewer: Bring me to the end of the shift. What did the final data show, and what did you decide? Participant: By the end, several parts were near or slightly under the lower spec limit. The wear sensor was up to 91%. Cpk for the last two hours had dropped from 1.42 to 1.05, which is a real capability hit. At that point I recommended an immediate tool change, a temporary update to the control chart center line, and I filed a deviation report covering the affected parts. Interviewer: What tipped you fully toward that recommendation? Participant: The Cpk drop was the clincher, honestly, combined with the wear number climbing another thirteen points in a short window. That's not marginal anymore, that's a tool that's clearly done. And with parts sitting near spec limits, a deviation report was required regardless of what I concluded about the cause. Interviewer: What happened after the tool change? Participant: It resolved it. The next shift's dimensions went right back to the historical baseline. And when the lab result on that new material lot finally came back, the hardness was within spec after all — so that wasn't a factor. Interviewer: If the tool wear data had been available an hour earlier, do you think it would have changed your call at the offset-adjustment point? Participant: Possibly. If I'd seen 78% that much earlier with more of the shift left, I might have leaned toward the tool change sooner rather than the offset. The compressed time at the end made a bigger intervention feel less appealing. Interviewer: And if the lot hardness test had come back out of spec instead? Participant: Then I'd have had two live explanations instead of one, and I probably would have had to test them against each other more directly instead of settling on temperature early. Interviewer: Anything you'd do differently in how you weighed the temperature information against the lot information? Participant: In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote. Interviewer: Last one — how much did the approaching shift changeover and time pressure shape your decisions overall? Participant: Quite a bit, especially at the tool wear point. Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in. Interviewer: That's really helpful, thank you for walking through all of that in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.00s · gen 150.15s · total 154.7s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0278 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0274 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0272 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0266 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
5. **Hallihan_etal_DTM_12.pdf** — 0.0258 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0250 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0250 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0235 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0235 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0226 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0213 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0211 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0209 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0207 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
15. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0206 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
17. **Lyell Automation bias and verification complexity.pdf** — 0.0200 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0186 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0186 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0184 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
21. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0183 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
23. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0179 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
24. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0177 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
27. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0164 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
30. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0162 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0150 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0150 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration more often than th_
39. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0148 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
42. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0148 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
43. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0147 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
44. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0143 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
45. **Pinto (2023). Methodological and Cognitive biases in Science issues for current research and ways to counteract them.pdf** — 0.0142 (rrf) — _Test (IAT). The conclusion of the study states: argumentqualitytoin extent of message processing_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0137 (rrf) — _## Evolut ionary Cognitive Psychology | mals in Pleistocene caves, for instance, demonstrate one_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0137 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0136 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of the participant's self-reported reasoning during an SPC event. Time pressure and resource constraints were treated as contextual unless a distinct cognitive or motivational mechanism was affirmatively evidenced."
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
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["hypothesis confirmation bias", "confirmatory hypothesis testing"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, favor, and recall information in ways that confirm or support one's existing beliefs or hypotheses, while giving disproportionately little attention to alternative hypotheses or disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Causal attribution after the out-of-control signal",
      "decision_point_description": "Selecting which potential causes to test after the LCL breach, when both a temperature rise and a new material lot were roughly time-aligned with the drift.",
      "affected_reasoning_operation": "Hypothesis testing and causal attribution",
      "bias_specific_mechanism": "Once the temperature explanation was strengthened by apparent timing and the process engineer's prior-experience comment, the participant treated it as sufficiently explanatory, directed attention toward documenting the temperature correlation, and deferred a feasible falsification check of the material-lot hypothesis.",
      "manifestation_in_interview": "The participant explicitly described the temperature story as explaining things well enough that he did not prioritize the lot hardness test, and later characterized the lot hypothesis as an unexamined footnote.",
      "effect_on_reasoning_or_decision": "The alternative material-lot hypothesis remained untested at the time, and the participant continued monitoring under the temperature explanation; the hardness result later arrived after the actual cause had already been addressed by a tool change.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking. And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and honestly the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.",
          "evidence_explanation": "Shows an early favored causal explanation and an explicit decision not to run a disconfirming test because that explanation felt sufficient."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption.",
          "evidence_explanation": "Demonstrates asymmetric attention: the favored explanation received active documentation while the alternative was merely logged."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote.",
          "evidence_explanation": "Retrospective acknowledgement that the feasible disconfirmation check was available and that the alternative hypothesis was left unexamined."
        }
      ],
      "correction_or_counterevidence": "The participant did record the lot as a secondary possibility, and the final lab result showed the lot was within spec; however, at the decision point the alternative was not actively tested. The participant later recognized the lot sample could have been pulled earlier.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Parasuraman and Manzey (2010) discusses confirmation bias in processing sampled information; other retrieved passages were partially OCR-degraded, so this source was used as the primary corpus anchor.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "In addition, an explanation in terms of confirmation bias in processing the sampled information or difficulties of comprehension is also unlikely, given that the participants were very well trained and that the system parameter always contradicted the aid’s diagnosis in an unequivocal way.",
          "mechanism_supported_by_source": "Confirmation bias can involve biased processing of sampled or available information rather than even-handed causal search.",
          "relevance_to_this_occurrence": "Supports using confirmation bias as a label for the participant's uneven treatment of the temperature and material-lot hypotheses."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment", "insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value, belief, or mental model and to adjust insufficiently when new evidence contradicts or qualifies that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to the 78% tool-wear sensor reading",
      "decision_point_description": "Choosing among immediate tool change, running unchanged, or an offset adjustment after sensor data indicated 78% of rated tool life.",
      "affected_reasoning_operation": "Belief updating and diagnostic judgment about tool condition",
      "bias_specific_mechanism": "The participant anchored on the prior mental model that the insert was recently serviced and therefore should not be a major factor, and adjusted only partially to the 78% wear reading by making a small offset instead of changing the tool.",
      "manifestation_in_interview": "He said the prior model was hard to fully shake in the moment and described the strong wear reading as not yet the whole story; his chosen action was an offset adjustment rather than a tool change.",
      "effect_on_reasoning_or_decision": "Delayed the tool replacement; the drift continued, the offset was not holding, and tool wear increased to 91% with parts near or slightly under the lower spec limit.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was.",
          "evidence_explanation": "Identifies the prior mental model or anchor that the tool should not yet be worn."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment.",
          "evidence_explanation": "Explicitly describes the carryover of the initial tool-age belief despite contradictory sensor data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away.",
          "evidence_explanation": "Shows the partial, insufficient adjustment away from the anchor: action was limited to an offset rather than replacing the worn tool."
        }
      ],
      "correction_or_counterevidence": "The participant did acknowledge the sensor reading as one he could not dismiss, made an interim adjustment, and ultimately recommended a tool change when Cpk dropped and wear reached 91%. He also said earlier availability of the 78% reading might have led him to change the tool sooner.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Rastogi et al. (2022) addresses anchoring-and-adjustment; the passage is OCR-degraded but substantively relevant.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Anchoring-and-adjustment involves insufficient adjustment away from an anchor, with adjustment quality influenced by available time and processing conditions.",
          "relevance_to_this_occurrence": "The participant's prior belief about the recently serviced tool served as an anchor; despite the striking 78% wear reading, he adjusted only partially via an offset."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis", "continuation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an existing plan or course of action despite emerging evidence or cues suggesting the plan should be changed.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to keep running after the tool-wear sensor reading",
      "decision_point_description": "After the 78% tool-wear sensor reading, deciding whether to stop for a tool change or continue toward shift changeover.",
      "affected_reasoning_operation": "Decision threshold for stopping production and intervening",
      "bias_specific_mechanism": "A motivational commitment to continue the production run to shift changeover made the participant set an excessively high evidence threshold for a full stop, requiring evidence to be overwhelming before changing course.",
      "manifestation_in_interview": "The participant stated that knowing changeover was close made him want to avoid a full stop until evidence was overwhelming, and that this is why he chose the smaller offset first instead of pulling the tool.",
      "effect_on_reasoning_or_decision": "The tool change was delayed; the subsequent sample continued toward the lower spec limit, and by the end of shift parts were near or slightly under spec and Cpk dropped.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one.",
          "evidence_explanation": "Shows that proximity to a planned shift changeover made stopping feel disproportionate despite the sensor reading."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in.",
          "evidence_explanation": "Directly states a high evidence threshold for abandoning the original run plan, tying the continuation decision to the desired changeover timeline."
        }
      ],
      "correction_or_counterevidence": "The participant did not ignore the wear cue entirely; he made an offset adjustment and monitored the next subgroups, and he eventually recommended an immediate tool change when Cpk and wear data became stronger. The contextual time pressure is a genuine operational constraint, so this identification is made only at low confidence.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit-cognition paper mentions plan continuation as a recurring cognitive bias but provides only sparse mechanism detail.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "and plan continuation , and in some cases multiple biases",
          "mechanism_supported_by_source": "Identifies plan continuation as a cognitive bias observed in aviation incident/accident reports, though the passage offers only sparse mechanism detail.",
          "relevance_to_this_occurrence": "The participant's continuation of the production run toward shift changeover despite contradictory tool-wear evidence is the same kind of plan-continuation pattern."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on retrospective self-report in a debrief interview, so the occurrence of bias is inferred from the participant's own account rather than direct observation.",
    "Retrieved corpus support for plan continuation bias is sparse in the provided passages, and the source mainly lists bias types rather than giving a detailed mechanism definition.",
    "Some decisions involve genuine time and resource pressures that overlap with legitimate operational heuristics, so those influences are reported only where a distinct bias-specific mechanism is stated or strongly implied."
  ]
}

