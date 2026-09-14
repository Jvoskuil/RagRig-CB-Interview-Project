# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal research purposes only, and you can pause or skip anything. Is that alright? Participant: Yep, that's fine. Interviewer: Great. Can you start by telling me your role and roughly how long you've been doing it? Participant: I'm a Security Architect. I've been at the company about five years, and for the last three I've owned most of our network segmentation architecture — design, implementation, the whole Zero Trust rollout. Interviewer: Let's talk through the incident we discussed scheduling this around. What triggered it? Participant: We had an external penetration test as part of prep for our annual audit cycle. The report came back with three findings. One was a segmentation gap allowing lateral movement between two zones we thought were isolated. Another was stale service-account credentials, and the third was incomplete log retention. Only the segmentation one was rated critical. Interviewer: What was your objective once you saw that report? Participant: Close the critical gap before the compliance window, without blowing up the rest of the Zero Trust program or causing outages. We had six weeks. Engineering bandwidth was tight — I basically had myself and one platform engineer who could help part-time. Any vendor spend needed budget sign-off, and leadership wanted an actual remediation plan, not just 'we found a problem.' Interviewer: Walk me through what happened first. Participant: First thing was triage. Three findings, limited hands, six weeks. I looked at severity and exploitability — the segmentation gap was the only one that let an attacker actually traverse between trust zones, so it was the obvious pick to go first. Credential rotation is scriptable and fast, log retention is a config change, neither needed the same urgency. So I told the CISO we'd tackle segmentation first and run the other two in parallel at lower priority, mostly automated. Interviewer: What information did you have at that point versus what you learned afterward? Participant: Initially I just had severity ratings. Once we dug in, we confirmed the lateral movement path was real — not just theoretical — between two zones that were supposed to be firewalled from each other. That's when platform engineering told me they genuinely didn't have spare capacity to fix all three at full depth simultaneously, which confirmed the sequencing call. Interviewer: Let's go deeper on that first decision. Any alternative you seriously considered? Participant: Running all three in parallel at reduced depth crossed my mind, but diluting effort across three findings when only one is critical felt like the wrong risk math. I ruled it out fairly quickly. Interviewer: Once segmentation was the priority, how did you approach fixing it? Participant: That's the part that took the most back-and-forth. The segmentation layer runs on a framework I built myself when we started the Zero Trust program. I know its internals cold — every policy enforcement point, every identity-aware proxy hook. The pentest vendor actually flagged that a vendor-managed ZTNA platform could close the same gap with less custom engineering, and there were some independent benchmarks suggesting similar coverage. Interviewer: What sources did you pull in to compare the two paths? Participant: I looked at our own effort estimates mostly. Patching the in-house framework was about four weeks of engineering time, with some uncertainty on edge-case coverage. The vendor path was quoted around three weeks including their security review, and they were offering coverage guarantees in writing. Interviewer: So the vendor path was faster and came with a written guarantee. What made you go with the in-house patch? Participant: Honestly, I trust what I built. I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider. The vendor's guarantee sounds good on paper, but 'guarantee' from a sales engineer isn't the same as proof in our specific environment. I wanted to see their platform actually validated against our topology before I'd trust it the way I trust code I wrote and have watched in production for three years. Interviewer: Did you apply that same validation standard to the in-house patch — proving it against your topology before trusting it? Participant: Not really the same way, no. I mean, I've lived with that system for three years, so it's not like I needed to re-prove it from scratch. It's more that the vendor is the newer unknown. Interviewer: Had you evaluated ZTNA vendors before this incident? Participant: We'd looked at two platforms about a year earlier for a different project, and didn't move forward, mostly on cost. So there was some familiarity, but no deep hands-on testing. Interviewer: How did time pressure factor into that decision? Participant: There was pressure, but not extreme — six weeks was workable either way at that point. It wasnns't really the deadline pushing me toward the in-house option; it was more that I was confident I understood exactly what patching would take. Interviewer: What did you present to the CISO? Participant: I recommended patching and extending the existing framework, and that's what we went with. Afterward, platform engineering raised some integration concerns — mainly around a legacy service that didn't fit cleanly into the updated policy model — that hadn't been fully weighted when I made the original comparison. Interviewer: Let's move to rollout. Once the patch was ready, what were your options? Participant: Two real choices: a narrow pilot on one trust zone first, or roll out to all affected zones at once to save time, since we were now down to four weeks. There was also a middle option — stage it by risk tier over two weeks. Interviewer: What did you choose and why? Participant: Staged by risk tier. Full rollout all at once felt too risky if something broke — you'd have no isolated blast radius. A narrow pilot alone would've been safer but slower, and we didn't have four weeks to spare on a single-zone pilot before expanding. Staging let us validate against the highest-risk zones first while still making progress elsewhere. Interviewer: Did anything unexpected come up during that rollout? Participant: Yes — a legacy service ended up bypassing the new policy enforcement point entirely. It wasn't something we'd flagged as a risk going in. Platform engineering said fixing it properly would need more time than we had left. Interviewer: What information, if you'd had it earlier, would have changed that rollout decision? Participant: If we'd known about that legacy service's behavior beforehand, I probably would've included a targeted pilot on that specific service before staging everything else, rather than finding out mid-rollout. Interviewer: Final decision point — reporting to the audit committee with two weeks left and an unresolved edge case. What were your options? Participant: Report it as fully remediated, report as substantially remediated with a compensating control and a follow-up date, or ask for a deadline extension. Interviewer: What did you decide? Participant: Substantially remediated, with a documented compensating control on the legacy service and a committed date to close it out next sprint. Fully remediated would've been inaccurate given the open edge case, and I didn't think an extension was necessary since the core lateral-movement path was actually closed. Interviewer: How confident were you in that characterization? Participant: Reasonably confident. The committee accepted it with a follow-up item, which is roughly what I expected. Interviewer: Looking back — if a different engineer, someone no longer at the company, had originally built that segmentation framework instead of you, do you think the remediation choice at decision point two plays out the same way? Participant: That's a fair question. I'd like to think I'd have weighed the vendor option the same either way, but I'll admit — if it were someone else's code, someone I couldn't personally vouch for at 2 a.m. if something broke, I might have leaned harder on the vendor's written guarantees instead of my own confidence in the system. Interviewer: And if the vendor platform had been proposed to replace someone else's system rather than yours? Participant: I probably would've asked for the same proof-of-concept against our topology from both sides, rather than treating my own system as the trusted baseline by default. Interviewer: Last one — anything you'd do differently facing this same situation again? Participant: Maybe get an outside technical review of both options before I made the call, just to check my own read on the comparison. Overall the outcome was fine, but I can see how the sequence of judgments got there. Interviewer: That's really helpful — thank you for walking through it in this much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 4.14s · gen 158.90s · total 165.8s_

