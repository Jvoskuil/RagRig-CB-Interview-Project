# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about your decision-making during the last refueling outage, not a performance review. Everything you share is for process improvement. Can you tell me your role and roughly how long you've been doing outage coordination? Participant: Sure, happy to walk through it. I'm the maintenance planner and outage coordinator for the unit — been doing this specific role about six years, plus four years as a planner before that. My main job during the outage is to sequence work orders against the critical path, allocate craft-hours, and make sure everything closes out before we hit the mode change hold points. Interviewer: What made this particular outage stand out from a routine one? Participant: Honestly, the sheer volume — we had around 140 concurrent work orders competing for a fixed 21-day window, and craft-hours were tighter than usual because two contractor crews got pulled to another site mid-cycle. So there was a lot of juggling. The item that ended up taking more of my attention than I expected was FW-IV-204, one of our feedwater isolation valves. Interviewer: Take me through the sequence of events, from initial scoping to final return to service. Participant: At the start of scoping, FW-IV-204 had a minor packing weep — nothing new, it had shown up in two prior outage condition reports, both closed as acceptable-as-found. No trend showing it was getting worse. But right around scoping, I'd just heard a pretty detailed account from a colleague about a similar valve at a sister unit that failed and caused a multi-day slip to their critical path. That story was fresh in my head when I built the priority list. I bumped FW-IV-204 up to top-tier priority for rework. Then, once we got into execution, craft-hours were running thin one afternoon and I had to lock in a crew configuration fast for the valve job — Outage Manager wanted it settled within the hour. I went with the first configuration that cleared the minimum schedule and safety requirements. Later in the outage, during post-maintenance testing, we saw a mild vibration anomaly on the pump bearing right next to FW-IV-204. My first thought was residual misalignment from the rework we'd just done. I pulled vibration data that fit that theory, we closed it out, and eventually got system engineer concurrence and did the walkdown before returning the unit to service. Interviewer: Let's slow down and reconstruct the timeline in more detail. When exactly did FW-IV-204 first come onto your radar for this outage? Participant: Right at the outset of scoping, maybe day one or two of pre-outage planning. It was already on the work list from the prior cycle's CR, so it wasn't a surprise. What changed was how I ranked it relative to everything else. Interviewer: And the vibration anomaly — when did that surface relative to the valve work? Participant: That was maybe day fourteen, after the valve rework was already complete and we were running post-maintenance functional tests on the adjacent feedwater pump. Interviewer: Let's go through each of those decision points one at a time. First — the priority ranking. What information did you actually have in front of you when you made that call? Participant: I had the two prior CRs, both closed, no adverse trend on leak rate. I also had the backlog of other work orders, some with comparable or even higher CR severity ratings. Objectively, on paper, FW-IV-204 wasn't the most urgent thing on the list. Interviewer: So what tipped it to top-tier? Participant: The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me. I remember thinking, we don't want to be the ones explaining a multi-day slip because we treated this as routine. So I moved it up. Interviewer: Did you go back and re-check the trend data before finalizing that ranking? Participant: No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted. It felt like the kind of thing where the downside of being wrong was bad enough that I didn't need to. Interviewer: Understood. Second decision point — the crew configuration under the tight craft-hour window. Walk me through that. Participant: We were maybe two-thirds through the day's craft-hour budget, and I had several configurations that would technically work — different mixes of overtime, different sequencing with other jobs. The Outage Manager wanted a decision inside the hour to protect the critical path. I looked at the first configuration that met minimum schedule and safety requirements, confirmed it cleared those bars, and locked it in. Interviewer: Did you consider comparing the other options more fully? Participant: I thought about it, but comparing all the variables — overtime cost, fatigue limits, downstream sequencing — for three or four configurations would have eaten time I didn't have. So I went with what worked and moved to the next fire. Interviewer: What happened as a result? Participant: It created a minor sequencing conflict later with an unrelated pump job — nothing that blew the schedule, but craft had to shuffle around it. When we reviewed it afterward, there was a configuration that would have avoided that friction. Marginally better, not dramatically. Interviewer: Third decision point — the vibration anomaly. What was your first working theory? Participant: Residual misalignment from the valve rework. It made sense sequentially — we'd just had hands in that area, and a little post-maintenance vibration isn't unheard of. Interviewer: What data did you pull to check that theory? Participant: I asked for the immediate vibration readings from the test run, the ones that would show whether the signature matched a misalignment pattern. They looked consistent with that, so I documented the anomaly as resolved on that basis. Interviewer: Was there other data available that you didn't request at that point? Participant: In hindsight, yes. There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched. Interviewer: What about the full trend history for that bearing? Participant: Also didn't pull that at the time. The system engineer reviewed it later, after the fact. Interviewer: Last decision point — the final return-to-service call. What was your basis for concurring? Participant: By that point, all the CRs on the valve and the adjacent pump were formally closed, the system engineer had given written concurrence, and I did the walkdown myself with operations. Given the sign-offs and what I observed directly during the walkdown, I concurred with return to service. I did weigh the earlier vibration discussion against that documentation, but everything on paper and everything I saw in the field lined up, so I didn't see a basis to hold it further. Interviewer: Did you consider requesting extra monitoring time before mode change? Participant: I did think about it briefly, given the anomaly earlier in the outage, but with the engineering concurrence and a clean walkdown, holding the unit longer without a specific technical reason didn't seem justified. Interviewer: How much time pressure were you under across these decisions, generally? Participant: Constant, honestly, but it spiked hardest around the crew assignment call — that was the one hour deadline. The priority ranking and the vibration call had a bit more breathing room, even if it didn't always feel that way in the moment. Interviewer: If the lubrication log had been sitting on your desk when the vibration anomaly came up, do you think it would have changed your review? Participant: Possibly. If it had shown something inconsistent with misalignment, I probably would have widened the investigation. It just wasn't something I went looking for at the time. Interviewer: Looking back, is there a point where a different call on FW-IV-204's priority might have changed how things unfolded? Participant: Maybe. If I'd ranked it purely on the documented trend, it might have sat lower in the queue, and I'd have had more craft-hours free for other jobs earlier. Hard to say if that changes anything meaningfully, since the valve work itself went fine. Interviewer: Anything you'd tell a newer planner based on this outage? Participant: Mainly to keep coming back to the actual trend data, even when a recent story or a tight clock makes a different path feel more urgent. It's not that those instincts are wrong, just that they're easy to lean on more than the numbers warrant.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.86s · gen 180.57s · total 186.3s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0286 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0268 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0267 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0241 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0241 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0231 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0217 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0216 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
9. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0211 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
10. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0208 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0206 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
12. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0199 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0195 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
16. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0187 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
17. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
18. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0178 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0168 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0165 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
25. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0164 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
27. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0161 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0154 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
30. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0153 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
32. **Lyell Automation bias and verification complexity.pdf** — 0.0153 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
34. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0152 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
36. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0150 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0147 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
40. **Hallihan_etal_DTM_12.pdf** — 0.0145 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0144 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. C han, U. Dulleck et al. In the triage decisio_
42. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0142 (rrf) — _# 188 | to the one in the | explanation condition). Informed by prior work that a slow algorithm_
43. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0142 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 382 operators purp_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
47. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
49. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0138 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the interview transcript for affirmative, mechanism-grounded cognitive bias occurrences in maintenance outage decision-making. The transcript was treated as the sole factual authority; retrieved passages were used only for theoretical and taxonomic support."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
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
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive heuristic in which the judged likelihood, urgency, or importance of an event is inflated by the ease and vividness with which a similar instance is recalled from memory, rather than by objective base rates or documented trends.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "FW-IV-204 priority ranking during pre-outage scoping",
      "decision_point_description": "Ranking FW-IV-204 among approximately 140 concurrent work orders for a fixed 21-day outage window.",
      "affected_reasoning_operation": "Risk/urgency assessment and work-order prioritization",
      "bias_specific_mechanism": "A recent, detailed, emotionally consequential account of a sister-unit valve failure was highly available in memory and disproportionately weighted in the participant's subjective risk assessment, overriding the objective evidence that FW-IV-204 showed no adverse trend and was not the most urgent item on paper.",
      "manifestation_in_interview": "The participant explicitly stated that the valve was not objectively the most urgent on paper, but the vivid sister-unit story stuck with him and led him to move FW-IV-204 to top-tier priority without rechecking the trend data.",
      "effect_on_reasoning_or_decision": "Distorted allocation of scarce outage attention and craft-hours; FW-IV-204 received top-tier priority despite objective severity data not supporting that ranking.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Objectively, on paper, FW-IV-204 wasn't the most urgent thing on the list.",
          "evidence_explanation": "This statement establishes that the documented evidence did not support the extreme priority ranking, making the subsequent non-documentary influence salient."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me. I remember thinking, we don't want to be the ones explaining a multi-day slip because we treated this as routine. So I moved it up.",
          "evidence_explanation": "This quote directly shows that the recent, vivid sister-unit failure account, rather than FW-IV-204's own documented condition, drove the priority upgrade."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted.",
          "evidence_explanation": "This shows the participant did not seek objective trend data to test the urgency judgment, consistent with availability-based risk perception overriding systematic evidence review."
        }
      ],
      "correction_or_counterevidence": "The participant later reflected that ranking purely on the documented trend might have left the valve lower in the queue, but this retrospective acknowledgment occurred after the prioritization decision and did not correct the initial resource allocation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support for the availability heuristic was not present in the retrieved passages. Classification relies on established cognitive-science knowledge, particularly the availability heuristic as described by Tversky and Kahneman.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["positive test strategy"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's pre-existing hypothesis, while avoiding or underweighting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-maintenance vibration anomaly diagnosis for adjacent pump bearing",
      "decision_point_description": "Determining the cause and closure of a mild vibration anomaly observed near FW-IV-204 on approximately day 14 of the outage.",
      "affected_reasoning_operation": "Diagnostic causal inference and evidence search",
      "bias_specific_mechanism": "The participant formed an initial hypothesis of residual misalignment, then selectively requested and accepted vibration readings consistent with that hypothesis while not pulling contemporaneously available disconfirming data, including a lubrication log entry and the bearing trend history.",
      "manifestation_in_interview": "The participant documented the anomaly as resolved based on confirmatory vibration data and explicitly stated that he did not widen the search because the misalignment explanation already fit what he was seeing.",
      "effect_on_reasoning_or_decision": "The vibration anomaly was closed out on the basis of hypothesis-consistent data without evaluating available evidence that could have disconfirmed residual misalignment and suggested an alternative cause.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought was residual misalignment from the rework we'd just done.",
          "evidence_explanation": "This establishes the initial causal hypothesis that subsequently shaped the participant's evidence search."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I asked for the immediate vibration readings from the test run, the ones that would show whether the signature matched a misalignment pattern. They looked consistent with that, so I documented the anomaly as resolved on that basis.",
          "evidence_explanation": "This shows the participant sought data specifically designed to test for a match with the preferred explanation and then accepted confirming evidence as sufficient for closure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched.",
          "evidence_explanation": "This is direct affirmative evidence that available non-confirming information was not retrieved because the initial hypothesis already appeared supported."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Also didn't pull that at the time. The system engineer reviewed it later, after the fact.",
          "evidence_explanation": "This further confirms that trend history capable of testing the misalignment interpretation was neglected until after the participant had already made the closure decision."
        }
      ],
      "correction_or_counterevidence": "The system engineer later reviewed the bearing trend history after the participant had already documented the anomaly as resolved. This subsequent review did not prevent the initial confirmation-driven closure decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages mention confirmation bias in operational and engineering contexts, supporting confirmation bias as an established label and confirming its role in selective explanation maintenance.",
      "corpus_evidence": [
        {
          "source_identifier": "Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The retrieved passage discusses confirmation bias leading operators to believe a particular failure explanation and preventing them from noticing and identifying an alternative cause.",
          "mechanism_supported_by_source": "The source supports confirmation bias as a mechanism in which an initial interpretation is maintained and alternative explanations are not detected.",
          "relevance_to_this_occurrence": "The participant adhered to the residual-misalignment explanation and did not identify or seek an alternative lubrication-related cause despite available data."
        },
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The retrieved passage lists 'confirmation, expectation, and plan continuation' as cognitive biases identified in operational reports.",
          "mechanism_supported_by_source": "The source supports confirmation bias as a recognized operational cognitive bias.",
          "relevance_to_this_occurrence": "Supports the classification of the participant's hypothesis-consistent search and closure as confirmation bias in an operational maintenance setting."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring and adjustment",
      "alternative_labels": ["satisficing"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Crew configuration selection under one-hour deadline",
      "supporting_interview_quote": "I looked at the first configuration that met minimum schedule and safety requirements, confirmed it cleared those bars, and locked it in.",
      "plausible_mechanism": "The first acceptable configuration may have served as an anchor, with insufficient comparison to later alternatives leading to a marginally suboptimal choice and a later sequencing conflict.",
      "why_not_identified": "The behavior is also consistent with bounded-rational satisficing under explicit time pressure. The transcript does not provide affirmative evidence that a distinct anchoring distortion, rather than deadline-driven acceptance of a sufficient option, produced the decision."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final return-to-service concurrence",
      "supporting_interview_quote": "Given the sign-offs and what I observed directly during the walkdown, I concurred with return to service. I did weigh the earlier vibration discussion against that documentation, but everything on paper and everything I saw in the field lined up, so I didn't see a basis to hold it further.",
      "plausible_mechanism": "The participant may have preferentially weighted confirmatory documentation and clean walkdown observations while underweighting the earlier vibration anomaly as a reason to request additional monitoring.",
      "why_not_identified": "The decision followed formal engineering concurrence and a direct walkdown. There is insufficient affirmative evidence that a distinct confirmation-driven distortion, rather than ordinary reliance on completed checks and authority sign-off, caused the concurrence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus contained limited formal definitions and did not include substantive material on the availability heuristic; that classification relies on established cognitive-science knowledge.",
    "The analysis is constrained to the transcript record and does not include independent operational data to verify outcomes or competing explanations."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about your decision-making during the last refueling outage, not a performance review. Everything you share is for process improvement. Can you tell me your role and roughly how long you've been doing outage coordination? Participant: Sure, happy to walk through it. I'm the maintenance planner and outage coordinator for the unit — been doing this specific role about six years, plus four years as a planner before that. My main job during the outage is to sequence work orders against the critical path, allocate craft-hours, and make sure everything closes out before we hit the mode change hold points. Interviewer: What made this particular outage stand out from a routine one? Participant: Honestly, the sheer volume — we had around 140 concurrent work orders competing for a fixed 21-day window, and craft-hours were tighter than usual because two contractor crews got pulled to another site mid-cycle. So there was a lot of juggling. The item that ended up taking more of my attention than I expected was FW-IV-204, one of our feedwater isolation valves. Interviewer: Take me through the sequence of events, from initial scoping to final return to service. Participant: At the start of scoping, FW-IV-204 had a minor packing weep — nothing new, it had shown up in two prior outage condition reports, both closed as acceptable-as-found. No trend showing it was getting worse. But right around scoping, I'd just heard a pretty detailed account from a colleague about a similar valve at a sister unit that failed and caused a multi-day slip to their critical path. That story was fresh in my head when I built the priority list. I bumped FW-IV-204 up to top-tier priority for rework. Then, once we got into execution, craft-hours were running thin one afternoon and I had to lock in a crew configuration fast for the valve job — Outage Manager wanted it settled within the hour. I went with the first configuration that cleared the minimum schedule and safety requirements. Later in the outage, during post-maintenance testing, we saw a mild vibration anomaly on the pump bearing right next to FW-IV-204. My first thought was residual misalignment from the rework we'd just done. I pulled vibration data that fit that theory, we closed it out, and eventually got system engineer concurrence and did the walkdown before returning the unit to service. Interviewer: Let's slow down and reconstruct the timeline in more detail. When exactly did FW-IV-204 first come onto your radar for this outage? Participant: Right at the outset of scoping, maybe day one or two of pre-outage planning. It was already on the work list from the prior cycle's CR, so it wasn't a surprise. What changed was how I ranked it relative to everything else. Interviewer: And the vibration anomaly — when did that surface relative to the valve work? Participant: That was maybe day fourteen, after the valve rework was already complete and we were running post-maintenance functional tests on the adjacent feedwater pump. Interviewer: Let's go through each of those decision points one at a time. First — the priority ranking. What information did you actually have in front of you when you made that call? Participant: I had the two prior CRs, both closed, no adverse trend on leak rate. I also had the backlog of other work orders, some with comparable or even higher CR severity ratings. Objectively, on paper, FW-IV-204 wasn't the most urgent thing on the list. Interviewer: So what tipped it to top-tier? Participant: The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me. I remember thinking, we don't want to be the ones explaining a multi-day slip because we treated this as routine. So I moved it up. Interviewer: Did you go back and re-check the trend data before finalizing that ranking? Participant: No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted. It felt like the kind of thing where the downside of being wrong was bad enough that I didn't need to. Interviewer: Understood. Second decision point — the crew configuration under the tight craft-hour window. Walk me through that. Participant: We were maybe two-thirds through the day's craft-hour budget, and I had several configurations that would technically work — different mixes of overtime, different sequencing with other jobs. The Outage Manager wanted a decision inside the hour to protect the critical path. I looked at the first configuration that met minimum schedule and safety requirements, confirmed it cleared those bars, and locked it in. Interviewer: Did you consider comparing the other options more fully? Participant: I thought about it, but comparing all the variables — overtime cost, fatigue limits, downstream sequencing — for three or four configurations would have eaten time I didn't have. So I went with what worked and moved to the next fire. Interviewer: What happened as a result? Participant: It created a minor sequencing conflict later with an unrelated pump job — nothing that blew the schedule, but craft had to shuffle around it. When we reviewed it afterward, there was a configuration that would have avoided that friction. Marginally better, not dramatically. Interviewer: Third decision point — the vibration anomaly. What was your first working theory? Participant: Residual misalignment from the valve rework. It made sense sequentially — we'd just had hands in that area, and a little post-maintenance vibration isn't unheard of. Interviewer: What data did you pull to check that theory? Participant: I asked for the immediate vibration readings from the test run, the ones that would show whether the signature matched a misalignment pattern. They looked consistent with that, so I documented the anomaly as resolved on that basis. Interviewer: Was there other data available that you didn't request at that point? Participant: In hindsight, yes. There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched. Interviewer: What about the full trend history for that bearing? Participant: Also didn't pull that at the time. The system engineer reviewed it later, after the fact. Interviewer: Last decision point — the final return-to-service call. What was your basis for concurring? Participant: By that point, all the CRs on the valve and the adjacent pump were formally closed, the system engineer had given written concurrence, and I did the walkdown myself with operations. Given the sign-offs and what I observed directly during the walkdown, I concurred with return to service. I did weigh the earlier vibration discussion against that documentation, but everything on paper and everything I saw in the field lined up, so I didn't see a basis to hold it further. Interviewer: Did you consider requesting extra monitoring time before mode change? Participant: I did think about it briefly, given the anomaly earlier in the outage, but with the engineering concurrence and a clean walkdown, holding the unit longer without a specific technical reason didn't seem justified. Interviewer: How much time pressure were you under across these decisions, generally? Participant: Constant, honestly, but it spiked hardest around the crew assignment call — that was the one hour deadline. The priority ranking and the vibration call had a bit more breathing room, even if it didn't always feel that way in the moment. Interviewer: If the lubrication log had been sitting on your desk when the vibration anomaly came up, do you think it would have changed your review? Participant: Possibly. If it had shown something inconsistent with misalignment, I probably would have widened the investigation. It just wasn't something I went looking for at the time. Interviewer: Looking back, is there a point where a different call on FW-IV-204's priority might have changed how things unfolded? Participant: Maybe. If I'd ranked it purely on the documented trend, it might have sat lower in the queue, and I'd have had more craft-hours free for other jobs earlier. Hard to say if that changes anything meaningfully, since the valve work itself went fine. Interviewer: Anything you'd tell a newer planner based on this outage? Participant: Mainly to keep coming back to the actual trend data, even when a recent story or a tight clock makes a different path feel more urgent. It's not that those instincts are wrong, just that they're easy to lean on more than the numbers warrant.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.67s · gen 228.78s · total 234.0s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0286 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0268 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0267 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0241 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0241 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0231 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0217 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0216 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
9. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0211 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
10. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0208 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0206 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
12. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0199 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0195 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
16. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0187 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
17. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
18. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0178 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0168 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0165 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
25. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0164 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
27. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0161 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0154 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
30. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0153 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
32. **Lyell Automation bias and verification complexity.pdf** — 0.0153 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
34. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0152 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
36. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0150 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0147 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
40. **Hallihan_etal_DTM_12.pdf** — 0.0145 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0144 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. C han, U. Dulleck et al. In the triage decisio_
42. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0142 (rrf) — _# 188 | to the one in the | explanation condition). Informed by prior work that a slow algorithm_
43. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0142 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 382 operators purp_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
47. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
49. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0138 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the participant's described outage decision-making for bias-specific mechanisms, using retrieved corpus passages where available."
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
      "bias_label": "satisficing",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments of likelihood or urgency are influenced by the ease with which vivid or recent examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Priority ranking of FW-IV-204 during pre-outage scoping",
      "decision_point_description": "Ranking FW-IV-204 among concurrent work orders for the 21-day outage, based on condition reports and a recent sister-unit failure story.",
      "affected_reasoning_operation": "Risk/urgency judgment and work-order prioritization",
      "bias_specific_mechanism": "A detailed, recent, emotionally salient sister-unit valve failure was easily recalled and assigned high subjective weight, overriding the weak trend data in the condition reports.",
      "manifestation_in_interview": "The participant explicitly says the sister-unit story was fresh in his head when building the priority list and that it, not the documented trend, tipped the valve to top tier.",
      "effect_on_reasoning_or_decision": "FW-IV-204 was elevated to top-tier rework despite prior condition reports showing no worsening trend, potentially distorting craft-hour and sequencing priorities.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right around scoping, I'd just heard a pretty detailed account from a colleague about a similar valve at a sister unit that failed and caused a multi-day slip to their critical path. That story was fresh in my head when I built the priority list. I bumped FW-IV-204 up to top-tier priority for rework.",
          "evidence_explanation": "Shows the recent vivid story was mentally available and directly connected to the priority decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me. I remember thinking, we don't want to be the ones explaining a multi-day slip because we treated this as routine. So I moved it up.",
          "evidence_explanation": "Demonstrates the vividness and salience of the easily recalled case, which supplied the motivation for moving the item up."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted. It felt like the kind of thing where the downside of being wrong was bad enough that I didn't need to.",
          "evidence_explanation": "Indicates the participant did not seek out the less vivid trend data that would have tested the availability-driven concern."
        }
      ],
      "correction_or_counterevidence": "Later in the interview the participant acknowledged that on paper FW-IV-204 was not the most urgent item and that the valve work ultimately went fine; he reflected that planners should return to actual trend data rather than recent stories.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage provided a mechanism-level account of the availability heuristic; the label is applied from general cognitive-science knowledge. One retrieved passage mentioned availability only in passing, which was insufficient as mechanism support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "satisficing",
      "alternative_labels": ["satisficing heuristic", "Simon's satisficing"],
      "taxonomy_status": "established_label",
      "bias_definition": "A decision strategy in which a person selects the first option that meets a minimum acceptability threshold rather than optimizing across all available alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Crew configuration selection for FW-IV-204 under time pressure",
      "decision_point_description": "Selecting a crew configuration within a one-hour deadline while craft-hours were constrained during outage execution.",
      "affected_reasoning_operation": "Option generation and choice among feasible crew configurations",
      "bias_specific_mechanism": "The participant halted search at the first configuration that met minimum schedule and safety requirements, using acceptability thresholds rather than comparing alternatives on overtime, fatigue, and downstream sequencing.",
      "manifestation_in_interview": "The participant reports having several technically workable configurations but locking in the first acceptable one rather than comparing all variables.",
      "effect_on_reasoning_or_decision": "Produced a feasible crew configuration but one that later caused a minor sequencing conflict; a marginally better alternative existed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I had several configurations that would technically work — different mixes of overtime, different sequencing with other jobs. The Outage Manager wanted a decision inside the hour to protect the critical path. I looked at the first configuration that met minimum schedule and safety requirements, confirmed it cleared those bars, and locked it in.",
          "evidence_explanation": "Explicitly describes a satisficing search rule: first option meeting minimum criteria was chosen."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it, but comparing all the variables — overtime cost, fatigue limits, downstream sequencing — for three or four configurations would have eaten time I didn't have. So I went with what worked and moved to the next fire.",
          "evidence_explanation": "Shows the deliberate decision not to optimize because of time pressure, choosing an acceptable rather than optimal option."
        }
      ],
      "correction_or_counterevidence": "The participant later reported that a different configuration was only marginally better and that the operational time constraint was immediate; satisficing may have been adaptive under the one-hour deadline and resource constraints.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism are from general cognitive-science knowledge; no retrieved passage addressed satisficing or first-acceptable-option search.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory search", "myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm an existing hypothesis or belief, while giving insufficient attention to disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of post-maintenance pump bearing vibration anomaly",
      "decision_point_description": "Deciding the cause of a mild vibration anomaly on the adjacent feedwater pump bearing and whether to close it out as resolved.",
      "affected_reasoning_operation": "Diagnostic hypothesis formation and information search",
      "bias_specific_mechanism": "An initial hypothesis—residual misalignment from recent valve rework—guided selective data collection: the participant requested vibration readings consistent with misalignment and did not pull available disconfirming sources such as the lubrication log or bearing trend history.",
      "manifestation_in_interview": "The participant explicitly says he did not widen the search once he had a reading that matched, because the misalignment explanation already fit.",
      "effect_on_reasoning_or_decision": "The vibration anomaly was documented as resolved based on hypothesis-consistent readings alone, while the lubrication log and full trend history were not reviewed at the time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought was residual misalignment from the rework we'd just done. I pulled vibration data that fit that theory, we closed it out, and eventually got system engineer concurrence and did the walkdown before returning the unit to service.",
          "evidence_explanation": "Shows that the initial hypothesis led directly to selecting data that fit that theory."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I asked for the immediate vibration readings from the test run, the ones that would show whether the signature matched a misalignment pattern. They looked consistent with that, so I documented the anomaly as resolved on that basis.",
          "evidence_explanation": "Demonstrates hypothesis-consistent information search and interpretation, without seeking disconfirming data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched.",
          "evidence_explanation": "Direct evidence of avoiding an available disconfirming source because the current hypothesis felt sufficient."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Also didn't pull that at the time. The system engineer reviewed it later, after the fact.",
          "evidence_explanation": "Confirms the full trend history was not examined until after the closure decision, consistent with confirmation-driven search."
        }
      ],
      "correction_or_counterevidence": "The participant said if the lubrication log had shown something inconsistent he probably would have widened the investigation, and the system engineer later reviewed the full trend history after the fact; however, these did not occur before the closure decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support was available from a paper discussing confirmation bias in plant operations; it describes confirmation bias preventing operators from noticing or identifying alternative causes.",
      "corpus_evidence": [
        {
          "source_identifier": "Murtat Influence of Cognitive Biases in Distorting Decision Making and.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The confirmation bias that leads the  operators to believe that such a  also prevented them from noticing and identifyi It took a long time to identify the cause of th temperature, which led to the meltdown of the react effect (bias) that generally makes operators not  multiple perspectives, especially under emergency  frame that they usually used and could not apply a of the cause).",
          "mechanism_supported_by_source": "Confirmation bias operates by preventing operators from noticing or identifying alternative explanations and from applying multiple perspectives under uncertainty.",
          "relevance_to_this_occurrence": "The participant's selective search for misalignment-consistent vibration data and failure to pull lubrication/trend information reflect the same mechanism of not examining alternative causes once an initial interpretation seemed adequate."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final return-to-service concurrence after earlier vibration anomaly",
      "supporting_interview_quote": "I did think about it briefly, given the anomaly earlier in the outage, but with the engineering concurrence and a clean walkdown, holding the unit longer without a specific technical reason didn't seem justified.",
      "plausible_mechanism": "A tendency to continue the planned outage/return-to-service path once formal documentation and direct observations appear consistent, despite an earlier mild abnormal indication.",
      "why_not_identified": "There is no affirmative evidence that the participant irrationally favored the schedule over safety; the decision was supported by engineer concurrence, closed condition reports, and a direct walkdown. Lack of a specific technical reason to hold is a plausible non-bias explanation."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Single interview; analysis relies on participant self-report and retrospective reconstruction.",
    "Retrieved corpus support was limited and some passages contain OCR/parsing artifacts; availability and satisficing labels rely on general cognitive-science knowledge.",
    "The analysis does not include objective verification of condition reports, craft-hour data, vibration logs, or other records.",
    "Confidence judgments reflect the interview evidence only, not a formal behavioral measurement."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about your decision-making during the last refueling outage, not a performance review. Everything you share is for process improvement. Can you tell me your role and roughly how long you've been doing outage coordination? Participant: Sure, happy to walk through it. I'm the maintenance planner and outage coordinator for the unit — been doing this specific role about six years, plus four years as a planner before that. My main job during the outage is to sequence work orders against the critical path, allocate craft-hours, and make sure everything closes out before we hit the mode change hold points. Interviewer: What made this particular outage stand out from a routine one? Participant: Honestly, the sheer volume — we had around 140 concurrent work orders competing for a fixed 21-day window, and craft-hours were tighter than usual because two contractor crews got pulled to another site mid-cycle. So there was a lot of juggling. The item that ended up taking more of my attention than I expected was FW-IV-204, one of our feedwater isolation valves. Interviewer: Take me through the sequence of events, from initial scoping to final return to service. Participant: At the start of scoping, FW-IV-204 had a minor packing weep — nothing new, it had shown up in two prior outage condition reports, both closed as acceptable-as-found. No trend showing it was getting worse. But right around scoping, I'd just heard a pretty detailed account from a colleague about a similar valve at a sister unit that failed and caused a multi-day slip to their critical path. That story was fresh in my head when I built the priority list. I bumped FW-IV-204 up to top-tier priority for rework. Then, once we got into execution, craft-hours were running thin one afternoon and I had to lock in a crew configuration fast for the valve job — Outage Manager wanted it settled within the hour. I went with the first configuration that cleared the minimum schedule and safety requirements. Later in the outage, during post-maintenance testing, we saw a mild vibration anomaly on the pump bearing right next to FW-IV-204. My first thought was residual misalignment from the rework we'd just done. I pulled vibration data that fit that theory, we closed it out, and eventually got system engineer concurrence and did the walkdown before returning the unit to service. Interviewer: Let's slow down and reconstruct the timeline in more detail. When exactly did FW-IV-204 first come onto your radar for this outage? Participant: Right at the outset of scoping, maybe day one or two of pre-outage planning. It was already on the work list from the prior cycle's CR, so it wasn't a surprise. What changed was how I ranked it relative to everything else. Interviewer: And the vibration anomaly — when did that surface relative to the valve work? Participant: That was maybe day fourteen, after the valve rework was already complete and we were running post-maintenance functional tests on the adjacent feedwater pump. Interviewer: Let's go through each of those decision points one at a time. First — the priority ranking. What information did you actually have in front of you when you made that call? Participant: I had the two prior CRs, both closed, no adverse trend on leak rate. I also had the backlog of other work orders, some with comparable or even higher CR severity ratings. Objectively, on paper, FW-IV-204 wasn't the most urgent thing on the list. Interviewer: So what tipped it to top-tier? Participant: The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me. I remember thinking, we don't want to be the ones explaining a multi-day slip because we treated this as routine. So I moved it up. Interviewer: Did you go back and re-check the trend data before finalizing that ranking? Participant: No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted. It felt like the kind of thing where the downside of being wrong was bad enough that I didn't need to. Interviewer: Understood. Second decision point — the crew configuration under the tight craft-hour window. Walk me through that. Participant: We were maybe two-thirds through the day's craft-hour budget, and I had several configurations that would technically work — different mixes of overtime, different sequencing with other jobs. The Outage Manager wanted a decision inside the hour to protect the critical path. I looked at the first configuration that met minimum schedule and safety requirements, confirmed it cleared those bars, and locked it in. Interviewer: Did you consider comparing the other options more fully? Participant: I thought about it, but comparing all the variables — overtime cost, fatigue limits, downstream sequencing — for three or four configurations would have eaten time I didn't have. So I went with what worked and moved to the next fire. Interviewer: What happened as a result? Participant: It created a minor sequencing conflict later with an unrelated pump job — nothing that blew the schedule, but craft had to shuffle around it. When we reviewed it afterward, there was a configuration that would have avoided that friction. Marginally better, not dramatically. Interviewer: Third decision point — the vibration anomaly. What was your first working theory? Participant: Residual misalignment from the valve rework. It made sense sequentially — we'd just had hands in that area, and a little post-maintenance vibration isn't unheard of. Interviewer: What data did you pull to check that theory? Participant: I asked for the immediate vibration readings from the test run, the ones that would show whether the signature matched a misalignment pattern. They looked consistent with that, so I documented the anomaly as resolved on that basis. Interviewer: Was there other data available that you didn't request at that point? Participant: In hindsight, yes. There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched. Interviewer: What about the full trend history for that bearing? Participant: Also didn't pull that at the time. The system engineer reviewed it later, after the fact. Interviewer: Last decision point — the final return-to-service call. What was your basis for concurring? Participant: By that point, all the CRs on the valve and the adjacent pump were formally closed, the system engineer had given written concurrence, and I did the walkdown myself with operations. Given the sign-offs and what I observed directly during the walkdown, I concurred with return to service. I did weigh the earlier vibration discussion against that documentation, but everything on paper and everything I saw in the field lined up, so I didn't see a basis to hold it further. Interviewer: Did you consider requesting extra monitoring time before mode change? Participant: I did think about it briefly, given the anomaly earlier in the outage, but with the engineering concurrence and a clean walkdown, holding the unit longer without a specific technical reason didn't seem justified. Interviewer: How much time pressure were you under across these decisions, generally? Participant: Constant, honestly, but it spiked hardest around the crew assignment call — that was the one hour deadline. The priority ranking and the vibration call had a bit more breathing room, even if it didn't always feel that way in the moment. Interviewer: If the lubrication log had been sitting on your desk when the vibration anomaly came up, do you think it would have changed your review? Participant: Possibly. If it had shown something inconsistent with misalignment, I probably would have widened the investigation. It just wasn't something I went looking for at the time. Interviewer: Looking back, is there a point where a different call on FW-IV-204's priority might have changed how things unfolded? Participant: Maybe. If I'd ranked it purely on the documented trend, it might have sat lower in the queue, and I'd have had more craft-hours free for other jobs earlier. Hard to say if that changes anything meaningfully, since the valve work itself went fine. Interviewer: Anything you'd tell a newer planner based on this outage? Participant: Mainly to keep coming back to the actual trend data, even when a recent story or a tight clock makes a different path feel more urgent. It's not that those instincts are wrong, just that they're easy to lean on more than the numbers warrant.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.47s · gen 196.84s · total 201.8s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0286 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0268 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0267 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0241 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0241 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0231 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0217 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0216 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
9. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0211 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
10. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0208 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0206 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
12. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0199 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0195 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
16. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0187 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
17. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
18. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0178 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0168 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
24. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0165 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
25. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0164 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
27. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0161 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0154 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
30. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0153 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
32. **Lyell Automation bias and verification complexity.pdf** — 0.0153 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
34. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0152 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
36. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0150 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0147 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
40. **Hallihan_etal_DTM_12.pdf** — 0.0145 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0144 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. C han, U. Dulleck et al. In the triage decisio_
42. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0142 (rrf) — _# 188 | to the one in the | explanation condition). Informed by prior work that a slow algorithm_
43. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0142 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 382 operators purp_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
47. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
49. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0138 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the transcript for affirmative evidence of bias-specific mechanisms; no experimental condition or expected bias count was assumed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
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
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "Availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which the perceived likelihood or urgency of an event is influenced by how easily a vivid or recent instance can be brought to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Priority ranking of FW-IV-204",
      "decision_point_description": "During pre-outage scoping, the participant ranked FW-IV-204 as top-tier rework priority despite documented evidence of stable acceptable-as-found condition.",
      "affected_reasoning_operation": "Risk/urgency assessment and work priority allocation",
      "bias_specific_mechanism": "A recent, detailed, and emotionally salient sister-unit valve failure was highly available in memory, and the participant used that exemplar to judge the current valve's failure risk as high, overriding documented trend data and severity ratings.",
      "manifestation_in_interview": "The participant states that the sister-unit story was fresh in his head and 'stuck with' him, then moved the valve up without re-checking trend data, even though the available CR history showed no adverse trend and other work had comparable or higher severity ratings.",
      "effect_on_reasoning_or_decision": "FW-IV-204 was assigned scarce craft-hours and top priority based on an available anecdote rather than its documented risk, potentially displacing objectively higher-risk work.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me.",
          "evidence_explanation": "The participant identifies a recent, detailed, similar failure as the salient reason for the ranking; this is a direct report of availability influencing his judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking, we don't want to be the ones explaining a multi-day slip because we treated this as routine. So I moved it up.",
          "evidence_explanation": "The decision is explicitly linked to the vivid sister-unit scenario rather than the valve's documented condition or trend."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted. It felt like the kind of thing where the downside of being wrong was bad enough that I didn't need to.",
          "evidence_explanation": "This shows he did not seek objective trend data after the salient story elevated his concern, consistent with availability-based urgency overriding analytical verification."
        }
      ],
      "correction_or_counterevidence": "The participant notes that objectively FW-IV-204 was not the most urgent item on paper, and later advises newer planners to keep returning to actual trend data when a recent story makes a different path feel more urgent.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not define or support the availability heuristic; this occurrence is classified using an established cognitive-science label from general knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Selective information search",
        "Hypothesis-confirming search"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to seek, interpret, or prioritize information that is consistent with an existing hypothesis while failing to seek or consider disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vibration anomaly diagnosis and closure",
      "decision_point_description": "During post-maintenance testing, a mild vibration anomaly appeared on the pump bearing adjacent to FW-IV-204; the participant selected data and closed the anomaly based on a preferred misalignment explanation.",
      "affected_reasoning_operation": "Diagnostic hypothesis testing and information search",
      "bias_specific_mechanism": "The participant formed an initial hypothesis, residual misalignment, then searched for and accepted vibration data that matched that hypothesis while not retrieving available disconfirming data, specifically the lubrication log and full bearing trend history.",
      "manifestation_in_interview": "The participant states that his first thought was residual misalignment, that he pulled vibration data that fit that theory, and that he did not pull the lubrication log or trend history because the misalignment explanation already seemed to fit.",
      "effect_on_reasoning_or_decision": "The anomaly was closed on a confirming data pattern without checking readily available information that could have pointed to an alternative bearing problem, potentially producing premature diagnostic closure.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought was residual misalignment from the rework we'd just done. I pulled vibration data that fit that theory, we closed it out, and eventually got system engineer concurrence and did the walkdown before returning the unit to service.",
          "evidence_explanation": "The participant describes selecting data to fit an already-formed hypothesis and closing the anomaly, a pattern of confirmation-based search."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched.",
          "evidence_explanation": "This explicitly shows that available disconfirming information was not sought because the chosen information matched the preferred explanation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Also didn't pull that at the time. The system engineer reviewed it later, after the fact.",
          "evidence_explanation": "Full trend-history data, which could have tested the hypothesis more rigorously, was not retrieved during the diagnostic episode."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledges in hindsight that the lubrication log and full trend history were available and that inconsistent findings might have widened the investigation; the system engineer reviewed the trend later, after the fact.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "A retrieved source identifies confirmation bias as making operators hold an existing belief and fail to notice or identify contrary information; it is used here to support the mechanism of selective information search, while the transcript supplies affirmative evidence that this pattern occurred.",
      "corpus_evidence": [
        {
          "source_identifier": "Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The confirmation bias that leads the  operators to believe that such a  also prevented them from noticing and identifyi",
          "mechanism_supported_by_source": "Confirmation bias can cause an operator to maintain an existing belief and fail to notice or identify contrary information.",
          "relevance_to_this_occurrence": "The participant maintained the residual-misalignment explanation and did not seek available lubrication-log or trend-history information that could have disconfirmed it."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "Satisficing heuristic",
        "First-acceptable-option bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Crew configuration selection under one-hour deadline",
      "supporting_interview_quote": "I looked at the first configuration that met minimum schedule and safety requirements, confirmed it cleared those bars, and locked it in.",
      "plausible_mechanism": "The first acceptable crew configuration may have served as an anchor, leading to insufficient comparison of alternative configurations; a later review found a marginally better configuration that would have avoided a sequencing conflict.",
      "why_not_identified": "The transcript primarily attributes the choice to a one-hour deadline and satisficing under time pressure. There is insufficient affirmative evidence of a distinct bias-specific mechanism, such as inadequate anchor-driven adjustment, beyond ordinary bounded-rationality decision making."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support for the availability heuristic occurrence was unavailable; that occurrence relies on established cognitive-science knowledge with disclosure.",
    "The retrieved corpus passage on confirmation bias is fragmented in the available text, so metadata fields are limited to the document identifier and the quoted passage is preserved exactly as retrieved.",
    "Speaker attribution is based solely on transcript labels and participant self-report; the analysis does not have independent behavioral observation data."
  ]
}

