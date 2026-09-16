# RAG Benchmark — 2026-09-15

## Gemini Prompt 8192

**Q1:** **Interviewer:** Thanks for taking the time. Just to confirm — this is a cognitive task analysis interview, it's confidential, and I'll be asking you to reconstruct a specific incident in detail. There's no evaluation of your performance here, just your reasoning process. Can you start by telling me your role and roughly when this happened? **Participant:** Sure. I'm a process safety engineer at the site — I cover the batch nitration unit among others. This was about four months ago, night shift transition. I'd just come on when the trend started. **Interviewer:** Good. Before we get into the sequence, what was the operational objective that shift? **Participant:** Straightforward — get the batch through its exothermic hold step cleanly and into the next unit operation without deviation, so we could hand off a clean batch at shift change. Nothing unusual planned. **Interviewer:** Walk me through what first drew your attention to the reactor. **Participant:** The DCS trend. Pressure was running about eight percent above the expected curve for that stage of the hold. Temperature was fine, right in band, which is usually the first thing you check because if temperature's climbing too you're thinking runaway. It wasn't. So it read more like an instrumentation quirk than a reaction problem, at least on the surface. **Interviewer:** What did you do with that information? **Participant:** Well, by the time I'd pulled up the trend, the shift supervisor and two operators were already standing around the panel talking about it. And honestly, that conversation shaped things a lot. Someone said 'this looks like the same thing we saw in March,' and someone else agreed, and by the time I'd joined in, the feeling in the room was pretty settled — everyone was more confident it was benign than any one of us probably was on our own five minutes earlier. I remember thinking, going into that conversation, I wasn't sure, but coming out of it I felt fairly sure. We'd had two prior deviations like this, both chalked up to sensor drift, no incident either time. That history was doing a lot of work in the room. **Interviewer:** So what was the actual decision at that point — stop the batch, escalate, or continue? **Participant:** Continue monitoring. We didn't interrupt. Looking back, the alternative was to call an emergency hold pending manual inspection, or escalate straight to the on-call plant manager. I didn't push for either. The shared read in the room was 'probably the same sensor issue,' and that's the frame I went with. **Interviewer:** What happened next? **Participant:** Pressure kept climbing, slowly, over about twenty minutes. Eventually the relief valve lifted — you could hear it, a distinct pop — and then pressure fell back and reseated. No release beyond the relief line, nobody hurt. But at that point we genuinely didn't know if the batch chemistry itself was compromised. **Interviewer:** How did you move from 'we had a relief lift' to a root cause? **Participant:** I concluded fairly quickly it was the same sensor drift pattern we'd seen before. It matched — same unit, same kind of gradual pressure creep, no temperature excursion. A full instrument and kinetics review would've taken three to four hours, and that would blow past shift changeover, so there was real pressure to land on something workable. **Interviewer:** Did anything about this batch differ from the two prior 'drift' events? **Participant:** Yeah, actually — this batch was running a newer catalyst lot. Neither of the earlier drift events used that lot. I knew that going in, but I didn't weight it heavily. It looked enough like the earlier pattern that I was comfortable calling it drift without waiting on the fuller review. **Interviewer:** How confident were you in that diagnosis at the time? **Participant:** Fairly confident, honestly. I've been on this unit a long time, I've seen this signature before. It felt like a case I recognized rather than a case I needed to dig into further. **Interviewer:** What did you learn afterward that touched on that conclusion? **Participant:** A partial calibration spot-check later showed the transmitter was actually within tolerance. That undercuts the drift explanation somewhat. And nobody had gone back and independently reviewed the new catalyst lot's exotherm profile. So the diagnosis I'd settled on quickly was never really closed out on the chemistry side. **Interviewer:** Let's move to the mitigation decision. What options were in front of you? **Participant:** The external relief-system contractor reviewed the incident and came back with a data package showing our existing relief system had a narrower margin than we'd assumed, specifically for this catalyst lot. Their recommendation was to add an automated high-pressure interlock trip before restart. It's a system with a decent track record at two comparable plants. The alternative was keeping our current manual response procedure, which has run for years here without failure. **Interviewer:** What did you decide? **Participant:** I recommended keeping the manual procedure for this restart. The interlock wasn't something our operators had hands-on familiarity with, and introducing something new felt like it carried its own risk profile that we hadn't lived with yet. Our manual process, whatever its limits, was a known quantity. **Interviewer:** How did you weigh the contractor's margin data against that operational familiarity? **Participant:** I didn't dismiss the margin data, I just — I think I gave more weight to the fact that the interlock was unproven here specifically, on our unit, with our people. The margin reduction was real on paper, but it hadn't caused an actual failure yet either. The known system winning out over the new one felt like the safer bet. **Interviewer:** Any information afterward relevant to that call? **Participant:** The plant manager pointed out later that adding the interlock then would've cost about one shift of downtime, versus none for keeping status quo. And no further excursions happened for the rest of the campaign, so we never really got a clean test of whether the interlock would've mattered. **Interviewer:** Take me into the MOC meeting. Who was there and what was the disagreement? **Participant:** Myself, the senior process safety engineer — he was on the original commissioning team for this unit, well known across the plant for a strong safety record — and the contractor. The senior engineer backed my sensor-drift read, said it matched his experience with the unit over the years. The contractor's written analysis flagged the catalyst-lot kinetics as an open gap and recommended keeping the MOC open until that was resolved. No new data had come in since the calibration check. **Interviewer:** How did you resolve that? **Participant:** I sided with the senior engineer's view. He's someone I've worked alongside for years, part of the original team that built this unit — that carries weight with me, knowing he's lived with this reactor longer than most people on-site. And frankly, his overall safety record here is excellent, so when he says something lines up with his experience, I tend to trust that assessment even without new numbers behind it. The contractor's point was on paper, but it felt like an outside read compared to someone who's actually run this unit for fifteen years. **Interviewer:** What happened after the MOC closed? **Participant:** We restarted without the kinetics review. Production since then hasn't clearly proven or disproven that call either way. **Interviewer:** Looking back across the shift, where did time pressure weigh most heavily? **Participant:** Definitely the root cause call and the MOC closure — both had that shift-changeover clock running, and neither had a hard deadline forcing an answer, but it felt like there was one. **Interviewer:** If the contractor's report had arrived before the control-room discussion instead of after, do you think the outcome changes? **Participant:** Possibly. If that margin data had been sitting on the table before everyone converged on 'probably fine,' it might have slowed the room down. Order mattered more than I'd like to admit. **Interviewer:** If a less senior colleague had proposed the sensor-drift explanation in that MOC meeting, would you have accepted it as readily? **Participant:** Probably not with the same confidence, no. **Interviewer:** What would you do differently with a similar deviation on a new catalyst lot? **Participant:** Flag the lot change explicitly, early, before pattern-matching to prior events — treat it as its own case rather than assuming it inherits the old explanation.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.49s · gen 158.13s · total 163.1s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0305 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0282 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0264 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0260 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0254 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0253 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
7. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0238 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0234 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0228 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
10. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0228 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0204 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
12. **Lyell Automation bias and verification complexity.pdf** — 0.0203 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
14. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0200 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0193 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0181 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0178 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
20. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0178 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0177 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
23. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0176 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
24. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0173 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0168 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
28. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0167 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
29. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0167 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
30. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0166 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0166 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
32. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
33. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
34. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0162 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
35. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0162 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0156 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
39. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0154 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
40. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0151 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
41. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0150 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
43. **Hallihan_etal_DTM_12.pdf** — 0.0147 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
44. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0146 (rrf) — _## Influence of Cognitive Biases in Distorting Decision Making and Leading to Critical Unfavorab_
45. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0145 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
46. **Hallihan_etal_DTM_12.pdf** — 0.0145 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
47. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0144 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs opinions when presented with new eviden_
48. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0141 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
49. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0140 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the participant's retrospective reconstruction of a process safety deviation for affirmative, mechanism-grounded cognitive bias indications; only self-reported reasoning and decision-making were assessed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bandwagon effect",
      "alternative_labels": [
        "social proof",
        "conformity bias",
        "groupthink"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to adopt a belief or decision because others have adopted it, creating a group consensus that can amplify confidence beyond what the individual evidence supports.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial pressure-deviation assessment and control-room discussion",
      "decision_point_description": "Whether to continue monitoring the reactor versus calling an emergency hold or escalating to the on-call plant manager.",
      "affected_reasoning_operation": "Risk assessment and escalation decision",
      "bias_specific_mechanism": "The presence of the shift supervisor and two operators agreeing on a prior-event interpretation produced a shared consensus that moved the participant from initial uncertainty to subjective confidence without new technical data.",
      "manifestation_in_interview": "The participant described entering the discussion uncertain, but after hearing others label the event as the same March sensor issue, he adopted the group frame and did not push for escalation.",
      "effect_on_reasoning_or_decision": "The participant did not call an emergency hold or escalate to the on-call plant manager and instead continued monitoring.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Well, by the time I'd pulled up the trend, the shift supervisor and two operators were already standing around the panel talking about it. And honestly, that conversation shaped things a lot. Someone said 'this looks like the same thing we saw in March,' and someone else agreed, and by the time I'd joined in, the feeling in the room was pretty settled — everyone was more confident it was benign than any one of us probably was on our own five minutes earlier.",
          "evidence_explanation": "This directly shows a group consensus forming around a prior-event interpretation and the participant attributing increased confidence to the conversation rather than to new technical evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking, going into that conversation, I wasn't sure, but coming out of it I felt fairly sure.",
          "evidence_explanation": "This explicitly documents a shift from uncertainty to confidence after exposure to the group view, which is the core mechanism of social-proof-driven belief adoption."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The shared read in the room was 'probably the same sensor issue,' and that's the frame I went with.",
          "evidence_explanation": "This shows that the participant adopted the consensus frame as the basis for his subsequent decision."
        }
      ],
      "correction_or_counterevidence": "No direct correction was reported during the control-room discussion. The later relief-valve lift showed that the shared benign interpretation may have been premature, but the bias mechanism here concerns social influence on confidence and decision framing, not the eventual outcome.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly operationalized this bias; classification is based on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment heuristic",
      "alternative_labels": [
        "representativeness heuristic",
        "availability heuristic",
        "confirmation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A judgment heuristic in which an initial value, prior belief, or familiar pattern serves as an anchor, and subsequent estimates or interpretations are insufficiently adjusted away from that anchor in light of new information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Deviation assessment and post-relief root-cause diagnosis",
      "decision_point_description": "Whether to attribute the pressure deviation and subsequent relief-valve lift to sensor drift or to treat the new catalyst lot as a distinct chemistry concern warranting fuller review.",
      "affected_reasoning_operation": "Causal diagnosis and evidence weighting",
      "bias_specific_mechanism": "The prior sensor-drift diagnosis from earlier events served as an anchor for interpreting the current pressure signature. The participant recognized that the current batch used a new catalyst lot but did not sufficiently adjust the diagnosis away from the anchor, and therefore did not pursue a fuller chemistry review.",
      "manifestation_in_interview": "The participant repeatedly matched the current pressure pattern to prior drift events, explicitly acknowledged the new catalyst-lot difference, but stated that he did not weight it heavily and felt comfortable calling the event drift without waiting for fuller review.",
      "effect_on_reasoning_or_decision": "The participant settled on sensor drift as the root cause and did not independently review the new catalyst lot's exotherm profile, leaving the chemistry side of the diagnosis unresolved.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd had two prior deviations like this, both chalked up to sensor drift, no incident either time. That history was doing a lot of work in the room.",
          "evidence_explanation": "This establishes that the prior drift diagnosis was the dominant initial reference point for interpreting the current event."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I concluded fairly quickly it was the same sensor drift pattern we'd seen before. It matched — same unit, same kind of gradual pressure creep, no temperature excursion.",
          "evidence_explanation": "This shows an initial diagnosis anchored on similarity to prior events rather than a search for differential features."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, actually — this batch was running a newer catalyst lot. Neither of the earlier drift events used that lot. I knew that going in, but I didn't weight it heavily. It looked enough like the earlier pattern that I was comfortable calling it drift without waiting on the fuller review.",
          "evidence_explanation": "This is the strongest evidence of insufficient adjustment: the participant had a diagnostic feature that distinguished the current batch from prior events but explicitly underweighted it."
        }
      ],
      "correction_or_counterevidence": "A later partial calibration spot-check showed the transmitter was within tolerance, which undercut the drift explanation. The participant also acknowledged that the catalyst-lot exotherm profile was never independently reviewed. However, this post-hoc information was not available at the time of the initial diagnosis.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus contains a description of anchoring and adjustment in engineering reasoning, which supports the mechanism of an initial known answer dominating later judgment.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described by Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information... 'adjustments are typically insufficient.' One arena in engineering where this can be seen is in the use of socalled 'heritage'. The component, system, or concept level, the initial answer people have in mind when they first consider a problem can dominate the entire development process.",
          "mechanism_supported_by_source": "An initial answer or known design can anchor subsequent engineering judgment, and adjustment from that anchor is typically insufficient even when new information becomes available.",
          "relevance_to_this_occurrence": "The participant anchored on the prior sensor-drift pattern and insufficiently adjusted away from it after recognizing the new catalyst lot, which parallels the anchoring process described in the retrieved passage."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "authority bias",
      "alternative_labels": [
        "halo effect",
        "expert deference"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to attribute greater accuracy or credibility to an authority figure or experienced source and to be unduly influenced by their opinion, independent of the quality of the supporting evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "MOC disagreement resolution",
      "decision_point_description": "Whether to close the MOC despite the contractor's written analysis flagging catalyst-lot kinetics as an unresolved gap, or to keep the MOC open pending further review.",
      "affected_reasoning_operation": "Evidence evaluation and source weighting",
      "bias_specific_mechanism": "The senior engineer's experience and strong safety record were used as a heuristic to validate his sensor-drift view, leading the participant to discount the contractor's written analysis even though no new data had resolved the disagreement.",
      "manifestation_in_interview": "The participant sided with the senior engineer based on the engineer's long unit experience and excellent safety record, explicitly saying he trusted that assessment without new numbers. He also acknowledged he would not accept the same explanation as readily from a less senior colleague.",
      "effect_on_reasoning_or_decision": "The MOC was closed and the unit restarted without the kinetics review, despite the contractor's open gap.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I sided with the senior engineer's view. He's someone I've worked alongside for years, part of the original team that built this unit — that carries weight with me, knowing he's lived with this reactor longer than most people on-site.",
          "evidence_explanation": "This shows that source status and personal history, rather than new evidence, drove the decision to side with the senior engineer."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "his overall safety record here is excellent, so when he says something lines up with his experience, I tend to trust that assessment even without new numbers behind it.",
          "evidence_explanation": "This explicitly demonstrates reliance on authority and reputation in place of new data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The contractor's point was on paper, but it felt like an outside read compared to someone who's actually run this unit for fifteen years.",
          "evidence_explanation": "This shows the participant discounting a written, data-based analysis in favor of a locally experienced authority figure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not with the same confidence, no.",
          "evidence_explanation": "In response to the interviewer's question about whether he would accept the same sensor-drift explanation from a less senior colleague, the participant confirms that his confidence depends on the source's seniority rather than solely on the evidence."
        }
      ],
      "correction_or_counterevidence": "Production since the restart did not clearly prove or disprove the decision. No new data was introduced in the MOC meeting, yet the participant treated the senior engineer's experience as sufficient to close the matter.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly operationalized this bias; classification is based on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "status quo bias",
      "alternative_labels": [
        "familiarity bias",
        "ambiguity aversion"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Mitigation decision after contractor review",
      "supporting_interview_quote": "I recommended keeping the manual procedure for this restart. The interlock wasn't something our operators had hands-on familiarity with, and introducing something new felt like it carried its own risk profile that we hadn't lived with yet. Our manual process, whatever its limits, was a known quantity.",
      "plausible_mechanism": "A preference for the current manual procedure and the known system over the new automated interlock, even in the presence of quantitative margin data favoring change.",
      "why_not_identified": "The preference for the known manual procedure may be explained by a legitimate, domain-appropriate safety risk assessment rather than a clear cognitive-bias distortion. The transcript does not contain enough evidence to distinguish status quo bias from reasonable risk-averse conservatism under operational uncertainty."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on retrospective self-report from a single participant, which may be affected by memory reconstruction or self-presentation.",
    "The retrieved corpus was sparse and did not cover all identified bias labels; some classifications rely on general cognitive-science knowledge rather than supplied passages.",
    "Some reasoning patterns in high-risk process safety contexts may reflect legitimate professional heuristics, so low-confidence or candidate treatment was used where non-bias explanations could not be ruled out."
  ]
}