**Retrieved** (ranked by store ranker):
1. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0282 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0268 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0263 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0251 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
5. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0241 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
6. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0231 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
7. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0227 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
8. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0218 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
9. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0199 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0185 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0181 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0180 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **Hallihan_etal_DTM_12.pdf** — 0.0180 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
14. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0178 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
16. **Hallihan_etal_DTM_12.pdf** — 0.0170 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0170 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
18. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0167 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
19. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0167 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
21. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0165 (rrf) — _# f Space Flight by inadequate communication. One contributing facto this lack of communication _
22. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0165 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
23. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0165 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0165 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0164 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
26. **Hallihan_etal_DTM_12.pdf** — 0.0162 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
28. **Lyell Automation bias and verification complexity.pdf** — 0.0160 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
29. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
30. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0158 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0156 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
36. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0155 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
39. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0150 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
41. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0145 (rrf) — _# 4.2 Answering our RQs AI & SOCIETY the AI’s recommendation, provided as a second opinion, alig_
42. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0143 (rrf) — _# Appendix A. Survey Questionnaire • Incorporating personal elements such as phone numbers, birt_
43. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0142 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
45. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0141 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
47. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0139 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
49. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0137 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
50. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0136 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Mechanism-first evaluation of the participant's self-reported reasoning during a security incident remediation decision chain. Only affirmative, evidence-supported distortions were classified as identified occurrences; plausible but unconfirmed patterns were retained as candidates."
  },
  "identified_bias_summary": [
    {
      "bias_label": "IKEA effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "IKEA effect",
      "alternative_labels": [
        "Not invented here bias",
        "Effort justification"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overvalue objects, solutions, or systems that one has created or assembled, leading to inflated trust or preference relative to externally produced alternatives even when objective attributes do not justify that preference.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Remediation approach selection: in-house patch vs vendor-managed ZTNA",
      "decision_point_description": "Choice between patching the internally built segmentation framework and adopting a vendor-managed ZTNA platform to close the critical segmentation gap.",
      "affected_reasoning_operation": "Evaluation and weighting of alternative remediation options; comparative risk/benefit and trust assessment before recommendation to the CISO.",
      "bias_specific_mechanism": "The participant treated the self-built in-house system as a trusted baseline by default and applied an asymmetrical validation standard: the vendor platform was required to prove itself against the environment, while the in-house system was not. This inflated the relative perceived value of the self-created option and led to discounting the vendor's objectively favorable attributes, including shorter estimated timeline and written coverage guarantees.",
      "manifestation_in_interview": "The participant acknowledged the vendor path was faster and came with written guarantees, but recommended the in-house patch based on trust in code he wrote. He explicitly stated he did not require the same validation of the in-house system, and later admitted that if someone else had built the framework, he might have weighed the vendor option differently.",
      "effect_on_reasoning_or_decision": "The recommendation was directed toward the self-built system despite an objectively competitive or advantageous external option. Platform engineering later raised integration concerns that had not been fully weighted in the original comparison.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I trust what I built. I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider. The vendor's guarantee sounds good on paper, but 'guarantee' from a sales engineer isn't the same as proof in our specific environment. I wanted to see their platform actually validated against our topology before I'd trust it the way I trust code I wrote and have watched in production for three years.",
          "evidence_explanation": "Shows default trust in the self-built system and a higher evidentiary demand for the vendor option despite the vendor's favorable attributes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really the same way, no. I mean, I've lived with that system for three years, so it's not like I needed to re-prove it from scratch. It's more that the vendor is the newer unknown.",
          "evidence_explanation": "Directly demonstrates the asymmetrical validation standard: the in-house solution was exempted from the proof requirement applied to the vendor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd like to think I'd have weighed the vendor option the same either way, but I'll admit — if it were someone else's code, someone I couldn't personally vouch for at 2 a.m. if something broke, I might have leaned harder on the vendor's written guarantees instead of my own confidence in the system.",
          "evidence_explanation": "Counterfactual admission that self-ownership, rather than purely technical evidence, influenced the relative weighting of options."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I probably would've asked for the same proof-of-concept against our topology from both sides, rather than treating my own system as the trusted baseline by default.",
          "evidence_explanation": "Acknowledges that the self-built system was treated as a default trusted baseline rather than being compared symmetrically with the external alternative."
        }
      ],
      "correction_or_counterevidence": "The in-house system had a real operational track record, and the participant had legitimate technical familiarity with it. Requiring vendor validation before trusting an external platform was not entirely irrational. However, the explicit asymmetry in validation demands and the counterfactual self-report indicate that self-creation/ownership bias materially distorted the comparison.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The supplied retrieval context did not include passages on the IKEA effect, not-invented-here bias, or effort justification. Classification relies on established general cognitive-science knowledge rather than the retrieved corpus.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Overestimation",
        "Planning fallacy"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "In-house patch planning and rollout risk assessment",
      "supporting_interview_quote": "I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider.",
      "plausible_mechanism": "Excessive confidence in the completeness of the participant's knowledge about the self-built system may have led to underweighting integration risks and failing to anticipate the legacy service bypass later encountered during rollout.",
      "why_not_identified": "The transcript also includes recognition that the in-house patch had uncertainty on edge-case coverage, and the later legacy service issue may reflect incomplete operational information rather than a distinct overconfidence distortion at the time of the decision."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was not available for the identified IKEA effect/not-invented-here mechanism, so the label and mechanism were supplied from general cognitive-science knowledge.",
    "The analysis relies on participant self-report, which may omit or rationalize aspects of the reasoning.",
    "A legitimate expertise-based explanation for preferring the known in-house system cannot be fully excluded, although the asymmetrical validation standard supports the bias classification."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal research purposes only, and you can pause or skip anything. Is that alright? Participant: Yep, that's fine. Interviewer: Great. Can you start by telling me your role and roughly how long you've been doing it? Participant: I'm a Security Architect. I've been at the company about five years, and for the last three I've owned most of our network segmentation architecture — design, implementation, the whole Zero Trust rollout. Interviewer: Let's talk through the incident we discussed scheduling this around. What triggered it? Participant: We had an external penetration test as part of prep for our annual audit cycle. The report came back with three findings. One was a segmentation gap allowing lateral movement between two zones we thought were isolated. Another was stale service-account credentials, and the third was incomplete log retention. Only the segmentation one was rated critical. Interviewer: What was your objective once you saw that report? Participant: Close the critical gap before the compliance window, without blowing up the rest of the Zero Trust program or causing outages. We had six weeks. Engineering bandwidth was tight — I basically had myself and one platform engineer who could help part-time. Any vendor spend needed budget sign-off, and leadership wanted an actual remediation plan, not just 'we found a problem.' Interviewer: Walk me through what happened first. Participant: First thing was triage. Three findings, limited hands, six weeks. I looked at severity and exploitability — the segmentation gap was the only one that let an attacker actually traverse between trust zones, so it was the obvious pick to go first. Credential rotation is scriptable and fast, log retention is a config change, neither needed the same urgency. So I told the CISO we'd tackle segmentation first and run the other two in parallel at lower priority, mostly automated. Interviewer: What information did you have at that point versus what you learned afterward? Participant: Initially I just had severity ratings. Once we dug in, we confirmed the lateral movement path was real — not just theoretical — between two zones that were supposed to be firewalled from each other. That's when platform engineering told me they genuinely didn't have spare capacity to fix all three at full depth simultaneously, which confirmed the sequencing call. Interviewer: Let's go deeper on that first decision. Any alternative you seriously considered? Participant: Running all three in parallel at reduced depth crossed my mind, but diluting effort across three findings when only one is critical felt like the wrong risk math. I ruled it out fairly quickly. Interviewer: Once segmentation was the priority, how did you approach fixing it? Participant: That's the part that took the most back-and-forth. The segmentation layer runs on a framework I built myself when we started the Zero Trust program. I know its internals cold — every policy enforcement point, every identity-aware proxy hook. The pentest vendor actually flagged that a vendor-managed ZTNA platform could close the same gap with less custom engineering, and there were some independent benchmarks suggesting similar coverage. Interviewer: What sources did you pull in to compare the two paths? Participant: I looked at our own effort estimates mostly. Patching the in-house framework was about four weeks of engineering time, with some uncertainty on edge-case coverage. The vendor path was quoted around three weeks including their security review, and they were offering coverage guarantees in writing. Interviewer: So the vendor path was faster and came with a written guarantee. What made you go with the in-house patch? Participant: Honestly, I trust what I built. I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider. The vendor's guarantee sounds good on paper, but 'guarantee' from a sales engineer isn't the same as proof in our specific environment. I wanted to see their platform actually validated against our topology before I'd trust it the way I trust code I wrote and have watched in production for three years. Interviewer: Did you apply that same validation standard to the in-house patch — proving it against your topology before trusting it? Participant: Not really the same way, no. I mean, I've lived with that system for three years, so it's not like I needed to re-prove it from scratch. It's more that the vendor is the newer unknown. Interviewer: Had you evaluated ZTNA vendors before this incident? Participant: We'd looked at two platforms about a year earlier for a different project, and didn't move forward, mostly on cost. So there was some familiarity, but no deep hands-on testing. Interviewer: How did time pressure factor into that decision? Participant: There was pressure, but not extreme — six weeks was workable either way at that point. It wasnns't really the deadline pushing me toward the in-house option; it was more that I was confident I understood exactly what patching would take. Interviewer: What did you present to the CISO? Participant: I recommended patching and extending the existing framework, and that's what we went with. Afterward, platform engineering raised some integration concerns — mainly around a legacy service that didn't fit cleanly into the updated policy model — that hadn't been fully weighted when I made the original comparison. Interviewer: Let's move to rollout. Once the patch was ready, what were your options? Participant: Two real choices: a narrow pilot on one trust zone first, or roll out to all affected zones at once to save time, since we were now down to four weeks. There was also a middle option — stage it by risk tier over two weeks. Interviewer: What did you choose and why? Participant: Staged by risk tier. Full rollout all at once felt too risky if something broke — you'd have no isolated blast radius. A narrow pilot alone would've been safer but slower, and we didn't have four weeks to spare on a single-zone pilot before expanding. Staging let us validate against the highest-risk zones first while still making progress elsewhere. Interviewer: Did anything unexpected come up during that rollout? Participant: Yes — a legacy service ended up bypassing the new policy enforcement point entirely. It wasn't something we'd flagged as a risk going in. Platform engineering said fixing it properly would need more time than we had left. Interviewer: What information, if you'd had it earlier, would have changed that rollout decision? Participant: If we'd known about that legacy service's behavior beforehand, I probably would've included a targeted pilot on that specific service before staging everything else, rather than finding out mid-rollout. Interviewer: Final decision point — reporting to the audit committee with two weeks left and an unresolved edge case. What were your options? Participant: Report it as fully remediated, report as substantially remediated with a compensating control and a follow-up date, or ask for a deadline extension. Interviewer: What did you decide? Participant: Substantially remediated, with a documented compensating control on the legacy service and a committed date to close it out next sprint. Fully remediated would've been inaccurate given the open edge case, and I didn't think an extension was necessary since the core lateral-movement path was actually closed. Interviewer: How confident were you in that characterization? Participant: Reasonably confident. The committee accepted it with a follow-up item, which is roughly what I expected. Interviewer: Looking back — if a different engineer, someone no longer at the company, had originally built that segmentation framework instead of you, do you think the remediation choice at decision point two plays out the same way? Participant: That's a fair question. I'd like to think I'd have weighed the vendor option the same either way, but I'll admit — if it were someone else's code, someone I couldn't personally vouch for at 2 a.m. if something broke, I might have leaned harder on the vendor's written guarantees instead of my own confidence in the system. Interviewer: And if the vendor platform had been proposed to replace someone else's system rather than yours? Participant: I probably would've asked for the same proof-of-concept against our topology from both sides, rather than treating my own system as the trusted baseline by default. Interviewer: Last one — anything you'd do differently facing this same situation again? Participant: Maybe get an outside technical review of both options before I made the call, just to check my own read on the comparison. Overall the outcome was fine, but I can see how the sequence of judgments got there. Interviewer: That's really helpful — thank you for walking through it in this much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.69s · gen 221.46s · total 226.7s_

**Retrieved** (ranked by store ranker):
1. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0282 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0268 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0263 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0251 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
5. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0241 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
6. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0231 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
7. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0227 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
8. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0218 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
9. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0199 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0185 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0181 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0180 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **Hallihan_etal_DTM_12.pdf** — 0.0180 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
14. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0178 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
16. **Hallihan_etal_DTM_12.pdf** — 0.0170 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0170 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
18. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0167 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
19. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0167 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
21. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0165 (rrf) — _# f Space Flight by inadequate communication. One contributing facto this lack of communication _
22. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0165 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
23. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0165 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0165 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0164 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
26. **Hallihan_etal_DTM_12.pdf** — 0.0162 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
28. **Lyell Automation bias and verification complexity.pdf** — 0.0160 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
29. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
30. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0158 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0156 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
36. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0155 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
39. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0150 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
41. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0145 (rrf) — _# 4.2 Answering our RQs AI & SOCIETY the AI’s recommendation, provided as a second opinion, alig_
42. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0143 (rrf) — _# Appendix A. Survey Questionnaire • Incorporating personal elements such as phone numbers, birt_
43. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0142 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
45. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0141 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
47. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0139 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
49. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0137 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
50. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0136 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of the participant's self-reported reasoning during a security remediation project; only mechanisms with affirmative interview evidence are reported."
  },
  "identified_bias_summary": [
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
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or hypotheses, while giving less weight to contrary evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of remediation approach for the critical segmentation gap",
      "decision_point_description": "Choosing between patching the participant-built in-house Zero Trust framework and adopting a vendor-managed ZTNA platform",
      "affected_reasoning_operation": "Evidence evaluation and option comparison",
      "bias_specific_mechanism": "The participant's prior belief that his own code was trustworthy created asymmetric evidentiary standards: he treated the in-house system as a trusted baseline by default, while requiring the vendor to supply topology-specific proof before he would trust its written guarantees and benchmark evidence.",
      "manifestation_in_interview": "The participant reported relying mostly on his own effort estimates, discounted the vendor's faster quote and written coverage guarantee as sales-engineer talk, and explicitly acknowledged not applying the same validation standard to the in-house patch. He later stated that if the system had been built by someone else, he would likely have requested the same proof-of-concept from both sides.",
      "effect_on_reasoning_or_decision": "He selected the in-house patch even though the vendor path was quoted as faster and offered written coverage guarantees; platform engineering later raised integration concerns that had not been fully weighted in the original comparison.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I trust what I built. I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider. The vendor's guarantee sounds good on paper, but 'guarantee' from a sales engineer isn't the same as proof in our specific environment. I wanted to see their platform actually validated against our topology before I'd trust it the way I trust code I wrote and have watched in production for three years.",
          "evidence_explanation": "This quote reveals the prior trust in the self-built system and the demand for stronger proof from the vendor, an asymmetry consistent with confirmation bias in evidence evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really the same way, no. I mean, I've lived with that system for three years, so it's not like I needed to re-prove it from scratch. It's more that the vendor is the newer unknown.",
          "evidence_explanation": "This direct admission shows that the in-house option was exempted from the validation standard required of the vendor, confirming asymmetric evidence weighting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I probably would've asked for the same proof-of-concept against our topology from both sides, rather than treating my own system as the trusted baseline by default.",
          "evidence_explanation": "This counterfactual self-insight supports a bias-specific mechanism: the default trust depended on authorship, not on neutral technical comparison."
        }
      ],
      "correction_or_counterevidence": "Participant later acknowledged the asymmetry and said he would consider an outside technical review next time; also noted that if someone else had built the framework, he might have leaned harder on the vendor's written guarantees. This recognition does not undo the original biased comparison.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The confirmation-bias label and the evidence-selection/prioritization mechanism are supported by the retrieved Cook/Smallman passage.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Results revealed no bias at as- sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "The source documents a confirmation-bias mechanism in which analysts favor and prioritize evidence that supports an initial hypothesis rather than applying balanced evidentiary standards.",
          "relevance_to_this_occurrence": "The participant displayed a similar pattern during option comparison: evidence favoring the trusted in-house system was accepted on familiarity, while vendor evidence was subjected to a stricter proof requirement."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The evidence is retrospective self-report rather than direct observation of the decision process, so the asymmetry may be partly reconstructed after the fact.",
    "The retrieved confirmation-bias support comes from an intelligence-analysis domain, not cybersecurity vendor selection, so cross-domain transfer is inferential.",
    "Organizational constraints, familiarity with the existing system, and legitimate concerns about vendor guarantees could also explain part of the choice; the bias identification relies on the participant's explicit asymmetric validation standard and later counterfactual admission."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal research purposes only, and you can pause or skip anything. Is that alright? Participant: Yep, that's fine. Interviewer: Great. Can you start by telling me your role and roughly how long you've been doing it? Participant: I'm a Security Architect. I've been at the company about five years, and for the last three I've owned most of our network segmentation architecture — design, implementation, the whole Zero Trust rollout. Interviewer: Let's talk through the incident we discussed scheduling this around. What triggered it? Participant: We had an external penetration test as part of prep for our annual audit cycle. The report came back with three findings. One was a segmentation gap allowing lateral movement between two zones we thought were isolated. Another was stale service-account credentials, and the third was incomplete log retention. Only the segmentation one was rated critical. Interviewer: What was your objective once you saw that report? Participant: Close the critical gap before the compliance window, without blowing up the rest of the Zero Trust program or causing outages. We had six weeks. Engineering bandwidth was tight — I basically had myself and one platform engineer who could help part-time. Any vendor spend needed budget sign-off, and leadership wanted an actual remediation plan, not just 'we found a problem.' Interviewer: Walk me through what happened first. Participant: First thing was triage. Three findings, limited hands, six weeks. I looked at severity and exploitability — the segmentation gap was the only one that let an attacker actually traverse between trust zones, so it was the obvious pick to go first. Credential rotation is scriptable and fast, log retention is a config change, neither needed the same urgency. So I told the CISO we'd tackle segmentation first and run the other two in parallel at lower priority, mostly automated. Interviewer: What information did you have at that point versus what you learned afterward? Participant: Initially I just had severity ratings. Once we dug in, we confirmed the lateral movement path was real — not just theoretical — between two zones that were supposed to be firewalled from each other. That's when platform engineering told me they genuinely didn't have spare capacity to fix all three at full depth simultaneously, which confirmed the sequencing call. Interviewer: Let's go deeper on that first decision. Any alternative you seriously considered? Participant: Running all three in parallel at reduced depth crossed my mind, but diluting effort across three findings when only one is critical felt like the wrong risk math. I ruled it out fairly quickly. Interviewer: Once segmentation was the priority, how did you approach fixing it? Participant: That's the part that took the most back-and-forth. The segmentation layer runs on a framework I built myself when we started the Zero Trust program. I know its internals cold — every policy enforcement point, every identity-aware proxy hook. The pentest vendor actually flagged that a vendor-managed ZTNA platform could close the same gap with less custom engineering, and there were some independent benchmarks suggesting similar coverage. Interviewer: What sources did you pull in to compare the two paths? Participant: I looked at our own effort estimates mostly. Patching the in-house framework was about four weeks of engineering time, with some uncertainty on edge-case coverage. The vendor path was quoted around three weeks including their security review, and they were offering coverage guarantees in writing. Interviewer: So the vendor path was faster and came with a written guarantee. What made you go with the in-house patch? Participant: Honestly, I trust what I built. I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider. The vendor's guarantee sounds good on paper, but 'guarantee' from a sales engineer isn't the same as proof in our specific environment. I wanted to see their platform actually validated against our topology before I'd trust it the way I trust code I wrote and have watched in production for three years. Interviewer: Did you apply that same validation standard to the in-house patch — proving it against your topology before trusting it? Participant: Not really the same way, no. I mean, I've lived with that system for three years, so it's not like I needed to re-prove it from scratch. It's more that the vendor is the newer unknown. Interviewer: Had you evaluated ZTNA vendors before this incident? Participant: We'd looked at two platforms about a year earlier for a different project, and didn't move forward, mostly on cost. So there was some familiarity, but no deep hands-on testing. Interviewer: How did time pressure factor into that decision? Participant: There was pressure, but not extreme — six weeks was workable either way at that point. It wasnns't really the deadline pushing me toward the in-house option; it was more that I was confident I understood exactly what patching would take. Interviewer: What did you present to the CISO? Participant: I recommended patching and extending the existing framework, and that's what we went with. Afterward, platform engineering raised some integration concerns — mainly around a legacy service that didn't fit cleanly into the updated policy model — that hadn't been fully weighted when I made the original comparison. Interviewer: Let's move to rollout. Once the patch was ready, what were your options? Participant: Two real choices: a narrow pilot on one trust zone first, or roll out to all affected zones at once to save time, since we were now down to four weeks. There was also a middle option — stage it by risk tier over two weeks. Interviewer: What did you choose and why? Participant: Staged by risk tier. Full rollout all at once felt too risky if something broke — you'd have no isolated blast radius. A narrow pilot alone would've been safer but slower, and we didn't have four weeks to spare on a single-zone pilot before expanding. Staging let us validate against the highest-risk zones first while still making progress elsewhere. Interviewer: Did anything unexpected come up during that rollout? Participant: Yes — a legacy service ended up bypassing the new policy enforcement point entirely. It wasn't something we'd flagged as a risk going in. Platform engineering said fixing it properly would need more time than we had left. Interviewer: What information, if you'd had it earlier, would have changed that rollout decision? Participant: If we'd known about that legacy service's behavior beforehand, I probably would've included a targeted pilot on that specific service before staging everything else, rather than finding out mid-rollout. Interviewer: Final decision point — reporting to the audit committee with two weeks left and an unresolved edge case. What were your options? Participant: Report it as fully remediated, report as substantially remediated with a compensating control and a follow-up date, or ask for a deadline extension. Interviewer: What did you decide? Participant: Substantially remediated, with a documented compensating control on the legacy service and a committed date to close it out next sprint. Fully remediated would've been inaccurate given the open edge case, and I didn't think an extension was necessary since the core lateral-movement path was actually closed. Interviewer: How confident were you in that characterization? Participant: Reasonably confident. The committee accepted it with a follow-up item, which is roughly what I expected. Interviewer: Looking back — if a different engineer, someone no longer at the company, had originally built that segmentation framework instead of you, do you think the remediation choice at decision point two plays out the same way? Participant: That's a fair question. I'd like to think I'd have weighed the vendor option the same either way, but I'll admit — if it were someone else's code, someone I couldn't personally vouch for at 2 a.m. if something broke, I might have leaned harder on the vendor's written guarantees instead of my own confidence in the system. Interviewer: And if the vendor platform had been proposed to replace someone else's system rather than yours? Participant: I probably would've asked for the same proof-of-concept against our topology from both sides, rather than treating my own system as the trusted baseline by default. Interviewer: Last one — anything you'd do differently facing this same situation again? Participant: Maybe get an outside technical review of both options before I made the call, just to check my own read on the comparison. Overall the outcome was fine, but I can see how the sequence of judgments got there. Interviewer: That's really helpful — thank you for walking through it in this much detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.55s · gen 146.27s · total 151.3s_

