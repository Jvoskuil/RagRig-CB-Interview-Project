# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a cognitive task analysis study, not for any evaluation of your performance or record. You can decline to answer anything. Are you okay to proceed? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you tell me your role and what your responsibilities were that night? Participant: I was the Battle Captain on the night shift at the JOC, so I'm the watch officer responsible for the common operational picture, coordinating sensor and ISR tasking, and making the call on escalation — QRF alerts, higher headquarters notifications, that kind of thing. That night we were short an intel analyst, so the S2 shop was thinner than usual, and we only had one UAV available for the whole sector. Interviewer: Walk me through what happened, starting from the first indication something was off. Participant: Around 0215 a perimeter sensor near NAI-7, up on the northern boundary, logged a motion alert. Single sensor, no visual confirmation, and the weather that night — some ground fog — was already degrading sensor reliability. We didn't have any HUMINT or SIGINT corroborating it yet. Normally that's the kind of thing you'd log and keep an eye on. But I'll be honest, that specific sensor and that specific stretch of perimeter rang a bell for me. About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away. Interviewer: What exactly about the current alert reminded you of that earlier incident? Participant: Mostly the location and the hour. Both around 0200, both NAI-7. I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way. Interviewer: Okay. What happened next? Participant: I had the S2 analyst start pulling historical activity for the sector while I looked at tasking the UAV. That's where things got tight, because we only had the one asset and there were competing requests elsewhere in the sector that night. Interviewer: Let's stay on that first call for a second — classifying the alert as elevated. What alternatives did you consider? Participant: I could've left it routine and waited for more data, or reached out to the adjacent unit for corroboration before deciding priority. Comms with them were spotty that night, intermittent SATCOM, so that would've cost time. I went with elevating it based on what I already knew. Interviewer: How confident were you in that classification at the time? Participant: Moderately. I didn't have hard evidence, just the pattern match in my head to the earlier event. Interviewer: Understood. So then you moved to the ISR tasking decision — walk me through that. Participant: Right, with only one UAV, I had to justify diverting it to NAI-7 over the other requests. To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first. Interviewer: Were there other sources you could have checked? Participant: Sure, there's the adjacent-unit SIGACT log and a sector-wide pattern-of-life database that tracks things like livestock movement and civilian traffic patterns near the perimeter. Both were accessible that night despite the comms issue — the pattern-of-life database is stored locally, actually. Interviewer: Did you look at those before tasking the UAV? Participant: No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later. Interviewer: What made you stick with just the own-sector feed? Participant: Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes. Interviewer: What did the UAV feed show once it arrived on station? Participant: Ambiguous thermal signatures. Could've been a small dismounted element, could've been livestock — genuinely hard to tell from the imagery alone. No weapons visible, no confirmed hostile indicators. Interviewer: What did you do with that information? Participant: I put the QRF on 15-minute alert status. Interviewer: What alternatives were on the table at that point? Participant: I could've held the current posture and requested more UAV dwell time to get a clearer picture, or asked the adjacent unit to send a ground patrol to verify visually before touching QRF readiness at all. Interviewer: What tipped you toward alerting QRF instead of those options? Participant: We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time. Interviewer: Did the thermal evidence itself favor the ambush interpretation over livestock? Participant: Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other. Interviewer: What happened after QRF went to alert status? Participant: Additional analyst review came back later and assessed the signatures as most consistent with livestock movement, based on movement speed and clustering patterns. QRF was never launched, just held at readiness. Interviewer: How did you handle the final reporting for shift change? Participant: I wrote it up as a genuinely mixed picture — noted the initial elevation, the QRF alert, and then the follow-up analyst assessment leaning non-hostile. I didn't want to call it a clean false alarm because the imagery was ambiguous enough that I couldn't rule out the dismounted-element read. I also didn't want to overstate it as an ongoing threat given what the analyst found. Higher headquarters ended up asking for a follow-up clarification the next day, which is pretty normal for anything left open like that. Interviewer: Was there a point where you considered recommending a sensor review for NAI-7 instead? Participant: I mentioned it as a secondary note, since that spot generates a fair number of ambiguous alerts, but I didn't want to bury the main SITREP under an infrastructure recommendation when the operational question was still open. Interviewer: Stepping back — if the alert had come in during a quiet stretch with no recent similar incident in your memory, do you think you'd have classified it the same way? Participant: Probably not as quickly to elevated. I think I'd have waited for the S2 pull before deciding priority. Interviewer: If you'd checked the adjacent-unit and pattern-of-life data first, before your own-sector feed, do you think the tasking decision changes? Participant: The UAV probably still goes to NAI-7 — that part of the call felt justified regardless. But I think how I framed the justification would've been different, maybe more grounded in actual cross-referenced history instead of just what was in front of me. Interviewer: And if you hadn't run that ambush rehearsal in training recently, would you have read the thermal imagery differently? Participant: Yeah, I think so. Without that scenario fresh in my head, I might have leaned toward requesting more dwell time instead of alerting QRF right away, since the imagery on its own really didn't point clearly either way. Interviewer: Last question — looking back with everything you know now, what would you change? Participant: Honestly, probably slow down at each of those first three points and force myself to check the wider data before trusting my first read. None of the individual calls were unreasonable given what I had in front of me, but I can see now where I leaned on what came to mind fastest instead of what was actually available. Interviewer: That's really helpful. Thanks for walking through it in that much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.34s · gen 378.11s · total 384.2s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0265 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0256 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0248 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0241 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
5. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0225 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0206 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0205 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0197 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0196 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0195 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0187 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0169 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0165 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0164 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Lyell Automation bias and verification complexity.pdf** — 0.0161 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
26. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0158 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _## 16 5 Accidents & incidents Observed Expected The results of the chi 5.76 , p = .01 . The resu_
28. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
32. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
33. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
35. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0150 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0148 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration complacency? Three_
41. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
42. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0147 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
43. **Hallihan_etal_DTM_12.pdf** — 0.0147 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
45. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0144 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
47. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
48. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - an earlier obser_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Blind review of a single CTA interview for affirmatively evidenced cognitive biases. The transcript was treated as the primary evidence; retrieved passages were used only to supply or validate labels and mechanisms where available."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "expectation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "simulation heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "expectation bias",
      "alternative_labels": [
        "expectancy bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for prior experience and expected patterns to shape interpretation of new ambiguous information, so that the information is processed as more consistent with the expected event than the evidence alone would support.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial priority classification of NAI-7 perimeter sensor alert",
      "decision_point_description": "Whether to leave the 0215 single-sensor motion alert at routine priority or elevate it in the common operational picture before corroborating data arrived.",
      "affected_reasoning_operation": "Threat classification and prioritization under uncertainty",
      "bias_specific_mechanism": "A real infiltration attempt five weeks earlier at the same location and similar time made the current ambiguous sensor alert feel like a repetition. The participant matched on salient surface features, especially location and hour, and did not retrieve or compare the prior event's actual signature data before elevating priority.",
      "manifestation_in_interview": "The participant elevated the NAI-7 sensor alert to elevated priority almost immediately after stating that it reminded him of the prior real infiltration attempt, even though the current alert was from a single sensor, lacked visual confirmation, and had no HUMINT or SIGINT corroboration.",
      "effect_on_reasoning_or_decision": "The alert was assigned elevated priority in the common operational picture despite being an ambiguous single-sensor activation with degraded sensor reliability and no corroborating intelligence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away.",
          "evidence_explanation": "This shows the participant used the earlier incident as the primary basis for elevating priority, explicitly describing a gut-level pattern match to a prior real event."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way.",
          "evidence_explanation": "This demonstrates that the classification was not based on a systematic comparison of diagnostic sensor data, but on the subjective feeling that the current ambiguous alert was the same as the remembered event."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that the sensor was already degraded by ground fog and that there was no HUMINT or SIGINT corroboration at the time. He also later indicated that without the recent similar incident he probably would have waited for the S2 pull before deciding priority. No immediate debiasing occurred before the initial elevation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved O'Connor paper identifies expectation as a common operational cognitive bias, though it does not provide a formal mechanism definition. The mechanism description above therefore also draws on general cognitive-science knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "The retrieved discussion identifies confirmation, expectation, and plan continuation as common cognitive bias types in operational reports, and highlights an apparent false sense of normality created by cognitive bias.",
          "mechanism_supported_by_source": "The source supports expectation as a recurrent cognitive bias in operational decision-making and is consistent with the participant's expectation-driven pattern matching to the earlier infiltration attempt.",
          "relevance_to_this_occurrence": "The participant's prior real infiltration created an expectation that a same-location, same-time sensor alert was again a real infiltration, leading to elevated classification before corroborating signature data was obtained."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely on information that is most easily brought to mind or most immediately accessible as the primary basis for judgment, even when other relevant information is available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "ISR source selection and UAV tasking justification",
      "decision_point_description": "Which available information sources to consult before tasking the sole UAV to NAI-7.",
      "affected_reasoning_operation": "Information search and selection in support of an ISR asset allocation decision",
      "bias_specific_mechanism": "The participant defaulted to the own-sector SIGINT feed because it was habitually open and fast to check. He did not consult the accessible adjacent-unit SIGACT log or the locally stored pattern-of-life database before tasking the UAV. The decision was therefore driven by the ease of access and retrieval of the own-sector feed rather than by a systematic search across all relevant available repositories.",
      "manifestation_in_interview": "The participant used only own-sector summaries to make the UAV tasking call and did not look at the adjacent-unit log or pattern-of-life database, despite acknowledging both were accessible that night and the pattern-of-life database would have taken only about five extra minutes.",
      "effect_on_reasoning_or_decision": "The UAV tasking justification was built on a narrow, habitually accessible information set, omitting relevant adjacent-unit and local pattern-of-life data that later proved relevant.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first.",
          "evidence_explanation": "This shows the source selection was driven by what was habitually available and immediately accessible on his terminal, rather than by a diagnostic assessment of which sources were most relevant."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later.",
          "evidence_explanation": "This confirms that relevant accessible sources were not consulted and that the decision was made on the basis of the immediately available own-sector feed."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes.",
          "evidence_explanation": "This attributes the restricted search to habit and speed, and explicitly acknowledges that a locally accessible relevant source would not have required a large additional effort."
        }
      ],
      "correction_or_counterevidence": "Time pressure and the shift-change SITREP were real constraints, and the participant judged that the UAV likely would still have gone to NAI-7 even with broader data. However, he explicitly framed the shortcut as habit and as relying on what came to mind fastest, rather than as a deliberate, optimized resource-rational tradeoff. The pattern-of-life database was locally accessible and would have taken only about five minutes to consult.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage supplied a definition or mechanism for the availability heuristic; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "simulation heuristic",
      "alternative_labels": [
        "simulation bias",
        "imaginability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the probability or plausibility of an event by the ease with which a detailed scenario can be mentally simulated or imagined, rather than by the diagnostic value of the available evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "QRF readiness decision after ambiguous UAV thermal imagery",
      "decision_point_description": "Whether to hold current posture, request more dwell time or ground patrol verification, or place QRF on 15-minute alert status.",
      "affected_reasoning_operation": "Interpretation of ambiguous sensor imagery and escalation judgment",
      "bias_specific_mechanism": "A recent training exercise rehearsed a small-unit ambush approaching through similar thermal-masking terrain, making that scenario easy to imagine in detailed, step-by-step form. The participant treated this vivid mental simulation as evidence of plausibility even though the thermal signatures were equally consistent with a benign livestock explanation.",
      "manifestation_in_interview": "The participant placed QRF on 15-minute alert after stating that the thermal evidence did not favor ambush over livestock. The escalation was driven by the vivid, step-by-step ambush scenario from recent training rather than by diagnostic differences in the imagery.",
      "effect_on_reasoning_or_decision": "QRF readiness was escalated despite ambiguous imagery and an explicit judgment that the evidence was equally consistent with a non-hostile explanation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Ambiguous thermal signatures. Could've been a small dismounted element, could've been livestock — genuinely hard to tell from the imagery alone. No weapons visible, no confirmed hostile indicators.",
          "evidence_explanation": "This establishes that the available imagery was diagnostically ambiguous and did not favor either the hostile or benign interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time.",
          "evidence_explanation": "This attributes the QRF alert decision to the ease and vividness with which the participant could mentally simulate the rehearsed ambush scenario, not to direct evidence in the thermal imagery."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other.",
          "evidence_explanation": "This explicitly contrasts the diagnostic equality of the two explanations with the difference in mental-simulation vividness, which is the mechanism of the simulation heuristic."
        }
      ],
      "correction_or_counterevidence": "Subsequent analyst review assessed the thermal signatures as most consistent with livestock movement based on movement speed and clustering patterns. QRF was never launched, only held at readiness. The participant also acknowledged that without the recent training scenario he might have requested more dwell time instead of alerting QRF right away.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage supplied a definition or mechanism for the simulation heuristic; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "selective exposure"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "ISR source selection and UAV tasking justification",
      "supporting_interview_quote": "To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first.",
      "plausible_mechanism": "The participant may have engaged in selective exposure to a familiar own-sector feed that was more likely to support the already-elevated threat classification, while avoiding adjacent-unit or pattern-of-life data that could have disconfirmed the threat narrative.",
      "why_not_identified": "The transcript attributes the source choice primarily to habit, speed, and perceived time pressure rather than to an active effort to preserve or confirm a preferred hypothesis. The availability heuristic provides a more direct mechanism with clearer transcript support."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial priority classification of NAI-7 perimeter sensor alert",
      "supporting_interview_quote": "About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away.",
      "plausible_mechanism": "The prior real infiltration may have served as an initial threat estimate or anchor, and the participant's subsequent classification may reflect insufficient adjustment from that anchor to the current degraded-sensor, no-corroboration, ambiguous condition.",
      "why_not_identified": "The transcript does not indicate an explicit numeric or baseline estimate being adjusted. The participant describes pattern matching and expectation rather than anchoring-and-adjustment, so expectation bias better captures the manifested mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a retrospective self-report, so some causal attributions about the participant's reasoning may include post-hoc reflection rather than purely contemporaneous process tracing.",
    "The supplied retrieval corpus contained only sparse extracted text and did not provide formal definitions for all identified labels, particularly the availability and simulation heuristics.",
    "The analysis does not evaluate whether the participant's operational decisions would have differed under a normatively optimal information search, only whether a bias-specific mechanism was affirmatively evidenced in the transcript."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a cognitive task analysis study, not for any evaluation of your performance or record. You can decline to answer anything. Are you okay to proceed? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you tell me your role and what your responsibilities were that night? Participant: I was the Battle Captain on the night shift at the JOC, so I'm the watch officer responsible for the common operational picture, coordinating sensor and ISR tasking, and making the call on escalation — QRF alerts, higher headquarters notifications, that kind of thing. That night we were short an intel analyst, so the S2 shop was thinner than usual, and we only had one UAV available for the whole sector. Interviewer: Walk me through what happened, starting from the first indication something was off. Participant: Around 0215 a perimeter sensor near NAI-7, up on the northern boundary, logged a motion alert. Single sensor, no visual confirmation, and the weather that night — some ground fog — was already degrading sensor reliability. We didn't have any HUMINT or SIGINT corroborating it yet. Normally that's the kind of thing you'd log and keep an eye on. But I'll be honest, that specific sensor and that specific stretch of perimeter rang a bell for me. About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away. Interviewer: What exactly about the current alert reminded you of that earlier incident? Participant: Mostly the location and the hour. Both around 0200, both NAI-7. I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way. Interviewer: Okay. What happened next? Participant: I had the S2 analyst start pulling historical activity for the sector while I looked at tasking the UAV. That's where things got tight, because we only had the one asset and there were competing requests elsewhere in the sector that night. Interviewer: Let's stay on that first call for a second — classifying the alert as elevated. What alternatives did you consider? Participant: I could've left it routine and waited for more data, or reached out to the adjacent unit for corroboration before deciding priority. Comms with them were spotty that night, intermittent SATCOM, so that would've cost time. I went with elevating it based on what I already knew. Interviewer: How confident were you in that classification at the time? Participant: Moderately. I didn't have hard evidence, just the pattern match in my head to the earlier event. Interviewer: Understood. So then you moved to the ISR tasking decision — walk me through that. Participant: Right, with only one UAV, I had to justify diverting it to NAI-7 over the other requests. To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first. Interviewer: Were there other sources you could have checked? Participant: Sure, there's the adjacent-unit SIGACT log and a sector-wide pattern-of-life database that tracks things like livestock movement and civilian traffic patterns near the perimeter. Both were accessible that night despite the comms issue — the pattern-of-life database is stored locally, actually. Interviewer: Did you look at those before tasking the UAV? Participant: No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later. Interviewer: What made you stick with just the own-sector feed? Participant: Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes. Interviewer: What did the UAV feed show once it arrived on station? Participant: Ambiguous thermal signatures. Could've been a small dismounted element, could've been livestock — genuinely hard to tell from the imagery alone. No weapons visible, no confirmed hostile indicators. Interviewer: What did you do with that information? Participant: I put the QRF on 15-minute alert status. Interviewer: What alternatives were on the table at that point? Participant: I could've held the current posture and requested more UAV dwell time to get a clearer picture, or asked the adjacent unit to send a ground patrol to verify visually before touching QRF readiness at all. Interviewer: What tipped you toward alerting QRF instead of those options? Participant: We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time. Interviewer: Did the thermal evidence itself favor the ambush interpretation over livestock? Participant: Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other. Interviewer: What happened after QRF went to alert status? Participant: Additional analyst review came back later and assessed the signatures as most consistent with livestock movement, based on movement speed and clustering patterns. QRF was never launched, just held at readiness. Interviewer: How did you handle the final reporting for shift change? Participant: I wrote it up as a genuinely mixed picture — noted the initial elevation, the QRF alert, and then the follow-up analyst assessment leaning non-hostile. I didn't want to call it a clean false alarm because the imagery was ambiguous enough that I couldn't rule out the dismounted-element read. I also didn't want to overstate it as an ongoing threat given what the analyst found. Higher headquarters ended up asking for a follow-up clarification the next day, which is pretty normal for anything left open like that. Interviewer: Was there a point where you considered recommending a sensor review for NAI-7 instead? Participant: I mentioned it as a secondary note, since that spot generates a fair number of ambiguous alerts, but I didn't want to bury the main SITREP under an infrastructure recommendation when the operational question was still open. Interviewer: Stepping back — if the alert had come in during a quiet stretch with no recent similar incident in your memory, do you think you'd have classified it the same way? Participant: Probably not as quickly to elevated. I think I'd have waited for the S2 pull before deciding priority. Interviewer: If you'd checked the adjacent-unit and pattern-of-life data first, before your own-sector feed, do you think the tasking decision changes? Participant: The UAV probably still goes to NAI-7 — that part of the call felt justified regardless. But I think how I framed the justification would've been different, maybe more grounded in actual cross-referenced history instead of just what was in front of me. Interviewer: And if you hadn't run that ambush rehearsal in training recently, would you have read the thermal imagery differently? Participant: Yeah, I think so. Without that scenario fresh in my head, I might have leaned toward requesting more dwell time instead of alerting QRF right away, since the imagery on its own really didn't point clearly either way. Interviewer: Last question — looking back with everything you know now, what would you change? Participant: Honestly, probably slow down at each of those first three points and force myself to check the wider data before trusting my first read. None of the individual calls were unreasonable given what I had in front of me, but I can see now where I leaned on what came to mind fastest instead of what was actually available. Interviewer: That's really helpful. Thanks for walking through it in that much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.42s · gen 375.26s · total 381.2s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0265 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0256 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0248 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0241 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
5. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0225 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0206 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0205 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0197 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0196 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0195 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0187 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0169 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0165 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0164 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Lyell Automation bias and verification complexity.pdf** — 0.0161 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
26. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0158 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _## 16 5 Accidents & incidents Observed Expected The results of the chi 5.76 , p = .01 . The resu_
28. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
32. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
33. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
35. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0150 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0148 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration complacency? Three_
41. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
42. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0147 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
43. **Hallihan_etal_DTM_12.pdf** — 0.0147 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
45. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0144 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
47. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
48. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - an earlier obser_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis of a single post hoc interview transcript for cognitive bias mechanisms in the participant's reasoning and decisions, not an evaluation of outcome correctness."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Representativeness heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Simulation heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": ["Representativeness bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the probability or classification of an event by how much it resembles a familiar case or prototype, often without sufficiently comparing diagnostic evidence or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Classification of NAI-7 motion alert as elevated priority",
      "decision_point_description": "Deciding whether to treat the NAI-7 perimeter motion alert as routine or elevated priority.",
      "affected_reasoning_operation": "Threat classification and probability judgment",
      "bias_specific_mechanism": "The participant treated a superficial match with a prior infiltration incident, same sensor and same approximate time, as diagnostic of the current event being a similar threat, without pulling and comparing the prior event's actual signature data or waiting for corroboration.",
      "manifestation_in_interview": "He stated that the current alert 'looks like' the prior real infiltration and that he elevated priority even though he had not compared sensor duration, movement pattern, or other signature data.",
      "effect_on_reasoning_or_decision": "The alert was bumped to elevated priority in the common operational picture immediately, which shaped the subsequent ISR tasking and QRF decisions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away.",
          "evidence_explanation": "This shows a similarity-based judgment using the earlier infiltration as a prototype for the current alert."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the location and the hour. Both around 0200, both NAI-7. I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way.",
          "evidence_explanation": "He explicitly relied on surface resemblance rather than comparing diagnostic event signatures, which is the core representativeness mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as quickly to elevated. I think I'd have waited for the S2 pull before deciding priority.",
          "evidence_explanation": "The counterfactual supports that the availability of a similar prior case facilitated the resemblance-based classification rather than evidence-based assessment alone."
        }
      ],
      "correction_or_counterevidence": "A real infiltration had previously occurred in the same area at a similar time, so surface similarity had some diagnostic value. The participant acknowledged only moderate confidence and no hard evidence. Later analyst review of the subsequent thermal signature suggested a non-hostile explanation, and the participant ultimately reported a mixed picture.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label and mechanism are drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Status quo bias",
      "alternative_labels": ["Default bias", "Status quo heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for the current or habitually used option or process over alternatives, even when alternatives may provide relevant additional information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of information sources to justify ISR tasking",
      "decision_point_description": "Deciding which information repositories to consult before tasking the only UAV to NAI-7.",
      "affected_reasoning_operation": "Information acquisition and source selection",
      "bias_specific_mechanism": "The participant relied on the information source he habitually used and had open on his terminal, the own-sector SIGINT summaries, rather than systematically considering other accessible sources such as the adjacent-unit SIGACT log or the locally stored pattern-of-life database.",
      "manifestation_in_interview": "He checked the own-sector feed by default and did not examine the adjacent-unit log or pattern-of-life database before tasking the UAV, explaining that it was habit and that he did not feel he had time.",
      "effect_on_reasoning_or_decision": "The UAV was tasked toward NAI-7 based on an incomplete cross-referenced picture, and the participant later acknowledged that the justification would have been more grounded if broader data had been checked.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first.",
          "evidence_explanation": "This indicates that the habitual, default information source was selected rather than a deliberate comparison of available sources."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later.",
          "evidence_explanation": "He confirms that he did not consult another relevant source before acting, and that the unconsulted source contained relevant history."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes.",
          "evidence_explanation": "This shows the default/habitual practice carried the decision, even though a more informative alternative was accessible at low cost."
        }
      ],
      "correction_or_counterevidence": "The participant believed the UAV would likely have gone to NAI-7 regardless, and time pressure from the shift-change SITREP was real. Using the own-sector feed was fast and familiar, and the decision may still have been justified on the available information.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label and mechanism are drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Simulation heuristic",
      "alternative_labels": ["Vividness heuristic", "Availability heuristic via imaginability"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood of an event by the ease or vividness with which a possible scenario can be mentally simulated or imagined.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of ambiguous UAV thermal imagery and QRF alert decision",
      "decision_point_description": "Deciding among holding current posture, requesting more UAV dwell time, requesting ground patrol verification, or placing QRF on 15-minute alert.",
      "affected_reasoning_operation": "Interpretation of ambiguous imagery and response selection",
      "bias_specific_mechanism": "The participant used the vividness and ease of mentally replaying a recently rehearsed ambush scenario as a cue to the likelihood of that interpretation, even though the thermal evidence was equally consistent with livestock movement.",
      "manifestation_in_interview": "He described being able to picture the rehearsed ambush scenario 'step by step' and said the livestock explanation lacked that same vividness, which pushed him toward alerting QRF.",
      "effect_on_reasoning_or_decision": "He placed the QRF on 15-minute alert rather than requesting more dwell time or ground verification, despite the imagery being ambiguous.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time.",
          "evidence_explanation": "The vivid mental simulation of the trained ambush scenario directly shaped the QRF decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other.",
          "evidence_explanation": "He explicitly acknowledges that the evidence did not favor the ambush interpretation, but that the differential vividness of the simulated scenario drove his judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without that scenario fresh in my head, I might have leaned toward requesting more dwell time instead of alerting QRF right away, since the imagery on its own really didn't point clearly either way.",
          "evidence_explanation": "The counterfactual reinforces that the trained scenario, not the imagery itself, influenced the QRF alert decision."
        }
      ],
      "correction_or_counterevidence": "The thermal signatures were genuinely ambiguous and consistent with a small dismounted element, so raising QRF readiness was a precautionary action rather than a launch. Later analyst review assessed the signatures as most consistent with livestock movement, and the participant reported this mixed picture.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label and mechanism are drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved scientific-passage corpus did not contain adequate definitions or supporting passages for representativeness heuristic, status quo bias, or simulation heuristic, so those labels derive from general cognitive-science knowledge.",
    "The analysis relies on a single self-reported interview and counterfactual reflections, which may themselves be influenced by hindsight or social desirability.",
    "Some decisions occurred under operational time pressure and uncertainty, so bias attribution is probabilistic rather than definitive.",
    "No objective normative benchmark or experimental condition was available from the transcript alone."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a cognitive task analysis study, not for any evaluation of your performance or record. You can decline to answer anything. Are you okay to proceed? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you tell me your role and what your responsibilities were that night? Participant: I was the Battle Captain on the night shift at the JOC, so I'm the watch officer responsible for the common operational picture, coordinating sensor and ISR tasking, and making the call on escalation — QRF alerts, higher headquarters notifications, that kind of thing. That night we were short an intel analyst, so the S2 shop was thinner than usual, and we only had one UAV available for the whole sector. Interviewer: Walk me through what happened, starting from the first indication something was off. Participant: Around 0215 a perimeter sensor near NAI-7, up on the northern boundary, logged a motion alert. Single sensor, no visual confirmation, and the weather that night — some ground fog — was already degrading sensor reliability. We didn't have any HUMINT or SIGINT corroborating it yet. Normally that's the kind of thing you'd log and keep an eye on. But I'll be honest, that specific sensor and that specific stretch of perimeter rang a bell for me. About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away. Interviewer: What exactly about the current alert reminded you of that earlier incident? Participant: Mostly the location and the hour. Both around 0200, both NAI-7. I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way. Interviewer: Okay. What happened next? Participant: I had the S2 analyst start pulling historical activity for the sector while I looked at tasking the UAV. That's where things got tight, because we only had the one asset and there were competing requests elsewhere in the sector that night. Interviewer: Let's stay on that first call for a second — classifying the alert as elevated. What alternatives did you consider? Participant: I could've left it routine and waited for more data, or reached out to the adjacent unit for corroboration before deciding priority. Comms with them were spotty that night, intermittent SATCOM, so that would've cost time. I went with elevating it based on what I already knew. Interviewer: How confident were you in that classification at the time? Participant: Moderately. I didn't have hard evidence, just the pattern match in my head to the earlier event. Interviewer: Understood. So then you moved to the ISR tasking decision — walk me through that. Participant: Right, with only one UAV, I had to justify diverting it to NAI-7 over the other requests. To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first. Interviewer: Were there other sources you could have checked? Participant: Sure, there's the adjacent-unit SIGACT log and a sector-wide pattern-of-life database that tracks things like livestock movement and civilian traffic patterns near the perimeter. Both were accessible that night despite the comms issue — the pattern-of-life database is stored locally, actually. Interviewer: Did you look at those before tasking the UAV? Participant: No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later. Interviewer: What made you stick with just the own-sector feed? Participant: Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes. Interviewer: What did the UAV feed show once it arrived on station? Participant: Ambiguous thermal signatures. Could've been a small dismounted element, could've been livestock — genuinely hard to tell from the imagery alone. No weapons visible, no confirmed hostile indicators. Interviewer: What did you do with that information? Participant: I put the QRF on 15-minute alert status. Interviewer: What alternatives were on the table at that point? Participant: I could've held the current posture and requested more UAV dwell time to get a clearer picture, or asked the adjacent unit to send a ground patrol to verify visually before touching QRF readiness at all. Interviewer: What tipped you toward alerting QRF instead of those options? Participant: We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time. Interviewer: Did the thermal evidence itself favor the ambush interpretation over livestock? Participant: Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other. Interviewer: What happened after QRF went to alert status? Participant: Additional analyst review came back later and assessed the signatures as most consistent with livestock movement, based on movement speed and clustering patterns. QRF was never launched, just held at readiness. Interviewer: How did you handle the final reporting for shift change? Participant: I wrote it up as a genuinely mixed picture — noted the initial elevation, the QRF alert, and then the follow-up analyst assessment leaning non-hostile. I didn't want to call it a clean false alarm because the imagery was ambiguous enough that I couldn't rule out the dismounted-element read. I also didn't want to overstate it as an ongoing threat given what the analyst found. Higher headquarters ended up asking for a follow-up clarification the next day, which is pretty normal for anything left open like that. Interviewer: Was there a point where you considered recommending a sensor review for NAI-7 instead? Participant: I mentioned it as a secondary note, since that spot generates a fair number of ambiguous alerts, but I didn't want to bury the main SITREP under an infrastructure recommendation when the operational question was still open. Interviewer: Stepping back — if the alert had come in during a quiet stretch with no recent similar incident in your memory, do you think you'd have classified it the same way? Participant: Probably not as quickly to elevated. I think I'd have waited for the S2 pull before deciding priority. Interviewer: If you'd checked the adjacent-unit and pattern-of-life data first, before your own-sector feed, do you think the tasking decision changes? Participant: The UAV probably still goes to NAI-7 — that part of the call felt justified regardless. But I think how I framed the justification would've been different, maybe more grounded in actual cross-referenced history instead of just what was in front of me. Interviewer: And if you hadn't run that ambush rehearsal in training recently, would you have read the thermal imagery differently? Participant: Yeah, I think so. Without that scenario fresh in my head, I might have leaned toward requesting more dwell time instead of alerting QRF right away, since the imagery on its own really didn't point clearly either way. Interviewer: Last question — looking back with everything you know now, what would you change? Participant: Honestly, probably slow down at each of those first three points and force myself to check the wider data before trusting my first read. None of the individual calls were unreasonable given what I had in front of me, but I can see now where I leaned on what came to mind fastest instead of what was actually available. Interviewer: That's really helpful. Thanks for walking through it in that much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.51s · gen 439.97s · total 446.0s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0265 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0256 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0248 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0241 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
5. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0225 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0206 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0205 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0197 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0196 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0195 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0187 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0169 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0165 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0164 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Lyell Automation bias and verification complexity.pdf** — 0.0161 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
26. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0158 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _## 16 5 Accidents & incidents Observed Expected The results of the chi 5.76 , p = .01 . The resu_
28. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
32. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
33. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
35. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0150 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0148 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration complacency? Three_
41. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
42. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0147 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
43. **Hallihan_etal_DTM_12.pdf** — 0.0147 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
45. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0144 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
47. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
48. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - an earlier obser_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of the CTA transcript. No experimental condition or intended bias count was inferred. Retrieved passages were used only for conceptual grounding; transcript evidence determines whether a bias occurred."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
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
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias",
        "similarity-based judgment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood or classification of an event by superficial similarity to a previously observed or remembered instance, while underweighting diagnostic evidence and base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial sensor alert classification at NAI-7",
      "decision_point_description": "At 0215, deciding whether to treat a single unconfirmed perimeter sensor alert as routine or elevated.",
      "affected_reasoning_operation": "Classification and priority judgment under uncertainty",
      "bias_specific_mechanism": "The current alert matched the prior infiltration on two superficial features, location and time. The participant treated that resemblance as diagnostic and elevated priority without comparing actual signature data or requiring corroboration.",
      "manifestation_in_interview": "The participant said the alert 'rang a bell' and that his gut said the situation looked like the earlier infiltration, then bumped it to elevated priority in the COP before obtaining hard evidence.",
      "effect_on_reasoning_or_decision": "The single unconfirmed sensor alert was escalated to elevated priority in the COP, bypassing the usual watch-and-wait/corroboration step.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away.",
          "evidence_explanation": "Shows a recent, salient prior event being used as the template for the current alert, leading to immediate escalation based on felt similarity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the location and the hour. Both around 0200, both NAI-7. I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way.",
          "evidence_explanation": "Demonstrates that the judgment relied on superficial matching features rather than diagnostic signature data, which is core to representativeness."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Moderately. I didn't have hard evidence, just the pattern match in my head to the earlier event.",
          "evidence_explanation": "Confirms the reasoning operation was an explicit pattern match rather than evidence-based discrimination."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged moderate confidence and lack of hard evidence; he considered leaving the alert routine or obtaining adjacent-unit corroboration but rejected those alternatives. Later analyst review of subsequent imagery leaned non-hostile, though it did not specifically re-evaluate the initial sensor alert.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied to this analyzer specifically defined representativeness heuristic or its mechanism; the label is assigned from widely established cognitive-science knowledge rather than retrieved corpus evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment heuristic",
        "anchoring-and-adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Relying too heavily on an initial piece of information or first-accessed source and making insufficient adjustment when additional relevant information is available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "UAV ISR tasking justification",
      "decision_point_description": "Deciding which sources to use to justify diverting the sole UAV to NAI-7 over competing sector requests.",
      "affected_reasoning_operation": "Information retrieval and justification for a resource allocation decision",
      "bias_specific_mechanism": "The habitual own-sector SIGINT feed was used as the initial informational anchor. The participant did not check accessible adjacent-unit SIGACT or the pattern-of-life database, leaving the tasking justification insufficiently adjusted from that first source.",
      "manifestation_in_interview": "The participant pulled only the own-sector summaries he checks nightly, used that feed to make the call, and tasked the UAV without consulting other available repositories that he later acknowledged were relevant.",
      "effect_on_reasoning_or_decision": "The UAV was tasked to NAI-7 on the basis of a narrower own-sector justification. The participant believed the final diversion might not have changed, but the reasoning and framing would have been more grounded with broader cross-referenced data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first.",
          "evidence_explanation": "Shows that the first-pulled source was the familiar, habitually checked feed, establishing the informational anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later.",
          "evidence_explanation": "Shows he made the call based on the initially accessed source despite accessible alternatives, and later learned there was relevant history elsewhere."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes.",
          "evidence_explanation": "Shows incomplete adjustment away from the initial source: additional relevant repositories were skipped even though one would have taken only about five minutes."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the pattern-of-life database would have taken only five extra minutes and that the UAV likely still would have gone, limiting the effect to justification quality rather than necessarily the final allocation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages address anchoring-and-adjustment generally and in AI-assisted decision-making. They support the label and mechanism but do not by themselves prove the occurrence.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, “adjustments are typically insufficient.”",
          "mechanism_supported_by_source": "Anchoring-and-adjustment: people start from an initial answer and insufficiently adjust with additional information.",
          "relevance_to_this_occurrence": "The participant started from the habitual own-sector feed and did not adequately adjust with accessible additional repositories."
        },
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Anchoring-and-adjustment as a resource-rational tradeoff; adjustment away from an initial anchor is often insufficient under time constraints.",
          "relevance_to_this_occurrence": "The participant cited time pressure as a reason for not checking additional repositories, consistent with incomplete adjustment away from the initially accessed feed."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "ease of imagination",
        "vividness heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Assessing the likelihood or plausibility of an interpretation by how easily and vividly it can be brought to mind or mentally simulated, rather than by objective evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "QRF alert decision after ambiguous thermal imagery",
      "decision_point_description": "Deciding whether to place QRF on 15-minute alert, hold current posture, or request more UAV dwell time.",
      "affected_reasoning_operation": "Interpretation of ambiguous thermal imagery and escalation readiness decision",
      "bias_specific_mechanism": "A recent, vivid training exercise made the ambush scenario easy to imagine and mentally simulate. The livestock explanation was not as vivid, so the participant treated the easily imagined scenario as more likely despite equal evidence.",
      "manifestation_in_interview": "The participant said he could 'basically see' the rehearsed ambush scenario and 'picture exactly how it would unfold,' and he explicitly stated the livestock explanation did not have the same vividness.",
      "effect_on_reasoning_or_decision": "He placed QRF on 15-minute alert instead of holding current posture or requesting further UAV dwell time, despite ambiguous thermal signatures with no confirmed hostile indicators.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time.",
          "evidence_explanation": "Shows a mentally available recent training scenario being used as a vivid simulation and driving the escalation decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other.",
          "evidence_explanation": "Explicitly shows interpretation was based on vividness or ease of imagination rather than diagnostic evidence, which is the core availability mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, I think so. Without that scenario fresh in my head, I might have leaned toward requesting more dwell time instead of alerting QRF right away, since the imagery on its own really didn't point clearly either way.",
          "evidence_explanation": "Counterfactual admission supports the conclusion that the easily available training scenario, not the imagery itself, caused the QRF alert."
        }
      ],
      "correction_or_counterevidence": "The imagery was objectively ambiguous and the participant acknowledged it did not favor either interpretation. Later analyst review assessed the signatures as most consistent with livestock, and QRF was never launched.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied to this analyzer specifically defined the availability heuristic or its imaginative-vividness route; the label is assigned from widely established cognitive-science knowledge rather than retrieved corpus evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages did not include definitions or mechanisms for representativeness or availability heuristics; those labels are based on general knowledge and are disclosed as such.",
    "The anchoring occurrence has a plausible competing time-pressure/habit explanation, so it was rated moderate rather than high.",
    "Some retrieved passages contained OCR artifacts; only retrieved text exactly as supplied was used."
  ]
}

