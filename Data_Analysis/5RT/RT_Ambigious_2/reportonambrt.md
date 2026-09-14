# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. This is just a debrief for training purposes — we're looking at how you worked through the call, not grading the outcome. Okay to go ahead? Participant: Yeah, that's fine. Interviewer: Can you tell me your role and set the scene for that evening? Participant: I'm a signal maintainer covering the territory that includes the Marlow interlocking, out on the secondary main line. I got paged out in the evening after a track crew reported the signal dropping to a more restrictive aspect twice during their shift, then clearing back to normal on its own both times. It had rained earlier that day, so everything out there was still damp. My job was to figure out what was going on and get the signal back to reliable automatic operation before the next scheduled train movement, without stringing the possession out longer than it needed to be. Interviewer: Walk me through what you found and what you did first. Participant: When I got to the cabinet, there was no fault code logged at the interlocking — nothing tripped that would point me straight at a component. No history of this signal giving trouble before, either, so it wasn't a repeat offender. I did a visual first: no obvious damage, no standing water in the case, gasket looked a little worn but nothing dramatic. At that point I had two ways I could go. I could sit and watch the signal through another cycle or two to see if the drop repeated in a way I could actually observe, or I could go straight into bench testing the track circuit and relay to start ruling things in or out. Interviewer: Which way did you go? Participant: I went straight into testing. Waiting around for it to happen again felt like it could burn time I didn't have if the next train was going to need a clear signal, and testing gets me actual numbers instead of just watching and hoping it repeats on a schedule that suits me. Interviewer: How confident were you that testing first was the better call? Participant: Fairly confident, but I'll be honest, it wasn't a slam dunk either way. Watching it might've told me more about the actual pattern — whether it was tied to a specific type of train movement, say. But testing gets me hard numbers right away, and with the clock running, I leaned that way. Interviewer: What did the testing show? Participant: That's where it got murkier. I ran three insulation resistance cycles. Two came back within normal tolerance, one came back marginally low — not a fail, just lower than I'd like to see. No single component gave me a clean, readable fault. So now I've got a relay and wiring that's original to a fifteen-year-old installation, and one reading out of three that's a little off. Interviewer: What were you weighing at that point? Participant: Whether to just replace the relay and that wiring segment right there, using the marginal reading as my justification, or hold off and run more cycles to see if a real pattern showed up before committing to a replacement. Interviewer: What did you decide? Participant: I ran more cycles instead of replacing on the spot. One marginal reading against two normal ones didn't feel like enough to hang a full replacement on — it could've been the wiring starting to go, or it could've been a temporary moisture effect given the damp conditions. I gave it a fourth cycle after some extra drying time, and that one came back normal. Interviewer: Did that resolve it for you? Participant: Not entirely. It made the moisture explanation more plausible, but it didn't rule out the wiring either — a marginal insulation reading can come and go for more than one reason, so I still didn't have a clean answer. Interviewer: That brings us to the next call — what were the options once you had that pattern of readings? Participant: The gasket on the cabinet was showing some wear, and the marginal reading lined up with timing not long after that earlier rain. So I had a lower-cost option: dry everything out, clean the connections, reseal the case, and monitor. Or I could go straight to a full replacement of the wiring segment, which would take a lot longer and eat into overtime I'd need approval to extend. Interviewer: What tipped it for you? Participant: The timing with the rain was a real data point, not just a guess — it's a known failure mode on older cabinets with worn gaskets. That gave me a specific, testable explanation I hadn't ruled out yet, so trying the cheaper fix first and watching the results made sense to me before committing the extra hours to a full swap. Interviewer: How did that play out? Participant: Readings stayed stable through two more monitored cycles after the drying and resealing. Which was encouraging, but two clean cycles after a marginal one doesn't fully prove the wiring's fine — it's consistent with the fix working, and it's also consistent with the marginal reading just being a one-off that would've cleared up on its own. Interviewer: Last decision — putting the signal back in service. Participant: Right, by that point I had two stable cycles, the next scheduled movement was coming up, and I still didn't have a confirmed root cause — could've been the moisture issue resolved, could've been a quiet wiring problem that just hadn't shown itself again yet. My options were to restore automatic service on the strength of those two stable readings, or keep it under manual block protection for the rest of the shift and take another look in daylight. Interviewer: What did you go with, and why? Participant: I restored it to automatic service. Two consecutive normal readings after the interim fix was enough for me to move forward, and keeping manual protection running all night has its own cost — it ties up a dispatcher's attention and slows things down for every movement through there. But I did flag it for a follow-up inspection rather than calling it closed, because I knew I hadn't actually nailed down which explanation was right. Interviewer: Did it hold up? Participant: Yeah, ran clean through the rest of the shift. But I want to be clear, that doesn't tell me for certain I got the diagnosis right — it just means nothing happened on my watch that night. Interviewer: If that fourth test cycle had come back marginal again instead of normal, would you have done something different? Participant: Almost certainly, yeah. Two marginal readings out of four would've pushed me toward the full replacement instead of the interim fix — that's a different pattern than what I actually saw. Interviewer: And if you'd had open-ended overtime approval that night? Participant: Honestly, I might have leaned toward the full wiring replacement regardless, just to close the loop completely instead of leaving it on an interim fix. The time and approval limits were part of what made the cheaper option attractive. Interviewer: Looking back, is there anything you'd want more information on, even now? Participant: I'd still like a cleaner way to separate a moisture-related reading from an early-stage wiring issue on that generation of cabinet. Right now both look the same on my meter, and that's the part of this call I'm least settled on.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.28s · gen 81.00s · total 85.7s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0283 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0279 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0268 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0264 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0247 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
6. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0225 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0225 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0215 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
9. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0201 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0194 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0186 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
14. **Lyell Automation bias and verification complexity.pdf** — 0.0184 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
15. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
16. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0180 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0179 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
19. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0174 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0172 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
22. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0169 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0168 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0166 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0164 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
27. **Hallihan_etal_DTM_12.pdf** — 0.0160 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
28. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
30. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
34. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0154 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
36. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0151 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _# to Dangers from Humans speed, brute strength, sensory acuity, and apparent det allies to attac_
39. **Hallihan_etal_DTM_12.pdf** — 0.0149 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
41. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0146 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _### TER 33 | p ut forward by Kathryn Coe (2003) that art serves primarily to signal affiliation _
44. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0146 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
45. **Hallihan_etal_DTM_12.pdf** — 0.0145 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
46. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0144 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
47. **Hallihan_etal_DTM_12.pdf** — 0.0143 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
48. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0141 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
50. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0137 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative, mechanism-first evaluation of the maintainer debrief. No affirmative cognitive bias occurrence met the identification threshold; plausible but insufficient patterns are recorded as candidates only."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Restoring signal to automatic service after interim fix",
      "supporting_interview_quote": "I restored it to automatic service. Two consecutive normal readings after the interim fix was enough for me to move forward, and keeping manual protection running all night has its own cost — it ties up a dispatcher's attention and slows things down for every movement through there.",
      "plausible_mechanism": "Operational schedule pressure and the desire to restore normal service may have biased risk acceptance toward returning the signal to automatic operation despite unresolved root-cause uncertainty.",
      "why_not_identified": "The transcript contains an explicit acknowledgement that two normal readings do not prove the diagnosis, and the decision is framed as a deliberate operational risk/cost tradeoff under resource constraints. These provide a plausible non-bias explanation that prevents an affirmative identification."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory search"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Choosing moisture mitigation over full wiring replacement",
      "supporting_interview_quote": "The timing with the rain was a real data point, not just a guess — it's a known failure mode on older cabinets with worn gaskets. That gave me a specific, testable explanation I hadn't ruled out yet, so trying the cheaper fix first and watching the results made sense to me before committing the extra hours to a full swap.",
      "plausible_mechanism": "A plausible, contextually cued moisture hypothesis may have been favored, with subsequent evidence interpreted in light of that preferred explanation.",
      "why_not_identified": "The participant did not engage in one-sided search or interpretation; he explicitly acknowledged the competing wiring explanation, sought additional test cycles, and maintained uncertainty after the decision. The reasoning is therefore better explained by ordinary diagnostic caution than by a confirmatory bias mechanism."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "Anchoring and adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Interpreting one marginal insulation resistance reading among three",
      "supporting_interview_quote": "One marginal reading against two normal ones didn't feel like enough to hang a full replacement on — it could've been the wiring starting to go, or it could've been a temporary moisture effect given the damp conditions.",
      "plausible_mechanism": "The initial normal readings may have served as an anchor, potentially leading to insufficient adjustment in response to the marginal reading.",
      "why_not_identified": "The transcript does not supply affirmative evidence that the participant's caution was a distorted anchoring process; requiring more evidence before replacing a component on the basis of a single marginal reading is a defensible epistemic standard under uncertainty."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "The interview contains explicit reasoning that is often well-calibrated, including acknowledgement of uncertainty and alternative explanations, which reduces the likelihood of affirmative bias identification under a conservative threshold.",
    "Retrieved corpus passages provided limited definitions for biases relevant to this maintenance-decision context, so candidate classifications relied on established cognitive-science knowledge rather than corpus-confirmed mechanisms.",
    "The analysis did not identify any occurrence meeting the threshold for an affirmative, mechanism-grounding cognitive bias; therefore, retrieved_corpus_support_used is false."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. This is just a debrief for training purposes — we're looking at how you worked through the call, not grading the outcome. Okay to go ahead? Participant: Yeah, that's fine. Interviewer: Can you tell me your role and set the scene for that evening? Participant: I'm a signal maintainer covering the territory that includes the Marlow interlocking, out on the secondary main line. I got paged out in the evening after a track crew reported the signal dropping to a more restrictive aspect twice during their shift, then clearing back to normal on its own both times. It had rained earlier that day, so everything out there was still damp. My job was to figure out what was going on and get the signal back to reliable automatic operation before the next scheduled train movement, without stringing the possession out longer than it needed to be. Interviewer: Walk me through what you found and what you did first. Participant: When I got to the cabinet, there was no fault code logged at the interlocking — nothing tripped that would point me straight at a component. No history of this signal giving trouble before, either, so it wasn't a repeat offender. I did a visual first: no obvious damage, no standing water in the case, gasket looked a little worn but nothing dramatic. At that point I had two ways I could go. I could sit and watch the signal through another cycle or two to see if the drop repeated in a way I could actually observe, or I could go straight into bench testing the track circuit and relay to start ruling things in or out. Interviewer: Which way did you go? Participant: I went straight into testing. Waiting around for it to happen again felt like it could burn time I didn't have if the next train was going to need a clear signal, and testing gets me actual numbers instead of just watching and hoping it repeats on a schedule that suits me. Interviewer: How confident were you that testing first was the better call? Participant: Fairly confident, but I'll be honest, it wasn't a slam dunk either way. Watching it might've told me more about the actual pattern — whether it was tied to a specific type of train movement, say. But testing gets me hard numbers right away, and with the clock running, I leaned that way. Interviewer: What did the testing show? Participant: That's where it got murkier. I ran three insulation resistance cycles. Two came back within normal tolerance, one came back marginally low — not a fail, just lower than I'd like to see. No single component gave me a clean, readable fault. So now I've got a relay and wiring that's original to a fifteen-year-old installation, and one reading out of three that's a little off. Interviewer: What were you weighing at that point? Participant: Whether to just replace the relay and that wiring segment right there, using the marginal reading as my justification, or hold off and run more cycles to see if a real pattern showed up before committing to a replacement. Interviewer: What did you decide? Participant: I ran more cycles instead of replacing on the spot. One marginal reading against two normal ones didn't feel like enough to hang a full replacement on — it could've been the wiring starting to go, or it could've been a temporary moisture effect given the damp conditions. I gave it a fourth cycle after some extra drying time, and that one came back normal. Interviewer: Did that resolve it for you? Participant: Not entirely. It made the moisture explanation more plausible, but it didn't rule out the wiring either — a marginal insulation reading can come and go for more than one reason, so I still didn't have a clean answer. Interviewer: That brings us to the next call — what were the options once you had that pattern of readings? Participant: The gasket on the cabinet was showing some wear, and the marginal reading lined up with timing not long after that earlier rain. So I had a lower-cost option: dry everything out, clean the connections, reseal the case, and monitor. Or I could go straight to a full replacement of the wiring segment, which would take a lot longer and eat into overtime I'd need approval to extend. Interviewer: What tipped it for you? Participant: The timing with the rain was a real data point, not just a guess — it's a known failure mode on older cabinets with worn gaskets. That gave me a specific, testable explanation I hadn't ruled out yet, so trying the cheaper fix first and watching the results made sense to me before committing the extra hours to a full swap. Interviewer: How did that play out? Participant: Readings stayed stable through two more monitored cycles after the drying and resealing. Which was encouraging, but two clean cycles after a marginal one doesn't fully prove the wiring's fine — it's consistent with the fix working, and it's also consistent with the marginal reading just being a one-off that would've cleared up on its own. Interviewer: Last decision — putting the signal back in service. Participant: Right, by that point I had two stable cycles, the next scheduled movement was coming up, and I still didn't have a confirmed root cause — could've been the moisture issue resolved, could've been a quiet wiring problem that just hadn't shown itself again yet. My options were to restore automatic service on the strength of those two stable readings, or keep it under manual block protection for the rest of the shift and take another look in daylight. Interviewer: What did you go with, and why? Participant: I restored it to automatic service. Two consecutive normal readings after the interim fix was enough for me to move forward, and keeping manual protection running all night has its own cost — it ties up a dispatcher's attention and slows things down for every movement through there. But I did flag it for a follow-up inspection rather than calling it closed, because I knew I hadn't actually nailed down which explanation was right. Interviewer: Did it hold up? Participant: Yeah, ran clean through the rest of the shift. But I want to be clear, that doesn't tell me for certain I got the diagnosis right — it just means nothing happened on my watch that night. Interviewer: If that fourth test cycle had come back marginal again instead of normal, would you have done something different? Participant: Almost certainly, yeah. Two marginal readings out of four would've pushed me toward the full replacement instead of the interim fix — that's a different pattern than what I actually saw. Interviewer: And if you'd had open-ended overtime approval that night? Participant: Honestly, I might have leaned toward the full wiring replacement regardless, just to close the loop completely instead of leaving it on an interim fix. The time and approval limits were part of what made the cheaper option attractive. Interviewer: Looking back, is there anything you'd want more information on, even now? Participant: I'd still like a cleaner way to separate a moisture-related reading from an early-stage wiring issue on that generation of cabinet. Right now both look the same on my meter, and that's the part of this call I'm least settled on.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.88s · gen 67.44s · total 71.4s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0283 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0279 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0268 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0264 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0247 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
6. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0225 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0225 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0215 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
9. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0201 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0194 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0186 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
14. **Lyell Automation bias and verification complexity.pdf** — 0.0184 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
15. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
16. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0180 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0179 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
19. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0174 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0172 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
22. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0169 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0168 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0166 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0164 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
27. **Hallihan_etal_DTM_12.pdf** — 0.0160 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
28. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
30. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
34. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0154 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
36. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0151 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _# to Dangers from Humans speed, brute strength, sensory acuity, and apparent det allies to attac_
39. **Hallihan_etal_DTM_12.pdf** — 0.0149 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
41. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0146 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _### TER 33 | p ut forward by Kathryn Coe (2003) that art serves primarily to signal affiliation _
44. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0146 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
45. **Hallihan_etal_DTM_12.pdf** — 0.0145 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
46. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0144 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
47. **Hallihan_etal_DTM_12.pdf** — 0.0143 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
48. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0141 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
50. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0137 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analyzed the participant's retrospective reasoning during a signal-fault diagnostic and restoration sequence. No identified bias occurrences met the mechanism-first evidentiary threshold; one possible candidate is noted."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "expectation bias",
      "alternative_labels": [
        "expectancy bias",
        "confirmation bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Choosing the lower-cost moisture remediation over full wiring replacement after a fourth normal insulation reading",
      "supporting_interview_quote": "The timing with the rain was a real data point, not just a guess — it's a known failure mode on older cabinets with worn gaskets. That gave me a specific, testable explanation I hadn't ruled out yet, so trying the cheaper fix first and watching the results made sense to me before committing the extra hours to a full swap.",
      "plausible_mechanism": "The participant's pre-existing knowledge that rain and a worn gasket could cause moisture-related insulation changes may have made the moisture explanation more salient and acceptable when interpreting an ambiguous marginal reading. This could resemble expectancy or confirmation processes in which a contextual cue is weighted as supporting a favored situational hypothesis.",
      "why_not_identified": "The interview does not show selective search, resistance to disconfirming evidence, or dismissal of the alternative wiring-failure hypothesis. The participant explicitly stated that the marginal reading did not distinguish moisture from early-stage wiring degradation, ran additional cycles, and flagged the issue for follow-up. The decision was also framed as a lower-cost, monitorable intervention under operational constraints rather than a biased conviction."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "The transcript is a retrospective self-report, which may be rationalized or presented as more deliberative than the original reasoning.",
    "No objective normative benchmark or outcome data is available to compare the participant's diagnostic decisions against.",
    "Retrieved corpus passages were limited in diagnostic criteria and were not used to identify a bias occurrence.",
    "Absence of an identified bias does not mean the participant's reasoning was optimal or error-free."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. This is just a debrief for training purposes — we're looking at how you worked through the call, not grading the outcome. Okay to go ahead? Participant: Yeah, that's fine. Interviewer: Can you tell me your role and set the scene for that evening? Participant: I'm a signal maintainer covering the territory that includes the Marlow interlocking, out on the secondary main line. I got paged out in the evening after a track crew reported the signal dropping to a more restrictive aspect twice during their shift, then clearing back to normal on its own both times. It had rained earlier that day, so everything out there was still damp. My job was to figure out what was going on and get the signal back to reliable automatic operation before the next scheduled train movement, without stringing the possession out longer than it needed to be. Interviewer: Walk me through what you found and what you did first. Participant: When I got to the cabinet, there was no fault code logged at the interlocking — nothing tripped that would point me straight at a component. No history of this signal giving trouble before, either, so it wasn't a repeat offender. I did a visual first: no obvious damage, no standing water in the case, gasket looked a little worn but nothing dramatic. At that point I had two ways I could go. I could sit and watch the signal through another cycle or two to see if the drop repeated in a way I could actually observe, or I could go straight into bench testing the track circuit and relay to start ruling things in or out. Interviewer: Which way did you go? Participant: I went straight into testing. Waiting around for it to happen again felt like it could burn time I didn't have if the next train was going to need a clear signal, and testing gets me actual numbers instead of just watching and hoping it repeats on a schedule that suits me. Interviewer: How confident were you that testing first was the better call? Participant: Fairly confident, but I'll be honest, it wasn't a slam dunk either way. Watching it might've told me more about the actual pattern — whether it was tied to a specific type of train movement, say. But testing gets me hard numbers right away, and with the clock running, I leaned that way. Interviewer: What did the testing show? Participant: That's where it got murkier. I ran three insulation resistance cycles. Two came back within normal tolerance, one came back marginally low — not a fail, just lower than I'd like to see. No single component gave me a clean, readable fault. So now I've got a relay and wiring that's original to a fifteen-year-old installation, and one reading out of three that's a little off. Interviewer: What were you weighing at that point? Participant: Whether to just replace the relay and that wiring segment right there, using the marginal reading as my justification, or hold off and run more cycles to see if a real pattern showed up before committing to a replacement. Interviewer: What did you decide? Participant: I ran more cycles instead of replacing on the spot. One marginal reading against two normal ones didn't feel like enough to hang a full replacement on — it could've been the wiring starting to go, or it could've been a temporary moisture effect given the damp conditions. I gave it a fourth cycle after some extra drying time, and that one came back normal. Interviewer: Did that resolve it for you? Participant: Not entirely. It made the moisture explanation more plausible, but it didn't rule out the wiring either — a marginal insulation reading can come and go for more than one reason, so I still didn't have a clean answer. Interviewer: That brings us to the next call — what were the options once you had that pattern of readings? Participant: The gasket on the cabinet was showing some wear, and the marginal reading lined up with timing not long after that earlier rain. So I had a lower-cost option: dry everything out, clean the connections, reseal the case, and monitor. Or I could go straight to a full replacement of the wiring segment, which would take a lot longer and eat into overtime I'd need approval to extend. Interviewer: What tipped it for you? Participant: The timing with the rain was a real data point, not just a guess — it's a known failure mode on older cabinets with worn gaskets. That gave me a specific, testable explanation I hadn't ruled out yet, so trying the cheaper fix first and watching the results made sense to me before committing the extra hours to a full swap. Interviewer: How did that play out? Participant: Readings stayed stable through two more monitored cycles after the drying and resealing. Which was encouraging, but two clean cycles after a marginal one doesn't fully prove the wiring's fine — it's consistent with the fix working, and it's also consistent with the marginal reading just being a one-off that would've cleared up on its own. Interviewer: Last decision — putting the signal back in service. Participant: Right, by that point I had two stable cycles, the next scheduled movement was coming up, and I still didn't have a confirmed root cause — could've been the moisture issue resolved, could've been a quiet wiring problem that just hadn't shown itself again yet. My options were to restore automatic service on the strength of those two stable readings, or keep it under manual block protection for the rest of the shift and take another look in daylight. Interviewer: What did you go with, and why? Participant: I restored it to automatic service. Two consecutive normal readings after the interim fix was enough for me to move forward, and keeping manual protection running all night has its own cost — it ties up a dispatcher's attention and slows things down for every movement through there. But I did flag it for a follow-up inspection rather than calling it closed, because I knew I hadn't actually nailed down which explanation was right. Interviewer: Did it hold up? Participant: Yeah, ran clean through the rest of the shift. But I want to be clear, that doesn't tell me for certain I got the diagnosis right — it just means nothing happened on my watch that night. Interviewer: If that fourth test cycle had come back marginal again instead of normal, would you have done something different? Participant: Almost certainly, yeah. Two marginal readings out of four would've pushed me toward the full replacement instead of the interim fix — that's a different pattern than what I actually saw. Interviewer: And if you'd had open-ended overtime approval that night? Participant: Honestly, I might have leaned toward the full wiring replacement regardless, just to close the loop completely instead of leaving it on an interim fix. The time and approval limits were part of what made the cheaper option attractive. Interviewer: Looking back, is there anything you'd want more information on, even now? Participant: I'd still like a cleaner way to separate a moisture-related reading from an early-stage wiring issue on that generation of cabinet. Right now both look the same on my meter, and that's the part of this call I'm least settled on.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.71s · gen 91.21s · total 95.0s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0283 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0279 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0268 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0264 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0247 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
6. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0225 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0225 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0215 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
9. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0201 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0194 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0186 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
14. **Lyell Automation bias and verification complexity.pdf** — 0.0184 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
15. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
16. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0180 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0179 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
19. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0174 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0172 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
22. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0169 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0168 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0166 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0164 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
27. **Hallihan_etal_DTM_12.pdf** — 0.0160 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
28. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
30. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
34. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0154 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
36. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0151 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _# to Dangers from Humans speed, brute strength, sensory acuity, and apparent det allies to attac_
39. **Hallihan_etal_DTM_12.pdf** — 0.0149 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
41. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0146 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _### TER 33 | p ut forward by Kathryn Coe (2003) that art serves primarily to signal affiliation _
44. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0146 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
45. **Hallihan_etal_DTM_12.pdf** — 0.0145 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
46. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0144 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
47. **Hallihan_etal_DTM_12.pdf** — 0.0143 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
48. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0141 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
50. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0137 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Mechanism-first review of a signal maintainer debrief covering diagnostic testing, interim repair, and restoration decisions. Operational constraints and explicit uncertainty management were not treated as bias unless a distinct bias-specific mechanism was affirmatively evidenced."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Action bias",
      "alternative_labels": ["bias for action"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Choosing immediate bench testing over passive observation",
      "supporting_interview_quote": "I went straight into testing. Waiting around for it to happen again felt like it could burn time I didn't have if the next train was going to need a clear signal, and testing gets me actual numbers instead of just watching and hoping it repeats on a schedule that suits me.",
      "plausible_mechanism": "A motivational tendency to prefer active intervention over waiting under uncertainty, possibly to reduce discomfort or feel that progress is being made.",
      "why_not_identified": "The transcript shows an explicit time-pressure and information-value rationale, and the participant later acknowledges that watching could have been informative; there is insufficient affirmative evidence that an affect- or motivation-driven action preference outweighed a clearly superior waiting strategy."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": ["get-there-itis"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Restoring automatic service despite unresolved root cause",
      "supporting_interview_quote": "I restored it to automatic service. Two consecutive normal readings after the interim fix was enough for me to move forward, and keeping manual protection running all night has its own cost — it ties up a dispatcher's attention and slows things down for every movement through there.",
      "plausible_mechanism": "A tendency to continue with the planned restoration and scheduled movement despite unresolved causal uncertainty and a recent marginal reading.",
      "why_not_identified": "The decision is presented as an explicit cost-benefit trade-off with a follow-up inspection and clear acknowledgment that the root cause was not confirmed; the transcript does not provide affirmative evidence of a bias-specific plan-adherence mechanism."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "Retrieved corpus passages were largely from aviation and automation domains and offered limited direct support for rail maintenance diagnostic reasoning.",
    "The analysis is based on a retrospective self-report debrief, which may not fully capture automatic or implicit cognitive processes present during the live decision events."
  ]
}

