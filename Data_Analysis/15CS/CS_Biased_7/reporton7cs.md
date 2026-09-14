# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for an internal case study on incident decision-making — nothing you say will be attributed outside this review. Participant: That's fine, happy to walk through it. Interviewer: Great. Can you start with your role and what you're responsible for day to day? Participant: I'm CISO at NorthGate Financial. We're a payments company — card and ACH processing, about 450 employees. I own the security program end to end: SOC operations, vendor risk, incident response, board reporting, budget. Small team, six people in the SOC, so I'm hands-on more than I'd be at a bigger shop. Interviewer: Tell me about the incident you want to discuss, and what you were trying to accomplish overall. Participant: Sure. This was a stretch about ten days ago where an intrusion overlapped with our annual vendor renewal cycle, which was already a bad coincidence. The objective was straightforward in theory — detect and contain whatever was happening without taking payments processing offline, and get our vendor contracts and budget numbers finalized on schedule. In practice those two things kept colliding. Our SIEM flagged an anomalous login on a jump server one of our payments engineers uses — off-hours access, from a network range we hadn't seen for that account before. The SIEM auto-scored it Medium severity based on its default model. That model doesn't know the account is privileged, it just looks at pattern deviation. I remember looking at it and thinking, okay, Medium, that tracks with what I'm seeing, and we went from there. One analyst was handling triage that day — we were down a person on leave — so scope mattered. There'd also been a second alert nine minutes earlier on an adjacent auth server, lower priority, and it just didn't get opened at that point; the jump server was the concrete thing in front of us. Interviewer: What happened next? Participant: We had the analyst dig into the jump server specifically — process history, recent auth events, that kind of thing. A few hours in, once we circled back to close out the queue, we noticed the earlier auth-server alert shared the same source IP range. That's when it stopped looking like an isolated anomaly and started looking like lateral movement toward the payments database segment. Interviewer: Let's go through the sequence in order. What did you know, and when? Participant: At the start, just the jump-server alert and its Medium score. A couple hours later, the IP overlap with the auth-server alert. That afternoon, the vendor renewal deadline hit — we had five business days before our EDR and threat-intel contract auto-renewed, and that decision needed to happen regardless of the incident. That evening, once lateral movement was confirmed, my team wrote a monitoring script overnight to watch the compromised account, and I had a call with the CFO about containment options. Two days later, once things were stable, I had to submit a remediation budget number to the board. Interviewer: Let's slow down at that first decision — the triage call. What cues stood out, and was anything competing for your attention? Participant: The privileged nature of the account stood out to me, honestly, but the Medium score was already sitting there, and it's usually a decent starting point for how urgently we move. I didn't pull in the second alert as something to check in parallel — the analyst was already stretched, and the jump server was the concrete lead. Interviewer: What alternatives did you weigh, and what tipped it? Participant: Escalating both alerts jointly right away, or asking for a correlation sweep across that time window before locking in severity. I didn't do either. The score gave me a number to anchor the conversation around, and given we were short-staffed, narrowing the analyst's focus felt efficient rather than risky at the time. Interviewer: How confident were you in that assessment? Participant: Reasonably, but not fully — I knew the automated score doesn't factor in account privilege. I just didn't push past it that morning. Interviewer: Moving to the vendor decision — walk me through that one. Participant: We'd used this EDR and threat-intel vendor six years. My team built a lot of custom detection logic and dashboards on top of their platform. Procurement had actually flagged three other vendors as offering comparable bundles this cycle, but I didn't go through that list closely. A couple of peer CISOs mentioned they use either this vendor or one close competitor, so my real comparison ended up being just those two. Interviewer: What made you settle on renewing? Participant: Mostly the investment already sitting in our detection rules and dashboards — rebuilding that on a new platform is real time and real risk during a period we're trying to stay stable. I didn't formally validate that the incumbent still outperforms the alternatives; it was more that switching felt costly given what we'd already built. Honestly, having built all of that ourselves on top of their platform just made the incumbent feel like the stronger product outright, even though I didn't have a current benchmark or a comparable bid on file that actually backed that up. Interviewer: Did the live incident affect that judgment at all? Participant: Maybe implicitly — I wasn't eager to introduce a new tool mid-incident. But the underlying reasoning was really about the sunk integration work, not the incident timing. Interviewer: Third decision point — containment, once lateral movement was confirmed. Participant: This was the hardest one. The IR retainer firm recommended full segment isolation, pending forensics, because there wasn't confirmed proof isolation would fully stop the threat — just that it was the safer play. My team had put together an overnight monitoring script watching the compromised account specifically. The CFO's position was blunt: isolating payments meant a guaranteed same-day hit, about $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was framed more as 'reduces risk,' not a number. Given the script gave us visibility on that account, I went with the targeted lockout and monitoring instead of full isolation. Interviewer: What was decisive there? Participant: Honestly, the guaranteed dollar figure against an unquantified benefit made the isolation option feel like the more expensive one, dollar for dollar, even though I couldn't put a number on the other side. And I felt like the script had that account covered. Interviewer: At the time, how confident were you that the script and lockout actually covered the paths the intruder could take? Participant: Fairly confident, honestly. Once we had that account locked and the script watching for any reuse, I felt like we'd boxed the intrusion in. I didn't have the team specifically test whether it would catch token reuse from a different host or a parallel session somewhere else in the environment — I more or less assumed that shutting down that one account's avenues was enough to hold the line while forensics caught up. Interviewer: What happened afterward? Participant: About two hours later, the same compromised credentials touched a second internal system the script wasn't watching. Forensics later found a small amount of data had already been exfiltrated before we even had the script running. Interviewer: Last decision point — the board budget recommendation. Participant: We'd scoped a privileged-access segmentation project eighteen months ago at $240,000, never funded. This week, with the incident fresh, I gathered current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since cloud components were added. The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes. Interviewer: Why start from the old figure rather than the new quotes? Participant: It was already the reference point I had in my head from planning cycles past. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work. Interviewer: If the SIEM hadn't pre-scored that first alert, do you think your response would have gone differently? Participant: Possibly — without a number already on the screen, I might have leaned harder on the account's privilege level from the start, and maybe caught the auth-server overlap sooner. Interviewer: What if the CFO's number hadn't been quantified? Participant: I think I'd have weighed the isolation call less as a straight cost comparison and spent more time pressing the IR firm on what 'reduces risk' actually meant in concrete terms. Interviewer: Looking back, anything you'd tell yourself facing that budget deadline again with a stale internal estimate on file? Participant: Get fresh numbers before you anchor on the old one — even under deadline pressure, a couple of quotes reframes the whole conversation.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 6.80s · gen 246.97s · total 256.7s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0260 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0239 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0233 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0227 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0210 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0207 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0204 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0195 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0185 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
11. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0184 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
12. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0181 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
13. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0176 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0176 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
15. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0175 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0168 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0165 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
19. **ijcma-08-2012-0064.pdf** — 0.0163 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
21. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
23. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0159 (rrf) — _### cKniff study, we focus on stress as stimuli perceived by individuals in the environment and _
24. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0159 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
25. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0159 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 agreement with the AI prediction. Thus, by measuring t_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0159 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
28. **Hallihan_etal_DTM_12.pdf** — 0.0157 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
29. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0156 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
30. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0156 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
31. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0155 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
32. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0154 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
33. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0153 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0151 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
35. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0150 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
37. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
39. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0149 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
40. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
41. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0147 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
42. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0147 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
44. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0146 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
45. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0144 (rrf) — _# 188 simulated AI always provided suggestions for replacing the ingredient highest in carbohydr_
46. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0141 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
49. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0138 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
50. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0137 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of the participant's incident decision-making; only affirmative, evidence-grounded bias mechanisms were classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring-and-adjustment heuristic", "adjustment insufficiency"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information when making subsequent judgments, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial triage of SIEM jump-server alert",
      "decision_point_description": "Whether to escalate the jump-server alert alone as Medium severity or jointly investigate the earlier auth-server alert and account privilege.",
      "affected_reasoning_operation": "Severity assessment and triage prioritization",
      "bias_specific_mechanism": "The SIEM severity score served as an initial numeric anchor. The participant explicitly used that score as the reference point and did not sufficiently adjust for known information the score omitted, namely the privileged nature of the account.",
      "manifestation_in_interview": "The participant reported seeing the Medium score, thinking it matched what he saw, and using it to anchor the team's response despite knowing the automated model did not factor account privilege.",
      "effect_on_reasoning_or_decision": "Narrowed the initial investigation to the jump-server alert and delayed discovery of the overlapping auth-server alert by several hours.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember looking at it and thinking, okay, Medium, that tracks with what I'm seeing, and we went from there.",
          "evidence_explanation": "Shows immediate acceptance of the pre-existing Medium score as the assessment frame."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The score gave me a number to anchor the conversation around, and given we were short-staffed, narrowing the analyst's focus felt efficient rather than risky at the time.",
          "evidence_explanation": "Explicitly identifies the score as an anchor that structured the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Reasonably, but not fully — I knew the automated score doesn't factor in account privilege. I just didn't push past it that morning.",
          "evidence_explanation": "Demonstrates known information was under-adjusted relative to the anchor."
        }
      ],
      "correction_or_counterevidence": "Later in the incident, the team noticed the auth-server alert shared the same source IP range and broadened the investigation. Resource constraints and use of the automated score as an initial heuristic may be mitigating factors, but they do not eliminate the anchoring mechanism because the participant explicitly described insufficient adjustment from the score.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Rastogi et al. (2022) passage supports the anchoring-and-adjustment heuristic in AI-assisted decision-making.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "The retrieved paper discusses anchoring bias and the anchoring-and-adjustment heuristic. It reports that participants' likelihood of sufficiently adjusting away from an incorrect AI prediction increased as time allocated increased, and frames anchoring-and-adjustment as a resource-rational tradeoff between time and accuracy.",
          "mechanism_supported_by_source": "Anchoring-and-adjustment heuristic: initial anchors influence decision-making and adjustment away from them may be insufficient.",
          "relevance_to_this_occurrence": "Supports the mechanism by which the SIEM severity score acted as an anchor and the participant did not sufficiently adjust for account privilege."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": ["escalation of commitment", "sunk-cost effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to favor an existing or previously invested-in option because of unrecoverable prior investments of time, effort, or money, even though those sunk costs should not influence forward-looking choice.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor renewal decision during annual renewal cycle",
      "decision_point_description": "Whether to renew the incumbent EDR/threat-intel vendor or evaluate and potentially switch to procurement-flagged alternatives.",
      "affected_reasoning_operation": "Vendor preference and comparative product evaluation",
      "bias_specific_mechanism": "Past effort and custom integration work on the incumbent platform made the product feel stronger and made switching feel more costly, despite the absence of current benchmark or comparable bid data supporting incumbent superiority.",
      "manifestation_in_interview": "The participant reported not reviewing procurement's three comparable vendors and inferred incumbent strength from prior build effort rather than current performance evidence.",
      "effect_on_reasoning_or_decision": "Reduced the comparison set to two familiar vendors and favored renewing the incumbent without formal validation that it still outperformed alternatives.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, having built all of that ourselves on top of their platform just made the incumbent feel like the stronger product outright, even though I didn't have a current benchmark or a comparable bid on file that actually backed that up.",
          "evidence_explanation": "Directly links prior integration work to enhanced product evaluation without supporting performance evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But the underlying reasoning was really about the sunk integration work, not the incident timing.",
          "evidence_explanation": "The participant himself names sunk integration work as the core driver."
        }
      ],
      "correction_or_counterevidence": "There were legitimate forward-looking switching costs and stability concerns, and procurement alternatives were not formally evaluated; these may partially explain the renewal. However the explicit attribution of product strength to prior build effort is consistent with sunk cost reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context directly addressed sunk cost fallacy or escalation of commitment. Classification uses established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": ["complacency", "overreliance on automation", "false sense of security"],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient verification or monitoring of an automated system's coverage or recommendations because of overtrust, leading to reduced information sampling or assumption of effectiveness.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment decision after lateral movement confirmation",
      "decision_point_description": "Whether to follow the IR retainer's recommendation for full segment isolation or use targeted lockout plus an overnight monitoring script.",
      "affected_reasoning_operation": "Risk assessment and evaluation of containment coverage",
      "bias_specific_mechanism": "The participant's confidence in the monitoring script led him to assume the script provided adequate coverage of the compromised account's avenues without testing whether it would catch token reuse from a different host or parallel session.",
      "manifestation_in_interview": "He stated he felt the script had the account covered and that the team did not test alternative paths, instead assuming shutting down one account's avenues was sufficient.",
      "effect_on_reasoning_or_decision": "This overtrust in the automated script contributed to selecting targeted lockout instead of full isolation; a second system was later touched outside script coverage.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "And I felt like the script had that account covered.",
          "evidence_explanation": "Shows reliance on the automated monitoring script as the primary reason for choosing targeted containment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have the team specifically test whether it would catch token reuse from a different host or a parallel session somewhere else in the environment — I more or less assumed that shutting down that one account's avenues was enough to hold the line while forensics caught up.",
          "evidence_explanation": "Demonstrates insufficient verification of automation coverage and assumption of effectiveness."
        }
      ],
      "correction_or_counterevidence": "The script was a reasonable temporary monitoring control under time pressure, but the explicit absence of testing alternative paths makes the confidence in its coverage a complacency-type overtrust. The later compromise of a second internal system is noted only as subsequent resolution, not as retrospective evidence.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Parasuraman and Manzey (2010) supports complacency in human-automation interaction, defined as insufficient verification of automated aid recommendations or coverage.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman and Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "The retrieved review discusses complacency in human use of automation. It describes operationalizing complacency by measuring whether participants verified automated diagnoses before accepting them; participants sampling less information than necessary to completely verify an aid's recommendation were considered complacent.",
          "mechanism_supported_by_source": "Complacency arises when operators sample less information than needed to verify automation, producing overtrust in the automated aid.",
          "relevance_to_this_occurrence": "The participant did not have the team verify whether the monitoring script caught alternative credential reuse, consistent with insufficient automation verification."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring-and-adjustment heuristic", "insufficient adjustment from stale estimate"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information when making subsequent judgments, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Board remediation budget recommendation",
      "decision_point_description": "Choosing a single remediation budget number for the board after receiving updated quotes of $310,000 to $340,000.",
      "affected_reasoning_operation": "Budget estimation and recommendation",
      "bias_specific_mechanism": "The prior unfunded estimate of $240,000 served as a mental reference point; the participant adjusted slightly upward from that stale anchor rather than building the recommendation from current quotes.",
      "manifestation_in_interview": "The participant said the old figure was already the reference point and that adjusting it felt like less friction than justifying the higher current quote.",
      "effect_on_reasoning_or_decision": "The submitted board number was based on an outdated estimate rather than current vendor quotes, potentially understating required remediation funding.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It was already the reference point I had in my head from planning cycles past. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work.",
          "evidence_explanation": "Explicitly identifies the old estimate as the anchor and describes insufficient adjustment from it."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Get fresh numbers before you anchor on the old one — even under deadline pressure, a couple of quotes reframes the whole conversation.",
          "evidence_explanation": "Participant retrospectively identifies the anchor-on-old-number mechanism as the key failure."
        }
      ],
      "correction_or_counterevidence": "The participant later reflected that obtaining fresh quotes would have been better. Deadline pressure and lack of scoping work are contextual factors, but they do not negate the anchoring mechanism.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Rastogi et al. (2022) passage supports the anchoring-and-adjustment heuristic.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "The retrieved paper discusses anchoring bias and the anchoring-and-adjustment heuristic. It reports that participants' likelihood of sufficiently adjusting away from an incorrect AI prediction increased as time allocated increased, and frames anchoring-and-adjustment as a resource-rational tradeoff between time and accuracy.",
          "mechanism_supported_by_source": "Anchoring-and-adjustment heuristic: initial anchors influence decision-making and adjustment away from them may be insufficient.",
          "relevance_to_this_occurrence": "Supports the mechanism by which the prior $240,000 estimate served as an anchor and the participant adjusted insufficiently from it."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "certainty effect",
      "alternative_labels": ["salience of quantified loss", "certainty bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Containment decision after lateral movement confirmation",
      "supporting_interview_quote": "Honestly, the guaranteed dollar figure against an unquantified benefit made the isolation option feel like the more expensive one, dollar for dollar, even though I couldn't put a number on the other side.",
      "plausible_mechanism": "Overweighting a certain, concrete $180,000 processing-fee loss relative to an unquantified security risk reduction.",
      "why_not_identified": "Could reflect a rational or preference-based risk tolerance toward guaranteed operational costs under uncertainty; the transcript does not establish that the comparison violated the participant's actual utility function or that a distinct bias mechanism was the sole driver."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "availability bias",
      "alternative_labels": ["salience bias", "attentional bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial triage of SIEM jump-server alert",
      "supporting_interview_quote": "the jump server was the concrete thing in front of us.",
      "plausible_mechanism": "The concrete and salient jump-server alert dominated attention while the earlier lower-priority auth-server alert was not opened in parallel.",
      "why_not_identified": "Resource constraints and analyst workload provide a strong non-bias explanation; focusing narrowly may have been an operational priority rather than a distinct availability or salience distortion."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Single interview transcript; no objective behavioral data or independent incident records were available to verify decision quality.",
    "Retrieved corpus support was limited; not all bias labels had directly retrieved passages.",
    "Analysis excludes outcome-based imputation; later outcomes were used only for correction context.",
    "Some plausible non-bias explanations remain for moderate-confidence findings."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for an internal case study on incident decision-making — nothing you say will be attributed outside this review. Participant: That's fine, happy to walk through it. Interviewer: Great. Can you start with your role and what you're responsible for day to day? Participant: I'm CISO at NorthGate Financial. We're a payments company — card and ACH processing, about 450 employees. I own the security program end to end: SOC operations, vendor risk, incident response, board reporting, budget. Small team, six people in the SOC, so I'm hands-on more than I'd be at a bigger shop. Interviewer: Tell me about the incident you want to discuss, and what you were trying to accomplish overall. Participant: Sure. This was a stretch about ten days ago where an intrusion overlapped with our annual vendor renewal cycle, which was already a bad coincidence. The objective was straightforward in theory — detect and contain whatever was happening without taking payments processing offline, and get our vendor contracts and budget numbers finalized on schedule. In practice those two things kept colliding. Our SIEM flagged an anomalous login on a jump server one of our payments engineers uses — off-hours access, from a network range we hadn't seen for that account before. The SIEM auto-scored it Medium severity based on its default model. That model doesn't know the account is privileged, it just looks at pattern deviation. I remember looking at it and thinking, okay, Medium, that tracks with what I'm seeing, and we went from there. One analyst was handling triage that day — we were down a person on leave — so scope mattered. There'd also been a second alert nine minutes earlier on an adjacent auth server, lower priority, and it just didn't get opened at that point; the jump server was the concrete thing in front of us. Interviewer: What happened next? Participant: We had the analyst dig into the jump server specifically — process history, recent auth events, that kind of thing. A few hours in, once we circled back to close out the queue, we noticed the earlier auth-server alert shared the same source IP range. That's when it stopped looking like an isolated anomaly and started looking like lateral movement toward the payments database segment. Interviewer: Let's go through the sequence in order. What did you know, and when? Participant: At the start, just the jump-server alert and its Medium score. A couple hours later, the IP overlap with the auth-server alert. That afternoon, the vendor renewal deadline hit — we had five business days before our EDR and threat-intel contract auto-renewed, and that decision needed to happen regardless of the incident. That evening, once lateral movement was confirmed, my team wrote a monitoring script overnight to watch the compromised account, and I had a call with the CFO about containment options. Two days later, once things were stable, I had to submit a remediation budget number to the board. Interviewer: Let's slow down at that first decision — the triage call. What cues stood out, and was anything competing for your attention? Participant: The privileged nature of the account stood out to me, honestly, but the Medium score was already sitting there, and it's usually a decent starting point for how urgently we move. I didn't pull in the second alert as something to check in parallel — the analyst was already stretched, and the jump server was the concrete lead. Interviewer: What alternatives did you weigh, and what tipped it? Participant: Escalating both alerts jointly right away, or asking for a correlation sweep across that time window before locking in severity. I didn't do either. The score gave me a number to anchor the conversation around, and given we were short-staffed, narrowing the analyst's focus felt efficient rather than risky at the time. Interviewer: How confident were you in that assessment? Participant: Reasonably, but not fully — I knew the automated score doesn't factor in account privilege. I just didn't push past it that morning. Interviewer: Moving to the vendor decision — walk me through that one. Participant: We'd used this EDR and threat-intel vendor six years. My team built a lot of custom detection logic and dashboards on top of their platform. Procurement had actually flagged three other vendors as offering comparable bundles this cycle, but I didn't go through that list closely. A couple of peer CISOs mentioned they use either this vendor or one close competitor, so my real comparison ended up being just those two. Interviewer: What made you settle on renewing? Participant: Mostly the investment already sitting in our detection rules and dashboards — rebuilding that on a new platform is real time and real risk during a period we're trying to stay stable. I didn't formally validate that the incumbent still outperforms the alternatives; it was more that switching felt costly given what we'd already built. Honestly, having built all of that ourselves on top of their platform just made the incumbent feel like the stronger product outright, even though I didn't have a current benchmark or a comparable bid on file that actually backed that up. Interviewer: Did the live incident affect that judgment at all? Participant: Maybe implicitly — I wasn't eager to introduce a new tool mid-incident. But the underlying reasoning was really about the sunk integration work, not the incident timing. Interviewer: Third decision point — containment, once lateral movement was confirmed. Participant: This was the hardest one. The IR retainer firm recommended full segment isolation, pending forensics, because there wasn't confirmed proof isolation would fully stop the threat — just that it was the safer play. My team had put together an overnight monitoring script watching the compromised account specifically. The CFO's position was blunt: isolating payments meant a guaranteed same-day hit, about $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was framed more as 'reduces risk,' not a number. Given the script gave us visibility on that account, I went with the targeted lockout and monitoring instead of full isolation. Interviewer: What was decisive there? Participant: Honestly, the guaranteed dollar figure against an unquantified benefit made the isolation option feel like the more expensive one, dollar for dollar, even though I couldn't put a number on the other side. And I felt like the script had that account covered. Interviewer: At the time, how confident were you that the script and lockout actually covered the paths the intruder could take? Participant: Fairly confident, honestly. Once we had that account locked and the script watching for any reuse, I felt like we'd boxed the intrusion in. I didn't have the team specifically test whether it would catch token reuse from a different host or a parallel session somewhere else in the environment — I more or less assumed that shutting down that one account's avenues was enough to hold the line while forensics caught up. Interviewer: What happened afterward? Participant: About two hours later, the same compromised credentials touched a second internal system the script wasn't watching. Forensics later found a small amount of data had already been exfiltrated before we even had the script running. Interviewer: Last decision point — the board budget recommendation. Participant: We'd scoped a privileged-access segmentation project eighteen months ago at $240,000, never funded. This week, with the incident fresh, I gathered current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since cloud components were added. The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes. Interviewer: Why start from the old figure rather than the new quotes? Participant: It was already the reference point I had in my head from planning cycles past. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work. Interviewer: If the SIEM hadn't pre-scored that first alert, do you think your response would have gone differently? Participant: Possibly — without a number already on the screen, I might have leaned harder on the account's privilege level from the start, and maybe caught the auth-server overlap sooner. Interviewer: What if the CFO's number hadn't been quantified? Participant: I think I'd have weighed the isolation call less as a straight cost comparison and spent more time pressing the IR firm on what 'reduces risk' actually meant in concrete terms. Interviewer: Looking back, anything you'd tell yourself facing that budget deadline again with a stale internal estimate on file? Participant: Get fresh numbers before you anchor on the old one — even under deadline pressure, a couple of quotes reframes the whole conversation.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.71s · gen 222.80s · total 228.5s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0260 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0239 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0233 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0227 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0210 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0207 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0204 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0195 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0185 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
11. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0184 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
12. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0181 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
13. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0176 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0176 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
15. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0175 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0168 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0165 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
19. **ijcma-08-2012-0064.pdf** — 0.0163 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
21. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
23. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0159 (rrf) — _### cKniff study, we focus on stress as stimuli perceived by individuals in the environment and _
24. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0159 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
25. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0159 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 agreement with the AI prediction. Thus, by measuring t_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0159 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
28. **Hallihan_etal_DTM_12.pdf** — 0.0157 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
29. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0156 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
30. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0156 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
31. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0155 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
32. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0154 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
33. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0153 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0151 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
35. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0150 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
37. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
39. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0149 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
40. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
41. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0147 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
42. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0147 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
44. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0146 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
45. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0144 (rrf) — _# 188 simulated AI always provided suggestions for replacing the ingredient highest in carbohydr_
46. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0141 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
49. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0138 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
50. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0137 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "The analysis focuses on the participant's reported decision-making during a cybersecurity incident and adjacent vendor and budget decisions. Retrieved passages were used to support anchoring and automation-complacency mechanisms; sunk cost labeling relied on widely established general cognitive-science knowledge because no retrieved passage directly supported that label."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment",
        "anchoring heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information, or anchor, when making subsequent judgments, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial triage and severity escalation for SIEM alert",
      "decision_point_description": "Whether to escalate both alerts jointly or focus on the jump-server alert at its SIEM-assigned Medium severity.",
      "affected_reasoning_operation": "Prioritization and severity assessment in security triage",
      "bias_specific_mechanism": "The SIEM's Medium severity score served as an initial anchor, and the participant insufficiently adjusted away from that anchor even though he noticed that the score did not incorporate the account's privileged nature.",
      "manifestation_in_interview": "The participant repeatedly referenced the Medium score as a starting point and did not open or correlate the adjacent auth-server alert until hours later.",
      "effect_on_reasoning_or_decision": "Narrowed triage to the jump server and delayed detection of the shared source IP range and possible lateral movement.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember looking at it and thinking, okay, Medium, that tracks with what I'm seeing, and we went from there.",
          "evidence_explanation": "Shows acceptance of the automated Medium score as the interpretive frame for the alert."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The privileged nature of the account stood out to me, honestly, but the Medium score was already sitting there, and it's usually a decent starting point for how urgently we move.",
          "evidence_explanation": "He notices a contradicting cue, the privileged account, but defers to the initial severity score rather than adjusting urgency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The score gave me a number to anchor the conversation around, and given we were short-staffed, narrowing the analyst's focus felt efficient rather than risky at the time.",
          "evidence_explanation": "Explicitly names anchoring around the initial severity number as shaping the triage decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly — without a number already on the screen, I might have leaned harder on the account's privilege level from the start, and maybe caught the auth-server overlap sooner.",
          "evidence_explanation": "Counterfactual acknowledgment that the pre-scored number influenced his initial reasoning."
        }
      ],
      "correction_or_counterevidence": "The SIEM default model genuinely did not incorporate privilege, and the SOC was short-staffed, so using the severity score as an efficiency heuristic was not wholly unreasonable. However, these constraints do not negate the explicit anchoring mechanism the participant reports.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by retrieved anchoring-and-adjustment research in AI-assisted decision-making.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source describes anchoring-and-adjustment as a heuristic in which decision makers insufficiently adjust away from an initial prediction or value.",
          "relevance_to_this_occurrence": "The participant's acceptance of the initial SIEM Medium score and failure to adjust for account privilege mirrors the anchoring-and-adjustment dynamic."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "sunk cost effect",
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to favor an incumbent option or continue an endeavor because of previously invested resources, even when those past investments should not determine future value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor renewal evaluation during annual renewal cycle",
      "decision_point_description": "Whether to renew the incumbent EDR and threat-intel vendor or closely evaluate comparable alternatives flagged by procurement.",
      "affected_reasoning_operation": "Vendor evaluation and comparative choice",
      "bias_specific_mechanism": "The participant weighted custom detection rules and dashboards built on the incumbent platform as a primary reason to renew, deriving perceived product superiority from accumulated integration work despite lacking current performance benchmarks.",
      "manifestation_in_interview": "He admitted that the integration investment made the incumbent feel like the stronger product outright, even though no current benchmark or comparable bid supported that conclusion.",
      "effect_on_reasoning_or_decision": "Reduced the comparison set to two familiar peer-mentioned vendors and reinforced renewal of the incumbent without formal validation of its current performance relative to alternatives.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd used this EDR and threat-intel vendor six years. My team built a lot of custom detection logic and dashboards on top of their platform.",
          "evidence_explanation": "Describes the accumulated integration investment on which the renewal reasoning came to rely."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, having built all of that ourselves on top of their platform just made the incumbent feel like the stronger product outright, even though I didn't have a current benchmark or a comparable bid on file that actually backed that up.",
          "evidence_explanation": "Direct evidence that past integration work produced a subjective quality judgment unsupported by current comparative data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But the underlying reasoning was really about the sunk integration work, not the incident timing.",
          "evidence_explanation": "The participant identifies sunk integration work as the core driver of the renewal reasoning."
        }
      ],
      "correction_or_counterevidence": "Rebuilding detection rules and dashboards on a new platform is partly a forward-looking switching cost, not purely irrecoverable. However, the participant himself frames the driver as the investment already made and the feeling that the incumbent was stronger without validating that with current benchmarks.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly supported the sunk cost fallacy; the label derives from widely established general cognitive-science usage.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "automation bias",
        "overtrust in automation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient verification and monitoring of an automated system because of overtrust or complacency about its coverage.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment choice after lateral movement confirmation",
      "decision_point_description": "Whether to implement the IR firm's full segment isolation recommendation or rely on targeted lockout plus a custom overnight monitoring script.",
      "affected_reasoning_operation": "Risk assessment and confidence in a security control",
      "bias_specific_mechanism": "The participant accepted the custom monitoring script as adequate coverage without verifying alternative compromise paths, such as token reuse from a different host or a parallel session elsewhere in the environment.",
      "manifestation_in_interview": "He reported feeling fairly confident that the team had boxed the intrusion in after locking the account and deploying the script, while also stating he did not test whether the script would catch reuse or parallel access outside that one account.",
      "effect_on_reasoning_or_decision": "The untested confidence supported choosing targeted lockout and monitoring over full segment isolation; about two hours later the same compromised credentials accessed a second internal system outside the script's watch.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My team had put together an overnight monitoring script watching the compromised account specifically.",
          "evidence_explanation": "Identifies the automated monitoring control that became the focus of the participant's containment confidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Given the script gave us visibility on that account, I went with the targeted lockout and monitoring instead of full isolation.",
          "evidence_explanation": "Shows that the script directly influenced the choice against the IR firm's isolation recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Fairly confident, honestly. Once we had that account locked and the script watching for any reuse, I felt like we'd boxed the intrusion in. I didn't have the team specifically test whether it would catch token reuse from a different host or a parallel session somewhere else in the environment — I more or less assumed that shutting down that one account's avenues was enough to hold the line while forensics caught up.",
          "evidence_explanation": "Demonstrates insufficient verification of the automated monitoring coverage and overtrust in the script's ability to contain the intrusion."
        }
      ],
      "correction_or_counterevidence": "The decision was also influenced by a concrete $180,000 same-day processing loss and the incident time pressure; forensics later showed some data had already been exfiltrated before the script was running, so the script's monitoring gap was not the sole cause. These are contextual factors, but the participant's own description still evidences insufficient verification of automated monitoring coverage.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by the retrieved passage on complacency and automation use, operationalized as insufficient verification before accepting automation.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it... participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "Defines complacency as accepting an automated system without sampling sufficient information to verify its functioning or recommendation.",
          "relevance_to_this_occurrence": "The participant did not have the team test the monitoring script against alternate compromise paths, analogous to accepting the automation's coverage without sufficient verification."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial reference point when making an estimate, with insufficient adjustment to new information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Board budget recommendation for privileged-access segmentation",
      "decision_point_description": "Choosing a single remediation budget number for the board after receiving current vendor quotes above the old internal estimate.",
      "affected_reasoning_operation": "Budget estimation and recommendation",
      "bias_specific_mechanism": "The 18-month-old $240,000 scoped estimate served as an anchor, and the participant adjusted only slightly upward from it despite current quotes of $310,000 to $340,000.",
      "manifestation_in_interview": "He selected a number near the old $240,000 rather than building off the current quotes, saying the old figure was already the reference point in his head and adjusting from it felt like less friction.",
      "effect_on_reasoning_or_decision": "The board recommendation was grounded in a stale internal estimate rather than this week's actual vendor quotes, likely understating current market costs.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd scoped a privileged-access segmentation project eighteen months ago at $240,000, never funded. This week, with the incident fresh, I gathered current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since cloud components were added. The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes.",
          "evidence_explanation": "Shows that current quotes were available but the old $240,000 figure remained the primary basis for the board recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was already the reference point I had in my head from planning cycles past. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work.",
          "evidence_explanation": "Directly identifies the prior figure as a mental reference point from which he made only a small adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Get fresh numbers before you anchor on the old one — even under deadline pressure, a couple of quotes reframes the whole conversation.",
          "evidence_explanation": "Explicit retrospective acknowledgment that the old estimate operated as an anchor."
        }
      ],
      "correction_or_counterevidence": "Deadline pressure and the need to justify a large jump to the board could make the prior baseline administratively easier to use. However, the current quotes were already available, and the participant retrospectively identified the old number as an anchor.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by the same retrieved anchoring-and-adjustment source as the triage occurrence.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source describes anchoring-and-adjustment as a heuristic in which decision makers insufficiently adjust away from an initial value.",
          "relevance_to_this_occurrence": "The participant started from the old $240,000 estimate and adjusted only slightly despite fresh quotes, matching the anchoring-and-adjustment pattern."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "certainty effect",
      "alternative_labels": [
        "ambiguity aversion",
        "concreteness bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Containment choice between full isolation and targeted lockout/monitoring",
      "supporting_interview_quote": "Honestly, the guaranteed dollar figure against an unquantified benefit made the isolation option feel like the more expensive one, dollar for dollar, even though I couldn't put a number on the other side.",
      "plausible_mechanism": "A concrete, immediate, quantified loss may have been weighted more heavily than an ambiguous or unquantified security benefit, producing an unbalanced cost comparison between isolation and monitoring.",
      "why_not_identified": "The evidence is consistent with but not strong enough to distinguish a specific cognitive bias from a reasonable decision-maker preference to avoid a certain loss under uncertainty and time pressure; no retrieved passage directly supported the mechanism, and there was no benchmark for the unquantified security benefit."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective interview rather than contemporaneous decision records or logs.",
    "Some labels, particularly sunk cost fallacy, relied on general cognitive-science knowledge because retrieved corpus support was unavailable.",
    "The retrieved corpus support for anchoring comes from AI-assisted decision-making and aviation/automation contexts, so its application to cybersecurity incident response is analogical.",
    "The analysis does not evaluate whether each decision was ultimately suboptimal from a normative security perspective."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for an internal case study on incident decision-making — nothing you say will be attributed outside this review. Participant: That's fine, happy to walk through it. Interviewer: Great. Can you start with your role and what you're responsible for day to day? Participant: I'm CISO at NorthGate Financial. We're a payments company — card and ACH processing, about 450 employees. I own the security program end to end: SOC operations, vendor risk, incident response, board reporting, budget. Small team, six people in the SOC, so I'm hands-on more than I'd be at a bigger shop. Interviewer: Tell me about the incident you want to discuss, and what you were trying to accomplish overall. Participant: Sure. This was a stretch about ten days ago where an intrusion overlapped with our annual vendor renewal cycle, which was already a bad coincidence. The objective was straightforward in theory — detect and contain whatever was happening without taking payments processing offline, and get our vendor contracts and budget numbers finalized on schedule. In practice those two things kept colliding. Our SIEM flagged an anomalous login on a jump server one of our payments engineers uses — off-hours access, from a network range we hadn't seen for that account before. The SIEM auto-scored it Medium severity based on its default model. That model doesn't know the account is privileged, it just looks at pattern deviation. I remember looking at it and thinking, okay, Medium, that tracks with what I'm seeing, and we went from there. One analyst was handling triage that day — we were down a person on leave — so scope mattered. There'd also been a second alert nine minutes earlier on an adjacent auth server, lower priority, and it just didn't get opened at that point; the jump server was the concrete thing in front of us. Interviewer: What happened next? Participant: We had the analyst dig into the jump server specifically — process history, recent auth events, that kind of thing. A few hours in, once we circled back to close out the queue, we noticed the earlier auth-server alert shared the same source IP range. That's when it stopped looking like an isolated anomaly and started looking like lateral movement toward the payments database segment. Interviewer: Let's go through the sequence in order. What did you know, and when? Participant: At the start, just the jump-server alert and its Medium score. A couple hours later, the IP overlap with the auth-server alert. That afternoon, the vendor renewal deadline hit — we had five business days before our EDR and threat-intel contract auto-renewed, and that decision needed to happen regardless of the incident. That evening, once lateral movement was confirmed, my team wrote a monitoring script overnight to watch the compromised account, and I had a call with the CFO about containment options. Two days later, once things were stable, I had to submit a remediation budget number to the board. Interviewer: Let's slow down at that first decision — the triage call. What cues stood out, and was anything competing for your attention? Participant: The privileged nature of the account stood out to me, honestly, but the Medium score was already sitting there, and it's usually a decent starting point for how urgently we move. I didn't pull in the second alert as something to check in parallel — the analyst was already stretched, and the jump server was the concrete lead. Interviewer: What alternatives did you weigh, and what tipped it? Participant: Escalating both alerts jointly right away, or asking for a correlation sweep across that time window before locking in severity. I didn't do either. The score gave me a number to anchor the conversation around, and given we were short-staffed, narrowing the analyst's focus felt efficient rather than risky at the time. Interviewer: How confident were you in that assessment? Participant: Reasonably, but not fully — I knew the automated score doesn't factor in account privilege. I just didn't push past it that morning. Interviewer: Moving to the vendor decision — walk me through that one. Participant: We'd used this EDR and threat-intel vendor six years. My team built a lot of custom detection logic and dashboards on top of their platform. Procurement had actually flagged three other vendors as offering comparable bundles this cycle, but I didn't go through that list closely. A couple of peer CISOs mentioned they use either this vendor or one close competitor, so my real comparison ended up being just those two. Interviewer: What made you settle on renewing? Participant: Mostly the investment already sitting in our detection rules and dashboards — rebuilding that on a new platform is real time and real risk during a period we're trying to stay stable. I didn't formally validate that the incumbent still outperforms the alternatives; it was more that switching felt costly given what we'd already built. Honestly, having built all of that ourselves on top of their platform just made the incumbent feel like the stronger product outright, even though I didn't have a current benchmark or a comparable bid on file that actually backed that up. Interviewer: Did the live incident affect that judgment at all? Participant: Maybe implicitly — I wasn't eager to introduce a new tool mid-incident. But the underlying reasoning was really about the sunk integration work, not the incident timing. Interviewer: Third decision point — containment, once lateral movement was confirmed. Participant: This was the hardest one. The IR retainer firm recommended full segment isolation, pending forensics, because there wasn't confirmed proof isolation would fully stop the threat — just that it was the safer play. My team had put together an overnight monitoring script watching the compromised account specifically. The CFO's position was blunt: isolating payments meant a guaranteed same-day hit, about $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was framed more as 'reduces risk,' not a number. Given the script gave us visibility on that account, I went with the targeted lockout and monitoring instead of full isolation. Interviewer: What was decisive there? Participant: Honestly, the guaranteed dollar figure against an unquantified benefit made the isolation option feel like the more expensive one, dollar for dollar, even though I couldn't put a number on the other side. And I felt like the script had that account covered. Interviewer: At the time, how confident were you that the script and lockout actually covered the paths the intruder could take? Participant: Fairly confident, honestly. Once we had that account locked and the script watching for any reuse, I felt like we'd boxed the intrusion in. I didn't have the team specifically test whether it would catch token reuse from a different host or a parallel session somewhere else in the environment — I more or less assumed that shutting down that one account's avenues was enough to hold the line while forensics caught up. Interviewer: What happened afterward? Participant: About two hours later, the same compromised credentials touched a second internal system the script wasn't watching. Forensics later found a small amount of data had already been exfiltrated before we even had the script running. Interviewer: Last decision point — the board budget recommendation. Participant: We'd scoped a privileged-access segmentation project eighteen months ago at $240,000, never funded. This week, with the incident fresh, I gathered current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since cloud components were added. The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes. Interviewer: Why start from the old figure rather than the new quotes? Participant: It was already the reference point I had in my head from planning cycles past. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work. Interviewer: If the SIEM hadn't pre-scored that first alert, do you think your response would have gone differently? Participant: Possibly — without a number already on the screen, I might have leaned harder on the account's privilege level from the start, and maybe caught the auth-server overlap sooner. Interviewer: What if the CFO's number hadn't been quantified? Participant: I think I'd have weighed the isolation call less as a straight cost comparison and spent more time pressing the IR firm on what 'reduces risk' actually meant in concrete terms. Interviewer: Looking back, anything you'd tell yourself facing that budget deadline again with a stale internal estimate on file? Participant: Get fresh numbers before you anchor on the old one — even under deadline pressure, a couple of quotes reframes the whole conversation.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.19s · gen 218.39s · total 224.4s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0260 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0239 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0233 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0227 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0210 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0207 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0204 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0195 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0185 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
11. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0184 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
12. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0181 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
13. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0176 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0176 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
15. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0175 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0168 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0165 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
19. **ijcma-08-2012-0064.pdf** — 0.0163 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
20. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
21. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
23. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0159 (rrf) — _### cKniff study, we focus on stress as stimuli perceived by individuals in the environment and _
24. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0159 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
25. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0159 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 agreement with the AI prediction. Thus, by measuring t_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0159 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
28. **Hallihan_etal_DTM_12.pdf** — 0.0157 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
29. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0156 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
30. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0156 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
31. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0155 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
32. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0154 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
33. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0153 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0151 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
35. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0150 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
37. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
39. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0149 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
40. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
41. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0147 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
42. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0147 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
44. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0146 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
45. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0144 (rrf) — _# 188 simulated AI always provided suggestions for replacing the ingredient highest in carbohydr_
46. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0141 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
49. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0138 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
50. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0137 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Only bias-specific mechanisms with affirmative transcript evidence were classified. Workload constraints, incident timing, and later bad outcomes were treated as contextual factors rather than standalone bias evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A judgmental heuristic in which an initial numeric value serves as a reference point and subsequent adjustment away from that anchor is insufficient, biasing the final judgment toward the anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial SIEM alert triage and escalation decision",
      "decision_point_description": "Deciding whether to focus only on the jump-server anomaly at Medium severity or to escalate and correlate the adjacent auth-server alert before locking in severity.",
      "affected_reasoning_operation": "Alert severity assessment, prioritization, and initial incident-scoping decision",
      "bias_specific_mechanism": "The participant used the SIEM's Medium severity score as an anchor for urgency and did not sufficiently adjust for the privileged account context or the nearby auth-server alert, even though the privileged nature of the account stood out to him.",
      "manifestation_in_interview": "He accepted the Medium score as consistent with his initial view, treated the jump-server alert as the concrete lead, and did not request a correlation sweep. He later said the score gave him a number to anchor the conversation around.",
      "effect_on_reasoning_or_decision": "The team narrowed triage to the jump server instead of immediately correlating the two alerts, delaying discovery of the shared source IP and possible lateral movement.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The SIEM auto-scored it Medium severity based on its default model. That model doesn't know the account is privileged, it just looks at pattern deviation. I remember looking at it and thinking, okay, Medium, that tracks with what I'm seeing, and we went from there.",
          "evidence_explanation": "Shows he accepted the automated score despite knowing its blindness to the privileged account, making the score the starting reference point for action."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The privileged nature of the account stood out to me, honestly, but the Medium score was already sitting there, and it's usually a decent starting point for how urgently we move.",
          "evidence_explanation": "Directly juxtaposes a high-relevance cue, account privilege, with the numeric anchor, and shows the anchor shaped urgency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Escalating both alerts jointly right away, or asking for a correlation sweep across that time window before locking in severity. I didn't do either. The score gave me a number to anchor the conversation around...",
          "evidence_explanation": "Explicitly identifies the anchoring mechanism and connects it to the non-escalation decision."
        }
      ],
      "correction_or_counterevidence": "A structural workload factor was also present: one analyst was handling triage and the team was short-staffed, which may have made focused triage feel efficient. The participant later broadened scope after seeing the shared IP range.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Rastogi et al. (2022) supports anchoring-and-adjustment in AI-assisted decision-making; here the SIEM's automated severity score served as the anchor.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports the anchoring-and-adjustment heuristic, in which people adjust insufficiently away from an initial automated or AI-supplied prediction.",
          "relevance_to_this_occurrence": "The participant anchored on the SIEM's automated severity score and underadjusted for privileged-account context, mirroring insufficient adjustment away from an initial automated value."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "sunk cost effect",
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue a course of action or retain an investment because of previously incurred, nonrecoverable costs, rather than evaluating prospective costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "EDR and threat-intel vendor renewal decision",
      "decision_point_description": "Whether to renew the incumbent EDR/threat-intel vendor or evaluate the comparable alternatives flagged by procurement.",
      "affected_reasoning_operation": "Vendor evaluation and renewal choice",
      "bias_specific_mechanism": "The participant weighted past investment in custom detection logic and dashboards as a reason to renew, and inferred incumbent product superiority from that sunk work rather than from current benchmark evidence or comparable bids.",
      "manifestation_in_interview": "He did not closely review procurement's comparable vendors, limited comparison to vendors mentioned by peers, and justified renewal through the investment already built on the incumbent platform. He stated the incumbent felt like the stronger product despite lacking current benchmark or comparable bid support.",
      "effect_on_reasoning_or_decision": "The renewal decision was driven by irrecoverable past integration costs rather than an unbiased prospective comparison, increasing the likelihood of retaining an incumbent that may not be the best current option.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd used this EDR and threat-intel vendor six years. My team built a lot of custom detection logic and dashboards on top of their platform. Procurement had actually flagged three other vendors as offering comparable bundles this cycle, but I didn't go through that list closely.",
          "evidence_explanation": "Establishes the sunk investment and that comparable alternatives existed but were not fully evaluated."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the investment already sitting in our detection rules and dashboards — rebuilding that on a new platform is real time and real risk during a period we're trying to stay stable. I didn't formally validate that the incumbent still outperforms the alternatives; it was more that switching felt costly given what we'd already built.",
          "evidence_explanation": "Shows the decision was based on past costs already incurred rather than on a current comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, having built all of that ourselves on top of their platform just made the incumbent feel like the stronger product outright, even though I didn't have a current benchmark or a comparable bid on file that actually backed that up.",
          "evidence_explanation": "Directly demonstrates that irretrievable prior work created an unsupported quality judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Maybe implicitly — I wasn't eager to introduce a new tool mid-incident. But the underlying reasoning was really about the sunk integration work, not the incident timing.",
          "evidence_explanation": "Rules out the live incident as the central explanation and identifies past investment as the operative reasoning."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged procurement had flagged comparable alternatives and that he lacked current benchmark or comparable bid evidence for incumbent superiority. He also noted the live incident may have had an implicit influence but stated the underlying reasoning was sunk integration work rather than incident timing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly addresses the sunk cost fallacy; this established label is applied from general knowledge rather than from retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency in monitoring automation",
        "over-trust in automated monitoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient verification or monitoring of an automated system based on over-trust, leading an operator to sample less information than needed to establish its true coverage or accuracy.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment selection after lateral movement confirmation",
      "decision_point_description": "Whether to implement full segment isolation as recommended by the IR retainer firm, or use targeted account lockout plus an in-house monitoring script.",
      "affected_reasoning_operation": "Containment sufficiency assessment and risk-control selection",
      "bias_specific_mechanism": "Complacent trust in the newly written monitoring script: the participant assumed it covered the compromised account's possible reuse paths without testing for other hosts, parallel sessions, or token reuse, and this unverified trust made a weaker containment option feel adequate.",
      "manifestation_in_interview": "He stated he felt the script had the account covered and was fairly confident, but he explicitly did not test whether it would detect token reuse from another host or a parallel session. He assumed shutting down one account's avenues was enough while forensics caught up.",
      "effect_on_reasoning_or_decision": "The team selected targeted lockout and monitoring instead of full isolation; two hours later the same credentials touched a second system the script was not watching, and forensics later found prior exfiltration.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given the script gave us visibility on that account, I went with the targeted lockout and monitoring instead of full isolation.",
          "evidence_explanation": "Shows that trust in the script directly influenced the containment choice."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Fairly confident, honestly. Once we had that account locked and the script watching for any reuse, I felt like we'd boxed the intrusion in.",
          "evidence_explanation": "Demonstrates confidence in coverage that was not actually verified."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have the team specifically test whether it would catch token reuse from a different host or a parallel session somewhere else in the environment — I more or less assumed that shutting down that one account's avenues was enough to hold the line while forensics caught up.",
          "evidence_explanation": "Demonstrates the insufficient-verification mechanism: an assumption of coverage replaced a test."
        }
      ],
      "correction_or_counterevidence": "The IR retainer recommended stronger isolation, and the CFO's quantified $180,000 processing-loss figure likely also influenced the same decision. The later second-system credential use and exfiltration are outcome evidence, not proof of bias at the time, but they exposed the script coverage gap.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The supplied Parasuraman and Manzey (2010) passage provides conceptual support for complacency as insufficient information sampling and verification in reliance on automation.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it.",
          "mechanism_supported_by_source": "Complacency in automation use is characterized by insufficient verification or sampling of information relative to what is needed to validate an automated aid's recommendation or coverage.",
          "relevance_to_this_occurrence": "The participant similarly did not perform the verification needed to establish the monitoring script's actual coverage before relying on it for the containment decision."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment heuristic",
        "insufficient adjustment from prior estimate"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A judgmental heuristic in which an initial numeric value serves as a reference point and subsequent adjustment away from that anchor is insufficient, biasing the final judgment toward the anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Board remediation budget recommendation",
      "decision_point_description": "Choosing a single budget number for privileged-access segmentation remediation after fresh vendor quotes came in higher than an 18-month-old internal estimate.",
      "affected_reasoning_operation": "Budget estimation and recommendation under updated cost information",
      "bias_specific_mechanism": "The participant anchored on the old $240,000 internal estimate from 18 months earlier and adjusted only slightly upward, rather than building the recommendation from current quotes of $310,000 to $340,000, because adjusting from the familiar anchor felt like less friction.",
      "manifestation_in_interview": "He acknowledged the new quotes and still recommended a number close to the original $240,000, nudged up, not based on this week's quotes. He described the old figure as the reference point in his head and said adjusting it felt like less friction than justifying a jump to $340,000.",
      "effect_on_reasoning_or_decision": "The board received a budget recommendation that may understate current market cost and expanded scope by anchoring on a stale planning estimate, potentially underfunding the remediation project.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd scoped a privileged-access segmentation project eighteen months ago at $240,000, never funded. This week, with the incident fresh, I gathered current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since cloud components were added.",
          "evidence_explanation": "Establishes the old anchor and the available updated information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes.",
          "evidence_explanation": "Shows the final estimate was anchored on the old figure rather than current market data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was already the reference point I had in my head from planning cycles past. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work.",
          "evidence_explanation": "Explicitly describes the anchor and the insufficient-adjustment mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Get fresh numbers before you anchor on the old one — even under deadline pressure, a couple of quotes reframes the whole conversation.",
          "evidence_explanation": "The participant's own debrief identifies the anchoring pattern in hindsight."
        }
      ],
      "correction_or_counterevidence": "He did gather and was aware of current quotes; the decision was not made in ignorance of newer information. The bias is in the weighting of the old anchor rather than lack of updated data. No formal correction before the recommendation is recorded.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Rastogi et al. (2022) supports anchoring-and-adjustment in decision-making under external numeric inputs; here the stale internal estimate served as the anchor.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports the anchoring-and-adjustment heuristic, in which people adjust insufficiently away from an initial value.",
          "relevance_to_this_occurrence": "The participant adjusted only slightly from the old $240,000 estimate despite having fresh quotes, consistent with insufficient adjustment from an anchor."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus is sparse and does not directly cover all labeled biases; the sunk cost fallacy occurrence rests on general knowledge rather than retrieval.",
    "The transcript is a single participant's retrospective self-report, so causal inference is limited to the participant's own description without independent operational verification.",
    "Some operational outcomes, such as post-decision credential reuse and exfiltration, were used only as context and not as evidence that the participant was biased at the time of the decision."
  ]
}

