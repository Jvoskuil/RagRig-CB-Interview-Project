# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a cognitive task analysis session—I'll be asking about a specific incident you worked through, and I'd like your candid recollection of how you reasoned through it, not a polished after-the-fact summary. Everything stays anonymized. Is that okay with you? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me your role and what you were responsible for during this incident? Participant: I lead a five-person team on our internal analytics platform—basically the tooling our support organization uses to look up customer accounts, usage history, that kind of thing. I own delivery for that dashboard and I report into the VP of Engineering. During this period I was accountable for keeping the platform stable and also for a demo we had coming up for leadership. Interviewer: Can you walk me through what first alerted you to a problem? Participant: Load times on the dashboard started creeping up—support tickets came in complaining pages were taking six, seven seconds instead of two. Over about two weeks it basically tripled. We hadn't touched much in that subsystem recently except our caching layer, which we'd built in-house—we call it QuickCache—about eight months earlier. Interviewer: What did you do first? Participant: I had two real options—run broad instrumentation across the whole stack to be safe, or go straight at QuickCache since it was the most recent change and the timing lined up. We were also getting pressure from the support lead because tickets kept climbing, so I didn't want to spend a week doing exhaustive profiling everywhere. I told the team to profile QuickCache specifically first, since it was the most likely suspect given the timing, and if that came back clean we'd widen the net. Interviewer: What came out of that? Participant: Profiling confirmed QuickCache was adding real latency under high load—invalidation was firing more than it should, forcing extra database round-trips. It also surfaced a separate, unrelated issue: a missing index on one of the support tables. Neither of those was hugely surprising, but it did mean two independent things needed fixing, not one. Interviewer: How did the investigation affect team workload? Participant: Priya, who originally built QuickCache, took point on diagnosing the invalidation logic. Dev, one of our other senior engineers, has also worked deep in that code. Everyone else picked up the index fix and other tickets. That's roughly how the two weeks split. Interviewer: Let's step through it chronologically. After profiling confirmed the QuickCache issue, what was the next major decision? Participant: That's where it got harder. QuickCache had taken us about eight months to build and stabilize—three separate patch rounds just to get it production-ready in the first place. Priya was adamant we were close, that one more targeted patch to the invalidation logic would fix it. On the other hand, there's a mature Redis-backed option out there that could probably replace QuickCache in about a sprint, with a track record we could actually point to. Interviewer: What did you decide? Participant: I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up. I figured one more focused patch, with the team that knows it best, would get us there. Interviewer: What information did you rely on most heavily for that call? Participant: Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily. Interviewer: What happened after that decision? Participant: The patch only bought us about fifteen percent improvement. Not enough to hit the demo deadline. And the extra sprint stretched the team thin on top of everything else going on. Interviewer: Third decision point—who owned the urgent fix at that stage? Participant: Right, so at this point we're down to days, not weeks. Dev has the deepest knowledge of QuickCache internals, but Dev had also been at the center of a production outage about three weeks earlier—a rushed deploy under pressure that caused a real incident, though the postmortem showed it was handled well and fixed fast. Marcus was the other option; he's been solid but has missed several deadlines over the past year, nothing dramatic, just a slower, steadier pattern of slipping. Interviewer: What did you decide, and why? Participant: I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet. Interviewer: How did that play out? Participant: Handoff was messy—Dev had context Marcus didn't, so there was friction getting him up to speed, and the fix took longer than it would have with Dev leading it outright. Interviewer: Looking back, how did you weigh Dev's eighteen months of strong delivery against that one incident? Participant: I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either. Interviewer: With three days left before the demo, what did you decide about reporting status? Participant: Latency was better but not fully resolved. I could've asked to push the demo, shipped quietly and hoped nobody noticed the remaining lag, or just told leadership straight where things stood. I went with transparency—laid out what was fixed, what wasn't, and proposed a follow-up sprint with monitoring in place. They accepted that. Interviewer: What was the reasoning behind choosing that option over delaying the demo? Participant: Delaying felt like it would cost more politically than it would gain technically—the partial fix was real progress, and monitoring would catch anything that slipped. Hiding it wasn't really on the table once I thought about it seriously. Interviewer: If you'd had the profiling data suggesting a structural rework earlier, would that have changed your patch-versus-switch decision? Participant: Possibly. If I'd seen it that clearly before committing the extra sprint, I might have pushed harder for the parallel evaluation option instead. Interviewer: If Dev's outage had happened a year earlier rather than three weeks before this decision, would you have assigned the fix differently? Participant: Probably, yeah. With more distance from it, I likely would have just given it to him outright given his familiarity with the system. Interviewer: Anything you'd tell a peer facing a similar in-house-build-versus-alternative call? Participant: Try to separate how much you've already put into something from what it's actually going to cost you going forward. Easier said than done when your team's pride and expertise are wrapped up in it.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.86s · gen 64.27s · total 68.5s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0280 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0263 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0245 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0224 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0208 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0198 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0197 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
9. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0197 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
10. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0193 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
11. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0193 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0187 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0185 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
15. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0184 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
16. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0184 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study anchor. Anchoring bias is_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0181 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0173 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
20. **Lyell Automation bias and verification complexity.pdf** — 0.0172 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0169 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0166 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
25. **Human_Cognitive_Bias_Identification_for.pdf** — 0.0163 (rrf) — _# Systems ISSN: 2277-3878, Volume-8 Issue-6, March 2020 C. Cognitive Bias Identification In Scen_
26. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0162 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
27. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0160 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0159 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
33. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0155 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
37. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0147 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
40. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0144 (rrf) — _# So This is it? d with sufficient clari , 2003; Berger to bridge the gap is it that we retrieve_
41. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
42. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0141 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
43. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
44. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0140 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
45. **Hallihan_etal_DTM_12.pdf** — 0.0140 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## ion of Language mu ndane forces operating over long periods of time. To this assumption, Pink_
47. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0138 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0137 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0136 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
50. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0135 (rrf) — _# ( " = 0 . 44 ) . \[1\] GaganBansal,BesmiraNushi,EceKamar,WalterSLasecki,DanielSWeld,andEricHor_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Evaluated the participant's retrospective reasoning across three discrete decision episodes: initial diagnostic targeting, build-versus-replace investment choice, and urgent-fix ownership assignment. No experimental condition or benchmark hypothesis was assumed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
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
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue investing in a course of action because of previously invested, irrecoverable resources, rather than evaluating its expected future costs and benefits independently of those sunk costs.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "QuickCache patch-versus-replace decision",
      "decision_point_description": "After profiling confirmed the QuickCache latency issue, the participant chose whether to invest another sprint in patching the in-house QuickCache system or replace it with a mature Redis-backed alternative.",
      "affected_reasoning_operation": "Prospective cost-benefit evaluation and technology replacement decision",
      "bias_specific_mechanism": "Prior engineering time, stabilization effort, team expertise, and organizational pride associated with QuickCache were treated as reasons to continue investing, even though those investments were already sunk and could not be recovered. This caused the participant to discount the profiling evidence that the invalidation architecture itself needed rethinking.",
      "manifestation_in_interview": "The participant explicitly weighed the eight months already spent building and stabilizing QuickCache, and the specialized knowledge the team had developed, as a central reason to commit another sprint rather than switch to a mature alternative.",
      "effect_on_reasoning_or_decision": "The participant committed another sprint to patching QuickCache despite profiling data suggesting a structural rework. The patch yielded only about a fifteen percent improvement, missed the demo target, and stretched the team.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "QuickCache had taken us about eight months to build and stabilize—three separate patch rounds just to get it production-ready in the first place.",
          "evidence_explanation": "This quote establishes that the participant was centrally considering irrecoverable past investment in the system when framing the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up.",
          "evidence_explanation": "This quote directly shows the choice being driven by accumulated past investment, team identity, and fear of wasting prior effort, rather than primarily by prospective technical evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily.",
          "evidence_explanation": "This quote demonstrates that the participant consciously privileged sunk engineering time over emerging evidence that the architecture needed more fundamental change, which is the core distortion in sunk cost reasoning."
        }
      ],
      "correction_or_counterevidence": "The subsequent patch produced only a partial improvement and did not meet the demo deadline. The participant also later reflected that trying to separate past investment from forward-looking cost is hard when team pride and expertise are involved. Some preference for retaining an in-house system with team expertise could be a legitimate strategic consideration, but the transcript indicates sunk costs and difficulty abandoning the prior investment materially influenced the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved passages did not provide a direct definition or operational diagnostic for sunk cost fallacy or escalation of commitment sufficient to support the classification. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "recency effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the probability, risk, or importance of an event by the ease with which examples come to mind, often making recent or emotionally salient instances disproportionately influential.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Urgent-fix ownership assignment",
      "decision_point_description": "With days remaining before the demo, the participant chose whether Dev or Marcus should lead the urgent QuickCache fix.",
      "affected_reasoning_operation": "Risk assessment and allocation of high-stakes engineering ownership under time pressure",
      "bias_specific_mechanism": "Dev's recent production outage, which had occurred only about three weeks earlier, was mentally available and emotionally salient. This made the participant treat Dev as a higher-risk choice than Marcus, even though Dev had eighteen months of strong delivery and Marcus had a slower pattern of missed deadlines.",
      "manifestation_in_interview": "The participant explicitly stated that the recent outage was 'the thing sitting right in front of me' when making the call, while Marcus's less dramatic but objectively relevant deadline slips lacked a salient moment.",
      "effect_on_reasoning_or_decision": "The participant removed Dev from primary ownership of the urgent fix and assigned it to Marcus, despite Dev's deeper relevant expertise. The handoff was messy, created friction, and lengthened the fix.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet.",
          "evidence_explanation": "This quote shows the decision was disproportionately shaped by the freshness and salience of one recent incident rather than a balanced comparison of overall reliability."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either.",
          "evidence_explanation": "The participant explicitly contrasts a broad positive track record with a vivid recent event and acknowledges that the less salient pattern of Marcus's missed deadlines was discounted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. With more distance from it, I likely would have just given it to him outright given his familiarity with the system.",
          "evidence_explanation": "This counterfactual supports the availability interpretation: greater temporal distance from the salient event would have reduced its influence on the ownership decision."
        }
      ],
      "correction_or_counterevidence": "A recent production incident can be a legitimate risk indicator, especially under deadline pressure. However, the postmortem indicated the incident was handled and fixed quickly, and the participant himself acknowledged Dev's overall strong record and Marcus's objectively poor deadline pattern, suggesting the recent incident received excessive weight through salience and availability.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved passages mentioned recency effects in usability testing but did not directly define or operationalize the availability heuristic in this decision-making context. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a retrospective self-report, which may be affected by memory reconstruction and self-presentation; observed statements are treated as evidence of the reasoning described.",
    "Retrieved corpus passages did not directly support the two identified bias labels, so classifications rely on established cognitive-science knowledge rather than corpus-grounded operational definitions.",
    "Some elements of the decisions could also be partially explained by legitimate professional considerations, such as retaining specialized team expertise or treating a recent incident as a risk signal; the identified biases were judged to materially distort reasoning, but the evidence is not entirely free of alternative interpretation."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a cognitive task analysis session—I'll be asking about a specific incident you worked through, and I'd like your candid recollection of how you reasoned through it, not a polished after-the-fact summary. Everything stays anonymized. Is that okay with you? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me your role and what you were responsible for during this incident? Participant: I lead a five-person team on our internal analytics platform—basically the tooling our support organization uses to look up customer accounts, usage history, that kind of thing. I own delivery for that dashboard and I report into the VP of Engineering. During this period I was accountable for keeping the platform stable and also for a demo we had coming up for leadership. Interviewer: Can you walk me through what first alerted you to a problem? Participant: Load times on the dashboard started creeping up—support tickets came in complaining pages were taking six, seven seconds instead of two. Over about two weeks it basically tripled. We hadn't touched much in that subsystem recently except our caching layer, which we'd built in-house—we call it QuickCache—about eight months earlier. Interviewer: What did you do first? Participant: I had two real options—run broad instrumentation across the whole stack to be safe, or go straight at QuickCache since it was the most recent change and the timing lined up. We were also getting pressure from the support lead because tickets kept climbing, so I didn't want to spend a week doing exhaustive profiling everywhere. I told the team to profile QuickCache specifically first, since it was the most likely suspect given the timing, and if that came back clean we'd widen the net. Interviewer: What came out of that? Participant: Profiling confirmed QuickCache was adding real latency under high load—invalidation was firing more than it should, forcing extra database round-trips. It also surfaced a separate, unrelated issue: a missing index on one of the support tables. Neither of those was hugely surprising, but it did mean two independent things needed fixing, not one. Interviewer: How did the investigation affect team workload? Participant: Priya, who originally built QuickCache, took point on diagnosing the invalidation logic. Dev, one of our other senior engineers, has also worked deep in that code. Everyone else picked up the index fix and other tickets. That's roughly how the two weeks split. Interviewer: Let's step through it chronologically. After profiling confirmed the QuickCache issue, what was the next major decision? Participant: That's where it got harder. QuickCache had taken us about eight months to build and stabilize—three separate patch rounds just to get it production-ready in the first place. Priya was adamant we were close, that one more targeted patch to the invalidation logic would fix it. On the other hand, there's a mature Redis-backed option out there that could probably replace QuickCache in about a sprint, with a track record we could actually point to. Interviewer: What did you decide? Participant: I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up. I figured one more focused patch, with the team that knows it best, would get us there. Interviewer: What information did you rely on most heavily for that call? Participant: Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily. Interviewer: What happened after that decision? Participant: The patch only bought us about fifteen percent improvement. Not enough to hit the demo deadline. And the extra sprint stretched the team thin on top of everything else going on. Interviewer: Third decision point—who owned the urgent fix at that stage? Participant: Right, so at this point we're down to days, not weeks. Dev has the deepest knowledge of QuickCache internals, but Dev had also been at the center of a production outage about three weeks earlier—a rushed deploy under pressure that caused a real incident, though the postmortem showed it was handled well and fixed fast. Marcus was the other option; he's been solid but has missed several deadlines over the past year, nothing dramatic, just a slower, steadier pattern of slipping. Interviewer: What did you decide, and why? Participant: I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet. Interviewer: How did that play out? Participant: Handoff was messy—Dev had context Marcus didn't, so there was friction getting him up to speed, and the fix took longer than it would have with Dev leading it outright. Interviewer: Looking back, how did you weigh Dev's eighteen months of strong delivery against that one incident? Participant: I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either. Interviewer: With three days left before the demo, what did you decide about reporting status? Participant: Latency was better but not fully resolved. I could've asked to push the demo, shipped quietly and hoped nobody noticed the remaining lag, or just told leadership straight where things stood. I went with transparency—laid out what was fixed, what wasn't, and proposed a follow-up sprint with monitoring in place. They accepted that. Interviewer: What was the reasoning behind choosing that option over delaying the demo? Participant: Delaying felt like it would cost more politically than it would gain technically—the partial fix was real progress, and monitoring would catch anything that slipped. Hiding it wasn't really on the table once I thought about it seriously. Interviewer: If you'd had the profiling data suggesting a structural rework earlier, would that have changed your patch-versus-switch decision? Participant: Possibly. If I'd seen it that clearly before committing the extra sprint, I might have pushed harder for the parallel evaluation option instead. Interviewer: If Dev's outage had happened a year earlier rather than three weeks before this decision, would you have assigned the fix differently? Participant: Probably, yeah. With more distance from it, I likely would have just given it to him outright given his familiarity with the system. Interviewer: Anything you'd tell a peer facing a similar in-house-build-versus-alternative call? Participant: Try to separate how much you've already put into something from what it's actually going to cost you going forward. Easier said than done when your team's pride and expertise are wrapped up in it.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.83s · gen 66.50s · total 70.6s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0280 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0263 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0245 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0224 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0208 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0198 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0197 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
9. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0197 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
10. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0193 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
11. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0193 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0187 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0185 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
15. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0184 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
16. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0184 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study anchor. Anchoring bias is_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0181 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0173 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
20. **Lyell Automation bias and verification complexity.pdf** — 0.0172 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0169 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0166 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
25. **Human_Cognitive_Bias_Identification_for.pdf** — 0.0163 (rrf) — _# Systems ISSN: 2277-3878, Volume-8 Issue-6, March 2020 C. Cognitive Bias Identification In Scen_
26. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0162 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
27. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0160 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0159 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
33. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0155 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
37. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0147 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
40. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0144 (rrf) — _# So This is it? d with sufficient clari , 2003; Berger to bridge the gap is it that we retrieve_
41. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
42. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0141 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
43. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
44. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0140 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
45. **Hallihan_etal_DTM_12.pdf** — 0.0140 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## ion of Language mu ndane forces operating over long periods of time. To this assumption, Pink_
47. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0138 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0137 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0136 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
50. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0135 (rrf) — _# ( " = 0 . 44 ) . \[1\] GaganBansal,BesmiraNushi,EceKamar,WalterSLasecki,DanielSWeld,andEricHor_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single interview transcript analyzed for distinct cognitive-bias mechanisms in the participant's reported reasoning. Retrieved passages were used where available; otherwise established labels from general knowledge are disclosed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
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
      "bias_label": "sunk cost fallacy",
      "alternative_labels": ["escalation of commitment", "Concorde fallacy"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an endeavor or base decisions on previously invested resources such as time, effort, or money, rather than on future costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Choosing between patching the in-house QuickCache system and replacing it with a Redis-backed alternative",
      "decision_point_description": "After profiling confirmed QuickCache latency and surfaced concerns that the invalidation architecture needed rethinking, the participant decided whether to commit another sprint to patching QuickCache or replace it.",
      "affected_reasoning_operation": "Resource allocation and continuation decision",
      "bias_specific_mechanism": "Prior investment in QuickCache, including eight months of build time, patch rounds, specialized team expertise, and leadership praise, was weighed as a reason to continue patching even though profiling data suggested the architecture needed structural rework.",
      "manifestation_in_interview": "The participant explicitly says the team had already sunk significant engineering time into QuickCache and that ripping it out felt like wasting specialized knowledge; he weighed that history heavily against profiling data indicating structural rework.",
      "effect_on_reasoning_or_decision": "The participant committed another sprint to patching QuickCache rather than replacing it or running a parallel evaluation; the patch produced only about fifteen percent improvement and missed the demo deadline.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up.",
          "evidence_explanation": "This shows past investment and identity-relevant history being used as a reason not to replace QuickCache, which is the core sunk-cost mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily.",
          "evidence_explanation": "The participant explicitly contrasts future-oriented profiling data with the weight given to past sunk engineering time, demonstrating that sunk cost influenced the continuation decision."
        }
      ],
      "correction_or_counterevidence": "The participant later said that if the profiling data had been clearer earlier, he might have pushed for parallel evaluation, and he advised separating past investment from future cost, but this reflection came after the decision and does not negate the mechanism at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism derive from general knowledge of sunk cost fallacy/escalation of commitment. The retrieved corpus did not contain a specific passage defining this bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["recency effect", "salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judgments and decisions are influenced by how easily examples come to mind; recent, vivid, or emotionally salient events are overweighted relative to broader base-rate or track-record information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Assigning urgent QuickCache fix ownership between Dev and Marcus",
      "decision_point_description": "With days remaining before the demo, the participant chose whether Dev or Marcus should lead the urgent fix after Dev's recent production outage.",
      "affected_reasoning_operation": "Personnel risk assessment and assignment decision",
      "bias_specific_mechanism": "The recent production outage was highly available and salient, leading the participant to overweight that single event relative to Dev's eighteen months of strong delivery and Marcus's slower pattern of missed deadlines.",
      "manifestation_in_interview": "The participant explicitly says the outage was fresh and sitting right in front of him, while Marcus's objective deadline issues lacked a vivid moment and therefore felt less urgent.",
      "effect_on_reasoning_or_decision": "The participant pulled Dev from primary ownership and assigned Marcus to lead, with Dev supporting; the handoff was messy and the fix took longer than it likely would have with Dev leading.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet.",
          "evidence_explanation": "This demonstrates the vividness and temporal proximity of Dev's outage dominating the risk judgment, which is the availability mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either.",
          "evidence_explanation": "The participant had access to broader base-rate information but reports being influenced by the salient recent event, directly evidencing availability-driven weighting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If Dev's outage had happened a year earlier rather than three weeks before this decision, would you have assigned the fix differently? Participant: Probably, yeah. With more distance from it, I likely would have just given it to him outright given his familiarity with the system.",
          "evidence_explanation": "The participant confirms that temporal proximity of the event was decisive, which is characteristic of availability and recency effects."
        }
      ],
      "correction_or_counterevidence": "The participant knew Dev's overall record was good and that Marcus's deadline record was objectively not great, suggesting relevant information was available but underweighted during the decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support covers the recency effect, a related mechanism in which recent events are more available in memory and influence judgment. The availability heuristic label itself is applied from general knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": null,
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly. For example, as participants use a device, they become more familiar the Priming and Recency Effect.",
          "mechanism_supported_by_source": "Recent events have disproportionate clarity or accessibility, which can shape later judgments.",
          "relevance_to_this_occurrence": "The participant's assignment decision was disproportionately influenced by Dev's recent production outage rather than his longer-term strong record, paralleling the documented tendency for recent events to dominate judgment."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support is limited and comes from automation/complacency, aviation, usability testing, and systems engineering contexts; not all bias labels were directly supported in the retrieved passages.",
    "The analysis is based on participant self-report rather than direct observation of decision behavior.",
    "No baseline or benchmark decisions were inferred; conclusions are limited to mechanisms evidenced in the interview."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a cognitive task analysis session—I'll be asking about a specific incident you worked through, and I'd like your candid recollection of how you reasoned through it, not a polished after-the-fact summary. Everything stays anonymized. Is that okay with you? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me your role and what you were responsible for during this incident? Participant: I lead a five-person team on our internal analytics platform—basically the tooling our support organization uses to look up customer accounts, usage history, that kind of thing. I own delivery for that dashboard and I report into the VP of Engineering. During this period I was accountable for keeping the platform stable and also for a demo we had coming up for leadership. Interviewer: Can you walk me through what first alerted you to a problem? Participant: Load times on the dashboard started creeping up—support tickets came in complaining pages were taking six, seven seconds instead of two. Over about two weeks it basically tripled. We hadn't touched much in that subsystem recently except our caching layer, which we'd built in-house—we call it QuickCache—about eight months earlier. Interviewer: What did you do first? Participant: I had two real options—run broad instrumentation across the whole stack to be safe, or go straight at QuickCache since it was the most recent change and the timing lined up. We were also getting pressure from the support lead because tickets kept climbing, so I didn't want to spend a week doing exhaustive profiling everywhere. I told the team to profile QuickCache specifically first, since it was the most likely suspect given the timing, and if that came back clean we'd widen the net. Interviewer: What came out of that? Participant: Profiling confirmed QuickCache was adding real latency under high load—invalidation was firing more than it should, forcing extra database round-trips. It also surfaced a separate, unrelated issue: a missing index on one of the support tables. Neither of those was hugely surprising, but it did mean two independent things needed fixing, not one. Interviewer: How did the investigation affect team workload? Participant: Priya, who originally built QuickCache, took point on diagnosing the invalidation logic. Dev, one of our other senior engineers, has also worked deep in that code. Everyone else picked up the index fix and other tickets. That's roughly how the two weeks split. Interviewer: Let's step through it chronologically. After profiling confirmed the QuickCache issue, what was the next major decision? Participant: That's where it got harder. QuickCache had taken us about eight months to build and stabilize—three separate patch rounds just to get it production-ready in the first place. Priya was adamant we were close, that one more targeted patch to the invalidation logic would fix it. On the other hand, there's a mature Redis-backed option out there that could probably replace QuickCache in about a sprint, with a track record we could actually point to. Interviewer: What did you decide? Participant: I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up. I figured one more focused patch, with the team that knows it best, would get us there. Interviewer: What information did you rely on most heavily for that call? Participant: Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily. Interviewer: What happened after that decision? Participant: The patch only bought us about fifteen percent improvement. Not enough to hit the demo deadline. And the extra sprint stretched the team thin on top of everything else going on. Interviewer: Third decision point—who owned the urgent fix at that stage? Participant: Right, so at this point we're down to days, not weeks. Dev has the deepest knowledge of QuickCache internals, but Dev had also been at the center of a production outage about three weeks earlier—a rushed deploy under pressure that caused a real incident, though the postmortem showed it was handled well and fixed fast. Marcus was the other option; he's been solid but has missed several deadlines over the past year, nothing dramatic, just a slower, steadier pattern of slipping. Interviewer: What did you decide, and why? Participant: I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet. Interviewer: How did that play out? Participant: Handoff was messy—Dev had context Marcus didn't, so there was friction getting him up to speed, and the fix took longer than it would have with Dev leading it outright. Interviewer: Looking back, how did you weigh Dev's eighteen months of strong delivery against that one incident? Participant: I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either. Interviewer: With three days left before the demo, what did you decide about reporting status? Participant: Latency was better but not fully resolved. I could've asked to push the demo, shipped quietly and hoped nobody noticed the remaining lag, or just told leadership straight where things stood. I went with transparency—laid out what was fixed, what wasn't, and proposed a follow-up sprint with monitoring in place. They accepted that. Interviewer: What was the reasoning behind choosing that option over delaying the demo? Participant: Delaying felt like it would cost more politically than it would gain technically—the partial fix was real progress, and monitoring would catch anything that slipped. Hiding it wasn't really on the table once I thought about it seriously. Interviewer: If you'd had the profiling data suggesting a structural rework earlier, would that have changed your patch-versus-switch decision? Participant: Possibly. If I'd seen it that clearly before committing the extra sprint, I might have pushed harder for the parallel evaluation option instead. Interviewer: If Dev's outage had happened a year earlier rather than three weeks before this decision, would you have assigned the fix differently? Participant: Probably, yeah. With more distance from it, I likely would have just given it to him outright given his familiarity with the system. Interviewer: Anything you'd tell a peer facing a similar in-house-build-versus-alternative call? Participant: Try to separate how much you've already put into something from what it's actually going to cost you going forward. Easier said than done when your team's pride and expertise are wrapped up in it.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.88s · gen 103.85s · total 108.0s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0280 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0263 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0245 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0224 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0208 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0198 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0197 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
9. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0197 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
10. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0193 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
11. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0193 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0187 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0185 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
15. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0184 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
16. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0184 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study anchor. Anchoring bias is_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0181 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0173 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
20. **Lyell Automation bias and verification complexity.pdf** — 0.0172 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0169 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0166 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
25. **Human_Cognitive_Bias_Identification_for.pdf** — 0.0163 (rrf) — _# Systems ISSN: 2277-3878, Volume-8 Issue-6, March 2020 C. Cognitive Bias Identification In Scen_
26. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0162 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
27. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0160 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0159 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
33. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0155 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
37. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0147 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
40. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0144 (rrf) — _# So This is it? d with sufficient clari , 2003; Berger to bridge the gap is it that we retrieve_
41. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
42. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0141 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
43. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
44. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0140 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
45. **Hallihan_etal_DTM_12.pdf** — 0.0140 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## ion of Language mu ndane forces operating over long periods of time. To this assumption, Pink_
47. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0138 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0137 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0136 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
50. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0135 (rrf) — _# ( " = 0 . 44 ) . \[1\] GaganBansal,BesmiraNushi,EceKamar,WalterSLasecki,DanielSWeld,andEricHor_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis restricted to affirmative evidence in the interview transcript; retrieved passages used only for conceptual grounding and support, with no assumed experimental condition or expected bias count."
  },
  "identified_bias_summary": [
    {
      "bias_label": "recency effect",
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
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an investment or course of action because of previously invested resources—such as time, effort, or money—rather than evaluating prospective costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Patch-versus-replace decision for QuickCache",
      "decision_point_description": "After profiling confirmed QuickCache latency and suggested the invalidation architecture needed rethinking, the participant chose another sprint of patching QuickCache rather than replacing it with a mature Redis-backed alternative.",
      "affected_reasoning_operation": "Choice between continuing to patch an in-house caching system and replacing it with a proven alternative.",
      "bias_specific_mechanism": "The prior investment of approximately eight months of engineering time and multiple stabilization patches was treated as a central reason to keep investing in QuickCache, despite prospective evidence that the architecture needed structural rework and that a mature alternative existed.",
      "manifestation_in_interview": "The participant explicitly cited already-sunk engineering time, team expertise, and leadership pride as reasons for patching, while also acknowledging that profiling data indicated the invalidation architecture needed rethinking rather than a tweak.",
      "effect_on_reasoning_or_decision": "The participant committed another sprint to patching QuickCache; the patch yielded only about fifteen percent improvement, did not meet the demo deadline, and stretched the team thin.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up. I figured one more focused patch, with the team that knows it best, would get us there.",
          "evidence_explanation": "Shows the choice to continue was justified by prior investment, team pride, and fear of wasting built-up knowledge rather than by prospective evaluation of the replacement option."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily.",
          "evidence_explanation": "Explicitly states that sunk engineering time and system history were weighed heavily over profiling data indicating structural rework, the core sunk-cost mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant noted the profiling data suggested structural rework, and later said that if he had seen that clearly before committing the extra sprint, he might have pushed for a parallel evaluation option instead. This is retrospective reflection rather than an in-the-moment correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly defined or supported sunk cost fallacy or escalation of commitment. The label is applied from established general knowledge in cognitive science, not from retrieved corpus evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "recency effect",
      "alternative_labels": [
        "availability heuristic",
        "recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for recent events to be more available in memory and to exert disproportionate influence on judgments and decisions relative to older or more diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Urgent fix ownership assignment between Dev and Marcus",
      "decision_point_description": "Days before the leadership demo, after the QuickCache patch produced insufficient improvement, the participant chose Marcus over Dev as primary owner for the urgent fix, with Dev supporting in a reduced capacity.",
      "affected_reasoning_operation": "Risk assessment and assignment of the urgent fix owner based on recent incident history.",
      "bias_specific_mechanism": "The freshness and salience of Dev's production outage three weeks earlier made that event disproportionately available in memory and heavily weighted in the risk judgment, overshadowing Dev's broader record of strong delivery and Marcus's slower pattern of missed deadlines.",
      "manifestation_in_interview": "The participant acknowledged knowing Dev's track record was good overall but stated that the recent outage 'was the thing sitting right in front of me' and that Marcus's deadline pattern lacked a similarly vivid incident, making it feel less urgent.",
      "effect_on_reasoning_or_decision": "The participant pulled Dev off primary ownership and assigned Marcus, resulting in a messy handoff, lost context, and a longer fix than would likely have occurred with Dev leading.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet.",
          "evidence_explanation": "Shows that the freshness of the recent outage directly drove the risk judgment and ownership decision, not a broader evaluation of the two engineers' records."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either.",
          "evidence_explanation": "Explicitly contrasts overall record with the salient recent event, demonstrating that recency and availability of the outage outweighed more diagnostic base-rate information."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the objective mismatch in Marcus's deadline record and later indicated that if Dev's outage had happened a year earlier, he likely would have assigned the fix to Dev outright. This is retrospective recognition rather than an in-the-moment correction.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved passage provides direct support for the recency effect, though the interview effect is on risk-based assignment rather than simple recall.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": "Natesan et al.",
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Recent events are more accessible in memory and can therefore disproportionately influence subsequent judgments or responses.",
          "relevance_to_this_occurrence": "The participant's ownership decision was driven by the three-week-old outage rather than Dev's broader record or Marcus's deadline pattern, consistent with recent events being more available and influential."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective CTA self-report, so causal attribution of cognitive mechanisms depends on the participant's described reasoning.",
    "Retrieved corpus coverage was sparse and did not include a direct passage on sunk-cost fallacy or escalation of commitment; that occurrence relies on general knowledge with explicit disclosure."
  ]
}

