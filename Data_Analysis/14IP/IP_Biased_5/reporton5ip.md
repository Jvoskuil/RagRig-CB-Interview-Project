# RAG Benchmark — 2026-09-13

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time today. This is a cognitive task analysis interview — I'm just trying to understand how you actually worked through a real production issue, step by step, including what you knew at each point and how you decided what to do. Nothing here is evaluative of you personally, and I may ask you to reconstruct things in detail even if they seem obvious. Sound okay? Participant: Sure, happy to walk through it. I've got a good one — the Line 3 flash issue before the Meridian shipment a few weeks back. Interviewer: Perfect. Before we get into the decisions, can you just describe the incident overall — what was the situation and what were you trying to achieve? Participant: We run three shifts on Line 3, automotive interior clips for Meridian, and we had a 72-hour window to hit a shipment. Partway through a night shift, our scrap rate jumped from about 1.8% up to 6.4%, mostly flash defects, a few short shots mixed in. My objective was straightforward on paper — get quality back under 2% without blowing the ship date and without a full shutdown, since corporate wants VP sign-off for that and we didn't have time to chase approvals. Interviewer: What were the first signs something was wrong? Participant: Quality flagged the scrap numbers at shift change, and when I pulled the SPC chart, you could see cavity pressure had started drifting mid-shift. That's usually a decent early indicator. Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper. Interviewer: So walk me through what you did with that first. Participant: I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case. In hindsight, tooling wear was already flagged as a possibility by the tooling lead, but I didn't prioritize pulling that data until humidity came back clean. Interviewer: What did you learn once the humidity results came in? Participant: They were normal, well within range, so that ruled it out. That's when the tooling lead came back and said the mold had racked up wear cycles since the last inspection — more than we'd expected. So we lost a bit of time chasing the humidity angle before we got to the actual contributing factor. Interviewer: If you'd had the pressure and wear data side by side from the start, would you have sequenced it differently? Participant: Possibly. I think if I hadn't had that six-month-old case so fresh in mind, I might have pulled wear data in parallel instead of after. Interviewer: Let's move to the fix itself. Once wear was confirmed, what were your options? Participant: Wear was moderate, not severe. We had two real options — an incremental hold-pressure adjustment, which is lower risk but takes longer to validate, or a full mold-insert swap, which is more disruptive but felt like the more thorough fix. We had a press-down window shared with two other product runs, so timing was tight either way. Interviewer: What tipped you toward the insert swap? Participant: Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that. When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted. Interviewer: Did you compare the wear numbers to your swap criteria directly? Participant: Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing. Interviewer: What happened after the swap? Participant: It got done inside the window, which was good. But results were partial — scrap improved but didn't fully get back to baseline, so there was still something unresolved. Interviewer: Let's go to the third point — the sister-plant call. Participant: Right, around day two our quality engineer was out sick, so I had less statistical support than I wanted. I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network. Interviewer: What did you decide? Participant: I adopted it. Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out. Interviewer: Did you consider waiting for that validation, or a modified version? Participant: I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally. Interviewer: What came out of that? Participant: Short-term, flash defects dropped, which felt like a win. But two shifts later we started seeing a new warping issue on a subset of parts that hadn't shown up before. Interviewer: Let's get to the final decision — the rollout call. Participant: Right, so by the time Meridian's deadline was closing in, our most recent shift — the last eight hours — showed scrap down to 1.5%, best number we'd seen in four days. Corporate quality asked whether we should roll the fix out to Lines 4 and 6 as well. Interviewer: What was your reasoning? Participant: Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines. Interviewer: How did that stack up against the full four-day trend? Participant: The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call. Interviewer: Did the warping incident factor into your confidence level at that point? Participant: Less than it probably should have, looking back. I was focused on getting a clean answer to corporate fast. Interviewer: What happened with the rollout? Participant: Lines 4 and 6 looked fine initially, but one of them later threw a tooling alarm we hadn't seen before. And a fuller week-long review afterward showed the wear-related root cause was only partly addressed, not fully resolved like I'd said. Interviewer: If the last shift's numbers had come in worse instead of better, do you think you'd have made the same call? Participant: No, honestly, probably not — I think that reading was a big part of why I felt ready to greenlight it. Interviewer: What would you do differently if this happened again? Participant: Pull wear and pressure data in parallel from the start instead of chasing the familiar explanation first. And probably wait for a full trend view, not just the best shift, before telling corporate we were done. Interviewer: This has been really useful — thank you for walking through it in this much detail. Participant: No problem, happy to help.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.73s · gen 103.70s · total 107.7s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0290 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0261 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0261 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0252 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0240 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0226 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0218 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
9. **Hallihan_etal_DTM_12.pdf** — 0.0189 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
10. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
11. **Hallihan_etal_DTM_12.pdf** — 0.0181 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
12. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0180 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
13. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0179 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
14. **Lyell Automation bias and verification complexity.pdf** — 0.0177 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
15. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0176 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
16. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0173 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
19. **Hallihan_etal_DTM_12.pdf** — 0.0168 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
20. **Hallihan_etal_DTM_12.pdf** — 0.0168 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
21. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0167 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
22. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0165 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
23. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0162 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
27. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
28. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0160 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
29. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
30. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0156 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0156 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
33. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0154 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
34. **Hallihan_etal_DTM_12.pdf** — 0.0153 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
36. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0149 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
41. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
43. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0144 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
44. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0144 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
45. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0144 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
47. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0143 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
48. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0142 (rrf) — _## 2 COGNITIVE BIASES AND HEURISTICS Figure2:Acognitivereflectiontestquestion:What’sthefirst ans_
49. **Hallihan_etal_DTM_12.pdf** — 0.0140 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of a single cognitive task analysis interview. Only affirmative transcript evidence was used to identify cognitive biases, with retrieved passages used solely for definitional and mechanistic support."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency effect",
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
        "availability bias",
        "retrievability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which the ease of recalling a similar prior instance disproportionately influences judgments about current causes or risks.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial diagnosis of Line 3 scrap-rate increase",
      "decision_point_description": "Choosing which potential cause to investigate first after seeing flash defects and rising scrap.",
      "affected_reasoning_operation": "Hypothesis generation and evidence weighting",
      "bias_specific_mechanism": "The participant's immediate recall of a similar past humidity-related flash incident made that cause feel more probable, leading him to sequentially pursue humidity/drying checks and delay tooling wear data despite available pressure data and a tooling lead's warning.",
      "manifestation_in_interview": "The participant explicitly stated that the symptom pattern looked almost identical to a prior humidity event and directed first checks to drying conditions and humidity logs.",
      "effect_on_reasoning_or_decision": "Investigation was anchored to the prior humidity hypothesis, delaying identification of tooling wear as the actual contributing factor and causing lost time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper.",
          "evidence_explanation": "This quote shows the automatic retrieval of a vivid prior case as the primary hypothesis generation mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case. In hindsight, tooling wear was already flagged as a possibility by the tooling lead, but I didn't prioritize pulling that data until humidity came back clean.",
          "evidence_explanation": "This quote demonstrates that the available prior case directly shaped the information-search sequence, causing delay of competing and ultimately relevant tooling data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly. I think if I hadn't had that six-month-old case so fresh in mind, I might have pulled wear data in parallel instead of after.",
          "evidence_explanation": "The participant explicitly identifies the influence of the recalled case on the decision sequence."
        }
      ],
      "correction_or_counterevidence": "Humidity results were normal and ruled out the initial hypothesis; the participant then moved to tooling wear. A non-bias explanation is that sequential testing of a probable cause can be a legitimate diagnostic heuristic, but the explicit contrafactual and delay of available tooling data support an availability distortion.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly defines availability heuristic; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which the ease of recalling an emotionally salient prior failure disproportionately influences current risk assessment and choice.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of corrective action after tooling wear confirmation",
      "decision_point_description": "Choosing between hold-pressure adjustment and full mold-insert swap.",
      "affected_reasoning_operation": "Risk assessment and option comparison",
      "bias_specific_mechanism": "The vivid Line 5 insert failure and plant-wide debrief made that outcome highly available in memory, leading the participant to over-weight the risk of not swapping and to choose the more disruptive insert swap despite only moderate current wear.",
      "manifestation_in_interview": "The participant described the Line 5 failure as still very much on everyone's mind and said it pushed him toward the swap more than the current wear-severity comparison.",
      "effect_on_reasoning_or_decision": "The decision favored the full mold-insert swap over the lower-risk hold-pressure adjustment without rigorous comparison to swap criteria; scrap improved only partially.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that. When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted.",
          "evidence_explanation": "This quote directly links the recalled prior incident to the current risk comparison and indicates the prior case over-weighted the swap decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing.",
          "evidence_explanation": "This shows the comparison against the swap criteria was rushed, allowing the salient prior case to drive the decision."
        }
      ],
      "correction_or_counterevidence": "The swap was completed within the press-down window, but results were partial and did not fully return scrap to baseline. A rational risk-averse choice might still have favored the swap, but the participant's explicit statement that the prior case outweighed the current threshold supports an availability distortion.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly defines availability heuristic; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bandwagon effect",
      "alternative_labels": [
        "social proof",
        "conformity bias",
        "herding"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to adopt a practice or belief because many others have adopted it, sometimes without sufficient independent validation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Adoption of sister-plant cooling-time reduction protocol",
      "decision_point_description": "Deciding whether to adopt an aggressive cooling-time reduction protocol locally before completing local validation.",
      "affected_reasoning_operation": "Social information use and evidence weighting",
      "bias_specific_mechanism": "The participant placed high confidence in the protocol because three of four sister plants had adopted it and corporate quality framed it as standard, reducing perceived need for local validation against the site's resin lot and cavity geometry.",
      "manifestation_in_interview": "The participant stated that three out of four plants using the protocol gave strong confidence and that he chose the externally proven approach rather than waiting for or creating a local validation.",
      "effect_on_reasoning_or_decision": "The protocol was adopted without local validation; short-term flash decreased, but a new warping issue appeared two shifts later.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network.",
          "evidence_explanation": "This quote shows the social consensus information that formed the basis of the subsequent adoption decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out.",
          "evidence_explanation": "This quote shows the participant substituted social consensus for local validation, the core mechanism of the bandwagon effect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally.",
          "evidence_explanation": "This quote shows the participant explicitly prioritized social proof over local adaptation or validation."
        }
      ],
      "correction_or_counterevidence": "The participant did consider a more conservative version but explicitly judged the externally proven approach as lower-risk. Lack of in-house statistical support was a practical constraint, but it does not fully explain the confidence derived from the number of adopting plants.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly defines bandwagon effect or social proof; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "recency effect",
      "alternative_labels": [
        "recency bias",
        "availability of recent information"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to weight the most recent information more heavily than earlier information when forming judgments or making decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Rollout decision to Lines 4 and 6",
      "decision_point_description": "Approving plant-wide rollout after the latest shift showed improved scrap rate.",
      "affected_reasoning_operation": "Trend interpretation and confidence judgment",
      "bias_specific_mechanism": "The participant gave disproportionate evidential weight to the last eight hours' 1.5% scrap rate while under-weighting the messier four-day trend averaging about 2.9% and a prior warping issue, resulting in premature confidence that the root cause was resolved.",
      "manifestation_in_interview": "The participant stated that the last shift felt like real proof it had turned a corner and approved rollout to Lines 4 and 6, acknowledging the broader trend was messier.",
      "effect_on_reasoning_or_decision": "The participant approved rollout based on an overly favorable recent data point; Lines 4 and 6 later exhibited issues, and a week-long review showed the root cause was only partly addressed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines.",
          "evidence_explanation": "This quote links the latest shift's numbers directly to the confidence and rollout decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call.",
          "evidence_explanation": "This quote explicitly shows the participant recognized the broader trend was messier but chose to rely on the most recent point, the hallmark of recency weighting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Less than it probably should have, looking back. I was focused on getting a clean answer to corporate fast.",
          "evidence_explanation": "This quote shows the participant under-weighted contradictory information, including the warping incident, when forming the final confidence judgment."
        }
      ],
      "correction_or_counterevidence": "The participant subsequently acknowledged that if the last shift's numbers had been worse, he probably would not have made the same call. The later week-long review and Line 4 and 6 issues contradict the confidence expressed at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Natesan et al. (2016) passage defines recency effect, validating the identified mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": "Natesan et al.",
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "The source defines recency effect as increased clarity or prominence of recent events, supporting the mechanism of overweighting the most recent shift.",
          "relevance_to_this_occurrence": "The participant relied on the last shift's data rather than the full trend, consistent with the recency effect mechanism."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": [
        "selective information gathering",
        "confirmatory search"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial diagnosis of Line 3 scrap-rate increase",
      "supporting_interview_quote": "I told the team to re-check drying conditions and humidity logs first... In hindsight, tooling wear was already flagged as a possibility by the tooling lead, but I didn't prioritize pulling that data until humidity came back clean.",
      "plausible_mechanism": "The participant may have preferentially gathered information consistent with the humidity hypothesis and delayed disconfirming tooling data.",
      "why_not_identified": "The pattern is more parsimoniously attributed to availability-driven hypothesis prioritization than to a separate confirmatory search bias; the participant did eventually follow the tooling lead when humidity was normal and did not actively reject contradictory data."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "overconfidence effect",
      "alternative_labels": [
        "overconfidence bias",
        "miscalibration"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Rollout decision to Lines 4 and 6",
      "supporting_interview_quote": "Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines.",
      "plausible_mechanism": "The participant's subjective confidence may have exceeded the evidence, contributing to premature approval.",
      "why_not_identified": "The transcript more clearly supports recency effect as the mechanism that inflated confidence; overconfidence is not independently evidenced beyond the recency-weighted judgment."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on self-reported retrospective reconstruction, which may itself be affected by recall and hindsight biases.",
    "Retrieved corpus support was limited; availability heuristic and bandwagon effect classifications rely on established cognitive-science knowledge rather than directly retrieved passages.",
    "The interview provides a single case and no independent observational data, so causal attribution of bias is inferential."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time today. This is a cognitive task analysis interview — I'm just trying to understand how you actually worked through a real production issue, step by step, including what you knew at each point and how you decided what to do. Nothing here is evaluative of you personally, and I may ask you to reconstruct things in detail even if they seem obvious. Sound okay? Participant: Sure, happy to walk through it. I've got a good one — the Line 3 flash issue before the Meridian shipment a few weeks back. Interviewer: Perfect. Before we get into the decisions, can you just describe the incident overall — what was the situation and what were you trying to achieve? Participant: We run three shifts on Line 3, automotive interior clips for Meridian, and we had a 72-hour window to hit a shipment. Partway through a night shift, our scrap rate jumped from about 1.8% up to 6.4%, mostly flash defects, a few short shots mixed in. My objective was straightforward on paper — get quality back under 2% without blowing the ship date and without a full shutdown, since corporate wants VP sign-off for that and we didn't have time to chase approvals. Interviewer: What were the first signs something was wrong? Participant: Quality flagged the scrap numbers at shift change, and when I pulled the SPC chart, you could see cavity pressure had started drifting mid-shift. That's usually a decent early indicator. Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper. Interviewer: So walk me through what you did with that first. Participant: I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case. In hindsight, tooling wear was already flagged as a possibility by the tooling lead, but I didn't prioritize pulling that data until humidity came back clean. Interviewer: What did you learn once the humidity results came in? Participant: They were normal, well within range, so that ruled it out. That's when the tooling lead came back and said the mold had racked up wear cycles since the last inspection — more than we'd expected. So we lost a bit of time chasing the humidity angle before we got to the actual contributing factor. Interviewer: If you'd had the pressure and wear data side by side from the start, would you have sequenced it differently? Participant: Possibly. I think if I hadn't had that six-month-old case so fresh in mind, I might have pulled wear data in parallel instead of after. Interviewer: Let's move to the fix itself. Once wear was confirmed, what were your options? Participant: Wear was moderate, not severe. We had two real options — an incremental hold-pressure adjustment, which is lower risk but takes longer to validate, or a full mold-insert swap, which is more disruptive but felt like the more thorough fix. We had a press-down window shared with two other product runs, so timing was tight either way. Interviewer: What tipped you toward the insert swap? Participant: Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that. When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted. Interviewer: Did you compare the wear numbers to your swap criteria directly? Participant: Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing. Interviewer: What happened after the swap? Participant: It got done inside the window, which was good. But results were partial — scrap improved but didn't fully get back to baseline, so there was still something unresolved. Interviewer: Let's go to the third point — the sister-plant call. Participant: Right, around day two our quality engineer was out sick, so I had less statistical support than I wanted. I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network. Interviewer: What did you decide? Participant: I adopted it. Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out. Interviewer: Did you consider waiting for that validation, or a modified version? Participant: I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally. Interviewer: What came out of that? Participant: Short-term, flash defects dropped, which felt like a win. But two shifts later we started seeing a new warping issue on a subset of parts that hadn't shown up before. Interviewer: Let's get to the final decision — the rollout call. Participant: Right, so by the time Meridian's deadline was closing in, our most recent shift — the last eight hours — showed scrap down to 1.5%, best number we'd seen in four days. Corporate quality asked whether we should roll the fix out to Lines 4 and 6 as well. Interviewer: What was your reasoning? Participant: Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines. Interviewer: How did that stack up against the full four-day trend? Participant: The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call. Interviewer: Did the warping incident factor into your confidence level at that point? Participant: Less than it probably should have, looking back. I was focused on getting a clean answer to corporate fast. Interviewer: What happened with the rollout? Participant: Lines 4 and 6 looked fine initially, but one of them later threw a tooling alarm we hadn't seen before. And a fuller week-long review afterward showed the wear-related root cause was only partly addressed, not fully resolved like I'd said. Interviewer: If the last shift's numbers had come in worse instead of better, do you think you'd have made the same call? Participant: No, honestly, probably not — I think that reading was a big part of why I felt ready to greenlight it. Interviewer: What would you do differently if this happened again? Participant: Pull wear and pressure data in parallel from the start instead of chasing the familiar explanation first. And probably wait for a full trend view, not just the best shift, before telling corporate we were done. Interviewer: This has been really useful — thank you for walking through it in this much detail. Participant: No problem, happy to help.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.74s · gen 90.85s · total 94.8s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0290 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0261 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0261 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0252 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0240 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0226 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0218 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
9. **Hallihan_etal_DTM_12.pdf** — 0.0189 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
10. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
11. **Hallihan_etal_DTM_12.pdf** — 0.0181 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
12. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0180 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
13. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0179 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
14. **Lyell Automation bias and verification complexity.pdf** — 0.0177 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
15. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0176 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
16. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0173 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
19. **Hallihan_etal_DTM_12.pdf** — 0.0168 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
20. **Hallihan_etal_DTM_12.pdf** — 0.0168 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
21. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0167 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
22. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0165 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
23. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0162 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
27. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
28. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0160 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
29. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
30. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0156 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0156 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
33. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0154 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
34. **Hallihan_etal_DTM_12.pdf** — 0.0153 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
36. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0149 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
41. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
43. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0144 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
44. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0144 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
45. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0144 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
47. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0143 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
48. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0142 (rrf) — _## 2 COGNITIVE BIASES AND HEURISTICS Figure2:Acognitivereflectiontestquestion:What’sthefirst ans_
49. **Hallihan_etal_DTM_12.pdf** — 0.0140 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a single retrospective cognitive task interview about a production quality issue. Findings are based on the participant's self-reported reasoning and do not assume a normative benchmark or experimental condition."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "retrieval ease heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which the ease or vividness with which instances come to mind influences judgments of likelihood, importance, or cause.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial diagnostic prioritization after the scrap-rate increase",
      "decision_point_description": "Choosing whether to prioritize humidity/drying checks or tooling wear data as the likely explanation for the flash defect spike.",
      "affected_reasoning_operation": "Causal hypothesis generation and diagnostic information-seeking prioritization",
      "bias_specific_mechanism": "A previous similar incident came easily and vividly to mind, leading the participant to overestimate the likelihood that the same cause was operative and to prioritize confirming that familiar cause over other available data.",
      "manifestation_in_interview": "The participant interpreted the current symptoms as nearly identical to a six-month-old humidity-related case and directed the team to re-check drying conditions and humidity logs first, delaying tooling-wear data despite the pressure data and a tooling lead already flagging wear.",
      "effect_on_reasoning_or_decision": "The diagnostic sequence was skewed toward a familiar prior cause, delaying evaluation of tooling wear and losing time before the actual contributing factor was investigated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper.",
          "evidence_explanation": "The participant immediately retrieves a prior similar case and uses that similarity to form an initial causal hypothesis, demonstrating the accessibility of the prior case."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case.",
          "evidence_explanation": "The remembered prior fix is used to prioritize humidity checks over pressure and tooling data, showing that the easy-to-recall instance influenced information-seeking."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think if I hadn't had that six-month-old case so fresh in mind, I might have pulled wear data in parallel instead of after.",
          "evidence_explanation": "The participant explicitly attributes the sequencing decision to the freshness of the prior case, which is the core availability-heuristic mechanism."
        }
      ],
      "correction_or_counterevidence": "Counterevidence: the participant did not ignore tooling entirely, and once humidity came back clean he shifted to tooling. The prior similar case could be a legitimate diagnostic cue, and sequential checking under time pressure may be defensible. However, the participant himself states that the fresh prior case delayed parallel wear-data review.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the availability heuristic label was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "retrieval ease heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which the ease or vividness with which instances come to mind influences judgments of likelihood, importance, or cause.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Choice between hold-pressure adjustment and mold-insert swap",
      "decision_point_description": "Deciding whether to select the lower-risk incremental hold-pressure adjustment or the more disruptive full mold-insert swap after moderate wear was confirmed.",
      "affected_reasoning_operation": "Risk assessment and choice between corrective actions",
      "bias_specific_mechanism": "The salient memory of a prior insert failure and shutdown was highly available during the decision, increasing perceived risk of not swapping and pushing the participant toward the more drastic fix beyond what the current wear-severity evidence supported.",
      "manifestation_in_interview": "The participant said the earlier Line 5 insert failure kept coming up in his head and pushed him toward the insert swap, even though he did not directly compare current wear numbers to the swap-trigger criteria.",
      "effect_on_reasoning_or_decision": "The choice favored the more disruptive full insert swap over the lower-risk incremental adjustment without the participant rigorously comparing current wear data against the established swap threshold.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that.",
          "evidence_explanation": "The prior insert failure is described as highly salient and emotionally charged, which is the precondition for availability-based influence on risk perception."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted.",
          "evidence_explanation": "The participant explicitly connects the easily recalled prior case to disproportionate influence on the swap decision, rather than a criterion-based comparison of current wear."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing.",
          "evidence_explanation": "The participant admits the decision was not anchored to the current wear-to-criteria comparison, consistent with heuristic rather than analytic comparison."
        }
      ],
      "correction_or_counterevidence": "Counterevidence: the insert swap was completed within the window and concerns about a repeated insert failure were not irrational given the prior event. A risk-averse choice may be defensible. However, the participant explicitly states the memory of the prior failure pushed him beyond a strict comparison of current wear severity against threshold criteria.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the availability heuristic label was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bandwagon effect",
      "alternative_labels": ["social proof", "consensus bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to adopt a belief, action, or decision because many others have adopted it, using its prevalence as a proxy for correctness or appropriateness.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Adoption of sister-plant cooling-time reduction protocol",
      "decision_point_description": "Deciding whether to adopt an aggressive cooling-time reduction protocol locally or wait for in-house validation against the plant's specific resin lot and cavity geometry.",
      "affected_reasoning_operation": "Evaluation of external evidence and protocol-adoption decision",
      "bias_specific_mechanism": "The number of external sites already using the protocol operated as evidence of its safety and efficacy, leading the participant to generalize from majority adoption to local applicability without full local validation.",
      "manifestation_in_interview": "The participant gave weight to three of four sister plants already using the protocol and to corporate framing it as a standard, choosing adoption over a more conservative or validated local version.",
      "effect_on_reasoning_or_decision": "The participant adopted the aggressive protocol without in-house validation; short-term flash defects dropped, but a new warping issue appeared two shifts later.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network.",
          "evidence_explanation": "The participant was exposed to majority adoption and corporate standard framing, establishing the social consensus cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out.",
          "evidence_explanation": "Majority adoption is explicitly cited as the source of confidence in local effectiveness, substituting for local validation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally.",
          "evidence_explanation": "The participant chose the majority-endorsed approach because it was widely adopted, rather than tailoring the protocol to local conditions, consistent with bandwagon reasoning."
        }
      ],
      "correction_or_counterevidence": "Counterevidence: using multiple sister-plant experience and corporate standardization may be reasonable under time and personnel constraints, and the participant did consider a more conservative version. The bias-specific feature is that the count of adopters generated confidence independent of local validation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the bandwagon effect label was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "recency bias",
      "alternative_labels": ["recency effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overweight the most recent information or events relative to earlier or aggregated evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Rollout approval to Lines 4 and 6",
      "decision_point_description": "Deciding whether to approve rolling out the corrective fix to Lines 4 and 6 and whether to report the root cause as resolved to corporate quality.",
      "affected_reasoning_operation": "Evaluation of process stability and root-cause-resolution confidence",
      "bias_specific_mechanism": "The most recent eight-hour shift's favorable scrap-rate reading was highly accessible and was treated as more diagnostic than the longer, messier four-day trend, leading to overconfidence in the fix.",
      "manifestation_in_interview": "The participant leaned on the last shift's 1.5 percent scrap rate, the best in four days, and told corporate the root cause was resolved, even though the four-day trend averaged about 2.9 percent and included a new warping issue.",
      "effect_on_reasoning_or_decision": "The participant approved rollout to Lines 4 and 6 and communicated root-cause resolution based on the recent favorable shift, though a later weekly review showed the wear-related root cause was only partly addressed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines.",
          "evidence_explanation": "The participant's confidence and rollout decision were based on the most recent shift numbers, illustrating recency-based evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call.",
          "evidence_explanation": "The participant explicitly contrasts the fuller trend with the recent shift and indicates the recent shift was treated as decisive proof, the core recency-bias mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, honestly, probably not — I think that reading was a big part of why I felt ready to greenlight it.",
          "evidence_explanation": "The participant concedes that the favorable last-shift reading played a major role in the rollout decision, confirming the influence of recent information."
        }
      ],
      "correction_or_counterevidence": "Counterevidence: the last shift was a real, recent data point and could legitimately signal improvement; the participant was also under pressure to provide a fast answer to corporate. However, the participant himself acknowledges the fuller trend was messier and that the last shift's reading drove the call.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label is supported by a retrieved passage on the recency effect, though the retrieved source discusses recall in usability testing rather than process-data interpretation.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": "Natesan et al.",
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Recent information has disproportionate accessibility or salience in recall and judgment.",
          "relevance_to_this_occurrence": "Although the source concerns recall in usability testing, the same recency mechanism is consistent with the participant over-weighting the most recent shift's scrap rate relative to the longer trend."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "overconfidence effect",
      "alternative_labels": ["overconfidence bias", "overprecision"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Rollout approval to Lines 4 and 6",
      "supporting_interview_quote": "I told corporate I was confident the root cause was resolved and approved rollout to both lines.",
      "plausible_mechanism": "The participant's subjective confidence in root-cause resolution may have exceeded the available evidence, particularly given the messier four-day trend and unresolved warping signal.",
      "why_not_identified": "The confidence was largely driven by the recency bias already identified in the same episode, and the transcript does not provide a separate confidence-calibration baseline or direct measure, so a distinct overconfidence mechanism is plausible but not sufficiently separable."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on a single retrospective self-report, which can be affected by memory distortion and self-presentation.",
    "There is no controlled baseline or normative decision model against which to compare the participant's choices.",
    "Retrieved corpus support was sparse and partly from a different domain; availability and bandwagon labels rely on general cognitive-science knowledge.",
    "Some decisions occurred under genuine time, staffing, and production constraints that may make heuristic reliance more reasonable.",
    "Outcomes such as later warping or incomplete root-cause resolution are not treated as direct evidence of bias at the time of decision."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time today. This is a cognitive task analysis interview — I'm just trying to understand how you actually worked through a real production issue, step by step, including what you knew at each point and how you decided what to do. Nothing here is evaluative of you personally, and I may ask you to reconstruct things in detail even if they seem obvious. Sound okay? Participant: Sure, happy to walk through it. I've got a good one — the Line 3 flash issue before the Meridian shipment a few weeks back. Interviewer: Perfect. Before we get into the decisions, can you just describe the incident overall — what was the situation and what were you trying to achieve? Participant: We run three shifts on Line 3, automotive interior clips for Meridian, and we had a 72-hour window to hit a shipment. Partway through a night shift, our scrap rate jumped from about 1.8% up to 6.4%, mostly flash defects, a few short shots mixed in. My objective was straightforward on paper — get quality back under 2% without blowing the ship date and without a full shutdown, since corporate wants VP sign-off for that and we didn't have time to chase approvals. Interviewer: What were the first signs something was wrong? Participant: Quality flagged the scrap numbers at shift change, and when I pulled the SPC chart, you could see cavity pressure had started drifting mid-shift. That's usually a decent early indicator. Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper. Interviewer: So walk me through what you did with that first. Participant: I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case. In hindsight, tooling wear was already flagged as a possibility by the tooling lead, but I didn't prioritize pulling that data until humidity came back clean. Interviewer: What did you learn once the humidity results came in? Participant: They were normal, well within range, so that ruled it out. That's when the tooling lead came back and said the mold had racked up wear cycles since the last inspection — more than we'd expected. So we lost a bit of time chasing the humidity angle before we got to the actual contributing factor. Interviewer: If you'd had the pressure and wear data side by side from the start, would you have sequenced it differently? Participant: Possibly. I think if I hadn't had that six-month-old case so fresh in mind, I might have pulled wear data in parallel instead of after. Interviewer: Let's move to the fix itself. Once wear was confirmed, what were your options? Participant: Wear was moderate, not severe. We had two real options — an incremental hold-pressure adjustment, which is lower risk but takes longer to validate, or a full mold-insert swap, which is more disruptive but felt like the more thorough fix. We had a press-down window shared with two other product runs, so timing was tight either way. Interviewer: What tipped you toward the insert swap? Participant: Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that. When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted. Interviewer: Did you compare the wear numbers to your swap criteria directly? Participant: Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing. Interviewer: What happened after the swap? Participant: It got done inside the window, which was good. But results were partial — scrap improved but didn't fully get back to baseline, so there was still something unresolved. Interviewer: Let's go to the third point — the sister-plant call. Participant: Right, around day two our quality engineer was out sick, so I had less statistical support than I wanted. I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network. Interviewer: What did you decide? Participant: I adopted it. Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out. Interviewer: Did you consider waiting for that validation, or a modified version? Participant: I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally. Interviewer: What came out of that? Participant: Short-term, flash defects dropped, which felt like a win. But two shifts later we started seeing a new warping issue on a subset of parts that hadn't shown up before. Interviewer: Let's get to the final decision — the rollout call. Participant: Right, so by the time Meridian's deadline was closing in, our most recent shift — the last eight hours — showed scrap down to 1.5%, best number we'd seen in four days. Corporate quality asked whether we should roll the fix out to Lines 4 and 6 as well. Interviewer: What was your reasoning? Participant: Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines. Interviewer: How did that stack up against the full four-day trend? Participant: The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call. Interviewer: Did the warping incident factor into your confidence level at that point? Participant: Less than it probably should have, looking back. I was focused on getting a clean answer to corporate fast. Interviewer: What happened with the rollout? Participant: Lines 4 and 6 looked fine initially, but one of them later threw a tooling alarm we hadn't seen before. And a fuller week-long review afterward showed the wear-related root cause was only partly addressed, not fully resolved like I'd said. Interviewer: If the last shift's numbers had come in worse instead of better, do you think you'd have made the same call? Participant: No, honestly, probably not — I think that reading was a big part of why I felt ready to greenlight it. Interviewer: What would you do differently if this happened again? Participant: Pull wear and pressure data in parallel from the start instead of chasing the familiar explanation first. And probably wait for a full trend view, not just the best shift, before telling corporate we were done. Interviewer: This has been really useful — thank you for walking through it in this much detail. Participant: No problem, happy to help.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.68s · gen 96.83s · total 100.7s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0290 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0261 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0261 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0252 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0240 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0226 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0218 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
9. **Hallihan_etal_DTM_12.pdf** — 0.0189 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
10. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
11. **Hallihan_etal_DTM_12.pdf** — 0.0181 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
12. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0180 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
13. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0179 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
14. **Lyell Automation bias and verification complexity.pdf** — 0.0177 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
15. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0176 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
16. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0173 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
19. **Hallihan_etal_DTM_12.pdf** — 0.0168 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
20. **Hallihan_etal_DTM_12.pdf** — 0.0168 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
21. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0167 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
22. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0165 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
23. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0162 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
27. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
28. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0160 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
29. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
30. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0156 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0156 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
33. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0154 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
34. **Hallihan_etal_DTM_12.pdf** — 0.0153 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
36. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0149 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
41. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
43. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0144 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
44. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0144 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
45. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0144 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
47. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0143 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
48. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0142 (rrf) — _## 2 COGNITIVE BIASES AND HEURISTICS Figure2:Acognitivereflectiontestquestion:What’sthefirst ans_
49. **Hallihan_etal_DTM_12.pdf** — 0.0140 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis was limited to transcript evidence for bias occurrence. Retrieved passages were used only as conceptual support for labels and mechanisms."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability bias",
      "alternative_labels": ["availability heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge likelihood, relevance, or priority based on how easily similar instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial diagnosis and prioritization of humidity verification",
      "decision_point_description": "Choosing which data to check first after seeing SPC drift and an increase in flash defects.",
      "affected_reasoning_operation": "Hypothesis generation and diagnostic prioritization",
      "bias_specific_mechanism": "A readily recalled prior humidity-related case made the current problem seem highly similar, leading the participant to prioritize humidity checks over simultaneously available tooling data.",
      "manifestation_in_interview": "The participant immediately connected the current flash issue to a six-month-old humidity case, described the match as almost identical, and directed the team to re-check drying and humidity logs first while delaying tooling data.",
      "effect_on_reasoning_or_decision": "The participant lost time chasing the familiar humidity explanation before reaching the actual tooling-wear contributor.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper.",
          "evidence_explanation": "This shows the earlier humidity case was highly accessible and shaped the initial diagnostic hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case.",
          "evidence_explanation": "The participant explicitly prioritizes the recalled prior cause over available pressure data, demonstrating availability-based diagnostic prioritization."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think if I hadn't had that six-month-old case so fresh in mind, I might have pulled wear data in parallel instead of after.",
          "evidence_explanation": "The participant directly links the freshness of the prior case to the suboptimal sequencing of diagnostic checks."
        }
      ],
      "correction_or_counterevidence": "Humidity results came back normal and tooling wear was later confirmed as the actual contributing factor. The participant acknowledged that parallel data collection would have been better.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly supported availability bias. The label rests on established general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability bias",
      "alternative_labels": ["availability heuristic", "salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge risk or choose actions based on how easily salient past instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of mold-insert swap versus hold-pressure adjustment",
      "decision_point_description": "Choosing between an incremental hold-pressure adjustment and a full mold-insert swap after confirming moderate mold wear.",
      "affected_reasoning_operation": "Risk comparison and choice between two repair options",
      "bias_specific_mechanism": "A vivid prior insert-failure event from the plant was easily recalled and inflated the perceived risk of not performing the more disruptive insert swap, outweighing a strict comparison of current wear severity against swap criteria.",
      "manifestation_in_interview": "The participant said the Line 5 insert failure kept coming up in his head and pushed him toward the insert swap, despite wear being moderate and without rigorously comparing the current wear numbers to swap thresholds.",
      "effect_on_reasoning_or_decision": "The participant selected the more disruptive full insert swap partly because of the salient prior failure rather than a strict current-condition assessment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that. When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted.",
          "evidence_explanation": "The participant explicitly identifies the salient past event as a driver of the swap decision, rather than a strict current-state comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing.",
          "evidence_explanation": "This acknowledges that the swap decision was not based on a rigorous comparison of wear data to criteria, consistent with availability-driven judgment."
        }
      ],
      "correction_or_counterevidence": "Wear was moderate, not severe, and the participant acknowledged he did not rigorously compare the wear numbers to swap criteria. Time pressure from the press-down window was also present.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly supported availability bias. The label rests on established general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bandwagon effect",
      "alternative_labels": ["social proof", "herding"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to adopt a belief or action because many other people or organizations have adopted it, rather than relying primarily on independent evaluation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Adoption of sister-plant cooling-time reduction protocol",
      "decision_point_description": "Deciding whether to adopt the sister-plant cooling-time reduction protocol without local validation.",
      "affected_reasoning_operation": "Evaluation of local applicability of an external protocol",
      "bias_specific_mechanism": "The number of sister plants already using the protocol and corporate framing of it as standard were treated as strong evidence that it would work locally, reducing the perceived need for local validation.",
      "manifestation_in_interview": "The participant learned that three of four sister plants had adopted the protocol and that corporate quality framed it as becoming standard. He adopted it, citing the high adoption rate as giving him confidence, even though no local validation was performed.",
      "effect_on_reasoning_or_decision": "The participant adopted the protocol locally without running a validation specific to the local resin lot and cavity geometry, and later experienced new warping issues.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network.",
          "evidence_explanation": "The participant describes information about majority adoption and corporate standard framing that became central to his decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I adopted it. Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out.",
          "evidence_explanation": "The adoption rate was explicitly used as evidence for local success, while local validation was skipped."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally.",
          "evidence_explanation": "The participant chose to follow the majority rather than pursue a locally tailored or validated version."
        }
      ],
      "correction_or_counterevidence": "The quality engineer was out sick, corporate quality was framing the protocol as standard, and the participant considered a more conservative version. These factors provide a competing explanation based on standardization and resource constraints, but the majority-adoption mechanism is still affirmatively present.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly supported bandwagon effect or social proof. The label rests on established general cognitive-science and social-influence knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "recency bias",
      "alternative_labels": ["recency effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overemphasize the most recent information or outcome when forming a judgment or decision.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final rollout approval for Lines 4 and 6",
      "decision_point_description": "Deciding whether to approve rollout of the fix to Lines 4 and 6 after corporate quality asked about extending it.",
      "affected_reasoning_operation": "Assessment of whether the root cause was resolved and approval decision",
      "bias_specific_mechanism": "The participant over-weighted the most recent eight-hour shift, which showed the best scrap rate in four days, while under-weighting the broader, messier four-day trend and prior warping issue.",
      "manifestation_in_interview": "The participant used the last shift's 1.5% scrap rate as the primary evidence that the root cause was resolved and approved rollout, despite acknowledging the broader trend averaged 2.9% and included variability and warping.",
      "effect_on_reasoning_or_decision": "The participant told corporate quality that the root cause was resolved and approved rollout to Lines 4 and 6, based heavily on the most recent shift result.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines.",
          "evidence_explanation": "The participant explicitly says the last shift's numbers were the basis for his confidence and rollout decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call.",
          "evidence_explanation": "This shows the participant consciously prioritized the recent favorable shift over the broader trend and prior problem."
        },
        {
          "speaker": "Interviewer",
          "verbatim_quote": "If the last shift's numbers had come in worse instead of better, do you think you'd have made the same call?",
          "evidence_explanation": "The interviewer prompts the participant to evaluate the influence of the recent data point."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, honestly, probably not — I think that reading was a big part of why I felt ready to greenlight it.",
          "evidence_explanation": "The participant confirms that his decision was substantially driven by the latest shift's favorable result."
        }
      ],
      "correction_or_counterevidence": "A fuller week-long review later showed the wear-related root cause was only partly addressed, and Lines 4 and 6 later had a tooling alarm. The participant acknowledged the warping issue factored in less than it should have.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus contained a passage on recency effect from natesan et al. (2016), which supports the general tendency for recent events to be more available or influential in judgments.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive bias in usability testing",
          "authors": null,
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly. For example, as participants use a device, they become more familiar the Priming and Recency Effect. While participants should be surveyed following the study, the way questions are asked and the timing of those questions may change the way a participant actually felt when working with the device. In general, the participant’s opinion is much more subjective and may change over time.",
          "mechanism_supported_by_source": "The passage describes a recency effect in which recent events are remembered more clearly and can distort reports or judgments.",
          "relevance_to_this_occurrence": "The participant's rollout decision was driven by the most recent shift result rather than the full trend, consistent with the described tendency to weight recent events more heavily."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is retrospective self-report, so internal cognitive mechanisms cannot be directly observed.",
    "The retrieved corpus did not include direct support for availability bias or bandwagon effect; those labels rely on general cognitive-science and social-influence knowledge.",
    "Some decisions occurred under real operational constraints, such as time pressure and absent statistical support, which can provide competing non-bias explanations."
  ]
}

