# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a retrospective walkthrough of a specific vulnerability case you handled, purely for process review — nothing about individual performance evaluation. Can you tell me your role and how long you've been doing vulnerability management? Participant: Sure, no problem. I'm a Vulnerability Management Analyst, I've been in this seat about three years now, before that I did general SOC monitoring. Right now I own triage and remediation tracking for our internet-facing assets, so patch coordination, compensating controls, closing out tickets against our SLA. Interviewer: Great. Walk me through how this particular case started and what you were trying to accomplish. Participant: So this began when our threat intel feed flagged a new CVE, critical, 9.8 on CVSS, and it had confirmed exploitation already happening in the wild. It hit the web framework running underneath our legacy order-processing gateway — that's the system customers hit when they check out, so it's tagged Tier-1 criticality, internet-facing, revenue-generating. My objective was straightforward on paper: get this closed within our 30-day SLA without taking the gateway down during a peak sales stretch. The complication is that gateway is old, it needs vendor coordination to patch, and we had a partial change freeze coming up in about ten days, so the runway to actually get a maintenance window was shrinking fast. On top of that I had two other high-severity tickets open at the same time, so this wasn't the only thing on my plate. Interviewer: Given all that, how did the incident actually unfold, in order? Participant: Day one, the alert comes in, I do initial triage and decide to push for an emergency change board session instead of waiting for the normal 21-day cycle. That gets approved, but it's only a two-hour window, not enough for full regression testing. So around day three, we deploy a WAF rule as an interim compensating control instead of the real patch. While I'm watching the dashboard for that, I notice there's also some odd outbound DNS traffic from the same host, but it's not part of what I'm tracking for this ticket. About a week in, IT Ops points out there's now a vendor SIEM correlation rule available for this CVE family, versus the detection script I'd built myself months earlier, and I decide how to handle that overlap. Then by day 27, with the SLA clock running out and the actual patch still not deployed, I make the call on whether to close the ticket as mitigated. Interviewer: Let's slow down on the first one — the decision to escalate. What made you push for the emergency CAB slot instead of the standard cycle? Participant: Honestly, the exploit-in-the-wild status was the trigger, that's usually a hard line for us. But what really drove how I pitched it to my manager was framing what happens if we don't act — we're talking about a checkout system, so if this gets popped, we're looking at a breached customer-payment flow, contract penalties from at least one retail partner, and reputational fallout that's hard to walk back. I basically built the case around what we stood to lose if we sat on it for 21 days. Interviewer: Did you weigh that against the cost of disrupting the gateway with an emergency patch attempt? Participant: A little, but not as heavily. I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation. I think it got the CAB slot faster because of that. Interviewer: Understood. Second decision point — once you had the WAF rule in place, how did you handle the DNS anomaly you mentioned? Participant: Yeah, so the dashboard was showing a clean match on the known exploit payload pattern, which is what the ticket was actually about, and I spent most of my time confirming that signature was blocked correctly. The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as 'anomalous, monitor' and moved on. My focus was really on validating the compensating control against the threat we knew about. Interviewer: Was there a reason you didn't open a parallel look into the DNS traffic at that point? Participant: I considered it briefly, but I was heads-down on making sure the WAF rule actually caught the payload variant we had confirmed. Two days later a different analyst ended up escalating that DNS pattern separately as a possible unrelated compromise indicator, so it did turn out to be something. At the time, though, it just wasn't where my attention was. Interviewer: Third decision — the detection tooling. What happened there? Participant: Right, so I'd written a detection script for this six months back, tuned it myself against our traffic. When the vendor's SIEM correlation rule came out covering multiple payload variants, IT Ops suggested we just standardize on that instead. I kept my script as the primary and put the vendor rule in a secondary, lower-priority slot. Interviewer: What was the reasoning behind keeping yours in the lead role, given the vendor rule had broader coverage? Participant: I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us. The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own. I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well. Interviewer: Did that decision have downstream effects? Participant: About a week later a slightly different payload variant showed up that my script didn't flag, but the vendor rule would have caught it. We caught it another way eventually, but it was a gap. Interviewer: Last decision point — closing the ticket at day 27. Walk me through that. Participant: At that point we still didn't have the actual vendor patch deployed, just the WAF rule and my script running as compensating controls. The SLA clock was almost out. I closed it as adequately mitigated. Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup. There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open. Interviewer: How much of that closure decision was based on the specific residual-risk data for this ticket versus that broader context? Participant: Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script. I did note those in the ticket, but I don't think I treated them as blocking the closure the way I maybe should have. Interviewer: Was there uncertainty at that point about whether the controls were fully sufficient? Participant: Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered. A post-incident audit about a month later found there was actually a narrow exposure window that never got closed, though nothing was ever exploited through it. Interviewer: If you'd had another week before the SLA deadline, would anything have gone differently? Participant: Probably would have chased down the DNS anomaly properly and maybe pushed harder for the actual vendor patch instead of leaning on compensating controls that long. Interviewer: If that ransomware story hadn't been in the news that week, do you think the closure decision changes? Participant: Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then. Interviewer: And if the vendor SIEM rule had existed from day one, would you have built your own script at all? Participant: Hard to say — probably still would have, honestly, just because I like understanding exactly what's under the hood. Though maybe I'd have made it secondary from the start instead of the other way around. Interviewer: Looking back across the whole case, is there a point where you think you gave one piece of evidence more weight than it really deserved? Participant: Probably the closure call. Between my own confidence in the controls I'd built and everything going on in the news that week, I think I leaned on those more than the actual open items on the ticket. Interviewer: That's really helpful, thank you for walking through it in this much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.87s · gen 381.05s · total 386.6s_

