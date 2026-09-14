# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process-review purposes, and it's fine to speak candidly about decisions, including ones that didn't pan out the way you expected. Can you start by telling me your role and how you got pulled into the micro-pitting issue on the anodizing line? Participant: Sure. I'm the process engineer responsible for surface treatment qualification on new equipment. I got pulled in when QA flagged intermittent pitting on aluminum brackets coming off the new anodizing line — this was about three weeks before a customer PPAP submission, so there wasn't a lot of slack in the schedule. Interviewer: Walk me through what happened when you were first assigned. Participant: The first thing on my desk that morning was a handoff note from the night-shift operator saying the bath temperature had spiked overnight and he suspected that was causing the pitting. That made immediate sense to me — anodizing bath temperature is a classic culprit for pitting, it's easy to check, and it fit a story I could act on right away. So I started there. I pulled the chiller maintenance history and had our tech verify the temperature controller. There was actually a short rectifier-log summary sitting in the same folder that flagged a calibration deviation from a few days earlier, but I didn't open it that week — the temperature story was already the frame I was working from, so the chiller took priority and the rectifier note just sat there. Interviewer: What was your objective at that point? Participant: Just to stop the bleeding — figure out the root cause fast enough that we could run a clean trial lot and still hit the PPAP window. Interviewer: Let's reconstruct the timeline a bit before we get into specifics. What information did you have on day one versus what came later? Participant: Day one, I had the operator's note, the unopened rectifier summary, and a defect-rate report showing day-shift batches were pitting more than night-shift batches. Coil certs also existed but I hadn't reviewed them. Within about a day we fixed the chiller and temperatures stabilized. But pitting didn't disappear — it dropped, but a low rate persisted. That told me temperature wasn't the whole story. From there we moved into looking at the dosing system, since the residual defect pattern looked more like a chemistry consistency issue. Interviewer: When you saw that day-shift batches had a higher defect rate than night-shift, what was your read on that? Participant: Honestly, my first instinct was that the day-shift operator was less careful — he's newer, and I'd noticed him rushing rack loading a couple times. I flagged it in my notes as a contributing factor. Looking back, I didn't spend much time asking whether the equipment was in worse condition during the day, or whether the chemistry itself might drift over the course of a shift. I focused on him. Interviewer: Did you consider other explanations for that gap? Participant: Not seriously at the time, no. It seemed like a reasonably clean explanation given what I'd observed of him. Interviewer: Let's move to the second decision — selecting a corrective dosing technology. What were you weighing? Participant: Once we knew residual pitting was chemistry-related, we needed a better dosing control system. There were two options. Vendor A had an automated retrofit already running at three of our sister plants. Vendor B had a newer inline sensor-based system with a stronger spec sheet on paper — actually stronger on the sensing and control criteria we cared about most — but only one reference installation, and their documentation was thin, with gaps in the install manual and unclear commissioning steps. Interviewer: How did you decide between them? Participant: I called a couple of engineers at sister plants, and they were generally happy with Vendor A — three plants running it gave me some confidence it was a known quantity. We'd started a requirement-by-requirement comparison of the two systems, and early on it was actually tilting toward Vendor B on the technical side. But once I had three sister plants confirming Vendor A worked, that was enough for me — I didn't finish walking through the rest of the comparison. Vendor B's applications engineer even offered to walk us through the open commissioning questions, and there wasn't any identified incompatibility, but the unresolved gaps still felt less acceptable to me than Vendor A's familiar unknowns, so I didn't take him up on it. Interviewer: Did anything about Vendor A's track record give you pause? Participant: One of the three plants had reported mixed results with it. I knew that going in. But with three plants running it versus one incomplete installation elsewhere, it felt like the safer bet. Interviewer: What happened after installation? Participant: Retrofit went in within three days. First two batches still showed minor pitting, which was a little concerning. Then the next five batches came back completely clean. Interviewer: What was your interpretation of that pattern? Participant: Honestly, after those two rough batches, having five clean ones in a row felt like the process had settled the score — like whatever bad luck or instability had been in the system early on had been used up, so another rough batch felt a lot less likely right then. I remember telling the quality manager the odds of another bad one showing up were pretty low, given the run we'd had. Interviewer: Did you complete the full SPC sample size that's normally recommended before declaring a process stable? Participant: No, we hadn't hit the full sample yet. We started prepping the certification paperwork in parallel because the timeline demanded it, not because I was ready to call the process stable — I was still treating that call as open. The streak affected my gut read more than it should have, but the certification-prep timing itself was really about the calendar. Interviewer: Was there anything else happening during that same window that could have contributed to the improvement? Participant: There was a routine bath chemistry replenishment scheduled in there too. But honestly, I attributed most of the turnaround to the manual rectifier voltage adjustments I was making between runs — small tweaks based on how the previous batch looked. I felt like I was actively steering it back into spec. I never really separated the two effects out. Interviewer: That leads to the final decision — signing off for PPAP. What did that process look like? Participant: We had a full two-week trial dataset with real variability in the earlier lots, and then a final validation lot the day before the deadline that came back completely clean. The customer SQE needed the sign-off memo within 24 hours. Interviewer: How did you weigh the earlier variability against that final lot? Participant: The final lot was really what tipped my confidence. It was the cleanest result we'd seen, run right before submission, so it felt like the truest picture of where the process actually stood. I referenced the earlier trial data in the memo, but the final lot carried most of the weight in my recommendation to certify. Interviewer: Was there any other data available at that point, like the Cpk finding from the independent audit? Participant: There was a marginal Cpk result from a quality audit, yes, but it had been filed separately from the sign-off packet, so it wasn't front and center when I was writing the recommendation. Interviewer: Under less time pressure, would you have handled that differently? Participant: Maybe. I think I would have pulled that Cpk data into the memo directly rather than letting the last lot speak for itself. Interviewer: Let me ask a couple of hypotheticals. If you'd reviewed the rectifier calibration logs before the operator's temperature note, do you think the investigation would have unfolded differently? Participant: Possibly — if the rectifier deviation had been the first thing in front of me, I probably would have chased that first instead of the chiller. It's hard to say which one I'd have found more compelling, but the order I got things in definitely shaped where I looked first. Interviewer: And if that final validation lot had shown pitting instead of coming back clean? Participant: Then I'd have had to delay and either extend the deadline or issue something conditional. It would have forced a harder look at the full dataset rather than leaning on one result. Interviewer: Looking back, is there anything about how you weighed the evidence you'd reconsider? Participant: Probably how much credit I gave myself for the manual adjustments versus the chemistry replenishment — I never really separated those out. And I'd want to revisit that attribution I made about the day-shift operator; I never fully ruled out equipment or process factors there. I'd also go back and actually open that rectifier summary on day one instead of letting the first explanation carry the week. Otherwise, given the time we had, I think the calls were defensible. Interviewer: That's a helpful place to stop. Thanks for walking through this in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.18s · gen 152.90s · total 157.7s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0291 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0268 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0252 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0245 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0222 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0212 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
8. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0207 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
10. **Hallihan_etal_DTM_12.pdf** — 0.0199 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
12. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0192 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
13. **Hallihan_etal_DTM_12.pdf** — 0.0189 (rrf) — _A: I’m thinking that the penguin’s feet really looks like the scrubber, I’m not really sure of t_
14. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0188 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0186 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
16. **Lyell Automation bias and verification complexity.pdf** — 0.0182 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
17. **Hallihan_etal_DTM_12.pdf** — 0.0181 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
18. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0181 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
19. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0180 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0173 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
22. **Hallihan_etal_DTM_12.pdf** — 0.0173 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0173 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
24. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0167 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
27. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
28. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0165 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
29. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0165 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
30. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0163 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0161 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
32. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
33. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
34. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0155 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
35. **Hallihan_etal_DTM_12.pdf** — 0.0153 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
36. **Hallihan_etal_DTM_12.pdf** — 0.0152 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0151 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0151 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
41. **Lyell Automation bias and verification complexity.pdf** — 0.0148 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
42. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0147 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
43. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0147 (rrf) — _# 3Results On this point, Rezazade Mehrizi et al. (2023) investigated how AI explainability tool_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0141 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
48. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0141 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
49. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0141 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
50. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0140 (rrf) — _## 1Introduction RQ3: Can explainability or transparency mitigate automation bias? RQ4: Is AI li_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first evaluation of affirmative evidence in the interview. Retrieved corpus passages were used where they directly supported a specific mechanism; other established labels are noted as not directly supported by the supplied retrieval context."
  },
  "identified_bias_summary": [
    {
      "bias_label": "ambiguity aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "fundamental attribution error",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "gambler's fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "self-serving bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring-and-adjustment heuristic", "confirmation bias", "selective information search"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information as a reference point for subsequent judgment and search, with insufficient adjustment away from that starting point.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial root-cause investigation of anodizing pitting",
      "decision_point_description": "Selecting the initial root-cause hypothesis to pursue under schedule pressure.",
      "affected_reasoning_operation": "Information search and causal hypothesis prioritization",
      "bias_specific_mechanism": "The night-shift operator's temperature note served as an early, plausible anchor. The participant accepted it as the primary frame, prioritized chiller and temperature controller checks, and did not adjust away by opening the accessible rectifier calibration summary that indicated an alternative diagnostic lead.",
      "manifestation_in_interview": "The participant immediately treated the operator's temperature handoff as the explanation and deferred inspection of a contradictory rectifier calibration note, later acknowledging that information order shaped where he looked first.",
      "effect_on_reasoning_or_decision": "Directed early diagnostic effort toward the chiller and temperature controller and delayed consideration of the rectifier calibration deviation for about a week.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The first thing on my desk that morning was a handoff note from the night-shift operator saying the bath temperature had spiked overnight and he suspected that was causing the pitting. That made immediate sense to me — anodizing bath temperature is a classic culprit for pitting, it's easy to check, and it fit a story I could act on right away. So I started there.",
          "evidence_explanation": "Shows the initial temperature note became the anchor and action frame before other available evidence was examined."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was actually a short rectifier-log summary sitting in the same folder that flagged a calibration deviation from a few days earlier, but I didn't open it that week — the temperature story was already the frame I was working from, so the chiller took priority and the rectifier note just sat there.",
          "evidence_explanation": "Demonstrates insufficient adjustment away from the anchor: accessible contradictory or alternative evidence was not sampled."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly — if the rectifier deviation had been the first thing in front of me, I probably would have chased that first instead of the chiller. It's hard to say which one I'd have found more compelling, but the order I got things in definitely shaped where I looked first.",
          "evidence_explanation": "Participant explicitly attributes the direction of the investigation to the order of initial information, consistent with anchoring."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized that temperature was not the whole story after pitting persisted following chiller repair, and stated he would go back and open the rectifier summary on day one. This does not negate the early distortion because the initial framing materially delayed consideration of an alternative diagnostic lead.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Rastogi et al. (2022) passage supports the anchoring-and-adjustment mechanism, specifically that decision-makers anchor to an initial value and may adjust insufficiently.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoring-and-adjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoring-and-adjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports the general anchoring-and-adjustment heuristic: an initial value or prediction can anchor judgment, and adjustment away from it may be insufficient under time constraints.",
          "relevance_to_this_occurrence": "Although the source examines AI predictions, the same mechanism explains how the participant anchored on an initial temperature explanation and failed to sufficiently adjust by inspecting the rectifier evidence."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "fundamental attribution error",
      "alternative_labels": ["correspondence bias", "dispositional attribution bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overattribute another person's behavior or an outcome to their disposition or character while underweighting situational, environmental, or systemic factors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of day-shift versus night-shift defect-rate difference",
      "decision_point_description": null,
      "affected_reasoning_operation": "Causal attribution",
      "bias_specific_mechanism": "When confronted with a higher day-shift defect rate, the participant attributed the pattern primarily to the day-shift operator's carelessness because the operator was newer and had been seen rushing. He did not systematically examine situational alternatives such as equipment condition during the day or shift-related chemistry drift.",
      "manifestation_in_interview": "The participant noted the day-shift operator was less careful in his initial notes and later acknowledged he had focused on the person rather than equipment or process factors.",
      "effect_on_reasoning_or_decision": "Produced a person-centered causal explanation that could have steered remedial action toward operator behavior rather than day-shift equipment or chemistry conditions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first instinct was that the day-shift operator was less careful — he's newer, and I'd noticed him rushing rack loading a couple times. I flagged it in my notes as a contributing factor.",
          "evidence_explanation": "Shows dispositional attribution to the operator based on perceived personal characteristics and observed behavior."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I didn't spend much time asking whether the equipment was in worse condition during the day, or whether the chemistry itself might drift over the course of a shift. I focused on him.",
          "evidence_explanation": "Directly indicates underweighting situational or system-level alternatives while focusing on the individual operator."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd want to revisit that attribution I made about the day-shift operator; I never fully ruled out equipment or process factors there.",
          "evidence_explanation": "Later recognition that situational factors were not adequately considered before forming the attribution."
        }
      ],
      "correction_or_counterevidence": "The participant had observed the day-shift operator rushing rack loading, so the dispositional hypothesis was not baseless. However, he explicitly stated that equipment and chemistry drift explanations were not ruled out, which is the core attributional imbalance.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support was unavailable for fundamental attribution error. The classification relies on established cognitive-science knowledge of social attribution mechanisms.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "ambiguity aversion",
      "alternative_labels": ["ambiguity effect", "uncertainty aversion"],
      "taxonomy_status": "established_label",
      "bias_definition": "A preference for options with known probabilities or familiar risk profiles over options with unknown, ambiguous probabilities, even when the ambiguous option may be stronger on relevant criteria.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of corrective dosing control system",
      "decision_point_description": "Choosing between Vendor A and Vendor B for the dosing-control retrofit.",
      "affected_reasoning_operation": "Option evaluation under uncertainty and evidence search",
      "bias_specific_mechanism": "Vendor B was described as stronger on the technical criteria the team cared about most, but it had only one reference installation and documentation gaps. Vendor A had three sister-plant installations and therefore represented a known risk profile. The participant stopped conducting the full requirement-by-requirement comparison once Vendor A appeared sufficient and framed Vendor A's familiar unknowns as more acceptable than Vendor B's unresolved ambiguities.",
      "manifestation_in_interview": "The participant noted the comparison was initially tilting toward Vendor B on technical grounds, but then selected Vendor A after sister-plant confirmations, without finishing the comparison or taking up Vendor B's offer to resolve open commissioning questions.",
      "effect_on_reasoning_or_decision": "Led to selection of the technically stronger but institutionally familiar Vendor A retrofit, while leaving Vendor B's open commissioning questions unresolved rather than obtaining the missing information.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Vendor B had a newer inline sensor-based system with a stronger spec sheet on paper — actually stronger on the sensing and control criteria we cared about most — but only one reference installation, and their documentation was thin, with gaps in the install manual and unclear commissioning steps.",
          "evidence_explanation": "Establishes that Vendor B was stronger on relevant criteria while having a more ambiguous implementation profile."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Early on it was actually tilting toward Vendor B on the technical side. But once I had three sister plants confirming Vendor A worked, that was enough for me — I didn't finish walking through the rest of the comparison.",
          "evidence_explanation": "Shows premature closure of the evaluation after information that favored the known option, leaving the technical comparison incomplete."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Vendor B's applications engineer even offered to walk us through the open commissioning questions, and there wasn't any identified incompatibility, but the unresolved gaps still felt less acceptable to me than Vendor A's familiar unknowns, so I didn't take him up on it.",
          "evidence_explanation": "Directly expresses the classic ambiguity-aversion tradeoff: known unknowns were preferred over unresolved ambiguity, despite a path to resolve it."
        }
      ],
      "correction_or_counterevidence": "Vendor A had been used at three sister plants and one had reported mixed results, so preference for a proven option under schedule pressure could be a bounded-rational risk-management choice. The occurrence is identified with low confidence because a legitimate professional heuristic is a plausible competing explanation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support was unavailable for ambiguity aversion. The classification relies on established behavioral decision-research knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "gambler's fallacy",
      "alternative_labels": ["Monte Carlo fallacy", "negative recency", "misperception of randomness"],
      "taxonomy_status": "established_label",
      "bias_definition": "The erroneous belief that past deviations from chance in a sequence of independent events make future deviations less likely, as though a run of one outcome uses up a limited supply of the other.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of post-install batch sequence",
      "decision_point_description": null,
      "affected_reasoning_operation": "Probabilistic estimation of future process failures",
      "bias_specific_mechanism": "After two rough batches followed by five clean batches, the participant treated the clean run as evidence that earlier instability had been 'used up,' and therefore estimated that another rough batch was less likely. This is a negative recency inference about independent production events.",
      "manifestation_in_interview": "The participant explicitly told the quality manager that the odds of another bad batch were low because of the clean streak.",
      "effect_on_reasoning_or_decision": "Skewed his informal stability assessment and gut-level risk estimate before the full SPC sample had been collected.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, after those two rough batches, having five clean ones in a row felt like the process had settled the score — like whatever bad luck or instability had been in the system early on had been used up, so another rough batch felt a lot less likely right then.",
          "evidence_explanation": "Directly expresses the gambler's fallacy mechanism: interpreting a clean run as reducing the probability of a future rough batch because the earlier bad luck was 'used up.'"
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember telling the quality manager the odds of another bad one showing up were pretty low, given the run we'd had.",
          "evidence_explanation": "Shows the biased probability estimate was communicated as a risk judgment to another decision-relevant actor."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that the streak affected his gut read more than it should have, though he distinguished this from the parallel timeline-driven decision to begin certification preparation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support was unavailable for gambler's fallacy. The classification relies on established cognitive-science knowledge of probability and randomness misconceptions.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "self-serving bias",
      "alternative_labels": ["self-serving attributional bias", "self-enhancement bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The motivational tendency to attribute positive outcomes to one's own actions or dispositions while attributing negative outcomes to external factors or bad luck.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Causal attribution of process improvement",
      "decision_point_description": null,
      "affected_reasoning_operation": "Causal attribution of process improvement",
      "bias_specific_mechanism": "When the pitting improved, the participant attributed most of the turnaround to his own manual rectifier voltage adjustments, even though a routine bath chemistry replenishment occurred in the same window and the two influences were never separated.",
      "manifestation_in_interview": "He described feeling as if he was actively steering the process back into spec and only later questioned whether he had over-credited his own adjustments.",
      "effect_on_reasoning_or_decision": "Produced an inflated causal account of personal control that may have influenced what actions were seen as responsible for the improved outcome.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a routine bath chemistry replenishment scheduled in there too. But honestly, I attributed most of the turnaround to the manual rectifier voltage adjustments I was making between runs — small tweaks based on how the previous batch looked. I felt like I was actively steering it back into spec. I never really separated the two effects out.",
          "evidence_explanation": "Shows disproportionate credit given to personal action while a plausible external cause was not separated out."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably how much credit I gave myself for the manual adjustments versus the chemistry replenishment — I never really separated those out.",
          "evidence_explanation": "Later acknowledgment confirms the causal attribution was not analytically grounded but influenced by self-credit."
        }
      ],
      "correction_or_counterevidence": "Manual rectifier adjustments could genuinely have contributed to the improvement; the bias concerns the imbalance in causal attribution and failure to separate the two causes, not a proven false belief.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support was unavailable for self-serving bias. The classification relies on established cognitive-science knowledge of motivated attribution.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "recency effect",
      "alternative_labels": ["recency bias", "availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for recent events to be remembered or weighted more heavily than earlier information when forming judgments or decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final PPAP certification recommendation",
      "decision_point_description": "Whether to recommend certification/PPAP sign-off given the trial and validation data.",
      "affected_reasoning_operation": "Evidence weighting and stability evaluation",
      "bias_specific_mechanism": "The participant weighted the final clean validation lot as the 'truest picture' of process stability and allowed it to carry most of the recommendation weight, while earlier trial variability and a separately filed marginal Cpk finding were not similarly integrated.",
      "manifestation_in_interview": "The final validation lot dominated his confidence for PPAP sign-off, and he acknowledged that under less time pressure he would have pulled the marginal Cpk data into the memo.",
      "effect_on_reasoning_or_decision": "Led to a certification recommendation that overrepresented the most recent clean lot and underweighted earlier variability and an independent marginal Cpk result.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The final lot was really what tipped my confidence. It was the cleanest result we'd seen, run right before submission, so it felt like the truest picture of where the process actually stood. I referenced the earlier trial data in the memo, but the final lot carried most of the weight in my recommendation to certify.",
          "evidence_explanation": "Directly shows recent-event overweighting in the certification decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a marginal Cpk result from a quality audit, yes, but it had been filed separately from the sign-off packet, so it wasn't front and center when I was writing the recommendation.",
          "evidence_explanation": "Shows that less recent, less salient but relevant evidence was not integrated into the recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Maybe. I think I would have pulled that Cpk data into the memo directly rather than letting the last lot speak for itself.",
          "evidence_explanation": "The participant's counterfactual confirms that the final lot was allowed to dominate the judgment more than the full dataset warranted."
        }
      ],
      "correction_or_counterevidence": "There was genuine time pressure to meet the customer deadline, and the final validation lot was a relevant, current result. However, the participant explicitly states the last lot spoke for itself and that he would have integrated the Cpk data under less pressure, supporting a recency-driven weighting distortion.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Natesan et al. (2016) passage directly defines recency effect as a tendency to remember recent events more clearly, supporting the mechanism of disproportionate recent-information salience.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": "Natesan et al.",
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "The source supports the recency effect as a cognitive tendency involving heightened clarity or salience of recent events, which can distort the weighting of evidence.",
          "relevance_to_this_occurrence": "The participant's overweighting of the final validation lot is consistent with the recency effect defined in the retrieved source."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on a single retrospective self-report; participant memory and self-presentation may affect the evidence.",
    "Retrieved corpus passages provided direct support for only anchoring and recency; other classifications rely on established cognitive-science knowledge.",
    "Some low-confidence findings have plausible non-bias explanations, as documented in correction_or_counterevidence."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process-review purposes, and it's fine to speak candidly about decisions, including ones that didn't pan out the way you expected. Can you start by telling me your role and how you got pulled into the micro-pitting issue on the anodizing line? Participant: Sure. I'm the process engineer responsible for surface treatment qualification on new equipment. I got pulled in when QA flagged intermittent pitting on aluminum brackets coming off the new anodizing line — this was about three weeks before a customer PPAP submission, so there wasn't a lot of slack in the schedule. Interviewer: Walk me through what happened when you were first assigned. Participant: The first thing on my desk that morning was a handoff note from the night-shift operator saying the bath temperature had spiked overnight and he suspected that was causing the pitting. That made immediate sense to me — anodizing bath temperature is a classic culprit for pitting, it's easy to check, and it fit a story I could act on right away. So I started there. I pulled the chiller maintenance history and had our tech verify the temperature controller. There was actually a short rectifier-log summary sitting in the same folder that flagged a calibration deviation from a few days earlier, but I didn't open it that week — the temperature story was already the frame I was working from, so the chiller took priority and the rectifier note just sat there. Interviewer: What was your objective at that point? Participant: Just to stop the bleeding — figure out the root cause fast enough that we could run a clean trial lot and still hit the PPAP window. Interviewer: Let's reconstruct the timeline a bit before we get into specifics. What information did you have on day one versus what came later? Participant: Day one, I had the operator's note, the unopened rectifier summary, and a defect-rate report showing day-shift batches were pitting more than night-shift batches. Coil certs also existed but I hadn't reviewed them. Within about a day we fixed the chiller and temperatures stabilized. But pitting didn't disappear — it dropped, but a low rate persisted. That told me temperature wasn't the whole story. From there we moved into looking at the dosing system, since the residual defect pattern looked more like a chemistry consistency issue. Interviewer: When you saw that day-shift batches had a higher defect rate than night-shift, what was your read on that? Participant: Honestly, my first instinct was that the day-shift operator was less careful — he's newer, and I'd noticed him rushing rack loading a couple times. I flagged it in my notes as a contributing factor. Looking back, I didn't spend much time asking whether the equipment was in worse condition during the day, or whether the chemistry itself might drift over the course of a shift. I focused on him. Interviewer: Did you consider other explanations for that gap? Participant: Not seriously at the time, no. It seemed like a reasonably clean explanation given what I'd observed of him. Interviewer: Let's move to the second decision — selecting a corrective dosing technology. What were you weighing? Participant: Once we knew residual pitting was chemistry-related, we needed a better dosing control system. There were two options. Vendor A had an automated retrofit already running at three of our sister plants. Vendor B had a newer inline sensor-based system with a stronger spec sheet on paper — actually stronger on the sensing and control criteria we cared about most — but only one reference installation, and their documentation was thin, with gaps in the install manual and unclear commissioning steps. Interviewer: How did you decide between them? Participant: I called a couple of engineers at sister plants, and they were generally happy with Vendor A — three plants running it gave me some confidence it was a known quantity. We'd started a requirement-by-requirement comparison of the two systems, and early on it was actually tilting toward Vendor B on the technical side. But once I had three sister plants confirming Vendor A worked, that was enough for me — I didn't finish walking through the rest of the comparison. Vendor B's applications engineer even offered to walk us through the open commissioning questions, and there wasn't any identified incompatibility, but the unresolved gaps still felt less acceptable to me than Vendor A's familiar unknowns, so I didn't take him up on it. Interviewer: Did anything about Vendor A's track record give you pause? Participant: One of the three plants had reported mixed results with it. I knew that going in. But with three plants running it versus one incomplete installation elsewhere, it felt like the safer bet. Interviewer: What happened after installation? Participant: Retrofit went in within three days. First two batches still showed minor pitting, which was a little concerning. Then the next five batches came back completely clean. Interviewer: What was your interpretation of that pattern? Participant: Honestly, after those two rough batches, having five clean ones in a row felt like the process had settled the score — like whatever bad luck or instability had been in the system early on had been used up, so another rough batch felt a lot less likely right then. I remember telling the quality manager the odds of another bad one showing up were pretty low, given the run we'd had. Interviewer: Did you complete the full SPC sample size that's normally recommended before declaring a process stable? Participant: No, we hadn't hit the full sample yet. We started prepping the certification paperwork in parallel because the timeline demanded it, not because I was ready to call the process stable — I was still treating that call as open. The streak affected my gut read more than it should have, but the certification-prep timing itself was really about the calendar. Interviewer: Was there anything else happening during that same window that could have contributed to the improvement? Participant: There was a routine bath chemistry replenishment scheduled in there too. But honestly, I attributed most of the turnaround to the manual rectifier voltage adjustments I was making between runs — small tweaks based on how the previous batch looked. I felt like I was actively steering it back into spec. I never really separated the two effects out. Interviewer: That leads to the final decision — signing off for PPAP. What did that process look like? Participant: We had a full two-week trial dataset with real variability in the earlier lots, and then a final validation lot the day before the deadline that came back completely clean. The customer SQE needed the sign-off memo within 24 hours. Interviewer: How did you weigh the earlier variability against that final lot? Participant: The final lot was really what tipped my confidence. It was the cleanest result we'd seen, run right before submission, so it felt like the truest picture of where the process actually stood. I referenced the earlier trial data in the memo, but the final lot carried most of the weight in my recommendation to certify. Interviewer: Was there any other data available at that point, like the Cpk finding from the independent audit? Participant: There was a marginal Cpk result from a quality audit, yes, but it had been filed separately from the sign-off packet, so it wasn't front and center when I was writing the recommendation. Interviewer: Under less time pressure, would you have handled that differently? Participant: Maybe. I think I would have pulled that Cpk data into the memo directly rather than letting the last lot speak for itself. Interviewer: Let me ask a couple of hypotheticals. If you'd reviewed the rectifier calibration logs before the operator's temperature note, do you think the investigation would have unfolded differently? Participant: Possibly — if the rectifier deviation had been the first thing in front of me, I probably would have chased that first instead of the chiller. It's hard to say which one I'd have found more compelling, but the order I got things in definitely shaped where I looked first. Interviewer: And if that final validation lot had shown pitting instead of coming back clean? Participant: Then I'd have had to delay and either extend the deadline or issue something conditional. It would have forced a harder look at the full dataset rather than leaning on one result. Interviewer: Looking back, is there anything about how you weighed the evidence you'd reconsider? Participant: Probably how much credit I gave myself for the manual adjustments versus the chemistry replenishment — I never really separated those out. And I'd want to revisit that attribution I made about the day-shift operator; I never fully ruled out equipment or process factors there. I'd also go back and actually open that rectifier summary on day one instead of letting the first explanation carry the week. Otherwise, given the time we had, I think the calls were defensible. Interviewer: That's a helpful place to stop. Thanks for walking through this in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.21s · gen 140.65s · total 145.3s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0291 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0268 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0252 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0245 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0222 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0212 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
8. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0207 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
10. **Hallihan_etal_DTM_12.pdf** — 0.0199 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
12. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0192 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
13. **Hallihan_etal_DTM_12.pdf** — 0.0189 (rrf) — _A: I’m thinking that the penguin’s feet really looks like the scrubber, I’m not really sure of t_
14. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0188 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0186 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
16. **Lyell Automation bias and verification complexity.pdf** — 0.0182 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
17. **Hallihan_etal_DTM_12.pdf** — 0.0181 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
18. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0181 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
19. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0180 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0173 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
22. **Hallihan_etal_DTM_12.pdf** — 0.0173 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0173 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
24. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0167 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
27. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
28. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0165 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
29. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0165 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
30. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0163 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0161 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
32. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
33. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
34. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0155 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
35. **Hallihan_etal_DTM_12.pdf** — 0.0153 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
36. **Hallihan_etal_DTM_12.pdf** — 0.0152 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0151 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0151 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
41. **Lyell Automation bias and verification complexity.pdf** — 0.0148 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
42. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0147 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
43. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0147 (rrf) — _# 3Results On this point, Rezazade Mehrizi et al. (2023) investigated how AI explainability tool_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0141 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
48. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0141 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
49. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0141 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
50. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0140 (rrf) — _## 1Introduction RQ3: Can explainability or transparency mitigate automation bias? RQ4: Is AI li_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of the participant's described reasoning in a single process-review interview. Only occurrences with affirmative evidence of a bias-specific mechanism were classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "ambiguity aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "fundamental attribution error",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "gambler's fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "self-serving bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "primacy bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to rely heavily on an initial piece of information and to adjust insufficiently from that anchor in subsequent judgment and search.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial root-cause hypothesis selection for pitting",
      "decision_point_description": "Choosing which root-cause hypothesis to pursue first after receiving the handoff note",
      "affected_reasoning_operation": "Hypothesis generation and initial information-search prioritization",
      "bias_specific_mechanism": "The first information encountered, an operator note about a temperature spike, served as an anchor; subsequent investigation stayed anchored to the temperature/chiller path and did not sufficiently adjust toward the alternative rectifier deviation.",
      "manifestation_in_interview": "The participant immediately accepted the night-shift operator's temperature hypothesis, started with chiller maintenance and temperature controller verification, and left the rectifier-log summary unopened that week.",
      "effect_on_reasoning_or_decision": "The investigation initially pursued the temperature/chiller path, delaying consideration of the rectifier calibration deviation and potentially delaying identification of the true root cause.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The first thing on my desk that morning was a handoff note from the night-shift operator saying the bath temperature had spiked overnight and he suspected that was causing the pitting. That made immediate sense to me — anodizing bath temperature is a classic culprit for pitting, it's easy to check, and it fit a story I could act on right away. So I started there.",
          "evidence_explanation": "Shows that the first available explanation quickly became the anchor for the root-cause investigation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly — if the rectifier deviation had been the first thing in front of me, I probably would have chased that first instead of the chiller. It's hard to say which one I'd have found more compelling, but the order I got things in definitely shaped where I looked first.",
          "evidence_explanation": "The participant explicitly recognizes that the order of initial information shaped his investigation direction, consistent with anchoring."
        }
      ],
      "correction_or_counterevidence": "Later, when pitting persisted after chiller repair, the participant broadened the investigation to dosing and chemistry; at the end he also says he would go back and open the rectifier summary on day one.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Corpus support for anchoring was available from Rastogi et al. 2022.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoring-and-adjustment. ... participants' likelihood of sufficiently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoring-and-adjustment heuristic is a resource-rational tradeoff between time and accuracy.",
          "mechanism_supported_by_source": "Describes the anchoring-and-adjustment heuristic: people adjust insufficiently from an initial anchor, with adjustment increasing as time or resources increase.",
          "relevance_to_this_occurrence": "Supports the mechanism by which the initial temperature note anchored the participant's root-cause search and limited adjustment to the alternative rectifier signal."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "myside bias",
        "selective exposure"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in ways that confirm existing beliefs or hypotheses and to ignore or discount contradictory information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-one information sampling during temperature hypothesis",
      "decision_point_description": "Deciding which technical documents and systems to inspect first",
      "affected_reasoning_operation": "Selective information search and prioritization",
      "bias_specific_mechanism": "After forming the temperature hypothesis, the participant preferentially directed attention to temperature-supporting information, such as chiller maintenance and the temperature controller, and did not open a contradicting rectifier-calibration summary, consistent with confirmation-driven selective exposure.",
      "manifestation_in_interview": "The participant reports that the rectifier log was sitting in the same folder but remained unopened because the temperature story was already the frame; the chiller took priority.",
      "effect_on_reasoning_or_decision": "Reduced the chance of disconfirming the temperature hypothesis and likely delayed identification of the rectifier issue.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was actually a short rectifier-log summary sitting in the same folder that flagged a calibration deviation from a few days earlier, but I didn't open it that week — the temperature story was already the frame I was working from, so the chiller took priority and the rectifier note just sat there.",
          "evidence_explanation": "The existing frame led to ignoring a directly relevant contradictory document while temperature-consistent avenues were pursued."
        }
      ],
      "correction_or_counterevidence": "The participant later says he would go back and open the rectifier summary on day one; the persistence of pitting also eventually forced broader investigation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Corpus support discusses confirmation bias as biased processing of sampled information and discounting of contradictory information.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "In addition, an explanation in terms of confirmation bias in processing the sampled information or difficulties of comprehension is also unlikely ... Thus, the two types of decision bias discussed previously, confirmation bias and discounting bias, can be ruled out as explanations, at least for this group.",
          "mechanism_supported_by_source": "The passage explicitly links confirmation bias to biased processing of sampled information and discounting of contradictory information.",
          "relevance_to_this_occurrence": "Supports labeling the participant's selective prioritization of the chiller path and non-opening of the contradictory rectifier summary as confirmation bias."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "fundamental attribution error",
      "alternative_labels": [
        "correspondence bias",
        "attribution bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to overattribute a person's outcomes to dispositional traits while underweighting situational or systemic factors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting day-shift versus night-shift pitting-rate gap",
      "decision_point_description": "Attributing the cause of the shift-wise defect-rate difference",
      "affected_reasoning_operation": "Causal attribution",
      "bias_specific_mechanism": "The participant inferred that the day-shift operator's carelessness was the cause of the higher day-shift defect rate from dispositional impressions, including that the operator was newer and had been seen rushing, while explicitly not considering equipment or chemistry drift.",
      "manifestation_in_interview": "The participant flagged the day-shift operator as a contributing factor and did not seriously consider equipment or process explanations at the time.",
      "effect_on_reasoning_or_decision": "Potentially misdirected attention toward individual operator behavior and away from systematic process or equipment factors.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first instinct was that the day-shift operator was less careful — he's newer, and I'd noticed him rushing rack loading a couple times. I flagged it in my notes as a contributing factor. Looking back, I didn't spend much time asking whether the equipment was in worse condition during the day, or whether the chemistry itself might drift over the course of a shift. I focused on him.",
          "evidence_explanation": "Shows a dispositional attribution to the operator and explicit neglect of situational or process explanations."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not seriously at the time, no. It seemed like a reasonably clean explanation given what I'd observed of him.",
          "evidence_explanation": "Confirms that alternative explanations were not seriously considered at the time."
        }
      ],
      "correction_or_counterevidence": "Looking back, the participant says he would revisit the attribution and never fully ruled out equipment or process factors.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label is from widely established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "ambiguity aversion",
      "alternative_labels": [
        "status quo bias",
        "familiarity bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to prefer known options with clearer risk profiles over ambiguous options, even when the ambiguous option is stronger on explicit criteria.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection between Vendor A and Vendor B dosing control system",
      "decision_point_description": "Choosing which corrective dosing technology to purchase",
      "affected_reasoning_operation": "Preference construction under uncertainty and familiarity",
      "bias_specific_mechanism": "The unresolved documentation and commissioning gaps for Vendor B were subjectively less acceptable than Vendor A's known limitations; the participant declined an opportunity to resolve those gaps and stopped comparison after confirmatory reports from sister plants.",
      "manifestation_in_interview": "Despite Vendor B being stronger on technical criteria, the participant chose Vendor A because three sister plants were running it and Vendor B's unresolved gaps felt less acceptable than Vendor A's familiar unknowns.",
      "effect_on_reasoning_or_decision": "The choice favored the familiar option and foreclosed further evaluation of potentially superior Vendor B, including an offered walkthrough of the open commissioning questions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Vendor B had a newer inline sensor-based system with a stronger spec sheet on paper — actually stronger on the sensing and control criteria we cared about most — but only one reference installation, and their documentation was thin, with gaps in the install manual and unclear commissioning steps.",
          "evidence_explanation": "Establishes that Vendor B was technically stronger but more ambiguous."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But once I had three sister plants confirming Vendor A worked, that was enough for me — I didn't finish walking through the rest of the comparison. Vendor B's applications engineer even offered to walk us through the open commissioning questions, and there wasn't any identified incompatibility, but the unresolved gaps still felt less acceptable to me than Vendor A's familiar unknowns, so I didn't take him up on it.",
          "evidence_explanation": "Shows preference for the known option and avoidance of ambiguity, including declining an opportunity to reduce the uncertainty about Vendor B."
        }
      ],
      "correction_or_counterevidence": "The participant knew one of the three sister plants had reported mixed results with Vendor A, yet still treated Vendor A as safer; time pressure and a need for a known retrofit are plausible non-bias explanations.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label is from widely established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "gambler's fallacy",
      "alternative_labels": [
        "Monte Carlo fallacy",
        "negative recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to believe that past independent outcomes change the probability of future outcomes, such as believing a streak of good results makes a subsequent bad result less likely.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting five consecutive clean batches after two rough batches",
      "decision_point_description": "Estimating the probability of another rough batch after a run of clean results",
      "affected_reasoning_operation": "Probability judgment and short-term process-stability inference",
      "bias_specific_mechanism": "The participant interpreted five clean batches as though early bad luck or instability had been used up, making another rough batch feel less likely in the near term.",
      "manifestation_in_interview": "The participant reported telling the quality manager that the odds of another bad batch were low because of the recent clean run, despite not having completed the full SPC sample.",
      "effect_on_reasoning_or_decision": "Inflated confidence in near-term process stability and contributed to a gut read that another bad batch was unlikely.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, after those two rough batches, having five clean ones in a row felt like the process had settled the score — like whatever bad luck or instability had been in the system early on had been used up, so another rough batch felt a lot less likely right then. I remember telling the quality manager the odds of another bad one showing up were pretty low, given the run we'd had.",
          "evidence_explanation": "Explicitly articulates the gambler's fallacy mechanism: recent successes being treated as lowering the probability of a future failure."
        }
      ],
      "correction_or_counterevidence": "The participant clarified that he was still treating the process-stability call as open and that the streak affected his gut read more than it should have.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label is from widely established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "self-serving bias",
      "alternative_labels": [
        "self-serving attribution",
        "illusory control"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to attribute positive outcomes to one's own actions while underweighting or failing to separate external or situational causes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Attributing the pitting improvement to manual voltage adjustments versus chemistry replenishment",
      "decision_point_description": "Causal attribution of the observed turnaround in batch quality",
      "affected_reasoning_operation": "Causal attribution",
      "bias_specific_mechanism": "The participant credited the improvement primarily to his own manual rectifier voltage adjustments and did not separate this from a scheduled bath chemistry replenishment, despite the two effects being confounded.",
      "manifestation_in_interview": "The participant reported feeling he was actively steering the process back into spec and never separated the manual-adjustment effect from the replenishment effect.",
      "effect_on_reasoning_or_decision": "Created an overly self-attributed causal account of the improvement and potentially misleading learning about which corrective action was effective.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a routine bath chemistry replenishment scheduled in there too. But honestly, I attributed most of the turnaround to the manual rectifier voltage adjustments I was making between runs — small tweaks based on how the previous batch looked. I felt like I was actively steering it back into spec. I never really separated the two effects out.",
          "evidence_explanation": "Shows self-attribution of the positive outcome and failure to separate an external confounded cause."
        }
      ],
      "correction_or_counterevidence": "Later he says he would probably reconsider how much credit he gave himself for the manual adjustments versus the chemistry replenishment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label is from widely established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_007",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "recency effect",
      "alternative_labels": [
        "recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to give disproportionate weight to the most recent information or events when forming judgments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final PPAP sign-off recommendation",
      "decision_point_description": "Weighing earlier trial variability versus the final validation lot before recommending certification",
      "affected_reasoning_operation": "Evidence weighting and confidence judgment",
      "bias_specific_mechanism": "The most recent validation lot, which was clean and close in time, was treated as the truest picture of process performance; earlier variability and a separately filed marginal Cpk result were underweighted.",
      "manifestation_in_interview": "The participant stated that the final lot carried most of the weight in the recommendation, even though a full two-week trial dataset with earlier variability existed and a marginal Cpk finding was available.",
      "effect_on_reasoning_or_decision": "The PPAP certification recommendation relied heavily on the final lot rather than integrating the full evidence base.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The final lot was really what tipped my confidence. It was the cleanest result we'd seen, run right before submission, so it felt like the truest picture of where the process actually stood. I referenced the earlier trial data in the memo, but the final lot carried most of the weight in my recommendation to certify.",
          "evidence_explanation": "Shows the recent clean lot dominating confidence and recommendation weight."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a marginal Cpk result from a quality audit, yes, but it had been filed separately from the sign-off packet, so it wasn't front and center when I was writing the recommendation.",
          "evidence_explanation": "Indicates that a non-recent, potentially disconfirming result was not integrated into the decision-making process."
        }
      ],
      "correction_or_counterevidence": "The participant did reference earlier trial data in the memo and acknowledged that under less time pressure he would have pulled the Cpk data into the memo directly.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Corpus support for the recency effect was available from Natesan et al. 2016.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": "Natesan et al.",
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly. For example, as participants use a device, they become more familiar the ...",
          "mechanism_supported_by_source": "Describes the recency effect as a tendency for recent events to be more available and influential.",
          "relevance_to_this_occurrence": "Supports the mechanism by which the final clean validation lot was more available and weighted more heavily than earlier data."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on retrospective self-report, so at-the-time reasoning may be partially reconstructed.",
    "Several labels (fundamental attribution error, ambiguity aversion, gambler's fallacy, self-serving bias) lack direct support in the retrieved corpus passages and are drawn from general cognitive-science knowledge.",
    "Time pressure and real-world operational constraints are present and may provide non-bias explanations for some choices; these were treated as counterevidence where relevant.",
    "No experimental benchmark or normative model is available for these specific process decisions."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process-review purposes, and it's fine to speak candidly about decisions, including ones that didn't pan out the way you expected. Can you start by telling me your role and how you got pulled into the micro-pitting issue on the anodizing line? Participant: Sure. I'm the process engineer responsible for surface treatment qualification on new equipment. I got pulled in when QA flagged intermittent pitting on aluminum brackets coming off the new anodizing line — this was about three weeks before a customer PPAP submission, so there wasn't a lot of slack in the schedule. Interviewer: Walk me through what happened when you were first assigned. Participant: The first thing on my desk that morning was a handoff note from the night-shift operator saying the bath temperature had spiked overnight and he suspected that was causing the pitting. That made immediate sense to me — anodizing bath temperature is a classic culprit for pitting, it's easy to check, and it fit a story I could act on right away. So I started there. I pulled the chiller maintenance history and had our tech verify the temperature controller. There was actually a short rectifier-log summary sitting in the same folder that flagged a calibration deviation from a few days earlier, but I didn't open it that week — the temperature story was already the frame I was working from, so the chiller took priority and the rectifier note just sat there. Interviewer: What was your objective at that point? Participant: Just to stop the bleeding — figure out the root cause fast enough that we could run a clean trial lot and still hit the PPAP window. Interviewer: Let's reconstruct the timeline a bit before we get into specifics. What information did you have on day one versus what came later? Participant: Day one, I had the operator's note, the unopened rectifier summary, and a defect-rate report showing day-shift batches were pitting more than night-shift batches. Coil certs also existed but I hadn't reviewed them. Within about a day we fixed the chiller and temperatures stabilized. But pitting didn't disappear — it dropped, but a low rate persisted. That told me temperature wasn't the whole story. From there we moved into looking at the dosing system, since the residual defect pattern looked more like a chemistry consistency issue. Interviewer: When you saw that day-shift batches had a higher defect rate than night-shift, what was your read on that? Participant: Honestly, my first instinct was that the day-shift operator was less careful — he's newer, and I'd noticed him rushing rack loading a couple times. I flagged it in my notes as a contributing factor. Looking back, I didn't spend much time asking whether the equipment was in worse condition during the day, or whether the chemistry itself might drift over the course of a shift. I focused on him. Interviewer: Did you consider other explanations for that gap? Participant: Not seriously at the time, no. It seemed like a reasonably clean explanation given what I'd observed of him. Interviewer: Let's move to the second decision — selecting a corrective dosing technology. What were you weighing? Participant: Once we knew residual pitting was chemistry-related, we needed a better dosing control system. There were two options. Vendor A had an automated retrofit already running at three of our sister plants. Vendor B had a newer inline sensor-based system with a stronger spec sheet on paper — actually stronger on the sensing and control criteria we cared about most — but only one reference installation, and their documentation was thin, with gaps in the install manual and unclear commissioning steps. Interviewer: How did you decide between them? Participant: I called a couple of engineers at sister plants, and they were generally happy with Vendor A — three plants running it gave me some confidence it was a known quantity. We'd started a requirement-by-requirement comparison of the two systems, and early on it was actually tilting toward Vendor B on the technical side. But once I had three sister plants confirming Vendor A worked, that was enough for me — I didn't finish walking through the rest of the comparison. Vendor B's applications engineer even offered to walk us through the open commissioning questions, and there wasn't any identified incompatibility, but the unresolved gaps still felt less acceptable to me than Vendor A's familiar unknowns, so I didn't take him up on it. Interviewer: Did anything about Vendor A's track record give you pause? Participant: One of the three plants had reported mixed results with it. I knew that going in. But with three plants running it versus one incomplete installation elsewhere, it felt like the safer bet. Interviewer: What happened after installation? Participant: Retrofit went in within three days. First two batches still showed minor pitting, which was a little concerning. Then the next five batches came back completely clean. Interviewer: What was your interpretation of that pattern? Participant: Honestly, after those two rough batches, having five clean ones in a row felt like the process had settled the score — like whatever bad luck or instability had been in the system early on had been used up, so another rough batch felt a lot less likely right then. I remember telling the quality manager the odds of another bad one showing up were pretty low, given the run we'd had. Interviewer: Did you complete the full SPC sample size that's normally recommended before declaring a process stable? Participant: No, we hadn't hit the full sample yet. We started prepping the certification paperwork in parallel because the timeline demanded it, not because I was ready to call the process stable — I was still treating that call as open. The streak affected my gut read more than it should have, but the certification-prep timing itself was really about the calendar. Interviewer: Was there anything else happening during that same window that could have contributed to the improvement? Participant: There was a routine bath chemistry replenishment scheduled in there too. But honestly, I attributed most of the turnaround to the manual rectifier voltage adjustments I was making between runs — small tweaks based on how the previous batch looked. I felt like I was actively steering it back into spec. I never really separated the two effects out. Interviewer: That leads to the final decision — signing off for PPAP. What did that process look like? Participant: We had a full two-week trial dataset with real variability in the earlier lots, and then a final validation lot the day before the deadline that came back completely clean. The customer SQE needed the sign-off memo within 24 hours. Interviewer: How did you weigh the earlier variability against that final lot? Participant: The final lot was really what tipped my confidence. It was the cleanest result we'd seen, run right before submission, so it felt like the truest picture of where the process actually stood. I referenced the earlier trial data in the memo, but the final lot carried most of the weight in my recommendation to certify. Interviewer: Was there any other data available at that point, like the Cpk finding from the independent audit? Participant: There was a marginal Cpk result from a quality audit, yes, but it had been filed separately from the sign-off packet, so it wasn't front and center when I was writing the recommendation. Interviewer: Under less time pressure, would you have handled that differently? Participant: Maybe. I think I would have pulled that Cpk data into the memo directly rather than letting the last lot speak for itself. Interviewer: Let me ask a couple of hypotheticals. If you'd reviewed the rectifier calibration logs before the operator's temperature note, do you think the investigation would have unfolded differently? Participant: Possibly — if the rectifier deviation had been the first thing in front of me, I probably would have chased that first instead of the chiller. It's hard to say which one I'd have found more compelling, but the order I got things in definitely shaped where I looked first. Interviewer: And if that final validation lot had shown pitting instead of coming back clean? Participant: Then I'd have had to delay and either extend the deadline or issue something conditional. It would have forced a harder look at the full dataset rather than leaning on one result. Interviewer: Looking back, is there anything about how you weighed the evidence you'd reconsider? Participant: Probably how much credit I gave myself for the manual adjustments versus the chemistry replenishment — I never really separated those out. And I'd want to revisit that attribution I made about the day-shift operator; I never fully ruled out equipment or process factors there. I'd also go back and actually open that rectifier summary on day one instead of letting the first explanation carry the week. Otherwise, given the time we had, I think the calls were defensible. Interviewer: That's a helpful place to stop. Thanks for walking through this in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.16s · gen 183.17s · total 187.8s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0291 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0268 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0252 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0245 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0222 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0212 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
8. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0207 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
10. **Hallihan_etal_DTM_12.pdf** — 0.0199 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
12. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0192 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
13. **Hallihan_etal_DTM_12.pdf** — 0.0189 (rrf) — _A: I’m thinking that the penguin’s feet really looks like the scrubber, I’m not really sure of t_
14. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0188 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0186 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
16. **Lyell Automation bias and verification complexity.pdf** — 0.0182 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
17. **Hallihan_etal_DTM_12.pdf** — 0.0181 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
18. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0181 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
19. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0180 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0173 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
22. **Hallihan_etal_DTM_12.pdf** — 0.0173 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0173 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
24. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0167 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
27. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
28. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0165 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
29. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0165 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
30. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0163 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0161 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
32. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
33. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
34. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0155 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
35. **Hallihan_etal_DTM_12.pdf** — 0.0153 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
36. **Hallihan_etal_DTM_12.pdf** — 0.0152 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0151 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0151 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
41. **Lyell Automation bias and verification complexity.pdf** — 0.0148 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
42. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0147 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
43. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0147 (rrf) — _# 3Results On this point, Rezazade Mehrizi et al. (2023) investigated how AI explainability tool_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0141 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
48. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0141 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
49. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0141 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
50. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0140 (rrf) — _## 1Introduction RQ3: Can explainability or transparency mitigate automation bias? RQ4: Is AI li_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focused on the process engineer's reasoning episodes in the CTA interview. Structural constraints such as time pressure and legitimate professional heuristics were not classified as bias unless a distinct bias-specific cognitive mechanism was affirmatively evidenced in the transcript."
  },
  "identified_bias_summary": [
    {
      "bias_label": "ambiguity aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "fundamental attribution error",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "gambler's fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "illusion of control",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to rely too heavily on an initial piece of information when forming judgments or deciding where to focus, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial root-cause hypothesis after night-shift handoff",
      "decision_point_description": "Choosing to begin the investigation with the chiller and bath-temperature story after reading the night-shift handoff note.",
      "affected_reasoning_operation": "Hypothesis generation and initial search priority",
      "bias_specific_mechanism": "The night-shift operator's temperature note served as an initial anchor; the participant adopted it quickly and allowed it to shape subsequent investigative attention without sufficiently adjusting toward the alternative rectifier-calibration possibility.",
      "manifestation_in_interview": "The participant said the temperature story made immediate sense and started there, and later acknowledged that the order in which information arrived shaped where he looked first.",
      "effect_on_reasoning_or_decision": "Narrowed the early diagnostic path toward temperature/chiller work and delayed consideration of the rectifier calibration log.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The first thing on my desk that morning was a handoff note from the night-shift operator saying the bath temperature had spiked overnight and he suspected that was causing the pitting. That made immediate sense to me — anodizing bath temperature is a classic culprit for pitting, it's easy to check, and it fit a story I could act on right away. So I started there.",
          "evidence_explanation": "This shows the initial handoff note was treated as an immediately acceptable explanation and became the starting point for the investigation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It's hard to say which one I'd have found more compelling, but the order I got things in definitely shaped where I looked first.",
          "evidence_explanation": "This explicitly indicates that the initial information anchored the direction of subsequent inquiry."
        }
      ],
      "correction_or_counterevidence": "After the chiller was fixed and pitting persisted, the participant did update away from the initial temperature-only explanation and moved to chemistry, but the early search had already been anchored.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Rastogi et al. (2022) was used for the general anchoring-and-adjustment mechanism, though the source concerns AI-assisted decision making rather than this exact industrial setting.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoring-and-adjustment heuristic is a resourcerational tradeo between time and accuracy",
          "mechanism_supported_by_source": "Anchoring-and-adjustment involves starting from an initial reference point and insufficiently adjusting away from it.",
          "relevance_to_this_occurrence": "The participant began with the night-shift note as the initial reference point and then showed insufficient adjustment toward the rectifier-calibration alternative."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "selective exposure",
        "confirmatory search"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, attend to, interpret, or recall information in a way that confirms an existing hypothesis or belief while discounting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Early investigation under the temperature hypothesis",
      "decision_point_description": "Choosing not to open the rectifier-log summary in the same folder during the first week of investigation.",
      "affected_reasoning_operation": "Information search and attention allocation",
      "bias_specific_mechanism": "Once the temperature story was accepted, the participant prioritized temperature-related checks and did not sample the disconfirming rectifier calibration log that was available in the same folder.",
      "manifestation_in_interview": "The participant stated that the temperature story was already the frame and that the rectifier note 'just sat there' while the chiller took priority.",
      "effect_on_reasoning_or_decision": "A potentially relevant alternative cause was not reviewed early, delaying a more complete root-cause search.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was actually a short rectifier-log summary sitting in the same folder that flagged a calibration deviation from a few days earlier, but I didn't open it that week — the temperature story was already the frame I was working from, so the chiller took priority and the rectifier note just sat there.",
          "evidence_explanation": "This demonstrates selective attention toward information consistent with the temperature hypothesis and neglect of a disconfirming alternative."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd also go back and actually open that rectifier summary on day one instead of letting the first explanation carry the week.",
          "evidence_explanation": "This retrospective statement confirms that the initial explanation was allowed to dominate early search behavior."
        }
      ],
      "correction_or_counterevidence": "When pitting persisted after temperature stabilization, the participant did shift to the dosing/chemistry hypothesis, so the bias did not permanently fix the final diagnosis, but it did shape early information search.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Parasuraman and Manzey (2010) was used only to connect the occurrence to the general confirmation-bias mechanism of discounting contradictory information in diagnostic/automation contexts.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "an explanation in terms of confirmation bias in processing the sampled information or difficulties of comprehension is also unlikely",
          "mechanism_supported_by_source": "Confirmation bias is discussed as a decision bias involving processing sampled information in a way consistent with an existing diagnosis.",
          "relevance_to_this_occurrence": "The participant processed search priorities in line with the initial temperature diagnosis and left a contradicting calibration summary unread, matching a confirmatory-search pattern."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "fundamental attribution error",
      "alternative_labels": [
        "correspondence bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to overemphasize dispositional factors and underemphasize situational or systemic factors when explaining another person's behavior or outcomes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Explaining day-shift vs night-shift defect-rate difference",
      "decision_point_description": "Flagging the day-shift operator's perceived carelessness as a contributing factor in his notes.",
      "affected_reasoning_operation": "Causal attribution of production defect variation",
      "bias_specific_mechanism": "The participant attributed the higher day-shift defect rate to the operator's individual carelessness and experience, while underweighting situational explanations such as equipment condition or chemistry drift over a shift.",
      "manifestation_in_interview": "He said his first instinct was that the day-shift operator was less careful and that he focused on him.",
      "effect_on_reasoning_or_decision": "Produced a premature person-centered attribution and reduced early exploration of process or equipment factors.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first instinct was that the day-shift operator was less careful — he's newer, and I'd noticed him rushing rack loading a couple times. I flagged it in my notes as a contributing factor.",
          "evidence_explanation": "This shows a dispositional explanation being adopted rapidly and entered into the investigation record."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I didn't spend much time asking whether the equipment was in worse condition during the day, or whether the chemistry itself might drift over the course of a shift. I focused on him.",
          "evidence_explanation": "This directly acknowledges underweighting of situational/process causes relative to the operator-focused explanation."
        }
      ],
      "correction_or_counterevidence": "Later in the interview the participant says he would want to revisit that attribution because he never fully ruled out process or equipment factors, though this did not correct the initial note.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available for fundamental attribution error; the label and mechanism rest on general cognitive-social psychology knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bandwagon effect",
      "alternative_labels": [
        "social proof",
        "conformity bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to adopt a belief or course of action because many others have adopted it, rather than through independent evaluation of the evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor selection for dosing control system",
      "decision_point_description": "Selecting Vendor A and stopping the structured comparison after hearing that three sister plants were running it.",
      "affected_reasoning_operation": "Vendor evaluation and evidence weighting",
      "bias_specific_mechanism": "Social evidence from three sister plants served as a sufficient substitute for completing the independent requirement-by-requirement comparison, producing early closure on Vendor A.",
      "manifestation_in_interview": "The participant said that once three sister plants confirmed Vendor A worked, that was enough and he did not finish the comparison.",
      "effect_on_reasoning_or_decision": "Vendor A was chosen even though the technical comparison had been tilting toward Vendor B, and the remaining comparison was left incomplete.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But once I had three sister plants confirming Vendor A worked, that was enough for me — I didn't finish walking through the rest of the comparison.",
          "evidence_explanation": "This shows the decision was closed based on adoption by other sites rather than completion of independent evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "One of the three plants had reported mixed results with it. I knew that going in. But with three plants running it versus one incomplete installation elsewhere, it felt like the safer bet.",
          "evidence_explanation": "The participant acknowledged conflicting evidence from one site but still treated the majority usage as the overriding signal."
        }
      ],
      "correction_or_counterevidence": "There was also a legitimate heuristic justification for valuing installed-base evidence from sister plants, and the participant had begun a formal comparison; confidence is moderate because the behavior overlaps with a reasonable professional practice.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available for the bandwagon effect; the label and mechanism rest on general social-influence knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "ambiguity aversion",
      "alternative_labels": [
        "ambiguity effect",
        "uncertainty aversion"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for known or familiar risks over unknown risks, even when the unfamiliar option may have better expected features.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor selection for dosing control system (uncertainty assessment)",
      "decision_point_description": "Deciding not to pursue Vendor B's offer to walk through the open commissioning questions and instead choosing Vendor A.",
      "affected_reasoning_operation": "Risk/uncertainty assessment in technology selection",
      "bias_specific_mechanism": "Vendor B's documentation gaps and incomplete reference installation made its uncertainty feel less acceptable than Vendor A's familiar unknowns, even though Vendor B was stronger on the technical criteria the participant cared about most.",
      "manifestation_in_interview": "The participant said unresolved gaps felt less acceptable than Vendor A's familiar unknowns and so he did not take up the Vendor B engineer's offer.",
      "effect_on_reasoning_or_decision": "A potentially better technical alternative was rejected because of discomfort with unfamiliar/unknown implementation details.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Vendor B had a newer inline sensor-based system with a stronger spec sheet on paper — actually stronger on the sensing and control criteria we cared about most — but only one reference installation, and their documentation was thin, with gaps in the install manual and unclear commissioning steps.",
          "evidence_explanation": "This establishes that Vendor B was technically stronger but had less-certain implementation details."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Vendor B's applications engineer even offered to walk us through the open commissioning questions, and there wasn't any identified incompatibility, but the unresolved gaps still felt less acceptable to me than Vendor A's familiar unknowns, so I didn't take him up on it.",
          "evidence_explanation": "This shows a preference for the familiar uncertainty of Vendor A over the less familiar uncertainty of Vendor B."
        }
      ],
      "correction_or_counterevidence": "Avoiding a thin-documentation vendor with only one reference installation could also be a rational risk-management choice; the bias interpretation is supported by the explicit contrast between familiar unknowns and unresolved gaps, but a non-bias explanation is plausible.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available for ambiguity aversion; the label and mechanism rest on general decision-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "gambler's fallacy",
      "alternative_labels": [
        "Monte Carlo fallacy",
        "negative recency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Mistaken belief that past random or independent outcomes change the probability of future outcomes, such as believing that bad luck has been used up after a run of good outcomes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting post-install batch sequence",
      "decision_point_description": "Telling the quality manager that the odds of another bad batch were low after five clean batches.",
      "affected_reasoning_operation": "Probability judgment about future process outcomes",
      "bias_specific_mechanism": "The clean-batch streak was interpreted as evidence that earlier instability had been exhausted, making a future rough batch seem less likely.",
      "manifestation_in_interview": "The participant said the system had 'used up' its bad luck or instability and reported telling the quality manager the odds of another bad batch were low.",
      "effect_on_reasoning_or_decision": "Produced an overly optimistic informal probability judgment about the near-term likelihood of another bad batch.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, after those two rough batches, having five clean ones in a row felt like the process had settled the score — like whatever bad luck or instability had been in the system early on had been used up, so another rough batch felt a lot less likely right then.",
          "evidence_explanation": "The phrase 'used up' directly expresses the gambler's-fallacy mechanism that past good outcomes reduce the probability of future bad outcomes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember telling the quality manager the odds of another bad one showing up were pretty low, given the run we'd had.",
          "evidence_explanation": "This confirms that the biased probability estimate was communicated as a judgment about future risk."
        }
      ],
      "correction_or_counterevidence": "The participant did state that certification prep timing was calendar-driven and that he still treated the process-stability call as open, so the biased probability judgment did not fully determine the certification action.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available for gambler's fallacy; the label and mechanism rest on general decision-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_007",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "illusion of control",
      "alternative_labels": [
        "self-serving bias",
        "self-attribution bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Overestimation of one's personal influence or control over outcomes, attributing success to one's own actions while neglecting external causes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Attributing source of post-install improvement",
      "decision_point_description": "Attributing the clean-batch turnaround mostly to his manual rectifier voltage adjustments rather than the concurrent chemistry replenishment.",
      "affected_reasoning_operation": "Causal attribution of process improvement",
      "bias_specific_mechanism": "The participant treated his small manual voltage tweaks as the primary cause of the clean-batch turnaround and did not separate their effect from the scheduled chemistry replenishment.",
      "manifestation_in_interview": "He said he felt like he was actively steering the process back into spec and had not separated the two possible causes.",
      "effect_on_reasoning_or_decision": "Inflated confidence in his own manual adjustments as the cause of improvement and delayed a more systematic separation of causes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But honestly, I attributed most of the turnaround to the manual rectifier voltage adjustments I was making between runs — small tweaks based on how the previous batch looked. I felt like I was actively steering it back into spec. I never really separated the two effects out.",
          "evidence_explanation": "This shows personal agency was assigned primary causal credit despite an unexplored concurrent treatment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably how much credit I gave myself for the manual adjustments versus the chemistry replenishment — I never really separated those out.",
          "evidence_explanation": "This acknowledges that the causal separation was not performed, supporting the illusion-of-control interpretation."
        }
      ],
      "correction_or_counterevidence": "The participant later recognizes this as a point he would reconsider, but there is no evidence that the attribution was corrected during the decision episode itself.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available for illusion of control; the label and mechanism rest on general cognitive-bias knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_008",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "recency effect",
      "alternative_labels": [
        "recency bias",
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to weigh the most recent or easily recalled information more heavily than older or less salient information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "PPAP certification sign-off recommendation",
      "decision_point_description": "Writing the certification recommendation with primary weight on the final validation lot rather than the full trial dataset or marginal Cpk result.",
      "affected_reasoning_operation": "Evidence weighting for certification sign-off",
      "bias_specific_mechanism": "The most recent clean validation lot was treated as the most representative picture of process performance, while earlier trial variability and the separately filed marginal Cpk result were underweighted.",
      "manifestation_in_interview": "The participant said the final lot carried most of the weight in his recommendation and that the marginal Cpk result was not front and center.",
      "effect_on_reasoning_or_decision": "The certification recommendation relied disproportionately on the latest clean lot and may have underweighted earlier variability and the marginal capability finding.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The final lot was really what tipped my confidence. It was the cleanest result we'd seen, run right before submission, so it felt like the truest picture of where the process actually stood. I referenced the earlier trial data in the memo, but the final lot carried most of the weight in my recommendation to certify.",
          "evidence_explanation": "This demonstrates disproportionate weighting of the most recent result over the broader trial data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a marginal Cpk result from a quality audit, yes, but it had been filed separately from the sign-off packet, so it wasn't front and center when I was writing the recommendation.",
          "evidence_explanation": "This shows a less salient but analytically relevant piece of evidence was not given active weight during the recommendation."
        }
      ],
      "correction_or_counterevidence": "The participant says that under less time pressure he would have pulled the Cpk data into the memo directly, and time pressure may have contributed to the weighting; however, the recency mechanism is independently evident in his description of the final lot as the truest picture.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Natesan et al. (2016) was used for the recency-effect mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": "Natesan et al.",
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Recent events are more easily remembered and can disproportionately influence evaluation.",
          "relevance_to_this_occurrence": "The participant gave the most recent clean lot disproportionate weight in the certification decision, consistent with the recency-effect mechanism."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Sparse retrieved corpus did not include direct sources for several detected mechanisms, including fundamental attribution error, bandwagon effect, ambiguity aversion, gambler's fallacy, and illusion of control; those labels rest on general knowledge and are disclosed as such.",
    "Some transcripts are retrospective self-reports and may be affected by memory reconstruction; the analysis used only affirmative statements in the interview.",
    "Several episodes include plausible non-bias explanations, especially time pressure and legitimate vendor risk management; confidence was adjusted where those explanations coexist with the bias-specific mechanism."
  ]
}

