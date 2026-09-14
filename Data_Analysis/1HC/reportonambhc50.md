# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. This is for an internal review of decision-making during admissions, and I may ask follow-up questions as we go. Are you comfortable with that? Participant: Yes, that's fine. Interviewer: Can you tell me your role on the team during this admission? Participant: I was the attending on the general medicine service, with a resident rotating through. We picked this patient up on day one after she came in for an unrelated complaint and the monitor flagged something new. Interviewer: What was your overall goal for her care during the stay? Participant: To sort out the new finding properly and get her home with a plan that actually made sense given everything else going on with her, not just the one issue. Interviewer: Walk me through what happened, from the diagnosis to discharge. Participant: The admission ECG showed persistent atrial fibrillation, new to us. Her CHA2DS2-VASc came out to 4, so meaningful annual stroke risk if she goes untreated. HAS-BLED was 2 — moderate, not a contraindication on its own. Pharmacy checked for interactions with the DOAC we'd typically use and didn't find any, though they flagged her renal function was sitting at the low end of normal and wanted it monitored. The complicating piece was a fall about three weeks earlier. When we asked her about it directly, she said she tripped, but she also mentioned feeling briefly lightheaded right before — and that part had never been worked up anywhere. So we didn't actually know if this was a mechanical trip or something with a cardiac or orthostatic component that nobody had chased down. Given that gap, I asked for a fall-risk assessment and held off committing to a start date until we had more to go on. The formal assessment came back borderline — not clearly low, not clearly high. I also asked cardiology for a curbside opinion on timing anticoagulation after an unexplained pre-fall symptom, and their answer was honestly that the literature doesn't give a clean threshold for a case like this. On day two, one of the nurses mentioned that a patient down the hall had a bleeding complication on anticoagulation the month before. My patient's daughter had heard about it and asked me directly how similar the situations were. I didn't have the other patient's details memorized, so I asked the resident to pull what was available before I answered her — turned out that patient had notably worse renal clearance and was also on an antiplatelet, which changes the picture substantially. That took a day to sort out. By day three, we had that comparison clarified, but her own fall-risk score was still sitting in that borderline zone, and the CHA2DS2-VASc and HAS-BLED numbers hadn't moved — they still leaned toward treating. Discharge was set for the next morning. I asked for one more renal function check before finalizing a dose, since her creatinine had been borderline on admission and I wanted a same-admission number rather than working off something a few days old. On day four, right before discharge, she had a small bruise where blood had been drawn. She wasn't on anticoagulation yet, so it wasn't drug-related, but the renal result still hadn't come back. I finalized the discharge without starting treatment and arranged outpatient follow-up, which ended up being three weeks out rather than the two we'd hoped for. Interviewer: Let's go through each of those points in more detail. At the first one — right after diagnosis — what stood out most? Participant: The lightheadedness before the fall. If that fall had a cardiac cause we hadn't identified, starting anticoagulation without understanding it felt premature. But I'll be honest, it's a judgment call — plenty of people would say the stroke-risk numbers were clear enough to just start and monitor. Interviewer: What alternatives did you weigh? Participant: Start the DOAC right away given the score, defer until the lightheadedness was evaluated, or start a reduced empirical dose in the meantime. I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer. Interviewer: At the second point, with the comparator patient — what were you trying to do there? Participant: Give the daughter an accurate answer instead of a reassuring guess. Without knowing the other patient's renal function or medications, I couldn't tell her anything meaningful, so I had the resident check before we talked further. Interviewer: How much time pressure did that add? Participant: Some — it pushed the conversation back a day, which mattered given discharge planning. But answering her with an unverified comparison seemed worse than the delay. Interviewer: At the third point, after the comparison was clarified and fall risk was still borderline — what was the reasoning behind getting another renal check? Participant: Her creatinine on admission was borderline, and dosing a DOAC on stale numbers, especially this close to discharge, didn't sit right with me. Someone could reasonably argue the scores already justified starting and adjusting later if needed. I didn't feel strongly that one path was clearly correct. Interviewer: Had a similar situation come up for you before? Participant: Something like it, yes — dosing decisions where the renal number is borderline. It usually comes down to how much runway you have before discharge, and here we had very little. Interviewer: At the fourth point, the bruise at discharge — how did that factor in? Participant: It didn't really change anything clinically since she wasn't on the drug yet. The bigger factor was still the pending renal result. We noted the bruise for the outpatient team and moved on. Interviewer: If the fall-risk assessment had come back clearly low instead of borderline, would you have decided differently? Participant: Probably, yes — a clear low score would have resolved a lot of the hesitation at the first decision point. Interviewer: If the comparator patient's chart details had been available immediately, do you think the outcome would have changed? Participant: Possibly the family conversation would have gone faster, but I don't think it would have changed the actual treatment timing much — the renal question was separate. Interviewer: Looking back, what would you tell a colleague facing something similar? Participant: Chase down unexplained symptoms before they get labeled as routine falls, and don't assume a story about another patient applies to yours without checking the details. Beyond that, I think reasonable people could have made different calls at almost every step here.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.43s · gen 147.00s · total 150.4s_