**Retrieved** (ranked by store ranker):
1. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0282 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0268 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0263 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0251 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
5. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0241 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
6. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0231 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
7. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0227 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
8. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0218 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
9. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0199 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0185 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0181 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0180 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **Hallihan_etal_DTM_12.pdf** — 0.0180 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
14. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0178 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
16. **Hallihan_etal_DTM_12.pdf** — 0.0170 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0170 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
18. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0167 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
19. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0167 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
21. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0165 (rrf) — _# f Space Flight by inadequate communication. One contributing facto this lack of communication _
22. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0165 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
23. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0165 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0165 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0164 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
26. **Hallihan_etal_DTM_12.pdf** — 0.0162 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
28. **Lyell Automation bias and verification complexity.pdf** — 0.0160 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
29. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
30. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0158 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0156 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
36. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0155 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
39. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0150 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
41. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0145 (rrf) — _# 4.2 Answering our RQs AI & SOCIETY the AI’s recommendation, provided as a second opinion, alig_
42. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0143 (rrf) — _# Appendix A. Survey Questionnaire • Incorporating personal elements such as phone numbers, birt_
43. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0142 (rrf) — _# 5. Discussions 5.1. Comparison with Previous Research Our results indicate that cybersecurity _
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
45. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0141 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
47. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0139 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
49. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0137 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
50. **Cau Mitigating Human Errors and Cognitive Bias for Cyber.pdf** — 0.0136 (rrf) — _# 2. Related Work easily identifiable by humans, reducing its effectiveness in deceiving partici_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analyzed the transcript for affirmative, mechanism-specific evidence of cognitive/perceptual/memory/motivational/affective/social-influence/group-decision biases. Structural constraints, rational prioritization, insufficient information, and ordinary uncertainty were not classified as bias."
  },
  "identified_bias_summary": [
    {
      "bias_label": "IKEA effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "IKEA effect",
      "alternative_labels": ["not invented here syndrome", "endowment effect", "effort justification"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overvalue an object, solution, or system because one personally created, assembled, or invested effort in it, leading to inflated trust and asymmetric evaluation compared with externally produced alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Choice between patching the internally built segmentation framework and adopting a vendor-managed ZTNA platform",
      "decision_point_description": "During remediation of the critical segmentation gap, the participant compared extending the in-house framework against a faster vendor path with written coverage guarantees and selected the in-house patch.",
      "affected_reasoning_operation": "Option evaluation and selection; assignment of trust and validation standards across remediation alternatives",
      "bias_specific_mechanism": "Overvaluation of a self-built system due to direct authorship and multi-year production familiarity. The participant treated the in-house framework as a trusted baseline and did not apply the same proof-of-fit requirement to it that he demanded of the vendor platform. Vendor guarantees were discounted as sales claims while self-authored code was accepted as already proven.",
      "manifestation_in_interview": "The participant acknowledged that the vendor path was faster and offered written coverage guarantees, but still recommended the in-house patch. He stated that he trusted what he built and knew exactly how it behaved. When asked whether he applied the same validation standard to the in-house patch, he said not really, because the vendor was the newer unknown. He later conceded that if the framework had been someone else's code, he might have leaned harder on the vendor's written guarantees, and that he would otherwise have sought proof-of-concept from both sides.",
      "effect_on_reasoning_or_decision": "The evaluation was tilted toward the in-house option despite a faster vendor alternative with written guarantees. The asymmetric trust led to the selection of the in-house patch, and later platform engineering raised integration concerns about a legacy service that had not been fully weighted in the original comparison.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I trust what I built. I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider. The vendor's guarantee sounds good on paper, but 'guarantee' from a sales engineer isn't the same as proof in our specific environment. I wanted to see their platform actually validated against our topology before I'd trust it the way I trust code I wrote and have watched in production for three years.",
          "evidence_explanation": "This directly ties trust to self-authorship and production familiarity while discounting the vendor's evidence, demonstrating ownership-based overvaluation rather than equivalent technical comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really the same way, no. I mean, I've lived with that system for three years, so it's not like I needed to re-prove it from scratch. It's more that the vendor is the newer unknown.",
          "evidence_explanation": "This is an explicit admission of an asymmetric evidentiary standard: the self-built system was exempted from the same validation required of the external platform."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That's a fair question. I'd like to think I'd have weighed the vendor option the same either way, but I'll admit — if it were someone else's code, someone I couldn't personally vouch for at 2 a.m. if something broke, I might have leaned harder on the vendor's written guarantees instead of my own confidence in the system.",
          "evidence_explanation": "This counterfactual isolates the participant's personal authorship as the source of the differential trust, rather than objective technical merits of the two options."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I probably would've asked for the same proof-of-concept against our topology from both sides, rather than treating my own system as the trusted baseline by default.",
          "evidence_explanation": "This further confirms that the in-house system was treated as a trusted baseline by default because it was his own system, revealing the bias mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant later offered a reflective counterfactual: if the framework had been someone else's code, he might have weighed the vendor's written guarantees more heavily. He also said that facing the same situation again he might obtain an outside technical review of both options to check his own comparison. These are retrospective acknowledgments rather than contemporaneous correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus did not provide a directly applicable passage on the IKEA effect, ownership overvaluation, or not-invented-here mechanism in this engineering-remediation context. The label is applied from established general cognitive-science knowledge, not from retrieved sources.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages were not directly relevant to the self-generated/ownership overvaluation mechanism, so this analysis relies on general-knowledge labeling for the IKEA effect.",
    "Potential rollout-related biases such as optimism or planning fallacy were considered but lacked sufficient affirmative mechanism-specific interview evidence.",
    "The analysis is based on a single retrospective interview account, so contemporaneous decision processes are evaluated only through the participant's reported reasoning."
  ]
}