**Retrieved** (ranked by store ranker):
1. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0239 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0239 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0229 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0228 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
5. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0205 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
6. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0201 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
7. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0197 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0179 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0173 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
14. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0167 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
15. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0167 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
16. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _# 592 G t ly; when it was a chore (taking out the garbage), only 44% did so. This dradecrease in_
17. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0163 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
18. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
21. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0159 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs introduced to the model. In both varian_
22. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
23. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# 4. Results The results indicate that users who employ strong password creation practices and f_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0155 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
27. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# 3. Materials and Methods curve (AUC) serving as the primary metric for assessing predictive ac_
28. **ijcma-08-2012-0064.pdf** — 0.0151 (rrf) — _# 378 et al. , 1994), Downloaded from http://www.emerald.com/ijcma/articlepdf/24/4/374/817133/ij_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
31. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
32. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0149 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
34. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0145 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION the same as theirs. However, participants may conclude ci_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
36. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0142 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
37. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0142 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## a nd Prey 212 S experience and dishabituating to deviations from the learned trajectories, be_
40. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0138 (rrf) — _# 6. Conclusions This study provides empirical evidence that heuristicdriven decisionmaking play_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
42. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0138 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
43. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0137 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
44. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0137 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
45. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0135 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0135 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
47. **Lyell Automation bias and verification complexity.pdf** — 0.0135 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
48. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0133 (rrf) — _# across domains and different parts of the search process. 2 Note that our review was not a sys_
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0133 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
50. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0133 (rrf) — _## , Floredana Constantin and Sabina-Cristiana Necula \* 1 Department of Accounting, Business In_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative mechanism-first analysis of the participant's retrospective vulnerability-management case; no experimental condition or benchmark hypothesis was assumed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "IKEA effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "illusion of control",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "loss aversion",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "loss aversion",
      "alternative_labels": ["framing effect", "loss framing"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to weigh potential losses more heavily than equivalent costs or gains, producing asymmetric risk assessments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Emergency CAB escalation decision",
      "decision_point_description": "Whether to push for an emergency change board session instead of waiting for the standard 21-day change cycle.",
      "affected_reasoning_operation": "Risk assessment and evidence weighting",
      "bias_specific_mechanism": "The participant framed the escalation case around severe potential loss outcomes—customer-payment breach, contract penalties, and reputational fallout—and explicitly gave less weight to the downtime risk of an emergency patch attempt. The loss-side narrative dominated the risk trade-off.",
      "manifestation_in_interview": "The participant built the escalation case around what the organization stood to lose and later acknowledged that the emergency-patch downside was not weighed as heavily.",
      "effect_on_reasoning_or_decision": "The decision and pitch favored emergency escalation, with the cost of disruption receiving comparatively weak consideration.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But what really drove how I pitched it to my manager was framing what happens if we don't act — we're talking about a checkout system, so if this gets popped, we're looking at a breached customer-payment flow, contract penalties from at least one retail partner, and reputational fallout that's hard to walk back. I basically built the case around what we stood to lose if we sat on it for 21 days.",
          "evidence_explanation": "Shows active loss-framing of the escalation decision, not a balanced enumeration of gains and losses."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A little, but not as heavily. I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation. I think it got the CAB slot faster because of that.",
          "evidence_explanation": "Explicitly confirms the asymmetry: the recognized downtime risk was underweighted relative to loss-side considerations."
        }
      ],
      "correction_or_counterevidence": "Active exploitation of a Tier-1 revenue-facing system and SLA compliance provided legitimate urgent-risk grounds; the bias claim rests on the participant's own underweighting of the emergency-patch downside.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed loss aversion or framing; classification relies on established decision-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["selective attention", "attentional bias", "confirmatory information search"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to search for, attend to, interpret, or recall information in ways that confirm an existing expectation or task frame while underweighting disconfirming or anomalous signals.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "WAF compensating control validation and DNS anomaly triage",
      "decision_point_description": "How to handle the outbound DNS anomaly that appeared while validating the WAF blocking rule.",
      "affected_reasoning_operation": "Information search and anomaly detection",
      "bias_specific_mechanism": "The participant concentrated on confirming that the WAF signature blocked the known exploit payload pattern. Because the DNS spike did not match the CVE's known indicators, it was deprioritized despite being visible in the same dashboard. The search for evidence confirming the expected threat pattern dominated attention.",
      "manifestation_in_interview": "The DNS anomaly was logged as 'anomalous, monitor' rather than investigated in parallel; a separate analyst escalated it two days later as a possible unrelated compromise indicator.",
      "effect_on_reasoning_or_decision": "A concurrent possible compromise signal was not promptly investigated, delaying independent escalation and response to the DNS anomaly.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, so the dashboard was showing a clean match on the known exploit payload pattern, which is what the ticket was actually about, and I spent most of my time confirming that signature was blocked correctly. The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as 'anomalous, monitor' and moved on.",
          "evidence_explanation": "Demonstrates selective attention to the expected/confirmed exploit pattern and deprioritization of a visible anomaly that did not fit the current task hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered it briefly, but I was heads-down on making sure the WAF rule actually caught the payload variant we had confirmed. Two days later a different analyst ended up escalating that DNS pattern separately as a possible unrelated compromise indicator, so it did turn out to be something.",
          "evidence_explanation": "Confirms the anomaly received only brief consideration and that the participant remained occupied with expected-threat confirmation; the independent escalation documents the signal's relevance."
        }
      ],
      "correction_or_counterevidence": "The participant did log the DNS anomaly for monitoring, so this was not total omission. The bias is in the asymmetric information-search priority rather than complete denial.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage provided a directly usable operational definition for confirmation bias in this anomaly-triaging context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "IKEA effect",
      "alternative_labels": ["not invented here bias", "endowment effect", "status quo bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive tendency to place disproportionately high value on solutions one has personally built or assembled, even when an externally sourced alternative offers stronger objective performance or coverage.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Detection tooling selection",
      "decision_point_description": "Choosing whether to keep the self-built detection script primary or standardize on the vendor SIEM correlation rule.",
      "affected_reasoning_operation": "Technology-selection and risk evaluation",
      "bias_specific_mechanism": "The participant trusted and preferred his self-built script because he built and tuned it, and framed switching to the vendor rule as adding risk mid-incident—even while acknowledging the vendor rule covered more payload variants. Ownership and familiarity inflated the script's perceived relative value.",
      "manifestation_in_interview": "The self-built script remained primary and the vendor rule was placed in a secondary slot. A later variant was missed by the self-built rule but would have been caught by the vendor rule.",
      "effect_on_reasoning_or_decision": "The detection gap persisted because broader vendor coverage was not used as primary detection, resulting in a later missed variant.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us. The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own. I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well.",
          "evidence_explanation": "The justification invokes personal authorship, familiarity, and ownership as decisive factors even after conceding the external rule's broader coverage."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "About a week later a slightly different payload variant showed up that my script didn't flag, but the vendor rule would have caught it. We caught it another way eventually, but it was a gap.",
          "evidence_explanation": "Documents a concrete downstream detection gap attributable to the primary/secondary placement decision."
        }
      ],
      "correction_or_counterevidence": "Caution about switching primary detection during an active incident is a plausible professional risk-management concern; however, the participant explicitly framed his preference around authorship and trust rather than a comparison of verification status.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed the IKEA effect or not-invented-here bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "illusion of control",
      "alternative_labels": ["overconfidence bias", "optimism bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to overestimate one's ability to control or secure an outcome, especially when one has personally implemented or configured the relevant safeguards.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-27 ticket closure decision",
      "decision_point_description": "Deciding whether to close the critical CVE ticket as mitigated with the vendor patch still undeployed.",
      "affected_reasoning_operation": "Residual-risk evaluation and closure judgment",
      "bias_specific_mechanism": "The participant placed substantial weight on the fact that he personally configured the compensating controls, treating that personal implementation as evidence that the exploit path was shut down. This inflated confidence contributed to closure despite unresolved DNS anomaly and detection-gap information.",
      "manifestation_in_interview": "The ticket was closed as adequately mitigated; the participant later stated he felt the pieces he had put in place had it covered, though he acknowledged some uncertainty.",
      "effect_on_reasoning_or_decision": "The closure decision underweighted residual risk, and a post-incident audit later identified a narrow exposure window.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup.",
          "evidence_explanation": "Links confidence in mitigation directly to personal implementation, the central mechanism of illusion of control."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered. A post-incident audit about a month later found there was actually a narrow exposure window that never got closed, though nothing was ever exploited through it.",
          "evidence_explanation": "Shows the confidence was not complete, but also confirms the residual-risk assessment was biased and later identified a gap."
        }
      ],
      "correction_or_counterevidence": "Professional confidence in self-implemented controls can reflect legitimate detailed knowledge; the participant also acknowledged uncertainty. This is classified only as low confidence because a non-bias explanation is plausible.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed illusion of control in operational risk closure; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive heuristic in which the ease or vividness with which an event comes to mind inflates its perceived likelihood, urgency, or relevance, independent of case-specific risk data.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-27 ticket closure decision",
      "decision_point_description": "Whether to close the ticket as mitigated under SLA pressure with unresolved residual items.",
      "affected_reasoning_operation": "Risk urgency and closure decision",
      "bias_specific_mechanism": "A recent, vivid ransomware news story about another company was highly salient and widely discussed by the team. This exemplar increased the perceived urgency to close decisively, leading the participant to give more weight to general urgency than to the ticket's specific residual open items.",
      "manifestation_in_interview": "The participant reported that the news story added to the sense that the ticket needed to be wrapped up and later judged that without that story he would have sat with the open items longer.",
      "effect_on_reasoning_or_decision": "The closure call shifted toward closing as mitigated, despite unresolved DNS anomaly and known detection gap.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open.",
          "evidence_explanation": "Directly documents a salient external exemplar influencing the sense of urgency attached to a separate, specific ticket."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script.",
          "evidence_explanation": "Confirms that general salience-driven urgency outweighed specific residual-risk data in the closure reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then.",
          "evidence_explanation": "Participant's counterfactual directly links the news story to the premature closure impulse, strengthening the availability mechanism."
        }
      ],
      "correction_or_counterevidence": "SLA deadline pressure and compensating controls were legitimate closure inputs; however, the participant's explicit statement that the news story changed his likely behavior isolates the availability mechanism from ordinary deadline management.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed the availability heuristic in this operational context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": ["plan continuation", "commitment to course", "entrapment"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Day-27 ticket closure decision",
      "supporting_interview_quote": "Probably would have chased down the DNS anomaly properly and maybe pushed harder for the actual vendor patch instead of leaning on compensating controls that long.",
      "plausible_mechanism": "SLA deadline and accumulated investment in compensating controls may have created pressure to continue with the existing mitigation plan rather than re-evaluate remaining residual risk.",
      "why_not_identified": "The specific distorting mechanism is confounded with already-identified availability and illusion-of-control effects; the transcript does not isolate a distinct plan-continuation driver."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "affect heuristic",
      "alternative_labels": ["risk-as-feelings", "emotional heuristic"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Day-27 ticket closure decision",
      "supporting_interview_quote": "There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open.",
      "plausible_mechanism": "Emotional urgency from a vivid ransomware example may have shaped risk judgment independently of the specific ticket's residual risk metrics.",
      "why_not_identified": "The more precisely evidenced mechanism is availability/salience; affect is plausibly entangled but not separable enough to justify a further distinct occurrence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrospective self-report can conflate after-the-fact rationalization with in-the-moment reasoning mechanism.",
    "The retrieved corpus consisted largely of topically adjacent cybersecurity and automation papers; it did not provide direct operational definitions for most identified biases.",
    "Single interview; classifications are based on narrative evidence rather than independent behavioral, log, or eye-tracking data.",
    "Low-confidence findings remain positive identifications and should be interpreted cautiously because competing non-bias explanations are possible."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a retrospective walkthrough of a specific vulnerability case you handled, purely for process review — nothing about individual performance evaluation. Can you tell me your role and how long you've been doing vulnerability management? Participant: Sure, no problem. I'm a Vulnerability Management Analyst, I've been in this seat about three years now, before that I did general SOC monitoring. Right now I own triage and remediation tracking for our internet-facing assets, so patch coordination, compensating controls, closing out tickets against our SLA. Interviewer: Great. Walk me through how this particular case started and what you were trying to accomplish. Participant: So this began when our threat intel feed flagged a new CVE, critical, 9.8 on CVSS, and it had confirmed exploitation already happening in the wild. It hit the web framework running underneath our legacy order-processing gateway — that's the system customers hit when they check out, so it's tagged Tier-1 criticality, internet-facing, revenue-generating. My objective was straightforward on paper: get this closed within our 30-day SLA without taking the gateway down during a peak sales stretch. The complication is that gateway is old, it needs vendor coordination to patch, and we had a partial change freeze coming up in about ten days, so the runway to actually get a maintenance window was shrinking fast. On top of that I had two other high-severity tickets open at the same time, so this wasn't the only thing on my plate. Interviewer: Given all that, how did the incident actually unfold, in order? Participant: Day one, the alert comes in, I do initial triage and decide to push for an emergency change board session instead of waiting for the normal 21-day cycle. That gets approved, but it's only a two-hour window, not enough for full regression testing. So around day three, we deploy a WAF rule as an interim compensating control instead of the real patch. While I'm watching the dashboard for that, I notice there's also some odd outbound DNS traffic from the same host, but it's not part of what I'm tracking for this ticket. About a week in, IT Ops points out there's now a vendor SIEM correlation rule available for this CVE family, versus the detection script I'd built myself months earlier, and I decide how to handle that overlap. Then by day 27, with the SLA clock running out and the actual patch still not deployed, I make the call on whether to close the ticket as mitigated. Interviewer: Let's slow down on the first one — the decision to escalate. What made you push for the emergency CAB slot instead of the standard cycle? Participant: Honestly, the exploit-in-the-wild status was the trigger, that's usually a hard line for us. But what really drove how I pitched it to my manager was framing what happens if we don't act — we're talking about a checkout system, so if this gets popped, we're looking at a breached customer-payment flow, contract penalties from at least one retail partner, and reputational fallout that's hard to walk back. I basically built the case around what we stood to lose if we sat on it for 21 days. Interviewer: Did you weigh that against the cost of disrupting the gateway with an emergency patch attempt? Participant: A little, but not as heavily. I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation. I think it got the CAB slot faster because of that. Interviewer: Understood. Second decision point — once you had the WAF rule in place, how did you handle the DNS anomaly you mentioned? Participant: Yeah, so the dashboard was showing a clean match on the known exploit payload pattern, which is what the ticket was actually about, and I spent most of my time confirming that signature was blocked correctly. The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as 'anomalous, monitor' and moved on. My focus was really on validating the compensating control against the threat we knew about. Interviewer: Was there a reason you didn't open a parallel look into the DNS traffic at that point? Participant: I considered it briefly, but I was heads-down on making sure the WAF rule actually caught the payload variant we had confirmed. Two days later a different analyst ended up escalating that DNS pattern separately as a possible unrelated compromise indicator, so it did turn out to be something. At the time, though, it just wasn't where my attention was. Interviewer: Third decision — the detection tooling. What happened there? Participant: Right, so I'd written a detection script for this six months back, tuned it myself against our traffic. When the vendor's SIEM correlation rule came out covering multiple payload variants, IT Ops suggested we just standardize on that instead. I kept my script as the primary and put the vendor rule in a secondary, lower-priority slot. Interviewer: What was the reasoning behind keeping yours in the lead role, given the vendor rule had broader coverage? Participant: I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us. The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own. I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well. Interviewer: Did that decision have downstream effects? Participant: About a week later a slightly different payload variant showed up that my script didn't flag, but the vendor rule would have caught it. We caught it another way eventually, but it was a gap. Interviewer: Last decision point — closing the ticket at day 27. Walk me through that. Participant: At that point we still didn't have the actual vendor patch deployed, just the WAF rule and my script running as compensating controls. The SLA clock was almost out. I closed it as adequately mitigated. Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup. There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open. Interviewer: How much of that closure decision was based on the specific residual-risk data for this ticket versus that broader context? Participant: Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script. I did note those in the ticket, but I don't think I treated them as blocking the closure the way I maybe should have. Interviewer: Was there uncertainty at that point about whether the controls were fully sufficient? Participant: Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered. A post-incident audit about a month later found there was actually a narrow exposure window that never got closed, though nothing was ever exploited through it. Interviewer: If you'd had another week before the SLA deadline, would anything have gone differently? Participant: Probably would have chased down the DNS anomaly properly and maybe pushed harder for the actual vendor patch instead of leaning on compensating controls that long. Interviewer: If that ransomware story hadn't been in the news that week, do you think the closure decision changes? Participant: Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then. Interviewer: And if the vendor SIEM rule had existed from day one, would you have built your own script at all? Participant: Hard to say — probably still would have, honestly, just because I like understanding exactly what's under the hood. Though maybe I'd have made it secondary from the start instead of the other way around. Interviewer: Looking back across the whole case, is there a point where you think you gave one piece of evidence more weight than it really deserved? Participant: Probably the closure call. Between my own confidence in the controls I'd built and everything going on in the news that week, I think I leaned on those more than the actual open items on the ticket. Interviewer: That's really helpful, thank you for walking through it in this much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.83s · gen 277.04s · total 283.5s_

**Retrieved** (ranked by store ranker):
1. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0239 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0239 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0229 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0228 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
5. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0205 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
6. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0201 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
7. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0197 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0179 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0173 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
14. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0167 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
15. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0167 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
16. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _# 592 G t ly; when it was a chore (taking out the garbage), only 44% did so. This dradecrease in_
17. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0163 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
18. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
21. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0159 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs introduced to the model. In both varian_
22. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
23. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# 4. Results The results indicate that users who employ strong password creation practices and f_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0155 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
27. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# 3. Materials and Methods curve (AUC) serving as the primary metric for assessing predictive ac_
28. **ijcma-08-2012-0064.pdf** — 0.0151 (rrf) — _# 378 et al. , 1994), Downloaded from http://www.emerald.com/ijcma/articlepdf/24/4/374/817133/ij_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
31. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
32. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0149 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
34. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0145 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION the same as theirs. However, participants may conclude ci_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
36. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0142 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
37. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0142 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## a nd Prey 212 S experience and dishabituating to deviations from the learned trajectories, be_
40. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0138 (rrf) — _# 6. Conclusions This study provides empirical evidence that heuristicdriven decisionmaking play_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
42. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0138 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
43. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0137 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
44. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0137 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
45. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0135 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0135 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
47. **Lyell Automation bias and verification complexity.pdf** — 0.0135 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
48. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0133 (rrf) — _# across domains and different parts of the search process. 2 Note that our review was not a sys_
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0133 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
50. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0133 (rrf) — _## , Floredana Constantin and Sabina-Cristiana Necula \* 1 Department of Accounting, Business In_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single-interview retrospective process review. The participant's described reasoning was analyzed for affirmative evidence of bias-specific mechanisms; later outcomes were used only as corroborating context, not sole evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "familiarity heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "confirmation bias",
      "alternative_labels": ["expectation bias", "selective attention", "tunnel vision"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to attend to, interpret, or favor information that confirms existing beliefs or expected patterns while discounting information that does not fit those expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Handling of anomalous DNS traffic during WAF validation",
      "decision_point_description": "Whether to open a parallel investigation into odd outbound DNS traffic while validating the WAF rule for the known CVE.",
      "affected_reasoning_operation": "attention allocation and diagnostic interpretation of an unexpected network anomaly",
      "bias_specific_mechanism": "The participant had an existing threat hypothesis organized around the CVE's known indicators. The DNS anomaly did not match those expected indicators, so it was interpreted as unrelated and deprioritized rather than treated as potentially important new or disconfirming evidence.",
      "manifestation_in_interview": "The participant saw the DNS spike in the same dashboard but logged it as 'anomalous, monitor' and continued focusing only on validating the WAF rule against the known payload.",
      "effect_on_reasoning_or_decision": "The anomaly was not escalated by the participant; another analyst escalated it two days later as a possible separate compromise indicator.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as 'anomalous, monitor' and moved on. My focus was really on validating the compensating control against the threat we knew about.",
          "evidence_explanation": "The quote shows the participant used fit with known CVE indicators as the basis for dismissing a new anomaly, consistent with confirmation/expectation-driven selective attention."
        }
      ],
      "correction_or_counterevidence": "The participant had a specific CVE ticket and high workload, so deprioritizing out-of-scope traffic may partly reflect legitimate triage rather than bias. He also said he considered opening a parallel look briefly but did not do so.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage provided a definition or mechanism for confirmation bias; the label derives from widely established cognitive-science knowledge. A retrieved operational-incident paper mentioned confirmation/expectation bias, but only as a label rather than a developed mechanism.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "familiarity heuristic",
      "alternative_labels": ["self-creation bias", "IKEA effect", "status quo bias", "not invented here"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which decisions are disproportionately influenced by what is familiar, known, or self-produced rather than by a full comparative assessment of alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of primary detection tooling after vendor SIEM rule became available",
      "decision_point_description": "Whether to keep the self-built detection script primary or adopt the newly available vendor SIEM correlation rule with broader payload coverage.",
      "affected_reasoning_operation": "evaluation and selection of detection tooling",
      "bias_specific_mechanism": "Trust in the familiar, self-created script and reluctance to hand over something he had personally tuned led to underweighting the objectively broader coverage of the vendor rule.",
      "manifestation_in_interview": "The participant kept his own script as primary and placed the vendor rule in a secondary, lower-priority slot even after acknowledging the vendor rule covered more variants.",
      "effect_on_reasoning_or_decision": "A later payload variant was not flagged by his script but would have been caught by the vendor rule, creating a detection gap.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us. The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own. I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well.",
          "evidence_explanation": "The quote shows a preference based on familiarity and personal investment rather than solely on comparative detection coverage."
        }
      ],
      "correction_or_counterevidence": "The participant gave a plausible operational reason—avoiding mid-incident tooling changes—and knowing a tool's false-positive behavior can be a legitimate reliability consideration. This lowers confidence in a bias classification.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cybersecurity-heuristics paper explicitly discusses the familiarity heuristic as influencing decisions in security-relevant contexts.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf",
          "authors": "Greavu-Şerban et al.",
          "publication_year": "2025",
          "retrieved_passage_or_finding": "To identify the presence of the affect heuristic and the familiarity heuristic on the decisionmaking process regarding the sharing of sensitive data ... the majority of respondents indicated that their decisions regarding the sharing of sensitive information were influenced by social contexts, emotions, and the degree of familiarity with the person they were interacting with.",
          "mechanism_supported_by_source": "The source identifies familiarity as a heuristic that can influence security-relevant decisions.",
          "relevance_to_this_occurrence": "It supports using the familiarity heuristic label for a decision in which familiarity with a self-built tool outweighed broader coverage from a less familiar vendor rule."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence effect",
      "alternative_labels": ["illusion of control", "complacency"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for subjective confidence in one's judgments, controls, or decisions to be systematically greater than warranted by the available evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-27 closure decision under SLA pressure",
      "decision_point_description": "Whether to close the vulnerability ticket as adequately mitigated despite an unresolved DNS anomaly and a known detection gap.",
      "affected_reasoning_operation": "risk judgment and closure decision",
      "bias_specific_mechanism": "The participant's confidence that the exploit path was shut down derived substantially from having personally configured the compensating controls, leading him to treat his own setup as sufficient despite acknowledged uncertainty and unresolved items.",
      "manifestation_in_interview": "The participant stated that he closed the ticket as mitigated partly because he personally configured both controls and was confident the exploit path was shut down.",
      "effect_on_reasoning_or_decision": "Residual-risk items were noted but not treated as blocking; a later audit found a narrow exposure window that was never closed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I closed it as adequately mitigated. Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup.",
          "evidence_explanation": "The quote directly ties closure confidence to personal implementation rather than to itemized residual-risk validation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered.",
          "evidence_explanation": "The quote shows subjective confidence coexisted with admitted uncertainty, consistent with overconfidence rather than calibrated certainty."
        }
      ],
      "correction_or_counterevidence": "The controls may have substantially reduced risk, and nothing was exploited. The post-incident audit finding is not by itself proof that the decision was unreasonable. However, the participant later said he probably leaned on his confidence in the controls more than on the actual open items.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derived from general knowledge of the overconfidence effect; retrieved corpus support for overconfidence in this type of cybersecurity closure decision was not available.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["affect heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge risk, likelihood, or urgency by the ease with which salient or vivid examples come to mind, rather than by a full analysis of the specific evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-27 closure decision under SLA pressure",
      "decision_point_description": "Whether to close the ticket as adequately mitigated based on specific residual-risk data versus broader contextual urgency.",
      "affected_reasoning_operation": "risk/urgency judgment and closure decision",
      "bias_specific_mechanism": "A vivid recent ransomware news story became a highly salient example that increased the felt urgency to close the ticket, even though it was not specific evidence about this ticket's residual risk.",
      "manifestation_in_interview": "The participant reported that the ransomware news story added to the sense that the ticket needed to be wrapped up decisively, and later said that without it he likely would have sat with the open items longer.",
      "effect_on_reasoning_or_decision": "Closure was driven more by general urgency from the salient news event than by itemizing the DNS anomaly and detection gap as blocking conditions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open.",
          "evidence_explanation": "The quote shows a vivid external example influenced the closure urgency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If that ransomware story hadn't been in the news that week, do you think the closure decision changes? Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then.",
          "evidence_explanation": "The counterfactual response explicitly links the news story to the closure decision, strengthening the availability mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant also faced a real SLA deadline and a change freeze, so time pressure was not solely an internal bias. The news story may have carried some rational signal about ransomware risk generally, but it was not specific to this ticket.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derived from general knowledge of the availability heuristic; retrieved corpus support for availability was not available.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "loss aversion",
      "alternative_labels": ["framing effect"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision to escalate to emergency CAB slot",
      "supporting_interview_quote": "A little, but not as heavily. I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation.",
      "plausible_mechanism": "Potential losses from not acting were weighted more heavily than possible downtime losses from acting, influencing the escalation decision and how it was advocated.",
      "why_not_identified": "The interview does not provide an objective baseline showing that the loss weighting was distorted; this may reflect strategic advocacy or a reasonable conclusion that breach consequences were more severe than downtime risk."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective self-report; causal attribution of bias is limited by memory and motivated self-presentation.",
    "No objective normative benchmark for the risk weighting, escalation, or closure decisions is available in the transcript.",
    "Some behaviors may reflect legitimate triage, workload, SLA, change-freeze, or operational constraints rather than cognitive bias.",
    "Retrieved corpus support was partial: familiarity heuristic had suitable support; confirmation, availability, and overconfidence labels rely primarily on general cognitive-science knowledge."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a retrospective walkthrough of a specific vulnerability case you handled, purely for process review — nothing about individual performance evaluation. Can you tell me your role and how long you've been doing vulnerability management? Participant: Sure, no problem. I'm a Vulnerability Management Analyst, I've been in this seat about three years now, before that I did general SOC monitoring. Right now I own triage and remediation tracking for our internet-facing assets, so patch coordination, compensating controls, closing out tickets against our SLA. Interviewer: Great. Walk me through how this particular case started and what you were trying to accomplish. Participant: So this began when our threat intel feed flagged a new CVE, critical, 9.8 on CVSS, and it had confirmed exploitation already happening in the wild. It hit the web framework running underneath our legacy order-processing gateway — that's the system customers hit when they check out, so it's tagged Tier-1 criticality, internet-facing, revenue-generating. My objective was straightforward on paper: get this closed within our 30-day SLA without taking the gateway down during a peak sales stretch. The complication is that gateway is old, it needs vendor coordination to patch, and we had a partial change freeze coming up in about ten days, so the runway to actually get a maintenance window was shrinking fast. On top of that I had two other high-severity tickets open at the same time, so this wasn't the only thing on my plate. Interviewer: Given all that, how did the incident actually unfold, in order? Participant: Day one, the alert comes in, I do initial triage and decide to push for an emergency change board session instead of waiting for the normal 21-day cycle. That gets approved, but it's only a two-hour window, not enough for full regression testing. So around day three, we deploy a WAF rule as an interim compensating control instead of the real patch. While I'm watching the dashboard for that, I notice there's also some odd outbound DNS traffic from the same host, but it's not part of what I'm tracking for this ticket. About a week in, IT Ops points out there's now a vendor SIEM correlation rule available for this CVE family, versus the detection script I'd built myself months earlier, and I decide how to handle that overlap. Then by day 27, with the SLA clock running out and the actual patch still not deployed, I make the call on whether to close the ticket as mitigated. Interviewer: Let's slow down on the first one — the decision to escalate. What made you push for the emergency CAB slot instead of the standard cycle? Participant: Honestly, the exploit-in-the-wild status was the trigger, that's usually a hard line for us. But what really drove how I pitched it to my manager was framing what happens if we don't act — we're talking about a checkout system, so if this gets popped, we're looking at a breached customer-payment flow, contract penalties from at least one retail partner, and reputational fallout that's hard to walk back. I basically built the case around what we stood to lose if we sat on it for 21 days. Interviewer: Did you weigh that against the cost of disrupting the gateway with an emergency patch attempt? Participant: A little, but not as heavily. I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation. I think it got the CAB slot faster because of that. Interviewer: Understood. Second decision point — once you had the WAF rule in place, how did you handle the DNS anomaly you mentioned? Participant: Yeah, so the dashboard was showing a clean match on the known exploit payload pattern, which is what the ticket was actually about, and I spent most of my time confirming that signature was blocked correctly. The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as 'anomalous, monitor' and moved on. My focus was really on validating the compensating control against the threat we knew about. Interviewer: Was there a reason you didn't open a parallel look into the DNS traffic at that point? Participant: I considered it briefly, but I was heads-down on making sure the WAF rule actually caught the payload variant we had confirmed. Two days later a different analyst ended up escalating that DNS pattern separately as a possible unrelated compromise indicator, so it did turn out to be something. At the time, though, it just wasn't where my attention was. Interviewer: Third decision — the detection tooling. What happened there? Participant: Right, so I'd written a detection script for this six months back, tuned it myself against our traffic. When the vendor's SIEM correlation rule came out covering multiple payload variants, IT Ops suggested we just standardize on that instead. I kept my script as the primary and put the vendor rule in a secondary, lower-priority slot. Interviewer: What was the reasoning behind keeping yours in the lead role, given the vendor rule had broader coverage? Participant: I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us. The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own. I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well. Interviewer: Did that decision have downstream effects? Participant: About a week later a slightly different payload variant showed up that my script didn't flag, but the vendor rule would have caught it. We caught it another way eventually, but it was a gap. Interviewer: Last decision point — closing the ticket at day 27. Walk me through that. Participant: At that point we still didn't have the actual vendor patch deployed, just the WAF rule and my script running as compensating controls. The SLA clock was almost out. I closed it as adequately mitigated. Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup. There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open. Interviewer: How much of that closure decision was based on the specific residual-risk data for this ticket versus that broader context? Participant: Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script. I did note those in the ticket, but I don't think I treated them as blocking the closure the way I maybe should have. Interviewer: Was there uncertainty at that point about whether the controls were fully sufficient? Participant: Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered. A post-incident audit about a month later found there was actually a narrow exposure window that never got closed, though nothing was ever exploited through it. Interviewer: If you'd had another week before the SLA deadline, would anything have gone differently? Participant: Probably would have chased down the DNS anomaly properly and maybe pushed harder for the actual vendor patch instead of leaning on compensating controls that long. Interviewer: If that ransomware story hadn't been in the news that week, do you think the closure decision changes? Participant: Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then. Interviewer: And if the vendor SIEM rule had existed from day one, would you have built your own script at all? Participant: Hard to say — probably still would have, honestly, just because I like understanding exactly what's under the hood. Though maybe I'd have made it secondary from the start instead of the other way around. Interviewer: Looking back across the whole case, is there a point where you think you gave one piece of evidence more weight than it really deserved? Participant: Probably the closure call. Between my own confidence in the controls I'd built and everything going on in the news that week, I think I leaned on those more than the actual open items on the ticket. Interviewer: That's really helpful, thank you for walking through it in this much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.03s · gen 293.55s · total 299.5s_

**Retrieved** (ranked by store ranker):
1. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0239 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0239 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0229 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0228 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
5. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0205 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
6. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0201 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
7. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0197 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0179 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0173 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
14. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0167 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
15. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0167 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
16. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _# 592 G t ly; when it was a chore (taking out the garbage), only 44% did so. This dradecrease in_
17. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0163 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
18. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
21. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0159 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs introduced to the model. In both varian_
22. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
23. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# 4. Results The results indicate that users who employ strong password creation practices and f_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0155 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
27. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# 3. Materials and Methods curve (AUC) serving as the primary metric for assessing predictive ac_
28. **ijcma-08-2012-0064.pdf** — 0.0151 (rrf) — _# 378 et al. , 1994), Downloaded from http://www.emerald.com/ijcma/articlepdf/24/4/374/817133/ij_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
31. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
32. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0149 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
34. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0145 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION the same as theirs. However, participants may conclude ci_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
36. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0142 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
37. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0142 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## a nd Prey 212 S experience and dishabituating to deviations from the learned trajectories, be_
40. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0138 (rrf) — _# 6. Conclusions This study provides empirical evidence that heuristicdriven decisionmaking play_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
42. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0138 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
43. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0137 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
44. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0137 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
45. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0135 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0135 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
47. **Lyell Automation bias and verification complexity.pdf** — 0.0135 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
48. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0133 (rrf) — _# across domains and different parts of the search process. 2 Note that our review was not a sys_
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0133 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
50. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0133 (rrf) — _## , Floredana Constantin and Sabina-Cristiana Necula \* 1 Department of Accounting, Business In_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first analysis of participant self-reported reasoning in a vulnerability-management CTA interview. Only bias-specific mechanisms affirmatively evidenced by the transcript were classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "familiarity heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "loss aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "loss aversion",
      "alternative_labels": [
        "framing effect",
        "negativity bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to weigh potential losses more heavily than equivalent gains or competing risks, especially when outcomes are framed in terms of losses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Emergency CAB escalation decision",
      "decision_point_description": "Choosing whether to push for an emergency change board slot instead of the normal 21-day cycle for a critical CVE.",
      "affected_reasoning_operation": "Weighing risks and benefits of emergency escalation and framing the case to management.",
      "bias_specific_mechanism": "The participant constructed and weighted the escalation decision around the vivid potential losses of inaction—breach, contract penalties, reputational harm—while explicitly giving less weight to the potential disruption risk of the emergency patch.",
      "manifestation_in_interview": "When describing the pitch to management, the participant framed the argument primarily in terms of what would be lost by waiting and acknowledged that the downtime risk was noted but not weighed as heavily.",
      "effect_on_reasoning_or_decision": "The loss-framed argument carried the conversation and likely accelerated the emergency CAB slot, with decision weight concentrated on breach and penalty losses rather than equal consideration of operational disruption risk.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But what really drove how I pitched it to my manager was framing what happens if we don't act — we're talking about a checkout system, so if this gets popped, we're looking at a breached customer-payment flow, contract penalties from at least one retail partner, and reputational fallout that's hard to walk back.",
          "evidence_explanation": "This quote shows the escalation case was built primarily as a loss-framed narrative, emphasizing potential harms of inaction."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation. I think it got the CAB slot faster because of that.",
          "evidence_explanation": "This quote explicitly reports asymmetric weighting: the potential loss side was treated as more influential than the operational downside."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A little, but not as heavily.",
          "evidence_explanation": "This answer directly confirms that disruption risk was considered less heavily than loss-related concerns."
        }
      ],
      "correction_or_counterevidence": "Exploit-in-the-wild status and Tier-1 criticality provided a legitimate non-bias basis for escalation; the potential operating-risk was not entirely ignored and was mentioned in the ticket.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly supported loss aversion or framing; the label rests on established general-knowledge bias taxonomy.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "familiarity heuristic",
      "alternative_labels": [
        "status quo bias",
        "familiarity bias",
        "not-invented-here bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A judgmental heuristic in which familiar, well-known options are preferred over less familiar alternatives, even when objective evidence favors the unfamiliar alternative.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Detection tooling overlap decision",
      "decision_point_description": "Choosing whether to adopt the new vendor SIEM correlation rule as the primary detection or keep the participant-built script in the lead role.",
      "affected_reasoning_operation": "Comparing and selecting detection tools under incident time pressure.",
      "bias_specific_mechanism": "The participant relied on familiarity with his self-built script and treated the unfamiliarity of the vendor rule as a source of risk, despite acknowledging that the vendor rule had objectively broader variant coverage.",
      "manifestation_in_interview": "The participant kept his own script as primary and placed the broader vendor rule in a lower-priority slot, explicitly citing trust, ownership, and reluctance to change something already working.",
      "effect_on_reasoning_or_decision": "The familiar self-built script remained primary; approximately one week later, a payload variant was missed that the vendor rule would have caught.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us.",
          "evidence_explanation": "This shows the decision was anchored in familiarity with and ownership of the existing tool rather than objective coverage."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own.",
          "evidence_explanation": "This shows the unfamiliar alternative was evaluated as riskier primarily because it was new, not because of evidence that it would perform worse."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well.",
          "evidence_explanation": "This explicitly demonstrates that objective coverage information was subordinated to familiarity and ownership preferences."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the vendor rule's broader coverage, and a later detection gap demonstrated a concrete downside. However, the stated reason for resisting the switch was not an evidence-based reliability problem with the vendor rule.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Greavu-Şerban et al. (2025) was used to ground the familiarity heuristic.",
      "corpus_evidence": [
        {
          "source_identifier": "Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf",
          "paper_title": "Exploring Heuristics and Biases in Cybersecurity: A Factor Analysis of Social Engineering Vulnerabilities",
          "authors": "Greavu-Şerban et al.",
          "publication_year": "2025",
          "retrieved_passage_or_finding": "To identify the presence of the affect heuristic and the familiarity heuristic on the decisionmaking process regarding the sharing of sensitive data, the following question was posed: ‘Have you ever provided sensitive information to acquaintances or close individuals?’ According to the collected responses, the majority of respondents indicated that their decisions regarding the sharing of sensitive information were influenced by social contexts, emotions, and the degree of familiarity with the person they were interacting with.",
          "mechanism_supported_by_source": "The passage supports the familiarity heuristic as a decision-making influence: individuals rely on the degree of familiarity with an entity when deciding how to act, potentially overriding other considerations.",
          "relevance_to_this_occurrence": "Although the source context is social engineering data sharing, the same general mechanism appears here: the participant relied on familiarity with his own detection script when deciding to keep it primary over the unfamiliar vendor rule."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence bias",
      "alternative_labels": [
        "overconfidence effect",
        "illusion of control"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a person's subjective confidence in their judgment or decision to exceed the objective evidence or accuracy, leading them to discount residual uncertainty.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day 27 ticket closure decision: control sufficiency",
      "decision_point_description": "Choosing whether to close the ticket as adequately mitigated given that the vendor patch was still not deployed and residual-risk items remained open.",
      "affected_reasoning_operation": "Assessing whether personally configured compensating controls were sufficient to close the ticket.",
      "bias_specific_mechanism": "The participant's confidence that the exploit path was covered was inflated by the fact that he had personally configured the controls, causing him to underweight the specific unresolved items on the ticket.",
      "manifestation_in_interview": "The participant reported feeling confident the exploit path was shut down because of his own setup, acknowledged uncertainty, but still treated unresolved DNS and detection-gap items as non-blocking.",
      "effect_on_reasoning_or_decision": "The ticket was closed as adequately mitigated even though the DNS anomaly had not been fully resolved and the detection script had a known coverage gap.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup.",
          "evidence_explanation": "This quote directly links the closure decision to confidence derived from personal configuration of the controls."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered.",
          "evidence_explanation": "This shows subjective confidence persisted despite acknowledged uncertainty."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did note those in the ticket, but I don't think I treated them as blocking the closure the way I maybe should have.",
          "evidence_explanation": "This shows that specific residual-risk items were available but were underweighted in the closure judgment."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged uncertainty and noted the open items in the ticket; however, those items were not treated as blocking, which is consistent with overconfidence having affected the residual-risk assessment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly supported overconfidence bias or illusion of control; the label rests on established general-knowledge bias taxonomy.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "affect heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or urgency of events based on how easily examples come to mind, often making recent or emotionally salient cases disproportionately influential.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day 27 ticket closure decision: urgency from recent news",
      "decision_point_description": "Choosing whether to close the ticket as mitigated while under SLA pressure and influenced by a recent ransomware news story.",
      "affected_reasoning_operation": "Judging how urgently the ticket needed to be closed and whether residual risks should be treated as blocking.",
      "bias_specific_mechanism": "A recent, emotionally salient ransomware news story was easily available in the participant's mind and inflated the sense that the ticket needed to be wrapped up decisively, rather than evaluating the ticket-specific residual risk.",
      "manifestation_in_interview": "The participant stated that the news story added to the sense of needing decisive closure and that more weight went to the general sense of urgency than to itemizing the specific open items.",
      "effect_on_reasoning_or_decision": "The closure decision was driven partly by generalized urgency from the salient news event; the participant indicated that without the news story he likely would have sat with the open items longer.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open.",
          "evidence_explanation": "This quote directly identifies the news story as influencing the felt need for closure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script.",
          "evidence_explanation": "This quote explicitly contrasts the availability-driven urgency with the ticket-specific evidence that should have been weighed."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then.",
          "evidence_explanation": "This counterfactual answer supports the causal role of the news story in the closure decision."
        }
      ],
      "correction_or_counterevidence": "SLA pressure and the existence of compensating controls were legitimate decision inputs, but the participant's own account indicates the general news-driven urgency outweighed specific residual-risk analysis.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly supported the availability heuristic; the label rests on established general-knowledge bias taxonomy.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "attentional bias",
      "alternative_labels": [
        "confirmation bias",
        "selective attention"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Handling anomalous outbound DNS traffic observed from the same host while validating WAF rule",
      "supporting_interview_quote": "The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as 'anomalous, monitor' and moved on. My focus was really on validating the compensating control against the threat we knew about.",
      "plausible_mechanism": "Possible narrowing of attention toward the confirmed exploit payload and known indicators, reducing exploration of an unrelated anomaly in the same dashboard.",
      "why_not_identified": "The transcript also supports ordinary triage under task load and ticket scope: the anomaly was logged for monitoring rather than ignored, and a different analyst later escalated it. There is insufficient affirmative evidence that a bias-specific mechanism, rather than legitimate prioritization, caused the decision."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieval coverage was sparse for several identified labels; loss aversion, overconfidence bias, and availability heuristic classifications rely on established general knowledge rather than retrieved corpus support.",
    "The transcript is retrospective self-report, so bias classifications are based on the participant's own description of prior reasoning rather than direct observation of real-time behavior."
  ]
}

