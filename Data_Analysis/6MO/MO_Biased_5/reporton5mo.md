# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the turbocharger incident from your last contract, and that this is just for internal review purposes—nothing punitive. Participant: Sure, no problem. Happy to go through it. Interviewer: Can you set the scene for me—what vessel, what voyage, and what was your role at the time? Participant: I was Chief Engineer on a geared bulk carrier, mid-size, about 55,000 deadweight. We were on a laden leg, roughly 30 hours out from the discharge port. My job was running the engine room day to day—main engine, auxiliaries, all the monitoring. We'd just come off a turbocharger overhaul on the main engine, done about three weeks prior at a yard stop. It wasn't cheap, and the office had been asking for updates on it, so it was very much front of mind. Interviewer: Take me through what happened, from the first sign of trouble to how it eventually got resolved. Participant: About two days into that leg, I noticed the exhaust gas temperature on one unit was running a touch high, and there was a bit more vibration on the turbocharger casing than I'd expect. Nothing alarming—still inside the normal band, no alarm triggered. Given we'd literally just had that unit stripped and rebuilt, my first read was that it was probably just bedding in, maybe slightly different clearances after the overhaul. I kept an eye on it rather than pulling back on load, because we had a tide-restricted berth waiting for us and reducing speed then would have put that window at risk. The readings actually settled down over the next few hours, so at the time it felt like the right call. A day or so later, the monitoring system was showing everything back in the green—temperatures, scavenge air pressure, all nominal. I didn't have my second engineer pull a lube oil sample at that point. The system was telling me it was fine, and honestly that's what it's there for. We left it at that and planned to look at it properly at the next scheduled maintenance. Then, maybe twelve hours before that, my second engineer had flagged during rounds that the fuel filter differential pressure had crept up a bit. I was pretty focused on the turbocharger numbers at that point given the earlier concern, so I told him to keep an eye on it and we'd deal with it later—there was no fuel consumption issue or anything on the combustion side, so it didn't feel urgent next to what I was already watching. The real event came about ten hours before the tide window closed. We got a sudden exhaust temperature spike and a distinct knock-type vibration—clearly the bearing itself now, not just bedding in. At that point we were deep into it. We jury-rigged a fix, brought the load down, and pushed on to make berth rather than diverting. Interviewer: Let's slow down and reconstruct that in order. What did you observe first, and how did things develop from there? Participant: First was the mild vibration and temperature deviation, day two of the leg. Then it settled, then the system showed clean readings for a good stretch. The filter differential pressure note came in maybe a day and a half after that. Then the temperature spike and vibration event came about ten hours before we were due at the tide window. So there was a real gap—almost three days—between the first hint and the actual failure. Interviewer: Going back to that first deviation—what information did you actually have, and what did you weigh? Participant: I had the raw numbers, both inside the normal band, and I had the fact that this unit had just been fully overhauled. Those two things pulled in different directions a bit—on one hand you could say any deviation after a rebuild deserves a look, but on the other, we'd just paid to have that bearing and the running gear replaced, so a bearing problem three weeks later seemed like a stretch. I remember thinking it made more sense as running-in than as an actual fault. The alternative was to ease off and inspect right there, but with the tide window ahead, and given we'd just sunk real money and yard time into that unit, continuing and monitoring felt like the more reasonable read of the situation. Interviewer: When the system showed everything back in the green band, what led you to skip the manual check? Participant: Mainly that the system readout was clean across the board—no alarms, nothing trending badly. I had the option of pulling a sample; my second engineer wasn't tied up with anything else. But the system existed exactly to tell us this kind of thing, and it was telling me things were fine. Doing a manual check on top of a clean system readout felt like it would've just confirmed what the instruments were already saying. Interviewer: When the fuel filter report came in, how did you decide where to put your attention? Participant: At that moment I was watching the turbocharger closely because of the earlier reading, so that's where my head was. The filter note got acknowledged—I told him we'd track it—but I didn't stop what I was doing to dig into it. There was no fuel or combustion symptom tied to it, so it didn't compete strongly for attention against what I already considered the open item. Interviewer: When the bearing failed with the tide window ten hours out, what options did you consider, and what tipped it? Participant: Two real options: reduce right down and divert to the nearest port for a proper repair, which would've cost us the tide window and probably several days, or jury-rig something at reduced load and make our original berth. We only had a partial bearing kit onboard, not a full replacement. What tipped it, honestly, was that we'd already put so much into this unit—the overhaul cost, the time we'd already spent watching and troubleshooting it—and diverting felt like it would waste all of that on top of the schedule hit. So we went with the jury rig. Interviewer: How much did time pressure factor in across these moments, and how confident were you at each stage? Participant: The tide window was in the back of my mind at every one of these points, more so as we got closer to it. Early on I was fairly confident it was running-in. By the green-band reading I was quite confident there was nothing there. By the fuel filter note I wasn't worried at all—it seemed unrelated. By the failure itself, confidence obviously dropped, but by then options were also narrower. Interviewer: What would have changed your decision at any of these points—what information was missing? Participant: If the system had actually thrown an alarm at that first deviation, or if a manual sample early on had shown metal particulates, I'd have acted immediately. The instruments just never gave me that trigger until the spike itself. Interviewer: Looking back now, how would you characterize that very first vibration reading? Participant: Honestly, looking at it now, it was probably the bearing telling us something from the start—it seems fairly clear in hindsight that that was the early stage of the same failure, not bedding in at all. Interviewer: If the overhaul hadn't just happened, do you think you'd have reacted differently to that first signal? Participant: Probably, yes. Without the overhaul fresh in mind, an elevated reading like that might've gotten a closer look sooner rather than being read as settling-in. Interviewer: And if there'd been no tide window at all—would the decision at the failure point have gone differently? Participant: It's possible. Without that deadline pulling at me, diverting might have felt like a cleaner, more straightforward call rather than one that came with a schedule cost attached. Interviewer: Last one—what would you tell a junior engineer to watch for differently, based on this? Participant: I'd say don't let a recent repair make you assume a component's off the table for new problems, and don't let one system you're watching closely crowd out something else being reported to you, even if it seems minor at the time.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.96s · gen 198.13s · total 202.6s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0276 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0276 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0257 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0254 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0245 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0238 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0226 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0201 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0198 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
11. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0197 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0188 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0187 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
14. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0186 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
15. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0180 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0179 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0178 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0175 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
20. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0169 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
21. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0167 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
22. **Lyell Automation bias and verification complexity.pdf** — 0.0165 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0163 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
28. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0159 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0154 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
32. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0153 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
33. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0151 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
35. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0150 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
36. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0150 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
37. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
38. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
41. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0146 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0145 (rrf) — _# Results d along with the results. occur during incidents and accidents? in the reports. ssocia_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _## 16 5 Accidents & incidents Observed Expected The results of the chi 5.76 , p = .01 . The resu_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
49. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0142 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
50. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Retrospective narrative of a turbocharger incident on a bulk carrier. Analysis focuses on the Chief Engineer's reported reasoning at each decision point, not on outcome alone."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "expectation bias",
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
      "confidence": "moderate",
      "bias_label": "expectation bias",
      "alternative_labels": ["expectancy bias", "expectation-driven interpretation"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to perceive and interpret information in ways consistent with existing expectations, leading to underestimation of conflicting or unexpected explanations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation of elevated EGT and turbocharger casing vibration after overhaul",
      "decision_point_description": "Whether to treat the mild high EGT and vibration as benign bedding-in and continue monitoring, or to ease off and inspect immediately.",
      "affected_reasoning_operation": "Diagnostic interpretation and evidence weighting",
      "bias_specific_mechanism": "The recent turbocharger overhaul created a strong expectation that the unit was newly rebuilt and unlikely to fail. This expectation shaped interpretation of ambiguous early warning cues, making the fault hypothesis seem less plausible than the bedding-in explanation.",
      "manifestation_in_interview": "The participant interpreted a mild temperature deviation and vibration as 'probably just bedding in' because the unit had just been overhauled, and later stated that without the overhaul fresh in mind he would likely have inspected sooner.",
      "effect_on_reasoning_or_decision": "The participant decided not to ease off or inspect immediately, delaying detection of what he later considered the early stage of the bearing failure.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given we'd literally just had that unit stripped and rebuilt, my first read was that it was probably just bedding in, maybe slightly different clearances after the overhaul.",
          "evidence_explanation": "Shows that the recent overhaul, rather than only the raw readings, shaped the initial diagnostic interpretation of the abnormal cues."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking it made more sense as running-in than as an actual fault.",
          "evidence_explanation": "Directly demonstrates an expectation-consistent interpretation being favored over the possibility of a new fault."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yes. Without the overhaul fresh in mind, an elevated reading like that might've gotten a closer look sooner rather than being read as settling-in.",
          "evidence_explanation": "Counterfactual statement supports the causal role of the overhaul-based expectation in shaping the initial response."
        }
      ],
      "correction_or_counterevidence": "The readings were still inside the normal band and a recent overhaul could legitimately produce some bedding-in effects, so the interpretation was not inherently unreasonable. However, the participant's own counterfactual statement and later failure link indicate that expectation materially shaped the decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit: A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation,",
          "mechanism_supported_by_source": "The retrieved passage identifies expectation as one of the cognitive biases found in cockpit incidents and accidents.",
          "relevance_to_this_occurrence": "Supports classification of the participant's overhaul-driven interpretation of the early turbocharger cues as expectation bias."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "automation complacency",
      "alternative_labels": ["automation bias", "overtrust in automation", "automation-induced complacency"],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient monitoring, verification, or information sampling in interaction with automated systems because of overtrust in those systems.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to skip manual lube oil sampling after monitoring system returned green readings",
      "decision_point_description": "Whether to pull a lube oil sample for manual verification or rely on the clean automated monitoring-system readings and defer inspection.",
      "affected_reasoning_operation": "Verification and information sampling",
      "bias_specific_mechanism": "The participant trusted the automated monitoring system to serve as the authoritative signal for engine condition. Because the system showed all parameters in the green band, he judged a manual diagnostic check as redundant rather than as a necessary independent verification, leading to reduced information sampling.",
      "manifestation_in_interview": "The participant explicitly stated that he had the option to pull a sample and that his second engineer was available, but he reasoned that the clean system readout made a manual check merely confirmatory.",
      "effect_on_reasoning_or_decision": "The decision skipped an available manual lube oil sample, removing a diagnostic opportunity that could have revealed early bearing particulates before the failure escalation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The system was telling me it was fine, and honestly that's what it's there for.",
          "evidence_explanation": "Indicates reliance on the automated monitoring system as sufficient to establish engine condition."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I had the option of pulling a sample; my second engineer wasn't tied up with anything else. But the system existed exactly to tell us this kind of thing, and it was telling me things were fine. Doing a manual check on top of a clean system readout felt like it would've just confirmed what the instruments were already saying.",
          "evidence_explanation": "Demonstrates reduced verification sampling due to overtrust in the automated display, despite available resources for a manual cross-check."
        }
      ],
      "correction_or_counterevidence": "The automated system was objectively displaying nominal green-band readings and there may not have been a procedure requiring a lube oil sample at that exact moment. The under-verification is therefore not unequivocally unsafe, but the reasoning pattern matches automation complacency.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "The source operationalizes operator complacency as sampling less information than necessary to verify automation output.",
          "relevance_to_this_occurrence": "The participant sampled less diagnostic information than available after the automated system displayed clean readings, consistent with this definition of automation complacency."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis", "plan continuation", "sunk cost fallacy"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an original plan even when new information or changing conditions suggest that the plan should be abandoned or revised.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to bearing failure ten hours before the tide-window berth",
      "decision_point_description": "Whether to divert to the nearest port for proper repair or jury-rig the turbocharger at reduced load and continue to the original destination berth.",
      "affected_reasoning_operation": "Choice between diversion and plan continuation under degraded conditions",
      "bias_specific_mechanism": "After a clear bearing failure, the participant continued toward the original destination rather than diverting. He was influenced by the prior overhaul investment, time already spent troubleshooting, and schedule commitment, which biased the evaluation of the diversion option as more costly than continued degraded operation.",
      "manifestation_in_interview": "The participant framed the decision as two real options, but reported that prior investment and schedule pressure tipped him toward a jury-rigged fix and making the original berth.",
      "effect_on_reasoning_or_decision": "The participant chose to continue the voyage with a jury-rigged reduced-load running arrangement and only a partial bearing kit onboard rather than diverting for a proper repair.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We jury-rigged a fix, brought the load down, and pushed on to make berth rather than diverting.",
          "evidence_explanation": "Directly states the decision to continue the original plan instead of diverting after the failure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "What tipped it, honestly, was that we'd already put so much into this unit—the overhaul cost, the time we'd already spent watching and troubleshooting it—and diverting felt like it would waste all of that on top of the schedule hit. So we went with the jury rig.",
          "evidence_explanation": "Shows the motivational drivers of plan continuation: sunk costs in the overhaul and troubleshooting effort, plus schedule pressure, rather than a technical judgment that continuing was safer or equally safe."
        }
      ],
      "correction_or_counterevidence": "There may have been real operational or parts constraints limiting the attractiveness of diversion, but the participant did not cite those as the primary reason. His stated reasoning foregrounds prior investment and the schedule cost of diverting.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit: A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "plan continuation , and in some cases multiple biases",
          "mechanism_supported_by_source": "The retrieved passage identifies plan continuation as a cognitive bias operating in crew decisions during incidents and accidents.",
          "relevance_to_this_occurrence": "Supports classification of the decision to press on to the original berth after bearing failure as plan continuation bias."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "attentional tunneling",
      "alternative_labels": ["task fixation", "selective attention"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Deprioritization of fuel filter differential pressure report while monitoring the turbocharger",
      "supporting_interview_quote": "At that moment I was watching the turbocharger closely because of the earlier reading, so that's where my head was. The filter note got acknowledged—I told him we'd track it—but I didn't stop what I was doing to dig into it. There was no fuel or combustion symptom tied to it, so it didn't compete strongly for attention against what I already considered the open item.",
      "plausible_mechanism": "Top-down attention to the previously flagged turbocharger may have reduced processing of the new fuel filter cue, potentially delaying detection of a separately developing problem.",
      "why_not_identified": "The fuel filter differential pressure change was minor and had no associated fuel or combustion symptom. Prioritizing the turbocharger may have been a reasonable triage decision rather than a clear bias-driven distortion."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "hindsight bias",
      "alternative_labels": ["knew-it-all-along effect"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Retrospective assessment of the first vibration reading after the bearing failure",
      "supporting_interview_quote": "Honestly, looking at it now, it was probably the bearing telling us something from the start—it seems fairly clear in hindsight that that was the early stage of the same failure, not bedding in at all.",
      "plausible_mechanism": "After learning the outcome, the participant may retroactively judge the early cue as more diagnostic than it appeared at the time.",
      "why_not_identified": "The participant explicitly frames the clarity as hindsight and may be appropriately updating his causal understanding after the failure; there is no clear statement that he would have predicted the failure at the time."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective self-report interview without independent operational data, engine logs, or objective sensor records.",
    "Some retrieved corpus passages are OCR-fragmented or incomplete, limiting precise definitional and metadata extraction.",
    "Attribution of bias relies partly on self-reported reasoning and counterfactual reflections rather than direct behavioral observation.",
    "Candidate biases were not counted as identified occurrences because they could be explained by legitimate triage, outcome knowledge, or ordinary professional judgment.",
    "Confidence levels reflect the strength of affirmative transcript evidence and available corpus support, not the severity of the operational outcome."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the turbocharger incident from your last contract, and that this is just for internal review purposes—nothing punitive. Participant: Sure, no problem. Happy to go through it. Interviewer: Can you set the scene for me—what vessel, what voyage, and what was your role at the time? Participant: I was Chief Engineer on a geared bulk carrier, mid-size, about 55,000 deadweight. We were on a laden leg, roughly 30 hours out from the discharge port. My job was running the engine room day to day—main engine, auxiliaries, all the monitoring. We'd just come off a turbocharger overhaul on the main engine, done about three weeks prior at a yard stop. It wasn't cheap, and the office had been asking for updates on it, so it was very much front of mind. Interviewer: Take me through what happened, from the first sign of trouble to how it eventually got resolved. Participant: About two days into that leg, I noticed the exhaust gas temperature on one unit was running a touch high, and there was a bit more vibration on the turbocharger casing than I'd expect. Nothing alarming—still inside the normal band, no alarm triggered. Given we'd literally just had that unit stripped and rebuilt, my first read was that it was probably just bedding in, maybe slightly different clearances after the overhaul. I kept an eye on it rather than pulling back on load, because we had a tide-restricted berth waiting for us and reducing speed then would have put that window at risk. The readings actually settled down over the next few hours, so at the time it felt like the right call. A day or so later, the monitoring system was showing everything back in the green—temperatures, scavenge air pressure, all nominal. I didn't have my second engineer pull a lube oil sample at that point. The system was telling me it was fine, and honestly that's what it's there for. We left it at that and planned to look at it properly at the next scheduled maintenance. Then, maybe twelve hours before that, my second engineer had flagged during rounds that the fuel filter differential pressure had crept up a bit. I was pretty focused on the turbocharger numbers at that point given the earlier concern, so I told him to keep an eye on it and we'd deal with it later—there was no fuel consumption issue or anything on the combustion side, so it didn't feel urgent next to what I was already watching. The real event came about ten hours before the tide window closed. We got a sudden exhaust temperature spike and a distinct knock-type vibration—clearly the bearing itself now, not just bedding in. At that point we were deep into it. We jury-rigged a fix, brought the load down, and pushed on to make berth rather than diverting. Interviewer: Let's slow down and reconstruct that in order. What did you observe first, and how did things develop from there? Participant: First was the mild vibration and temperature deviation, day two of the leg. Then it settled, then the system showed clean readings for a good stretch. The filter differential pressure note came in maybe a day and a half after that. Then the temperature spike and vibration event came about ten hours before we were due at the tide window. So there was a real gap—almost three days—between the first hint and the actual failure. Interviewer: Going back to that first deviation—what information did you actually have, and what did you weigh? Participant: I had the raw numbers, both inside the normal band, and I had the fact that this unit had just been fully overhauled. Those two things pulled in different directions a bit—on one hand you could say any deviation after a rebuild deserves a look, but on the other, we'd just paid to have that bearing and the running gear replaced, so a bearing problem three weeks later seemed like a stretch. I remember thinking it made more sense as running-in than as an actual fault. The alternative was to ease off and inspect right there, but with the tide window ahead, and given we'd just sunk real money and yard time into that unit, continuing and monitoring felt like the more reasonable read of the situation. Interviewer: When the system showed everything back in the green band, what led you to skip the manual check? Participant: Mainly that the system readout was clean across the board—no alarms, nothing trending badly. I had the option of pulling a sample; my second engineer wasn't tied up with anything else. But the system existed exactly to tell us this kind of thing, and it was telling me things were fine. Doing a manual check on top of a clean system readout felt like it would've just confirmed what the instruments were already saying. Interviewer: When the fuel filter report came in, how did you decide where to put your attention? Participant: At that moment I was watching the turbocharger closely because of the earlier reading, so that's where my head was. The filter note got acknowledged—I told him we'd track it—but I didn't stop what I was doing to dig into it. There was no fuel or combustion symptom tied to it, so it didn't compete strongly for attention against what I already considered the open item. Interviewer: When the bearing failed with the tide window ten hours out, what options did you consider, and what tipped it? Participant: Two real options: reduce right down and divert to the nearest port for a proper repair, which would've cost us the tide window and probably several days, or jury-rig something at reduced load and make our original berth. We only had a partial bearing kit onboard, not a full replacement. What tipped it, honestly, was that we'd already put so much into this unit—the overhaul cost, the time we'd already spent watching and troubleshooting it—and diverting felt like it would waste all of that on top of the schedule hit. So we went with the jury rig. Interviewer: How much did time pressure factor in across these moments, and how confident were you at each stage? Participant: The tide window was in the back of my mind at every one of these points, more so as we got closer to it. Early on I was fairly confident it was running-in. By the green-band reading I was quite confident there was nothing there. By the fuel filter note I wasn't worried at all—it seemed unrelated. By the failure itself, confidence obviously dropped, but by then options were also narrower. Interviewer: What would have changed your decision at any of these points—what information was missing? Participant: If the system had actually thrown an alarm at that first deviation, or if a manual sample early on had shown metal particulates, I'd have acted immediately. The instruments just never gave me that trigger until the spike itself. Interviewer: Looking back now, how would you characterize that very first vibration reading? Participant: Honestly, looking at it now, it was probably the bearing telling us something from the start—it seems fairly clear in hindsight that that was the early stage of the same failure, not bedding in at all. Interviewer: If the overhaul hadn't just happened, do you think you'd have reacted differently to that first signal? Participant: Probably, yes. Without the overhaul fresh in mind, an elevated reading like that might've gotten a closer look sooner rather than being read as settling-in. Interviewer: And if there'd been no tide window at all—would the decision at the failure point have gone differently? Participant: It's possible. Without that deadline pulling at me, diverting might have felt like a cleaner, more straightforward call rather than one that came with a schedule cost attached. Interviewer: Last one—what would you tell a junior engineer to watch for differently, based on this? Participant: I'd say don't let a recent repair make you assume a component's off the table for new problems, and don't let one system you're watching closely crowd out something else being reported to you, even if it seems minor at the time.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.81s · gen 222.68s · total 226.8s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0276 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0276 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0257 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0254 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0245 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0238 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0226 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0201 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0198 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
11. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0197 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0188 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0187 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
14. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0186 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
15. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0180 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0179 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0178 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0175 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
20. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0169 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
21. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0167 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
22. **Lyell Automation bias and verification complexity.pdf** — 0.0165 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0163 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
28. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0159 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0154 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
32. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0153 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
33. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0151 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
35. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0150 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
36. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0150 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
37. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
38. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
41. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0146 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0145 (rrf) — _# Results d along with the results. occur during incidents and accidents? in the reports. ssocia_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _## 16 5 Accidents & incidents Observed Expected The results of the chi 5.76 , p = .01 . The resu_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
49. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0142 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
50. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis covers the participant's description of the turbocharger incident, including initial interpretation of ambiguous readings, monitoring decisions, attention allocation, final repair/diversion decision, and retrospective judgments."
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
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "hindsight bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
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
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "expectation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation of post-overhaul turbocharger vibration and exhaust temperature deviation",
      "decision_point_description": "Whether to reduce load/inspect immediately or continue and monitor",
      "affected_reasoning_operation": "Causal interpretation of ambiguous engine parameter deviations",
      "bias_specific_mechanism": "The recent overhaul created a strong prior expectation that elevated vibration/temperature was 'bedding in,' leading ambiguous readings to be interpreted as consistent with that benign explanation rather than as a possible bearing fault.",
      "manifestation_in_interview": "The participant explicitly stated that the recent overhaul made 'running-in' seem more plausible than an actual fault, and chose to monitor rather than inspect.",
      "effect_on_reasoning_or_decision": "Delayed investigation or load reduction by almost three days; the initial cue of the eventual bearing failure was explained away.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given we'd literally just had that unit stripped and rebuilt, my first read was that it was probably just bedding in, maybe slightly different clearances after the overhaul.",
          "evidence_explanation": "Shows prior expectation from the recent overhaul guiding interpretation of the first ambiguous signal."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking it made more sense as running-in than as an actual fault. The alternative was to ease off and inspect right there, but with the tide window ahead, and given we'd just sunk real money and yard time into that unit, continuing and monitoring felt like the more reasonable read of the situation.",
          "evidence_explanation": "Explicitly describes weighing alternative interpretations but choosing the one consistent with his prior expectation that the overhauled unit should be sound."
        }
      ],
      "correction_or_counterevidence": "The readings were still inside the normal band, settled over the next few hours, and a tide-restricted berth created a genuine operational reason to avoid immediate slowdown; initially monitoring could have appeared reasonable.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism drawn from general cognitive-science knowledge; no suitable retrieved corpus passage was available for this specific occurrence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "automation bias",
        "complacency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient monitoring or verification of automated systems because of over-trust or reliance on their indications.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Skipping manual lube-oil sampling after automated monitoring returned green",
      "decision_point_description": "Whether to pull a manual lube oil sample despite clean system readout",
      "affected_reasoning_operation": "Verification and monitoring decision",
      "bias_specific_mechanism": "Over-trust in the clean automated-monitoring readout reduced information seeking; he treated absence of alarms as sufficient proof of no fault and skipped available manual confirmation.",
      "manifestation_in_interview": "The participant said the system existed to tell them this kind of thing and that a manual check would merely confirm the instruments.",
      "effect_on_reasoning_or_decision": "Missed an opportunity to detect metal particulates or other early oil evidence before the bearing failure.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The system was telling me it was fine, and honestly that's what it's there for.",
          "evidence_explanation": "Direct expression of overtrust in automated monitoring as sufficient grounds not to investigate further."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Doing a manual check on top of a clean system readout felt like it would've just confirmed what the instruments were already saying.",
          "evidence_explanation": "Shows the automation output discouraged independent verification rather than prompting it."
        }
      ],
      "correction_or_counterevidence": "The system was indeed showing nominal values and no alarms; under ordinary circumstances, manual sampling may have seemed redundant.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passage from Parasuraman and Manzey supports the complacency mechanism in automation monitoring.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it. Participants were provided independent access (via mouse click) to all relevant system information... needed to verify the aid’s diagnoses... However, participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "Complacency is operationalized as insufficient independent verification of an automated aid before accepting its diagnosis or recommendation.",
          "relevance_to_this_occurrence": "The participant accepted the automated monitoring system's clean indication without performing available independent verification via lube-oil sampling, matching this pattern."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "attentional tunneling",
      "alternative_labels": [
        "cognitive tunneling",
        "attentional bias",
        "tunnel vision"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Narrowing of attention to one salient channel or task, reducing processing of other potentially relevant signals.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "De-prioritization of fuel-filter differential-pressure increase",
      "decision_point_description": "Whether to investigate the fuel filter differential-pressure increase immediately or log and monitor it",
      "affected_reasoning_operation": "Attention allocation between concurrent operational cues",
      "bias_specific_mechanism": "Attention remained anchored to the turbocharger concern from earlier, so the new fuel-filter cue was appraised as non-urgent and not independently investigated.",
      "manifestation_in_interview": "The participant said the filter note did not compete strongly for attention against the open item he was already watching.",
      "effect_on_reasoning_or_decision": "A potentially developing fuel-system issue was deferred because the turbocharger concern crowded it out.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I was pretty focused on the turbocharger numbers at that point given the earlier concern, so I told him to keep an eye on it and we'd deal with it later—there was no fuel consumption issue or anything on the combustion side, so it didn't feel urgent next to what I was already watching.",
          "evidence_explanation": "Shows attention locked on a prior concern shaped the urgency judgment for the new cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The filter note got acknowledged—I told him we'd track it—but I didn't stop what I was doing to dig into it. There was no fuel or combustion symptom tied to it, so it didn't compete strongly for attention against what I already considered the open item.",
          "evidence_explanation": "The participant describes a narrowed attention allocation in which the turbocharger remained the dominant open item."
        }
      ],
      "correction_or_counterevidence": "No fuel or combustion symptom was present, and acknowledging and tracking the filter differential pressure may have been a reasonable triage decision rather than a clear bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism drawn from general cognitive-science knowledge; no suitable retrieved corpus passage was available for this specific attentional-narrowing occurrence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-there-itis",
        "continuation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to persist with an original plan or goal despite emerging cues that a change is warranted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Continuation to original berth after bearing failure",
      "decision_point_description": "Whether to divert to the nearest port for repair or jury-rig and continue to the original tide-restricted berth",
      "affected_reasoning_operation": "Goal and plan maintenance under changed operational conditions",
      "bias_specific_mechanism": "The original plan to make the tide-restricted berth remained dominant once the failure occurred; the participant continued under reduced load rather than revising the plan, even though the bearing failure was evident.",
      "manifestation_in_interview": "The participant described pushing on to make berth rather than diverting and framed the choice as preserving the original berth plan.",
      "effect_on_reasoning_or_decision": "Continued toward the original berth with a jury-rigged repair and reduced load instead of diverting for proper repair.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we were deep into it. We jury-rigged a fix, brought the load down, and pushed on to make berth rather than diverting.",
          "evidence_explanation": "Directly indicates continuation of the original destination plan despite the failure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Two real options: reduce right down and divert to the nearest port for a proper repair, which would've cost us the tide window and probably several days, or jury-rig something at reduced load and make our original berth.",
          "evidence_explanation": "Frames the decision in terms of preserving the original plan versus a costly revision."
        }
      ],
      "correction_or_counterevidence": "Diversion was a real operational cost with schedule and logistical consequences; use of a partial bearing kit and reduced-load operation may have made continuation a considered operational choice.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved aviation-safety corpus discusses plan continuation bias as a cognitive bias associated with continuing toward destination during later stages of flight.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Plan continuation bias was found to have influenced the crew evidence to suppor t a relationship between RE events and plan continuation bias. This continuation bias, in that it appears to occur in frequently during runway excursions on landing, after longer duties and at the latter stages of flight.",
          "mechanism_supported_by_source": "Supports plan continuation as a bias in which crews continue with the original plan even under late-stage abnormal events.",
          "relevance_to_this_occurrence": "The participant continued toward the original berth under abnormal late-voyage conditions, analogous to plan continuation bias."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to continue an endeavor or course of action because of previously invested resources, even though those costs cannot be recovered and should not influence future decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Repair/diversion decision after bearing failure",
      "decision_point_description": "Whether to divert for proper repair or jury-rig and continue toward the original berth",
      "affected_reasoning_operation": "Evaluation of repair and diversion options",
      "bias_specific_mechanism": "Past non-recoverable investments, including the overhaul cost and the time spent troubleshooting, were treated as reasons to continue with the original unit or plan rather than evaluating only future costs and benefits.",
      "manifestation_in_interview": "The participant said the decisive factor was that too much had already been put into the unit and diverting would feel like wasting that investment.",
      "effect_on_reasoning_or_decision": "The subjective weight of past costs helped justify the riskier jury-rigged continuation instead of diverting for proper repair.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "What tipped it, honestly, was that we'd already put so much into this unit—the overhaul cost, the time we'd already spent watching and troubleshooting it—and diverting felt like it would waste all of that on top of the schedule hit. So we went with the jury rig.",
          "evidence_explanation": "Explicitly weighs irrecoverable past costs as a decisive factor in the repair/diversion decision."
        }
      ],
      "correction_or_counterevidence": "Diversion also carried real future costs such as the tide window and several days of delay; the sunk cost was not the only factor, and a partial repair kit and reduced load were also considered.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism drawn from general cognitive-science knowledge; no suitable retrieved corpus passage was available for sunk cost fallacy.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to perceive events as having been more predictable after the outcome is known.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Retrospective judgment about the first turbocharger vibration reading",
      "decision_point_description": null,
      "affected_reasoning_operation": "Retrospective causal interpretation and assessment of an early signal",
      "bias_specific_mechanism": "Knowledge of the eventual bearing failure led him to reconstruct the earlier ambiguous vibration as obviously indicative of that failure.",
      "manifestation_in_interview": "The participant said it seemed fairly clear in hindsight that the first reading was the early stage of the same failure.",
      "effect_on_reasoning_or_decision": "The early ambiguous signal was retrospectively treated as more diagnostic than it appeared at the time, potentially distorting lessons learned.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, looking at it now, it was probably the bearing telling us something from the start—it seems fairly clear in hindsight that that was the early stage of the same failure, not bedding in at all.",
          "evidence_explanation": "Explicitly attributes his current sense of clarity to hindsight rather than to information available at the time."
        }
      ],
      "correction_or_counterevidence": "He hedged with 'probably,' and the early signal may actually have been the bearing failure, so the retrospective inference is not necessarily false.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism drawn from general cognitive-science knowledge; no suitable retrieved corpus passage was available for hindsight bias.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus support is partial; several established labels, including confirmation bias, sunk cost fallacy, hindsight bias, and attentional tunneling, are applied from general cognitive-science knowledge because no directly supporting passage was retrieved.",
    "The transcript is a single self-report, so classifications depend on the participant's narrative framing and may not capture biases held by other crew members.",
    "Some episodes involve overlapping mechanisms, particularly the failure-point decision where sunk cost and plan continuation may both contribute; confidence reflects this difficulty.",
    "The corpus passages from the aviation cockpit document contain extraction artifacts, so only limited verbatim support is available."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the turbocharger incident from your last contract, and that this is just for internal review purposes—nothing punitive. Participant: Sure, no problem. Happy to go through it. Interviewer: Can you set the scene for me—what vessel, what voyage, and what was your role at the time? Participant: I was Chief Engineer on a geared bulk carrier, mid-size, about 55,000 deadweight. We were on a laden leg, roughly 30 hours out from the discharge port. My job was running the engine room day to day—main engine, auxiliaries, all the monitoring. We'd just come off a turbocharger overhaul on the main engine, done about three weeks prior at a yard stop. It wasn't cheap, and the office had been asking for updates on it, so it was very much front of mind. Interviewer: Take me through what happened, from the first sign of trouble to how it eventually got resolved. Participant: About two days into that leg, I noticed the exhaust gas temperature on one unit was running a touch high, and there was a bit more vibration on the turbocharger casing than I'd expect. Nothing alarming—still inside the normal band, no alarm triggered. Given we'd literally just had that unit stripped and rebuilt, my first read was that it was probably just bedding in, maybe slightly different clearances after the overhaul. I kept an eye on it rather than pulling back on load, because we had a tide-restricted berth waiting for us and reducing speed then would have put that window at risk. The readings actually settled down over the next few hours, so at the time it felt like the right call. A day or so later, the monitoring system was showing everything back in the green—temperatures, scavenge air pressure, all nominal. I didn't have my second engineer pull a lube oil sample at that point. The system was telling me it was fine, and honestly that's what it's there for. We left it at that and planned to look at it properly at the next scheduled maintenance. Then, maybe twelve hours before that, my second engineer had flagged during rounds that the fuel filter differential pressure had crept up a bit. I was pretty focused on the turbocharger numbers at that point given the earlier concern, so I told him to keep an eye on it and we'd deal with it later—there was no fuel consumption issue or anything on the combustion side, so it didn't feel urgent next to what I was already watching. The real event came about ten hours before the tide window closed. We got a sudden exhaust temperature spike and a distinct knock-type vibration—clearly the bearing itself now, not just bedding in. At that point we were deep into it. We jury-rigged a fix, brought the load down, and pushed on to make berth rather than diverting. Interviewer: Let's slow down and reconstruct that in order. What did you observe first, and how did things develop from there? Participant: First was the mild vibration and temperature deviation, day two of the leg. Then it settled, then the system showed clean readings for a good stretch. The filter differential pressure note came in maybe a day and a half after that. Then the temperature spike and vibration event came about ten hours before we were due at the tide window. So there was a real gap—almost three days—between the first hint and the actual failure. Interviewer: Going back to that first deviation—what information did you actually have, and what did you weigh? Participant: I had the raw numbers, both inside the normal band, and I had the fact that this unit had just been fully overhauled. Those two things pulled in different directions a bit—on one hand you could say any deviation after a rebuild deserves a look, but on the other, we'd just paid to have that bearing and the running gear replaced, so a bearing problem three weeks later seemed like a stretch. I remember thinking it made more sense as running-in than as an actual fault. The alternative was to ease off and inspect right there, but with the tide window ahead, and given we'd just sunk real money and yard time into that unit, continuing and monitoring felt like the more reasonable read of the situation. Interviewer: When the system showed everything back in the green band, what led you to skip the manual check? Participant: Mainly that the system readout was clean across the board—no alarms, nothing trending badly. I had the option of pulling a sample; my second engineer wasn't tied up with anything else. But the system existed exactly to tell us this kind of thing, and it was telling me things were fine. Doing a manual check on top of a clean system readout felt like it would've just confirmed what the instruments were already saying. Interviewer: When the fuel filter report came in, how did you decide where to put your attention? Participant: At that moment I was watching the turbocharger closely because of the earlier reading, so that's where my head was. The filter note got acknowledged—I told him we'd track it—but I didn't stop what I was doing to dig into it. There was no fuel or combustion symptom tied to it, so it didn't compete strongly for attention against what I already considered the open item. Interviewer: When the bearing failed with the tide window ten hours out, what options did you consider, and what tipped it? Participant: Two real options: reduce right down and divert to the nearest port for a proper repair, which would've cost us the tide window and probably several days, or jury-rig something at reduced load and make our original berth. We only had a partial bearing kit onboard, not a full replacement. What tipped it, honestly, was that we'd already put so much into this unit—the overhaul cost, the time we'd already spent watching and troubleshooting it—and diverting felt like it would waste all of that on top of the schedule hit. So we went with the jury rig. Interviewer: How much did time pressure factor in across these moments, and how confident were you at each stage? Participant: The tide window was in the back of my mind at every one of these points, more so as we got closer to it. Early on I was fairly confident it was running-in. By the green-band reading I was quite confident there was nothing there. By the fuel filter note I wasn't worried at all—it seemed unrelated. By the failure itself, confidence obviously dropped, but by then options were also narrower. Interviewer: What would have changed your decision at any of these points—what information was missing? Participant: If the system had actually thrown an alarm at that first deviation, or if a manual sample early on had shown metal particulates, I'd have acted immediately. The instruments just never gave me that trigger until the spike itself. Interviewer: Looking back now, how would you characterize that very first vibration reading? Participant: Honestly, looking at it now, it was probably the bearing telling us something from the start—it seems fairly clear in hindsight that that was the early stage of the same failure, not bedding in at all. Interviewer: If the overhaul hadn't just happened, do you think you'd have reacted differently to that first signal? Participant: Probably, yes. Without the overhaul fresh in mind, an elevated reading like that might've gotten a closer look sooner rather than being read as settling-in. Interviewer: And if there'd been no tide window at all—would the decision at the failure point have gone differently? Participant: It's possible. Without that deadline pulling at me, diverting might have felt like a cleaner, more straightforward call rather than one that came with a schedule cost attached. Interviewer: Last one—what would you tell a junior engineer to watch for differently, based on this? Participant: I'd say don't let a recent repair make you assume a component's off the table for new problems, and don't let one system you're watching closely crowd out something else being reported to you, even if it seems minor at the time.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.92s · gen 215.19s · total 219.4s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0276 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0276 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0257 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0254 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0245 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0238 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0226 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0201 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0198 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
11. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0197 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0188 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0187 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
14. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0186 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
15. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0180 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0179 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0178 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0175 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
20. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0169 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
21. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0167 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
22. **Lyell Automation bias and verification complexity.pdf** — 0.0165 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0164 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0163 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
28. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0159 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0154 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
32. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0153 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
33. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0151 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
35. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0150 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
36. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0150 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
37. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
38. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
41. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0146 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0145 (rrf) — _# Results d along with the results. occur during incidents and accidents? in the reports. ssocia_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _## 16 5 Accidents & incidents Observed Expected The results of the chi 5.76 , p = .01 . The resu_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
49. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0142 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
50. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Mechanism-first conservative analysis of a single CTA interview; did not infer bias from hindsight alone, poor outcome, or time pressure without a distinct bias-specific mechanism."
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
      "bias_label": "expectation bias",
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
      "bias_label": "expectation bias",
      "alternative_labels": [
        "prior expectation bias",
        "confirmation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for prior expectations to shape the interpretation of ambiguous information, leading to discounting of evidence inconsistent with those expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of initial turbocharger vibration and EGT deviation after overhaul",
      "decision_point_description": "On day two of the laden leg, elevated EGT and vibration readings occurred shortly after a turbocharger overhaul; the participant interpreted them as running-in and decided to continue monitoring rather than reduce load or inspect.",
      "affected_reasoning_operation": "Diagnostic interpretation of ambiguous engine indications",
      "bias_specific_mechanism": "A recent overhaul was highly salient and made the running-in explanation appear more plausible than an actual bearing fault, so within-band deviations were interpreted as benign.",
      "manifestation_in_interview": "The participant stated the overhaul was front of mind and described reading the first deviation as bedding in, then later acknowledged that without the overhaul fresh in mind the same reading would likely have received closer scrutiny.",
      "effect_on_reasoning_or_decision": "Delayed inspection and manual oil sampling while continuing full operation, missing an early possible warning of the eventual bearing failure.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given we'd literally just had that unit stripped and rebuilt, my first read was that it was probably just bedding in, maybe slightly different clearances after the overhaul.",
          "evidence_explanation": "Shows the recent overhaul directly shaping the initial diagnostic interpretation of ambiguous engine indications."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking it made more sense as running-in than as an actual fault.",
          "evidence_explanation": "Demonstrates that the interpretation was driven by prior expectation rather than direct evidence of a fault."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without the overhaul fresh in mind, an elevated reading like that might've gotten a closer look sooner rather than being read as settling-in.",
          "evidence_explanation": "Confirms that the overhaul-specific expectation changed the diagnostic response."
        }
      ],
      "correction_or_counterevidence": "The readings were still inside the normal band and no alarm triggered, which is a legitimate non-bias reason for not acting more strongly initially.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved aviation corpus identifies expectation bias among cognitive biases implicated in cockpit incidents, but does not provide a detailed mechanism definition.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit: A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation , and in some cases multiple biases",
          "mechanism_supported_by_source": "The source identifies expectation bias as a recognized cognitive bias in operational incidents, supporting its use here.",
          "relevance_to_this_occurrence": "Supports classification of the participant's expectation-mediated interpretation of the post-overhaul engine indications as expectation bias."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "complacency",
        "automation-induced complacency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Reduced monitoring or verification of an automated system because of overreliance on or trust in its reliability.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to skip manual lube oil sampling after system returned to green",
      "decision_point_description": "When the monitoring system showed nominal readings after the earlier deviation, the participant chose not to have the second engineer pull a lube oil sample.",
      "affected_reasoning_operation": "Monitoring and verification behavior",
      "bias_specific_mechanism": "High trust in the clean automated monitoring readout made an additional manual check seem redundant, lowering verification effort despite a prior concern.",
      "manifestation_in_interview": "The participant stated that the system was telling him things were fine and that a manual check would have merely confirmed what the instruments already said.",
      "effect_on_reasoning_or_decision": "Omitted a manual check that could have detected early wear particulates, allowing the bearing problem to develop undetected.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The system was telling me it was fine, and honestly that's what it's there for.",
          "evidence_explanation": "Demonstrates trust in the automated monitoring system as sufficient grounds for accepting the system state."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Doing a manual check on top of a clean system readout felt like it would've just confirmed what the instruments were already saying.",
          "evidence_explanation": "Shows reduced verification behavior because the automated readout was clean."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the system had actually thrown an alarm at that first deviation, or if a manual sample early on had shown metal particulates, I'd have acted immediately.",
          "evidence_explanation": "Indicates that action was contingent on an automated alarm rather than proactive manual verification."
        }
      ],
      "correction_or_counterevidence": "The monitoring system showed nominal readings and no negative trend, so skipping a manual sample had a plausible non-bias operational basis.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved human-automation passage directly supports complacency as reduced verification of automation output.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it.",
          "mechanism_supported_by_source": "Defines complacency as accepting automation output without sufficient verification.",
          "relevance_to_this_occurrence": "The participant accepted a clean automated monitoring readout and skipped manual verification, matching this complacency mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "attentional tunneling",
      "alternative_labels": [
        "cognitive tunneling",
        "tunnel vision",
        "attention bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Narrowing of attention onto one salient item or task at the expense of other relevant signals.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Deferred response to fuel filter differential pressure report",
      "decision_point_description": "After the second engineer reported increased fuel filter differential pressure, the participant acknowledged the report but did not investigate, while continuing to monitor the turbocharger.",
      "affected_reasoning_operation": "Attention allocation and triage of newly reported information",
      "bias_specific_mechanism": "The active monitoring of the turbocharger preoccupied attention, so the newly reported fuel filter indication was not fully evaluated and was deferred despite being a separate potential system issue.",
      "manifestation_in_interview": "The participant described being focused on the turbocharger numbers and stated that the filter note did not compete strongly for attention against the existing open item.",
      "effect_on_reasoning_or_decision": "A potentially relevant new indication was not investigated promptly, illustrating attention being crowded out by the prior concern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I was pretty focused on the turbocharger numbers at that point given the earlier concern, so I told him to keep an eye on it and we'd deal with it later—there was no fuel consumption issue or anything on the combustion side, so it didn't feel urgent next to what I was already watching.",
          "evidence_explanation": "Shows attention narrowing toward the existing turbocharger concern at the expense of a new report."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The filter note got acknowledged—I told him we'd track it—but I didn't stop what I was doing to dig into it.",
          "evidence_explanation": "Demonstrates that the report was recognized but attention was not reallocated to investigate it."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd say don't let a recent repair make you assume a component's off the table for new problems, and don't let one system you're watching closely crowd out something else being reported to you, even if it seems minor at the time.",
          "evidence_explanation": "The participant's own lesson identifies the attentional crowding mechanism."
        }
      ],
      "correction_or_counterevidence": "The fuel filter differential pressure was mild and lacked combustion symptoms, so deferring it may have been ordinary operational triage rather than bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported attentional tunneling; the label and mechanism rely on general knowledge of human factors and cognitive bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-home-itis",
        "plan continuation error",
        "commitment to course of action"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an original plan or course of action even in the face of significant new information suggesting the plan should be reconsidered.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to jury-rig and make original berth after turbocharger bearing failure",
      "decision_point_description": "After the bearing failure occurred about ten hours before a tide-restricted berth, the participant considered diverting versus jury-rigging and chose to continue toward the original berth.",
      "affected_reasoning_operation": "Evaluation of alternative courses of action after a major failure",
      "bias_specific_mechanism": "Sunk costs from the overhaul and prior troubleshooting, plus schedule pressure from the tide window, made diverting feel wasteful and made continuation with a temporary repair seem acceptable.",
      "manifestation_in_interview": "The participant stated that the decision was tipped by the money and time already invested and the schedule hit, and that without the deadline diverting might have felt cleaner.",
      "effect_on_reasoning_or_decision": "Produced continuation with a jury-rigged repair to meet the original port schedule rather than diverting for a proper repair.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We jury-rigged a fix, brought the load down, and pushed on to make berth rather than diverting.",
          "evidence_explanation": "Shows the action of continuing the original plan after the failure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "What tipped it, honestly, was that we'd already put so much into this unit—the overhaul cost, the time we'd already spent watching and troubleshooting it—and diverting felt like it would waste all of that on top of the schedule hit. So we went with the jury rig.",
          "evidence_explanation": "Demonstrates sunk-cost and schedule-pressure mechanisms driving continuation rather than diversion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without that deadline pulling at me, diverting might have felt like a cleaner, more straightforward call rather than one that came with a schedule cost attached.",
          "evidence_explanation": "Supports the role of the deadline in reinforcing the continuation commitment."
        }
      ],
      "correction_or_counterevidence": "The vessel had a partial bearing kit and could reduce load; a jury-rig may have been a legitimate operational option, and the transcript does not state an accident occurred. Time pressure alone is not classified as bias; the participant's stated sunk-cost and plan-continuation reasoning is the bias-specific mechanism.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved aviation source identifies continuation bias in operational incidents, supporting the label.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit: A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "continuation bias, in that it appears to occur in frequently during runway excursions on landing, after longer duties and at the latter stages of flight.",
          "mechanism_supported_by_source": "Identifies continuation bias as a recognized driver of continuing toward the original destination despite emerging problems.",
          "relevance_to_this_occurrence": "Supports labeling the participant's continuation toward the original berth after bearing failure as plan continuation bias."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages for the aviation occurrence were partly garbled and sparse; attentional tunneling lacks direct retrieved corpus support and is based on general human-factors knowledge.",
    "Retrospective hindsight statements were not treated as independent findings or as proof of earlier bias, and contextual factors such as time pressure and operational constraints are noted where they compete with bias explanations."
  ]
}