## Sonar Prompt 8192

**Q1:** **Interviewer:** Thanks for taking the time. Just to confirm — this is a cognitive task analysis interview, it's confidential, and I'll be asking you to reconstruct a specific incident in detail. There's no evaluation of your performance here, just your reasoning process. Can you start by telling me your role and roughly when this happened? **Participant:** Sure. I'm a process safety engineer at the site — I cover the batch nitration unit among others. This was about four months ago, night shift transition. I'd just come on when the trend started. **Interviewer:** Good. Before we get into the sequence, what was the operational objective that shift? **Participant:** Straightforward — get the batch through its exothermic hold step cleanly and into the next unit operation without deviation, so we could hand off a clean batch at shift change. Nothing unusual planned. **Interviewer:** Walk me through what first drew your attention to the reactor. **Participant:** The DCS trend. Pressure was running about eight percent above the expected curve for that stage of the hold. Temperature was fine, right in band, which is usually the first thing you check because if temperature's climbing too you're thinking runaway. It wasn't. So it read more like an instrumentation quirk than a reaction problem, at least on the surface. **Interviewer:** What did you do with that information? **Participant:** Well, by the time I'd pulled up the trend, the shift supervisor and two operators were already standing around the panel talking about it. And honestly, that conversation shaped things a lot. Someone said 'this looks like the same thing we saw in March,' and someone else agreed, and by the time I'd joined in, the feeling in the room was pretty settled — everyone was more confident it was benign than any one of us probably was on our own five minutes earlier. I remember thinking, going into that conversation, I wasn't sure, but coming out of it I felt fairly sure. We'd had two prior deviations like this, both chalked up to sensor drift, no incident either time. That history was doing a lot of work in the room. **Interviewer:** So what was the actual decision at that point — stop the batch, escalate, or continue? **Participant:** Continue monitoring. We didn't interrupt. Looking back, the alternative was to call an emergency hold pending manual inspection, or escalate straight to the on-call plant manager. I didn't push for either. The shared read in the room was 'probably the same sensor issue,' and that's the frame I went with. **Interviewer:** What happened next? **Participant:** Pressure kept climbing, slowly, over about twenty minutes. Eventually the relief valve lifted — you could hear it, a distinct pop — and then pressure fell back and reseated. No release beyond the relief line, nobody hurt. But at that point we genuinely didn't know if the batch chemistry itself was compromised. **Interviewer:** How did you move from 'we had a relief lift' to a root cause? **Participant:** I concluded fairly quickly it was the same sensor drift pattern we'd seen before. It matched — same unit, same kind of gradual pressure creep, no temperature excursion. A full instrument and kinetics review would've taken three to four hours, and that would blow past shift changeover, so there was real pressure to land on something workable. **Interviewer:** Did anything about this batch differ from the two prior 'drift' events? **Participant:** Yeah, actually — this batch was running a newer catalyst lot. Neither of the earlier drift events used that lot. I knew that going in, but I didn't weight it heavily. It looked enough like the earlier pattern that I was comfortable calling it drift without waiting on the fuller review. **Interviewer:** How confident were you in that diagnosis at the time? **Participant:** Fairly confident, honestly. I've been on this unit a long time, I've seen this signature before. It felt like a case I recognized rather than a case I needed to dig into further. **Interviewer:** What did you learn afterward that touched on that conclusion? **Participant:** A partial calibration spot-check later showed the transmitter was actually within tolerance. That undercuts the drift explanation somewhat. And nobody had gone back and independently reviewed the new catalyst lot's exotherm profile. So the diagnosis I'd settled on quickly was never really closed out on the chemistry side. **Interviewer:** Let's move to the mitigation decision. What options were in front of you? **Participant:** The external relief-system contractor reviewed the incident and came back with a data package showing our existing relief system had a narrower margin than we'd assumed, specifically for this catalyst lot. Their recommendation was to add an automated high-pressure interlock trip before restart. It's a system with a decent track record at two comparable plants. The alternative was keeping our current manual response procedure, which has run for years here without failure. **Interviewer:** What did you decide? **Participant:** I recommended keeping the manual procedure for this restart. The interlock wasn't something our operators had hands-on familiarity with, and introducing something new felt like it carried its own risk profile that we hadn't lived with yet. Our manual process, whatever its limits, was a known quantity. **Interviewer:** How did you weigh the contractor's margin data against that operational familiarity? **Participant:** I didn't dismiss the margin data, I just — I think I gave more weight to the fact that the interlock was unproven here specifically, on our unit, with our people. The margin reduction was real on paper, but it hadn't caused an actual failure yet either. The known system winning out over the new one felt like the safer bet. **Interviewer:** Any information afterward relevant to that call? **Participant:** The plant manager pointed out later that adding the interlock then would've cost about one shift of downtime, versus none for keeping status quo. And no further excursions happened for the rest of the campaign, so we never really got a clean test of whether the interlock would've mattered. **Interviewer:** Take me into the MOC meeting. Who was there and what was the disagreement? **Participant:** Myself, the senior process safety engineer — he was on the original commissioning team for this unit, well known across the plant for a strong safety record — and the contractor. The senior engineer backed my sensor-drift read, said it matched his experience with the unit over the years. The contractor's written analysis flagged the catalyst-lot kinetics as an open gap and recommended keeping the MOC open until that was resolved. No new data had come in since the calibration check. **Interviewer:** How did you resolve that? **Participant:** I sided with the senior engineer's view. He's someone I've worked alongside for years, part of the original team that built this unit — that carries weight with me, knowing he's lived with this reactor longer than most people on-site. And frankly, his overall safety record here is excellent, so when he says something lines up with his experience, I tend to trust that assessment even without new numbers behind it. The contractor's point was on paper, but it felt like an outside read compared to someone who's actually run this unit for fifteen years. **Interviewer:** What happened after the MOC closed? **Participant:** We restarted without the kinetics review. Production since then hasn't clearly proven or disproven that call either way. **Interviewer:** Looking back across the shift, where did time pressure weigh most heavily? **Participant:** Definitely the root cause call and the MOC closure — both had that shift-changeover clock running, and neither had a hard deadline forcing an answer, but it felt like there was one. **Interviewer:** If the contractor's report had arrived before the control-room discussion instead of after, do you think the outcome changes? **Participant:** Possibly. If that margin data had been sitting on the table before everyone converged on 'probably fine,' it might have slowed the room down. Order mattered more than I'd like to admit. **Interviewer:** If a less senior colleague had proposed the sensor-drift explanation in that MOC meeting, would you have accepted it as readily? **Participant:** Probably not with the same confidence, no. **Interviewer:** What would you do differently with a similar deviation on a new catalyst lot? **Participant:** Flag the lot change explicitly, early, before pattern-matching to prior events — treat it as its own case rather than assuming it inherits the old explanation.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.98s · gen 166.28s · total 171.8s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0305 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0282 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0264 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0260 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0254 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0253 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
7. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0238 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0234 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0228 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
10. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0228 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0204 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
12. **Lyell Automation bias and verification complexity.pdf** — 0.0203 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
14. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0200 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0193 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0181 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0178 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
20. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0178 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0177 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
23. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0176 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
24. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0173 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0168 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
28. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0167 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
29. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0167 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
30. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0166 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0166 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
32. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
33. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
34. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0162 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
35. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0162 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0156 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
39. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0154 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
40. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0151 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
41. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0150 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
43. **Hallihan_etal_DTM_12.pdf** — 0.0147 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
44. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0146 (rrf) — _## Influence of Cognitive Biases in Distorting Decision Making and Leading to Critical Unfavorab_
45. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0145 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
46. **Hallihan_etal_DTM_12.pdf** — 0.0145 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
47. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0144 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs opinions when presented with new eviden_
48. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0141 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
49. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0140 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a process safety engineer's retrospective reconstruction of a high-pressure reactor deviation and subsequent diagnostic, mitigation, and MOC decisions; focus on reasoning mechanisms rather than performance evaluation."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Group polarization",
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
      "confidence": "high",
      "bias_label": "Group polarization",
      "alternative_labels": [
        "Bandwagon effect",
        "Social proof",
        "Conformity bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for discussion within a group to produce a position that is more extreme than the initial inclinations of individual group members.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Control-room discussion of pressure deviation",
      "decision_point_description": "Whether to continue monitoring versus stopping or escalating the batch",
      "affected_reasoning_operation": "Risk interpretation and escalation decision",
      "bias_specific_mechanism": "The participant reports that the group discussion shifted him from uncertainty to confidence and that the shared group view became more confident than any individual had been before the discussion, indicating group-level amplification of an initial benign interpretation.",
      "manifestation_in_interview": "The participant explicitly states that the room-level conversation shaped his interpretation and led him to adopt the shared benign sensor-drift frame.",
      "effect_on_reasoning_or_decision": "The amplified benign interpretation led the participant and the room to continue monitoring rather than stopping the batch or escalating to the on-call plant manager.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly, that conversation shaped things a lot. Someone said 'this looks like the same thing we saw in March,' and someone else agreed, and by the time I'd joined in, the feeling in the room was pretty settled — everyone was more confident it was benign than any one of us probably was on our own five minutes earlier.",
          "evidence_explanation": "This directly describes a group discussion producing greater confidence than individual pre-discussion judgments, which is the core mechanism of group polarization."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking, going into that conversation, I wasn't sure, but coming out of it I felt fairly sure.",
          "evidence_explanation": "This shows the participant's own judgment shifted from uncertainty toward confidence as a result of the group interaction."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The shared read in the room was 'probably the same sensor issue,' and that's the frame I went with.",
          "evidence_explanation": "This indicates that the group consensus became the decision frame for the participant's subsequent action."
        }
      ],
      "correction_or_counterevidence": "No explicit correction occurred during this episode; later calibration evidence weakened the drift explanation, but that was after the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable for this group-social mechanism; the label is used from general cognitive and social psychology.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "Anchoring heuristic",
        "Insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The heuristic whereby people make estimates or judgments based on an initial value, prior case, or first impression, and then adjust insufficiently from that anchor in light of subsequent information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-relief root-cause diagnosis",
      "decision_point_description": "Diagnosing the pressure excursion as sensor drift versus catalyst-lot kinetics",
      "affected_reasoning_operation": "Causal diagnosis and attribution",
      "bias_specific_mechanism": "The participant anchored on the previously observed sensor-drift pattern and did not sufficiently adjust for the new catalyst lot, which had not been used in those prior drift events.",
      "manifestation_in_interview": "The participant acknowledges knowing the catalyst lot was new and differed from prior drift events, but reports that he did not weight that information heavily because the case resembled the earlier pattern.",
      "effect_on_reasoning_or_decision": "The participant settled on the sensor-drift diagnosis without waiting for a full instrument and kinetics review, which influenced later restart and MOC decisions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "This batch was running a newer catalyst lot. Neither of the earlier drift events used that lot. I knew that going in, but I didn't weight it heavily. It looked enough like the earlier pattern that I was comfortable calling it drift without waiting on the fuller review.",
          "evidence_explanation": "This explicitly describes an initial pattern anchor and insufficient adjustment for a distinguishing feature, namely the new catalyst lot."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I concluded fairly quickly it was the same sensor drift pattern we'd seen before. It matched — same unit, same kind of gradual pressure creep, no temperature excursion.",
          "evidence_explanation": "This shows the diagnosis was driven by similarity to the previously anchored cases rather than by a full analysis of the current case."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I've been on this unit a long time, I've seen this signature before. It felt like a case I recognized rather than a case I needed to dig into further.",
          "evidence_explanation": "This indicates the prior recognized pattern dominated the reasoning process."
        }
      ],
      "correction_or_counterevidence": "A partial calibration spot-check later showed the transmitter was actually within tolerance, undercutting the drift explanation; no independent review of the new catalyst lot's exotherm profile had been performed.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passage from a space-flight verification and validation paper supports the anchoring and adjustment mechanism in engineering reasoning.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive Bias in the Verification and Validation of Space Flight Systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, \u201cadjustments are typic insufficient.\u201d",
          "mechanism_supported_by_source": "Anchoring on an initial value or prior answer, with subsequent adjustments that are typically insufficient.",
          "relevance_to_this_occurrence": "The participant anchored on prior sensor-drift cases and did not sufficiently adjust for the new catalyst lot before diagnosing the current deviation."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Status quo bias",
      "alternative_labels": [
        "Default bias",
        "Preference for current state"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to prefer the current or familiar state of affairs and to treat change or new options as riskier than they may be, even when evidence favors the alternative.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Mitigation decision after contractor review",
      "decision_point_description": "Whether to add an automated high-pressure interlock trip or retain the manual response procedure",
      "affected_reasoning_operation": "Risk-management choice between alternative mitigation strategies",
      "bias_specific_mechanism": "The participant overweighted the familiarity and known-ness of the existing manual procedure and treated the new interlock as riskier because it was not yet proven locally, despite contractor data showing a narrower margin.",
      "manifestation_in_interview": "The participant states that the known system defeating the new system felt like the safer bet and that he gave more weight to local unfamiliarity than to the margin data.",
      "effect_on_reasoning_or_decision": "The participant recommended keeping the manual procedure, so the interlock was not added before restart.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I recommended keeping the manual procedure for this restart. The interlock wasn't something our operators had hands-on familiarity with, and introducing something new felt like it carried its own risk profile that we hadn't lived with yet. Our manual process, whatever its limits, was a known quantity.",
          "evidence_explanation": "This expresses a preference for the existing procedure because it is known, while framing the new system as riskier due to unfamiliarity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I gave more weight to the fact that the interlock was unproven here specifically, on our unit, with our people. The margin reduction was real on paper, but it hadn't caused an actual failure yet either. The known system winning out over the new one felt like the safer bet.",
          "evidence_explanation": "This shows the participant weighted familiarity over the contractor's margin data, a hallmark of status quo preference."
        }
      ],
      "correction_or_counterevidence": "The plant manager later noted the interlock would have cost about one shift of downtime; no further excursions occurred, so the choice was not cleanly tested.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable for status quo bias; the label is used from general cognitive science.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Authority bias",
      "alternative_labels": [
        "Credential bias",
        "Halo effect",
        "Expert over-reliance"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to assign greater accuracy or credibility to the judgment of an authority or high-status person even when objective evidence is absent, weak, or in conflict.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "MOC meeting closure decision",
      "decision_point_description": "Whether to close the MOC despite the contractor's open catalyst-lot kinetics gap",
      "affected_reasoning_operation": "Evaluation of conflicting recommendations and safety-critical closure",
      "bias_specific_mechanism": "The participant accepted the senior engineer's sensor-drift judgment because of his tenure, commissioning-team membership, and safety record rather than because of new data; the participant explicitly says he would not give the same confidence to a less senior colleague.",
      "manifestation_in_interview": "The participant sided with the senior engineer's experience over the contractor's written analysis without new numbers supporting the senior engineer's position.",
      "effect_on_reasoning_or_decision": "The MOC was closed and restart proceeded without the kinetics review.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I sided with the senior engineer's view. He's someone I've worked alongside for years, part of the original team that built this unit — that carries weight with me, knowing he's lived with this reactor longer than most people on-site.",
          "evidence_explanation": "This shows the evaluation of the recommendation was based on the source's tenure and status rather than on the data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And frankly, his overall safety record here is excellent, so when he says something lines up with his experience, I tend to trust that assessment even without new numbers behind it.",
          "evidence_explanation": "This directly reports trusting the senior engineer's assessment without new data, which is the core authority-bias mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not with the same confidence, no.",
          "evidence_explanation": "This admission, in response to whether a less senior colleague would have been accepted as readily, shows the confidence was status-contingent."
        }
      ],
      "correction_or_counterevidence": "The contractor's written analysis flagged the catalyst-lot kinetics as an open gap and recommended keeping the MOC open; no new data had come in since the calibration check.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable for authority bias; the label is used from general cognitive science.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Miscalibration",
        "Overprecision"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-relief root-cause diagnosis",
      "supporting_interview_quote": "Fairly confident, honestly. I've been on this unit a long time, I've seen this signature before. It felt like a case I recognized rather than a case I needed to dig into further.",
      "plausible_mechanism": "Subjective confidence in the sensor-drift diagnosis may have exceeded the evidence available before a full review, especially given the new catalyst lot.",
      "why_not_identified": "The transcript does not include a clear probability estimate or direct evidence of miscalibration at the time; stated confidence could reflect legitimate expert recognition, so it remains only a candidate."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Single-interview retrospective self-report; memory and knowledge of later outcomes may color recall.",
    "Retrieved scientific corpus support was limited, especially for social, status quo, and authority mechanisms.",
    "No objective behavioral or decision records were available to verify the reasoning mechanisms.",
    "Several plausible biases overlap; labels were assigned conservatively to distinct episodes and mechanisms."
  ]
}

