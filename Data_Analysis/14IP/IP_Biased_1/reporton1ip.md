# RAG Benchmark — 2026-09-13

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific incident from your work as a production planner, and I'll be asking you to walk me through what happened and why you made the calls you did. Nothing you say here affects your performance record. Sound good? Participant: Yeah, that's fine. Happy to walk through it. It was a memorable afternoon. Interviewer: Can you tell me a bit about your role, then give me the overview of the incident? Participant: I'm the production planner for three parallel lines at our plant — discrete assembly, mid-volume SKUs, frequent changeovers. I sequence what runs where, manage changeover windows, and hit ship cutoffs without blowing labor budgets. This was a Friday. A subcomponent we needed for two customer orders — Order A and Order B — came in four hours late from the supplier. Both had the same end-of-shift ship cutoff, so as soon as I heard about the delay I knew I had a compressed window to get everything sequenced and out the door. Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened after you learned about the late delivery? Participant: Once I confirmed the component landed, I pulled up the MES to see where Line 1 and Line 2 stood — both mid-run on other SKUs, so I needed changeovers on both to get to the rush SKUs. Problem was, I only had one certified changeover tech on shift. That was my first call — which line gets the tech first. Around the same time, an operator flagged that Line 3 had thrown an intermittent alarm twice in the past hour. That line wasn't part of the original plan, but it had open capacity, so it became relevant as a potential overflow resource. Then there was a batch sitting in the Line 2 output buffer that QA hadn't released yet, which mattered because Order B needed some of those units. Finally, toward the end, a labeling issue on part of that batch ate into our remaining time right as the ship cutoff closed in. So four points where I had to make a call under pressure. Interviewer: Let's reconstruct the timeline before we dig into each decision. Participant: Component lands around 1pm, four hours later than the morning window. I make the technician call almost immediately, maybe 1:15. The Line 3 alarm conversation happens about 20 minutes after, while the first changeover is underway. The QA buffer question comes up around 2:30, once I'm mapping how many units Order B still needs. QA doesn't call back until 3:10, which is when the labeling discrepancy surfaces. From there it's a sprint — cutoff is 5pm, so the last call, about overtime and the carrier, happens around 3:30. Interviewer: Let's start with the technician assignment. What information did you have? Participant: I knew Order A was the bigger order by unit count, and Line 2 had a tighter downstream packaging slot later on. Technically Line 2's changeover being late would ripple further because packaging was booked tight. In the moment I went with unit count — Order A first — partly because that's our default rule when picking between two rush jobs. I didn't split the tech's time across both lines in shorter blocks, which was an option, because that would have delayed both changeovers instead of finishing one cleanly. Interviewer: Any hesitation about the packaging slot issue? Participant: A little. But finishing one line's changeover completely felt more reliable than half-finishing two, and Order A's volume backed that up. Interviewer: Let's move to the Line 3 alarm. Walk me through that call. Participant: The operator told me the alarm had come up before and 'usually clears itself' — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience. Given that, and given I had two other things actively unfolding — the changeover and the ship cutoff clock — I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue. Interviewer: Did you look into whether anything else depended on Line 3's output during that window? Participant: Honestly, no. I didn't check. My focus was entirely on Order A and Order B — those were the two fires in front of me — so I didn't cross-reference the schedule for anything else running through Line 3. It turned out a smaller order, Order C, also needed Line 3 output that same shift, but I didn't find that out until later. I wasn't ignoring it on purpose, it just wasn't on my radar with everything else going on. Interviewer: When you found out about Order C afterward, what was your reaction? Participant: A bit of an 'oh, right' moment. Not catastrophic — we fit it in later — but it made me realize I'd made that overflow call pretty quickly without stepping back to check what else was in play on that line. Interviewer: Let's talk about the QA buffer decision. What was going through your mind? Participant: Order B needed units from that batch plus new production to hit full quantity. QA hadn't confirmed release yet, and their lead was off-site with spotty response time. I decided to provisionally build the buffer units into the Order B plan rather than wait, because waiting with no ETA on a callback risked losing time I couldn't get back. I told the team we'd adjust if QA flagged something. Interviewer: What made provisional inclusion feel right versus excluding those units? Participant: Excluding them would have guaranteed a lower fill rate regardless of what QA said, and historically that batch type passes more often than not. It felt like a reasonable bet given the clock, not a guarantee. Interviewer: And QA did call back? Participant: About forty minutes later. They confirmed the batch passed, but flagged a labeling discrepancy on a subset of units, meaning rework. Interviewer: That leads to the final decision — rework and shipment. What were you weighing? Participant: The rework was going to eat twenty minutes of Line 2 time, and cutoff was ninety minutes out. Order A was tracking fine. Order B was now at risk. Overtime authorization had just come through, but it adds cost. I could also have accepted a partial shipment and expedited the rest next shift, or called the account manager to renegotiate the cutoff. Interviewer: Why overtime and carrier coordination instead of the other two? Participant: Partial shipment felt like a worse customer experience than a slightly late full shipment, and renegotiating the cutoff was a last resort I wanted to avoid if I could still make it work operationally. Overtime plus talking to the carrier directly gave me a shot at getting the full order out with minimal disruption, even shipping a few minutes past official cutoff. Interviewer: How did that play out? Participant: Order B shipped about twelve minutes past cutoff after the carrier agreed to hold pickup briefly. Order A shipped on time. Not a clean day, but nothing was lost. Interviewer: Looking back, if you'd known upfront that Order C depended on Line 3, would you have handled that decision differently? Participant: Probably. I likely would have taken two minutes to check the schedule before committing Line 3 as overflow, rather than just going with the operator's read on the alarm. It wouldn't have changed the outcome much, but I'd have made the call with a clearer picture. Interviewer: And if you'd had fifteen more minutes before the technician assignment, would anything have changed? Participant: Maybe I'd have looked harder at splitting the tech's time, but I think I still land on Order A first given the volume difference. Interviewer: Is there a point in this sequence where, in hindsight, you wish you'd gathered more information before deciding? Participant: The Line 3 call, for sure. Everything else I feel like I had a reasonable handle on given what was knowable at the time. That one I moved through fast because I was juggling two other things, and it's the one place where a little more digging would have given me a fuller picture before I committed the line. Interviewer: That's really helpful, thank you. I think that covers everything I need. Participant: No problem, glad it was useful.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.98s · gen 93.86s · total 100.4s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0302 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0267 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0257 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0252 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0234 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0230 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0228 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0210 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0207 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0207 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
11. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0203 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0202 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0200 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0197 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
15. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0187 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0184 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0184 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
19. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0173 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0173 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
24. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0171 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0166 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
28. **Hallihan_etal_DTM_12.pdf** — 0.0165 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
29. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
31. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0159 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
33. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0158 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
34. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0158 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## Afterword | a nd rich with smells because the genes that built its brain have survived throug_
36. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0153 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0153 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
38. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration et al., 1994; McGu_
40. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0151 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## lIs sues in M ADE M E D O I T , A rmine law and order. But, if you tell the judge that your g_
42. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0149 (rrf) — _# Self - other Placement W ith no other evidence chance of success w ould also the p rinciple of_
43. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0149 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs | Suppose you are [[a/an]] [[specialist_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
45. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
47. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0142 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
48. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
49. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0138 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
50. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0138 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Blind, conservative, mechanism-first examination of the interview transcript for affirmatively demonstrated cognitive bias occurrences, using retrieved scientific passages only for label and mechanism validation."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency",
        "premature cognitive commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A reduction in information sampling or verification associated with high trust or repeated benign experience with a system, especially under high task load, leading to acceptance of system status without adequate independent cross-checking.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Line 3 intermittent alarm and overflow allocation",
      "decision_point_description": "Whether to treat Line 3 as available overflow capacity without cross-referencing schedule dependencies",
      "affected_reasoning_operation": "Information search and resource allocation under time pressure",
      "bias_specific_mechanism": "Under high task load and concurrent changeover/shipment pressures, the participant relied on the operator's report that the alarm 'usually clears itself' and on prior experience of no stoppages. This repeated benign exposure supported a premature cognitive commitment and complacent under-sampling: he allocated Line 3 as overflow capacity without independently checking the schedule for other dependencies. His attention was narrowed toward the two active orders, further reducing verification behavior.",
      "manifestation_in_interview": "The participant explicitly described accepting the intermittent alarm as noncritical based on history and workload, then moving on without checking what else depended on Line 3. He later discovered that Order C also required Line 3 output that shift.",
      "effect_on_reasoning_or_decision": "Led the participant to commit Line 3 as available overflow while missing an existing production dependency for Order C, requiring reactive replanning later.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The operator told me the alarm had come up before and 'usually clears itself' — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience. Given that, and given I had two other things actively unfolding — the changeover and the ship cutoff clock — I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue.",
          "evidence_explanation": "Shows the participant accepted a benign system status based on repeated exposure and current workload, with no described verification of the alarm or the line's other schedule commitments before allocating it as overflow."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, no. I didn't check. My focus was entirely on Order A and Order B — those were the two fires in front of me — so I didn't cross-reference the schedule for anything else running through Line 3.",
          "evidence_explanation": "Directly demonstrates incomplete information sampling: the participant did not check schedule dependencies, consistent with complacent under-sampling under narrowed attention."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That one I moved through fast because I was juggling two other things, and it's the one place where a little more digging would have given me a fuller picture before I committed the line.",
          "evidence_explanation": "Retrospective acknowledgement that decision speed and competing task load caused insufficient information gathering before committing Line 3."
        }
      ],
      "correction_or_counterevidence": "The participant later discovered Order C and reported that it was fit in later. A plausible non-bias explanation is that ordinary triage under severe time pressure and limited attention, rather than a distinct trust-driven bias, produced the omission. However, the pattern of incomplete verification following repeated benign exposure and high workload is structurally consistent with automation complacency.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Parasuraman and Manzey material supplies the operational definition of complacency as incomplete information sampling under automation reliability and high task load, and the related concept of premature cognitive commitment from repeated exposure.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Analyses of informationsampling behavior revealed that half of the participants made this commission error because of a clear complacency effect, as reflected in an incomplete sampling of information needed for automation verification.",
          "mechanism_supported_by_source": "Complacency operates through incomplete sampling or verification of information when an operator accepts system-provided assessments under workload demands.",
          "relevance_to_this_occurrence": "The participant similarly accepted the operator's benign characterization of the Line 3 alarm and did not sample schedule information needed to verify that the line was truly available for overflow."
        },
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "repeated exposure to the same experience leads people to engage in 'automated' or 'mindless' behavior.",
          "mechanism_supported_by_source": "Repeated benign exposure can induce premature cognitive commitment and mindless acceptance rather than active verification.",
          "relevance_to_this_occurrence": "The participant cited prior instances of the intermittent alarm clearing without stoppage, which supports a premature cognitive commitment to that line being non-problematic."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Technician assignment between Line 1 and Line 2",
      "supporting_interview_quote": "In the moment I went with unit count — Order A first — partly because that's our default rule when picking between two rush jobs.",
      "plausible_mechanism": "The default unit-count rule may have served as an initial anchor, with insufficient adjustment for Line 2's tighter downstream packaging slot.",
      "why_not_identified": "The participant explicitly considered the downstream packaging issue and later stated that with additional time he would likely still choose Order A first. The decision appears strongly consistent with a deliberate production-scheduling heuristic rather than a demonstrable anchoring distortion."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation",
        "get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Rework and final shipment decision",
      "supporting_interview_quote": "Partial shipment felt like a worse customer experience than a slightly late full shipment, and renegotiating the cutoff was a last resort I wanted to avoid if I could still make it work operationally.",
      "plausible_mechanism": "Continued commitment to the original full-shipment plan despite time compression and rework, potentially reflecting plan continuation or overoptimism about meeting the cutoff.",
      "why_not_identified": "The participant weighed alternatives explicitly, including partial shipment and cutoff renegotiation, and the full shipment was ultimately completed with only a brief delay. The transcript does not clearly establish a bias-driven distortion rather than a reasonable operational trade-off."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on self-reported interview testimony rather than direct observation or system data.",
    "The retrieved corpus support is limited to the supplied passages; closely related mechanisms such as attentional tunneling were considered but lacked direct corpus support.",
    "Confidence levels are intentionally conservative because time pressure and multitasking provide plausible competing operational explanations for the identified behavior."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific incident from your work as a production planner, and I'll be asking you to walk me through what happened and why you made the calls you did. Nothing you say here affects your performance record. Sound good? Participant: Yeah, that's fine. Happy to walk through it. It was a memorable afternoon. Interviewer: Can you tell me a bit about your role, then give me the overview of the incident? Participant: I'm the production planner for three parallel lines at our plant — discrete assembly, mid-volume SKUs, frequent changeovers. I sequence what runs where, manage changeover windows, and hit ship cutoffs without blowing labor budgets. This was a Friday. A subcomponent we needed for two customer orders — Order A and Order B — came in four hours late from the supplier. Both had the same end-of-shift ship cutoff, so as soon as I heard about the delay I knew I had a compressed window to get everything sequenced and out the door. Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened after you learned about the late delivery? Participant: Once I confirmed the component landed, I pulled up the MES to see where Line 1 and Line 2 stood — both mid-run on other SKUs, so I needed changeovers on both to get to the rush SKUs. Problem was, I only had one certified changeover tech on shift. That was my first call — which line gets the tech first. Around the same time, an operator flagged that Line 3 had thrown an intermittent alarm twice in the past hour. That line wasn't part of the original plan, but it had open capacity, so it became relevant as a potential overflow resource. Then there was a batch sitting in the Line 2 output buffer that QA hadn't released yet, which mattered because Order B needed some of those units. Finally, toward the end, a labeling issue on part of that batch ate into our remaining time right as the ship cutoff closed in. So four points where I had to make a call under pressure. Interviewer: Let's reconstruct the timeline before we dig into each decision. Participant: Component lands around 1pm, four hours later than the morning window. I make the technician call almost immediately, maybe 1:15. The Line 3 alarm conversation happens about 20 minutes after, while the first changeover is underway. The QA buffer question comes up around 2:30, once I'm mapping how many units Order B still needs. QA doesn't call back until 3:10, which is when the labeling discrepancy surfaces. From there it's a sprint — cutoff is 5pm, so the last call, about overtime and the carrier, happens around 3:30. Interviewer: Let's start with the technician assignment. What information did you have? Participant: I knew Order A was the bigger order by unit count, and Line 2 had a tighter downstream packaging slot later on. Technically Line 2's changeover being late would ripple further because packaging was booked tight. In the moment I went with unit count — Order A first — partly because that's our default rule when picking between two rush jobs. I didn't split the tech's time across both lines in shorter blocks, which was an option, because that would have delayed both changeovers instead of finishing one cleanly. Interviewer: Any hesitation about the packaging slot issue? Participant: A little. But finishing one line's changeover completely felt more reliable than half-finishing two, and Order A's volume backed that up. Interviewer: Let's move to the Line 3 alarm. Walk me through that call. Participant: The operator told me the alarm had come up before and 'usually clears itself' — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience. Given that, and given I had two other things actively unfolding — the changeover and the ship cutoff clock — I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue. Interviewer: Did you look into whether anything else depended on Line 3's output during that window? Participant: Honestly, no. I didn't check. My focus was entirely on Order A and Order B — those were the two fires in front of me — so I didn't cross-reference the schedule for anything else running through Line 3. It turned out a smaller order, Order C, also needed Line 3 output that same shift, but I didn't find that out until later. I wasn't ignoring it on purpose, it just wasn't on my radar with everything else going on. Interviewer: When you found out about Order C afterward, what was your reaction? Participant: A bit of an 'oh, right' moment. Not catastrophic — we fit it in later — but it made me realize I'd made that overflow call pretty quickly without stepping back to check what else was in play on that line. Interviewer: Let's talk about the QA buffer decision. What was going through your mind? Participant: Order B needed units from that batch plus new production to hit full quantity. QA hadn't confirmed release yet, and their lead was off-site with spotty response time. I decided to provisionally build the buffer units into the Order B plan rather than wait, because waiting with no ETA on a callback risked losing time I couldn't get back. I told the team we'd adjust if QA flagged something. Interviewer: What made provisional inclusion feel right versus excluding those units? Participant: Excluding them would have guaranteed a lower fill rate regardless of what QA said, and historically that batch type passes more often than not. It felt like a reasonable bet given the clock, not a guarantee. Interviewer: And QA did call back? Participant: About forty minutes later. They confirmed the batch passed, but flagged a labeling discrepancy on a subset of units, meaning rework. Interviewer: That leads to the final decision — rework and shipment. What were you weighing? Participant: The rework was going to eat twenty minutes of Line 2 time, and cutoff was ninety minutes out. Order A was tracking fine. Order B was now at risk. Overtime authorization had just come through, but it adds cost. I could also have accepted a partial shipment and expedited the rest next shift, or called the account manager to renegotiate the cutoff. Interviewer: Why overtime and carrier coordination instead of the other two? Participant: Partial shipment felt like a worse customer experience than a slightly late full shipment, and renegotiating the cutoff was a last resort I wanted to avoid if I could still make it work operationally. Overtime plus talking to the carrier directly gave me a shot at getting the full order out with minimal disruption, even shipping a few minutes past official cutoff. Interviewer: How did that play out? Participant: Order B shipped about twelve minutes past cutoff after the carrier agreed to hold pickup briefly. Order A shipped on time. Not a clean day, but nothing was lost. Interviewer: Looking back, if you'd known upfront that Order C depended on Line 3, would you have handled that decision differently? Participant: Probably. I likely would have taken two minutes to check the schedule before committing Line 3 as overflow, rather than just going with the operator's read on the alarm. It wouldn't have changed the outcome much, but I'd have made the call with a clearer picture. Interviewer: And if you'd had fifteen more minutes before the technician assignment, would anything have changed? Participant: Maybe I'd have looked harder at splitting the tech's time, but I think I still land on Order A first given the volume difference. Interviewer: Is there a point in this sequence where, in hindsight, you wish you'd gathered more information before deciding? Participant: The Line 3 call, for sure. Everything else I feel like I had a reasonable handle on given what was knowable at the time. That one I moved through fast because I was juggling two other things, and it's the one place where a little more digging would have given me a fuller picture before I committed the line. Interviewer: That's really helpful, thank you. I think that covers everything I need. Participant: No problem, glad it was useful.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.49s · gen 91.23s · total 96.4s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0302 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0267 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0257 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0252 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0234 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0230 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0228 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0210 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0207 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0207 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
11. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0203 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0202 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0200 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0197 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
15. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0187 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0184 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0184 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
19. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0173 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0173 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
24. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0171 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0166 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
28. **Hallihan_etal_DTM_12.pdf** — 0.0165 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
29. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
31. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0159 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
33. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0158 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
34. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0158 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## Afterword | a nd rich with smells because the genes that built its brain have survived throug_
36. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0153 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0153 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
38. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration et al., 1994; McGu_
40. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0151 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## lIs sues in M ADE M E D O I T , A rmine law and order. But, if you tell the judge that your g_
42. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0149 (rrf) — _# Self - other Placement W ith no other evidence chance of success w ould also the p rinciple of_
43. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0149 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs | Suppose you are [[a/an]] [[specialist_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
45. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
47. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0142 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
48. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
49. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0138 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
50. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0138 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single recall-based interview analysis of a production planner's compressed Friday shipment incident. Analysis focuses on decision episodes described by the participant and uses retrieved corpus passages primarily for automation complacency."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency",
        "premature cognitive commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Automation complacency is a human operator's failure to adequately monitor or verify an automated system or alarm, often because of prior reliable experience or high trust, leading to incomplete information sampling and missed failures or constraints.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Line 3 intermittent alarm and overflow capacity decision",
      "decision_point_description": "While managing two rush orders and a compressed ship cutoff, the participant decided to treat Line 3 as available overflow capacity without cross-checking what else depended on Line 3.",
      "affected_reasoning_operation": "Monitoring, verification, and scheduling judgment about Line 3 availability",
      "bias_specific_mechanism": "Repeated exposure to an intermittent sensor fault that 'usually clears itself' produced a form of premature cognitive commitment or mindless acceptance. Under high task load, the participant did not sample the schedule information needed to verify the Line 3 commitment.",
      "manifestation_in_interview": "The participant accepted the operator's read that the alarm usually clears itself and treated Line 3 as available overflow, later discovering that Order C also needed Line 3 output that shift.",
      "effect_on_reasoning_or_decision": "The participant committed Line 3 as overflow capacity without recognizing a competing dependency, resulting in a later surprise about Order C and a retrospective acknowledgment that the call was made too quickly.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The operator told me the alarm had come up before and 'usually clears itself' — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience. Given that, and given I had two other things actively unfolding — the changeover and the ship cutoff clock — I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue.",
          "evidence_explanation": "This quote shows the participant relying on prior non-events and the operator's usual-clears framing as sufficient justification to commit the line without further verification, which is consistent with complacent under-sampling of available information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, no. I didn't check. My focus was entirely on Order A and Order B — those were the two fires in front of me — so I didn't cross-reference the schedule for anything else running through Line 3. It turned out a smaller order, Order C, also needed Line 3 output that same shift, but I didn't find that out until later. I wasn't ignoring it on purpose, it just wasn't on my radar with everything else going on.",
          "evidence_explanation": "This directly describes incomplete information sampling before acting: the participant committed Line 3 as overflow without checking other schedule dependencies, which is the core behavioral marker of complacency in monitoring/verification."
        }
      ],
      "correction_or_counterevidence": "The participant later reflected that the Line 3 call was the one place where more digging would have given a fuller picture, and he likely would have checked the schedule first. However, this correction occurred after the decision and did not prevent the initial missed dependency. The operator's factual claim about the alarm not causing stoppages may also be accurate, so the error was not necessarily in trusting the alarm history but in not checking the surrounding schedule.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label and mechanism are supported by retrieved passages on automation complacency, incomplete information sampling, and premature cognitive commitment.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Langer (1982) proposed that repeated exposure to the same experience leads people to engage in \"automated\" or \"mindless\" behavior. ... half of the participants made this commission error because of a clear complacency effect, as reflected in an incomplete sampling of information needed for automation verification.",
          "mechanism_supported_by_source": "The passage links complacency to incomplete information sampling during automation-related monitoring and ties repeated exposure to mindless acceptance of a system's state.",
          "relevance_to_this_occurrence": "The participant's acceptance of the intermittent alarm as a familiar non-issue, followed by not checking the schedule before committing Line 3, mirrors the incomplete sampling mechanism described in the passage."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Technician assignment between Order A and Order B rush changeovers",
      "supporting_interview_quote": "In the moment I went with unit count — Order A first — partly because that's our default rule when picking between two rush jobs.",
      "plausible_mechanism": "The default rule and unit-count cue may have served as an anchor, with insufficient adjustment away from that anchor when considering Line 2's tighter downstream packaging slot.",
      "why_not_identified": "The participant did consider the packaging-slot information and offered an operational rationale for finishing one changeover cleanly rather than splitting time. There is insufficient affirmative evidence that the decision involved an inadequate adjustment rather than a legitimate prioritization heuristic."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final rework and shipment decision under time pressure",
      "supporting_interview_quote": "renegotiating the cutoff was a last resort I wanted to avoid if I could still make it work operationally.",
      "plausible_mechanism": "The participant may have continued the original full-shipment plan despite mounting time pressure, preferring overtime and carrier coordination over partial shipment or cutoff renegotiation.",
      "why_not_identified": "The participant explicitly weighed the alternatives and selected an operational workaround rather than simply perseverating. The statement is also consistent with ordinary operational preference, and no distinct bias-specific mechanism is strongly demonstrated."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Assessment of Line 3 alarm seriousness",
      "supporting_interview_quote": "The operator told me the alarm had come up before and 'usually clears itself' — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience.",
      "plausible_mechanism": "Easily recalled past non-events may have made the current alarm seem more benign than the available schedule information would have justified.",
      "why_not_identified": "This mechanism is reported secondhand through the operator's reasoning and is substantially captured by the identified automation-complacency occurrence; the distinct availability-heuristic component is not separable enough from the main failure to verify schedule dependencies."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Only one interview transcript was analyzed, with no independent verification of the participant's recall or actual decision data.",
    "Time pressure and multitasking are present and could contribute to non-bias performance limitations, so they are treated as context rather than bias mechanisms unless accompanied by distinct cognitive evidence.",
    "Retrieved corpus support was limited to the provided passages; other established biases, if present, may not have adequate corpus support.",
    "Hindsight reflection by the participant was not treated as proof of biased reasoning at the time of the decisions."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific incident from your work as a production planner, and I'll be asking you to walk me through what happened and why you made the calls you did. Nothing you say here affects your performance record. Sound good? Participant: Yeah, that's fine. Happy to walk through it. It was a memorable afternoon. Interviewer: Can you tell me a bit about your role, then give me the overview of the incident? Participant: I'm the production planner for three parallel lines at our plant — discrete assembly, mid-volume SKUs, frequent changeovers. I sequence what runs where, manage changeover windows, and hit ship cutoffs without blowing labor budgets. This was a Friday. A subcomponent we needed for two customer orders — Order A and Order B — came in four hours late from the supplier. Both had the same end-of-shift ship cutoff, so as soon as I heard about the delay I knew I had a compressed window to get everything sequenced and out the door. Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened after you learned about the late delivery? Participant: Once I confirmed the component landed, I pulled up the MES to see where Line 1 and Line 2 stood — both mid-run on other SKUs, so I needed changeovers on both to get to the rush SKUs. Problem was, I only had one certified changeover tech on shift. That was my first call — which line gets the tech first. Around the same time, an operator flagged that Line 3 had thrown an intermittent alarm twice in the past hour. That line wasn't part of the original plan, but it had open capacity, so it became relevant as a potential overflow resource. Then there was a batch sitting in the Line 2 output buffer that QA hadn't released yet, which mattered because Order B needed some of those units. Finally, toward the end, a labeling issue on part of that batch ate into our remaining time right as the ship cutoff closed in. So four points where I had to make a call under pressure. Interviewer: Let's reconstruct the timeline before we dig into each decision. Participant: Component lands around 1pm, four hours later than the morning window. I make the technician call almost immediately, maybe 1:15. The Line 3 alarm conversation happens about 20 minutes after, while the first changeover is underway. The QA buffer question comes up around 2:30, once I'm mapping how many units Order B still needs. QA doesn't call back until 3:10, which is when the labeling discrepancy surfaces. From there it's a sprint — cutoff is 5pm, so the last call, about overtime and the carrier, happens around 3:30. Interviewer: Let's start with the technician assignment. What information did you have? Participant: I knew Order A was the bigger order by unit count, and Line 2 had a tighter downstream packaging slot later on. Technically Line 2's changeover being late would ripple further because packaging was booked tight. In the moment I went with unit count — Order A first — partly because that's our default rule when picking between two rush jobs. I didn't split the tech's time across both lines in shorter blocks, which was an option, because that would have delayed both changeovers instead of finishing one cleanly. Interviewer: Any hesitation about the packaging slot issue? Participant: A little. But finishing one line's changeover completely felt more reliable than half-finishing two, and Order A's volume backed that up. Interviewer: Let's move to the Line 3 alarm. Walk me through that call. Participant: The operator told me the alarm had come up before and 'usually clears itself' — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience. Given that, and given I had two other things actively unfolding — the changeover and the ship cutoff clock — I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue. Interviewer: Did you look into whether anything else depended on Line 3's output during that window? Participant: Honestly, no. I didn't check. My focus was entirely on Order A and Order B — those were the two fires in front of me — so I didn't cross-reference the schedule for anything else running through Line 3. It turned out a smaller order, Order C, also needed Line 3 output that same shift, but I didn't find that out until later. I wasn't ignoring it on purpose, it just wasn't on my radar with everything else going on. Interviewer: When you found out about Order C afterward, what was your reaction? Participant: A bit of an 'oh, right' moment. Not catastrophic — we fit it in later — but it made me realize I'd made that overflow call pretty quickly without stepping back to check what else was in play on that line. Interviewer: Let's talk about the QA buffer decision. What was going through your mind? Participant: Order B needed units from that batch plus new production to hit full quantity. QA hadn't confirmed release yet, and their lead was off-site with spotty response time. I decided to provisionally build the buffer units into the Order B plan rather than wait, because waiting with no ETA on a callback risked losing time I couldn't get back. I told the team we'd adjust if QA flagged something. Interviewer: What made provisional inclusion feel right versus excluding those units? Participant: Excluding them would have guaranteed a lower fill rate regardless of what QA said, and historically that batch type passes more often than not. It felt like a reasonable bet given the clock, not a guarantee. Interviewer: And QA did call back? Participant: About forty minutes later. They confirmed the batch passed, but flagged a labeling discrepancy on a subset of units, meaning rework. Interviewer: That leads to the final decision — rework and shipment. What were you weighing? Participant: The rework was going to eat twenty minutes of Line 2 time, and cutoff was ninety minutes out. Order A was tracking fine. Order B was now at risk. Overtime authorization had just come through, but it adds cost. I could also have accepted a partial shipment and expedited the rest next shift, or called the account manager to renegotiate the cutoff. Interviewer: Why overtime and carrier coordination instead of the other two? Participant: Partial shipment felt like a worse customer experience than a slightly late full shipment, and renegotiating the cutoff was a last resort I wanted to avoid if I could still make it work operationally. Overtime plus talking to the carrier directly gave me a shot at getting the full order out with minimal disruption, even shipping a few minutes past official cutoff. Interviewer: How did that play out? Participant: Order B shipped about twelve minutes past cutoff after the carrier agreed to hold pickup briefly. Order A shipped on time. Not a clean day, but nothing was lost. Interviewer: Looking back, if you'd known upfront that Order C depended on Line 3, would you have handled that decision differently? Participant: Probably. I likely would have taken two minutes to check the schedule before committing Line 3 as overflow, rather than just going with the operator's read on the alarm. It wouldn't have changed the outcome much, but I'd have made the call with a clearer picture. Interviewer: And if you'd had fifteen more minutes before the technician assignment, would anything have changed? Participant: Maybe I'd have looked harder at splitting the tech's time, but I think I still land on Order A first given the volume difference. Interviewer: Is there a point in this sequence where, in hindsight, you wish you'd gathered more information before deciding? Participant: The Line 3 call, for sure. Everything else I feel like I had a reasonable handle on given what was knowable at the time. That one I moved through fast because I was juggling two other things, and it's the one place where a little more digging would have given me a fuller picture before I committed the line. Interviewer: That's really helpful, thank you. I think that covers everything I need. Participant: No problem, glad it was useful.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.97s · gen 70.33s · total 74.6s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0302 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0267 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0257 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0252 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0234 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0230 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0228 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0210 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0207 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0207 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
11. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0203 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0202 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0200 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0197 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
15. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0187 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0184 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0184 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
19. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0173 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0173 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
24. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0171 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0166 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
28. **Hallihan_etal_DTM_12.pdf** — 0.0165 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
29. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
31. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0159 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
33. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0158 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
34. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0158 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## Afterword | a nd rich with smells because the genes that built its brain have survived throug_
36. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0153 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0153 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
38. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration et al., 1994; McGu_
40. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0151 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## lIs sues in M ADE M E D O I T , A rmine law and order. But, if you tell the judge that your g_
42. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0149 (rrf) — _# Self - other Placement W ith no other evidence chance of success w ould also the p rinciple of_
43. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0149 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs | Suppose you are [[a/an]] [[specialist_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
45. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
47. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0142 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
48. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0140 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
49. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0138 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
50. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0138 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focuses only on participant reasoning and decision episodes affirmatively evidenced in the interview. Retrospective statements are considered only as counterevidence or contextual acknowledgment, not as independent bias occurrences."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency",
        "premature cognitive commitment",
        "automation-induced complacency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Automation complacency occurs when an operator under-samples or incompletely verifies available information about a monitored system because of prior reliable or benign system performance, especially under high task load.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Line 3 intermittent alarm and overflow-capacity decision",
      "decision_point_description": "Around 1:35 pm, after the operator reported that the Line 3 alarm had occurred before and usually cleared itself, the participant decided to treat Line 3 as available overflow capacity without cross-checking other schedule dependencies.",
      "affected_reasoning_operation": "Risk assessment and allocation of Line 3 as an overflow resource under time pressure",
      "bias_specific_mechanism": "The participant under-sampled information needed to fully evaluate the Line 3 alarm decision: he accepted the operator's report that the intermittent alarm had never caused a stoppage, and because of high task load focused narrowly on Order A and Order B rather than verifying what else depended on Line 3.",
      "manifestation_in_interview": "The participant explicitly reports accepting the operator's 'usually clears itself' description of the intermittent Line 3 alarm, deciding to treat Line 3 as available overflow, and then not checking the schedule for other dependencies such as Order C until later.",
      "effect_on_reasoning_or_decision": "The participant committed Line 3 as overflow capacity without discovering that Order C also depended on Line 3 output, so the resource-allocation decision was made with an incomplete picture of the line's actual schedule commitments.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The operator told me the alarm had come up before and 'usually clears itself' — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience. Given that, and given I had two other things actively unfolding — the changeover and the ship cutoff clock — I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue.",
          "evidence_explanation": "This quote directly shows the participant using the alarm's prior benign history and current task load as the basis for accepting Line 3 as overflow without further verification, which is the incomplete-sampling mechanism central to complacency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, no. I didn't check. My focus was entirely on Order A and Order B — those were the two fires in front of me — so I didn't cross-reference the schedule for anything else running through Line 3.",
          "evidence_explanation": "This confirms the participant did not sample available schedule information before committing the line, which is the critical verification failure defining the complacency mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I wasn't ignoring it on purpose, it just wasn't on my radar with everything else going on.",
          "evidence_explanation": "This statement shows the attentional narrowing associated with complacency under high workload: the omitted check was not an intentional decision to ignore the information but a failure to bring it into the verification process."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The Line 3 call, for sure. Everything else I feel like I had a reasonable handle on given what was knowable at the time. That one I moved through fast because I was juggling two other things, and it's the one place where a little more digging would have given me a fuller picture before I committed the line.",
          "evidence_explanation": "The participant's own post-incident assessment identifies the Line 3 decision as the point where insufficient information gathering occurred while multitasking, reinforcing the complacency interpretation."
        }
      ],
      "correction_or_counterevidence": "Later, after learning about Order C, the participant showed correction awareness: 'Probably. I likely would have taken two minutes to check the schedule before committing Line 3 as overflow, rather than just going with the operator's read on the alarm. It wouldn't have changed the outcome much, but I'd have made the call with a clearer picture.' This is retrospective recognition rather than real-time correction, so the initial decision remains classifiable, but it is recorded as counterevidence of insight after the fact.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Parasuraman and Manzey passages support automation complacency as incomplete verification or under-sampling of available system information, particularly under high task load. The present occurrence applies the same mechanism to an industrial alarm/resource-allocation context rather than a laboratory automation diagnostic task.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it. Participants were provided independent access (via mouse click) to all relevant system information (e.g., tank levels, flow rates at different valves, history graphs displaying the time course of system parameters), needed to verify the aid’s diagnoses. This procedure allowed the investigators to assess the level of operator complacency in interaction with the aid by contrasting the actual information sampling behavior of operators with a “normative model” of optimal behavior. According to this logic, any participant who accessed just the information appropriate to verify a given diagnosis before accepting it was regarded as showing noncomplacent (eutactic) behavior in interaction with the aid. However, participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "Complacency is operationalized as sampling less information than necessary to verify a system or aid before accepting its status or recommendation.",
          "relevance_to_this_occurrence": "The participant treated the operator's report about the intermittent alarm as sufficient and did not sample schedule information needed to verify that Line 3 could be safely used as overflow capacity."
        },
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "R. Parasuraman et al. (1993) provided the first empirical evidence for automation complacency and for the contributing role of high task load. They had participants perform three concurrent tasks from the Multiple Task Battery (MATB): a twodimensional compensatory tracking and an engine fuel management task, both of which had to be carried out manually, and a third task involving engine monitoring that required participants to detect abnormal readings on one of four gauges; this task was supported by an automated system that was not perfectly reliable. In different conditions, the automation had either high (88%) or low (52%) reliability in detecting engine malfunctions. Complacency was operationally defined as the operator’s not detecting or being slow to detect failures of the automation to detect engine malfunctions.",
          "mechanism_supported_by_source": "High task load and prior reliable functioning of a monitored system contribute to complacency, characterized by failure or slowness in detecting that a system status is not benign.",
          "relevance_to_this_occurrence": "The participant was juggling changeover and cutoff tasks and relied on the alarm's prior non-consequence, paralleling the high-task-load and prior-reliability conditions associated with automation complacency."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-there-itis",
        "plan continuation"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final rework and shipment decision as cutoff approached",
      "supporting_interview_quote": "Partial shipment felt like a worse customer experience than a slightly late full shipment, and renegotiating the cutoff was a last resort I wanted to avoid if I could still make it work operationally.",
      "plausible_mechanism": "The participant may have continued with the original full-shipment plan despite schedule disruption and evaluated alternatives such as partial shipment or renegotiation unfavorably in order to preserve the original plan.",
      "why_not_identified": "The transcript shows explicit consideration of alternatives and operational tradeoffs, including cost, customer experience, and the availability of overtime/carrier coordination. There is insufficient affirmative evidence that commitment to the original plan or sunk cost distorted the reasoning; the choice appears consistent with ordinary cost/risk balancing under time pressure."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a single retrospective self-report, so objective corroboration of alarms, schedule dependencies, or actual information availability is not present.",
    "The retrieved corpus support concerns automation complacency mainly in experimental or aviation settings, so the label is applied analogically to a production-planning alarm decision.",
    "Some retrospective statements from the participant could be influenced by knowing the later Order C outcome, so real-time versus hindsight reasoning was separated conservatively."
  ]
}