**Retrieved** (ranked by store ranker):
1. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0323 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
2. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0240 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
3. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0213 (rrf) — _# decisionmaking examined the relationship between nurses' bias to healthcare disparities. In th_
4. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0212 (rrf) — _## Uwe Dulleck, PhD revealed that if a patient was having lower abdominal pain with a temperatur_
5. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0209 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
6. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0203 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
7. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0188 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0186 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0185 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0183 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0179 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
13. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0173 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0170 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
15. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0165 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
16. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0164 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
17. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0164 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0161 (rrf) — _## Types of Cognitive Biases criticize themselves rather than the device. Priming Effect. The te_
20. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0160 (rrf) — _# support were adapted from translated into German scenario in less the use of heuristics for on_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
22. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0159 (rrf) — _# 4on patient outcomes in the emergency department: A scoping We used the eligibility and exclus_
23. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0159 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0158 (rrf) — _## Uwe Dulleck, PhD ical decisionmaking \[ The fi ndings of our study have signi patient health _
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0158 (rrf) — _# to Dangers from Humans speed, brute strength, sensory acuity, and apparent det allies to attac_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0157 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0155 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
28. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0154 (rrf) — _# fi cation Physicians engaged with the AI to inquire about evidence supporting clinical decisio_
29. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0153 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
30. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0152 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
31. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0150 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
32. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0149 (rrf) — _## Uwe Dulleck, PhD tive biases or risktaking behavior and triage accuracy varied according 2.1._
34. **Hallihan_etal_DTM_12.pdf** — 0.0149 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
35. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0149 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs | Option 7 : Very likely opinion B | | _
36. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _# American Journal of Emergency Medicine journal homepage: abstract Background: source usage. Su_
37. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0146 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
38. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0145 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
39. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0143 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
40. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0143 (rrf) — _## BMC Medical Ethics Open Access incapacitated patient. ey list ve main biases related to infor_
41. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0140 (rrf) — _# decisionmaking Barnato et al., 2011 ; Green et al., et al., 2015 ; Maina et al., 2018 ; Saposn_
42. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0140 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
43. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _# Clinical decisionmaking: Cognitive biases and heuristics in triage decisions in the emergency _
44. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0139 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
45. **Hallihan_etal_DTM_12.pdf** — 0.0138 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
46. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0137 (rrf) — _# 6.2 Analysis of the structural model people make mistakes and errors occur. Errors can be redu_
47. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0137 (rrf) — _# fi cation 8 demonstrating human biases in clinical interpretation. Participants were randomize_
48. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0136 (rrf) — _# decisionmaking black and white elder simulated patients with end- Emergency nurses' and physic_
49. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0135 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
50. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0131 (rrf) — _## Elliott RN, PhD 1 Faculty of Health, School of Nursing and Midwifery, University of Technolog_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Evaluated the interview for affirmatively demonstrated cognitive bias occurrences in clinical anticoagulation timing reasoning. No occurrence met the specified evidence threshold; plausible but unconfirmed patterns are recorded as candidates only."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Omission bias",
      "alternative_labels": [
        "status quo bias",
        "default bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Day four discharge decision without starting anticoagulation",
      "supporting_interview_quote": "I finalized the discharge without starting treatment and arranged outpatient follow-up, which ended up being three weeks out rather than the two we'd hoped for.",
      "plausible_mechanism": "Inaction may be preferred when both action and omission carry risk; starting anticoagulation could cause immediate bleeding, whereas omitting treatment may permit stroke, but omission-related harms may be less salient and less likely to trigger regret.",
      "why_not_identified": "The transcript attributes the decision to unresolved fall history, a borderline fall-risk score, and pending renal function rather than to a bias-driven preference for inaction. There is no affirmative statement indicating distorted risk weighting or regret avoidance."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Availability bias",
      "alternative_labels": [
        "availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Response to nurse's report of another patient's bleeding complication on anticoagulation and subsequent treatment timing",
      "supporting_interview_quote": "one of the nurses mentioned that a patient down the hall had a bleeding complication on anticoagulation the month before. My patient's daughter had heard about it and asked me directly how similar the situations were.",
      "plausible_mechanism": "A vivid recent bleeding complication could inflate the perceived likelihood or salience of bleeding risk, making anticoagulation seem more hazardous and potentially leading to delay or excess caution.",
      "why_not_identified": "The participant explicitly requested the other patient's chart details, identified key differences including worse renal clearance and antiplatelet use, and stated the comparison mainly affected timing of the family conversation rather than the final treatment decision. No transcript evidence shows the event distorted the final risk estimate."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "anchoring heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial decision to defer anticoagulation after new atrial fibrillation diagnosis with recent fall and pre-fall lightheadedness",
      "supporting_interview_quote": "Given that gap, I asked for a fall-risk assessment and held off committing to a start date until we had more to go on.",
      "plausible_mechanism": "The initial concern about the fall and unexplained lightheadedness may have served as an anchor, with subsequently borderline information interpreted as supporting the initial deferral rather than prompting movement toward guideline-supported anticoagulation.",
      "why_not_identified": "The participant explicitly weighed CHA2DS2-VASc and HAS-BLED scores and acknowledged that they still leaned toward treating. There is no affirmative evidence of failure to adjust from the initial concern; the transcript shows ongoing updating and consultation rather than fixed anchoring."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "This is a single retrospective self-report interview; introspective accounts may omit or rationalize cognitive processes.",
    "No objective decision outcome, experimental manipulation, or independent task performance measure was available to verify biased reasoning.",
    "A conservative evidence threshold was applied; plausible but unconfirmed patterns were recorded as candidates rather than identified occurrences.",
    "Retrieved corpus passages were available for terminology, but no retrieved passage can by itself establish that a bias occurred in this transcript."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. This is for an internal review of decision-making during admissions, and I may ask follow-up questions as we go. Are you comfortable with that? Participant: Yes, that's fine. Interviewer: Can you tell me your role on the team during this admission? Participant: I was the attending on the general medicine service, with a resident rotating through. We picked this patient up on day one after she came in for an unrelated complaint and the monitor flagged something new. Interviewer: What was your overall goal for her care during the stay? Participant: To sort out the new finding properly and get her home with a plan that actually made sense given everything else going on with her, not just the one issue. Interviewer: Walk me through what happened, from the diagnosis to discharge. Participant: The admission ECG showed persistent atrial fibrillation, new to us. Her CHA2DS2-VASc came out to 4, so meaningful annual stroke risk if she goes untreated. HAS-BLED was 2 — moderate, not a contraindication on its own. Pharmacy checked for interactions with the DOAC we'd typically use and didn't find any, though they flagged her renal function was sitting at the low end of normal and wanted it monitored. The complicating piece was a fall about three weeks earlier. When we asked her about it directly, she said she tripped, but she also mentioned feeling briefly lightheaded right before — and that part had never been worked up anywhere. So we didn't actually know if this was a mechanical trip or something with a cardiac or orthostatic component that nobody had chased down. Given that gap, I asked for a fall-risk assessment and held off committing to a start date until we had more to go on. The formal assessment came back borderline — not clearly low, not clearly high. I also asked cardiology for a curbside opinion on timing anticoagulation after an unexplained pre-fall symptom, and their answer was honestly that the literature doesn't give a clean threshold for a case like this. On day two, one of the nurses mentioned that a patient down the hall had a bleeding complication on anticoagulation the month before. My patient's daughter had heard about it and asked me directly how similar the situations were. I didn't have the other patient's details memorized, so I asked the resident to pull what was available before I answered her — turned out that patient had notably worse renal clearance and was also on an antiplatelet, which changes the picture substantially. That took a day to sort out. By day three, we had that comparison clarified, but her own fall-risk score was still sitting in that borderline zone, and the CHA2DS2-VASc and HAS-BLED numbers hadn't moved — they still leaned toward treating. Discharge was set for the next morning. I asked for one more renal function check before finalizing a dose, since her creatinine had been borderline on admission and I wanted a same-admission number rather than working off something a few days old. On day four, right before discharge, she had a small bruise where blood had been drawn. She wasn't on anticoagulation yet, so it wasn't drug-related, but the renal result still hadn't come back. I finalized the discharge without starting treatment and arranged outpatient follow-up, which ended up being three weeks out rather than the two we'd hoped for. Interviewer: Let's go through each of those points in more detail. At the first one — right after diagnosis — what stood out most? Participant: The lightheadedness before the fall. If that fall had a cardiac cause we hadn't identified, starting anticoagulation without understanding it felt premature. But I'll be honest, it's a judgment call — plenty of people would say the stroke-risk numbers were clear enough to just start and monitor. Interviewer: What alternatives did you weigh? Participant: Start the DOAC right away given the score, defer until the lightheadedness was evaluated, or start a reduced empirical dose in the meantime. I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer. Interviewer: At the second point, with the comparator patient — what were you trying to do there? Participant: Give the daughter an accurate answer instead of a reassuring guess. Without knowing the other patient's renal function or medications, I couldn't tell her anything meaningful, so I had the resident check before we talked further. Interviewer: How much time pressure did that add? Participant: Some — it pushed the conversation back a day, which mattered given discharge planning. But answering her with an unverified comparison seemed worse than the delay. Interviewer: At the third point, after the comparison was clarified and fall risk was still borderline — what was the reasoning behind getting another renal check? Participant: Her creatinine on admission was borderline, and dosing a DOAC on stale numbers, especially this close to discharge, didn't sit right with me. Someone could reasonably argue the scores already justified starting and adjusting later if needed. I didn't feel strongly that one path was clearly correct. Interviewer: Had a similar situation come up for you before? Participant: Something like it, yes — dosing decisions where the renal number is borderline. It usually comes down to how much runway you have before discharge, and here we had very little. Interviewer: At the fourth point, the bruise at discharge — how did that factor in? Participant: It didn't really change anything clinically since she wasn't on the drug yet. The bigger factor was still the pending renal result. We noted the bruise for the outpatient team and moved on. Interviewer: If the fall-risk assessment had come back clearly low instead of borderline, would you have decided differently? Participant: Probably, yes — a clear low score would have resolved a lot of the hesitation at the first decision point. Interviewer: If the comparator patient's chart details had been available immediately, do you think the outcome would have changed? Participant: Possibly the family conversation would have gone faster, but I don't think it would have changed the actual treatment timing much — the renal question was separate. Interviewer: Looking back, what would you tell a colleague facing something similar? Participant: Chase down unexplained symptoms before they get labeled as routine falls, and don't assume a story about another patient applies to yours without checking the details. Beyond that, I think reasonable people could have made different calls at almost every step here.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.38s · gen 146.07s · total 149.4s_

**Retrieved** (ranked by store ranker):
1. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0323 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
2. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0240 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
3. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0213 (rrf) — _# decisionmaking examined the relationship between nurses' bias to healthcare disparities. In th_
4. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0212 (rrf) — _## Uwe Dulleck, PhD revealed that if a patient was having lower abdominal pain with a temperatur_
5. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0209 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
6. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0203 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
7. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0188 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0186 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0185 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0183 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0179 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
13. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0173 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0170 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
15. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0165 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
16. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0164 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
17. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0164 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0161 (rrf) — _## Types of Cognitive Biases criticize themselves rather than the device. Priming Effect. The te_
20. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0160 (rrf) — _# support were adapted from translated into German scenario in less the use of heuristics for on_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
22. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0159 (rrf) — _# 4on patient outcomes in the emergency department: A scoping We used the eligibility and exclus_
23. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0159 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0158 (rrf) — _## Uwe Dulleck, PhD ical decisionmaking \[ The fi ndings of our study have signi patient health _
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0158 (rrf) — _# to Dangers from Humans speed, brute strength, sensory acuity, and apparent det allies to attac_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0157 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0155 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
28. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0154 (rrf) — _# fi cation Physicians engaged with the AI to inquire about evidence supporting clinical decisio_
29. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0153 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
30. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0152 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
31. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0150 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
32. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0149 (rrf) — _## Uwe Dulleck, PhD tive biases or risktaking behavior and triage accuracy varied according 2.1._
34. **Hallihan_etal_DTM_12.pdf** — 0.0149 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
35. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0149 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs | Option 7 : Very likely opinion B | | _
36. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _# American Journal of Emergency Medicine journal homepage: abstract Background: source usage. Su_
37. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0146 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
38. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0145 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
39. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0143 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
40. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0143 (rrf) — _## BMC Medical Ethics Open Access incapacitated patient. ey list ve main biases related to infor_
41. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0140 (rrf) — _# decisionmaking Barnato et al., 2011 ; Green et al., et al., 2015 ; Maina et al., 2018 ; Saposn_
42. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0140 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
43. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _# Clinical decisionmaking: Cognitive biases and heuristics in triage decisions in the emergency _
44. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0139 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
45. **Hallihan_etal_DTM_12.pdf** — 0.0138 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
46. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0137 (rrf) — _# 6.2 Analysis of the structural model people make mistakes and errors occur. Errors can be redu_
47. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0137 (rrf) — _# fi cation 8 demonstrating human biases in clinical interpretation. Participants were randomize_
48. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0136 (rrf) — _# decisionmaking black and white elder simulated patients with end- Emergency nurses' and physic_
49. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0135 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
50. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0131 (rrf) — _## Elliott RN, PhD 1 Faculty of Health, School of Nursing and Midwifery, University of Technolog_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis of the attending physician's self-reported reasoning during a hospital admission involving new atrial fibrillation and a decision to defer anticoagulation. Assessed only for bias-specific mechanisms explicitly or clearly implied in the interview text; no experimental benchmark was assumed."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring",
      "alternative_labels": ["Anchoring and adjustment"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial decision to defer anticoagulation after new atrial fibrillation diagnosis",
      "supporting_interview_quote": "The lightheadedness before the fall. If that fall had a cardiac cause we hadn't identified, starting anticoagulation without understanding it felt premature.",
      "plausible_mechanism": "The participant may have anchored on the recent fall and pre-fall lightheadedness as the most important issue, weighing it heavily relative to the patient's CHA2DS2-VASc stroke-risk score.",
      "why_not_identified": "There is no affirmative evidence that the selected reference point produced insufficient adjustment or that the deferral was driven by an anchor rather than by ordinary clinical uncertainty and a deliberate request for fall-risk and cardiology input."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Availability bias",
      "alternative_labels": ["Availability heuristic"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Concern after nurse mentioned another patient's bleeding complication on anticoagulation",
      "supporting_interview_quote": "On day two, one of the nurses mentioned that a patient down the hall had a bleeding complication on anticoagulation the month before.",
      "plausible_mechanism": "A vivid, recent bleeding complication could have made bleeding-related harms more cognitively available, potentially increasing caution about anticoagulation.",
      "why_not_identified": "The participant explicitly fact-checked the comparator case, concluded the other patient differed on relevant factors, and stated the comparison likely would not have changed treatment timing; this substantially works against a material availability-bias effect."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "Omission bias",
      "alternative_labels": ["Status quo bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Discharge without starting anticoagulation despite remaining stroke risk",
      "supporting_interview_quote": "I finalized the discharge without starting treatment and arranged outpatient follow-up, which ended up being three weeks out rather than the two we'd hoped for.",
      "plausible_mechanism": "Harm from not acting, such as stroke, may have been treated as less blameworthy or less salient than potential harm from starting a DOAC, prompting a passive approach.",
      "why_not_identified": "No explicit preference for inaction or asymmetry in regret is present; the delay appears tied to pending renal function and unresolved fall risk, which are legitimate clinical reasons."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "The transcript is a retrospective self-report, not direct observation of real-time reasoning, so bias-specific mechanisms are difficult to establish.",
    "Many decisions reflect unresolved clinical risk and borderline information; these were treated as ordinary uncertainty rather than bias.",
    "Retrieved corpus support was not used for identified occurrences because no occurrence met the affirmative-evidence threshold."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. This is for an internal review of decision-making during admissions, and I may ask follow-up questions as we go. Are you comfortable with that? Participant: Yes, that's fine. Interviewer: Can you tell me your role on the team during this admission? Participant: I was the attending on the general medicine service, with a resident rotating through. We picked this patient up on day one after she came in for an unrelated complaint and the monitor flagged something new. Interviewer: What was your overall goal for her care during the stay? Participant: To sort out the new finding properly and get her home with a plan that actually made sense given everything else going on with her, not just the one issue. Interviewer: Walk me through what happened, from the diagnosis to discharge. Participant: The admission ECG showed persistent atrial fibrillation, new to us. Her CHA2DS2-VASc came out to 4, so meaningful annual stroke risk if she goes untreated. HAS-BLED was 2 — moderate, not a contraindication on its own. Pharmacy checked for interactions with the DOAC we'd typically use and didn't find any, though they flagged her renal function was sitting at the low end of normal and wanted it monitored. The complicating piece was a fall about three weeks earlier. When we asked her about it directly, she said she tripped, but she also mentioned feeling briefly lightheaded right before — and that part had never been worked up anywhere. So we didn't actually know if this was a mechanical trip or something with a cardiac or orthostatic component that nobody had chased down. Given that gap, I asked for a fall-risk assessment and held off committing to a start date until we had more to go on. The formal assessment came back borderline — not clearly low, not clearly high. I also asked cardiology for a curbside opinion on timing anticoagulation after an unexplained pre-fall symptom, and their answer was honestly that the literature doesn't give a clean threshold for a case like this. On day two, one of the nurses mentioned that a patient down the hall had a bleeding complication on anticoagulation the month before. My patient's daughter had heard about it and asked me directly how similar the situations were. I didn't have the other patient's details memorized, so I asked the resident to pull what was available before I answered her — turned out that patient had notably worse renal clearance and was also on an antiplatelet, which changes the picture substantially. That took a day to sort out. By day three, we had that comparison clarified, but her own fall-risk score was still sitting in that borderline zone, and the CHA2DS2-VASc and HAS-BLED numbers hadn't moved — they still leaned toward treating. Discharge was set for the next morning. I asked for one more renal function check before finalizing a dose, since her creatinine had been borderline on admission and I wanted a same-admission number rather than working off something a few days old. On day four, right before discharge, she had a small bruise where blood had been drawn. She wasn't on anticoagulation yet, so it wasn't drug-related, but the renal result still hadn't come back. I finalized the discharge without starting treatment and arranged outpatient follow-up, which ended up being three weeks out rather than the two we'd hoped for. Interviewer: Let's go through each of those points in more detail. At the first one — right after diagnosis — what stood out most? Participant: The lightheadedness before the fall. If that fall had a cardiac cause we hadn't identified, starting anticoagulation without understanding it felt premature. But I'll be honest, it's a judgment call — plenty of people would say the stroke-risk numbers were clear enough to just start and monitor. Interviewer: What alternatives did you weigh? Participant: Start the DOAC right away given the score, defer until the lightheadedness was evaluated, or start a reduced empirical dose in the meantime. I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer. Interviewer: At the second point, with the comparator patient — what were you trying to do there? Participant: Give the daughter an accurate answer instead of a reassuring guess. Without knowing the other patient's renal function or medications, I couldn't tell her anything meaningful, so I had the resident check before we talked further. Interviewer: How much time pressure did that add? Participant: Some — it pushed the conversation back a day, which mattered given discharge planning. But answering her with an unverified comparison seemed worse than the delay. Interviewer: At the third point, after the comparison was clarified and fall risk was still borderline — what was the reasoning behind getting another renal check? Participant: Her creatinine on admission was borderline, and dosing a DOAC on stale numbers, especially this close to discharge, didn't sit right with me. Someone could reasonably argue the scores already justified starting and adjusting later if needed. I didn't feel strongly that one path was clearly correct. Interviewer: Had a similar situation come up for you before? Participant: Something like it, yes — dosing decisions where the renal number is borderline. It usually comes down to how much runway you have before discharge, and here we had very little. Interviewer: At the fourth point, the bruise at discharge — how did that factor in? Participant: It didn't really change anything clinically since she wasn't on the drug yet. The bigger factor was still the pending renal result. We noted the bruise for the outpatient team and moved on. Interviewer: If the fall-risk assessment had come back clearly low instead of borderline, would you have decided differently? Participant: Probably, yes — a clear low score would have resolved a lot of the hesitation at the first decision point. Interviewer: If the comparator patient's chart details had been available immediately, do you think the outcome would have changed? Participant: Possibly the family conversation would have gone faster, but I don't think it would have changed the actual treatment timing much — the renal question was separate. Interviewer: Looking back, what would you tell a colleague facing something similar? Participant: Chase down unexplained symptoms before they get labeled as routine falls, and don't assume a story about another patient applies to yours without checking the details. Beyond that, I think reasonable people could have made different calls at almost every step here.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.36s · gen 279.02s · total 282.2s_

**Retrieved** (ranked by store ranker):
1. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0323 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
2. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0240 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
3. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0213 (rrf) — _# decisionmaking examined the relationship between nurses' bias to healthcare disparities. In th_
4. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0212 (rrf) — _## Uwe Dulleck, PhD revealed that if a patient was having lower abdominal pain with a temperatur_
5. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0209 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
6. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0203 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
7. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0188 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0186 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0185 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0183 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0179 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
13. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0173 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0170 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
15. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0165 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
16. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0164 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
17. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0164 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0161 (rrf) — _## Types of Cognitive Biases criticize themselves rather than the device. Priming Effect. The te_
20. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0160 (rrf) — _# support were adapted from translated into German scenario in less the use of heuristics for on_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
22. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0159 (rrf) — _# 4on patient outcomes in the emergency department: A scoping We used the eligibility and exclus_
23. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0159 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0158 (rrf) — _## Uwe Dulleck, PhD ical decisionmaking \[ The fi ndings of our study have signi patient health _
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0158 (rrf) — _# to Dangers from Humans speed, brute strength, sensory acuity, and apparent det allies to attac_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0157 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0155 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
28. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0154 (rrf) — _# fi cation Physicians engaged with the AI to inquire about evidence supporting clinical decisio_
29. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0153 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
30. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0152 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
31. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0150 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
32. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0149 (rrf) — _## Uwe Dulleck, PhD tive biases or risktaking behavior and triage accuracy varied according 2.1._
34. **Hallihan_etal_DTM_12.pdf** — 0.0149 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
35. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0149 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs | Option 7 : Very likely opinion B | | _
36. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _# American Journal of Emergency Medicine journal homepage: abstract Background: source usage. Su_
37. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0146 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
38. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0145 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
39. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0143 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
40. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0143 (rrf) — _## BMC Medical Ethics Open Access incapacitated patient. ey list ve main biases related to infor_
41. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0140 (rrf) — _# decisionmaking Barnato et al., 2011 ; Green et al., et al., 2015 ; Maina et al., 2018 ; Saposn_
42. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0140 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
43. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _# Clinical decisionmaking: Cognitive biases and heuristics in triage decisions in the emergency _
44. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0139 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
45. **Hallihan_etal_DTM_12.pdf** — 0.0138 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
46. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0137 (rrf) — _# 6.2 Analysis of the structural model people make mistakes and errors occur. Errors can be redu_
47. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0137 (rrf) — _# fi cation 8 demonstrating human biases in clinical interpretation. Participants were randomize_
48. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0136 (rrf) — _# decisionmaking black and white elder simulated patients with end- Emergency nurses' and physic_
49. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0135 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
50. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0131 (rrf) — _## Elliott RN, PhD 1 Faculty of Health, School of Nursing and Midwifery, University of Technolog_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the provided CTA admissions interview for affirmative evidence of bias-specific reasoning mechanisms; retrieved passages used only for conceptual classification."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring",
        "Anchoring and adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial or salient piece of information and to adjust insufficiently from it when making a judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to defer starting anticoagulation after newly detected atrial fibrillation",
      "decision_point_description": "Initial decision to defer the DOAC start date and subsequent discharge without starting anticoagulation.",
      "affected_reasoning_operation": "Treatment initiation judgment under uncertainty",
      "bias_specific_mechanism": "The unexplained lightheadedness before a fall became a salient anchor that made the history feel incomplete; subsequent objective data such as CHA2DS2-VASc/HAS-BLED scores favoring anticoagulation and a borderline fall-risk assessment were not sufficient to shift the decision away from deferral.",
      "manifestation_in_interview": "The participant repeatedly tied the anticoagulation timing decision to the fall/lightheadedness, even after the formal fall-risk assessment was borderline and the risk scores still leaned toward treating.",
      "effect_on_reasoning_or_decision": "The clinical decision remained to withhold the DOAC before discharge and arrange outpatient follow-up, despite the participant acknowledging that the stroke-risk numbers favored treatment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The admission ECG showed persistent atrial fibrillation, new to us. Her CHA2DS2-VASc came out to 4, so meaningful annual stroke risk if she goes untreated. HAS-BLED was 2 — moderate, not a contraindication on its own.",
          "evidence_explanation": "Establishes the objective baseline favoring anticoagulation, against which the later deferral decision can be compared."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The complicating piece was a fall about three weeks earlier. When we asked her about it directly, she said she tripped, but she also mentioned feeling briefly lightheaded right before — and that part had never been worked up anywhere. So we didn't actually know if this was a mechanical trip or something with a cardiac or orthostatic component that nobody had chased down.",
          "evidence_explanation": "Shows the salient initial complication that becomes the anchor for the participant's anticoagulation timing reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The formal assessment came back borderline — not clearly low, not clearly high.",
          "evidence_explanation": "The fall-risk result was not clearly high, yet it continued to function as a gating factor for treatment, consistent with anchoring on the initial fall concern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer.",
          "evidence_explanation": "Explicitly ties the treatment decision to the initial fall/lightheadedness anchor and the resulting sense of an incomplete history."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "By day three, we had that comparison clarified, but her own fall-risk score was still sitting in that borderline zone, and the CHA2DS2-VASc and HAS-BLED numbers hadn't moved — they still leaned toward treating.",
          "evidence_explanation": "Demonstrates that subsequent information and objective scores favoring treatment did not adjust the participant away from the deferral anchored earlier."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yes — a clear low score would have resolved a lot of the hesitation at the first decision point.",
          "evidence_explanation": "Indicates that the fall-risk concern was the gating anchor; only a clearly low score would have resolved the hesitation."
        }
      ],
      "correction_or_counterevidence": "The participant considered alternatives, requested a fall-risk assessment, sought cardiology input, checked comparator-patient details rather than assuming similarity, and acknowledged that reasonable people could make different calls. Borderline fall risk, unexplained lightheadedness, and pending renal function are plausible non-bias reasons for caution, so this occurrence is reported with low confidence.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved source supports anchoring as a clinical reasoning bias conceptually, but it does not match this case directly. The label is grounded in this general mechanism rather than in a source specifically about anticoagulation decisions.",
      "corpus_evidence": [
        {
          "source_identifier": "From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf",
          "paper_title": "From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The cognitive failures identified here are \"anchoring\" and \"search satisficing.\" The resident and attending staff both anchored onto the chest wound as the most significant injury. When they satisfied themselves that the chest wound was stable, the resident failed to conduct a sufficient search to rule out other significant injuries.",
          "mechanism_supported_by_source": "Anchoring on a salient clinical feature as the most significant problem and failing to adjust or search sufficiently despite other possible significant issues.",
          "relevance_to_this_occurrence": "Supports the classification of the participant's persistent focus on the fall/lightheadedness as an anchoring feature that persisted even though objective risk scores leaned toward treatment."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Availability bias",
      "alternative_labels": [
        "Availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Evaluating daughter's question about the other patient's bleeding complication",
      "supporting_interview_quote": "On day two, one of the nurses mentioned that a patient down the hall had a bleeding complication on anticoagulation the month before. My patient's daughter had heard about it and asked me directly how similar the situations were.",
      "plausible_mechanism": "The recent bleeding complication was highly available and could have increased the perceived bleeding risk, potentially contributing to anticoagulation hesitancy.",
      "why_not_identified": "The participant explicitly did not rely on the comparison; he requested chart details, found key differences, and stated the comparator did not change treatment timing much. There is no affirmative evidence that the recent case influenced the anticoagulation decision."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Omission bias",
      "alternative_labels": [
        "Status quo bias",
        "Action/inaction asymmetry"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final discharge without starting anticoagulation",
      "supporting_interview_quote": "Someone could reasonably argue the scores already justified starting and adjusting later if needed. I didn't feel strongly that one path was clearly correct.",
      "plausible_mechanism": "A preference for inaction may have avoided immediate potential bleeding harm from treatment while accepting longer-term stroke risk from omission.",
      "why_not_identified": "The participant gave explicit non-bias reasons for inaction: incomplete fall/lightheadedness history, borderline fall-risk score, pending renal function, and no clear contraindication-free certainty. There is no direct comparative statement that bleeding harm outweighed stroke risk."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved passages are partially redacted or OCR-corrupted, making some metadata unavailable.",
    "The transcript provides limited access to the participant's private risk weighting, so some mechanism classifications are necessarily indirect and reported at low confidence.",
    "No clinical guideline knowledge was used to judge medical correctness; analysis is limited to reasoning mechanisms apparent in the transcript."
  ]
}