## Sonnet Prompt 8192

**Q1:** **Interviewer:** Thanks for taking the time. Just to confirm — this is a cognitive task analysis interview, it's confidential, and I'll be asking you to reconstruct a specific incident in detail. There's no evaluation of your performance here, just your reasoning process. Can you start by telling me your role and roughly when this happened? **Participant:** Sure. I'm a process safety engineer at the site — I cover the batch nitration unit among others. This was about four months ago, night shift transition. I'd just come on when the trend started. **Interviewer:** Good. Before we get into the sequence, what was the operational objective that shift? **Participant:** Straightforward — get the batch through its exothermic hold step cleanly and into the next unit operation without deviation, so we could hand off a clean batch at shift change. Nothing unusual planned. **Interviewer:** Walk me through what first drew your attention to the reactor. **Participant:** The DCS trend. Pressure was running about eight percent above the expected curve for that stage of the hold. Temperature was fine, right in band, which is usually the first thing you check because if temperature's climbing too you're thinking runaway. It wasn't. So it read more like an instrumentation quirk than a reaction problem, at least on the surface. **Interviewer:** What did you do with that information? **Participant:** Well, by the time I'd pulled up the trend, the shift supervisor and two operators were already standing around the panel talking about it. And honestly, that conversation shaped things a lot. Someone said 'this looks like the same thing we saw in March,' and someone else agreed, and by the time I'd joined in, the feeling in the room was pretty settled — everyone was more confident it was benign than any one of us probably was on our own five minutes earlier. I remember thinking, going into that conversation, I wasn't sure, but coming out of it I felt fairly sure. We'd had two prior deviations like this, both chalked up to sensor drift, no incident either time. That history was doing a lot of work in the room. **Interviewer:** So what was the actual decision at that point — stop the batch, escalate, or continue? **Participant:** Continue monitoring. We didn't interrupt. Looking back, the alternative was to call an emergency hold pending manual inspection, or escalate straight to the on-call plant manager. I didn't push for either. The shared read in the room was 'probably the same sensor issue,' and that's the frame I went with. **Interviewer:** What happened next? **Participant:** Pressure kept climbing, slowly, over about twenty minutes. Eventually the relief valve lifted — you could hear it, a distinct pop — and then pressure fell back and reseated. No release beyond the relief line, nobody hurt. But at that point we genuinely didn't know if the batch chemistry itself was compromised. **Interviewer:** How did you move from 'we had a relief lift' to a root cause? **Participant:** I concluded fairly quickly it was the same sensor drift pattern we'd seen before. It matched — same unit, same kind of gradual pressure creep, no temperature excursion. A full instrument and kinetics review would've taken three to four hours, and that would blow past shift changeover, so there was real pressure to land on something workable. **Interviewer:** Did anything about this batch differ from the two prior 'drift' events? **Participant:** Yeah, actually — this batch was running a newer catalyst lot. Neither of the earlier drift events used that lot. I knew that going in, but I didn't weight it heavily. It looked enough like the earlier pattern that I was comfortable calling it drift without waiting on the fuller review. **Interviewer:** How confident were you in that diagnosis at the time? **Participant:** Fairly confident, honestly. I've been on this unit a long time, I've seen this signature before. It felt like a case I recognized rather than a case I needed to dig into further. **Interviewer:** What did you learn afterward that touched on that conclusion? **Participant:** A partial calibration spot-check later showed the transmitter was actually within tolerance. That undercuts the drift explanation somewhat. And nobody had gone back and independently reviewed the new catalyst lot's exotherm profile. So the diagnosis I'd settled on quickly was never really closed out on the chemistry side. **Interviewer:** Let's move to the mitigation decision. What options were in front of you? **Participant:** The external relief-system contractor reviewed the incident and came back with a data package showing our existing relief system had a narrower margin than we'd assumed, specifically for this catalyst lot. Their recommendation was to add an automated high-pressure interlock trip before restart. It's a system with a decent track record at two comparable plants. The alternative was keeping our current manual response procedure, which has run for years here without failure. **Interviewer:** What did you decide? **Participant:** I recommended keeping the manual procedure for this restart. The interlock wasn't something our operators had hands-on familiarity with, and introducing something new felt like it carried its own risk profile that we hadn't lived with yet. Our manual process, whatever its limits, was a known quantity. **Interviewer:** How did you weigh the contractor's margin data against that operational familiarity? **Participant:** I didn't dismiss the margin data, I just — I think I gave more weight to the fact that the interlock was unproven here specifically, on our unit, with our people. The margin reduction was real on paper, but it hadn't caused an actual failure yet either. The known system winning out over the new one felt like the safer bet. **Interviewer:** Any information afterward relevant to that call? **Participant:** The plant manager pointed out later that adding the interlock then would've cost about one shift of downtime, versus none for keeping status quo. And no further excursions happened for the rest of the campaign, so we never really got a clean test of whether the interlock would've mattered. **Interviewer:** Take me into the MOC meeting. Who was there and what was the disagreement? **Participant:** Myself, the senior process safety engineer — he was on the original commissioning team for this unit, well known across the plant for a strong safety record — and the contractor. The senior engineer backed my sensor-drift read, said it matched his experience with the unit over the years. The contractor's written analysis flagged the catalyst-lot kinetics as an open gap and recommended keeping the MOC open until that was resolved. No new data had come in since the calibration check. **Interviewer:** How did you resolve that? **Participant:** I sided with the senior engineer's view. He's someone I've worked alongside for years, part of the original team that built this unit — that carries weight with me, knowing he's lived with this reactor longer than most people on-site. And frankly, his overall safety record here is excellent, so when he says something lines up with his experience, I tend to trust that assessment even without new numbers behind it. The contractor's point was on paper, but it felt like an outside read compared to someone who's actually run this unit for fifteen years. **Interviewer:** What happened after the MOC closed? **Participant:** We restarted without the kinetics review. Production since then hasn't clearly proven or disproven that call either way. **Interviewer:** Looking back across the shift, where did time pressure weigh most heavily? **Participant:** Definitely the root cause call and the MOC closure — both had that shift-changeover clock running, and neither had a hard deadline forcing an answer, but it felt like there was one. **Interviewer:** If the contractor's report had arrived before the control-room discussion instead of after, do you think the outcome changes? **Participant:** Possibly. If that margin data had been sitting on the table before everyone converged on 'probably fine,' it might have slowed the room down. Order mattered more than I'd like to admit. **Interviewer:** If a less senior colleague had proposed the sensor-drift explanation in that MOC meeting, would you have accepted it as readily? **Participant:** Probably not with the same confidence, no. **Interviewer:** What would you do differently with a similar deviation on a new catalyst lot? **Participant:** Flag the lot change explicitly, early, before pattern-matching to prior events — treat it as its own case rather than assuming it inherits the old explanation.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.76s · gen 110.13s · total 115.4s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0305 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0282 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0264 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0260 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0254 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0253 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
7. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0238 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0234 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0228 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
10. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0228 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0204 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
12. **Lyell Automation bias and verification complexity.pdf** — 0.0203 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
14. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0200 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0193 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0181 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0178 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
20. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0178 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0177 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
23. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0176 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
24. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0173 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0168 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
28. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0167 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
29. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0167 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
30. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0166 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0166 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
32. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
33. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
34. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0162 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
35. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0162 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0156 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
39. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0154 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
40. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0151 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
41. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0150 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
43. **Hallihan_etal_DTM_12.pdf** — 0.0147 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
44. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0146 (rrf) — _## Influence of Cognitive Biases in Distorting Decision Making and Leading to Critical Unfavorab_
45. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0145 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
46. **Hallihan_etal_DTM_12.pdf** — 0.0145 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
47. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0144 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs opinions when presented with new eviden_
48. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0141 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
49. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0140 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative mechanism-first analysis of a single CTA interview for cognitive, social-influence, and decision biases; no experimental condition or expected bias count assumed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "social proof",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "social proof",
      "alternative_labels": [
        "conformity",
        "consensus heuristic",
        "bandwagon effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A social-influence heuristic in which a person adopts or strengthens a belief because others in the group appear to hold it, increasing confidence beyond what the individual evidence would support.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Control-room discussion about abnormal reactor pressure",
      "decision_point_description": "Choosing to continue monitoring rather than stopping or escalating after the group converged on a benign sensor-issue explanation.",
      "affected_reasoning_operation": "Risk interpretation and initial deviation triage",
      "bias_specific_mechanism": "Informational social influence/consensus heuristic: observing agreement among the supervisor and operators transformed the participant's uncertainty into confidence and led him to adopt the group's frame as his own.",
      "manifestation_in_interview": "The participant described entering the discussion unsure, but after others labeled the pattern as the same March event and agreed, he came out feeling fairly sure it was benign. He then explicitly used the shared read as his decision frame.",
      "effect_on_reasoning_or_decision": "The group's shared confidence caused the participant to frame the deviation as probably the same sensor issue and choose continued monitoring rather than interrupting the batch, escalating, or calling for manual inspection.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly, that conversation shaped things a lot. Someone said 'this looks like the same thing we saw in March,' and someone else agreed, and by the time I'd joined in, the feeling in the room was pretty settled — everyone was more confident it was benign than any one of us probably was on our own five minutes earlier. I remember thinking, going into that conversation, I wasn't sure, but coming out of it I felt fairly sure.",
          "evidence_explanation": "This explicitly attributes the shift from uncertainty to confidence to the group's agreement rather than to new technical data or independent verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The shared read in the room was 'probably the same sensor issue,' and that's the frame I went with.",
          "evidence_explanation": "Shows that the group consensus became the participant's operative diagnosis and decision frame."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous dissent or debiasing was reported; the participant later acknowledged that if the contractor's margin data had arrived before the control-room discussion, it might have slowed the room down.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a clear, usable definition or mechanistic account for social proof/conformity; the label is assigned from general cognitive-science knowledge and no corpus citation is given.",
      "corpus_evidence": []
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
      "bias_definition": "The tendency to seek, interpret, or weight information in ways that support an existing hypothesis while underweighting or neglecting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-relief-valve root-cause diagnosis",
      "decision_point_description": "Diagnosing the pressure excursion as sensor drift rather than initiating a fuller instrument and kinetics review.",
      "affected_reasoning_operation": "Diagnostic hypothesis evaluation and evidence weighting",
      "bias_specific_mechanism": "Pattern-matching to prior events and treating the new catalyst lot as a minor detail; the participant selectively weighted confirmatory similarity and underweighted a specific disconfirming difference.",
      "manifestation_in_interview": "The participant concluded quickly that it was the same sensor-drift pattern because it matched prior events on unit and gradual pressure creep, despite knowing the batch used a new catalyst lot that prior drift events did not use.",
      "effect_on_reasoning_or_decision": "Produced premature diagnostic closure on sensor drift, so a full kinetics review was not pursued and the catalyst-lot gap remained open.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I concluded fairly quickly it was the same sensor drift pattern we'd seen before. It matched — same unit, same kind of gradual pressure creep, no temperature excursion.",
          "evidence_explanation": "The participant treats similarity to prior events as sufficient to confirm the drift hypothesis, illustrating confirmatory pattern matching."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, actually — this batch was running a newer catalyst lot. Neither of the earlier drift events used that lot. I knew that going in, but I didn't weight it heavily. It looked enough like the earlier pattern that I was comfortable calling it drift without waiting on the fuller review.",
          "evidence_explanation": "Explicitly acknowledges a disconfirming difference and states it was not weighted heavily, a core feature of confirmation bias in evidence evaluation."
        }
      ],
      "correction_or_counterevidence": "A later partial calibration spot-check showed the transmitter was within tolerance, undercutting the drift explanation, and no one independently reviewed the new catalyst lot's exotherm profile.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved passages mentioned confirmation bias only in a sparse or garbled form lacking a usable definition or mechanism; the label is assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "status quo bias",
      "alternative_labels": [
        "default bias",
        "familiarity preference"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for the current or familiar state, with risks and costs of change overweighted relative to risks of maintaining the status quo.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of restart mitigation approach",
      "decision_point_description": "Recommending the existing manual response procedure rather than adding the contractor-recommended automated high-pressure interlock before restart.",
      "affected_reasoning_operation": "Risk evaluation and option selection",
      "bias_specific_mechanism": "Status quo preference: the known manual procedure was judged safer because it was familiar, while the new interlock was discounted as unproven on this unit even though margin data favored it.",
      "manifestation_in_interview": "The participant acknowledged the margin reduction was real on paper but gave more weight to the interlock being unfamiliar here; the known system winning out felt like the safer bet.",
      "effect_on_reasoning_or_decision": "The restart proceeded with the manual procedure and no automated interlock, despite contractor data showing a narrower relief margin for this catalyst lot.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I recommended keeping the manual procedure for this restart. The interlock wasn't something our operators had hands-on familiarity with, and introducing something new felt like it carried its own risk profile that we hadn't lived with yet. Our manual process, whatever its limits, was a known quantity.",
          "evidence_explanation": "Choice is justified primarily by familiarity with the existing system and lack of familiarity with the new one, rather than by a comparative risk analysis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't dismiss the margin data, I just — I think I gave more weight to the fact that the interlock was unproven here specifically, on our unit, with our people. The margin reduction was real on paper, but it hadn't caused an actual failure yet either. The known system winning out over the new one felt like the safer bet.",
          "evidence_explanation": "Explicitly describes overweighting unfamiliarity and change risk while relying on current-state familiarity, a hallmark of status quo bias."
        }
      ],
      "correction_or_counterevidence": "The contractor's data package showed a narrower relief margin specifically for this catalyst lot and recommended an interlock; the participant acknowledged the margin reduction was real but did not act on it. Later, no further excursions occurred, so the decision was not cleanly tested.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed status quo bias or provided a usable mechanistic account; classification uses general cognitive-science knowledge without a corpus citation.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "authority bias",
      "alternative_labels": [
        "halo effect",
        "source-credibility bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to assign greater credibility to an opinion or claim because of the source's seniority, authority, or status, independent of the supporting evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "MOC meeting disagreement over sensor-drift closure",
      "decision_point_description": "Siding with the senior process safety engineer's experience-based sensor-drift view over the contractor's written analysis that identified the catalyst-lot kinetics gap.",
      "affected_reasoning_operation": "Evaluation of conflicting technical judgments",
      "bias_specific_mechanism": "Source-credibility/authority heuristic: the senior engineer's long tenure, original commissioning role, and strong overall safety record were used as a proxy for correctness on the specific sensor-drift claim, despite no new supporting data.",
      "manifestation_in_interview": "The participant stated that the senior engineer's experience and excellent safety record carry weight, leading him to trust the assessment without new numbers, while the contractor's analysis felt like an outside read.",
      "effect_on_reasoning_or_decision": "The MOC was closed without resolving the catalyst-lot kinetics gap, and restart proceeded without the kinetics review.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I sided with the senior engineer's view. He's someone I've worked alongside for years, part of the original team that built this unit — that carries weight with me, knowing he's lived with this reactor longer than most people on-site. And frankly, his overall safety record here is excellent, so when he says something lines up with his experience, I tend to trust that assessment even without new numbers behind it.",
          "evidence_explanation": "Demonstrates that the decision was driven by the source's seniority, history, and general reputation rather than new evidence specific to the claim."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not with the same confidence, no.",
          "evidence_explanation": "In response to the interviewer's question about a less senior colleague proposing the same explanation, this confirms that acceptance depends on the proposer's seniority and status, not only on technical content."
        }
      ],
      "correction_or_counterevidence": "The contractor's written analysis flagged the catalyst-lot kinetics as an open gap and recommended keeping the MOC open until resolved; no new data had arrived after the calibration check.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage provided a usable definition or mechanistic account for authority bias; the label is assigned from general cognitive-science knowledge without a corpus citation.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages were mostly sparse or OCR-damaged and did not provide directly usable definitions or mechanism-level support for any identified occurrence; classification for these specific labels therefore relies on general cognitive-science knowledge.",
    "The analysis relies on a single participant's retrospective self-report, so cognitive mechanisms are inferred from described reasoning and confidence shifts rather than direct behavioral observation.",
    "No independent confirmation of the group discussion, MOC disagreement, or decision outcomes was available within the transcript."
  ]
}

