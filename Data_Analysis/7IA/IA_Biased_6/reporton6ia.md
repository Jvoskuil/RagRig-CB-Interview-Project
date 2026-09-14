# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and I'll ask you to walk me through a specific shift in detail. You can skip anything you're not comfortable sharing. Can you tell me your role and how long you've been doing it? Participant: Sure. I'm a threat intelligence analyst on the SOC team, been in this seat about four years, mostly financial services environments. My job during shift is triage, attribution, and hunt scoping when something looks like it's more than commodity noise. Interviewer: Good. Let's start broad. Can you walk me through what this shift looked like when the alert cluster first appeared? Participant: It was maybe two hours into an overnight shift. EDR kicked out a cluster of alerts on a trading-support server — not the trading engine itself, but a box that feeds reporting data to it. The auto-triage score came back Low. Historically, that queue throws a lot of low-severity noise, especially from that server, so my first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing. Interviewer: What was your primary objective at that point? Participant: Get through the queue, keep the shift moving, and not waste the incident response lead's time on something that turns out to be benign. We only had about three hours left in the shift, and I wanted whatever I handed off to be solid, not a guess. Interviewer: Take me through what happened next, chronologically. Participant: So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet. About forty minutes later, a follow-up alert showed an outbound connection from that same host to an IP I didn't recognize. That's when I actually opened the case properly. I found a registry-key artifact that matched something documented in a GreyFalcon campaign from about six months back — I remembered writing that report myself, so it stuck with me. Around the same time, internal telemetry showed an attempted connection to the HR benefits database from that host, which was strange, but I moved forward with attribution anyway. Then I pulled a vendor bulletin that had just come in — the vendor portal access was closing soon, so I read it quickly. It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that. Near the end of shift, I had to write up a containment recommendation for the IR lead, and I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of 'possibly' and 'unclear.' Interviewer: Let's slow down and go through each of those decisions one at a time. First one — the initial Low-severity alert. What cues were you weighing right then? Participant: Mainly the auto-triage score and my own memory of that server generating false alarms before. No unusual business disruption was reported either, which reinforced it felt routine. Interviewer: What made you decide to defer the manual log pull rather than doing it right away? Participant: Time, mostly. The score was Low, I had precedent that Low from that host usually meant nothing, and pulling raw logs is a real time cost. Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me. It felt like a reasonable use of triage priority rather than checking every single alert by hand. Interviewer: Did you consider escalating to the IR lead first instead? Participant: I thought about it, but that seemed like overkill for a Low score with no other signal at that point. In hindsight, I probably could've spent the fifteen minutes given how the next forty minutes went, but at the time it didn't seem to justify interrupting anyone. Interviewer: Understood. Let's move to the attribution decision after the outbound connection appeared. What was the basis for assigning GreyFalcon? Participant: The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in. Interviewer: You mentioned the C2 domain's registration pattern looked different from GreyFalcon's usual infrastructure. How did that factor in? Participant: It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then. Interviewer: And the HR database access attempt — GreyFalcon has typically gone after trading or financial data in your prior tracking. How did you read that mismatch? Participant: My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly. So it didn't strike me as inconsistent with the group, more like an opportunistic pivot they'd make if they were being efficient about it. Interviewer: Did you weigh that explanation against the possibility that it wasn't GreyFalcon at all? Participant: Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself. Interviewer: Let's talk about the hunt scope decision, once the vendor bulletin came in. Walk me through how you decided what to include. Participant: The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up. It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources. There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary. Interviewer: The bulletin listed two file-hash IOCs last — how much did those factor into the scope? Participant: Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely. Interviewer: Was there consideration of scoping broadly across all five IOCs regardless of order? Participant: There was, briefly — business owners wanted it narrow anyway to avoid downtime on trading-adjacent systems, so narrow scope aligned with what they wanted too. That made it easier to just go with the scope that already made sense to me. Interviewer: Last decision point — the containment recommendation. You mentioned leaning on the vendor bulletin over a colleague's notes. What drove that? Participant: Time pressure, for one — I needed something to hand the IR lead within the hour. But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — 'possibly,' 'unclear if,' that kind of thing. The vendor version gave me something concrete to act on. Interviewer: Did you compare the actual evidence underlying each source, separate from how they were written? Participant: Not directly side by side, no. I read the vendor one, it felt solid, and I went with it. Interviewer: How confident were you overall in the final recommendation you handed off? Participant: Reasonably confident, maybe seven out of ten. Enough uncertainty that I flagged it as needing follow-up validation next shift, but I felt the containment steps were defensible given what I had. Interviewer: Looking back across the shift, if you'd pulled the raw logs immediately in phase one instead of deferring, how do you think things would've unfolded differently? Participant: I might have caught the odd outbound connection sooner, maybe before the vendor window closed, which could've changed how much I leaned on that bulletin later. Hard to say for certain. Interviewer: If the vendor bulletin had listed its IOCs in reverse order, hash-based ones first, do you think your scoping would have changed? Participant: Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope. Interviewer: Is there a point in this sequence where you'd want a second analyst's independent read before proceeding? Participant: Probably the attribution step. That's where I moved fastest from one piece of strong evidence to a full working theory, and a second set of eyes might have pushed back on the infrastructure mismatch or the HR access pattern before I built the rest of the shift around it. Interviewer: That's helpful, thank you. I think that covers what I need.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.19s · gen 320.08s · total 326.4s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0273 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0266 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0257 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0251 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0235 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0226 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
7. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0206 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0193 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0192 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
13. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0188 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_
14. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0187 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0184 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
16. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0184 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
17. **Lyell Automation bias and verification complexity.pdf** — 0.0183 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
19. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0179 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
21. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0171 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0169 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0169 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
25. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
26. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0166 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
27. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0165 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
28. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0161 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
30. **Hallihan_etal_DTM_12.pdf** — 0.0158 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
32. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0157 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
33. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
34. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0155 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
36. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0154 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
37. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0154 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
39. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0152 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
40. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0151 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
41. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0149 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
44. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0148 (rrf) — _# across domains and different parts of the search process. to help inform their opinions \[ 45 _
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
47. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0146 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
48. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0145 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
50. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0141 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Blind diagnostic evaluation of a single CTA interview transcript for affirmative cognitive bias occurrences; retrieved passages were used only for taxonomy and mechanism validation."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "automation bias",
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
      "bias_label": "automation bias",
      "alternative_labels": [
        "automation complacency",
        "overreliance on automated decision support"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to over-rely on automated decision support, leading to omission or commission errors when automation output is treated as authoritative rather than independently verified.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial Low-severity alert triage",
      "decision_point_description": "Whether to immediately pull raw logs and investigate a Low-severity auto-triage alert or defer manual verification.",
      "affected_reasoning_operation": "Verification and attention allocation in automated alert triage",
      "bias_specific_mechanism": "Over-reliance on the automated triage score led to insufficient manual log verification; the Low label and prior false-positive experience acted as an authority-like signal that suppressed deeper inspection of an anomalous parent process.",
      "manifestation_in_interview": "The participant deferred a manual raw log pull after a Low severity auto-triage score and later noticed an unfamiliar parent process but explained it away as unimportant because the score 'did the deciding.'",
      "effect_on_reasoning_or_decision": "Delayed detection and investigation of the outbound connection and anomalous parent process; the decision allowed the case to remain unexamined for approximately forty minutes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet.",
          "evidence_explanation": "Shows that the automated Low score directly preceded a decision to avoid manual verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me.",
          "evidence_explanation": "Demonstrates that the automated score overrode an anomalous cue, consistent with automation overreliance rather than purely time-based triage."
        }
      ],
      "correction_or_counterevidence": "Time pressure and a prior history of false positives from the same server provided a plausible non-bias basis for deferral; however, the explicit statement that the Low score 'did the deciding' supports a distinct automation bias mechanism. Later alerts eventually prompted case opening.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman and Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "approximately 43% of operators did not detect a wrong diagnosis of the aid when it occurred for the first time. Analyses of informationsampling behavior revealed that half of the participants made this commission error because of a clear complacency effect, as reflected in an incomplete sampling of information needed for automation verification.",
          "mechanism_supported_by_source": "Complacency in automation use causes incomplete information sampling and insufficient verification of automated advice.",
          "relevance_to_this_occurrence": "The participant similarly declined to pull raw logs and verify the automated triage score despite an anomalous parent process, leading to an omission error."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "hypothesis confirmation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or strengthens one's prior beliefs or hypotheses, while giving disproportionately little consideration to alternative possibilities or contradictory evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "GreyFalcon attribution decision",
      "decision_point_description": "Whether to adopt GreyFalcon as the working attribution hypothesis in view of partially inconsistent infrastructure and target-behavior evidence.",
      "affected_reasoning_operation": "Hypothesis evaluation and evidence weighting for threat attribution",
      "bias_specific_mechanism": "Confirmation bias led the participant to treat a single registry-key match as highly diagnostic while rationalizing mismatched infrastructure and HR data behavior as still consistent with GreyFalcon; he did not actively test non-GreyFalcon alternatives.",
      "manifestation_in_interview": "The participant fixed on GreyFalcon attribution after one strong artifact and dismissed contradictory infrastructure and target-set cues with ad hoc explanations.",
      "effect_on_reasoning_or_decision": "The participant prematurely adopted GreyFalcon attribution and propagated that frame into subsequent hunting and scoping decisions without adequately considering non-GreyFalcon explanations.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in.",
          "evidence_explanation": "Shows preferential weighting of confirmatory prior evidence and rapid adoption of a hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then.",
          "evidence_explanation": "Demonstrates a contradictory cue being acknowledged but then underweighted to maintain the initial attribution."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself.",
          "evidence_explanation": "Shows that inconsistent target behavior was explained away rather than used as a prompt to test alternatives."
        }
      ],
      "correction_or_counterevidence": "The participant did notice the infrastructure mismatch and HR data mismatch, and later rated confidence as seven out of ten with follow-up validation recommended; however, these were not sufficient to revise attribution during the shift.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human Factors of the Confirmation Bias in Intelligence Analysis: Decision Support from Graphical Evidence Layout",
          "authors": "Cook and Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at as- sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias can distort intelligence analysts' selection and prioritization of evidence.",
          "relevance_to_this_occurrence": "The participant selected and prioritized the registry-key match while discounting contradictory infrastructure and target-behavior evidence."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information as an anchor and to adjust insufficiently from that anchor when making subsequent judgments or decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hunt scope construction from vendor bulletin IOCs",
      "decision_point_description": "Which vendor bulletin IOCs and hypotheses should drive the hunt scope.",
      "affected_reasoning_operation": "Information ordering and scope construction",
      "bias_specific_mechanism": "Anchoring-and-adjustment: the first vendor IOC served as the initial anchor for the hunt scope; later, possibly more specific and lower-false-positive-risk IOCs were underweighted because the scope had already been built around the first item and the existing GreyFalcon story.",
      "manifestation_in_interview": "The participant built the hunt scope around the first IOC in the vendor bulletin and acknowledged he likely would have anchored on other IOCs if they had been listed first.",
      "effect_on_reasoning_or_decision": "Narrowed the hunt scope to systems matching the first IOC and the GreyFalcon pattern, potentially missing a broader infection or an alternative explanation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up. It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources.",
          "evidence_explanation": "Shows that the first listed IOC became the basis for the hunt scope."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely.",
          "evidence_explanation": "Explicitly identifies the order-based anchor and insufficient adjustment to later IOCs."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope.",
          "evidence_explanation": "Confirms that reversing the IOC order would have changed the anchor and likely the hunt scope."
        }
      ],
      "correction_or_counterevidence": "Business owners also wanted a narrow scope to avoid downtime on trading-adjacent systems, which may have reinforced the narrow scope; however, the participant explicitly attributed scope construction to first-item order and his existing GreyFalcon story.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "participants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Anchoring-and-adjustment can cause insufficient adjustment from an initial value, especially under time or resource constraints.",
          "relevance_to_this_occurrence": "The participant scoped the hunt around the first IOC as an anchor and underweighted later IOCs; he predicted a different anchor would have produced a different scope."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "authority bias",
      "alternative_labels": [
        "processing fluency bias",
        "source credibility heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to assign greater accuracy or evidentiary weight to information based on the perceived authority or superficial presentation of its source, rather than on the underlying evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final containment recommendation source selection",
      "decision_point_description": "Whether to rely on the vendor bulletin or the colleague's hedged notes for the containment recommendation.",
      "affected_reasoning_operation": "Source evaluation and evidentiary weighting",
      "bias_specific_mechanism": "Perceived authority and processing fluency of the vendor bulletin substituted for direct comparison of underlying evidence quality, leading the participant to rely on the vendor document over a colleague's accurate but hedged notes.",
      "manifestation_in_interview": "The participant chose the vendor bulletin for containment because it read as authoritative, clean, and confidently written, rather than comparing the actual evidence underlying each source.",
      "effect_on_reasoning_or_decision": "The containment recommendation rested on the vendor bulletin rather than a direct evidentiary comparison, potentially privileging style and source authority over substantive validation of the colleague's notes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — 'possibly,' 'unclear if,' that kind of thing. The vendor version gave me something concrete to act on.",
          "evidence_explanation": "Shows source selection driven by presentation quality and perceived authority rather than evidence quality."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly side by side, no. I read the vendor one, it felt solid, and I went with it.",
          "evidence_explanation": "Confirms that the participant did not compare the underlying evidence, relying instead on the subjective solidity of the vendor document."
        }
      ],
      "correction_or_counterevidence": "Vendor bulletins can be legitimate authoritative sources in SOC work, and time pressure constrained source comparison; the participant also flagged the final recommendation for follow-up validation, indicating some residual uncertainty.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly addressed authority or processing fluency biases; classification relies on established general cognitive-science knowledge of authority and fluency effects.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Single interview transcript without independent behavioral observation or outcome data.",
    "Retrieved corpus passages contained OCR noise and limited metadata; some passages may be incomplete.",
    "Several reasoning episodes involved time pressure and legitimate domain heuristics, which could partially explain some behavior.",
    "No experimental condition or counterfactual information was available."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and I'll ask you to walk me through a specific shift in detail. You can skip anything you're not comfortable sharing. Can you tell me your role and how long you've been doing it? Participant: Sure. I'm a threat intelligence analyst on the SOC team, been in this seat about four years, mostly financial services environments. My job during shift is triage, attribution, and hunt scoping when something looks like it's more than commodity noise. Interviewer: Good. Let's start broad. Can you walk me through what this shift looked like when the alert cluster first appeared? Participant: It was maybe two hours into an overnight shift. EDR kicked out a cluster of alerts on a trading-support server — not the trading engine itself, but a box that feeds reporting data to it. The auto-triage score came back Low. Historically, that queue throws a lot of low-severity noise, especially from that server, so my first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing. Interviewer: What was your primary objective at that point? Participant: Get through the queue, keep the shift moving, and not waste the incident response lead's time on something that turns out to be benign. We only had about three hours left in the shift, and I wanted whatever I handed off to be solid, not a guess. Interviewer: Take me through what happened next, chronologically. Participant: So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet. About forty minutes later, a follow-up alert showed an outbound connection from that same host to an IP I didn't recognize. That's when I actually opened the case properly. I found a registry-key artifact that matched something documented in a GreyFalcon campaign from about six months back — I remembered writing that report myself, so it stuck with me. Around the same time, internal telemetry showed an attempted connection to the HR benefits database from that host, which was strange, but I moved forward with attribution anyway. Then I pulled a vendor bulletin that had just come in — the vendor portal access was closing soon, so I read it quickly. It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that. Near the end of shift, I had to write up a containment recommendation for the IR lead, and I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of 'possibly' and 'unclear.' Interviewer: Let's slow down and go through each of those decisions one at a time. First one — the initial Low-severity alert. What cues were you weighing right then? Participant: Mainly the auto-triage score and my own memory of that server generating false alarms before. No unusual business disruption was reported either, which reinforced it felt routine. Interviewer: What made you decide to defer the manual log pull rather than doing it right away? Participant: Time, mostly. The score was Low, I had precedent that Low from that host usually meant nothing, and pulling raw logs is a real time cost. Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me. It felt like a reasonable use of triage priority rather than checking every single alert by hand. Interviewer: Did you consider escalating to the IR lead first instead? Participant: I thought about it, but that seemed like overkill for a Low score with no other signal at that point. In hindsight, I probably could've spent the fifteen minutes given how the next forty minutes went, but at the time it didn't seem to justify interrupting anyone. Interviewer: Understood. Let's move to the attribution decision after the outbound connection appeared. What was the basis for assigning GreyFalcon? Participant: The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in. Interviewer: You mentioned the C2 domain's registration pattern looked different from GreyFalcon's usual infrastructure. How did that factor in? Participant: It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then. Interviewer: And the HR database access attempt — GreyFalcon has typically gone after trading or financial data in your prior tracking. How did you read that mismatch? Participant: My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly. So it didn't strike me as inconsistent with the group, more like an opportunistic pivot they'd make if they were being efficient about it. Interviewer: Did you weigh that explanation against the possibility that it wasn't GreyFalcon at all? Participant: Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself. Interviewer: Let's talk about the hunt scope decision, once the vendor bulletin came in. Walk me through how you decided what to include. Participant: The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up. It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources. There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary. Interviewer: The bulletin listed two file-hash IOCs last — how much did those factor into the scope? Participant: Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely. Interviewer: Was there consideration of scoping broadly across all five IOCs regardless of order? Participant: There was, briefly — business owners wanted it narrow anyway to avoid downtime on trading-adjacent systems, so narrow scope aligned with what they wanted too. That made it easier to just go with the scope that already made sense to me. Interviewer: Last decision point — the containment recommendation. You mentioned leaning on the vendor bulletin over a colleague's notes. What drove that? Participant: Time pressure, for one — I needed something to hand the IR lead within the hour. But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — 'possibly,' 'unclear if,' that kind of thing. The vendor version gave me something concrete to act on. Interviewer: Did you compare the actual evidence underlying each source, separate from how they were written? Participant: Not directly side by side, no. I read the vendor one, it felt solid, and I went with it. Interviewer: How confident were you overall in the final recommendation you handed off? Participant: Reasonably confident, maybe seven out of ten. Enough uncertainty that I flagged it as needing follow-up validation next shift, but I felt the containment steps were defensible given what I had. Interviewer: Looking back across the shift, if you'd pulled the raw logs immediately in phase one instead of deferring, how do you think things would've unfolded differently? Participant: I might have caught the odd outbound connection sooner, maybe before the vendor window closed, which could've changed how much I leaned on that bulletin later. Hard to say for certain. Interviewer: If the vendor bulletin had listed its IOCs in reverse order, hash-based ones first, do you think your scoping would have changed? Participant: Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope. Interviewer: Is there a point in this sequence where you'd want a second analyst's independent read before proceeding? Participant: Probably the attribution step. That's where I moved fastest from one piece of strong evidence to a full working theory, and a second set of eyes might have pushed back on the infrastructure mismatch or the HR access pattern before I built the rest of the shift around it. Interviewer: That's helpful, thank you. I think that covers what I need.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.90s · gen 255.04s · total 261.7s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0273 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0266 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0257 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0251 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0235 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0226 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
7. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0206 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0193 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0192 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
13. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0188 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_
14. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0187 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0184 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
16. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0184 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
17. **Lyell Automation bias and verification complexity.pdf** — 0.0183 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
19. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0179 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
21. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0171 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0169 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0169 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
25. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
26. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0166 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
27. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0165 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
28. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0161 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
30. **Hallihan_etal_DTM_12.pdf** — 0.0158 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
32. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0157 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
33. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
34. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0155 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
36. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0154 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
37. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0154 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
39. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0152 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
40. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0151 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
41. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0149 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
44. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0148 (rrf) — _# across domains and different parts of the search process. to help inform their opinions \[ 45 _
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
47. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0146 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
48. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0145 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
50. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0141 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single-interview analysis of the participant's retrospective description of a SOC shift, with retrieved corpus passages used where they support an identified mechanism."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "automation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "fluency bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation bias",
      "alternative_labels": [
        "automation-induced complacency",
        "complacency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Overreliance on automated decision-support output, leading to reduced independent verification or information sampling.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial triage of low-severity EDR alert cluster",
      "decision_point_description": "Deciding whether to pull raw logs immediately or defer manual inspection after the Low auto-triage score",
      "affected_reasoning_operation": "Triage prioritization and verification-seeking",
      "bias_specific_mechanism": "The Low automated triage score was treated as authoritative, reducing independent verification; an unfamiliar parent process listed in the alert summary was not inspected because the automation label dominated the cue interpretation.",
      "manifestation_in_interview": "The participant deferred raw log pulls and did not examine the unfamiliar parent process because the Low label was treated as deciding the matter.",
      "effect_on_reasoning_or_decision": "Manual log inspection was deferred for roughly 40 minutes, leaving a potentially relevant cue unexamined and keeping the alert at low priority.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The auto-triage score came back Low. Historically, that queue throws a lot of low-severity noise, especially from that server, so my first instinct was it's probably another false positive.",
          "evidence_explanation": "Shows the automated score and prior noise as initial inputs, setting up reliance on the triage label."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me.",
          "evidence_explanation": "Explicitly demonstrates that the automation score suppressed inspection of a discrepant cue, which is the core automation-overreliance mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant framed the deferral as reasonable triage prioritization, and there was genuine time pressure plus a relevant history of false positives from the same server. These are non-bias pressures, but the quote shows the automation label specifically displaced independent cue inspection.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved source supports the mechanism of automation-induced complacency as incomplete verification of automation output.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Approximately 43% of operators did not detect a wrong diagnosis of the aid when it occurred for the first time. Analyses of information-sampling behavior revealed that half of the participants made this commission error because of a clear complacency effect, as reflected in an incomplete sampling of information needed for automation verification.",
          "mechanism_supported_by_source": "Automation-induced complacency leads to incomplete sampling or verification of automated aid output.",
          "relevance_to_this_occurrence": "The participant deferred manual log inspection and did not examine an unfamiliar parent process after a Low automation score, consistent with reduced verification of automation output."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "hypothesis-confirming bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Selective gathering or weighting of evidence that supports a favored hypothesis while underweighting or not pursuing disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Attribution of outbound connection and registry-key artifact to GreyFalcon campaign",
      "decision_point_description": "Deciding whether to adopt GreyFalcon attribution and whether to revise confidence after infrastructure and target mismatches",
      "affected_reasoning_operation": "Hypothesis evaluation and causal attribution",
      "bias_specific_mechanism": "The participant anchored on a confirmatory registry-key artifact, then noticed mismatches in C2 infrastructure and target behavior but did not treat them as reasons to question the GreyFalcon hypothesis; instead he generated a plausible motive-preserving explanation.",
      "manifestation_in_interview": "The participant reports that the infrastructure mismatch stood out but the confirmatory artifact felt stronger, and that the HR database access did not prompt him to question attribution because it fit a plausible opportunistic-pivot story.",
      "effect_on_reasoning_or_decision": "The GreyFalcon attribution was maintained prematurely and became the frame for later hunt scoping and containment recommendations.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I found a registry-key artifact that matched something documented in a GreyFalcon campaign from about six months back — I remembered writing that report myself, so it stuck with me. Around the same time, internal telemetry showed an attempted connection to the HR benefits database from that host, which was strange, but I moved forward with attribution anyway.",
          "evidence_explanation": "Shows movement from a confirmatory match to attribution despite noticing a strange feature, with no reported effort to resolve the mismatch before attribution."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then.",
          "evidence_explanation": "Explicitly demonstrates underweighting of disconfirming infrastructure evidence in favor of the hypothesis-consistent registry-key signal."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself.",
          "evidence_explanation": "Shows that an alternative explanation for the HR access mismatch was not seriously weighed against the favored GreyFalcon attribution."
        }
      ],
      "correction_or_counterevidence": "The registry-key artifact was a concrete prior IOP from the participant's own experience and could reasonably support attribution; however, two subsequent mismatches were explicitly noticed and not allowed to reduce confidence, which is the bias-specific pattern.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved source documents confirmation bias in intelligence analysis as selective selection and prioritization of hypothesis-supportive evidence over conflicting evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": "Cook & Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at assessment but a strong and pervasive confirmation bias for selecting and prioritizing evidence... Because the overwhelming majority of selected evidence was supportive, the remaining pool of 19% conflicting evidence was insufficient to allow eliminate bias.",
          "mechanism_supported_by_source": "Confirmation bias leads analysts to select and prioritize supportive evidence while giving insufficient weight to conflicting evidence.",
          "relevance_to_this_occurrence": "The participant prioritized the registry-key match as the strongest evidence and underweighted mismatched C2 infrastructure and HR target data, consistent with this evidence-selection and prioritization mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "order effect anchoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for an initial piece of information to serve as an anchor and for subsequent adjustment away from that anchor to be insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hunt scoping after vendor bulletin review",
      "decision_point_description": "Deciding which IOCs to prioritize when constructing the hunt scope",
      "affected_reasoning_operation": "Scope construction and IOC prioritization",
      "bias_specific_mechanism": "The first IOC listed in the vendor bulletin served as an anchor, and the participant built the scope around it; later file-hash IOCs were underweighted because of their list position despite being technically specific.",
      "manifestation_in_interview": "The participant explicitly says he scoped around the first IOC and that the file-hash IOCs received less attention because they were at the bottom of the list; he also states the order could have reversed the anchor.",
      "effect_on_reasoning_or_decision": "The hunt scope was built disproportionately around the first-listed C2 protocol signature rather than a balanced assessment across all five IOCs, potentially underweighting lower-false-positive hash-based indicators.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up.",
          "evidence_explanation": "Shows that the first-listed IOC became the central scope anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely.",
          "evidence_explanation": "Explicitly demonstrates order-based anchoring and the participant's own counterfactual that reversing the order would likely have changed the scope."
        }
      ],
      "correction_or_counterevidence": "Business owners wanted a narrow scope to avoid downtime, which may have also favored a narrower IOC set; however, the participant's explicit order-based counterfactual strongly supports an anchoring mechanism.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved source supports anchoring-and-adjustment as an insufficient-adjustment phenomenon under time constraints.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoring-and-adjustment. ... participants’ likelihood of sufficiently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoring-and-adjustment heuristic is a resource-rational tradeoff between time and accuracy.",
          "mechanism_supported_by_source": "Anchoring-and-adjustment: an initial value or cue anchors subsequent judgment, with insufficient adjustment away from it.",
          "relevance_to_this_occurrence": "The participant anchored on the first IOC and adjusted insufficiently to later IOCs, with time pressure also present."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "hypothesis-confirming bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Selective gathering or weighting of evidence that supports a favored hypothesis while underweighting or not pursuing disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hunt scope validation check decision",
      "decision_point_description": "Whether to run a comparable-host check that could disconfirm GreyFalcon attribution versus relying on the existing coherent story",
      "affected_reasoning_operation": "Hypothesis testing and evidence-seeking",
      "bias_specific_mechanism": "The participant considered a diagnostic check that could distinguish GreyFalcon from alternative explanations, but declined because the current GreyFalcon story already appeared sufficient; this favored hypothesis-consistent sufficiency over disconfirmation-seeking.",
      "manifestation_in_interview": "The participant reports that the check crossed his mind, but the GreyFalcon story accounted for what he was seeing well enough that running it did not feel necessary.",
      "effect_on_reasoning_or_decision": "Alternative explanations such as a misconfigured admin tool or commodity malware reusing the protocol were not tested before resources were committed to a GreyFalcon-scoped hunt.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary.",
          "evidence_explanation": "Explicitly shows a disconfirming test was considered but omitted because the current hypothesis already seemed to explain the observations."
        }
      ],
      "correction_or_counterevidence": "The participant did consider the check, and time/resource constraints may have contributed to omitting it; however, the stated reason was that the current story already accounted for the observations, which is the bias-specific sufficiency judgment.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The same intelligence-analysis confirmation-bias source supports this pattern of not adequately pursuing conflicting evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": "Cook & Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at assessment but a strong and pervasive confirmation bias for selecting and prioritizing evidence... Because the overwhelming majority of selected evidence was supportive, the remaining pool of 19% conflicting evidence was insufficient to allow eliminate bias.",
          "mechanism_supported_by_source": "Confirmation bias leads analysts to select and prioritize hypothesis-supportive evidence while giving insufficient weight to conflicting evidence and tests.",
          "relevance_to_this_occurrence": "The participant avoided a diagnostic test that could have generated conflicting evidence, favoring the hypothesis-consistent GreyFalcon story."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "fluency bias",
      "alternative_labels": [
        "processing fluency bias",
        "presentation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge information as more credible or persuasive when it is presented fluently, clearly, and with confident language, rather than based on the strength of the underlying evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment recommendation source selection between vendor bulletin and colleague notes",
      "decision_point_description": "Deciding which threat-intelligence source to rely on for the IR containment recommendation",
      "affected_reasoning_operation": "Source evaluation and recommendation formation",
      "bias_specific_mechanism": "The participant judged the vendor bulletin as more authoritative because it was clean, well formatted, and confidently worded, while discounting the colleague's hedged notes, without directly comparing the underlying evidence in each source.",
      "manifestation_in_interview": "The participant says the vendor bulletin 'read as more authoritative' and gave something concrete to act on, while the colleague's notes were accurate but full of hedges; he confirms he did not compare the actual evidence side by side.",
      "effect_on_reasoning_or_decision": "The containment recommendation was heavily based on the vendor bulletin's presentation and linguistic confidence rather than a direct evidence comparison, potentially over-weighting one source.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — 'possibly,' 'unclear if,' that kind of thing. The vendor version gave me something concrete to act on.",
          "evidence_explanation": "Shows the source was judged on formatting, presentation fluency, and linguistic confidence rather than on the evidence itself."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly side by side, no. I read the vendor one, it felt solid, and I went with it.",
          "evidence_explanation": "Confirms that no direct underlying-evidence comparison was made before source preference."
        }
      ],
      "correction_or_counterevidence": "Time pressure and the legitimate possibility that a vendor bulletin is authoritative are non-bias explanations; however, the stated reasons for choosing the source were formatting and confident language, making the mechanism plausible but not definitive.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage addressed this specific source-format or processing-fluency mechanism; the label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": [
        "ease-of-recall heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial interpretation of Low-severity EDR alert cluster",
      "supporting_interview_quote": "I'd seen that exact pattern twice in prior shifts and both times it was nothing.",
      "plausible_mechanism": "Ease or vividness of recalling prior false-positive alerts could inflate the subjective probability that the current alert was also false.",
      "why_not_identified": "The participant may have been using relevant, specific prior experience as a legitimate base-rate cue rather than showing a distinct availability-specific over-weighting; the evidence is too thin to identify separately from automation bias and ordinary triage judgment."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a retrospective self-report, so recall and self-presentation may affect the description of in-the-moment reasoning.",
    "Some retrieved corpus passages were fragmentary and not from the same operational domain, so mechanisms were mapped conservatively.",
    "Fluency bias was identified from general cognitive-science knowledge because no retrieved passage supported that specific mechanism.",
    "Time pressure and organizational scope constraints appear alongside the bias mechanisms and serve as partial non-bias explanations."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and I'll ask you to walk me through a specific shift in detail. You can skip anything you're not comfortable sharing. Can you tell me your role and how long you've been doing it? Participant: Sure. I'm a threat intelligence analyst on the SOC team, been in this seat about four years, mostly financial services environments. My job during shift is triage, attribution, and hunt scoping when something looks like it's more than commodity noise. Interviewer: Good. Let's start broad. Can you walk me through what this shift looked like when the alert cluster first appeared? Participant: It was maybe two hours into an overnight shift. EDR kicked out a cluster of alerts on a trading-support server — not the trading engine itself, but a box that feeds reporting data to it. The auto-triage score came back Low. Historically, that queue throws a lot of low-severity noise, especially from that server, so my first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing. Interviewer: What was your primary objective at that point? Participant: Get through the queue, keep the shift moving, and not waste the incident response lead's time on something that turns out to be benign. We only had about three hours left in the shift, and I wanted whatever I handed off to be solid, not a guess. Interviewer: Take me through what happened next, chronologically. Participant: So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet. About forty minutes later, a follow-up alert showed an outbound connection from that same host to an IP I didn't recognize. That's when I actually opened the case properly. I found a registry-key artifact that matched something documented in a GreyFalcon campaign from about six months back — I remembered writing that report myself, so it stuck with me. Around the same time, internal telemetry showed an attempted connection to the HR benefits database from that host, which was strange, but I moved forward with attribution anyway. Then I pulled a vendor bulletin that had just come in — the vendor portal access was closing soon, so I read it quickly. It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that. Near the end of shift, I had to write up a containment recommendation for the IR lead, and I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of 'possibly' and 'unclear.' Interviewer: Let's slow down and go through each of those decisions one at a time. First one — the initial Low-severity alert. What cues were you weighing right then? Participant: Mainly the auto-triage score and my own memory of that server generating false alarms before. No unusual business disruption was reported either, which reinforced it felt routine. Interviewer: What made you decide to defer the manual log pull rather than doing it right away? Participant: Time, mostly. The score was Low, I had precedent that Low from that host usually meant nothing, and pulling raw logs is a real time cost. Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me. It felt like a reasonable use of triage priority rather than checking every single alert by hand. Interviewer: Did you consider escalating to the IR lead first instead? Participant: I thought about it, but that seemed like overkill for a Low score with no other signal at that point. In hindsight, I probably could've spent the fifteen minutes given how the next forty minutes went, but at the time it didn't seem to justify interrupting anyone. Interviewer: Understood. Let's move to the attribution decision after the outbound connection appeared. What was the basis for assigning GreyFalcon? Participant: The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in. Interviewer: You mentioned the C2 domain's registration pattern looked different from GreyFalcon's usual infrastructure. How did that factor in? Participant: It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then. Interviewer: And the HR database access attempt — GreyFalcon has typically gone after trading or financial data in your prior tracking. How did you read that mismatch? Participant: My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly. So it didn't strike me as inconsistent with the group, more like an opportunistic pivot they'd make if they were being efficient about it. Interviewer: Did you weigh that explanation against the possibility that it wasn't GreyFalcon at all? Participant: Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself. Interviewer: Let's talk about the hunt scope decision, once the vendor bulletin came in. Walk me through how you decided what to include. Participant: The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up. It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources. There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary. Interviewer: The bulletin listed two file-hash IOCs last — how much did those factor into the scope? Participant: Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely. Interviewer: Was there consideration of scoping broadly across all five IOCs regardless of order? Participant: There was, briefly — business owners wanted it narrow anyway to avoid downtime on trading-adjacent systems, so narrow scope aligned with what they wanted too. That made it easier to just go with the scope that already made sense to me. Interviewer: Last decision point — the containment recommendation. You mentioned leaning on the vendor bulletin over a colleague's notes. What drove that? Participant: Time pressure, for one — I needed something to hand the IR lead within the hour. But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — 'possibly,' 'unclear if,' that kind of thing. The vendor version gave me something concrete to act on. Interviewer: Did you compare the actual evidence underlying each source, separate from how they were written? Participant: Not directly side by side, no. I read the vendor one, it felt solid, and I went with it. Interviewer: How confident were you overall in the final recommendation you handed off? Participant: Reasonably confident, maybe seven out of ten. Enough uncertainty that I flagged it as needing follow-up validation next shift, but I felt the containment steps were defensible given what I had. Interviewer: Looking back across the shift, if you'd pulled the raw logs immediately in phase one instead of deferring, how do you think things would've unfolded differently? Participant: I might have caught the odd outbound connection sooner, maybe before the vendor window closed, which could've changed how much I leaned on that bulletin later. Hard to say for certain. Interviewer: If the vendor bulletin had listed its IOCs in reverse order, hash-based ones first, do you think your scoping would have changed? Participant: Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope. Interviewer: Is there a point in this sequence where you'd want a second analyst's independent read before proceeding? Participant: Probably the attribution step. That's where I moved fastest from one piece of strong evidence to a full working theory, and a second set of eyes might have pushed back on the infrastructure mismatch or the HR access pattern before I built the rest of the shift around it. Interviewer: That's helpful, thank you. I think that covers what I need.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.03s · gen 239.23s · total 245.0s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0273 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0266 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0257 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0251 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0235 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0226 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
7. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0206 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0193 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0192 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
13. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0188 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_
14. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0187 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0184 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
16. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0184 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
17. **Lyell Automation bias and verification complexity.pdf** — 0.0183 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
19. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0179 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
21. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0171 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0169 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0169 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
25. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
26. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0166 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
27. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0165 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
28. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0161 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
30. **Hallihan_etal_DTM_12.pdf** — 0.0158 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
32. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0157 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
33. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
34. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0155 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
36. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0154 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
37. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0154 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
39. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0152 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
40. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0151 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
41. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0149 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
44. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0148 (rrf) — _# across domains and different parts of the search process. to help inform their opinions \[ 45 _
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
47. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0146 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
48. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0145 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
50. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0141 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the interview for affirmative transcript evidence of bias-specific cognitive mechanisms affecting reasoning or decisions. Retrospective self-reports were used only where they demonstrated a mechanism operating at the time of the described decisions."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "Authority bias",
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
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring and adjustment",
        "Insufficient adjustment",
        "Automation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information and to adjust insufficiently away from that anchor when new or contradictory information is available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial Low-severity alert triage",
      "decision_point_description": "Deciding whether to immediately pull raw logs or defer manual inspection and continue with the queue.",
      "affected_reasoning_operation": "Triage prioritization and alert interpretation",
      "bias_specific_mechanism": "The automated Low severity score and two prior false-positive episodes anchored the participant's initial judgment that the alert was probably another false positive; when an unfamiliar parent process appeared in the alert summary, the participant did not sufficiently adjust away from the Low anchor and therefore did not inspect it.",
      "manifestation_in_interview": "The participant stated that the Low score 'kind of did the deciding' and that an unfamiliar parent process did not receive closer inspection because the Low label was 'sitting on top of it.'",
      "effect_on_reasoning_or_decision": "The participant deferred manual log review and moved to other queue items, delaying discovery of the outbound connection by approximately forty minutes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It was maybe two hours into an overnight shift. EDR kicked out a cluster of alerts on a trading-support server — not the trading engine itself, but a box that feeds reporting data to it. The auto-triage score came back Low. Historically, that queue throws a lot of low-severity noise, especially from that server, so my first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing.",
          "evidence_explanation": "Shows the initial Low score and prior false-positive history supplied the anchor for interpreting the alert as routine."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet.",
          "evidence_explanation": "Demonstrates that the anchor affected the immediate triage action: deferral of manual inspection."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me.",
          "evidence_explanation": "Directly states that the Low score inhibited adjustment to a potentially contradictory cue, which is the anchoring-and-adjustment mechanism."
        }
      ],
      "correction_or_counterevidence": "At the time, the participant framed the deferral as a reasonable use of triage priority, time constraints, and prior base rates; in hindsight he said he probably could have spent the fifteen minutes, but no contemporaneous correction occurred.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Rastogi et al. (2022) describes anchoring-and-adjustment in AI-assisted decisions, including insufficient adjustment away from an initial AI-provided value.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports the anchoring-and-adjustment heuristic and insufficient adjustment away from an initial automated prediction.",
          "relevance_to_this_occurrence": "The participant encountered an automated triage score and showed insufficient adjustment from that initial Low anchor, paralleling the source's finding that anchoring on automated predictions can persist under time constraints."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Hypothesis confirmation",
        "Selective information processing",
        "Tunnel vision"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's existing beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "GreyFalcon attribution",
      "decision_point_description": "Assigning the observed activity to GreyFalcon and deciding whether to revise that attribution when encountering infrastructure and target mismatches.",
      "affected_reasoning_operation": "Hypothesis generation, evidence integration, and attribution",
      "bias_specific_mechanism": "After the registry-key artifact activated the GreyFalcon hypothesis, the participant interpreted subsequent ambiguous or mismatching cues as consistent with GreyFalcon and did not test alternative explanations such as commodity malware or non-GreyFalcon actors.",
      "manifestation_in_interview": "The participant noted a registrar/domain age mismatch and an unusual HR database access attempt but continued attribution; he described the GreyFalcon story as accounting for everything and therefore did not run a simple comparative check.",
      "effect_on_reasoning_or_decision": "Reinforced attribution to GreyFalcon and reduced search for disconfirming evidence, affecting subsequent hunt scoping and containment recommendations.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in.",
          "evidence_explanation": "Shows initial hypothesis activation and the subjective strength given to the matching artifact."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then.",
          "evidence_explanation": "Demonstrates disregarding disconfirming infrastructure evidence due to the strength of the initial confirmatory cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly. So it didn't strike me as inconsistent with the group, more like an opportunistic pivot they'd make if they were being efficient about it.",
          "evidence_explanation": "Shows reinterpretation of an unusual target-access pattern as consistent with the GreyFalcon hypothesis rather than as disconfirming evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself.",
          "evidence_explanation": "Direct admission that the mismatching HR access pattern was not weighed as a reason to question the attribution."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary.",
          "evidence_explanation": "Shows a disconfirming check was available but omitted because the existing GreyFalcon narrative already felt sufficient."
        }
      ],
      "correction_or_counterevidence": "The participant later identified the attribution step as the point where a second analyst's independent read would have helped, and acknowledged moving rapidly from one piece of strong evidence to a full working theory; however, no contemporaneous correction occurred.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Cook and Smallman (2008) documents confirmation bias in intelligence-analysis evidence selection and prioritization.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human factors of the confirmation bias in intelligence analysis: decision support from graphical evidence",
          "authors": "Cook and Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at assessment but a strong and pervasive confirmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "The source supports the presence of confirmation bias in selecting and prioritizing evidence in intelligence analysis.",
          "relevance_to_this_occurrence": "The participant selected and prioritized the registry-key match as strongly confirmatory while underweighting inconsistent infrastructure and target-access evidence, consistent with the source's confirmation-bias finding."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "Order effect",
        "Primacy effect",
        "Serial-position effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information and to adjust insufficiently away from that anchor when subsequent information is available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hunt scope construction from vendor bulletin",
      "decision_point_description": "Deciding which IOCs to prioritize when building a hunt scope from a five-item vendor bulletin.",
      "affected_reasoning_operation": "Hunt scope selection and evidence weighting",
      "bias_specific_mechanism": "The first IOC in the bulletin, a rare C2 protocol signature, served as an anchor; later IOCs, including two file-hash IOCs that may have been more specific or lower false-positive risk, were underweighted because the initial anchor had already structured the scope.",
      "manifestation_in_interview": "The participant built the hunt scope mostly around the first-listed IOC and admitted the file-hash IOCs factored less because they came at the bottom; he said reversing the order would likely have changed the anchor and the scope.",
      "effect_on_reasoning_or_decision": "Produced a narrower hunt scope centered on the first IOC, reducing consideration of alternative causes and potentially affecting resource allocation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that.",
          "evidence_explanation": "Shows the first-listed IOC was used as the primary basis for the hunt scope."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up. It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources.",
          "evidence_explanation": "Demonstrates that the first IOC and its coherence with the existing belief structured the hunt resource allocation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely.",
          "evidence_explanation": "Explicitly attributes underweighting to the serial position of the file-hash IOCs and acknowledges the influence of the initial anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope.",
          "evidence_explanation": "Directly supports the anchoring mechanism by indicating that different initial information would likely have produced a different scope."
        }
      ],
      "correction_or_counterevidence": "The participant briefly considered scoping across all five IOCs, but business owners' preference for a narrow scope aligned with the already anchored scope; the later acknowledgment that reversed IOC order would likely change the scope is retrospective rather than a contemporaneous correction.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Rastogi et al. (2022) describes anchoring-and-adjustment in decision tasks involving AI-generated information.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports the anchoring-and-adjustment heuristic and insufficient adjustment away from an initial anchor.",
          "relevance_to_this_occurrence": "The participant anchored on the first IOC in the vendor bulletin and insufficiently adjusted the scope based on later, potentially higher-value IOCs, consistent with the anchoring-and-adjustment mechanism described in the source."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Authority bias",
      "alternative_labels": [
        "Source credibility bias",
        "Authority heuristic",
        "Presentation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to attribute greater accuracy or credibility to information based on the perceived authority, confidence, or formatting of its source rather than on the quality of the underlying evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment recommendation source selection",
      "decision_point_description": "Choosing whether to base the containment recommendation primarily on the vendor bulletin or on a colleague's notes.",
      "affected_reasoning_operation": "Source reliability assessment and recommendation formulation",
      "bias_specific_mechanism": "The participant inferred evidentiary solidity from the vendor bulletin's clean formatting and confident language while discounting the more hedged colleague's notes, without directly comparing the underlying evidence or reliability of each source.",
      "manifestation_in_interview": "The participant said the vendor bulletin 'just read as more authoritative' because it was clean, formatted well, and confident; he also stated he did not compare the evidence underlying the two sources side by side.",
      "effect_on_reasoning_or_decision": "The containment recommendation was based primarily on the vendor bulletin, reducing the influence of potentially accurate but hedged analyst notes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Near the end of shift, I had to write up a containment recommendation for the IR lead, and I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of 'possibly' and 'unclear.'",
          "evidence_explanation": "Shows that the participant favored the vendor source partly because of its apparent clarity and specificity relative to the hedged notes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — 'possibly,' 'unclear if,' that kind of thing. The vendor version gave me something concrete to act on.",
          "evidence_explanation": "Explicitly identifies source authority as inferred from presentation and confident language rather than from an evidence comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly side by side, no. I read the vendor one, it felt solid, and I went with it.",
          "evidence_explanation": "Confirms the participant did not compare the actual underlying evidence before selecting the source."
        }
      ],
      "correction_or_counterevidence": "The participant flagged the final recommendation for follow-up validation next shift and retained some uncertainty, but this occurred after the source-selection decision and did not reduce the influence of source presentation at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable for authority bias. This widely established label is used from general cognitive-science knowledge, not from retrieval.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support is sparse and does not include all identified bias labels; authority bias is assigned from general cognitive-science knowledge rather than retrieval.",
    "The interview is a retrospective self-report, so the analysis captures reported reasoning rather than objectively observed behavior.",
    "The retrieved passages contain OCR noise and incomplete formatting, limiting the precision of quotations from scientific sources."
  ]
}

