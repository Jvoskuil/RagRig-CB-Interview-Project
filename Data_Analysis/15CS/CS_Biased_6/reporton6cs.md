# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm — this is for internal process research, not a performance review, and you can decline to answer anything. Okay? Participant: Yeah, that's fine. Interviewer: Can you tell me a bit about your role? Participant: I'm a vulnerability management analyst on the security operations team. I triage scanner findings, vendor advisories, coordinate patch timelines with IT ops, and escalate anything that looks like active exploitation to incident response. I also chase our open findings backlog for compliance reporting. Interviewer: Let's talk about the CVE that came in a few weeks back. Walk me through what happened. Participant: It was mid-morning when a vendor advisory landed — a new CVE, CVSS 9.8, remote code execution, affecting our internet-facing authentication API. At the same time I had roughly forty open findings from the previous week's scan sitting in my queue, with forty-eight hours until our compliance audit report was due. One backlog item was an unpatched database server with excessive service-account privileges, open ninety-plus days. And the week before, there'd been a big breach in the news — a VPN appliance that hadn't been patched — it caused a mess for that company and was all over our internal Slack. Interviewer: When the new CVE came in, what did you do first? Participant: My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere. I moved it to the top of the queue and started routing it into our standard remediation workflow. The database finding stayed where it was. Interviewer: Where did the routing go? Participant: Into our web-application remediation queue. Honestly, when I saw 'authentication' and 'internet-facing' together, my head just went straight to the same kind of injection-style tickets that make up most of what crosses my desk — that's the pattern I see constantly, so it's the one that came to mind first. There was a line in the advisory pointing more toward the API-gateway team being the better owner, but I didn't stop on it long enough to change course, and it went into the usual queue. Interviewer: Did you look closely at the advisory's technical detail before routing it? Participant: I skimmed it — saw 'authentication,' saw 'internet-facing,' saw the CVSS score, and that was enough to know it needed to move fast. I didn't dig into the exploit chain right away because time was tight. Interviewer: Later you found it wasn't quite a standard web-app issue? Participant: Right — it turned out to be an authentication bypass in the API gateway, a different exploit path than the injection-style stuff that queue usually handles. It got redirected eventually, but that cost some time. Interviewer: Going back to that first decision — the new CVE and the ninety-day-old database finding were competing for urgency. What made the new one win? Participant: Honestly, it felt more urgent. The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull. Interviewer: If you'd ranked them purely on asset criticality and exposure, independent of the news, how would that have gone? Participant: The database server probably deserved more attention than I gave it. It ended up flagged by the audit team afterward as our most severe open item. But at the time, the CVE felt like the more pressing thing. Interviewer: Later that day you were cross-referencing the CVE against the asset inventory when something else came up. Participant: Yeah, while going host by host through the inventory, the SIEM threw an alert — 'privilege escalation, low confidence' — on an internal box. That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on. Interviewer: Was there anything specific in that alert that stood out? Participant: There was a log entry with a lateral-movement timestamp that was a little unusual. I registered it existed, but I was heads-down trying to finish the asset match, so I didn't stop to dig in. Interviewer: Was there anything else on that dashboard view at the time? Participant: [pause] I'd have to think about that. I was really focused on the inventory cross-reference right then. Interviewer: There was an anomalous outbound traffic entry flagged on that same host, visible in the same panel. Do you recall it? Participant: I don't specifically remember it. I was scrolling through host records, not scanning that side panel. It's possible it was there and I just didn't register it — my attention was on matching CVE-affected assets, not general alert triage. Interviewer: That entry was later linked to a confirmed low-level compromise on that host. Does that change how you see the decision to move past the alert? Participant: It's easy to say now I should've stopped. At the time, given how often that label turns out to be routine, continuing with the task in front of me felt reasonable. I didn't have a strong signal telling me to drop what I was doing. Interviewer: Let's talk about the change window request. What went into that? Participant: IT ops needed written justification to approve an emergency window during business hours instead of the weekend cycle, since patching would disrupt customer transactions for about twenty minutes. I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast. Interviewer: What did the exploitation data actually say? Participant: The EPSS score put it at moderate probability, comparable to a handful of things we've handled on the normal weekend schedule over the past year. Not in the exceptional range. Interviewer: So the justification leaned more on what the company could lose than on that probability figure? Participant: Yeah, that's fair. When I sat down to write it, thinking through what we'd lose if it went wrong — the contract, the reputation hit, the audit exposure — made it feel like this had to move now. If I'd framed the same numbers around just getting ahead of the patch cycle or keeping things running smoothly, it probably wouldn't have felt as urgent to me, even though the underlying EPSS score and the twenty-minute disruption were exactly the same either way. Interviewer: Did it work? Participant: It did — they approved the window. Though nothing was actually observed exploiting that CVE the following week, so it's hard to say in hindsight whether the urgency was fully warranted. Interviewer: Last decision point — finalizing which systems to patch. Participant: The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out. Interviewer: Did you check the asset inventory outside that default view? Participant: Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture. Interviewer: There were actually three more hosts with the same vulnerable library, tagged under a different asset category, visible in the inventory with a manual filter change. Participant: One of those turned up still vulnerable in the follow-up audit scan a week later. A manual cross-check would have caught it, but with the clock running down, the scanner's output was what I had in front of me and it looked complete. Interviewer: If the VPN breach hadn't been in the news that week, would you have triaged the CVE the same way? Participant: Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding. Interviewer: If the scanner had surfaced five hosts instead of two, would scoping have gone differently? Participant: Probably — I'd have just patched whatever the tool showed me. I wasn't second-guessing whether the list was complete. Interviewer: Anything you'd flag differently now? Participant: The outbound traffic entry, for sure. And maybe relying less on how an alert label has resolved in the past versus what's specifically in front of me each time. Interviewer: If you had to write that justification again today, would you frame it differently? Participant: I might lead with the actual numbers instead of the worst-case story. Though the worst-case framing is usually what gets things approved quickly around here. Interviewer: That's really helpful, thank you. Participant: No problem, happy to help.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.99s · gen 175.31s · total 181.2s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0281 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0242 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0224 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0204 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0202 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
9. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0187 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0187 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **Lyell Automation bias and verification complexity.pdf** — 0.0187 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0178 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0178 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
15. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0175 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0174 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0165 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
18. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
20. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
22. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
23. **Goddard et al. (2011) Automation bias_a systematic review of frequency, effect mediators, and mitigators.pdf** — 0.0162 (rrf) — _## Jeremy C Wyatt ’ s expertise were considered. fi ed 14457 research papers REVIEW AIM AND OBJE_
24. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0161 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
25. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0160 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
26. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0160 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
27. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0160 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
28. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0158 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
30. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0157 (rrf) — _# across domains and different parts of the search process. to help inform their opinions \[ 45 _
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
33. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0152 (rrf) — _### cKniff 2004 ; Radley et al., 2013 and reporting others about medication errors, and it foste_
34. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0150 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
35. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0149 (rrf) — _### cKniff study, we focus on stress as stimuli perceived by individuals in the environment and _
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
37. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0147 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
38. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0146 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
39. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0145 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
40. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0144 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
41. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0144 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0141 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0140 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 394 when the aid p_
47. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision Projection) method , which entails from time to time projecting bombs onto the Xra_
48. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0139 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first evaluation of one security operations vulnerability-management interview for affirmative evidence of cognitive biases in prioritization, categorization, justification, and automation-supported scoping decisions."
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
      "bias_label": "framing effect",
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
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging frequency, probability, or urgency based on ease with which relevant instances come to mind; recent, salient, or emotionally vivid events disproportionately influence risk judgments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Prioritization of new CVE versus backlog database finding",
      "decision_point_description": "Choosing whether to move the new internet-facing CVE above the older database finding for immediate remediation.",
      "affected_reasoning_operation": "Risk/urgency prioritization and allocation of remediation attention",
      "bias_specific_mechanism": "The recent, salient VPN breach was highly available in memory and made a similar-sounding internet-facing CVE seem more urgent and likely to cause harm than the older database issue, even though the database issue was severe on its own technical merits.",
      "manifestation_in_interview": "The participant explicitly linked the new CVE's urgency to the fresh breach story and stated that the older database finding lacked that same pull because nothing new had happened with it.",
      "effect_on_reasoning_or_decision": "The new CVE was moved to the top of the queue and routed into the remediation workflow, while the database finding remained where it was.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere.",
          "evidence_explanation": "This shows the recent breach analog was immediately available and shaped the initial urgency judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull.",
          "evidence_explanation": "The participant contrasts a fresh, salient case with a severe but quiet backlog item, revealing availability-driven urgency rather than purely asset-criticality-based prioritization."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding.",
          "evidence_explanation": "The participant affirmatively acknowledges that the recent story affected triage speed, supporting the mechanism."
        }
      ],
      "correction_or_counterevidence": "The new CVE was genuinely critical and internet-facing, so high priority was not irrational. The bias concerns the incremental urgency over the older database issue caused by the recent salient event.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided context directly addressed the availability heuristic; classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias",
        "prototype bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging category membership or likelihood by similarity to a familiar prototype, often while ignoring diagnostic details or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial routing of new CVE to remediation queue",
      "decision_point_description": "Selecting the remediation queue and responsible team for the new CVE after skimming the advisory.",
      "affected_reasoning_operation": "Categorization and team routing under time pressure",
      "bias_specific_mechanism": "Superficial features of the CVE, especially 'authentication' and 'internet-facing,' matched the participant's familiar prototype of web-application injection tickets, causing him to categorize and route the issue to that usual queue despite an advisory cue indicating API-gateway ownership.",
      "manifestation_in_interview": "The participant said his head went straight to the frequent injection-style ticket pattern and that he did not stop on the API-gateway ownership line long enough to change course.",
      "effect_on_reasoning_or_decision": "The CVE was initially routed to the web-application remediation queue, later required redirection to the API gateway team, and cost time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, when I saw 'authentication' and 'internet-facing' together, my head just went straight to the same kind of injection-style tickets that make up most of what crosses my desk — that's the pattern I see constantly, so it's the one that came to mind first.",
          "evidence_explanation": "This demonstrates prototype-based categorization using superficial similarity to familiar injection-style tickets rather than detailed technical discrimination."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a line in the advisory pointing more toward the API-gateway team being the better owner, but I didn't stop on it long enough to change course, and it went into the usual queue.",
          "evidence_explanation": "A diagnostic cue pointing away from the initial category was available but underweighted, supporting representativeness-driven categorization."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Right — it turned out to be an authentication bypass in the API gateway, a different exploit path than the injection-style stuff that queue usually handles. It got redirected eventually, but that cost some time.",
          "evidence_explanation": "The outcome confirms that the initial category was wrong, and the participant attributes redirection cost directly to the misfiled queue decision."
        }
      ],
      "correction_or_counterevidence": "Time pressure and reliance on a familiar workflow may have contributed to the routing choice, but the explicit use of superficial category fit and the ignored contrary advisory cue support the representativeness mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided context directly addressed the representativeness heuristic; classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "framing effect",
      "alternative_labels": [
        "loss aversion",
        "gain/loss framing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Decisions change depending on whether outcomes are described or mentally represented as losses or gains; losses typically exert a stronger influence on urgency and risk acceptance.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Emergency change window justification",
      "decision_point_description": "Deciding how to justify and whether to request an emergency business-hours patching window.",
      "affected_reasoning_operation": "Risk-benefit evaluation and urgency judgment",
      "bias_specific_mechanism": "The participant represented the same EPSS probability and customer disruption in loss terms—contract exposure, reputational harm, audit findings—making the patch feel more urgent than when the same underlying numbers were considered in gain or routine-advance terms.",
      "manifestation_in_interview": "The participant explicitly stated that thinking through potential losses made the change feel like it had to move now, while a gain-framed version would not have felt as urgent.",
      "effect_on_reasoning_or_decision": "He wrote the emergency-window justification around potential losses, and the emergency window was approved.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast.",
          "evidence_explanation": "The justification was structured around a loss frame rather than probabilities or gains."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The EPSS score put it at moderate probability, comparable to a handful of things we've handled on the normal weekend schedule over the past year. Not in the exceptional range.",
          "evidence_explanation": "This establishes that the underlying probability did not independently require the urgent loss-framed conclusion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, that's fair. When I sat down to write it, thinking through what we'd lose if it went wrong — the contract, the reputation hit, the audit exposure — made it feel like this had to move now. If I'd framed the same numbers around just getting ahead of the patch cycle or keeping things running smoothly, it probably wouldn't have felt as urgent to me, even though the underlying EPSS score and the twenty-minute disruption were exactly the same either way.",
          "evidence_explanation": "The participant explicitly contrasts loss and gain frames and confirms that framing changed his own urgency judgment."
        }
      ],
      "correction_or_counterevidence": "The participant also noted that worst-case framing is usually what gets approvals in the organization, suggesting a persuasive or institutional norm may partly explain the framing. However, he separately reports that the loss frame changed his own perception of urgency.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided context directly addressed framing effects or loss aversion; classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency effect",
        "automation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient verification or monitoring of automated system output due to overtrust in the automation, leading to incomplete information sampling.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final scope confirmation for patch target list",
      "decision_point_description": "Choosing which systems to include in the CVE patch ticket based on the scanner dashboard output.",
      "affected_reasoning_operation": "Completeness verification and target scoping",
      "bias_specific_mechanism": "The participant treated the scanner dashboard's default output as the complete list of vulnerable systems and did not manually cross-check the asset inventory, reflecting incomplete information sampling due to overreliance on the automated tool.",
      "manifestation_in_interview": "The participant said the scanner's list is usually what the team works from and that he treated it as the full picture; a manual cross-check would have caught three additional hosts.",
      "effect_on_reasoning_or_decision": "The ticket was scoped to two hosts and closed, while one missed host was later found still vulnerable in a follow-up audit scan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out.",
          "evidence_explanation": "The decision to close the ticket was based on the automated dashboard output alone."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture.",
          "evidence_explanation": "This shows overtrust in the scanner's default output as a complete and sufficient picture, a core feature of automation complacency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A manual cross-check would have caught it, but with the clock running down, the scanner's output was what I had in front of me and it looked complete.",
          "evidence_explanation": "A verification step was available and would have revealed missed systems, confirming that incomplete verification rather than forced reliance drove the result."
        }
      ],
      "correction_or_counterevidence": "Time pressure and standard operational reliance on the scanner are legitimate contextual factors, but the availability of a simple manual cross-check and the mistaken perception that the tool output was complete support a complacency-based explanation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Parasuraman and Manzey (2010) material defines the complacency effect as incomplete sampling of information needed for automation verification, directly matching this behavior.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Analyses of informationsampling behavior revealed that half of the participants made this commission error because of a clear complacency effect, as reflected in an incomplete sampling of information needed for automation verification.",
          "mechanism_supported_by_source": "The source operationalizes complacency as incomplete information sampling needed to verify automation output.",
          "relevance_to_this_occurrence": "The participant's failure to cross-check the scanner output against the asset inventory mirrors the source's description of automation complacency."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "automation complacency",
      "alternative_labels": [
        "cry-wolf effect",
        "inattentional blindness"
      ],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Ignoring low-confidence SIEM privilege-escalation alert",
      "supporting_interview_quote": "That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on.",
      "plausible_mechanism": "Repeated exposure to low-confidence false-positive alert labels may have produced complacency or cry-wolf effects, and focused attention on the inventory cross-reference may have reduced processing of other dashboard information.",
      "why_not_identified": "The evidence is ambiguous because relying on historical false-positive experience can be a reasonable triage heuristic, and the transcript does not confirm a distinct cognitive bias mechanism rather than ordinary attentional prioritization under competing task demands."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was available only for automation complacency; availability, representativeness, and framing classifications rely on established general cognitive-science knowledge.",
    "The analysis is based on retrospective self-report, which may itself be affected by recall biases or hindsight reconstruction.",
    "Several decisions occurred under time pressure and workload constraints, making it difficult to fully isolate bias from bounded rational adaptation or legitimate operational triage."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm — this is for internal process research, not a performance review, and you can decline to answer anything. Okay? Participant: Yeah, that's fine. Interviewer: Can you tell me a bit about your role? Participant: I'm a vulnerability management analyst on the security operations team. I triage scanner findings, vendor advisories, coordinate patch timelines with IT ops, and escalate anything that looks like active exploitation to incident response. I also chase our open findings backlog for compliance reporting. Interviewer: Let's talk about the CVE that came in a few weeks back. Walk me through what happened. Participant: It was mid-morning when a vendor advisory landed — a new CVE, CVSS 9.8, remote code execution, affecting our internet-facing authentication API. At the same time I had roughly forty open findings from the previous week's scan sitting in my queue, with forty-eight hours until our compliance audit report was due. One backlog item was an unpatched database server with excessive service-account privileges, open ninety-plus days. And the week before, there'd been a big breach in the news — a VPN appliance that hadn't been patched — it caused a mess for that company and was all over our internal Slack. Interviewer: When the new CVE came in, what did you do first? Participant: My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere. I moved it to the top of the queue and started routing it into our standard remediation workflow. The database finding stayed where it was. Interviewer: Where did the routing go? Participant: Into our web-application remediation queue. Honestly, when I saw 'authentication' and 'internet-facing' together, my head just went straight to the same kind of injection-style tickets that make up most of what crosses my desk — that's the pattern I see constantly, so it's the one that came to mind first. There was a line in the advisory pointing more toward the API-gateway team being the better owner, but I didn't stop on it long enough to change course, and it went into the usual queue. Interviewer: Did you look closely at the advisory's technical detail before routing it? Participant: I skimmed it — saw 'authentication,' saw 'internet-facing,' saw the CVSS score, and that was enough to know it needed to move fast. I didn't dig into the exploit chain right away because time was tight. Interviewer: Later you found it wasn't quite a standard web-app issue? Participant: Right — it turned out to be an authentication bypass in the API gateway, a different exploit path than the injection-style stuff that queue usually handles. It got redirected eventually, but that cost some time. Interviewer: Going back to that first decision — the new CVE and the ninety-day-old database finding were competing for urgency. What made the new one win? Participant: Honestly, it felt more urgent. The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull. Interviewer: If you'd ranked them purely on asset criticality and exposure, independent of the news, how would that have gone? Participant: The database server probably deserved more attention than I gave it. It ended up flagged by the audit team afterward as our most severe open item. But at the time, the CVE felt like the more pressing thing. Interviewer: Later that day you were cross-referencing the CVE against the asset inventory when something else came up. Participant: Yeah, while going host by host through the inventory, the SIEM threw an alert — 'privilege escalation, low confidence' — on an internal box. That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on. Interviewer: Was there anything specific in that alert that stood out? Participant: There was a log entry with a lateral-movement timestamp that was a little unusual. I registered it existed, but I was heads-down trying to finish the asset match, so I didn't stop to dig in. Interviewer: Was there anything else on that dashboard view at the time? Participant: [pause] I'd have to think about that. I was really focused on the inventory cross-reference right then. Interviewer: There was an anomalous outbound traffic entry flagged on that same host, visible in the same panel. Do you recall it? Participant: I don't specifically remember it. I was scrolling through host records, not scanning that side panel. It's possible it was there and I just didn't register it — my attention was on matching CVE-affected assets, not general alert triage. Interviewer: That entry was later linked to a confirmed low-level compromise on that host. Does that change how you see the decision to move past the alert? Participant: It's easy to say now I should've stopped. At the time, given how often that label turns out to be routine, continuing with the task in front of me felt reasonable. I didn't have a strong signal telling me to drop what I was doing. Interviewer: Let's talk about the change window request. What went into that? Participant: IT ops needed written justification to approve an emergency window during business hours instead of the weekend cycle, since patching would disrupt customer transactions for about twenty minutes. I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast. Interviewer: What did the exploitation data actually say? Participant: The EPSS score put it at moderate probability, comparable to a handful of things we've handled on the normal weekend schedule over the past year. Not in the exceptional range. Interviewer: So the justification leaned more on what the company could lose than on that probability figure? Participant: Yeah, that's fair. When I sat down to write it, thinking through what we'd lose if it went wrong — the contract, the reputation hit, the audit exposure — made it feel like this had to move now. If I'd framed the same numbers around just getting ahead of the patch cycle or keeping things running smoothly, it probably wouldn't have felt as urgent to me, even though the underlying EPSS score and the twenty-minute disruption were exactly the same either way. Interviewer: Did it work? Participant: It did — they approved the window. Though nothing was actually observed exploiting that CVE the following week, so it's hard to say in hindsight whether the urgency was fully warranted. Interviewer: Last decision point — finalizing which systems to patch. Participant: The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out. Interviewer: Did you check the asset inventory outside that default view? Participant: Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture. Interviewer: There were actually three more hosts with the same vulnerable library, tagged under a different asset category, visible in the inventory with a manual filter change. Participant: One of those turned up still vulnerable in the follow-up audit scan a week later. A manual cross-check would have caught it, but with the clock running down, the scanner's output was what I had in front of me and it looked complete. Interviewer: If the VPN breach hadn't been in the news that week, would you have triaged the CVE the same way? Participant: Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding. Interviewer: If the scanner had surfaced five hosts instead of two, would scoping have gone differently? Participant: Probably — I'd have just patched whatever the tool showed me. I wasn't second-guessing whether the list was complete. Interviewer: Anything you'd flag differently now? Participant: The outbound traffic entry, for sure. And maybe relying less on how an alert label has resolved in the past versus what's specifically in front of me each time. Interviewer: If you had to write that justification again today, would you frame it differently? Participant: I might lead with the actual numbers instead of the worst-case story. Though the worst-case framing is usually what gets things approved quickly around here. Interviewer: That's really helpful, thank you. Participant: No problem, happy to help.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.65s · gen 236.70s · total 241.9s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0281 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0242 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0224 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0204 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0202 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
9. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0187 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0187 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **Lyell Automation bias and verification complexity.pdf** — 0.0187 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0178 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0178 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
15. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0175 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0174 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0165 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
18. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
20. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
22. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
23. **Goddard et al. (2011) Automation bias_a systematic review of frequency, effect mediators, and mitigators.pdf** — 0.0162 (rrf) — _## Jeremy C Wyatt ’ s expertise were considered. fi ed 14457 research papers REVIEW AIM AND OBJE_
24. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0161 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
25. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0160 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
26. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0160 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
27. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0160 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
28. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0158 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
30. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0157 (rrf) — _# across domains and different parts of the search process. to help inform their opinions \[ 45 _
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
33. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0152 (rrf) — _### cKniff 2004 ; Radley et al., 2013 and reporting others about medication errors, and it foste_
34. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0150 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
35. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0149 (rrf) — _### cKniff study, we focus on stress as stimuli perceived by individuals in the environment and _
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
37. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0147 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
38. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0146 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
39. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0145 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
40. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0144 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
41. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0144 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0141 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0140 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 394 when the aid p_
47. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision Projection) method , which entails from time to time projecting bombs onto the Xra_
48. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0139 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of one interview transcript for affirmative evidence of cognitive biases in security operations decision-making. No bias is inferred from poor outcomes or time pressure alone."
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
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "framing effect",
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
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments of likelihood, frequency, or urgency are influenced by how easily examples come to mind, especially salient or recent examples.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Prioritizing the new CVE versus the older database finding",
      "decision_point_description": "Choosing which vulnerability to handle first under an audit deadline.",
      "affected_reasoning_operation": "Urgency judgment and vulnerability prioritization",
      "bias_specific_mechanism": "The fresh, salient VPN breach news story made the internet-facing CVE feel especially urgent and easy to call to mind, so the participant prioritized it over an older high-privilege database finding that may have deserved at least equal attention.",
      "manifestation_in_interview": "The participant moved the new CVE to the top of the queue and left the database finding where it was, later acknowledging that the recent breach story likely shaped how quickly he moved past the database finding.",
      "effect_on_reasoning_or_decision": "The availability of the recent breach example inflated the subjective urgency of the new CVE and contributed to under-attending to the older database finding.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere. I moved it to the top of the queue and started routing it into our standard remediation workflow. The database finding stayed where it was.",
          "evidence_explanation": "The participant immediately links the new CVE to the recent breach profile and uses that resemblance to justify prioritization."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull.",
          "evidence_explanation": "This explicitly contrasts the easy salience of the recent breach story with the older database finding, showing availability-like influence on urgency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding.",
          "evidence_explanation": "The participant acknowledges the news story shaped the triage decision, supporting the identified mechanism."
        }
      ],
      "correction_or_counterevidence": "The CVE was genuinely critical, internet-facing, and severe, so prioritizing it could be justified on objective grounds independent of the news story. The participant also recognized in hindsight that the database finding may have deserved more attention.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was unavailable; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias",
        "prototype bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging or categorizing a case by its similarity to a familiar prototype or typical example, while underweighting specific diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Routing the new CVE to a remediation queue",
      "decision_point_description": "Selecting the initial remediation queue and owner for the new CVE.",
      "affected_reasoning_operation": "Categorization and queue assignment",
      "bias_specific_mechanism": "The terms \"authentication\" and \"internet-facing\" resembled the familiar injection-style web-app tickets that dominate the participant's workload, leading him to classify the new CVE by that prototype rather than attending to the advisory's API-gateway-specific diagnostic line.",
      "manifestation_in_interview": "The participant routed the CVE into the usual web-app remediation queue despite a line in the advisory pointing toward the API-gateway team. It was later redirected after being recognized as an authentication bypass in the API gateway.",
      "effect_on_reasoning_or_decision": "Prototype-based categorization produced an initial misroute and delayed correct remediation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, when I saw 'authentication' and 'internet-facing' together, my head just went straight to the same kind of injection-style tickets that make up most of what crosses my desk — that's the pattern I see constantly, so it's the one that came to mind first.",
          "evidence_explanation": "The participant describes using the familiar injection-style ticket prototype as the basis for categorization."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a line in the advisory pointing more toward the API-gateway team being the better owner, but I didn't stop on it long enough to change course, and it went into the usual queue.",
          "evidence_explanation": "Specific diagnostic information was available but underweighted relative to the familiar prototype."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Right — it turned out to be an authentication bypass in the API gateway, a different exploit path than the injection-style stuff that queue usually handles. It got redirected eventually, but that cost some time.",
          "evidence_explanation": "This confirms the classification did not match the actual technical nature of the issue and caused delay."
        }
      ],
      "correction_or_counterevidence": "The participant was under time pressure and skimmed the advisory, so the misroute may also reflect workload rather than a purely cognitive classification bias. The error was eventually corrected.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was unavailable; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "expectation bias",
        "confirmation-seeking"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, or favor information consistent with one's prior expectations while underweighting disconfirming or contradictory signals.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Responding to a low-confidence SIEM alert during asset matching",
      "decision_point_description": "Whether to stop and investigate a low-confidence SIEM alert or continue the asset-matching task.",
      "affected_reasoning_operation": "Threat assessment and alert triage",
      "bias_specific_mechanism": "The participant's prior expectation that low-confidence SIEM alerts are almost always routine led him to terminate information seeking and not evaluate an unusual lateral-movement timestamp that was incompatible with that expectation.",
      "manifestation_in_interview": "The participant saw the alert, noted the familiar label, and moved on without digging into the unusual log entry. The host was later linked to a confirmed low-level compromise.",
      "effect_on_reasoning_or_decision": "The alert was dismissed quickly, and an unusual indicator was not investigated, contributing to a missed or delayed response.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on.",
          "evidence_explanation": "The participant's prior belief made the alert appear routine and reduced further scrutiny."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a log entry with a lateral-movement timestamp that was a little unusual. I registered it existed, but I was heads-down trying to finish the asset match, so I didn't stop to dig in.",
          "evidence_explanation": "He noticed but did not process a potentially disconfirming detail, consistent with confirmation-biased information processing under prior expectation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It's easy to say now I should've stopped. At the time, given how often that label turns out to be routine, continuing with the task in front of me felt reasonable. I didn't have a strong signal telling me to drop what I was doing.",
          "evidence_explanation": "This reinforces that the prior false-positive experience dominated the interpretation, even though an unusual signal was present."
        }
      ],
      "correction_or_counterevidence": "The alert was explicitly labeled low-confidence and often turned out to be routine, so continuing the primary task may have been a defensible triage judgment. Time pressure and high workload provide a plausible non-bias explanation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was unavailable; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "framing effect",
      "alternative_labels": [
        "loss framing",
        "valence framing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A change in judgment or decision arising from how equivalent information is framed, particularly whether outcomes are presented as losses or gains.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Writing the emergency change window justification",
      "decision_point_description": "Choosing whether to frame the change request around potential losses or more neutral operational/statistical grounds.",
      "affected_reasoning_operation": "Urgency judgment and persuasive justification",
      "bias_specific_mechanism": "The participant framed the same EPSS/disruption numbers in terms of potential losses—contract, reputation, audit exposure—which increased his subjective sense of urgency compared with a neutral or gain-like framing.",
      "manifestation_in_interview": "The participant wrote the justification emphasizing what the organization stood to lose and later said a different framing would likely have felt less urgent even with identical underlying numbers.",
      "effect_on_reasoning_or_decision": "The loss-framed presentation made the change request feel as though it required immediate action, contributing to approval of an emergency window.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast.",
          "evidence_explanation": "The participant selected a loss-oriented framing for the change request."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I sat down to write it, thinking through what we'd lose if it went wrong — the contract, the reputation hit, the audit exposure — made it feel like this had to move now. If I'd framed the same numbers around just getting ahead of the patch cycle or keeping things running smoothly, it probably wouldn't have felt as urgent to me, even though the underlying EPSS score and the twenty-minute disruption were exactly the same either way.",
          "evidence_explanation": "This explicitly describes how equivalent information produced different urgency depending on frame, the core mechanism of the framing effect."
        }
      ],
      "correction_or_counterevidence": "The CVE was severe and patching was defensible, so the emergency request was not necessarily unjustified. The participant also noted that loss framing tends to get approvals quickly, so it may have been partly a strategic communication choice.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was unavailable; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency",
        "automation-induced complacency",
        "automation overreliance"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient verification or monitoring of automated system output due to overtrust or reliance on the automation, often resulting in incomplete information sampling.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Finalizing which systems to patch from scanner output",
      "decision_point_description": "Determining whether the default scanner dashboard list was complete before closing the patch ticket.",
      "affected_reasoning_operation": "Verification and scoping decision",
      "bias_specific_mechanism": "The participant accepted the scanner's default dashboard view as the complete population of vulnerable hosts and did not cross-check asset inventory or alternative filters, consistent with under-sampling information needed to verify automation output.",
      "manifestation_in_interview": "He scoped the ticket to the two hosts shown by the scanner and closed it out. Three additional vulnerable hosts under a different asset category were missed, and one was later found still vulnerable in a follow-up audit scan.",
      "effect_on_reasoning_or_decision": "Incomplete verification of the automated scanner output led to an under-scoped patch ticket and missed vulnerable systems.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out.",
          "evidence_explanation": "The participant used the automation output as the sole basis for scoping without additional verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture.",
          "evidence_explanation": "This directly states reliance on the tool's default output as if it were complete, a hallmark of automation complacency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "One of those turned up still vulnerable in the follow-up audit scan a week later. A manual cross-check would have caught it, but with the clock running down, the scanner's output was what I had in front of me and it looked complete.",
          "evidence_explanation": "The participant acknowledges that available verification steps would have caught the missed hosts, but the tool output appeared complete enough to stop searching."
        }
      ],
      "correction_or_counterevidence": "Time pressure and standard workflow practice contributed to reliance on the scanner's default view. The scanner did show the relevant library signature for the hosts it surfaced; discovering the additional hosts required a manual filter change.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support was available for the automation-complacency mechanism and is included below.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it. Participants were provided independent access (via mouse click) to all relevant system information (e.g., tank levels, flow rates at different valves, history graphs displaying the time course of system parameters), needed to verify the aid’s diagnoses. This procedure allowed the investigators to assess the level of operator complacency in interaction with the aid by contrasting the actual information sampling behavior of operators with a “normative model” of optimal behavior. According to this logic, any participant who accessed just the information appropriate to verify a given diagnosis before accepting it was regarded as showing noncomplacent (eutactic) behavior in interaction with the aid. However, participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "The source defines complacency as accepting automation output after sampling less verification information than necessary.",
          "relevance_to_this_occurrence": "The participant accepted the scanner's default output as complete without checking inventory filters or alternative asset categories, which mirrors the insufficient verification behavior described in the source."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "inattentional blindness",
      "alternative_labels": [
        "attentional tunneling",
        "selective attention"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Reviewing asset inventory while the alert and outbound traffic entry were visible",
      "supporting_interview_quote": "I don't specifically remember it. I was scrolling through host records, not scanning that side panel. It's possible it was there and I just didn't register it — my attention was on matching CVE-affected assets, not general alert triage.",
      "plausible_mechanism": "Attention allocated to the inventory matching task may have reduced processing of unattended side-panel information, consistent with inattentional blindness or attentional tunneling.",
      "why_not_identified": "The transcript shows ordinary focused attention under time pressure rather than a distinct bias-specific reasoning distortion, so it does not meet the threshold for identification."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was limited; several labels are based on general cognitive-science knowledge rather than the provided passages.",
    "The analysis relies on retrospective self-report, which may include rationalization or imperfect recall.",
    "Several episodes have plausible non-bias explanations such as time pressure, workload, standard workflow, and organizational approval incentives.",
    "No objective system data were available to verify severity, alert content, scanner coverage, or patch outcomes."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm — this is for internal process research, not a performance review, and you can decline to answer anything. Okay? Participant: Yeah, that's fine. Interviewer: Can you tell me a bit about your role? Participant: I'm a vulnerability management analyst on the security operations team. I triage scanner findings, vendor advisories, coordinate patch timelines with IT ops, and escalate anything that looks like active exploitation to incident response. I also chase our open findings backlog for compliance reporting. Interviewer: Let's talk about the CVE that came in a few weeks back. Walk me through what happened. Participant: It was mid-morning when a vendor advisory landed — a new CVE, CVSS 9.8, remote code execution, affecting our internet-facing authentication API. At the same time I had roughly forty open findings from the previous week's scan sitting in my queue, with forty-eight hours until our compliance audit report was due. One backlog item was an unpatched database server with excessive service-account privileges, open ninety-plus days. And the week before, there'd been a big breach in the news — a VPN appliance that hadn't been patched — it caused a mess for that company and was all over our internal Slack. Interviewer: When the new CVE came in, what did you do first? Participant: My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere. I moved it to the top of the queue and started routing it into our standard remediation workflow. The database finding stayed where it was. Interviewer: Where did the routing go? Participant: Into our web-application remediation queue. Honestly, when I saw 'authentication' and 'internet-facing' together, my head just went straight to the same kind of injection-style tickets that make up most of what crosses my desk — that's the pattern I see constantly, so it's the one that came to mind first. There was a line in the advisory pointing more toward the API-gateway team being the better owner, but I didn't stop on it long enough to change course, and it went into the usual queue. Interviewer: Did you look closely at the advisory's technical detail before routing it? Participant: I skimmed it — saw 'authentication,' saw 'internet-facing,' saw the CVSS score, and that was enough to know it needed to move fast. I didn't dig into the exploit chain right away because time was tight. Interviewer: Later you found it wasn't quite a standard web-app issue? Participant: Right — it turned out to be an authentication bypass in the API gateway, a different exploit path than the injection-style stuff that queue usually handles. It got redirected eventually, but that cost some time. Interviewer: Going back to that first decision — the new CVE and the ninety-day-old database finding were competing for urgency. What made the new one win? Participant: Honestly, it felt more urgent. The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull. Interviewer: If you'd ranked them purely on asset criticality and exposure, independent of the news, how would that have gone? Participant: The database server probably deserved more attention than I gave it. It ended up flagged by the audit team afterward as our most severe open item. But at the time, the CVE felt like the more pressing thing. Interviewer: Later that day you were cross-referencing the CVE against the asset inventory when something else came up. Participant: Yeah, while going host by host through the inventory, the SIEM threw an alert — 'privilege escalation, low confidence' — on an internal box. That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on. Interviewer: Was there anything specific in that alert that stood out? Participant: There was a log entry with a lateral-movement timestamp that was a little unusual. I registered it existed, but I was heads-down trying to finish the asset match, so I didn't stop to dig in. Interviewer: Was there anything else on that dashboard view at the time? Participant: [pause] I'd have to think about that. I was really focused on the inventory cross-reference right then. Interviewer: There was an anomalous outbound traffic entry flagged on that same host, visible in the same panel. Do you recall it? Participant: I don't specifically remember it. I was scrolling through host records, not scanning that side panel. It's possible it was there and I just didn't register it — my attention was on matching CVE-affected assets, not general alert triage. Interviewer: That entry was later linked to a confirmed low-level compromise on that host. Does that change how you see the decision to move past the alert? Participant: It's easy to say now I should've stopped. At the time, given how often that label turns out to be routine, continuing with the task in front of me felt reasonable. I didn't have a strong signal telling me to drop what I was doing. Interviewer: Let's talk about the change window request. What went into that? Participant: IT ops needed written justification to approve an emergency window during business hours instead of the weekend cycle, since patching would disrupt customer transactions for about twenty minutes. I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast. Interviewer: What did the exploitation data actually say? Participant: The EPSS score put it at moderate probability, comparable to a handful of things we've handled on the normal weekend schedule over the past year. Not in the exceptional range. Interviewer: So the justification leaned more on what the company could lose than on that probability figure? Participant: Yeah, that's fair. When I sat down to write it, thinking through what we'd lose if it went wrong — the contract, the reputation hit, the audit exposure — made it feel like this had to move now. If I'd framed the same numbers around just getting ahead of the patch cycle or keeping things running smoothly, it probably wouldn't have felt as urgent to me, even though the underlying EPSS score and the twenty-minute disruption were exactly the same either way. Interviewer: Did it work? Participant: It did — they approved the window. Though nothing was actually observed exploiting that CVE the following week, so it's hard to say in hindsight whether the urgency was fully warranted. Interviewer: Last decision point — finalizing which systems to patch. Participant: The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out. Interviewer: Did you check the asset inventory outside that default view? Participant: Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture. Interviewer: There were actually three more hosts with the same vulnerable library, tagged under a different asset category, visible in the inventory with a manual filter change. Participant: One of those turned up still vulnerable in the follow-up audit scan a week later. A manual cross-check would have caught it, but with the clock running down, the scanner's output was what I had in front of me and it looked complete. Interviewer: If the VPN breach hadn't been in the news that week, would you have triaged the CVE the same way? Participant: Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding. Interviewer: If the scanner had surfaced five hosts instead of two, would scoping have gone differently? Participant: Probably — I'd have just patched whatever the tool showed me. I wasn't second-guessing whether the list was complete. Interviewer: Anything you'd flag differently now? Participant: The outbound traffic entry, for sure. And maybe relying less on how an alert label has resolved in the past versus what's specifically in front of me each time. Interviewer: If you had to write that justification again today, would you frame it differently? Participant: I might lead with the actual numbers instead of the worst-case story. Though the worst-case framing is usually what gets things approved quickly around here. Interviewer: That's really helpful, thank you. Participant: No problem, happy to help.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.65s · gen 273.51s · total 278.7s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0281 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0242 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0224 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0204 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0202 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
9. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0187 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0187 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **Lyell Automation bias and verification complexity.pdf** — 0.0187 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0178 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0178 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
15. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0175 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0174 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0165 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
18. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
20. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
22. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
23. **Goddard et al. (2011) Automation bias_a systematic review of frequency, effect mediators, and mitigators.pdf** — 0.0162 (rrf) — _## Jeremy C Wyatt ’ s expertise were considered. fi ed 14457 research papers REVIEW AIM AND OBJE_
24. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0161 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
25. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0160 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
26. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0160 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
27. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0160 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
28. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0158 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
30. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0157 (rrf) — _# across domains and different parts of the search process. to help inform their opinions \[ 45 _
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
33. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0152 (rrf) — _### cKniff 2004 ; Radley et al., 2013 and reporting others about medication errors, and it foste_
34. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0150 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
35. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0149 (rrf) — _### cKniff study, we focus on stress as stimuli perceived by individuals in the environment and _
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
37. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0147 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
38. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0146 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
39. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0145 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
40. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0144 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_
41. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0144 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0141 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0140 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 394 when the aid p_
47. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision Projection) method , which entails from time to time projecting bombs onto the Xra_
48. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0139 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of the CTA transcript. Time pressure, routine professional triage heuristics, and poor outcomes were not classified as bias unless the transcript separately evidenced a distinct bias-specific mechanism."
  },
  "identified_bias_summary": [
    {
      "bias_label": "attentional tunneling",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "cry-wolf effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "framing effect",
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
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "recency bias",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the urgency or likelihood of an event based on how easily similar instances come to mind, especially recent or vivid cases.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Prioritizing new critical CVE versus old database finding",
      "decision_point_description": "Moving the new CVE to the top of the queue and leaving the 90-day-old unpatched database finding where it was.",
      "affected_reasoning_operation": "Threat prioritization and urgency triage",
      "bias_specific_mechanism": "The fresh, widely discussed VPN breach increased the cognitive availability of unpatched internet-facing RCE incidents, making the new CVE feel disproportionately urgent compared with an older, high-severity database finding.",
      "manifestation_in_interview": "The participant explicitly links the salience of the prior week's breach to the feeling that the new CVE matched that shape and therefore won over the database finding.",
      "effect_on_reasoning_or_decision": "The CVE was selected and prioritized while the database finding, later identified by audit as the most severe open item, remained untreated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere. I moved it to the top of the queue and started routing it into our standard remediation workflow. The database finding stayed where it was.",
          "evidence_explanation": "Shows the initial urgency judgment and triage decision favoring the CVE over the database finding."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull.",
          "evidence_explanation": "Explicitly identifies the fresh breach story as the source of the pull that influenced the prioritization."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding.",
          "evidence_explanation": "The participant himself attributes his triage speed and urgency partly to the recent news story."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledges the database server probably deserved more attention and was flagged by audit, but this is retrospective and did not correct the initial triage decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported the availability heuristic; the label is applied from general cognitive-science knowledge with disclosure.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "prototype bias",
        "premature closure",
        "availability of frequent ticket type"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging a new case by its superficial resemblance to a familiar category or prototype while underweighting diagnostic information that does not fit that category.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Routing the new CVE into the web-application remediation queue",
      "decision_point_description": "Classifying the CVE as a standard injection-style web-app ticket and routing it to that queue despite advisory information pointing to the API-gateway team.",
      "affected_reasoning_operation": "Incident categorization and ticket routing",
      "bias_specific_mechanism": "The terms internet-facing and authentication triggered the highly available mental prototype of common injection-style web-application tickets; the participant did not use the technical advisory detail about the API-gateway to adjust his initial classification.",
      "manifestation_in_interview": "The participant states that his head went straight to the pattern he sees constantly and that he did not stop on the line pointing to the API-gateway team.",
      "effect_on_reasoning_or_decision": "The CVE was misrouted into the usual web-app queue, later requiring redirection and costing time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, when I saw 'authentication' and 'internet-facing' together, my head just went straight to the same kind of injection-style tickets that make up most of what crosses my desk — that's the pattern I see constantly, so it's the one that came to mind first.",
          "evidence_explanation": "Demonstrates prototype-based classification driven by the most familiar pattern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a line in the advisory pointing more toward the API-gateway team being the better owner, but I didn't stop on it long enough to change course, and it went into the usual queue.",
          "evidence_explanation": "Shows diagnostic technical information was available but not used to adjust the initial categorization."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Right — it turned out to be an authentication bypass in the API gateway, a different exploit path than the injection-style stuff that queue usually handles. It got redirected eventually, but that cost some time.",
          "evidence_explanation": "Confirms the representative classification was incorrect and had an operational cost."
        }
      ],
      "correction_or_counterevidence": "The ticket was eventually redirected, but only after the incorrect routing decision produced delay.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressed the representativeness heuristic; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "cry-wolf effect",
      "alternative_labels": [
        "alarm fatigue",
        "false-alarm effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Reduced responsiveness to an alarm or warning after repeated false or low-validity alerts.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "SIEM low-confidence privilege-escalation alert triage",
      "decision_point_description": "Deciding to move past the SIEM alert without investigating the unusual lateral-movement timestamp.",
      "affected_reasoning_operation": "Alert triage and anomaly investigation decision",
      "bias_specific_mechanism": "Frequent prior false alarms under the same label led the participant to treat the new alert as routine, reducing attention to specific diagnostic information in the alert.",
      "manifestation_in_interview": "The participant states the label comes up a lot and is almost always nothing, saw the same label he had seen many times, and moved on despite registering an unusual log entry.",
      "effect_on_reasoning_or_decision": "The SIEM alert was not investigated at the time, and the host was later linked to a confirmed low-level compromise.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on.",
          "evidence_explanation": "Shows the learned non-response to a frequently false label, the core of the cry-wolf effect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a log entry with a lateral-movement timestamp that was a little unusual. I registered it existed, but I was heads-down trying to finish the asset match, so I didn't stop to dig in.",
          "evidence_explanation": "Demonstrates that a specific diagnostic cue was noticed but was not allowed to interrupt the learned routine response."
        }
      ],
      "correction_or_counterevidence": "The participant maintains that continuing felt reasonable at the time given the alert's usual validity, which is a plausible competing non-bias explanation; the labeling is therefore moderate rather than high confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported the cry-wolf effect or alarm fatigue; the label is applied from general human-factors/cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "attentional tunneling",
      "alternative_labels": [
        "inattentional blindness",
        "task fixation",
        "selective attention bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Narrowing of attention to a primary task such that peripheral but potentially important information is not perceived or registered.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Monitoring dashboard while cross-referencing CVE-affected assets",
      "decision_point_description": "Failing to register or act on an anomalous outbound traffic entry on the same panel while focused on host-by-host inventory matching.",
      "affected_reasoning_operation": "Visual attention allocation during security monitoring",
      "bias_specific_mechanism": "Attention was tightly focused on matching CVE-affected assets in the host inventory, producing reduced processing of the adjacent side-panel alert.",
      "manifestation_in_interview": "The participant says he was scrolling through host records, not scanning the side panel, and that it was possible the entry was present but he did not register it.",
      "effect_on_reasoning_or_decision": "The outbound traffic entry was missed and later linked to a confirmed low-level compromise on the host.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I don't specifically remember it. I was scrolling through host records, not scanning that side panel. It's possible it was there and I just didn't register it — my attention was on matching CVE-affected assets, not general alert triage.",
          "evidence_explanation": "Shows the attention allocation that likely prevented registration of the outbound traffic entry."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I was really focused on the inventory cross-reference right then.",
          "evidence_explanation": "Directly states the narrowed attentional focus."
        }
      ],
      "correction_or_counterevidence": "The participant cannot confirm the entry was visible, and the finding depends partly on interviewer-provided information that the entry was visible in the same panel.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported attentional tunneling; the label is applied from general cognitive-science/human-factors knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "framing effect",
      "alternative_labels": [
        "loss aversion",
        "risky-choice framing effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Evaluating equivalent information differently depending on whether it is framed in terms of losses versus gains or neutral terms.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Writing justification for emergency change window",
      "decision_point_description": "Framing the patch request around potential losses rather than around the same objective EPSS/probability and operational trade-offs.",
      "affected_reasoning_operation": "Risk/urgency judgment and persuasive justification",
      "bias_specific_mechanism": "Mentally simulating losses persuaded the participant that the patch had to move immediately, despite the same underlying numerical probability and disruption remaining unchanged.",
      "manifestation_in_interview": "The participant says the loss-framed justification made it feel urgent, and that a gain/neutral framing of the same numbers would not have felt as urgent.",
      "effect_on_reasoning_or_decision": "The emergency change window was approved even though exploitation probability was moderate and comparable to routine weekend-scheduled items.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast.",
          "evidence_explanation": "Shows the loss-based framing used in the justification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I sat down to write it, thinking through what we'd lose if it went wrong — the contract, the reputation hit, the audit exposure — made it feel like this had to move now.",
          "evidence_explanation": "Shows the framing affected the participant's own urgency judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd framed the same numbers around just getting ahead of the patch cycle or keeping things running smoothly, it probably wouldn't have felt as urgent to me, even though the underlying EPSS score and the twenty-minute disruption were exactly the same either way.",
          "evidence_explanation": "Explicitly identifies that the information was equivalent but framing changed the subjective urgency."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledges that the EPSS score was moderate and not exceptional, and that in hindsight nothing exploited the CVE the following week; however, the framing still influenced the decision at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported framing effects or loss aversion; the label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency",
        "overreliance on automation",
        "automation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient verification or information sampling of automated output because it is trusted as complete or correct.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scoping the patch ticket from the scanner's default dashboard view",
      "decision_point_description": "Using the scanner's two-host default list to scope the ticket and closing it without cross-checking the asset inventory.",
      "affected_reasoning_operation": "Vulnerability scope determination and ticket finalization",
      "bias_specific_mechanism": "Overreliance on the automated scanner's default output as the full set of vulnerable hosts, leading to insufficient manual verification of scope.",
      "manifestation_in_interview": "The participant said he treated the scanner list as the full picture, did not second-guess whether the list was complete, and did not cross-check the asset inventory.",
      "effect_on_reasoning_or_decision": "Three additional vulnerable hosts were omitted; at least one remained vulnerable in the follow-up audit scan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out.",
          "evidence_explanation": "Shows acceptance of automated default output as the complete scope."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture.",
          "evidence_explanation": "Demonstrates routine overreliance on the scanner output instead of cross-checking."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I wasn't second-guessing whether the list was complete.",
          "evidence_explanation": "Directly indicates insufficient verification of the automated tool output."
        }
      ],
      "correction_or_counterevidence": "A manual cross-check would have caught the additional hosts, but this was recognized only afterward; time pressure was present but the complacent acceptance of scanner completeness is the evidenced mechanism.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Parasuraman and Manzey passage supports classifying insufficient verification of an automated aid's output as complacency.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "However, participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "Automation complacency is operationally defined as sampling less information than necessary to verify automated output.",
          "relevance_to_this_occurrence": "The participant sampled only the scanner's default list and did not cross-check the asset inventory, directly paralleling insufficient verification of automation output."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was available only for automation complacency; the other labels are applied from general cognitive-science/human-factors knowledge with disclosure.",
    "The attentional tunneling and cry-wolf findings rely partly on participant recollection and interviewer-provided information about dashboard visibility.",
    "Time pressure is present throughout the transcript, but it was not treated as bias unless a distinct bias-specific mechanism was separately evidenced."
  ]
}

