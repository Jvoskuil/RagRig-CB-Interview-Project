# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our incident-response learning archive, not a performance review — you can skip anything you're not comfortable discussing. Can you start by stating your role and how long you've been on the Tier 2 triage rotation? Participant: Sure. I'm a Tier 2 SOC analyst, been doing log and alert triage for about two and a half years, most of that on the overnight rotation. This shift was a fairly typical Tuesday-into-Wednesday, except we had a scheduled vulnerability scan running against the 10.14.0.0/16 range. Interviewer: Good, let's go through what happened. Walk me through what you saw when you first opened the alert queue that night. Participant: I logged into the SIEM around 1 a.m. and the queue already had close to 300 new alerts in about twenty minutes, which is a lot even for us. Handoff notes from the day shift flagged that vuln management had an authenticated scan scheduled starting midnight, so I expected noise. When I sorted the queue, something like 92% of everything was tagged as coming from the scan subnet — port scans, auth attempts, the usual scanner fingerprint. That matched what I expected to see. Interviewer: What was your primary goal in those first ten minutes? Participant: Get through the noise fast so I wouldn't blow the 45-minute SLA on anything that actually mattered. With that volume, you can't eyeball every single alert individually — you triage by pattern. Interviewer: Okay, let's reconstruct the rest of the shift chronologically, then we'll go back and dig into specific decisions. What came after that initial queue review? Participant: I ran our saved scan-window filter to bulk-close the low-severity scan-tagged alerts, then almost immediately got pulled into a phishing cluster — a bunch of similar-looking emails landing in different inboxes. I spent maybe twenty minutes on that while the shift lead was pinging me for status. Then around 2:40, EDR kicked out an anomaly on a finance workstation, FIN-WK-114, with a process making periodic outbound connections. I looked at that, made a call, and moved on. About forty minutes later, a threat intel feed update came back and changed the picture on that same host, so I escalated to IR. Interviewer: Let's slow down on the first decision — closing that initial batch. What information did you actually have in front of you at the moment you applied the filter? Participant: The queue view, sorted by source subnet and severity. Almost everything was scan-subnet, low severity. There was one alert from FIN-WK-114 — a DNS query to a domain I didn't recognize — but it was sitting at low severity too, so visually it didn't distinguish itself from the rest of the batch. Interviewer: What other options did you consider before bulk-closing? Participant: I could have spot-checked a random sample of the low-severity ones outside the scan subnet before closing, or set a rule to pull out anything touching non-IT departments like finance for individual review. Honestly, with SLA pressure and that volume, the batch filter felt like the efficient move. I ran it across the whole set. Interviewer: And the FIN-WK-114 alert — what happened to it specifically? Participant: It went out with the rest of the batch. I didn't clock at the time that it wasn't actually part of the scan subnet — I was scanning for the scan pattern, saw a low-severity tag, and it got swept up. I didn't isolate it as a finance host outside 10.14.0.0/16 until I came back to it hours later. Interviewer: What would have needed to be different for you to catch that at the time? Participant: Probably if the queue view had color-coded by subnet instead of just severity, or if I'd run the spot-check option instead of the full batch close. In hindsight it was sitting right there. Interviewer: Let's move to the phishing cluster. What made you confident that was contained? Participant: I've got a suppression rule I wrote and deployed last week specifically to cut down on repeat-sender noise. When the phishing cluster came in, that rule auto-tagged about 40 duplicate alerts as handled almost immediately. Given how fast the visible queue cleared, I told the shift lead it looked contained. Interviewer: Did you verify that against anything else — inbox delivery logs, a manual sample? Participant: Not at that point, no. The rule's been solid since I built it, and seeing the count drop that fast felt like confirmation it was doing its job on this campaign too. I flagged it as contained in the ticket. Interviewer: Was there anything in the queue at that time that didn't fit that picture? Participant: There was one variant with a slightly different sender domain that the rule wouldn't have matched — I didn't clock that until later. At the time I was reading the drop in volume as the rule working. Interviewer: Understood. Now the EDR anomaly on FIN-WK-114 — what led you to the backup-agent explanation? Participant: The connection pattern — periodic, roughly every 55 seconds — looked a lot like something we'd seen twice in the previous two shifts, both traced back to a misconfigured backup agent on other hosts. That was fresh in my mind since I'd closed both of those tickets myself within the last week. Interviewer: Did the current alert have a direct signature match to that backup agent? Participant: No, it didn't — there was no IOC match, no clean fingerprint tying it to the agent. I noted it as 'likely backup-agent artifact, monitor only' based mostly on the interval pattern resembling those recent cases, and moved on to the phishing follow-up. Interviewer: Was pulling the process tree or checking the destination IP against threat intel an option at that point? Participant: Yeah, it was, and normally I'd lean that way if I weren't juggling two things. Since the pattern matched what I'd just dealt with twice, it felt like a safe bet to downgrade it and keep an eye on it rather than treat it as new. Interviewer: What told you it was 'safe' specifically — the interval, or something else? Participant: Mostly the interval and the fact that backup-agent issues had been the dominant explanation for anything beacon-like lately. If I'd seen this same alert two months ago, before those two tickets, I probably would've pulled the process tree first. Interviewer: Let's get to the fourth point — the escalation. What changed? Participant: About forty minutes later, threat intel updated and flagged that destination IP as a known C2 rendezvous point, which directly contradicted the backup-agent call. By then the SLA on that alert had already lapsed by twelve minutes, and my shift lead was tied up on another incident call for the next twenty. Interviewer: What were your options at that point? Participant: Escalate straight to IR with what I had, wait for the shift lead to be free for sign-off, or go back and rebuild the evidence chain from the earlier alerts first. I chose to escalate immediately — the SLA was already blown and waiting felt riskier than moving fast with an incomplete write-up. Interviewer: How did that play out? Participant: IR picked it up and confirmed lateral movement attempts from FIN-WK-114, consistent with that original DNS alert from hours earlier — the one that got closed in the batch. Interviewer: Looking back across the night, at what point were you least certain about your read of the situation? Participant: Probably the beacon classification. I remember having a flicker of doubt — no direct IOC match nagged at me a little — but the recent pattern felt like a strong enough anchor to act on given the time crunch. Interviewer: A couple of hypotheticals to close. If the scan window hadn't been running that night, do you think you'd have handled the FIN-WK-114 alert differently? Participant: Almost certainly. Without 300 scan alerts flooding the queue, that single DNS alert would have stood out on its own and I'd have looked at it individually. Interviewer: If you hadn't been the one who wrote the suppression rule, would you have checked phishing containment differently? Participant: Maybe — I might have been more inclined to ask someone else to verify it rather than trust the count dropping. Interviewer: And if the last two shifts hadn't involved backup-agent false positives, how might you have approached the beacon differently? Participant: I think I'd have gone straight to the process tree and IP lookup instead of pattern-matching against recent history. That comparison was really the whole reason I felt comfortable downgrading it. Interviewer: Last one — what single process change would have caught this earlier? Participant: Separating subnet visibility from severity in the queue view, so a scan-window filter can't accidentally sweep up a host that was never actually part of the scan. That's the gap that mattered most here. Interviewer: That's really helpful, thank you for walking through it in this much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.15s · gen 220.93s · total 227.0s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0286 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0250 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0241 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0239 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0238 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0229 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0224 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0209 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0180 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0177 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0170 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
13. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0168 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0166 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
16. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0163 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
17. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0162 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
19. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD tive biases or risktaking behavior and triage accuracy varied according 2.1._
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0161 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0161 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
22. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0160 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
23. **Lyell Automation bias and verification complexity.pdf** — 0.0159 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
25. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0157 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
26. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0156 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
27. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
32. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0149 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. Chan, U. Dulleck et al. 2.5. Statistical analy_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
36. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0144 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
37. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
38. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0141 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
39. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0141 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
43. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
45. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0138 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. C han, U. Dulleck et al. In the triage decisio_
46. **Lyell Automation bias and verification complexity.pdf** — 0.0137 (rrf) — _## INTRODUCTION | | • Monitoring tasks require the user to monitor for a change in | | parative _
47. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0136 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
48. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0136 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
49. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0135 (rrf) — _# i cdecision allegiance . As we move to the bottom of the taxonomy, we focus on the more fundam_
50. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0135 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Blind, mechanism-first diagnostic review of a single SOC analyst debrief. Only affirmative transcript-grounded bias mechanisms were classified; workload constraints, retrospective reports, or ordinary uncertainty were excluded unless a distinct cognitive distortion mechanism was evident."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "expectation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "expectation bias",
      "alternative_labels": ["expectancy bias", "confirmation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Expectation bias is the tendency for strong prior expectations to shape perception and classification, causing decision-makers to overlook or discount information that conflicts with the expected pattern.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial SIEM queue triage during scheduled vulnerability scan",
      "decision_point_description": "Whether to apply the saved scan-window filter as a bulk close across all low-severity scan-tagged alerts without excluding non-scan-subnet hosts such as FIN-WK-114.",
      "affected_reasoning_operation": "Alert triage, classification, and selection for bulk closure",
      "bias_specific_mechanism": "The analyst began with a strong prior expectation that the queue was dominated by scanner noise. He selectively matched alerts to the scan pattern and severity signal, so the FIN-WK-114 DNS alert, although not part of the scan subnet, was perceptually grouped with the expected noise and closed in the batch.",
      "manifestation_in_interview": "The participant described expecting scan noise, saw the queue as matching that expectation, and did not notice that FIN-WK-114 was outside 10.14.0.0/16 until later.",
      "effect_on_reasoning_or_decision": "The FIN-WK-114 DNS alert was swept into the bulk close, losing an early signal of the eventual compromise and contributing to delayed escalation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I sorted the queue, something like 92% of everything was tagged as coming from the scan subnet — port scans, auth attempts, the usual scanner fingerprint. That matched what I expected to see.",
          "evidence_explanation": "This quote establishes the prior expectation and the pattern-matching frame that governed the initial queue review."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It went out with the rest of the batch. I didn't clock at the time that it wasn't actually part of the scan subnet — I was scanning for the scan pattern, saw a low-severity tag, and it got swept up.",
          "evidence_explanation": "This quote directly shows the expectation-driven categorization error: the analyst scanned for the expected scan pattern, causing a non-scan host alert to be treated as noise."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized in the debrief that FIN-WK-114 was not part of the scan subnet and that a spot-check or subnet-separated view would have caught the alert. Workload and SLA pressure are substantial non-bias contributors, but the explicit description of scanning for the expected pattern supports a distinct expectation bias mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus mentions expectation as a common bias in aviation incident reports but does not provide an operational definition or mechanism sufficient to cite as direct support. Classification therefore relies on established cognitive-science knowledge of expectancy effects.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": ["complacency", "automation-induced complacency"],
      "taxonomy_status": "established_label",
      "bias_definition": "Automation complacency is insufficient verification or monitoring of automated output, resulting in acceptance of the automation's decisions without independently sampling the diagnostic information needed to confirm its recommendation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Phishing cluster containment determination",
      "decision_point_description": "Whether to declare the phishing cluster contained based on the suppression rule's auto-tagging and visible queue drop without checking delivery logs, sender variants, or a manual sample.",
      "affected_reasoning_operation": "Verification and containment assessment of a phishing campaign",
      "bias_specific_mechanism": "Trust in the analyst's self-built suppression rule reduced motivation to independently verify its operation in this campaign. The observed drop in visible alert count was interpreted as evidence of containment rather than as an automated tagging artifact, leading to premature closure of the ticket.",
      "manifestation_in_interview": "The participant told the shift lead the cluster looked contained and marked the ticket as contained without checking delivery logs or manual samples, citing the rule's prior reliability and the fast count drop.",
      "effect_on_reasoning_or_decision": "The phishing cluster was prematurely assessed as contained; a variant with a slightly different sender domain that the rule would not match was not initially detected or examined.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've got a suppression rule I wrote and deployed last week specifically to cut down on repeat-sender noise. When the phishing cluster came in, that rule auto-tagged about 40 duplicate alerts as handled almost immediately. Given how fast the visible queue cleared, I told the shift lead it looked contained.",
          "evidence_explanation": "The participant accepted the automated rule's handling as sufficient evidence of containment because the queue cleared quickly, illustrating reliance on automation output rather than independent verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. The rule's been solid since I built it, and seeing the count drop that fast felt like confirmation it was doing its job on this campaign too. I flagged it as contained in the ticket.",
          "evidence_explanation": "This quote shows under-sampling of diagnostic information and explicit trust in the automation as the basis for a containment decision."
        }
      ],
      "correction_or_counterevidence": "The participant later noticed a variant with a slightly different sender domain that the rule would not have matched. The bias occurred prior to that recognition; time pressure and legitimate use of suppression rules are contextual contributors, but the failure to verify before declaring containment matches automation complacency.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Parasuraman and Manzey source directly defines complacency as insufficient verification of automation output before acceptance, matching the participant's behavior.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it.",
          "mechanism_supported_by_source": "The source operationalizes complacency as accepting automation output without performing the information sampling necessary to verify the diagnosis.",
          "relevance_to_this_occurrence": "The participant accepted the suppression rule's automatic 'handled' tags without checking delivery logs or a manual sample, consistent with insufficient verification of automation output."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment heuristic", "anchoring effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Anchoring bias is the tendency to make judgments or classifications by starting from an initial value, example, or hypothesis and adjusting insufficiently from that anchor in light of additional information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "EDR anomaly classification for FIN-WK-114",
      "decision_point_description": "Whether to downgrade the FIN-WK-114 beacon-like anomaly as a likely backup-agent artifact and monitor only, or to pull the process tree and check the destination IP against threat intelligence.",
      "affected_reasoning_operation": "Anomaly classification, risk assessment, and downgrade decision",
      "bias_specific_mechanism": "Recent exposure to two prior backup-agent false positives provided an initial classification anchor. The analyst then adjusted insufficiently for the absence of a direct IOC match and downgraded the anomaly, even though the anchor was based on recency and interval similarity rather than signature evidence.",
      "manifestation_in_interview": "The participant classified the beacon-like activity as 'likely backup-agent artifact, monitor only' based mainly on the interval pattern resembling recent cases, with no direct IOC match.",
      "effect_on_reasoning_or_decision": "The anomalous C2 beacon was downgraded to monitor-only, delaying threat-intel correlation and escalation until after SLA lapse.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "No, it didn't — there was no IOC match, no clean fingerprint tying it to the agent. I noted it as 'likely backup-agent artifact, monitor only' based mostly on the interval pattern resembling those recent cases, and moved on to the phishing follow-up.",
          "evidence_explanation": "This quote shows an initial hypothesis drawn from recent cases while knowingly lacking direct signature evidence, a hallmark of anchoring from prior examples."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the interval and the fact that backup-agent issues had been the dominant explanation for anything beacon-like lately. If I'd seen this same alert two months ago, before those two tickets, I probably would've pulled the process tree first.",
          "evidence_explanation": "This counterfactual isolates the recent backup-agent pattern as the source of the anchored classification rather than the alert's own features."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably the beacon classification. I remember having a flicker of doubt — no direct IOC match nagged at me a little — but the recent pattern felt like a strong enough anchor to act on given the time crunch.",
          "evidence_explanation": "This explicitly identifies an anchor-like recent pattern and shows it overrode residual doubt from the missing IOC evidence."
        }
      ],
      "correction_or_counterevidence": "About forty minutes later, threat intelligence updated and flagged the destination IP as a known C2 rendezvous point, directly contradicting the backup-agent call and triggering an immediate escalation. The participant had recognized some doubt at the time but did not act on it before the later correction.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Rastogi et al. (2022) source supports anchoring-and-adjustment as a resource-rational but insufficient-adjustment process under time pressure.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source describes anchoring-and-adjustment as a time-pressured heuristic in which initial assessments are adjusted insufficiently, especially under shorter time allocations.",
          "relevance_to_this_occurrence": "The participant anchored on recent backup-agent cases and under-adjusted for the absence of a direct IOC match under time pressure, consistent with the anchoring-and-adjustment mechanism."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Single-participant retrospective self-report; no independent behavioral observation was available.",
    "The retrieved corpus contains OCR artifacts and limited definitions for expectation bias.",
    "High workload, SLA pressure, and time compression may partially explain some actions as bounded-rational adaptations rather than pure bias.",
    "The debrief format may not capture all contemporaneous cognitive processes."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our incident-response learning archive, not a performance review — you can skip anything you're not comfortable discussing. Can you start by stating your role and how long you've been on the Tier 2 triage rotation? Participant: Sure. I'm a Tier 2 SOC analyst, been doing log and alert triage for about two and a half years, most of that on the overnight rotation. This shift was a fairly typical Tuesday-into-Wednesday, except we had a scheduled vulnerability scan running against the 10.14.0.0/16 range. Interviewer: Good, let's go through what happened. Walk me through what you saw when you first opened the alert queue that night. Participant: I logged into the SIEM around 1 a.m. and the queue already had close to 300 new alerts in about twenty minutes, which is a lot even for us. Handoff notes from the day shift flagged that vuln management had an authenticated scan scheduled starting midnight, so I expected noise. When I sorted the queue, something like 92% of everything was tagged as coming from the scan subnet — port scans, auth attempts, the usual scanner fingerprint. That matched what I expected to see. Interviewer: What was your primary goal in those first ten minutes? Participant: Get through the noise fast so I wouldn't blow the 45-minute SLA on anything that actually mattered. With that volume, you can't eyeball every single alert individually — you triage by pattern. Interviewer: Okay, let's reconstruct the rest of the shift chronologically, then we'll go back and dig into specific decisions. What came after that initial queue review? Participant: I ran our saved scan-window filter to bulk-close the low-severity scan-tagged alerts, then almost immediately got pulled into a phishing cluster — a bunch of similar-looking emails landing in different inboxes. I spent maybe twenty minutes on that while the shift lead was pinging me for status. Then around 2:40, EDR kicked out an anomaly on a finance workstation, FIN-WK-114, with a process making periodic outbound connections. I looked at that, made a call, and moved on. About forty minutes later, a threat intel feed update came back and changed the picture on that same host, so I escalated to IR. Interviewer: Let's slow down on the first decision — closing that initial batch. What information did you actually have in front of you at the moment you applied the filter? Participant: The queue view, sorted by source subnet and severity. Almost everything was scan-subnet, low severity. There was one alert from FIN-WK-114 — a DNS query to a domain I didn't recognize — but it was sitting at low severity too, so visually it didn't distinguish itself from the rest of the batch. Interviewer: What other options did you consider before bulk-closing? Participant: I could have spot-checked a random sample of the low-severity ones outside the scan subnet before closing, or set a rule to pull out anything touching non-IT departments like finance for individual review. Honestly, with SLA pressure and that volume, the batch filter felt like the efficient move. I ran it across the whole set. Interviewer: And the FIN-WK-114 alert — what happened to it specifically? Participant: It went out with the rest of the batch. I didn't clock at the time that it wasn't actually part of the scan subnet — I was scanning for the scan pattern, saw a low-severity tag, and it got swept up. I didn't isolate it as a finance host outside 10.14.0.0/16 until I came back to it hours later. Interviewer: What would have needed to be different for you to catch that at the time? Participant: Probably if the queue view had color-coded by subnet instead of just severity, or if I'd run the spot-check option instead of the full batch close. In hindsight it was sitting right there. Interviewer: Let's move to the phishing cluster. What made you confident that was contained? Participant: I've got a suppression rule I wrote and deployed last week specifically to cut down on repeat-sender noise. When the phishing cluster came in, that rule auto-tagged about 40 duplicate alerts as handled almost immediately. Given how fast the visible queue cleared, I told the shift lead it looked contained. Interviewer: Did you verify that against anything else — inbox delivery logs, a manual sample? Participant: Not at that point, no. The rule's been solid since I built it, and seeing the count drop that fast felt like confirmation it was doing its job on this campaign too. I flagged it as contained in the ticket. Interviewer: Was there anything in the queue at that time that didn't fit that picture? Participant: There was one variant with a slightly different sender domain that the rule wouldn't have matched — I didn't clock that until later. At the time I was reading the drop in volume as the rule working. Interviewer: Understood. Now the EDR anomaly on FIN-WK-114 — what led you to the backup-agent explanation? Participant: The connection pattern — periodic, roughly every 55 seconds — looked a lot like something we'd seen twice in the previous two shifts, both traced back to a misconfigured backup agent on other hosts. That was fresh in my mind since I'd closed both of those tickets myself within the last week. Interviewer: Did the current alert have a direct signature match to that backup agent? Participant: No, it didn't — there was no IOC match, no clean fingerprint tying it to the agent. I noted it as 'likely backup-agent artifact, monitor only' based mostly on the interval pattern resembling those recent cases, and moved on to the phishing follow-up. Interviewer: Was pulling the process tree or checking the destination IP against threat intel an option at that point? Participant: Yeah, it was, and normally I'd lean that way if I weren't juggling two things. Since the pattern matched what I'd just dealt with twice, it felt like a safe bet to downgrade it and keep an eye on it rather than treat it as new. Interviewer: What told you it was 'safe' specifically — the interval, or something else? Participant: Mostly the interval and the fact that backup-agent issues had been the dominant explanation for anything beacon-like lately. If I'd seen this same alert two months ago, before those two tickets, I probably would've pulled the process tree first. Interviewer: Let's get to the fourth point — the escalation. What changed? Participant: About forty minutes later, threat intel updated and flagged that destination IP as a known C2 rendezvous point, which directly contradicted the backup-agent call. By then the SLA on that alert had already lapsed by twelve minutes, and my shift lead was tied up on another incident call for the next twenty. Interviewer: What were your options at that point? Participant: Escalate straight to IR with what I had, wait for the shift lead to be free for sign-off, or go back and rebuild the evidence chain from the earlier alerts first. I chose to escalate immediately — the SLA was already blown and waiting felt riskier than moving fast with an incomplete write-up. Interviewer: How did that play out? Participant: IR picked it up and confirmed lateral movement attempts from FIN-WK-114, consistent with that original DNS alert from hours earlier — the one that got closed in the batch. Interviewer: Looking back across the night, at what point were you least certain about your read of the situation? Participant: Probably the beacon classification. I remember having a flicker of doubt — no direct IOC match nagged at me a little — but the recent pattern felt like a strong enough anchor to act on given the time crunch. Interviewer: A couple of hypotheticals to close. If the scan window hadn't been running that night, do you think you'd have handled the FIN-WK-114 alert differently? Participant: Almost certainly. Without 300 scan alerts flooding the queue, that single DNS alert would have stood out on its own and I'd have looked at it individually. Interviewer: If you hadn't been the one who wrote the suppression rule, would you have checked phishing containment differently? Participant: Maybe — I might have been more inclined to ask someone else to verify it rather than trust the count dropping. Interviewer: And if the last two shifts hadn't involved backup-agent false positives, how might you have approached the beacon differently? Participant: I think I'd have gone straight to the process tree and IP lookup instead of pattern-matching against recent history. That comparison was really the whole reason I felt comfortable downgrading it. Interviewer: Last one — what single process change would have caught this earlier? Participant: Separating subnet visibility from severity in the queue view, so a scan-window filter can't accidentally sweep up a host that was never actually part of the scan. That's the gap that mattered most here. Interviewer: That's really helpful, thank you for walking through it in this much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.01s · gen 215.06s · total 220.8s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0286 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0250 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0241 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0239 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0238 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0229 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0224 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0209 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0180 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0177 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0170 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
13. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0168 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0166 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
16. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0163 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
17. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0162 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
19. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD tive biases or risktaking behavior and triage accuracy varied according 2.1._
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0161 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0161 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
22. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0160 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
23. **Lyell Automation bias and verification complexity.pdf** — 0.0159 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
25. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0157 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
26. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0156 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
27. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
32. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0149 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. Chan, U. Dulleck et al. 2.5. Statistical analy_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
36. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0144 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
37. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
38. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0141 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
39. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0141 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
43. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
45. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0138 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. C han, U. Dulleck et al. In the triage decisio_
46. **Lyell Automation bias and verification complexity.pdf** — 0.0137 (rrf) — _## INTRODUCTION | | • Monitoring tasks require the user to monitor for a change in | | parative _
47. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0136 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
48. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0136 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
49. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0135 (rrf) — _# i cdecision allegiance . As we move to the bottom of the taxonomy, we focus on the more fundam_
50. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0135 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the participant's incident-response narrative for reasoning episodes that show affirmative evidence of bias-specific mechanisms. Interviewer questions and hypothetical probes were not treated as evidence of bias; only the participant's actual reported reasoning and decisions were classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "expectation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "expectation bias",
      "alternative_labels": [
        "confirmation bias",
        "expectation-driven selective attention"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a prior expectation or hypothesis to shape perception and evaluation of information, leading to underweighting or overlooking disconfirming cues.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Bulk-closing scan-window alerts",
      "decision_point_description": "Whether to apply the saved scan-window filter across the full low-severity queue or first separate non-scan-subnet hosts.",
      "affected_reasoning_operation": "Triage categorization under alert overload",
      "bias_specific_mechanism": "The participant entered the shift expecting scanner noise from the scheduled vulnerability scan. That expectation led him to read ambiguous low-severity alerts as consistent with the scan-noise pattern, and he did not detect that FIN-WK-114 was outside the scan subnet before bulk-closing it.",
      "manifestation_in_interview": "The participant reported that the queue was overwhelmingly scan-subnet noise, matched his expectation, and that the one finance alert did not visually distinguish itself. He later stated he was scanning for the scan pattern and the alert got swept up.",
      "effect_on_reasoning_or_decision": "A non-scan-subnet finance DNS alert from FIN-WK-114 was bulk-closed with scanner noise, preventing early investigation of the host that later showed lateral movement attempts.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Handoff notes from the day shift flagged that vuln management had an authenticated scan scheduled starting midnight, so I expected noise.",
          "evidence_explanation": "This establishes the prior expectation that shaped his subsequent interpretation of the alert queue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I sorted the queue, something like 92% of everything was tagged as coming from the scan subnet — port scans, auth attempts, the usual scanner fingerprint. That matched what I expected to see.",
          "evidence_explanation": "He explicitly reports that the observed pattern matched his expectation, increasing the likelihood of treating the entire queue as scanner noise."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't clock at the time that it wasn't actually part of the scan subnet — I was scanning for the scan pattern, saw a low-severity tag, and it got swept up.",
          "evidence_explanation": "This shows the expectation-based search pattern: he looked for scan-subnet cues, and an out-of-subnet host was not noticed as disconfirming."
        }
      ],
      "correction_or_counterevidence": "The queue was genuinely dominated by scan-subnet alerts, the FIN-WK-114 alert was low severity, and the queue view did not color-code by subnet; SLA pressure also made pattern triage a plausible resource-conserving strategy. The participant did consider spot-checking before bulk-closing, and he later recognized the host was outside 10.14.0.0/16.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Available retrieved corpus material mentioned expectation bias only in passing without a mechanistic definition, so the label and mechanism here draw on general cognitive-science/human-factors knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency bias",
        "automation-induced complacency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient verification or monitoring of automated outputs because of excessive trust in the automation; the operator samples less information than necessary to validate the automation's recommendation or action.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Declaring phishing cluster contained after suppression-rule auto-tagging",
      "decision_point_description": "Whether to verify suppression-rule auto-tagging against inbox delivery logs or manual samples before reporting containment.",
      "affected_reasoning_operation": "Containment verification judgment",
      "bias_specific_mechanism": "The participant relied on a self-deployed suppression rule to auto-tag duplicate phishing alerts and accepted the rapid queue drop as sufficient evidence that the campaign was contained, without manually verifying delivery or sampling messages.",
      "manifestation_in_interview": "He told the shift lead the phishing cluster looked contained after the suppression rule cleared visible alerts. He did not verify against inbox logs or a manual sample at that point because the rule had been solid and the fast count drop felt confirmatory.",
      "effect_on_reasoning_or_decision": "The phishing cluster was prematurely reported as contained; a variant with a slightly different sender domain that the rule would not have matched was missed until later.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've got a suppression rule I wrote and deployed last week specifically to cut down on repeat-sender noise. When the phishing cluster came in, that rule auto-tagged about 40 duplicate alerts as handled almost immediately.",
          "evidence_explanation": "This shows the automated suppression rule producing the visible containment signal he relied upon."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Given how fast the visible queue cleared, I told the shift lead it looked contained.",
          "evidence_explanation": "He treated the speed of queue clearance as a sufficient containment indicator rather than seeking independent verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. The rule's been solid since I built it, and seeing the count drop that fast felt like confirmation it was doing its job on this campaign too.",
          "evidence_explanation": "Explicitly links reduced verification to trust in automation and interpretative confirmation from the count drop."
        }
      ],
      "correction_or_counterevidence": "The suppression rule had been reliable since deployment, and overall queue pressure was high. However, a later recognized variant with a different sender domain was outside the rule's match profile, indicating the containment check was incomplete.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved passage supports the automation-verification/complacency mechanism, using the term 'operator complacency' for insufficient verification of automation output.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation's diagnosis before accepting it. Participants were provided independent access (via mouse click) to all relevant system information ... needed to verify the aid's diagnoses. This procedure allowed the investigators to assess the level of operator complacency in interaction with the aid ... However, participants sampling less information than that necessary to completely verify the aid's recommendation were...",
          "mechanism_supported_by_source": "Automation complacency is evidenced when an operator samples less information than needed to verify an automated aid's output before accepting it.",
          "relevance_to_this_occurrence": "The participant accepted the suppression rule's auto-tagging and reported containment without accessing independent verification data such as delivery logs or a manual sample."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "availability heuristic",
        "representativeness heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "An initial value, example, or diagnosis anchors an estimate or classification, and subsequent adjustment away from that anchor tends to be insufficient even when new or disconfirming information is available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Classifying EDR beacon on FIN-WK-114 as likely backup-agent artifact",
      "decision_point_description": "Whether to treat the beacon as a known backup-agent artifact or investigate it as a novel threat by pulling the process tree and checking the destination IP.",
      "affected_reasoning_operation": "Diagnostic classification and risk assessment of an anomaly",
      "bias_specific_mechanism": "The participant anchored his interpretation of the current beacon to two recent backup-agent cases he had personally closed. Although the current alert had no IOC match, he did not adjust sufficiently away from the recent-case anchor and downgraded the alert to monitor-only.",
      "manifestation_in_interview": "The periodic interval pattern resembled recent backup-agent false positives, so the participant classified the beacon as a likely backup-agent artifact despite the absence of a direct signature match and moved on.",
      "effect_on_reasoning_or_decision": "The anomaly was downgraded without pulling the process tree or checking the destination IP, delaying escalation until threat intelligence later flagged the destination as a C2 rendezvous point.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The connection pattern — periodic, roughly every 55 seconds — looked a lot like something we'd seen twice in the previous two shifts, both traced back to a misconfigured backup agent on other hosts. That was fresh in my mind since I'd closed both of those tickets myself within the last week.",
          "evidence_explanation": "This shows the recent backup-agent cases supplying the initial diagnostic anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, it didn't — there was no IOC match, no clean fingerprint tying it to the agent. I noted it as 'likely backup-agent artifact, monitor only' based mostly on the interval pattern resembling those recent cases, and moved on to the phishing follow-up.",
          "evidence_explanation": "Disconfirming information existed, but the participant still classified the alert to match the anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember having a flicker of doubt — no direct IOC match nagged at me a little — but the recent pattern felt like a strong enough anchor to act on given the time crunch.",
          "evidence_explanation": "The participant explicitly describes the recent pattern as an anchor and acknowledges insufficient adjustment away from it."
        }
      ],
      "correction_or_counterevidence": "The participant reported a flicker of doubt about the absent IOC and said he would normally pull the process tree when not multi-tasking. Later threat-intel contradicting the backup-agent call led to escalation and IR confirmation of lateral movement attempts.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved passage supports the anchoring-and-adjustment heuristic, including the typical finding that adjustment away from the initial anchor is insufficient.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive Bias in the Verification and Validation of Space Flight Systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "people make estimates based on an initial answer, and adjustments from there based on additional informat Tversky and Kahneman put it, 'adjustments are typic insufficient.' [16]",
          "mechanism_supported_by_source": "The source describes anchoring on an initial answer and insufficient subsequent adjustment from that anchor.",
          "relevance_to_this_occurrence": "The participant anchored on recent backup-agent classifications and did not sufficiently adjust for the absence of a direct IOC match before downgrading the alert."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective self-report; recall and self-presentation may distort the original reasoning.",
    "No objective behavioral logs or normative benchmark were available to compare the participant's triage decisions against an optimal decision process.",
    "Retrieved corpus support was uneven: automation complacency and anchoring had relevant mechanistic excerpts, while expectation bias was identified primarily from general human-factors/cognitive-science knowledge because the available retrieved passage lacked detail.",
    "Resource constraints such as SLA pressure, queue volume, and concurrent incidents were treated as context, not as bias, unless a distinct bias-specific mechanism was evidenced."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our incident-response learning archive, not a performance review — you can skip anything you're not comfortable discussing. Can you start by stating your role and how long you've been on the Tier 2 triage rotation? Participant: Sure. I'm a Tier 2 SOC analyst, been doing log and alert triage for about two and a half years, most of that on the overnight rotation. This shift was a fairly typical Tuesday-into-Wednesday, except we had a scheduled vulnerability scan running against the 10.14.0.0/16 range. Interviewer: Good, let's go through what happened. Walk me through what you saw when you first opened the alert queue that night. Participant: I logged into the SIEM around 1 a.m. and the queue already had close to 300 new alerts in about twenty minutes, which is a lot even for us. Handoff notes from the day shift flagged that vuln management had an authenticated scan scheduled starting midnight, so I expected noise. When I sorted the queue, something like 92% of everything was tagged as coming from the scan subnet — port scans, auth attempts, the usual scanner fingerprint. That matched what I expected to see. Interviewer: What was your primary goal in those first ten minutes? Participant: Get through the noise fast so I wouldn't blow the 45-minute SLA on anything that actually mattered. With that volume, you can't eyeball every single alert individually — you triage by pattern. Interviewer: Okay, let's reconstruct the rest of the shift chronologically, then we'll go back and dig into specific decisions. What came after that initial queue review? Participant: I ran our saved scan-window filter to bulk-close the low-severity scan-tagged alerts, then almost immediately got pulled into a phishing cluster — a bunch of similar-looking emails landing in different inboxes. I spent maybe twenty minutes on that while the shift lead was pinging me for status. Then around 2:40, EDR kicked out an anomaly on a finance workstation, FIN-WK-114, with a process making periodic outbound connections. I looked at that, made a call, and moved on. About forty minutes later, a threat intel feed update came back and changed the picture on that same host, so I escalated to IR. Interviewer: Let's slow down on the first decision — closing that initial batch. What information did you actually have in front of you at the moment you applied the filter? Participant: The queue view, sorted by source subnet and severity. Almost everything was scan-subnet, low severity. There was one alert from FIN-WK-114 — a DNS query to a domain I didn't recognize — but it was sitting at low severity too, so visually it didn't distinguish itself from the rest of the batch. Interviewer: What other options did you consider before bulk-closing? Participant: I could have spot-checked a random sample of the low-severity ones outside the scan subnet before closing, or set a rule to pull out anything touching non-IT departments like finance for individual review. Honestly, with SLA pressure and that volume, the batch filter felt like the efficient move. I ran it across the whole set. Interviewer: And the FIN-WK-114 alert — what happened to it specifically? Participant: It went out with the rest of the batch. I didn't clock at the time that it wasn't actually part of the scan subnet — I was scanning for the scan pattern, saw a low-severity tag, and it got swept up. I didn't isolate it as a finance host outside 10.14.0.0/16 until I came back to it hours later. Interviewer: What would have needed to be different for you to catch that at the time? Participant: Probably if the queue view had color-coded by subnet instead of just severity, or if I'd run the spot-check option instead of the full batch close. In hindsight it was sitting right there. Interviewer: Let's move to the phishing cluster. What made you confident that was contained? Participant: I've got a suppression rule I wrote and deployed last week specifically to cut down on repeat-sender noise. When the phishing cluster came in, that rule auto-tagged about 40 duplicate alerts as handled almost immediately. Given how fast the visible queue cleared, I told the shift lead it looked contained. Interviewer: Did you verify that against anything else — inbox delivery logs, a manual sample? Participant: Not at that point, no. The rule's been solid since I built it, and seeing the count drop that fast felt like confirmation it was doing its job on this campaign too. I flagged it as contained in the ticket. Interviewer: Was there anything in the queue at that time that didn't fit that picture? Participant: There was one variant with a slightly different sender domain that the rule wouldn't have matched — I didn't clock that until later. At the time I was reading the drop in volume as the rule working. Interviewer: Understood. Now the EDR anomaly on FIN-WK-114 — what led you to the backup-agent explanation? Participant: The connection pattern — periodic, roughly every 55 seconds — looked a lot like something we'd seen twice in the previous two shifts, both traced back to a misconfigured backup agent on other hosts. That was fresh in my mind since I'd closed both of those tickets myself within the last week. Interviewer: Did the current alert have a direct signature match to that backup agent? Participant: No, it didn't — there was no IOC match, no clean fingerprint tying it to the agent. I noted it as 'likely backup-agent artifact, monitor only' based mostly on the interval pattern resembling those recent cases, and moved on to the phishing follow-up. Interviewer: Was pulling the process tree or checking the destination IP against threat intel an option at that point? Participant: Yeah, it was, and normally I'd lean that way if I weren't juggling two things. Since the pattern matched what I'd just dealt with twice, it felt like a safe bet to downgrade it and keep an eye on it rather than treat it as new. Interviewer: What told you it was 'safe' specifically — the interval, or something else? Participant: Mostly the interval and the fact that backup-agent issues had been the dominant explanation for anything beacon-like lately. If I'd seen this same alert two months ago, before those two tickets, I probably would've pulled the process tree first. Interviewer: Let's get to the fourth point — the escalation. What changed? Participant: About forty minutes later, threat intel updated and flagged that destination IP as a known C2 rendezvous point, which directly contradicted the backup-agent call. By then the SLA on that alert had already lapsed by twelve minutes, and my shift lead was tied up on another incident call for the next twenty. Interviewer: What were your options at that point? Participant: Escalate straight to IR with what I had, wait for the shift lead to be free for sign-off, or go back and rebuild the evidence chain from the earlier alerts first. I chose to escalate immediately — the SLA was already blown and waiting felt riskier than moving fast with an incomplete write-up. Interviewer: How did that play out? Participant: IR picked it up and confirmed lateral movement attempts from FIN-WK-114, consistent with that original DNS alert from hours earlier — the one that got closed in the batch. Interviewer: Looking back across the night, at what point were you least certain about your read of the situation? Participant: Probably the beacon classification. I remember having a flicker of doubt — no direct IOC match nagged at me a little — but the recent pattern felt like a strong enough anchor to act on given the time crunch. Interviewer: A couple of hypotheticals to close. If the scan window hadn't been running that night, do you think you'd have handled the FIN-WK-114 alert differently? Participant: Almost certainly. Without 300 scan alerts flooding the queue, that single DNS alert would have stood out on its own and I'd have looked at it individually. Interviewer: If you hadn't been the one who wrote the suppression rule, would you have checked phishing containment differently? Participant: Maybe — I might have been more inclined to ask someone else to verify it rather than trust the count dropping. Interviewer: And if the last two shifts hadn't involved backup-agent false positives, how might you have approached the beacon differently? Participant: I think I'd have gone straight to the process tree and IP lookup instead of pattern-matching against recent history. That comparison was really the whole reason I felt comfortable downgrading it. Interviewer: Last one — what single process change would have caught this earlier? Participant: Separating subnet visibility from severity in the queue view, so a scan-window filter can't accidentally sweep up a host that was never actually part of the scan. That's the gap that mattered most here. Interviewer: That's really helpful, thank you for walking through it in this much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.07s · gen 138.33s · total 144.5s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0286 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0250 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0241 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0239 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0238 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0229 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0224 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0209 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0180 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0177 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0170 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
13. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0168 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0166 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
16. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0163 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
17. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0162 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
19. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD tive biases or risktaking behavior and triage accuracy varied according 2.1._
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0161 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0161 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
22. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0160 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
23. **Lyell Automation bias and verification complexity.pdf** — 0.0159 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
25. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0157 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
26. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0156 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
27. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
32. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0149 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. Chan, U. Dulleck et al. 2.5. Statistical analy_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
36. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0144 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
37. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
38. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0141 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
39. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0141 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
43. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
45. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0138 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. C han, U. Dulleck et al. In the triage decisio_
46. **Lyell Automation bias and verification complexity.pdf** — 0.0137 (rrf) — _## INTRODUCTION | | • Monitoring tasks require the user to monitor for a change in | | parative _
47. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0136 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
48. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0136 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
49. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0135 (rrf) — _# i cdecision allegiance . As we move to the bottom of the taxonomy, we focus on the more fundam_
50. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0135 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a Tier 2 SOC analyst's retrospective incident debrief for affirmatively evidenced cognitive-bias mechanisms in triage, containment, and escalation decisions."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "expectation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "expectation bias",
      "alternative_labels": [
        "expectancy bias",
        "confirmation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for prior expectations to shape perception and interpretation, leading a decision-maker to overlook or discount information that is inconsistent with those expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial SIEM queue triage and bulk-close of low-severity scan-tagged alerts",
      "decision_point_description": "When the participant applied the saved scan-window filter and bulk-closed low-severity alerts, including a FIN-WK-114 DNS alert that was not part of the scan subnet.",
      "affected_reasoning_operation": "Alert classification and visual search: distinguishing expected scan noise from a potentially significant non-scan alert.",
      "bias_specific_mechanism": "The participant's prior expectation of scan-induced noise led him to search for a match to the scan pattern and to treat low severity as sufficient confirmation that the alert belonged to the scan batch, preventing him from noticing that the host was outside 10.14.0.0/16.",
      "manifestation_in_interview": "The participant reported expecting noise from the scheduled vulnerability scan, sorted by source subnet and severity, and applied a bulk filter. He acknowledged that a finance workstation alert was visually indistinct in that framing and was swept up even though it was not part of the scan subnet.",
      "effect_on_reasoning_or_decision": "The FIN-WK-114 DNS alert was bulk-closed with the scan-tagged alerts and was not individually triaged, delaying detection of a finance workstation that was later confirmed as attempting lateral movement.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Handoff notes from the day shift flagged that vuln management had an authenticated scan scheduled starting midnight, so I expected noise.",
          "evidence_explanation": "Shows an explicit prior expectation of scan noise that framed subsequent alert interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was one alert from FIN-WK-114 — a DNS query to a domain I didn't recognize — but it was sitting at low severity too, so visually it didn't distinguish itself from the rest of the batch.",
          "evidence_explanation": "The alert contained distinct cues, including an unrecognized domain and a finance host, but the expectation-driven scan/severity framing made it blend into the batch."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It went out with the rest of the batch. I didn't clock at the time that it wasn't actually part of the scan subnet — I was scanning for the scan pattern, saw a low-severity tag, and it got swept up.",
          "evidence_explanation": "Directly describes expectation-based selective processing: he was looking for the scan pattern and failed to register the mismatching subnet."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Almost certainly. Without 300 scan alerts flooding the queue, that single DNS alert would have stood out on its own and I'd have looked at it individually.",
          "evidence_explanation": "Counterfactual support that the scan-related expectation and queue context drove the oversight rather than the alert's intrinsic content."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized the missed alert after a threat-intel update and IR confirmation. High queue volume and SLA pressure are present as contextual factors, but the transcript also shows a specific expectation-driven failure to segregate a non-scan host.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved source identifies expectation as a cognitive bias type in operational incident reports, supporting the label's relevance, though the passage is brief.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality Sam O'Connor (1).pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation,\n\nand plan continuation , and in some cases multiple biases",
          "mechanism_supported_by_source": "Indicates expectation is recognized as a cognitive bias type contributing to operational incidents.",
          "relevance_to_this_occurrence": "Supports classification of the participant's scan-driven expectation as a bias rather than merely an ordinary workload heuristic."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "automation bias",
        "overreliance on automation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Reduced verification or monitoring of an automated aid due to trust, leading the operator to sample less information than necessary to detect failures or incomplete coverage.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Phishing cluster containment assessment after suppression-rule auto-tagging",
      "decision_point_description": "When the participant told the shift lead the phishing cluster looked contained and flagged it as contained in the ticket without verifying the suppression rule's coverage against inbox delivery logs or a manual sample.",
      "affected_reasoning_operation": "Verification and containment judgment: deciding whether the automated suppression rule had actually contained the phishing campaign.",
      "bias_specific_mechanism": "Over-trust in a self-authored, previously successful suppression rule caused the participant to treat the rapid reduction in visible alert count as sufficient evidence that the rule was working, without checking for variants the rule would not match.",
      "manifestation_in_interview": "The participant reported that he did not verify against inbox delivery logs or a manual sample at the time, and interpreted the fast drop in visible queue count as confirmation of containment. He later acknowledged that a variant with a different sender domain had been present but unnoticed.",
      "effect_on_reasoning_or_decision": "The phishing cluster was prematurely flagged as contained, and a phishing variant that the suppression rule would not have matched was missed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've got a suppression rule I wrote and deployed last week specifically to cut down on repeat-sender noise. When the phishing cluster came in, that rule auto-tagged about 40 duplicate alerts as handled almost immediately.",
          "evidence_explanation": "Establishes reliance on an automated suppression rule to process the phishing cluster."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Given how fast the visible queue cleared, I told the shift lead it looked contained.",
          "evidence_explanation": "Shows that the containment inference was based on visible queue clearance caused by automation rather than independent verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The rule's been solid since I built it, and seeing the count drop that fast felt like confirmation it was doing its job on this campaign too. I flagged it as contained in the ticket.",
          "evidence_explanation": "Demonstrates over-trust from prior success and authorship, and interpretation of the count drop as sufficient confirmation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was one variant with a slightly different sender domain that the rule wouldn’t have matched — I didn't clock that until later. At the time I was reading the drop in volume as the rule working.",
          "evidence_explanation": "Shows a disconfirming cue existed but was overlooked due to complacent reliance on the rule."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous verification was performed. The participant later noticed the variant, but only after initially flagging the cluster as contained.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved source provides a definitional framework for complacency as insufficient verification of an automated aid.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "However, participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "Defines complacency as insufficient information sampling before accepting an automated aid's recommendation.",
          "relevance_to_this_occurrence": "The participant sampled no independent information before accepting the suppression rule's apparent containment, matching this pattern."
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
        "recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive heuristic in which judgments are influenced by the ease with which examples come to mind; recent or salient instances can be overweighted relative to other diagnostic evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "EDR anomaly triage for FIN-WK-114 beaconing",
      "decision_point_description": "When the participant downgraded the FIN-WK-114 beaconing anomaly to 'likely backup-agent artifact, monitor only' without pulling the process tree or checking the destination IP against threat intel.",
      "affected_reasoning_operation": "Diagnostic classification: deciding whether the beacon-like connection pattern was malicious or a known benign backup-agent artifact.",
      "bias_specific_mechanism": "Two recent backup-agent cases from the previous shifts were highly accessible in memory, so the participant used their resemblance to the interval pattern as the primary basis for downgrading the alert, despite the absence of a direct IOC match.",
      "manifestation_in_interview": "The participant stated the recent backup-agent tickets were fresh in his mind and that he classified the alert based mostly on the interval pattern resembling those recent cases. He acknowledged he would likely have investigated more thoroughly without those recent examples.",
      "effect_on_reasoning_or_decision": "The C2 beacon was downgraded and monitored instead of investigated, delaying escalation until a later threat-intel update flagged the destination IP as a known C2 rendezvous point.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The connection pattern — periodic, roughly every 55 seconds — looked a lot like something we'd seen twice in the previous two shifts, both traced back to a misconfigured backup agent on other hosts. That was fresh in my mind since I'd closed both of those tickets myself within the last week.",
          "evidence_explanation": "Shows recent examples were easily recalled and dominated initial pattern interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I noted it as 'likely backup-agent artifact, monitor only' based mostly on the interval pattern resembling those recent cases, and moved on.",
          "evidence_explanation": "Indicates the diagnostic decision was based on similarity to available recent cases rather than current direct evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the interval and the fact that backup-agent issues had been the dominant explanation for anything beacon-like lately. If I'd seen this same alert two months ago, before those two tickets, I probably would've pulled the process tree first.",
          "evidence_explanation": "Explicitly attributes the downgrade to recent history rather than a diagnostic match."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the last two shifts hadn't involved backup-agent false positives... I think I'd have gone straight to the process tree and IP lookup instead of pattern-matching against recent history. That comparison was really the whole reason I felt comfortable downgrading it.",
          "evidence_explanation": "Counterfactual confirms the causal role of easily recalled recent cases in the downgrade decision."
        }
      ],
      "correction_or_counterevidence": "The participant noted a flicker of doubt about the missing IOC match but did not act on it. A later threat-intel update contradicted the backup-agent call.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically defines the availability heuristic; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a retrospective self-report; some mechanisms rely on the participant's counterfactual statements, but those statements are consistent with the recorded decisions.",
    "Retrieval coverage was sparse for the availability heuristic, so that occurrence is supported by general knowledge rather than retrieved corpus evidence."
  ]
}

