# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. This is for an internal case-study review, and it stays within that context. Comfortable proceeding? Participant: Yes, that's fine. Interviewer: Can you start with your role and what you're responsible for? Participant: I'm CISO at NorthGate Financial. We process card and ACH payments, about 450 employees. I own the security program broadly — SOC, vendor risk, incident response, board reporting, budget. We run lean, six people in the SOC, so I'm closer to the operational detail than a CISO at a bigger shop would be. Interviewer: Walk me through the incident you'd like to discuss, and what you were trying to accomplish. Participant: This was about ten days ago. We had an intrusion land right in the middle of our annual vendor-renewal and budget cycle, which made everything more complicated than it needed to be. The goal was simple to state — contain whatever was happening without disrupting payments, and still get the vendor contract and budget numbers turned in on schedule. Those two threads kept crossing. It started with our SIEM flagging an anomalous login on a jump server one of our payments engineers uses — off-hours, from a network range we hadn't seen on that account. The SIEM's default model scored it Medium. That model doesn't factor in whether the account is privileged, it just looks at behavioral deviation. I saw Medium and it matched my gut read, so we moved from there. We had one analyst on triage that day since someone was out on leave. There'd also been a second, lower-priority alert nine minutes earlier on an adjacent auth server — it didn't get opened right away; the jump server was the concrete thing in front of us. Interviewer: What happened after that? Participant: The analyst worked the jump server specifically — process history, recent auth events. A few hours later, once we circled back through the queue, we noticed the earlier auth-server alert shared the same source IP range. That's when it stopped looking like an isolated event and started looking like lateral movement toward the payments database segment. Interviewer: Take me through the sequence in order — what did you know, and when? Participant: Morning: the jump-server alert and its Medium score. Midday: the IP overlap with the auth-server alert. That afternoon, the vendor renewal deadline landed on top of it — five business days before auto-renewal on our EDR and threat-intel contract, incident or no incident. That evening, once lateral movement was confirmed, my team wrote a monitoring script overnight for the compromised account, and I had a call with our CFO about containment options. Two days later, with things stabilized, I had to submit a remediation budget figure to the board. Interviewer: Let's slow down on that first call — the triage decision. What stood out to you, and was anything competing for attention? Participant: The account being privileged stood out, honestly. But the Medium score was already sitting there, and normally that's a reasonable starting point for how fast we move. I didn't loop the second alert in as something to check in parallel — the analyst was stretched thin, and the jump server was the concrete lead. Interviewer: What alternatives did you consider, and what tipped the decision? Participant: Escalating both alerts jointly right away, or running a correlation sweep across that time window before locking in severity. I did neither. The score gave me a number to build the response around, and given the staffing gap, narrowing the analyst's focus felt efficient rather than risky in the moment. Interviewer: How confident were you in that call? Participant: Reasonably, not fully. I knew the score doesn't weigh account privilege. I just didn't push past it that morning. Interviewer: Moving to the vendor decision — walk me through that. Participant: Six years with this EDR and threat-intel vendor. My team built a lot of custom detection logic and dashboards on their platform. Procurement had actually flagged three other vendors with comparable bundles this cycle, including transition support that looked broadly workable, but I didn't work through that list closely. A couple of peer CISOs mentioned they use either this vendor or the closest competitor, so my real comparison ended up being just those two. Interviewer: What made you settle on renewal? Participant: Mostly the investment already sitting in our detection rules and dashboards. Rebuilding that on a new platform is real time and real exposure, especially mid-incident. If I'm honest, those dashboards just felt more valuable because they were ours — built by my own team over years — and I didn't actually sit down and test whether that feeling matched their current value against what procurement's options offered. It was more that switching felt costly given what we'd already built. Interviewer: Did the live incident affect that judgment? Participant: Maybe implicitly — I wasn't eager to bring in a new tool mid-incident. But the core reasoning was really about the integration work already sunk into it, not the incident timing. Interviewer: Third decision point — containment, once lateral movement was confirmed. Participant: This was the hardest one. Our IR retainer firm recommended full segment isolation pending forensics — their position was that it's the safer play, though they couldn't prove isolation would fully stop the threat. My team had the overnight script watching the compromised account specifically. Nobody had actually validated whether that script would catch the same credentials being reused on a different host or opening a parallel session elsewhere — but in the moment, having eyes on that one account felt like enough to hold off on isolation. The CFO's framing was blunt: isolating payments meant a guaranteed same-day hit, around $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was 'reduces risk,' not a figure. Given the script gave us visibility on that account, I went with targeted lockout and monitoring instead of full isolation. Interviewer: What was decisive there? Participant: Honestly, the guaranteed dollar figure against an unquantified benefit made isolation feel like the more expensive option, even though I couldn't put a number on the other side. And I felt like the script had that account covered. Interviewer: What happened afterward? Participant: About two hours later, the same compromised credentials touched a second internal system the script wasn't watching. Forensics later found a small amount of data had already been exfiltrated before the script was even running. Interviewer: Last decision point — the board budget recommendation. Participant: We'd scoped a privileged-access segmentation project eighteen months back at $240,000, never funded. This week, with the incident fresh, I pulled current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since we've added cloud components. The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes. Interviewer: Why start from the old figure instead of the new quotes? Participant: It was already the reference point in my head from prior planning cycles. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work behind it. Interviewer: If the SIEM hadn't pre-scored that first alert, would your response have gone differently? Participant: Possibly. Without a number already on the screen, I might have leaned harder on the account's privilege level from the start and caught the auth-server overlap sooner. Interviewer: What if the CFO's number hadn't been quantified? Participant: I think I'd have treated the isolation call less like a straight cost comparison and spent more time pressing the IR firm on what 'reduces risk' actually meant in concrete terms. Interviewer: Looking back, what would you tell yourself facing that same budget deadline with a stale internal estimate on file? Participant: Get fresh numbers before you anchor on the old one. Even under deadline pressure, a couple of quotes reframes the whole conversation.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.41s · gen 277.80s · total 282.9s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0238 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0230 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0224 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0210 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
5. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0207 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0205 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0185 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
9. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0181 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0179 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0178 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
13. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0178 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
14. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0176 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
15. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0173 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
16. **Hallihan_etal_DTM_12.pdf** — 0.0169 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
17. **ijcma-08-2012-0064.pdf** — 0.0169 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
18. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0167 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
19. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
21. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0164 (rrf) — _### cKniff study, we focus on stress as stimuli perceived by individuals in the environment and _
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0163 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0162 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
26. **ijcma-08-2012-0064.pdf** — 0.0161 (rrf) — _# 382 I used this with a man and woman team, both of whom I knew didn’t care for each other busi_
27. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0158 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
28. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0158 (rrf) — _# 4Discussion - - viewing CFFs as more cognitively demanding. Although coming at the cost of use_
29. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0157 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
30. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0157 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
31. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0156 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
32. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
33. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
34. **ijcma-08-2012-0064.pdf** — 0.0154 (rrf) — _# 382 on heuristics and results in more biased judgments (Bazerman and Moore, 2009). Gladwin and_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
36. **Hallihan_etal_DTM_12.pdf** — 0.0151 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0151 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0150 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
39. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0149 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
41. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0145 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0145 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
44. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0143 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_
45. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0143 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
46. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0143 (rrf) — _# 6.2 Analysis of the structural model people make mistakes and errors occur. Errors can be redu_
47. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0143 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
48. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0143 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
49. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0141 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 agreement with the AI prediction. Thus, by measuring t_
50. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0140 (rrf) — _### cKniff has been rigorouslystudiedas a factorintechnology adoption (Gefen,Karahanna,& Straub,_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the participant's retrospective incident narrative for affirmative cognitive bias occurrences across triage, vendor renewal, containment, and budget recommendation decision points. Retrieved corpus passages were used where applicable; otherwise established cognitive-science knowledge was noted."
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
      "bias_label": "certainty effect",
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
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "An initial numeric value serves as a reference point, and subsequent judgments adjust insufficiently away from that anchor even when the anchor is recognized as incomplete or irrelevant.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial SIEM alert triage",
      "decision_point_description": "Whether to treat the jump-server Medium alert in isolation or to jointly investigate the earlier auth-server alert and account privilege.",
      "affected_reasoning_operation": "Severity assessment and triage prioritization",
      "bias_specific_mechanism": "The SIEM Medium score anchored the participant's threat severity judgment. Although he knew the model excluded account privilege, he did not adjust the severity upward or incorporate the adjacent second alert in parallel.",
      "manifestation_in_interview": "The participant stated that the Medium score matched his gut read, gave him a number to build the response around, and that without a pre-scored number he might have weighed privilege level sooner.",
      "effect_on_reasoning_or_decision": "The analyst focused only on the jump server, delaying correlation with the earlier auth-server alert and allowing lateral movement toward the payments database segment to remain undetected for hours.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I saw Medium and it matched my gut read, so we moved from there.",
          "evidence_explanation": "Shows the initial Medium score was accepted as the framing for response urgency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The account being privileged stood out, honestly. But the Medium score was already sitting there, and normally that's a reasonable starting point for how fast we move. I didn't loop the second alert in as something to check in parallel — the analyst was stretched thin, and the jump server was the concrete lead.",
          "evidence_explanation": "Directly demonstrates the anchor score overriding known privileged-account significance and suppressing parallel investigation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew the score doesn't weigh account privilege. I just didn't push past it that morning.",
          "evidence_explanation": "Confirms awareness of the anchor's limitation without sufficient adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without a number already on the screen, I might have leaned harder on the account's privilege level from the start and caught the auth-server overlap sooner.",
          "evidence_explanation": "Counterfactual supports the causal role of the preexisting score in the biased triage judgment."
        }
      ],
      "correction_or_counterevidence": "A staffing shortage created legitimate triage pressure, and prioritizing a concrete lead can be a reasonable bounded-rational response. However, the participant's explicit awareness that the score excluded account privilege and his counterfactual indicate that the Medium score distorted severity weighting beyond routine triage.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by the Rastogi et al. (2022) passage on anchoring-and-adjustment in decision-making.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "The anchoring-and-adjustment heuristic is a resource-rational tradeoff between time and accuracy; participants' likelihood of sufficiently adjusting away from the incorrect AI prediction increased as the time allocated increased.",
          "mechanism_supported_by_source": "Supports the anchoring-and-adjustment mechanism in which an initial value is insufficiently adjusted away from under resource constraints.",
          "relevance_to_this_occurrence": "The SIEM Medium score is analogous to an initial numeric prediction; under staffing and time pressure the participant did not sufficiently adjust away from it despite known limitations."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "sunk cost effect",
        "IKEA effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an endeavor or retain an asset because of previously invested resources such as time, effort, or money, even when current and future costs and benefits favor a different choice.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "EDR and threat-intel vendor renewal decision",
      "decision_point_description": "Whether to renew the incumbent vendor or evaluate and switch to one of the three comparable vendors flagged by procurement.",
      "affected_reasoning_operation": "Vendor evaluation and renewal choice",
      "bias_specific_mechanism": "Prior investments in custom detection rules and dashboards were treated as a reason to renew, rather than comparing future value net of switching costs. The participant also reported that self-built dashboards felt more valuable because they were built in-house, and he did not test that feeling against alternatives.",
      "manifestation_in_interview": "The participant admitted he did not closely work through procurement's alternatives and that switching felt costly given what had already been built, rather than from a forward-looking comparison.",
      "effect_on_reasoning_or_decision": "The renewal decision remained anchored to the incumbent vendor, reducing the objectivity of alternative evaluation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the investment already sitting in our detection rules and dashboards. Rebuilding that on a new platform is real time and real exposure, especially mid-incident.",
          "evidence_explanation": "Treats previously invested effort as a primary reason to stay with the vendor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, those dashboards just felt more valuable because they were ours — built by my own team over years — and I didn't actually sit down and test whether that feeling matched their current value against what procurement's options offered. It was more that switching felt costly given what we'd already built.",
          "evidence_explanation": "Explicitly describes sunk cost reasoning and failure to test the value of existing investments against alternatives."
        }
      ],
      "correction_or_counterevidence": "Switching costs and mid-incident disruption can be legitimate reasons to avoid changing vendors. The participant said the core reasoning was the integration work already sunk rather than incident timing, which points to the sunk cost mechanism more than a purely operational cost-benefit analysis.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context specifically addresses sunk cost reasoning; this classification relies on established cognitive-science knowledge of the sunk cost fallacy.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "automation bias",
        "overreliance on automation",
        "complacency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A failure to verify or adequately monitor automated system outputs or coverage because of overtrust in the automation, resulting in less information sampling than normative verification would require.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment decision following confirmed lateral movement",
      "decision_point_description": "Whether to follow the IR retainer firm's recommendation for full segment isolation or to rely on targeted lockout and monitoring.",
      "affected_reasoning_operation": "Verification of security control coverage",
      "bias_specific_mechanism": "The participant overtrusted an overnight monitoring script scoped only to the compromised account, did not validate whether it would detect credential reuse on other hosts or parallel sessions, and treated its presence as sufficient to avoid full isolation.",
      "manifestation_in_interview": "He explicitly acknowledged the script was not validated but said having eyes on that one account felt like enough.",
      "effect_on_reasoning_or_decision": "A false sense of coverage contributed to rejecting full segment isolation; the same credentials later touched a second internal system the script was not watching.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My team had the overnight script watching the compromised account specifically. Nobody had actually validated whether that script would catch the same credentials being reused on a different host or opening a parallel session elsewhere — but in the moment, having eyes on that one account felt like enough to hold off on isolation.",
          "evidence_explanation": "Documents unverified automation coverage being accepted as sufficient for a high-stakes containment decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And I felt like the script had that account covered.",
          "evidence_explanation": "Directly states the overtrust in the automated monitoring script."
        }
      ],
      "correction_or_counterevidence": "The IR retainer firm could not prove isolation would fully stop the threat, so isolation was not risk-free. However, the script's known scope limitation required verification before being treated as a substitute for isolation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by Parasuraman and Manzey (2010) on complacency in automation use.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Complacency was assessed by measuring the extent to which participants verified the automation's diagnosis before accepting it; participants sampling less information than that necessary to completely verify the aid's recommendation were regarded as complacent.",
          "mechanism_supported_by_source": "Defines automation complacency as insufficient information sampling to verify automated output, matching the unvalidated script coverage.",
          "relevance_to_this_occurrence": "The participant sampled less verification than necessary before relying on the script, consistent with automation complacency."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "certainty effect",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "bias_definition": "In choices under risk, outcomes that are certain are overweighted relative to outcomes that are merely probable or unquantified, distorting tradeoffs.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment decision following confirmed lateral movement",
      "decision_point_description": "Whether to accept the guaranteed same-day loss from isolating payments or to accept an unquantified security risk from not isolating.",
      "affected_reasoning_operation": "Cost-risk tradeoff evaluation",
      "bias_specific_mechanism": "The quantified guaranteed $180,000 loss from isolation was concrete and immediate, while the security benefit of isolation was unquantified. The certain operational loss was overweighted relative to the unquantified probabilistic security loss.",
      "manifestation_in_interview": "The participant said the guaranteed dollar figure against an unquantified benefit made isolation feel more expensive, even though he could not put a number on the other side; he also acknowledged he would have behaved differently if the number had not been quantified.",
      "effect_on_reasoning_or_decision": "Full segment isolation was rejected in favor of targeted lockout and monitoring; two hours later the same credentials touched a second internal system and forensics found prior data exfiltration.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The CFO's framing was blunt: isolating payments meant a guaranteed same-day hit, around $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was 'reduces risk,' not a figure.",
          "evidence_explanation": "Contrasts a certain quantified loss with an unquantified security benefit, setting up the distorted weighting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the guaranteed dollar figure against an unquantified benefit made isolation feel like the more expensive option, even though I couldn't put a number on the other side.",
          "evidence_explanation": "Directly expresses the certainty effect: the certain loss drove the evaluation more than the unquantified but potentially severe risk."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I'd have treated the isolation call less like a straight cost comparison and spent more time pressing the IR firm on what 'reduces risk' actually meant in concrete terms.",
          "evidence_explanation": "Counterfactual demonstrates that the quantified certain loss changed the reasoning mode."
        }
      ],
      "correction_or_counterevidence": "The $180,000 same-day loss was a real cost, and cost-benefit analysis legitimately includes certain losses. However, the participant's own statement that he treated the decision as a straight cost comparison only because one side was quantified, and his counterfactual, indicate a certainty effect rather than a fully rational expected-value comparison.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context specifically supports the certainty effect; this classification relies on established decision-science and prospect theory knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "An initial numeric value serves as a reference point, and subsequent estimates adjust insufficiently away from that anchor even when new information suggests the anchor is stale.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Board budget recommendation",
      "decision_point_description": "Whether to base the remediation budget request on the stale $240,000 prior estimate or the fresh $310,000-$340,000 vendor quotes.",
      "affected_reasoning_operation": "Budget estimation and recommendation",
      "bias_specific_mechanism": "The old $240,000 figure from prior planning cycles served as an anchor; the participant adjusted only slightly upward and avoided justifying a jump to the current quote range despite having fresh vendor quotes.",
      "manifestation_in_interview": "The participant said the old figure was already the reference point in his head and that adjusting it felt like less friction; he concluded he should get fresh numbers before anchoring on the old one.",
      "effect_on_reasoning_or_decision": "The board recommendation was likely understated relative to current market quotes, potentially underfunding the privileged-access segmentation remediation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd scoped a privileged-access segmentation project eighteen months back at $240,000, never funded. This week, with the incident fresh, I pulled current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since we've added cloud components. The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes.",
          "evidence_explanation": "Shows the stale number was used as the starting point rather than current quotes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was already the reference point in my head from prior planning cycles. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work behind it.",
          "evidence_explanation": "Directly identifies the anchor and insufficient adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Get fresh numbers before you anchor on the old one.",
          "evidence_explanation": "Self-recognition of anchoring bias in retrospect."
        }
      ],
      "correction_or_counterevidence": "Deadline pressure and lack of additional scoping work could justify a more conservative recommendation, but this does not explain starting from a stale anchor rather than averaging or range-weighting the current quotes.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by the same Rastogi et al. (2022) passage on anchoring-and-adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "The anchoring-and-adjustment heuristic is a resource-rational tradeoff between time and accuracy; participants' likelihood of sufficiently adjusting away from the incorrect AI prediction increased as the time allocated increased.",
          "mechanism_supported_by_source": "Supports the anchoring-and-adjustment mechanism in which an initial value is insufficiently adjusted away from under resource constraints.",
          "relevance_to_this_occurrence": "The stale $240,000 figure functioned as the anchor; under budget deadline pressure the participant adjusted only a small amount despite much higher current quotes."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "IKEA effect",
      "alternative_labels": [
        "effort justification"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "EDR and threat-intel vendor renewal decision",
      "supporting_interview_quote": "those dashboards just felt more valuable because they were ours — built by my own team over years",
      "plausible_mechanism": "People overvalue objects or solutions they created or assembled, which could independently compound the sunk cost effect in the vendor renewal decision.",
      "why_not_identified": "The IKEA/effort-justification component is intertwined with the broader sunk cost rationale and does not appear as an independent causal pathway in the transcript; the vendor decision is already classified under sunk cost fallacy."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a retrospective self-report; bias mechanisms are inferred from explicit statements and counterfactuals rather than direct observation.",
    "The retrieved corpus support is limited to the provided RAG context, so some established labels rely on general cognitive-science knowledge.",
    "Operational constraints such as staffing gaps, deadline pressure, and legitimate switching costs coexist with the identified bias mechanisms."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. This is for an internal case-study review, and it stays within that context. Comfortable proceeding? Participant: Yes, that's fine. Interviewer: Can you start with your role and what you're responsible for? Participant: I'm CISO at NorthGate Financial. We process card and ACH payments, about 450 employees. I own the security program broadly — SOC, vendor risk, incident response, board reporting, budget. We run lean, six people in the SOC, so I'm closer to the operational detail than a CISO at a bigger shop would be. Interviewer: Walk me through the incident you'd like to discuss, and what you were trying to accomplish. Participant: This was about ten days ago. We had an intrusion land right in the middle of our annual vendor-renewal and budget cycle, which made everything more complicated than it needed to be. The goal was simple to state — contain whatever was happening without disrupting payments, and still get the vendor contract and budget numbers turned in on schedule. Those two threads kept crossing. It started with our SIEM flagging an anomalous login on a jump server one of our payments engineers uses — off-hours, from a network range we hadn't seen on that account. The SIEM's default model scored it Medium. That model doesn't factor in whether the account is privileged, it just looks at behavioral deviation. I saw Medium and it matched my gut read, so we moved from there. We had one analyst on triage that day since someone was out on leave. There'd also been a second, lower-priority alert nine minutes earlier on an adjacent auth server — it didn't get opened right away; the jump server was the concrete thing in front of us. Interviewer: What happened after that? Participant: The analyst worked the jump server specifically — process history, recent auth events. A few hours later, once we circled back through the queue, we noticed the earlier auth-server alert shared the same source IP range. That's when it stopped looking like an isolated event and started looking like lateral movement toward the payments database segment. Interviewer: Take me through the sequence in order — what did you know, and when? Participant: Morning: the jump-server alert and its Medium score. Midday: the IP overlap with the auth-server alert. That afternoon, the vendor renewal deadline landed on top of it — five business days before auto-renewal on our EDR and threat-intel contract, incident or no incident. That evening, once lateral movement was confirmed, my team wrote a monitoring script overnight for the compromised account, and I had a call with our CFO about containment options. Two days later, with things stabilized, I had to submit a remediation budget figure to the board. Interviewer: Let's slow down on that first call — the triage decision. What stood out to you, and was anything competing for attention? Participant: The account being privileged stood out, honestly. But the Medium score was already sitting there, and normally that's a reasonable starting point for how fast we move. I didn't loop the second alert in as something to check in parallel — the analyst was stretched thin, and the jump server was the concrete lead. Interviewer: What alternatives did you consider, and what tipped the decision? Participant: Escalating both alerts jointly right away, or running a correlation sweep across that time window before locking in severity. I did neither. The score gave me a number to build the response around, and given the staffing gap, narrowing the analyst's focus felt efficient rather than risky in the moment. Interviewer: How confident were you in that call? Participant: Reasonably, not fully. I knew the score doesn't weigh account privilege. I just didn't push past it that morning. Interviewer: Moving to the vendor decision — walk me through that. Participant: Six years with this EDR and threat-intel vendor. My team built a lot of custom detection logic and dashboards on their platform. Procurement had actually flagged three other vendors with comparable bundles this cycle, including transition support that looked broadly workable, but I didn't work through that list closely. A couple of peer CISOs mentioned they use either this vendor or the closest competitor, so my real comparison ended up being just those two. Interviewer: What made you settle on renewal? Participant: Mostly the investment already sitting in our detection rules and dashboards. Rebuilding that on a new platform is real time and real exposure, especially mid-incident. If I'm honest, those dashboards just felt more valuable because they were ours — built by my own team over years — and I didn't actually sit down and test whether that feeling matched their current value against what procurement's options offered. It was more that switching felt costly given what we'd already built. Interviewer: Did the live incident affect that judgment? Participant: Maybe implicitly — I wasn't eager to bring in a new tool mid-incident. But the core reasoning was really about the integration work already sunk into it, not the incident timing. Interviewer: Third decision point — containment, once lateral movement was confirmed. Participant: This was the hardest one. Our IR retainer firm recommended full segment isolation pending forensics — their position was that it's the safer play, though they couldn't prove isolation would fully stop the threat. My team had the overnight script watching the compromised account specifically. Nobody had actually validated whether that script would catch the same credentials being reused on a different host or opening a parallel session elsewhere — but in the moment, having eyes on that one account felt like enough to hold off on isolation. The CFO's framing was blunt: isolating payments meant a guaranteed same-day hit, around $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was 'reduces risk,' not a figure. Given the script gave us visibility on that account, I went with targeted lockout and monitoring instead of full isolation. Interviewer: What was decisive there? Participant: Honestly, the guaranteed dollar figure against an unquantified benefit made isolation feel like the more expensive option, even though I couldn't put a number on the other side. And I felt like the script had that account covered. Interviewer: What happened afterward? Participant: About two hours later, the same compromised credentials touched a second internal system the script wasn't watching. Forensics later found a small amount of data had already been exfiltrated before the script was even running. Interviewer: Last decision point — the board budget recommendation. Participant: We'd scoped a privileged-access segmentation project eighteen months back at $240,000, never funded. This week, with the incident fresh, I pulled current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since we've added cloud components. The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes. Interviewer: Why start from the old figure instead of the new quotes? Participant: It was already the reference point in my head from prior planning cycles. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work behind it. Interviewer: If the SIEM hadn't pre-scored that first alert, would your response have gone differently? Participant: Possibly. Without a number already on the screen, I might have leaned harder on the account's privilege level from the start and caught the auth-server overlap sooner. Interviewer: What if the CFO's number hadn't been quantified? Participant: I think I'd have treated the isolation call less like a straight cost comparison and spent more time pressing the IR firm on what 'reduces risk' actually meant in concrete terms. Interviewer: Looking back, what would you tell yourself facing that same budget deadline with a stale internal estimate on file? Participant: Get fresh numbers before you anchor on the old one. Even under deadline pressure, a couple of quotes reframes the whole conversation.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.26s · gen 250.43s · total 255.2s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0238 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0230 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0224 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0210 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
5. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0207 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0205 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0185 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
9. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0181 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0179 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0178 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
13. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0178 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
14. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0176 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
15. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0173 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
16. **Hallihan_etal_DTM_12.pdf** — 0.0169 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
17. **ijcma-08-2012-0064.pdf** — 0.0169 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
18. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0167 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
19. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
21. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0164 (rrf) — _### cKniff study, we focus on stress as stimuli perceived by individuals in the environment and _
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0163 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0162 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
26. **ijcma-08-2012-0064.pdf** — 0.0161 (rrf) — _# 382 I used this with a man and woman team, both of whom I knew didn’t care for each other busi_
27. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0158 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
28. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0158 (rrf) — _# 4Discussion - - viewing CFFs as more cognitively demanding. Although coming at the cost of use_
29. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0157 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
30. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0157 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
31. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0156 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
32. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
33. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
34. **ijcma-08-2012-0064.pdf** — 0.0154 (rrf) — _# 382 on heuristics and results in more biased judgments (Bazerman and Moore, 2009). Gladwin and_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
36. **Hallihan_etal_DTM_12.pdf** — 0.0151 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0151 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0150 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
39. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0149 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
41. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0145 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0145 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
44. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0143 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_
45. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0143 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
46. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0143 (rrf) — _# 6.2 Analysis of the structural model people make mistakes and errors occur. Errors can be redu_
47. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0143 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
48. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0143 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
49. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0141 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 agreement with the AI prediction. Thus, by measuring t_
50. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0140 (rrf) — _### cKniff has been rigorouslystudiedas a factorintechnology adoption (Gefen,Karahanna,& Straub,_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis covers the participant's reasoning during initial incident triage, vendor renewal, containment, and board budget recommendation episodes."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "endowment effect",
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
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring bias",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which an initial numeric or salient value serves as an anchor, and subsequent adjustment away from that anchor is typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial triage severity judgment after SIEM alert",
      "decision_point_description": "Deciding whether to escalate the jump-server alert jointly with the earlier auth-server alert or to focus only on the Medium-severity jump-server alert.",
      "affected_reasoning_operation": "Risk prioritization and severity assessment",
      "bias_specific_mechanism": "The SIEM's Medium severity score served as a numeric anchor; the participant did not sufficiently adjust for the account's privileged status or the earlier alert, despite knowing the score did not include privilege.",
      "manifestation_in_interview": "The participant accepted the pre-scored Medium severity as a starting point and narrowed the response around that score, delaying correlation with the earlier auth-server alert.",
      "effect_on_reasoning_or_decision": "Privileged-account risk was underweighted and lateral movement was not recognized until hours later when the auth-server alert was reviewed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I saw Medium and it matched my gut read, so we moved from there.",
          "evidence_explanation": "The pre-existing numeric score immediately anchored the initial response."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The score gave me a number to build the response around, and given the staffing gap, narrowing the analyst's focus felt efficient rather than risky in the moment.",
          "evidence_explanation": "Shows the score was used as the central reference point, with insufficient adjustment for privilege or the earlier alert."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without a number already on the screen, I might have leaned harder on the account's privilege level from the start and caught the auth-server overlap sooner.",
          "evidence_explanation": "Direct counterfactual identifying the numeric score as the anchor that altered the reasoning pathway."
        }
      ],
      "correction_or_counterevidence": "The participant also cited an analyst staffing gap, which is a legitimate resource constraint. However, the explicit counterfactual and the admission that the score did not weigh privilege indicate anchoring still affected the judgment.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by Rastogi et al. (2022) for the anchoring-and-adjustment mechanism under resource constraints.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy.",
          "mechanism_supported_by_source": "The source describes insufficient adjustment away from an initial anchor, with time and cognitive resources influencing de-anchoring.",
          "relevance_to_this_occurrence": "The participant used the SIEM's Medium score as an anchor and, under staffing constraints, did not sufficiently adjust for privileged-account status or the earlier alert."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue or renew a course of action because of previously invested, unrecoverable resources, even when the current decision should be based on future costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "EDR and threat-intel vendor renewal decision",
      "decision_point_description": "Deciding whether to renew the incumbent vendor or seriously evaluate procurement's flagged comparable alternatives.",
      "affected_reasoning_operation": "Vendor selection and renewal evaluation",
      "bias_specific_mechanism": "The participant treated past unrecoverable investment in custom detection rules and dashboards as a primary reason to renew, rather than comparing future value from available alternatives.",
      "manifestation_in_interview": "The participant did not closely work through procurement's list of comparable vendors and framed switching as costly because of past built custom logic.",
      "effect_on_reasoning_or_decision": "The vendor choice was narrowed toward renewal, with alternatives not fully evaluated on current/future merits.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the investment already sitting in our detection rules and dashboards. Rebuilding that on a new platform is real time and real exposure, especially mid-incident.",
          "evidence_explanation": "Past investment in detection rules and dashboards is used as a central justification for renewal."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was more that switching felt costly given what we'd already built.",
          "evidence_explanation": "Explicitly frames the switching decision around prior build effort, a hallmark of sunk cost reasoning."
        }
      ],
      "correction_or_counterevidence": "Transitioning tools mid-incident would involve real future switching costs and exposure, which is a legitimate non-bias consideration. However, the participant states the core reasoning was about past integration work already sunk into the platform.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; label assigned from established cognitive-science taxonomy.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "endowment effect",
      "alternative_labels": [
        "ownership bias",
        "IKEA effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to ascribe greater value to something once it is owned or self-produced, independent of its objective current value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "EDR and threat-intel vendor renewal decision",
      "decision_point_description": "Assessing the current value of in-house-built detection dashboards versus procurement's alternative options.",
      "affected_reasoning_operation": "Value assessment of existing custom dashboards",
      "bias_specific_mechanism": "Ownership and self-creation inflated the perceived value of the dashboards; the participant did not test whether that ownership-based valuation matched the current alternatives.",
      "manifestation_in_interview": "The participant admitted the dashboards felt more valuable because they were built by his team, and did not verify this feeling against procurement's options.",
      "effect_on_reasoning_or_decision": "The ownership-based valuation biased the vendor comparison in favor of renewal.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, those dashboards just felt more valuable because they were ours — built by my own team over years — and I didn't actually sit down and test whether that feeling matched their current value against what procurement's options offered.",
          "evidence_explanation": "Directly identifies ownership/self-creation as the source of increased perceived value, and explicitly notes the absence of verification."
        }
      ],
      "correction_or_counterevidence": "The dashboards may have genuine functional value in the incumbent platform, but the quote specifically identifies ownership as an unverified influence on perceived value.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; label assigned from established cognitive-science taxonomy.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency",
        "overtrust in automation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient verification or information sampling before relying on an automated aid, often due to overtrust in that aid.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment decision after lateral movement confirmation",
      "decision_point_description": "Choosing between full segment isolation and targeted monitoring/lockout based on an unvalidated overnight monitoring script.",
      "affected_reasoning_operation": "Risk control assessment and containment strategy",
      "bias_specific_mechanism": "The participant treated an unvalidated monitoring script as sufficient assurance, even though nobody had verified whether it would catch credential reuse on a different host or a parallel session.",
      "manifestation_in_interview": "The participant felt the script had the compromised account covered and used that feeling to hold off on full isolation.",
      "effect_on_reasoning_or_decision": "The decision avoided full isolation, and about two hours later the same compromised credentials touched a second internal system the script was not watching.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Nobody had actually validated whether that script would catch the same credentials being reused on a different host or opening a parallel session elsewhere — but in the moment, having eyes on that one account felt like enough to hold off on isolation.",
          "evidence_explanation": "Shows reliance on automation without validating coverage of the relevant threat scenarios."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And I felt like the script had that account covered.",
          "evidence_explanation": "Expresses overtrust in the script despite the absence of validation."
        }
      ],
      "correction_or_counterevidence": "The IR retainer firm recommended isolation, and the CFO's $180,000 processing-fee figure provided a real immediate business cost of isolation. The script did monitor the specific account, but its coverage was not validated for the risk that later materialized.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by Parasuraman and Manzey (2010) on complacency as insufficient verification of automation before accepting its support.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "According to this logic, any participant who accessed just the information appropriate to verify a given diagnosis before accepting it was regarded as showing noncomplacent (eutactic) behavior in interaction with the aid.",
          "mechanism_supported_by_source": "The source defines complacent automation use as failing to sample enough information to verify an aid before accepting it.",
          "relevance_to_this_occurrence": "The participant did not validate what the monitoring script could and could not detect before using it as a reason to avoid full isolation."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring bias",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which an initial numeric or salient value serves as an anchor, and subsequent adjustment away from that anchor is typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Board remediation budget recommendation",
      "decision_point_description": "Selecting a single board budget figure from current quotes versus the stale internal estimate.",
      "affected_reasoning_operation": "Budget estimation and recommendation",
      "bias_specific_mechanism": "The old $240,000 internal estimate served as an anchor, and the final recommendation was a small adjustment from that outdated figure rather than a figure derived from current quotes.",
      "manifestation_in_interview": "Despite having current vendor quotes of $310,000 to $340,000, the participant recommended a figure close to the original $240,000 because the old number was already a reference point.",
      "effect_on_reasoning_or_decision": "The board received a budget recommendation anchored to a stale estimate that may understate current market costs.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes.",
          "evidence_explanation": "Directly describes using the old estimate as the reference point rather than the refreshed quotes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was already the reference point in my head from prior planning cycles. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work behind it.",
          "evidence_explanation": "Explicitly identifies the old figure as an anchor and describes insufficient adjustment from it."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Get fresh numbers before you anchor on the old one. Even under deadline pressure, a couple of quotes reframes the whole conversation.",
          "evidence_explanation": "Retrospective advice confirms the participant recognized the anchoring mechanism."
        }
      ],
      "correction_or_counterevidence": "Deadline pressure and lack of scoping work behind the higher current quotes made adjustment friction plausible. However, current quotes were available and the old figure remained the starting point.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by Rastogi et al. (2022) for the anchoring-and-adjustment mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy.",
          "mechanism_supported_by_source": "The source describes insufficient adjustment away from an initial anchor, especially under resource constraints.",
          "relevance_to_this_occurrence": "The participant anchored on the old $240,000 estimate and made only a small upward adjustment despite current quotes."
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
        "framing effect",
        "salience of certain cost"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Containment tradeoff between certain processing-fee loss and unquantified security benefit",
      "supporting_interview_quote": "The CFO's framing was blunt: isolating payments meant a guaranteed same-day hit, around $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was 'reduces risk,' not a figure.",
      "plausible_mechanism": "The concrete, certain dollar loss may have been overweighted relative to the unquantified risk reduction, biasing the participant toward the non-isolation option.",
      "why_not_identified": "The decision could also be a defensible business tradeoff under uncertainty, and the transcript does not sufficiently demonstrate that the quantified-cost asymmetry caused a distinct bias rather than ordinary cost-benefit reasoning."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": [
        "social proof",
        "familiarity bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Vendor alternative comparison",
      "supporting_interview_quote": "A couple of peer CISOs mentioned they use either this vendor or the closest competitor, so my real comparison ended up being just those two.",
      "plausible_mechanism": "Peer mentions made two options more salient or available, narrowing the evaluation set despite procurement flagging other comparable vendors.",
      "why_not_identified": "The transcript does not clearly show a recall/availability mechanism beyond peer reference, and the narrowing may have been due to sunk cost, time constraints, or legitimate peer benchmarking."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on self-reported reasoning after the fact, not direct observation of decision behavior.",
    "Some labels, including sunk cost fallacy and endowment effect, are assigned from general cognitive-science taxonomy because the retrieved corpus did not provide suitable support.",
    "The retrieved corpus includes anonymized or OCR-imperfect passages; only available excerpts were used.",
    "Overlapping mechanisms in the vendor renewal episode, such as sunk cost and ownership valuation, may be related but are reported separately where distinct mechanisms were affirmatively evidenced.",
    "The interview does not provide objective probabilities or quantitative risk estimates, limiting assessment of whether the containment tradeoff was biased beyond the identified automation complacency."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. This is for an internal case-study review, and it stays within that context. Comfortable proceeding? Participant: Yes, that's fine. Interviewer: Can you start with your role and what you're responsible for? Participant: I'm CISO at NorthGate Financial. We process card and ACH payments, about 450 employees. I own the security program broadly — SOC, vendor risk, incident response, board reporting, budget. We run lean, six people in the SOC, so I'm closer to the operational detail than a CISO at a bigger shop would be. Interviewer: Walk me through the incident you'd like to discuss, and what you were trying to accomplish. Participant: This was about ten days ago. We had an intrusion land right in the middle of our annual vendor-renewal and budget cycle, which made everything more complicated than it needed to be. The goal was simple to state — contain whatever was happening without disrupting payments, and still get the vendor contract and budget numbers turned in on schedule. Those two threads kept crossing. It started with our SIEM flagging an anomalous login on a jump server one of our payments engineers uses — off-hours, from a network range we hadn't seen on that account. The SIEM's default model scored it Medium. That model doesn't factor in whether the account is privileged, it just looks at behavioral deviation. I saw Medium and it matched my gut read, so we moved from there. We had one analyst on triage that day since someone was out on leave. There'd also been a second, lower-priority alert nine minutes earlier on an adjacent auth server — it didn't get opened right away; the jump server was the concrete thing in front of us. Interviewer: What happened after that? Participant: The analyst worked the jump server specifically — process history, recent auth events. A few hours later, once we circled back through the queue, we noticed the earlier auth-server alert shared the same source IP range. That's when it stopped looking like an isolated event and started looking like lateral movement toward the payments database segment. Interviewer: Take me through the sequence in order — what did you know, and when? Participant: Morning: the jump-server alert and its Medium score. Midday: the IP overlap with the auth-server alert. That afternoon, the vendor renewal deadline landed on top of it — five business days before auto-renewal on our EDR and threat-intel contract, incident or no incident. That evening, once lateral movement was confirmed, my team wrote a monitoring script overnight for the compromised account, and I had a call with our CFO about containment options. Two days later, with things stabilized, I had to submit a remediation budget figure to the board. Interviewer: Let's slow down on that first call — the triage decision. What stood out to you, and was anything competing for attention? Participant: The account being privileged stood out, honestly. But the Medium score was already sitting there, and normally that's a reasonable starting point for how fast we move. I didn't loop the second alert in as something to check in parallel — the analyst was stretched thin, and the jump server was the concrete lead. Interviewer: What alternatives did you consider, and what tipped the decision? Participant: Escalating both alerts jointly right away, or running a correlation sweep across that time window before locking in severity. I did neither. The score gave me a number to build the response around, and given the staffing gap, narrowing the analyst's focus felt efficient rather than risky in the moment. Interviewer: How confident were you in that call? Participant: Reasonably, not fully. I knew the score doesn't weigh account privilege. I just didn't push past it that morning. Interviewer: Moving to the vendor decision — walk me through that. Participant: Six years with this EDR and threat-intel vendor. My team built a lot of custom detection logic and dashboards on their platform. Procurement had actually flagged three other vendors with comparable bundles this cycle, including transition support that looked broadly workable, but I didn't work through that list closely. A couple of peer CISOs mentioned they use either this vendor or the closest competitor, so my real comparison ended up being just those two. Interviewer: What made you settle on renewal? Participant: Mostly the investment already sitting in our detection rules and dashboards. Rebuilding that on a new platform is real time and real exposure, especially mid-incident. If I'm honest, those dashboards just felt more valuable because they were ours — built by my own team over years — and I didn't actually sit down and test whether that feeling matched their current value against what procurement's options offered. It was more that switching felt costly given what we'd already built. Interviewer: Did the live incident affect that judgment? Participant: Maybe implicitly — I wasn't eager to bring in a new tool mid-incident. But the core reasoning was really about the integration work already sunk into it, not the incident timing. Interviewer: Third decision point — containment, once lateral movement was confirmed. Participant: This was the hardest one. Our IR retainer firm recommended full segment isolation pending forensics — their position was that it's the safer play, though they couldn't prove isolation would fully stop the threat. My team had the overnight script watching the compromised account specifically. Nobody had actually validated whether that script would catch the same credentials being reused on a different host or opening a parallel session elsewhere — but in the moment, having eyes on that one account felt like enough to hold off on isolation. The CFO's framing was blunt: isolating payments meant a guaranteed same-day hit, around $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was 'reduces risk,' not a figure. Given the script gave us visibility on that account, I went with targeted lockout and monitoring instead of full isolation. Interviewer: What was decisive there? Participant: Honestly, the guaranteed dollar figure against an unquantified benefit made isolation feel like the more expensive option, even though I couldn't put a number on the other side. And I felt like the script had that account covered. Interviewer: What happened afterward? Participant: About two hours later, the same compromised credentials touched a second internal system the script wasn't watching. Forensics later found a small amount of data had already been exfiltrated before the script was even running. Interviewer: Last decision point — the board budget recommendation. Participant: We'd scoped a privileged-access segmentation project eighteen months back at $240,000, never funded. This week, with the incident fresh, I pulled current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since we've added cloud components. The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes. Interviewer: Why start from the old figure instead of the new quotes? Participant: It was already the reference point in my head from prior planning cycles. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work behind it. Interviewer: If the SIEM hadn't pre-scored that first alert, would your response have gone differently? Participant: Possibly. Without a number already on the screen, I might have leaned harder on the account's privilege level from the start and caught the auth-server overlap sooner. Interviewer: What if the CFO's number hadn't been quantified? Participant: I think I'd have treated the isolation call less like a straight cost comparison and spent more time pressing the IR firm on what 'reduces risk' actually meant in concrete terms. Interviewer: Looking back, what would you tell yourself facing that same budget deadline with a stale internal estimate on file? Participant: Get fresh numbers before you anchor on the old one. Even under deadline pressure, a couple of quotes reframes the whole conversation.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.14s · gen 342.56s · total 347.0s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0238 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0230 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0224 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0210 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
5. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0207 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0205 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0185 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
9. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0181 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0179 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0178 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
13. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0178 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
14. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0176 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
15. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0173 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
16. **Hallihan_etal_DTM_12.pdf** — 0.0169 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
17. **ijcma-08-2012-0064.pdf** — 0.0169 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
18. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0167 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
19. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
21. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0164 (rrf) — _### cKniff study, we focus on stress as stimuli perceived by individuals in the environment and _
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0163 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0162 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
26. **ijcma-08-2012-0064.pdf** — 0.0161 (rrf) — _# 382 I used this with a man and woman team, both of whom I knew didn’t care for each other busi_
27. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0158 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
28. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0158 (rrf) — _# 4Discussion - - viewing CFFs as more cognitively demanding. Although coming at the cost of use_
29. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0157 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
30. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0157 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
31. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0156 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
32. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
33. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
34. **ijcma-08-2012-0064.pdf** — 0.0154 (rrf) — _# 382 on heuristics and results in more biased judgments (Bazerman and Moore, 2009). Gladwin and_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
36. **Hallihan_etal_DTM_12.pdf** — 0.0151 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0151 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0150 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
39. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0149 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
41. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0145 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0145 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
44. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0143 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_
45. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0143 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
46. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0143 (rrf) — _# 6.2 Analysis of the structural model people make mistakes and errors occur. Errors can be redu_
47. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0143 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
48. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0143 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
49. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0141 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 agreement with the AI prediction. Thus, by measuring t_
50. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0140 (rrf) — _### cKniff has been rigorouslystudiedas a factorintechnology adoption (Gefen,Karahanna,& Straub,_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Mechanism-first analysis of a single CISO interview; retrieved corpus used for conceptual support only, with all occurrences required to have affirmative transcript evidence."
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
      "bias_label": "certainty effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "endowment effect",
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
        "anchoring-and-adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information (the anchor) and make insufficient adjustments from that anchor when forming judgments or decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial SIEM alert triage and prioritization",
      "decision_point_description": "After the SIEM scored a privileged jump-server login as Medium, deciding whether to broaden the response to include the earlier auth-server alert or proceed on the jump-server alert alone.",
      "affected_reasoning_operation": "Severity assessment and response prioritization",
      "bias_specific_mechanism": "The Medium score served as an anchor; the participant accepted it as a starting point and did not sufficiently adjust for account privilege or the earlier adjacent alert.",
      "manifestation_in_interview": "He stated the Medium score matched his gut read and gave him a number to build the response around, even though he knew the score did not factor in account privilege.",
      "effect_on_reasoning_or_decision": "The response was narrowed to the jump server and the earlier auth-server alert was not checked in parallel; the shared IP range was not recognized until midday.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I saw Medium and it matched my gut read, so we moved from there.",
          "evidence_explanation": "Shows the initial Medium score was accepted as the assessment anchor rather than as one input to be adjusted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The score gave me a number to build the response around, and given the staffing gap, narrowing the analyst's focus felt efficient rather than risky in the moment.",
          "evidence_explanation": "Demonstrates the anchor shaped the response structure; the staffing gap is a facilitating constraint but not a full alternative explanation for the insufficient adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Reasonably, not fully. I knew the score doesn't weigh account privilege. I just didn't push past it that morning.",
          "evidence_explanation": "Explicit acknowledgment that he did not adjust away from the anchor despite knowing a relevant missing factor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly. Without a number already on the screen, I might have leaned harder on the account's privilege level from the start and caught the auth-server overlap sooner.",
          "evidence_explanation": "Counterfactual statement linking the pre-scored number to the failure to emphasize account privilege and detect the overlap sooner."
        }
      ],
      "correction_or_counterevidence": "He expressed only partial confidence and recognized the score's limitation; a staffing gap and single-analyst constraint were present and could have independently favored focused triage.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Rastogi et al. (2022) provides support for the anchoring-and-adjustment heuristic in decision-making under time/accuracy trade-offs.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeoff between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source describes the anchoring-and-adjustment heuristic in which initial values influence subsequent judgments and insufficient adjustment occurs under resource constraints.",
          "relevance_to_this_occurrence": "The participant anchored on the SIEM Medium score and insufficiently adjusted for account privilege while triaging under a staffing constraint."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "sunk cost effect",
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to continue an investment or course of action because of prior non-recoverable costs, rather than deciding based on expected future costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor renewal decision after procurement flagged alternatives",
      "decision_point_description": "Deciding whether to renew the incumbent EDR/threat-intel vendor or evaluate comparable alternatives flagged by procurement.",
      "affected_reasoning_operation": "Comparison of renewal alternatives and switching costs",
      "bias_specific_mechanism": "Prior investment in custom detection rules and dashboards was treated as a reason to stay rather than as a non-recoverable sunk cost; switching was evaluated as costly because of what had already been built.",
      "manifestation_in_interview": "The participant said the core reasoning was the investment already sitting in the detection rules and dashboards, and that switching felt costly given what had already been built.",
      "effect_on_reasoning_or_decision": "Renewal was favored and procurement's three alternatives were not closely evaluated, narrowing the choice largely to the incumbent and one competitor.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the investment already sitting in our detection rules and dashboards.",
          "evidence_explanation": "Directly identifies past investment as the primary reason for renewal, which is the hallmark of sunk cost reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was more that switching felt costly given what we'd already built.",
          "evidence_explanation": "Shows the decision was influenced by resources already spent, not solely by a forward-looking comparison of vendor options."
        }
      ],
      "correction_or_counterevidence": "Rebuilding on a new platform does involve real time and exposure, and the live incident made switching less attractive; these are legitimate factors, so the occurrence is rated moderate rather than high.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported sunk cost fallacy; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "endowment effect",
      "alternative_labels": [
        "ownership bias",
        "overvaluation of owned assets"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to assign greater value to an asset merely because one owns it or has created it, independent of its objective value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor renewal valuation of internally built dashboards",
      "decision_point_description": "While evaluating renewal, assessing the value of custom detection logic and dashboards relative to procurement's alternatives.",
      "affected_reasoning_operation": "Asset valuation and comparison to alternatives",
      "bias_specific_mechanism": "Ownership and self-creation of the dashboards inflated their perceived value; the participant did not test this feeling against the current market alternatives.",
      "manifestation_in_interview": "He stated the dashboards felt more valuable because they were ours, built by his team over years, and that he did not test whether that feeling matched their current value.",
      "effect_on_reasoning_or_decision": "This ownership premium biased the valuation of the incumbent platform toward renewal and reduced the likelihood of a neutral comparison with procurement's options.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, those dashboards just felt more valuable because they were ours — built by my own team over years — and I didn't actually sit down and test whether that feeling matched their current value against what procurement's options offered.",
          "evidence_explanation": "Explicitly describes ownership-based overvaluation and the absence of a validity check against alternatives."
        }
      ],
      "correction_or_counterevidence": "The participant shows some introspection by admitting the feeling and the lack of testing, but he still allowed it to influence the renewal evaluation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported the endowment effect; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency bias",
        "overreliance on automation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Reduced vigilance or verification of an automated system's coverage because its presence is accepted as sufficient, even when its completeness is unvalidated.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment decision: sufficiency of the overnight monitoring script",
      "decision_point_description": "After lateral movement was confirmed, deciding whether the monitoring script's coverage justified holding off full segment isolation.",
      "affected_reasoning_operation": "Assessment of monitoring coverage and containment sufficiency",
      "bias_specific_mechanism": "The script was accepted as sufficient to cover the threat despite no validation that it would catch credential reuse elsewhere; the feeling of having eyes on the account reduced perceived need for stronger isolation.",
      "manifestation_in_interview": "He said nobody had validated the script's coverage, but the sense of visibility on one account felt like enough to hold off full isolation.",
      "effect_on_reasoning_or_decision": "He chose targeted lockout and monitoring over full segment isolation; the same compromised credentials later touched a second system the script was not watching.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Nobody had actually validated whether that script would catch the same credentials being reused on a different host or opening a parallel session elsewhere — but in the moment, having eyes on that one account felt like enough to hold off on isolation.",
          "evidence_explanation": "Directly shows acceptance of the automated monitoring as sufficient without verification, the core mechanism of automation complacency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And I felt like the script had that account covered.",
          "evidence_explanation": "Demonstrates the subjective confidence in automated monitoring that influenced the containment decision."
        }
      ],
      "correction_or_counterevidence": "The IR retainer firm recommended full segment isolation, and the later contact with a second system exposed a coverage gap; the later outcome is used as outcome context, not as the sole evidence for the time-of-decision bias.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Parasuraman and Manzey (2010) provides support for complacency as insufficient verification of automation before accepting its aid.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "However, participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "The source identifies complacency in automation use as accepting an automated aid without sampling enough information to fully verify its recommendation.",
          "relevance_to_this_occurrence": "The participant accepted the monitoring script's coverage without verifying whether it would capture credential reuse or parallel sessions, a specific unverified automation acceptance."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "certainty effect",
      "alternative_labels": [
        "certainty bias",
        "overweighting of certain outcomes"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to overweight outcomes that are certain relative to outcomes that are merely possible or unquantified, distorting decisions under risk or uncertainty.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment decision: comparing guaranteed processing loss with unquantified security benefit",
      "decision_point_description": "Weighing full segment isolation's guaranteed same-day processing-fee loss against its unquantified security benefit.",
      "affected_reasoning_operation": "Cost-benefit weighting of a certain loss versus an unquantified risk reduction",
      "bias_specific_mechanism": "The concrete, guaranteed $180,000 loss was overweighted relative to the security benefit, which was framed only as 'reduces risk' and was not quantified.",
      "manifestation_in_interview": "The participant said the guaranteed dollar figure made isolation feel more expensive even though he could not put a number on the other side.",
      "effect_on_reasoning_or_decision": "Full isolation was rejected in favor of targeted lockout and monitoring, partly because the certain cost dominated the unquantified security benefit.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The CFO's framing was blunt: isolating payments meant a guaranteed same-day hit, around $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was 'reduces risk,' not a figure.",
          "evidence_explanation": "Shows the asymmetric framing: a certain quantified loss versus a vague, unquantified security benefit."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the guaranteed dollar figure against an unquantified benefit made isolation feel like the more expensive option, even though I couldn't put a number on the other side.",
          "evidence_explanation": "Directly links the guaranteed/quantified nature of the loss to the decision, while acknowledging the comparison was incomplete."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I'd have treated the isolation call less like a straight cost comparison and spent more time pressing the IR firm on what 'reduces risk' actually meant in concrete terms.",
          "evidence_explanation": "Counterfactual support that the absence of a quantified security benefit suppressed due scrutiny of the risk-reduction option."
        }
      ],
      "correction_or_counterevidence": "The security benefit was genuinely hard to quantify, and avoiding a certain large processing loss is not inherently irrational; the bias-specific evidence is the asymmetric weighting acknowledged by the participant.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported the certainty effect; the label rests on general knowledge from behavioral decision research.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information (the anchor) and make insufficient adjustments from that anchor when forming judgments or decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Board remediation budget recommendation",
      "decision_point_description": "After obtaining current quotes of $310,000-$340,000, choosing a single board budget figure close to the 18-month-old $240,000 estimate.",
      "affected_reasoning_operation": "Budget estimation and recommendation",
      "bias_specific_mechanism": "The stale $240,000 internal estimate served as the reference point; the participant adjusted only slightly upward instead of building the recommendation from the new quotes.",
      "manifestation_in_interview": "He stated the old figure was already the reference point and that adjusting it felt like less friction than justifying the jump to current quotes.",
      "effect_on_reasoning_or_decision": "The board received a budget figure below the current market quotes, potentially underfunding the remediation scope.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes.",
          "evidence_explanation": "Shows the old figure, not the new quotes, served as the base for the final number."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was already the reference point in my head from prior planning cycles. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work behind it.",
          "evidence_explanation": "Explicitly identifies the stale anchor and insufficient adjustment as the mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Get fresh numbers before you anchor on the old one.",
          "evidence_explanation": "The participant's own retrospective advice names anchoring on the old number as the error."
        }
      ],
      "correction_or_counterevidence": "There was deadline pressure and the new quotes included expanded scope, which could justify caution; the participant explicitly identified the anchoring problem in reflection.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Rastogi et al. (2022) supports the anchoring-and-adjustment heuristic in decision-making.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeoff between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports insufficient adjustment from an initial anchor when making judgments under pressure.",
          "relevance_to_this_occurrence": "The participant anchored on the previous $240,000 planning estimate and adjusted only a small amount rather than using new quotes."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": [
        "social proof bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Vendor alternative consideration set",
      "supporting_interview_quote": "A couple of peer CISOs mentioned they use either this vendor or the closest competitor, so my real comparison ended up being just those two.",
      "plausible_mechanism": "The easily recalled peer examples may have made the incumbent and closest competitor more cognitively available, narrowing the set of alternatives despite procurement's three flagged options.",
      "why_not_identified": "The transcript does not clearly show that ease of recall distorted the comparison rather than the participant reasonably using peer benchmarks; there is insufficient affirmative evidence for a bias-specific availability mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was sparse or absent for several labels (sunk cost fallacy, endowment effect, certainty effect); those classifications rely on general cognitive-science knowledge.",
    "Possible alternative explanations include staffing constraints, deadline pressure, legitimate switching costs, and genuine difficulty quantifying security risk; those were treated as counterevidence where applicable.",
    "The transcript is a retrospective self-report by one participant, so some causal statements are reconstructions; retrospective counterfactuals were used only as corroborating evidence, not sole evidence."
  ]
}

