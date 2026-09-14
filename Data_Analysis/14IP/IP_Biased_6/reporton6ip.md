# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on how you handled scheduling decisions during that disruption a few weeks back — Press 3 and the coil-steel delay. Nothing you say here affects performance review, I just want to understand how you actually worked through it. Sound okay?  Participant: Sure, happy to walk through it. It was a fairly full week.  Interviewer: Can you start by telling me who you are and what your role was during this incident?  Participant: I'm the PPC analyst for the stamping shop — I own the rolling five-day schedule across Press 1, 2, and 3, and I coordinate with the three downstream assembly plants that pull from us. That week my job was basically to keep the master schedule intact despite two things going sideways at once.  Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened?  Participant: It started Monday morning. We had a weekend demand surge from one of the assembly plants — they needed an extra batch of the high-volume bracket variant, and Press 3 is the only press currently tooled for that part. I pulled up last week's throughput report and Press 3 had actually run above target, so capacity-wise it looked like the obvious answer. Before I locked anything in, I did get a short heads-up line from the scheduling assistant saying Press 3 had an open vibration advisory — not the full CMMS entry, just a flag. It read as low-priority, and set against how strong the throughput numbers were, it didn't seem like something that should change the call. So I allocated the full extra batch to Press 3.  Then Tuesday, our coil-steel supplier called in a four-day delay. Their rep mentioned 'internal allocation constraints,' which didn't mean much to me at the time. I've dealt with this supplier for a while — they've had two delays before, both around late December and late June, and both times it sorted itself out within a week without us needing backup stock. Their delays always seem to cluster around certain stretches for them, so I read the timing itself as the real signal — the 'internal allocation constraints' line sounded like their usual wording, not something new. So I figured this would follow the same pattern. I did reach out to our backup supplier contact just to have something in reserve, but honestly I called the first person on my list rather than shopping around — we were already stretched that day.  By Thursday, the reliability engineer sent an update saying Press 3's vibration had ticked up slightly since the weekend run. There's a full trend log you can pull that shows three weeks of data, but I didn't open it. Partly because things were moving fast, partly because the number itself wasn't dramatic — nothing like the Press 1 incident a couple years back, which is the kind of thing that jumps to mind when I think 'serious press problem.' This felt more like background noise.  Then Friday morning, right before I finalized the week's schedule, engineering upgraded Press 3 from 'monitor' to 'elevated concern.' When I asked what that actually meant, the engineer said it reflected a real increase in loading risk, not just a status update on paper. At that point the schedule was basically locked — downstream plants already had confirmation — and shifting the remaining volume to Press 1 would have meant a partial changeover costing several hours. I trimmed Friday's Press 3 run a bit but kept the plan mostly as it was.  Interviewer: Let's reconstruct that timeline a bit more precisely. What did you actually have in front of you Monday morning, before you made the allocation call?  Participant: The throughput report from the prior week, the demand surge notice from the assembly plant, the fact that Press 3 was the only tooled option, and that brief note flagging the vibration advisory. The full CMMS detail wasn't something I pulled up — I just had the short flag.  Interviewer: And the vibration advisory — how did that information reach you in more detail?  Participant: The maintenance tech mentioned more of it in passing, after the allocation was already set, saying there'd be a follow-up inspection recommended within two weeks. It wasn't presented as urgent even then.  Interviewer: When did you first hear about the supplier delay, and what was your first reaction?  Participant: Tuesday, from their account rep directly. My first thought was, 'this looks like the same thing that happened in December and June.'  Interviewer: Let's go back to the Monday allocation decision. What alternatives did you actually weigh?  Participant: I considered splitting the batch — running part on a temporarily retooled Press 1 and a reduced run on Press 3 — or pushing part of the order to the following week. But the changeover cost and the tight timeline made Press 3 alone the cleanest option.  Interviewer: What made the throughput report feel like the deciding piece of evidence, given you also had that vibration flag?  Participant: It was recent, it was concrete, and it directly answered the question I was asking — can Press 3 handle more volume. The flag was there, but it was low-priority and vague next to a full week of solid output numbers, so the throughput report just carried more weight for me.  Interviewer: On the supplier delay — walk me through the reasoning that led you to wait rather than order backup stock right away.  Participant: The pattern matched what I'd seen twice before with this supplier, so I expected a similar resolution — to me the timing itself was the tell, more than anything they actually said. Their rep's line about 'internal allocation constraints' sounded like the kind of thing they always say around these stretches, so it didn't register as pointing to anything different this time.  Interviewer: And the choice of backup contact — what determined which supplier you called?  Participant: Honestly, it's the one I already had a relationship with. I didn't compare lead times or pricing against other options that morning — there wasn't a clean window to do that kind of comparison shopping with everything else going on.  Interviewer: Thursday's vibration note — what determined whether you pulled the full trend log? Do you think opening it would have changed what you had to do that day?  Participant: I had the update in front of me, and I made a call not to dig further right then. If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line than a single number did, and that could have meant reworking Friday's plan on top of everything else already moving. The bi-weekly review was close enough that it felt fine to let it sit until then.  Interviewer: What situation were you picturing when you assessed how serious it might be?  Participant: If I'm honest, I was thinking of the Press 1 fire from a couple years ago — that's the reference point that comes to mind when someone says 'press failure.' This didn't look anything like that, so it didn't register as urgent.  Interviewer: Friday, when the status moved to 'elevated concern' — how did you weigh that against the schedule you'd already committed to?  Participant: At that point we were locked in with the downstream plants, and a full reallocation meant hours of changeover we didn't have room for. Even with the engineer telling me it reflected a real risk increase, the earlier data — the throughput numbers, the clean weekend run — still felt like the more solid read on how Press 3 actually performs, so I didn't weight the new label as heavily as what I already had. I trimmed the Friday run slightly rather than overhauling the plan.  Interviewer: What would have had to be different in that assessment for you to change the schedule more substantially?  Participant: Probably if the language had been stronger — something like an explicit downtime risk instead of 'elevated concern' — or if it had come earlier in the week when I had more room to maneuver.  Interviewer: What actually happened with Press 3 and the shipments that week?  Participant: Press 3 finished the week without failing. The reliability engineer did file a formal recommendation to reduce loading next cycle. Shipments went out on time to all three plants.  Interviewer: If that Monday flag had appeared directly inside your scheduling dashboard instead of arriving as a separate message from the scheduling assistant, do you think the allocation decision would have gone differently?  Participant: Possibly. If it had been sitting right there next to the throughput numbers instead of coming in as a separate note, I think I'd have paused longer on it instead of leaning mainly on the report.  Interviewer: If you'd had unlimited time that week, is there anything you'd have checked differently?  Participant: I'd have pulled the full trend log Thursday instead of going off the single update, and I probably would have called around to compare backup suppliers instead of just going with who I knew.  Interviewer: Last one — looking back, what's one thing about how information reached you that you'd want changed?  Participant: Honestly, just having the maintenance advisories show up in full where I'm already doing my scheduling. Right now I mostly get a quick flag and have to go looking for the rest, and that week, I didn't.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.96s · gen 137.68s · total 143.3s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0284 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0264 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0248 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0238 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0237 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0230 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0217 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0202 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0196 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0191 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0189 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0186 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
15. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0186 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0185 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0178 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
20. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0164 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
23. **Lyell Automation bias and verification complexity.pdf** — 0.0163 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
24. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0163 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0162 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
34. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0149 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
35. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
37. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0146 (rrf) — _# 4 Anchoring bias Lieder et al., 2018) suggests that after being anchored, humans tend to adjus_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
40. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0143 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
42. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0142 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
43. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0142 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
44. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0138 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0137 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0137 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
48. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0136 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0134 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Blinded evaluation of a single retrospective debrief interview for affirmative, mechanism-grounded cognitive bias occurrences in scheduling and risk decisions."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 2
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
      "bias_label": "anchoring and adjustment",
      "alternative_labels": ["anchoring bias", "anchoring-and-adjustment heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which an initial value or starting point exerts excessive influence and subsequent adjustments away from that anchor are insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Monday Press 3 allocation for demand surge",
      "decision_point_description": "Whether to allocate the full extra bracket batch to Press 3 or split/retime it given the vibration advisory.",
      "affected_reasoning_operation": "Evidence weighting and risk integration under uncertainty",
      "bias_specific_mechanism": "The participant anchored on last week's above-target throughput as the central indicator of Press 3 capability. The low-priority vibration flag was treated as a small adjustment from that anchor rather than as an independent risk signal.",
      "manifestation_in_interview": "The participant described the strong throughput report as making Press 3 the obvious answer and stated that the throughput report carried more weight than the vibration flag.",
      "effect_on_reasoning_or_decision": "Led to allocating the full extra batch to Press 3 without pulling the full CMMS detail or substantially weighting the vibration advisory.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pulled up last week's throughput report and Press 3 had actually run above target, so capacity-wise it looked like the obvious answer.",
          "evidence_explanation": "This reveals an initial anchor formed from recent throughput success before full risk integration."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It read as low-priority, and set against how strong the throughput numbers were, it didn't seem like something that should change the call.",
          "evidence_explanation": "The adverse flag was evaluated relative to the strong throughput anchor, reducing its impact."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was recent, it was concrete, and it directly answered the question I was asking — can Press 3 handle more volume. The flag was there, but it was low-priority and vague next to a full week of solid output numbers, so the throughput report just carried more weight for me.",
          "evidence_explanation": "This explicitly shows a concrete initial value dominating risk information, consistent with insufficient adjustment."
        }
      ],
      "correction_or_counterevidence": "The vibration advisory was described as low-priority and vague, and full CMMS details were not immediately available. Press 3 ultimately completed the week without failing, so the decision did not produce a realized failure.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages describe anchoring-and-adjustment as an initial value dominating subsequent adjustment; they support the mechanism and label.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The passage treats anchoring-and-adjustment as a heuristic in which initial predictions may be adjusted insufficiently.",
          "relevance_to_this_occurrence": "Supports the general mechanism of anchoring and insufficient adjustment from an initially compelling numerical/performance cue."
        },
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described by Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, “adjustments are typically insufficient.”",
          "mechanism_supported_by_source": "The passage directly states that initial answers anchor estimates and subsequent adjustments are typically insufficient.",
          "relevance_to_this_occurrence": "Directly supports the anchoring-and-adjustment characterization used for the Monday allocation decision."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to estimate the probability or frequency of an event by the ease with which similar instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Tuesday supplier delay response",
      "decision_point_description": "Whether to treat the four-day coil-steel delay as a routine pattern or to secure backup stock immediately.",
      "affected_reasoning_operation": "Predictive probability and risk assessment under uncertainty",
      "bias_specific_mechanism": "Ease of recalling two previous December and June delays made a same-pattern resolution seem more probable. Retrieval fluency from a small sample outweighed the unfamiliar diagnostic content of the current 'internal allocation constraints' message.",
      "manifestation_in_interview": "The participant immediately categorized the current delay as the same type of event as prior delays and interpreted timing as the real signal rather than the supplier's stated cause.",
      "effect_on_reasoning_or_decision": "He waited rather than ordering backup stock right away; the backup contact was used only as a reserve.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought was, 'this looks like the same thing that happened in December and June.'",
          "evidence_explanation": "The rapid recall of two prior similar-sounding delays shaped the initial diagnosis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I've dealt with this supplier for a while — they've had two delays before, both around late December and late June, and both times it sorted itself out within a week without us needing backup stock.",
          "evidence_explanation": "The availability of two prior examples provided the primary basis for predicting the current delay would also resolve."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The pattern matched what I'd seen twice before with this supplier, so I expected a similar resolution — to me the timing itself was the tell, more than anything they actually said.",
          "evidence_explanation": "This shows frequency/probability judgment driven by easy recall of a small set of prior cases rather than by current diagnostic evidence."
        }
      ],
      "correction_or_counterevidence": "Past delays did resolve within a week, and he did contact a backup supplier as a reserve. The historical pattern could be a rational, if small-sample, prior rather than purely bias-driven.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved RAG context does not provide a definition or empirical support for the availability heuristic; this classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["selective exposure", "motivated information avoidance"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, or remember information in ways that confirm existing beliefs or plans, and to avoid information that may challenge them.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Thursday trend-log inquiry",
      "decision_point_description": "Whether to open the full three-week trend log after the Thursday vibration update.",
      "affected_reasoning_operation": "Information search and diagnostic evidence seeking",
      "bias_specific_mechanism": "The existing Friday schedule and the preference to avoid disruption motivated avoiding the trend log because it might contain an upward-trend signal that would force reconsideration of the plan.",
      "manifestation_in_interview": "The participant explicitly acknowledged not opening the log partly because it might have shown a clearer upward line and required reworking Friday's plan.",
      "effect_on_reasoning_or_decision": "He did not obtain full trend data before finalizing the schedule and relied on the single nondramatic weekly update.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There's a full trend log you can pull that shows three weeks of data, but I didn't open it.",
          "evidence_explanation": "This establishes that additional diagnostic information was available but not sought."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line than a single number did, and that could have meant reworking Friday's plan on top of everything else already moving.",
          "evidence_explanation": "This states a motive to avoid disconfirming information because it might disrupt the existing plan."
        }
      ],
      "correction_or_counterevidence": "The participant also cited time pressure and an upcoming bi-weekly review. The single vibration number was not dramatic, and the trend log might not have changed the plan; however, the stated motive remains bias-relevant avoidance.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus mentions confirmation bias in technical information processing, providing nominal support for the term, though it does not provide a formal definition.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "In addition, an explanation in terms of confirmation bias in processing the sampled information or difficulties of comprehension is also unlikely, given that the participants were very well trained and that the system parameter always contradicted the aid’s diagnosis in an unequivocal way.",
          "mechanism_supported_by_source": "The passage explicitly references confirmation bias as a distinct information-processing bias in diagnostic technical decision-making.",
          "relevance_to_this_occurrence": "Grounds the confirmation-bias label even though the cited study ultimately ruled it out for that specific group."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or severity of an event by the ease with which salient examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Thursday severity assessment of Press 3 vibration",
      "decision_point_description": "Whether the reported Press 3 vibration increase should be treated as urgent or as background noise.",
      "affected_reasoning_operation": "Risk severity judgment",
      "bias_specific_mechanism": "Ease of recalling the dramatic Press 1 fire served as the dominant mental reference for serious press problems. Because the current vibration did not resemble that salient example, it was judged as not urgent.",
      "manifestation_in_interview": "The participant said the Press 1 fire was the reference point that came to mind when considering press failure, and the current issue did not resemble it.",
      "effect_on_reasoning_or_decision": "Underweighted the vibration risk and deferred further investigation, contributing to the Thursday decision not to open the trend log.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, I was thinking of the Press 1 fire from a couple years ago — that's the reference point that comes to mind when someone says 'press failure.' This didn't look anything like that, so it didn't register as urgent.",
          "evidence_explanation": "This directly shows severity judgment anchored to an easily recalled catastrophic event, with insufficient consideration of less dramatic but still material risk."
        }
      ],
      "correction_or_counterevidence": "The Press 1 fire was a real catastrophic event and may provide a meaningful upper-bound reference; however, using it as the primary risk reference can bias assessment of lower-severity failure modes.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved RAG context does not provide a definition or empirical support for the availability heuristic; this classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": ["anchoring bias", "anchoring-and-adjustment heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which an initial value or starting point exerts excessive influence and subsequent adjustments away from that anchor are insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Friday schedule lock after elevated concern",
      "decision_point_description": "Whether to substantially reallocate remaining Press 3 volume after the status was upgraded to 'elevated concern'.",
      "affected_reasoning_operation": "Integration of new risk information into an established plan",
      "bias_specific_mechanism": "The initial positive throughput report and clean weekend run remained a strong anchor. Despite the engineer's elevated-concern statement, the participant adjusted only slightly and underweighted the new label.",
      "manifestation_in_interview": "The participant explicitly said the earlier data still felt like a more solid read on Press 3's actual performance than the new elevated-concern label.",
      "effect_on_reasoning_or_decision": "He trimmed Friday's Press 3 run slightly but kept the plan mostly as it was rather than pursuing substantial reallocation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Even with the engineer telling me it reflected a real risk increase, the earlier data — the throughput numbers, the clean weekend run — still felt like the more solid read on how Press 3 actually performs, so I didn't weight the new label as heavily as what I already had.",
          "evidence_explanation": "This shows anchor preservation and insufficient adjustment in response to new risk information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I trimmed Friday's Press 3 run a bit but kept the plan mostly as it was.",
          "evidence_explanation": "The behavioral consequence was a small adjustment rather than a full reconsideration."
        }
      ],
      "correction_or_counterevidence": "The schedule was already committed to downstream plants, and full reallocation would have cost hours of changeover. Press 3 completed the week without failing, and a formal recommendation was filed for next cycle.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages describe anchoring-and-adjustment as an initial value dominating subsequent adjustment; they support the mechanism and label.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The passage treats anchoring-and-adjustment as a heuristic in which initial predictions may be adjusted insufficiently.",
          "relevance_to_this_occurrence": "Supports the mechanism of under-adjusting from earlier performance data in response to new risk information."
        },
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described by Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, “adjustments are typically insufficient.”",
          "mechanism_supported_by_source": "The passage directly states that initial answers anchor estimates and subsequent adjustments are typically insufficient.",
          "relevance_to_this_occurrence": "Directly supports the characterization of insufficient adjustment from the earlier Friday schedule anchor."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": ["escalation of commitment", "get-there-itis"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Friday Press 3 schedule lock after elevated concern",
      "supporting_interview_quote": "At that point the schedule was basically locked — downstream plants already had confirmation — and shifting the remaining volume to Press 1 would have meant a partial changeover costing several hours.",
      "plausible_mechanism": "The tendency to continue an existing plan despite new information indicating elevated risk, particularly after commitment or sunk costs have accumulated.",
      "why_not_identified": "The participant did partially adjust by trimming Friday's run, and the reluctance to reallocate may be explained by legitimate operational costs, time constraints, and downstream commitments rather than a distinct cognitive distortion."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrospective self-report from the participant may be influenced by memory reconstruction and hindsight.",
    "Retrieved RAG passages were limited and some contained OCR noise; direct corpus support was thin for confirmation bias and absent for availability heuristic.",
    "Outcome information, such as Press 3 completing the week without failure, was not used to impute bias at the time of decision.",
    "The analysis is restricted to a single interview and does not include independent verification of actual operational decisions."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on how you handled scheduling decisions during that disruption a few weeks back — Press 3 and the coil-steel delay. Nothing you say here affects performance review, I just want to understand how you actually worked through it. Sound okay?  Participant: Sure, happy to walk through it. It was a fairly full week.  Interviewer: Can you start by telling me who you are and what your role was during this incident?  Participant: I'm the PPC analyst for the stamping shop — I own the rolling five-day schedule across Press 1, 2, and 3, and I coordinate with the three downstream assembly plants that pull from us. That week my job was basically to keep the master schedule intact despite two things going sideways at once.  Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened?  Participant: It started Monday morning. We had a weekend demand surge from one of the assembly plants — they needed an extra batch of the high-volume bracket variant, and Press 3 is the only press currently tooled for that part. I pulled up last week's throughput report and Press 3 had actually run above target, so capacity-wise it looked like the obvious answer. Before I locked anything in, I did get a short heads-up line from the scheduling assistant saying Press 3 had an open vibration advisory — not the full CMMS entry, just a flag. It read as low-priority, and set against how strong the throughput numbers were, it didn't seem like something that should change the call. So I allocated the full extra batch to Press 3.  Then Tuesday, our coil-steel supplier called in a four-day delay. Their rep mentioned 'internal allocation constraints,' which didn't mean much to me at the time. I've dealt with this supplier for a while — they've had two delays before, both around late December and late June, and both times it sorted itself out within a week without us needing backup stock. Their delays always seem to cluster around certain stretches for them, so I read the timing itself as the real signal — the 'internal allocation constraints' line sounded like their usual wording, not something new. So I figured this would follow the same pattern. I did reach out to our backup supplier contact just to have something in reserve, but honestly I called the first person on my list rather than shopping around — we were already stretched that day.  By Thursday, the reliability engineer sent an update saying Press 3's vibration had ticked up slightly since the weekend run. There's a full trend log you can pull that shows three weeks of data, but I didn't open it. Partly because things were moving fast, partly because the number itself wasn't dramatic — nothing like the Press 1 incident a couple years back, which is the kind of thing that jumps to mind when I think 'serious press problem.' This felt more like background noise.  Then Friday morning, right before I finalized the week's schedule, engineering upgraded Press 3 from 'monitor' to 'elevated concern.' When I asked what that actually meant, the engineer said it reflected a real increase in loading risk, not just a status update on paper. At that point the schedule was basically locked — downstream plants already had confirmation — and shifting the remaining volume to Press 1 would have meant a partial changeover costing several hours. I trimmed Friday's Press 3 run a bit but kept the plan mostly as it was.  Interviewer: Let's reconstruct that timeline a bit more precisely. What did you actually have in front of you Monday morning, before you made the allocation call?  Participant: The throughput report from the prior week, the demand surge notice from the assembly plant, the fact that Press 3 was the only tooled option, and that brief note flagging the vibration advisory. The full CMMS detail wasn't something I pulled up — I just had the short flag.  Interviewer: And the vibration advisory — how did that information reach you in more detail?  Participant: The maintenance tech mentioned more of it in passing, after the allocation was already set, saying there'd be a follow-up inspection recommended within two weeks. It wasn't presented as urgent even then.  Interviewer: When did you first hear about the supplier delay, and what was your first reaction?  Participant: Tuesday, from their account rep directly. My first thought was, 'this looks like the same thing that happened in December and June.'  Interviewer: Let's go back to the Monday allocation decision. What alternatives did you actually weigh?  Participant: I considered splitting the batch — running part on a temporarily retooled Press 1 and a reduced run on Press 3 — or pushing part of the order to the following week. But the changeover cost and the tight timeline made Press 3 alone the cleanest option.  Interviewer: What made the throughput report feel like the deciding piece of evidence, given you also had that vibration flag?  Participant: It was recent, it was concrete, and it directly answered the question I was asking — can Press 3 handle more volume. The flag was there, but it was low-priority and vague next to a full week of solid output numbers, so the throughput report just carried more weight for me.  Interviewer: On the supplier delay — walk me through the reasoning that led you to wait rather than order backup stock right away.  Participant: The pattern matched what I'd seen twice before with this supplier, so I expected a similar resolution — to me the timing itself was the tell, more than anything they actually said. Their rep's line about 'internal allocation constraints' sounded like the kind of thing they always say around these stretches, so it didn't register as pointing to anything different this time.  Interviewer: And the choice of backup contact — what determined which supplier you called?  Participant: Honestly, it's the one I already had a relationship with. I didn't compare lead times or pricing against other options that morning — there wasn't a clean window to do that kind of comparison shopping with everything else going on.  Interviewer: Thursday's vibration note — what determined whether you pulled the full trend log? Do you think opening it would have changed what you had to do that day?  Participant: I had the update in front of me, and I made a call not to dig further right then. If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line than a single number did, and that could have meant reworking Friday's plan on top of everything else already moving. The bi-weekly review was close enough that it felt fine to let it sit until then.  Interviewer: What situation were you picturing when you assessed how serious it might be?  Participant: If I'm honest, I was thinking of the Press 1 fire from a couple years ago — that's the reference point that comes to mind when someone says 'press failure.' This didn't look anything like that, so it didn't register as urgent.  Interviewer: Friday, when the status moved to 'elevated concern' — how did you weigh that against the schedule you'd already committed to?  Participant: At that point we were locked in with the downstream plants, and a full reallocation meant hours of changeover we didn't have room for. Even with the engineer telling me it reflected a real risk increase, the earlier data — the throughput numbers, the clean weekend run — still felt like the more solid read on how Press 3 actually performs, so I didn't weight the new label as heavily as what I already had. I trimmed the Friday run slightly rather than overhauling the plan.  Interviewer: What would have had to be different in that assessment for you to change the schedule more substantially?  Participant: Probably if the language had been stronger — something like an explicit downtime risk instead of 'elevated concern' — or if it had come earlier in the week when I had more room to maneuver.  Interviewer: What actually happened with Press 3 and the shipments that week?  Participant: Press 3 finished the week without failing. The reliability engineer did file a formal recommendation to reduce loading next cycle. Shipments went out on time to all three plants.  Interviewer: If that Monday flag had appeared directly inside your scheduling dashboard instead of arriving as a separate message from the scheduling assistant, do you think the allocation decision would have gone differently?  Participant: Possibly. If it had been sitting right there next to the throughput numbers instead of coming in as a separate note, I think I'd have paused longer on it instead of leaning mainly on the report.  Interviewer: If you'd had unlimited time that week, is there anything you'd have checked differently?  Participant: I'd have pulled the full trend log Thursday instead of going off the single update, and I probably would have called around to compare backup suppliers instead of just going with who I knew.  Interviewer: Last one — looking back, what's one thing about how information reached you that you'd want changed?  Participant: Honestly, just having the maintenance advisories show up in full where I'm already doing my scheduling. Right now I mostly get a quick flag and have to go looking for the rest, and that week, I didn't.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.11s · gen 155.00s · total 159.6s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0284 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0264 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0248 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0238 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0237 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0230 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0217 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0202 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0196 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0191 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0189 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0186 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
15. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0186 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0185 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0178 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
20. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0164 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
23. **Lyell Automation bias and verification complexity.pdf** — 0.0163 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
24. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0163 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0162 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
34. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0149 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
35. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
37. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0146 (rrf) — _# 4 Anchoring bias Lieder et al., 2018) suggests that after being anchored, humans tend to adjus_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
40. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0143 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
42. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0142 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
43. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0142 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
44. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0138 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0137 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0137 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
48. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0136 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0134 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the full interview debrief for cognitive-bias mechanisms in the participant's scheduling, supplier-response, and risk-assessment reasoning."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
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
      "bias_label": "plan continuation bias",
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
      "bias_label": "anchoring and adjustment",
      "alternative_labels": ["anchoring bias", "insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "Relying on an initial value or piece of information as a reference point and making insufficient adjustments when subsequent information arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Monday allocation of extra bracket batch to Press 3",
      "decision_point_description": "Choosing whether to allocate the full extra batch to Press 3 despite a low-priority vibration advisory",
      "affected_reasoning_operation": "Evidence weighting and capacity allocation decision",
      "bias_specific_mechanism": "The prior week's strong throughput report served as the anchor for Press 3 capability; the later vibration advisory was treated as vague and low-priority, so the decision was insufficiently adjusted away from the anchor.",
      "manifestation_in_interview": "The participant said the throughput report was recent, concrete, and directly answered the capacity question, while the flag was vague and low-priority next to solid output numbers.",
      "effect_on_reasoning_or_decision": "The full extra batch was allocated to Press 3 and the vibration risk was not meaningfully incorporated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Before I locked anything in, I did get a short heads-up line from the scheduling assistant saying Press 3 had an open vibration advisory — not the full CMMS entry, just a flag. It read as low-priority, and set against how strong the throughput numbers were, it didn't seem like something that should change the call.",
          "evidence_explanation": "Shows the strong prior week throughput numbers acting as the initial anchor and the advisory being underweighted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was recent, it was concrete, and it directly answered the question I was asking — can Press 3 handle more volume. The flag was there, but it was low-priority and vague next to a full week of solid output numbers, so the throughput report just carried more weight for me.",
          "evidence_explanation": "Explicitly describes the anchoring and insufficient adjustment mechanism: the concrete anchor outweighed the new risk flag."
        }
      ],
      "correction_or_counterevidence": "The advisory was labelled low-priority, there were real changeover and timeline constraints, and Press 3 did not fail that week.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved space-flight verification source defines the anchoring and adjustment heuristic and states that adjustments are typically insufficient.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described by Tversky and Kahneman in 1974... people make estimates based on an initial answer, and adjustments from there based on additional information... 'adjustments are typically insufficient.'",
          "mechanism_supported_by_source": "Initial values dominate estimates and adjustments from them are typically insufficient.",
          "relevance_to_this_occurrence": "The participant started from a strong throughput report and did not sufficiently adjust the allocation decision when the vibration advisory appeared."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "representativeness heuristic",
      "alternative_labels": ["availability heuristic", "expectation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood of an event by its similarity to prior instances rather than by the diagnosticity or statistical reliability of current evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Tuesday supplier-delay response",
      "decision_point_description": "Deciding whether the four-day coil-steel delay required immediate backup-stock ordering or would likely resolve like past delays",
      "affected_reasoning_operation": "Predictive inference about supplier delay duration",
      "bias_specific_mechanism": "Two prior supplier delays were used as a mental prototype; the participant matched the current delay to that pattern based mainly on timing and treated the rep's specific wording as uninformative.",
      "manifestation_in_interview": "He described the timing as 'the real signal' and the phrase 'internal allocation constraints' as their usual wording, despite having only two prior instances.",
      "effect_on_reasoning_or_decision": "He did not order backup stock immediately and expected the delay to resolve on its own within a week.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've dealt with this supplier for a while — they've had two delays before, both around late December and late June, and both times it sorted itself out within a week without us needing backup stock. Their delays always seem to cluster around certain stretches for them, so I read the timing itself as the real signal — the 'internal allocation constraints' line sounded like their usual wording, not something new.",
          "evidence_explanation": "Shows similarity-based reasoning from a very small sample and dismissal of the current message content."
        }
      ],
      "correction_or_counterevidence": "Using past supplier behavior can be a reasonable heuristic under time pressure, and previous delays had resolved quickly; he did contact a backup supplier as a precaution.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the representativeness heuristic was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "availability heuristic",
      "alternative_labels": ["salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Estimating severity or likelihood based on how easily a vivid instance comes to mind, rather than on the full distribution of relevant evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Thursday risk assessment of Press 3 vibration",
      "decision_point_description": "Judging whether the vibration increase was serious enough to warrant immediate action",
      "affected_reasoning_operation": "Risk perception and severity judgment",
      "bias_specific_mechanism": "A vivid past event, the Press 1 fire, came easily to mind as the reference for a serious press problem; because the current vibration did not resemble it, the participant downgraded the risk to background noise.",
      "manifestation_in_interview": "The participant admitted he was picturing the Press 1 fire and concluded the current situation did not look like that.",
      "effect_on_reasoning_or_decision": "The vibration increase was treated as non-urgent and not acted upon on Thursday.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, I was thinking of the Press 1 fire from a couple years ago — that's the reference point that comes to mind when someone says 'press failure.' This didn't look anything like that, so it didn't register as urgent.",
          "evidence_explanation": "Shows a vivid recalled event dominating the severity judgment and causing underestimation of a less extreme risk."
        }
      ],
      "correction_or_counterevidence": "The current number was not dramatic and the press did not fail; comparing current signals to known past failures can be part of ordinary risk calibration.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the availability heuristic was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["selective exposure", "information avoidance"],
      "taxonomy_status": "established_label",
      "bias_definition": "Avoiding or underweighting information that could disconfirm an existing plan, belief, or preference while favoring information that supports it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Thursday decision not to open Press 3 trend log",
      "decision_point_description": "Choosing whether to examine three weeks of vibration trend data after the Thursday update",
      "affected_reasoning_operation": "Information search and evidence evaluation",
      "bias_specific_mechanism": "The participant avoided potentially disconfirming evidence: the full trend log might have shown an upward trend and forced rework, so he left the plan-favorable single update unexamined.",
      "manifestation_in_interview": "He explicitly said part of the reason for not opening the log was that it might have shown a clearer upward line requiring Friday schedule changes.",
      "effect_on_reasoning_or_decision": "The trend log was not opened, so its information was not available for Thursday's plan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I had the update in front of me, and I made a call not to dig further right then. If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line than a single number did, and that could have meant reworking Friday's plan on top of everything else already moving.",
          "evidence_explanation": "Explicitly shows information avoidance to protect the existing schedule from disconfirming evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There's a full trend log you can pull that shows three weeks of data, but I didn't open it.",
          "evidence_explanation": "Confirms the behavior: the participant had access to a more complete dataset but did not examine it."
        }
      ],
      "correction_or_counterevidence": "Time pressure and the proximity of the bi-weekly review were also cited; deciding not to open a log can be reasonable if the single update was not actionable.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for confirmation bias as selective information avoidance was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["commitment to plan", "escalation of commitment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an existing course of action despite emerging evidence that the plan may need revision.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Friday finalization of Press 3 schedule after elevated concern",
      "decision_point_description": "Deciding whether to substantially reallocate planned Press 3 volume after engineering upgraded the advisory to elevated concern",
      "affected_reasoning_operation": "Schedule revision decision under new risk information",
      "bias_specific_mechanism": "The committed schedule and earlier performance data maintained the existing plan; the elevated-risk label was discounted relative to that prior anchor, leading to only a minor trim instead of a full reassessment.",
      "manifestation_in_interview": "He said the schedule was basically locked and that the earlier data still felt like the more solid read, so he did not weight the new label as heavily.",
      "effect_on_reasoning_or_decision": "The plan remained mostly unchanged; only a slight reduction in Friday's Press 3 run was made.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point the schedule was basically locked — downstream plants already had confirmation — and shifting the remaining volume to Press 1 would have meant a partial changeover costing several hours. I trimmed Friday's Press 3 run a bit but kept the plan mostly as it was.",
          "evidence_explanation": "Shows continued adherence to the original plan despite the new risk label."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Even with the engineer telling me it reflected a real risk increase, the earlier data — the throughput numbers, the clean weekend run — still felt like the more solid read on how Press 3 actually performs, so I didn't weight the new label as heavily as what I already had.",
          "evidence_explanation": "Demonstrates the mechanism: new contradictory risk information was discounted relative to the existing plan-supporting evidence."
        }
      ],
      "correction_or_counterevidence": "The engineer said 'elevated concern' rather than an explicit downtime risk; substantial reallocation carried real changeover costs and downstream commitment changes; Press 3 completed the week without failing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for plan continuation bias as a defined mechanism was not available; the label derives from general cognitive-science knowledge. The retrieved cockpit source mentions the label but does not supply a mechanism definition in the available passage.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus support is uneven; only anchoring and adjustment has a clear definitional passage in the supplied material.",
    "Several labels rely on general cognitive-science knowledge and are disclosed as such.",
    "The interview concerns a single incident with normal operational constraints; identified biases are not evidence of poor outcome, since Press 3 did not fail and shipments went out on time.",
    "The analysis treats the participant's self-reported reasoning as evidence and cannot independently verify the actual information environment or internal mental states."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on how you handled scheduling decisions during that disruption a few weeks back — Press 3 and the coil-steel delay. Nothing you say here affects performance review, I just want to understand how you actually worked through it. Sound okay?  Participant: Sure, happy to walk through it. It was a fairly full week.  Interviewer: Can you start by telling me who you are and what your role was during this incident?  Participant: I'm the PPC analyst for the stamping shop — I own the rolling five-day schedule across Press 1, 2, and 3, and I coordinate with the three downstream assembly plants that pull from us. That week my job was basically to keep the master schedule intact despite two things going sideways at once.  Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened?  Participant: It started Monday morning. We had a weekend demand surge from one of the assembly plants — they needed an extra batch of the high-volume bracket variant, and Press 3 is the only press currently tooled for that part. I pulled up last week's throughput report and Press 3 had actually run above target, so capacity-wise it looked like the obvious answer. Before I locked anything in, I did get a short heads-up line from the scheduling assistant saying Press 3 had an open vibration advisory — not the full CMMS entry, just a flag. It read as low-priority, and set against how strong the throughput numbers were, it didn't seem like something that should change the call. So I allocated the full extra batch to Press 3.  Then Tuesday, our coil-steel supplier called in a four-day delay. Their rep mentioned 'internal allocation constraints,' which didn't mean much to me at the time. I've dealt with this supplier for a while — they've had two delays before, both around late December and late June, and both times it sorted itself out within a week without us needing backup stock. Their delays always seem to cluster around certain stretches for them, so I read the timing itself as the real signal — the 'internal allocation constraints' line sounded like their usual wording, not something new. So I figured this would follow the same pattern. I did reach out to our backup supplier contact just to have something in reserve, but honestly I called the first person on my list rather than shopping around — we were already stretched that day.  By Thursday, the reliability engineer sent an update saying Press 3's vibration had ticked up slightly since the weekend run. There's a full trend log you can pull that shows three weeks of data, but I didn't open it. Partly because things were moving fast, partly because the number itself wasn't dramatic — nothing like the Press 1 incident a couple years back, which is the kind of thing that jumps to mind when I think 'serious press problem.' This felt more like background noise.  Then Friday morning, right before I finalized the week's schedule, engineering upgraded Press 3 from 'monitor' to 'elevated concern.' When I asked what that actually meant, the engineer said it reflected a real increase in loading risk, not just a status update on paper. At that point the schedule was basically locked — downstream plants already had confirmation — and shifting the remaining volume to Press 1 would have meant a partial changeover costing several hours. I trimmed Friday's Press 3 run a bit but kept the plan mostly as it was.  Interviewer: Let's reconstruct that timeline a bit more precisely. What did you actually have in front of you Monday morning, before you made the allocation call?  Participant: The throughput report from the prior week, the demand surge notice from the assembly plant, the fact that Press 3 was the only tooled option, and that brief note flagging the vibration advisory. The full CMMS detail wasn't something I pulled up — I just had the short flag.  Interviewer: And the vibration advisory — how did that information reach you in more detail?  Participant: The maintenance tech mentioned more of it in passing, after the allocation was already set, saying there'd be a follow-up inspection recommended within two weeks. It wasn't presented as urgent even then.  Interviewer: When did you first hear about the supplier delay, and what was your first reaction?  Participant: Tuesday, from their account rep directly. My first thought was, 'this looks like the same thing that happened in December and June.'  Interviewer: Let's go back to the Monday allocation decision. What alternatives did you actually weigh?  Participant: I considered splitting the batch — running part on a temporarily retooled Press 1 and a reduced run on Press 3 — or pushing part of the order to the following week. But the changeover cost and the tight timeline made Press 3 alone the cleanest option.  Interviewer: What made the throughput report feel like the deciding piece of evidence, given you also had that vibration flag?  Participant: It was recent, it was concrete, and it directly answered the question I was asking — can Press 3 handle more volume. The flag was there, but it was low-priority and vague next to a full week of solid output numbers, so the throughput report just carried more weight for me.  Interviewer: On the supplier delay — walk me through the reasoning that led you to wait rather than order backup stock right away.  Participant: The pattern matched what I'd seen twice before with this supplier, so I expected a similar resolution — to me the timing itself was the tell, more than anything they actually said. Their rep's line about 'internal allocation constraints' sounded like the kind of thing they always say around these stretches, so it didn't register as pointing to anything different this time.  Interviewer: And the choice of backup contact — what determined which supplier you called?  Participant: Honestly, it's the one I already had a relationship with. I didn't compare lead times or pricing against other options that morning — there wasn't a clean window to do that kind of comparison shopping with everything else going on.  Interviewer: Thursday's vibration note — what determined whether you pulled the full trend log? Do you think opening it would have changed what you had to do that day?  Participant: I had the update in front of me, and I made a call not to dig further right then. If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line than a single number did, and that could have meant reworking Friday's plan on top of everything else already moving. The bi-weekly review was close enough that it felt fine to let it sit until then.  Interviewer: What situation were you picturing when you assessed how serious it might be?  Participant: If I'm honest, I was thinking of the Press 1 fire from a couple years ago — that's the reference point that comes to mind when someone says 'press failure.' This didn't look anything like that, so it didn't register as urgent.  Interviewer: Friday, when the status moved to 'elevated concern' — how did you weigh that against the schedule you'd already committed to?  Participant: At that point we were locked in with the downstream plants, and a full reallocation meant hours of changeover we didn't have room for. Even with the engineer telling me it reflected a real risk increase, the earlier data — the throughput numbers, the clean weekend run — still felt like the more solid read on how Press 3 actually performs, so I didn't weight the new label as heavily as what I already had. I trimmed the Friday run slightly rather than overhauling the plan.  Interviewer: What would have had to be different in that assessment for you to change the schedule more substantially?  Participant: Probably if the language had been stronger — something like an explicit downtime risk instead of 'elevated concern' — or if it had come earlier in the week when I had more room to maneuver.  Interviewer: What actually happened with Press 3 and the shipments that week?  Participant: Press 3 finished the week without failing. The reliability engineer did file a formal recommendation to reduce loading next cycle. Shipments went out on time to all three plants.  Interviewer: If that Monday flag had appeared directly inside your scheduling dashboard instead of arriving as a separate message from the scheduling assistant, do you think the allocation decision would have gone differently?  Participant: Possibly. If it had been sitting right there next to the throughput numbers instead of coming in as a separate note, I think I'd have paused longer on it instead of leaning mainly on the report.  Interviewer: If you'd had unlimited time that week, is there anything you'd have checked differently?  Participant: I'd have pulled the full trend log Thursday instead of going off the single update, and I probably would have called around to compare backup suppliers instead of just going with who I knew.  Interviewer: Last one — looking back, what's one thing about how information reached you that you'd want changed?  Participant: Honestly, just having the maintenance advisories show up in full where I'm already doing my scheduling. Right now I mostly get a quick flag and have to go looking for the rest, and that week, I didn't.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.11s · gen 150.19s · total 154.8s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0284 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0264 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0248 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0238 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0237 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0230 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0217 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0202 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0196 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0191 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0189 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0186 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
15. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0186 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0185 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0178 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
20. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
22. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0164 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
23. **Lyell Automation bias and verification complexity.pdf** — 0.0163 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
24. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0163 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0162 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
34. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0149 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
35. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
37. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0146 (rrf) — _# 4 Anchoring bias Lieder et al., 2018) suggests that after being anchored, humans tend to adjus_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
40. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0143 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
42. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0142 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
43. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0142 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
44. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0138 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0137 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0137 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
48. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0136 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0134 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Routine debrief of scheduling decisions during a disruption. Analysis restricted to mechanisms affirmatively evidenced in the participant's reasoning."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": ["anchoring heuristic", "insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "Making estimates based on an initial value or anchor and then adjusting insufficiently from it when new information arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Monday allocation of full extra batch to Press 3",
      "decision_point_description": "Whether to allocate the entire extra high-volume bracket batch to Press 3 despite the open vibration advisory.",
      "affected_reasoning_operation": "Capacity/risk assessment and allocation decision for Press 3",
      "bias_specific_mechanism": "The prior week's throughput report showing Press 3 ran above target served as an easily available, concrete initial estimate of Press 3 capacity. The participant then adjusted only weakly from that anchor after seeing the vibration advisory, treating the advisory as vague/low-priority relative to the throughput evidence.",
      "manifestation_in_interview": "The participant repeatedly framed the throughput report as the direct answer to the capacity question and the vibration flag as vague and low-priority, saying the throughput report 'carried more weight.'",
      "effect_on_reasoning_or_decision": "The full extra batch was allocated to Press 3 despite the vibration advisory; the alternatives of splitting the batch or pushing part of the order were rejected.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pulled up last week's throughput report and Press 3 had actually run above target, so capacity-wise it looked like the obvious answer.",
          "evidence_explanation": "This shows the throughput report formed the initial anchor for the capacity judgment before the vibration flag was integrated."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The flag was there, but it was low-priority and vague next to a full week of solid output numbers, so the throughput report just carried more weight for me.",
          "evidence_explanation": "This explicitly describes insufficient adjustment from the anchor: the advisory was not weighted in proportion to its possible risk because the anchor evidence seemed stronger and more concrete."
        }
      ],
      "correction_or_counterevidence": "The participant did consider splitting the batch or deferring part of the order, and the vibration flag was characterized as low-priority and vague; these are legitimate decision features, but the transcript still shows the throughput estimate dominating the final judgment.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label is grounded in retrieved passages on anchoring and adjustment from the verification and validation corpus and the Rastogi et al. AI decision-making paper.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, “adjustments are typically insufficient.”",
          "mechanism_supported_by_source": "The passage defines anchoring-and-adjustment as an initial estimate followed by typically insufficient adjustments from additional information.",
          "relevance_to_this_occurrence": "The participant used the throughput report as the initial answer and made an insufficient adjustment for the vibration advisory, matching this mechanism."
        },
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment... ipants’ likelihood of sufficiently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports anchoring and adjustment as a cognitive heuristic relevant to decision-making under time constraints.",
          "relevance_to_this_occurrence": "The participant was making a scheduling decision under time constraints and anchored on the throughput report rather than fully adjusting to the advisory."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["expectation bias", "confirmatory bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, or weight information in ways that support existing beliefs or expectations, including discounting contradictory information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Tuesday supplier delay response",
      "decision_point_description": "Whether to treat the supplier's four-day delay as business-as-usual and wait, or to order backup stock immediately.",
      "affected_reasoning_operation": "Interpretation of supplier delay communication and causal attribution of delay",
      "bias_specific_mechanism": "The participant activated a prior expectation based on two previous supplier delays around late December and late June. He then interpreted the current supplier's phrase 'internal allocation constraints' as the supplier's usual wording rather than as diagnostic information about this particular delay, thereby discounting information that did not fit the expected pattern.",
      "manifestation_in_interview": "The participant said the timing itself was 'the tell' and that the phrase 'internal allocation constraints' sounded like 'the kind of thing they always say', so it did not register as pointing to something different.",
      "effect_on_reasoning_or_decision": "He decided to wait rather than order backup stock immediately and only made a reserve contact with the habitual supplier.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought was, 'this looks like the same thing that happened in December and June.'",
          "evidence_explanation": "This reveals the prior expectation that shaped interpretation of the new supplier delay."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The pattern matched what I'd seen twice before with this supplier, so I expected a similar resolution — to me the timing itself was the tell, more than anything they actually said. Their rep's line about 'internal allocation constraints' sounded like the kind of thing they always say around these stretches, so it didn't register as pointing to anything different this time.",
          "evidence_explanation": "This is the mechanism: the current diagnostic information was discounted as routine wording because it conflicted with the previously activated expectation."
        }
      ],
      "correction_or_counterevidence": "The previous delays did resolve without backup stock, and the participant did contact a reserve supplier, so the decision was not completely unsupported; however, the explicit discounting of the supplier's current wording remains evidence of confirmation bias.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved parasuraman-manzey passage links confirmation bias to discounting contradictory information.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "discounting of contradictory information. In addition, an explanation in terms of confirmation bias in processing the sampled information or difficulties of comprehension is also unlikely, given that the participants were very well trained and that the system parameter always contradicted the aid’s diagnosis in an unequivocal way.",
          "mechanism_supported_by_source": "The passage explicitly connects confirmation bias to discounting contradictory information during decision making.",
          "relevance_to_this_occurrence": "The participant discounted the supplier's 'internal allocation constraints' statement as routine wording, consistent with confirmation-biased discounting of information that does not fit prior expectation."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["plan continuation error", "get-there-itis"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an original plan or course of action despite new information that suggests the plan should be reconsidered or changed.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Friday final schedule decision after elevated concern",
      "decision_point_description": "Whether to materially reallocate Press 3 volume after engineering upgraded the vibration concern to 'elevated concern.'",
      "affected_reasoning_operation": "Choice to maintain or revise the committed schedule",
      "bias_specific_mechanism": "The participant had a committed plan already confirmed with downstream plants. When the risk label escalated, he emphasized lock-in and changeover cost and kept the plan mostly intact, exhibiting plan continuation rather than a proportional re-evaluation of the new risk information.",
      "manifestation_in_interview": "The participant said the schedule was 'basically locked', downstream plants already had confirmation, and shifting volume would cost hours; he only trimmed Friday's run slightly.",
      "effect_on_reasoning_or_decision": "The final schedule remained largely unchanged for Press 3 despite the elevated concern, with only a slight trim.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we were locked in with the downstream plants, and a full reallocation meant hours of changeover we didn't have room for.",
          "evidence_explanation": "This shows the commitment to the existing plan and perceived cost of changing course, which is the core of plan continuation bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I trimmed the Friday run slightly rather than overhauling the plan.",
          "evidence_explanation": "This demonstrates that the plan was continued with only a minimal adjustment despite the explicit risk escalation."
        }
      ],
      "correction_or_counterevidence": "Downstream confirmations and changeover cost are real operational constraints, so plan continuation is inferred from the minimal response to the explicit risk escalation rather than from the constraints alone.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The O'Connor aviation-cockpit corpus passage lists plan continuation as one of the cognitive biases identified in incident reports.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit: A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation , and in some cases multiple biases",
          "mechanism_supported_by_source": "The source identifies plan continuation as a recognized cognitive bias in operational incidents.",
          "relevance_to_this_occurrence": "The participant continued with the original schedule despite an elevated risk signal, resembling the plan-continuation pattern described in the source."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": ["anchoring heuristic", "insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "Making estimates based on an initial value or anchor and then adjusting insufficiently from it when new information arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Friday interpretation of elevated concern update",
      "decision_point_description": "Whether to treat the engineer's 'elevated concern' update as a meaningful increase in loading risk, requiring revision of the earlier assessment.",
      "affected_reasoning_operation": "Risk assessment of Press 3 after the status upgrade",
      "bias_specific_mechanism": "The initial anchor from Monday's throughput report and the recent clean weekend run persisted into Friday. The participant under-adjusted from that earlier 'Press 3 is performing well' anchor when the engineer provided a clear risk escalation, so the new label was weighted less heavily than the prior performance data.",
      "manifestation_in_interview": "The participant explicitly said the earlier data still felt like 'the more solid read' and that he did not weight the new label as heavily as what he already had.",
      "effect_on_reasoning_or_decision": "The elevated concern was underweighted, contributing to only a minor adjustment in the final schedule.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Even with the engineer telling me it reflected a real risk increase, the earlier data — the throughput numbers, the clean weekend run — still felt like the more solid read on how Press 3 actually performs, so I didn't weight the new label as heavily as what I already had.",
          "evidence_explanation": "This explicitly shows under-adjustment from the earlier performance anchor despite receiving a clear risk upgrade."
        }
      ],
      "correction_or_counterevidence": "The participant did trim the Friday run slightly, indicating partial adjustment, and the 'elevated concern' was not an explicit downtime warning.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The same retrieved anchoring-and-adjustment passages support this later under-adjustment from the earlier throughput anchor.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, “adjustments are typically insufficient.”",
          "mechanism_supported_by_source": "The passage defines anchoring-and-adjustment as an initial estimate followed by typically insufficient adjustments from additional information.",
          "relevance_to_this_occurrence": "The participant maintained the earlier throughput/weekend-run estimate and insufficiently adjusted to the new 'elevated concern' label."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": ["status quo bias", "default effect"],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Backup supplier contact selection",
      "supporting_interview_quote": "Honestly, it's the one I already had a relationship with. I didn't compare lead times or pricing against other options that morning — there wasn't a clean window to do that kind of comparison shopping with everything else going on.",
      "plausible_mechanism": "The participant chose the most available/familiar contact rather than conducting a comparative search, possibly reflecting ease-of-retrieval or status quo tendencies.",
      "why_not_identified": "The decision was also shaped by explicit time pressure and existing relationship/resource constraints; no clear bias-specific mechanism is affirmatively demonstrated beyond a legitimate operational choice."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "information avoidance",
      "alternative_labels": ["ostrich effect"],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Thursday decision not to open full vibration trend log",
      "supporting_interview_quote": "I had the update in front of me, and I made a call not to dig further right then. If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line than a single number did, and that could have meant reworking Friday's plan on top of everything else already moving.",
      "plausible_mechanism": "The participant may have avoided information that could force plan revision, consistent with information avoidance or motivated reasoning.",
      "why_not_identified": "The statement also reflects ordinary prioritization under workload, and the candidate mechanism is not strongly evidenced by the retrieved corpus."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring and adjustment",
      "alternative_labels": ["availability heuristic"],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Thursday assessment of vibration severity against Press 1 fire reference",
      "supporting_interview_quote": "I was thinking of the Press 1 fire from a couple years ago — that's the reference point that comes to mind when someone says 'press failure.' This didn't look anything like that, so it didn't register as urgent.",
      "plausible_mechanism": "The participant anchored the concept of 'serious press problem' on a dramatic prior event and may have underweighted the current vibration signal because it did not resemble that event.",
      "why_not_identified": "The use of a severe past event as a comparison could be a reasonable risk calibration rather than a clearly evidenced bias, and no retrieved passage specifically supports this exact mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Some corpus passages were partially garbled by OCR; only exact retrieved snippets are used.",
    "The participant's account is retrospective, so reporting may contain some post hoc rationalization not separately classified.",
    "Operational constraints such as changeover cost and downstream commitments provide alternative explanations for some Friday decisions, addressed per occurrence."
  ]
}

