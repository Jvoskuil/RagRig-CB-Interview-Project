# RAG Benchmark — 2026-09-13

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'll ask you to walk me through a specific incident in detail, and there are no right or wrong answers. Everything's for internal learning purposes. Can you tell me your current role and how long you've been in it? Participant: Sure. I'm the ventilation engineer for the underground section — mainly responsible for the primary and auxiliary fan systems, the VOD setup, and gas monitoring across the active levels. I've been in this role about six years, underground ventilation for closer to eleven overall. Interviewer: Good. Let's start with the incident itself. What happened? Participant: This was during a shift where we had a scheduled production blast on 14 Level. Standard round, nothing unusual planned. About thirty minutes after blast clearance time, one of our gas stations — GS-14R, out in the return airway — started reading CO at 280 ppm. Baseline after a blast like that is usually under 50 ppm once the primary fan's had time to clear it. So that number stood out immediately. Interviewer: What went through your mind when you saw that? Participant: Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again. I pulled the telemetry log to check the trend, and it had spiked pretty sharply rather than climbing gradually, which is more consistent with a dust or particulate interference pattern than a genuine gas buildup, in my experience. Interviewer: Was there any other information available to you at that point? Participant: Yes — the gas monitoring technician had taken a handheld multi-gas detector reading out at the return airway around the same time, and that came back at 190 ppm. Lower than the station reading, but still well above baseline. No maintenance ticket had confirmed a fault on GS-14R yet either — that hadn't been checked this shift. Interviewer: How did you weigh those two numbers against each other? Participant: I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule. Interviewer: Did you consider getting a second confirmatory reading, or requesting a recalibration check before deciding? Participant: I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward. Interviewer: What happened next? Participant: Re-entry went ahead. About twenty minutes later, the shift boss called me — one of the crew wanted to hold at the refuge chamber a few extra minutes before heading further in, just as a precaution. Nothing specific triggering it, more a gut feeling. Interviewer: What was your reasoning at that point? Participant: That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe. Interviewer: Was there anything in the data at that point pointing toward fire specifically? Participant: Not really, no. No smoke reports, no heat, and the secondary gas trends weren't showing anything unusual — CO2 was flat. Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed. I didn't want to be the one who waved people through if there was any chance it was something bigger. Interviewer: How did that play out? Participant: No fire indicators ever showed up. We eventually put it down to a longer-than-usual round that took a bit more time to clear than normal. The fifteen-minute hold turned out to be unnecessary, though nobody complained about the extra caution. Interviewer: Let's move to the threshold question. What came up there? Participant: Later that shift, the mine planning superintendent asked whether we should revise the CO auto-cutoff setpoint on GS-14R before ramping the LHD fleet back up fully. Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now. Interviewer: Did you have newer data available? Participant: We did, and it was actually pretty usable. The recent baseline surveys had shown ambient CO trending noticeably higher under current depth and fleet conditions — enough that during normal diesel-heavy periods we were regularly running close to or past the old setting without anything else flagging as hazardous. A couple of us had even talked informally about a materially higher interim figure being more realistic given those numbers. We hadn't done a formal re-baseline since the fleet expanded two years ago, but the recent surveys were solid enough to work from for an interim call. Interviewer: What did you decide? Participant: I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher. I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested. Interviewer: How did that work out afterward? Participant: Not great, if I'm honest. Over the following shifts the auto-cutoff started tripping more often during normal diesel-heavy periods — nothing hazardous, just operational friction, alarms going off during routine LHD movement. We've since talked about doing the full re-baseline properly. Interviewer: Last decision point — the incident closeout. Walk me through that. Participant: The safety officer wanted a closing narrative before full production resumed. By that point we had three things on the table: the sensor's drift history, the LHD fleet idling near the loading point during the relevant window, and the fact that the round itself ran a bit long. None of those had been tested individually — we hadn't isolated the sensor alone, or the fleet alone, to see which one actually explained the spike. Interviewer: How did you write it up? Participant: I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure. Mine planning was waiting on that closure to greenlight full resumption, so I didn't push for a separate follow-up test. Interviewer: Looking back, is there another explanation that fits those same facts just as well? Participant: In principle, sure — it could've leaned more on the fleet, or more on the clearance delay, and the sensor could've been almost incidental. We never separated them out to check. But at the time, the combined account was what went into the record, and it's what mine planning worked from. Interviewer: If the handheld reading that morning had come back much higher than the station reading, would your first call have changed? Participant: Probably, yes. If it had matched or exceeded the station number, I'd have taken it more seriously as a real hazard rather than sensor noise. Interviewer: And if you'd had time to run a full re-baseline before setting the threshold? Participant: I'd have set it higher, most likely, based on the newer survey data. Time was the constraint there, not confidence in the old number. Interviewer: How much would you say the schedule pressure from mine planning shaped your decisions that day? Participant: More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 4.06s · gen 211.87s · total 219.0s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0289 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0279 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0269 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0253 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0234 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0218 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0208 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0207 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0205 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0184 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0176 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
13. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0173 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
14. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0173 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0167 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0166 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
19. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0165 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
21. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0163 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
24. **Hallihan_etal_DTM_12.pdf** — 0.0155 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
26. **Lyell Automation bias and verification complexity.pdf** — 0.0154 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
27. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0153 (rrf) — _# Cognitive Biases Within Decision Making 475 Perception Attentiveness Comprehension Credibility_
28. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
30. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0151 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
32. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0147 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
34. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0146 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
35. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0146 (rrf) — _## Influence of Cognitive Biases in Distorting Decision Making and Leading to Critical Unfavorab_
36. **Lyell Automation bias and verification complexity.pdf** — 0.0145 (rrf) — _# # – – – – – – – – – – – ### ### – P ¼ .031 ### > .05 ## < .001 DDS ( 31 ) 29 general practi- M_
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0145 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
38. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0145 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
39. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0143 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
40. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0142 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
41. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
42. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0141 (rrf) — _[61\] or the Observer-Expectancy Effects On that note, are we, as ISR researchers, also cognitiv_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
47. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0139 (rrf) — _# 478 Fire Technology 2019 This classification process is intended to highlight how the cognitiv_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
49. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0138 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias The confidence bias originates _
50. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0137 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single CTA interview analyzed for affirmatively demonstrated cognitive biases; retrieved corpus used for mechanism grounding where available."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
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
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["expectation bias", "selective evidence weighting", "myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm existing beliefs or expectations while discounting disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial assessment of GS-14R CO spike",
      "decision_point_description": "Interpreting whether the GS-14R CO reading represented a genuine gas hazard or a sensor artifact.",
      "affected_reasoning_operation": "Evidence weighting and hypothesis evaluation",
      "bias_specific_mechanism": "Pre-existing expectation of GS-14R sensor failure caused selective weighting of station history and telemetry features as confirmatory, while the handheld reading—a disconfirmatory but independent data point—was rationalized away as possible calibration drift.",
      "manifestation_in_interview": "The participant immediately categorized the high CO reading as another GS-14R sensor problem, interpreted the sharp spike as consistent with dust interference, and gave less weight to the 190 ppm handheld reading despite it still being well above baseline.",
      "effect_on_reasoning_or_decision": "The participant classified the spike as likely sensor artifact, underweighting the handheld reading, which supported immediate re-entry rather than precautionary verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again.",
          "evidence_explanation": "Demonstrates a pre-existing expectation about GS-14R sensor reliability that directed initial hypothesis formation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind.",
          "evidence_explanation": "Shows selective weighting of history consistent with the participant's existing belief about the sensor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have.",
          "evidence_explanation": "Explicitly acknowledges discounting an independent disconfirmatory reading through a plausible but unverified rationalization."
        }
      ],
      "correction_or_counterevidence": "The handheld was 190 ppm, still well above baseline, and no maintenance ticket had confirmed a GS-14R fault. The participant later acknowledged that if the handheld had matched or exceeded the station reading, he would have taken it more seriously. Eventual closeout suggested a longer round/clearance delay, though this was not known at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus mentioned confirmation bias only by name without providing an operational definition or mechanism; classification uses established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis", "plan continuation error"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an existing or planned course of action despite changing conditions or cues indicating it may be unsafe or inappropriate.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to proceed with scheduled re-entry after anomalous CO reading",
      "decision_point_description": "Choosing whether to delay re-entry for confirmatory sensor diagnostics or proceed on schedule.",
      "affected_reasoning_operation": "Risk assessment and go/no-go scheduling decision under uncertainty",
      "bias_specific_mechanism": "The default plan of re-entry/restart created commitment to continue; schedule pressure from mine planning increased the cost of delay and made continuation more attractive despite unresolved anomalous CO evidence.",
      "manifestation_in_interview": "The participant considered a second confirmatory reading or recalibration check but decided to proceed with scheduled re-entry after logging the handheld reading, partly because mine planning was waiting on restart timing.",
      "effect_on_reasoning_or_decision": "Re-entry went ahead without a second confirmatory reading or recalibration check, preserving production schedule at the expense of diagnostic certainty.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule.",
          "evidence_explanation": "Shows the decision to continue with the original re-entry plan despite an unresolved anomalous CO reading."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward.",
          "evidence_explanation": "Shows schedule pressure directly influenced the decision not to obtain a confirmatory reading or recalibration check."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.",
          "evidence_explanation": "Explicitly links production schedule pressure to decisions that favored continuation over delay."
        }
      ],
      "correction_or_counterevidence": "There were legitimate operational constraints, including mine planning pressure and lack of hard evidence, and the prior station false alarms made sensor error plausible. The eventual outcome did not show a fire or acute gas emergency.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus mentioned plan continuation bias by name but did not provide an operational definition or mechanism; classification uses general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge event likelihood by the ease with which vivid or recent instances come to mind, producing overestimation of salient risks.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Precautionary hold after crew gut feeling",
      "decision_point_description": "Deciding whether to grant the shift boss's request to hold crew and trigger partial fire-response protocol.",
      "affected_reasoning_operation": "Risk probability estimation and precautionary resource allocation",
      "bias_specific_mechanism": "The vivid, recent safety briefing about a fatal underground fire made fire scenarios mentally available and emotionally salient, inflating their subjective plausibility relative to base rates and current data.",
      "manifestation_in_interview": "When the shift boss requested a precautionary hold, the participant allowed the recent fire-fatality briefing to make a fire scenario feel more plausible than the objective data indicated.",
      "effect_on_reasoning_or_decision": "He approved a crew hold and partially triggered the fire-response protocol despite no fire-specific indicators.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me.",
          "evidence_explanation": "Identifies a vivid, recent safety event that was mentally available during the subsequent risk judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe.",
          "evidence_explanation": "Shows the available fire case directly influenced the precautionary decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed.",
          "evidence_explanation": "Explicitly acknowledges that subjective plausibility of fire was inflated by the remembered briefing rather than by current evidence."
        }
      ],
      "correction_or_counterevidence": "No fire indicators were present—no smoke, no heat, CO2 flat—and fume-clearance delay was the more common explanation. The hold was precautionary and not harmful, but the participant acknowledged the fire scenario felt more plausible than the data supported.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied an availability heuristic definition; classification relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment heuristic", "anchor effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value and make insufficient adjustments when incorporating subsequent information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Revision of CO auto-cutoff setpoint",
      "decision_point_description": "Deciding whether to keep the 100 ppm CO auto-cutoff setpoint or adjust it toward newer baseline survey values.",
      "affected_reasoning_operation": "Numeric threshold estimation and adjustment",
      "bias_specific_mechanism": "The existing 100 ppm commissioning setpoint served as an anchor; newer survey data indicating higher ambient CO were treated as insufficient justification to move far from the anchor, resulting in only a minor adjustment.",
      "manifestation_in_interview": "Despite newer baseline surveys showing ambient CO trending materially higher under current depth and fleet conditions, the participant made only a small adjustment and kept the setpoint close to the five-year-old commissioning figure.",
      "effect_on_reasoning_or_decision": "The setpoint remained near the old 100 ppm value; subsequent normal diesel-heavy periods caused frequent auto-cutoff trips and operational friction.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our commissioning report, from about five years back, had that threshold set at 100 ppm.",
          "evidence_explanation": "Identifies the initial value that served as the anchor for later judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher.",
          "evidence_explanation": "Shows the anchor was treated as an appropriate default despite newer data supporting a larger change."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested.",
          "evidence_explanation": "Demonstrates insufficient adjustment from the anchor despite usable recent survey data."
        }
      ],
      "correction_or_counterevidence": "The commissioning number had undergone formal review, and a full re-survey was not possible that day. However, newer baseline surveys and diesel-heavy operating data pointed toward a higher interim setpoint; subsequent auto-cutoff trips confirmed the retained anchor was too low.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus provided a description of anchoring and adjustment, including insufficient adjustment from an initial value, directly supporting the mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described by Tversky and Kahneman in 1974... people make estimates based on an initial answer, and adjustments from there based on additional information... Tversky and Kahneman put it, \"adjustments are typically insufficient.\"",
          "mechanism_supported_by_source": "Initial values serve as anchors, and subsequent adjustments are typically insufficient.",
          "relevance_to_this_occurrence": "The participant used the five-year-old 100 ppm commissioning setpoint as an anchor and made only a small adjustment despite newer baseline data supporting a materially higher threshold."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "narrative fallacy",
      "alternative_labels": ["coherence bias", "illusion of explanatory depth"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Incident closeout causal attribution",
      "supporting_interview_quote": "I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure.",
      "plausible_mechanism": "Coherence of a multi-causal narrative may have substituted for isolation testing, increasing perceived completeness and reducing the perceived need to test individual causes.",
      "why_not_identified": "Insufficient affirmative evidence that story coherence, rather than ordinary causal judgment under time and resource constraints, materially distorted the written causal attribution; the participant did not explicitly state overconfidence in the combined narrative."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages were OCR-impaired and provided limited mechanistic definitions for several labels.",
    "Single interview narrative may be affected by retrospective reconstruction and self-presentation, though temporal reasoning was evaluated from information available at the time.",
    "Low-confidence plan-continuation finding overlaps with legitimate production schedule constraints and should be interpreted cautiously.",
    "No follow-up evidence or independent verification of the incident details was available."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'll ask you to walk me through a specific incident in detail, and there are no right or wrong answers. Everything's for internal learning purposes. Can you tell me your current role and how long you've been in it? Participant: Sure. I'm the ventilation engineer for the underground section — mainly responsible for the primary and auxiliary fan systems, the VOD setup, and gas monitoring across the active levels. I've been in this role about six years, underground ventilation for closer to eleven overall. Interviewer: Good. Let's start with the incident itself. What happened? Participant: This was during a shift where we had a scheduled production blast on 14 Level. Standard round, nothing unusual planned. About thirty minutes after blast clearance time, one of our gas stations — GS-14R, out in the return airway — started reading CO at 280 ppm. Baseline after a blast like that is usually under 50 ppm once the primary fan's had time to clear it. So that number stood out immediately. Interviewer: What went through your mind when you saw that? Participant: Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again. I pulled the telemetry log to check the trend, and it had spiked pretty sharply rather than climbing gradually, which is more consistent with a dust or particulate interference pattern than a genuine gas buildup, in my experience. Interviewer: Was there any other information available to you at that point? Participant: Yes — the gas monitoring technician had taken a handheld multi-gas detector reading out at the return airway around the same time, and that came back at 190 ppm. Lower than the station reading, but still well above baseline. No maintenance ticket had confirmed a fault on GS-14R yet either — that hadn't been checked this shift. Interviewer: How did you weigh those two numbers against each other? Participant: I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule. Interviewer: Did you consider getting a second confirmatory reading, or requesting a recalibration check before deciding? Participant: I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward. Interviewer: What happened next? Participant: Re-entry went ahead. About twenty minutes later, the shift boss called me — one of the crew wanted to hold at the refuge chamber a few extra minutes before heading further in, just as a precaution. Nothing specific triggering it, more a gut feeling. Interviewer: What was your reasoning at that point? Participant: That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe. Interviewer: Was there anything in the data at that point pointing toward fire specifically? Participant: Not really, no. No smoke reports, no heat, and the secondary gas trends weren't showing anything unusual — CO2 was flat. Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed. I didn't want to be the one who waved people through if there was any chance it was something bigger. Interviewer: How did that play out? Participant: No fire indicators ever showed up. We eventually put it down to a longer-than-usual round that took a bit more time to clear than normal. The fifteen-minute hold turned out to be unnecessary, though nobody complained about the extra caution. Interviewer: Let's move to the threshold question. What came up there? Participant: Later that shift, the mine planning superintendent asked whether we should revise the CO auto-cutoff setpoint on GS-14R before ramping the LHD fleet back up fully. Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now. Interviewer: Did you have newer data available? Participant: We did, and it was actually pretty usable. The recent baseline surveys had shown ambient CO trending noticeably higher under current depth and fleet conditions — enough that during normal diesel-heavy periods we were regularly running close to or past the old setting without anything else flagging as hazardous. A couple of us had even talked informally about a materially higher interim figure being more realistic given those numbers. We hadn't done a formal re-baseline since the fleet expanded two years ago, but the recent surveys were solid enough to work from for an interim call. Interviewer: What did you decide? Participant: I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher. I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested. Interviewer: How did that work out afterward? Participant: Not great, if I'm honest. Over the following shifts the auto-cutoff started tripping more often during normal diesel-heavy periods — nothing hazardous, just operational friction, alarms going off during routine LHD movement. We've since talked about doing the full re-baseline properly. Interviewer: Last decision point — the incident closeout. Walk me through that. Participant: The safety officer wanted a closing narrative before full production resumed. By that point we had three things on the table: the sensor's drift history, the LHD fleet idling near the loading point during the relevant window, and the fact that the round itself ran a bit long. None of those had been tested individually — we hadn't isolated the sensor alone, or the fleet alone, to see which one actually explained the spike. Interviewer: How did you write it up? Participant: I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure. Mine planning was waiting on that closure to greenlight full resumption, so I didn't push for a separate follow-up test. Interviewer: Looking back, is there another explanation that fits those same facts just as well? Participant: In principle, sure — it could've leaned more on the fleet, or more on the clearance delay, and the sensor could've been almost incidental. We never separated them out to check. But at the time, the combined account was what went into the record, and it's what mine planning worked from. Interviewer: If the handheld reading that morning had come back much higher than the station reading, would your first call have changed? Participant: Probably, yes. If it had matched or exceeded the station number, I'd have taken it more seriously as a real hazard rather than sensor noise. Interviewer: And if you'd had time to run a full re-baseline before setting the threshold? Participant: I'd have set it higher, most likely, based on the newer survey data. Time was the constraint there, not confidence in the old number. Interviewer: How much would you say the schedule pressure from mine planning shaped your decisions that day? Participant: More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.86s · gen 301.98s · total 307.5s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0289 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0279 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0269 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0253 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0234 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0218 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0208 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0207 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0205 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0184 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0176 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
13. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0173 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
14. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0173 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0167 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0166 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
19. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0165 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
21. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0163 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
24. **Hallihan_etal_DTM_12.pdf** — 0.0155 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
26. **Lyell Automation bias and verification complexity.pdf** — 0.0154 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
27. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0153 (rrf) — _# Cognitive Biases Within Decision Making 475 Perception Attentiveness Comprehension Credibility_
28. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
30. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0151 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
32. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0147 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
34. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0146 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
35. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0146 (rrf) — _## Influence of Cognitive Biases in Distorting Decision Making and Leading to Critical Unfavorab_
36. **Lyell Automation bias and verification complexity.pdf** — 0.0145 (rrf) — _# # – – – – – – – – – – – ### ### – P ¼ .031 ### > .05 ## < .001 DDS ( 31 ) 29 general practi- M_
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0145 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
38. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0145 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
39. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0143 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
40. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0142 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
41. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
42. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0141 (rrf) — _[61\] or the Observer-Expectancy Effects On that note, are we, as ISR researchers, also cognitiv_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
47. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0139 (rrf) — _# 478 Fire Technology 2019 This classification process is intended to highlight how the cognitiv_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
49. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0138 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias The confidence bias originates _
50. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0137 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single interview analyzed for reasoning episodes with affirmative evidence of bias-specific mechanisms. Retrieved corpus passages were used where they supported a label or mechanism; several well-established labels were applied from general cognitive-science knowledge where retrieved support was unavailable."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Narrative fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Plan continuation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias", "Recency effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments of likelihood or frequency are influenced by how easily relevant instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation of GS-14R CO spike",
      "decision_point_description": "Deciding whether the 280 ppm CO reading reflected a real gas hazard or a sensor artifact",
      "affected_reasoning_operation": "Causal diagnosis and probability judgment about the gas reading",
      "bias_specific_mechanism": "Recent, easily recalled false-alarm episodes involving GS-14R dominated the participant's causal judgment, making another sensor-artifact explanation seem highly likely before all current evidence was weighed.",
      "manifestation_in_interview": "The participant immediately identified the station's recent false-spike history and said the pattern was 'fresh in my mind'; he then discounted the concurrent handheld reading and concluded it was probably another sensor issue.",
      "effect_on_reasoning_or_decision": "The diagnostic judgment favored sensor noise over a possible gas buildup, supporting the later decision to proceed with scheduled re-entry rather than delaying for confirmatory checks.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again.",
          "evidence_explanation": "Shows the immediate dominance of past false-alarm instances in framing the current reading."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind.",
          "evidence_explanation": "Explicitly describes weighting current evidence by the ease of recalling recent similar incidents, which is the availability mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant did examine the telemetry trend and had a handheld reading; the sensor-fault explanation was not confirmed false at the time. He later acknowledged he did not weight the handheld reading as heavily as he should have.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support specifically for the availability heuristic was not available; the label is applied from well-established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Myside bias", "Confirmatory bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that support an existing hypothesis or belief while discounting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Weighing station versus handheld CO readings",
      "decision_point_description": "Assessing whether the lower handheld reading should call the initial sensor-fault hypothesis into question",
      "affected_reasoning_operation": "Evidence integration and hypothesis testing",
      "bias_specific_mechanism": "After forming the initial sensor-fault hypothesis, the participant overweighted history consistent with that hypothesis and rationalized away the conflicting handheld reading, which was still well above baseline, by invoking possible calibration drift without checking it.",
      "manifestation_in_interview": "The participant said he leaned on the station's history more than the handheld number and elected not to obtain a second confirmatory reading or maintenance confirmation before proceeding.",
      "effect_on_reasoning_or_decision": "The disconfirming handheld reading was not given enough weight to trigger a delay or further check, leaving the initial sensor-fault hypothesis effectively intact.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have.",
          "evidence_explanation": "The participant offers a plausible reason for setting aside the conflicting value, but the statement also indicates underweighting disconfirming evidence after a sensor-fault hypothesis was already active."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned on the station's history more than the handheld number, honestly.",
          "evidence_explanation": "Shows selective weighting favoring the prior hypothesis over the current independent reading."
        }
      ],
      "correction_or_counterevidence": "The handheld reading was indeed lower than the station value, and calibration drift is a legitimate concern; no fault had been confirmed on either instrument at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for a definition of confirmation bias was not available; the label and mechanism are from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Plan continuation bias",
      "alternative_labels": ["Plan continuation error", "Get-there-itis"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an original plan or course of action despite cues that conditions have changed or uncertainty has increased.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Re-entry go/no-go after anomalous CO reading",
      "decision_point_description": "Whether to proceed with scheduled re-entry or delay while the CO discrepancy remained unresolved",
      "affected_reasoning_operation": "Risk-action decision under uncertainty",
      "bias_specific_mechanism": "The unresolved gas-reading anomaly did not interrupt the scheduled re-entry plan; the participant treated production restart timing and lack of 'hard evidence' as reasons to continue rather than as reasons to pause for confirmation.",
      "manifestation_in_interview": "The participant stated he made the call to proceed with re-entry on schedule and that delaying without hard evidence felt hard to justify, with mine planning already asking about restart timing.",
      "effect_on_reasoning_or_decision": "Crew proceeded into the area before confirmatory diagnostics; a later precautionary hold occurred only after additional concern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule.",
          "evidence_explanation": "Shows continuation with the planned re-entry despite an unresolved anomalous reading."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify.",
          "evidence_explanation": "Shows schedule pressure and a threshold asymmetry that favored continuation over delay."
        }
      ],
      "correction_or_counterevidence": "The continuation was downstream of a sensor-fault diagnosis and could be viewed as a rational response to that diagnosis plus schedule constraints; plan continuation is included with low confidence because the independent goal-continuation mechanism is not isolated from those pressures.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus material from the cockpit study supports the label and its operational relevance, though the mechanism definition is supplemented by general knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "This  continuation bias, in that it appears to occur in frequently during runway excursions on  landing, after longer duties and at the latter stages of flight.",
          "mechanism_supported_by_source": "Identifies plan continuation bias as an occurrence in operational accidents/incidents, particularly when continuing an active phase of flight.",
          "relevance_to_this_occurrence": "Mirrors the interview in which an existing plan, re-entry, was continued under unresolved conditions with production timing pressure."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias", "Salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments of likelihood are influenced by how easily vivid or emotional examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fire-risk judgment after shift boss's hold request",
      "decision_point_description": "Deciding whether to approve a precautionary hold and partially trigger fire-response when no fire indicators were present",
      "affected_reasoning_operation": "Probability and risk judgment about fire",
      "bias_specific_mechanism": "A recent, emotionally vivid fatal-fire briefing was highly available in memory and inflated the subjective plausibility of a fire scenario relative to the current data; the participant explicitly noted the data did not support that plausibility.",
      "manifestation_in_interview": "The participant said the briefing 'stuck with me' and was 'front and center', and that a fire scenario felt more plausible than it should have given flat CO2 and no smoke or heat.",
      "effect_on_reasoning_or_decision": "He approved the hold and partially triggered the fire-response protocol; the 15-minute hold proved unnecessary.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me.",
          "evidence_explanation": "Identifies a recent, emotionally vivid example that became easily retrievable."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe.",
          "evidence_explanation": "Shows the recalled example directly influencing the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed.",
          "evidence_explanation": "Explicitly describes the availability mechanism inflating subjective plausibility beyond the current evidence."
        }
      ],
      "correction_or_counterevidence": "The participant recognized that no smoke, heat, or secondary gas anomalies were present and that fume-clearance delays were the more common explanation; the caution was likely defensible.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support specifically for the availability heuristic was not available; the label is applied from well-established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment", "Anchoring effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Estimates are made based on an initial value, with adjustments from that anchor that are typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "CO auto-cutoff setpoint revision",
      "decision_point_description": "Deciding whether to revise the 100 ppm CO auto-cutoff setpoint using newer baseline surveys",
      "affected_reasoning_operation": "Numeric threshold estimation and adjustment",
      "bias_specific_mechanism": "The participant anchored on the original 100 ppm commissioning value, treating it as 'the number to stay near', and made only a minor adjustment despite newer survey data supporting a materially higher interim setpoint.",
      "manifestation_in_interview": "The participant stated the commissioning number had been reviewed and just felt like the number to stay near; he made a small tweak rather than moving to where interim numbers suggested.",
      "effect_on_reasoning_or_decision": "The cutoff remained too low for current operating conditions, causing frequent non-hazardous trips and operational friction.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher.",
          "evidence_explanation": "Shows the original value serving as a psychological anchor with only a minor adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested.",
          "evidence_explanation": "Demonstrates insufficient adjustment from the initial anchor despite newer evidence."
        }
      ],
      "correction_or_counterevidence": "Time pressure and lack of a formal re-baseline were real constraints; the participant says he would have set it higher with time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus passages directly support the anchoring-and-adjustment mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "People make estimates from an initial answer and adjust insufficiently from that anchor.",
          "relevance_to_this_occurrence": "The participant used the original commissioned 100 ppm value as an anchor and made only a minor adjustment despite new survey data pointing higher."
        }
      ]
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Narrative fallacy",
      "alternative_labels": ["Coherence bias", "Story bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to favor a coherent, complete narrative and to treat that coherence as evidence of explanatory validity.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Incident closeout causal explanation",
      "decision_point_description": "Writing the operative closing cause before full production resumption",
      "affected_reasoning_operation": "Causal attribution and explanation of the CO spike",
      "bias_specific_mechanism": "The participant constructed a combined three-factor account that 'read as a clean, complete account' and treated its completeness as sufficient for the operative cause without isolating or testing any factor individually.",
      "manifestation_in_interview": "He explicitly merged sensor drift, idling diesel fleet, and longer round into one narrative, and stated he did not pursue a separate follow-up test.",
      "effect_on_reasoning_or_decision": "The official closure attributed the spike to all three factors jointly despite none being separated; this became the basis for mine planning's resumption decision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw.",
          "evidence_explanation": "Shows a single explanatory narrative formed from multiple untested contributors."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure.",
          "evidence_explanation": "Shows subjective coherence being treated as sufficient for operational closure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We never separated them out to check.",
          "evidence_explanation": "Confirms the coherent account was not grounded in isolated empirical testing."
        }
      ],
      "correction_or_counterevidence": "Mine planning time pressure and lack of follow-up testing were both present; combining plausible contributors may have been a reasonable provisional closure, so this is classified with low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support specifically for narrative fallacy was not available; the label is applied from established cognitive-science and judgment-literature knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Single-interview, self-report data; the participant may rationalize or reconstruct decisions retrospectively.",
    "No direct behavioral measurement or objective benchmark confirming what a normative response would have been.",
    "Several decisions occurred under production time pressure; separating cognitive bias from legitimate operational constraint is difficult.",
    "Retrieved corpus support is sparse for several labels; some labels rely on general cognitive-science taxonomy rather than the provided RAG corpus.",
    "Confidence judgments are based on the interview alone and may understate the role of multiple interacting biases."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'll ask you to walk me through a specific incident in detail, and there are no right or wrong answers. Everything's for internal learning purposes. Can you tell me your current role and how long you've been in it? Participant: Sure. I'm the ventilation engineer for the underground section — mainly responsible for the primary and auxiliary fan systems, the VOD setup, and gas monitoring across the active levels. I've been in this role about six years, underground ventilation for closer to eleven overall. Interviewer: Good. Let's start with the incident itself. What happened? Participant: This was during a shift where we had a scheduled production blast on 14 Level. Standard round, nothing unusual planned. About thirty minutes after blast clearance time, one of our gas stations — GS-14R, out in the return airway — started reading CO at 280 ppm. Baseline after a blast like that is usually under 50 ppm once the primary fan's had time to clear it. So that number stood out immediately. Interviewer: What went through your mind when you saw that? Participant: Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again. I pulled the telemetry log to check the trend, and it had spiked pretty sharply rather than climbing gradually, which is more consistent with a dust or particulate interference pattern than a genuine gas buildup, in my experience. Interviewer: Was there any other information available to you at that point? Participant: Yes — the gas monitoring technician had taken a handheld multi-gas detector reading out at the return airway around the same time, and that came back at 190 ppm. Lower than the station reading, but still well above baseline. No maintenance ticket had confirmed a fault on GS-14R yet either — that hadn't been checked this shift. Interviewer: How did you weigh those two numbers against each other? Participant: I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule. Interviewer: Did you consider getting a second confirmatory reading, or requesting a recalibration check before deciding? Participant: I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward. Interviewer: What happened next? Participant: Re-entry went ahead. About twenty minutes later, the shift boss called me — one of the crew wanted to hold at the refuge chamber a few extra minutes before heading further in, just as a precaution. Nothing specific triggering it, more a gut feeling. Interviewer: What was your reasoning at that point? Participant: That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe. Interviewer: Was there anything in the data at that point pointing toward fire specifically? Participant: Not really, no. No smoke reports, no heat, and the secondary gas trends weren't showing anything unusual — CO2 was flat. Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed. I didn't want to be the one who waved people through if there was any chance it was something bigger. Interviewer: How did that play out? Participant: No fire indicators ever showed up. We eventually put it down to a longer-than-usual round that took a bit more time to clear than normal. The fifteen-minute hold turned out to be unnecessary, though nobody complained about the extra caution. Interviewer: Let's move to the threshold question. What came up there? Participant: Later that shift, the mine planning superintendent asked whether we should revise the CO auto-cutoff setpoint on GS-14R before ramping the LHD fleet back up fully. Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now. Interviewer: Did you have newer data available? Participant: We did, and it was actually pretty usable. The recent baseline surveys had shown ambient CO trending noticeably higher under current depth and fleet conditions — enough that during normal diesel-heavy periods we were regularly running close to or past the old setting without anything else flagging as hazardous. A couple of us had even talked informally about a materially higher interim figure being more realistic given those numbers. We hadn't done a formal re-baseline since the fleet expanded two years ago, but the recent surveys were solid enough to work from for an interim call. Interviewer: What did you decide? Participant: I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher. I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested. Interviewer: How did that work out afterward? Participant: Not great, if I'm honest. Over the following shifts the auto-cutoff started tripping more often during normal diesel-heavy periods — nothing hazardous, just operational friction, alarms going off during routine LHD movement. We've since talked about doing the full re-baseline properly. Interviewer: Last decision point — the incident closeout. Walk me through that. Participant: The safety officer wanted a closing narrative before full production resumed. By that point we had three things on the table: the sensor's drift history, the LHD fleet idling near the loading point during the relevant window, and the fact that the round itself ran a bit long. None of those had been tested individually — we hadn't isolated the sensor alone, or the fleet alone, to see which one actually explained the spike. Interviewer: How did you write it up? Participant: I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure. Mine planning was waiting on that closure to greenlight full resumption, so I didn't push for a separate follow-up test. Interviewer: Looking back, is there another explanation that fits those same facts just as well? Participant: In principle, sure — it could've leaned more on the fleet, or more on the clearance delay, and the sensor could've been almost incidental. We never separated them out to check. But at the time, the combined account was what went into the record, and it's what mine planning worked from. Interviewer: If the handheld reading that morning had come back much higher than the station reading, would your first call have changed? Participant: Probably, yes. If it had matched or exceeded the station number, I'd have taken it more seriously as a real hazard rather than sensor noise. Interviewer: And if you'd had time to run a full re-baseline before setting the threshold? Participant: I'd have set it higher, most likely, based on the newer survey data. Time was the constraint there, not confidence in the old number. Interviewer: How much would you say the schedule pressure from mine planning shaped your decisions that day? Participant: More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 4.32s · gen 224.04s · total 231.1s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0289 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0279 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0269 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0253 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0234 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0218 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0208 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0207 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0205 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0184 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0176 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
13. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0173 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
14. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0173 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0172 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0167 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0166 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
19. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0165 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
21. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0163 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
24. **Hallihan_etal_DTM_12.pdf** — 0.0155 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
26. **Lyell Automation bias and verification complexity.pdf** — 0.0154 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
27. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0153 (rrf) — _# Cognitive Biases Within Decision Making 475 Perception Attentiveness Comprehension Credibility_
28. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
30. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0151 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
32. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0147 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
34. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0146 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
35. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0146 (rrf) — _## Influence of Cognitive Biases in Distorting Decision Making and Leading to Critical Unfavorab_
36. **Lyell Automation bias and verification complexity.pdf** — 0.0145 (rrf) — _# # – – – – – – – – – – – ### ### – P ¼ .031 ### > .05 ## < .001 DDS ( 31 ) 29 general practi- M_
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0145 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
38. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0145 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
39. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0143 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
40. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0142 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
41. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
42. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0141 (rrf) — _[61\] or the Observer-Expectancy Effects On that note, are we, as ISR researchers, also cognitiv_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
47. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0139 (rrf) — _# 478 Fire Technology 2019 This classification process is intended to highlight how the cognitiv_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
49. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0138 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias The confidence bias originates _
50. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0137 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focused on the participant's reported reasoning during the initial CO reading interpretation, the precautionary hold, the setpoint revision, and the incident closeout. Retrieved corpus support was used where it directly addressed a mechanism."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 2
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
      "alternative_labels": ["Availability bias", "Recency effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to judge the likelihood or frequency of an event by the ease with which examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation of GS-14R CO reading and re-entry decision",
      "decision_point_description": "Evaluation of an elevated CO reading at GS-14R and the decision to proceed with re-entry.",
      "affected_reasoning_operation": "Causal attribution and probability judgment about whether the elevated CO reading indicated a sensor fault or a genuine gas hazard.",
      "bias_specific_mechanism": "Recent instances of false GS-14R spikes were easily recalled and salient, making a sensor fault feel more probable than a real gas hazard.",
      "manifestation_in_interview": "The participant immediately interpreted the elevated reading as another instance of the known station problem, citing two prior false spikes and the sharp telemetry pattern before fully weighing the contradictory handheld reading.",
      "effect_on_reasoning_or_decision": "It led the participant to treat the reading as probably a sensor issue and proceed with scheduled re-entry despite a handheld reading of 190 ppm and no confirmed maintenance fault.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again.",
          "evidence_explanation": "Shows prior false alarms came immediately to mind and shaped the participant's initial causal hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind.",
          "evidence_explanation": "Explicitly links the freshness and easy recall of prior events to the participant's judgment."
        }
      ],
      "correction_or_counterevidence": "A handheld multi-gas detector reading of 190 ppm was available and was logged, and no maintenance ticket had confirmed a sensor fault. The participant did not completely ignore the handheld reading, but discounted it.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved source supports the recency/ease-of-recall component of the availability heuristic; the full heuristic label is applied from general knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Supports the recency/ease-of-recall component that makes recent examples more cognitively available.",
          "relevance_to_this_occurrence": "The participant's two prior false alarms were recent and therefore readily recalled, supporting the availability component of the heuristic."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Confirmation heuristic", "Congeniality bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's prior beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Weighing GS-14R station reading against handheld multi-gas reading",
      "decision_point_description": "Deciding whether the elevated CO readings indicated a sensor fault or a genuine gas hazard.",
      "affected_reasoning_operation": "Evidence weighting and hypothesis evaluation.",
      "bias_specific_mechanism": "After forming the sensor-fault hypothesis, the participant gave more weight to the station's history and telemetry pattern while rationalizing away the disconfirming handheld reading as possible calibration drift.",
      "manifestation_in_interview": "The participant explicitly reports leaning on the station's history more than the handheld number and treating the lower handheld reading as less probative despite it still being well above baseline.",
      "effect_on_reasoning_or_decision": "It contributed to the decision to proceed with re-entry despite unresolved contradictory evidence and no maintenance ticket confirming a sensor fault.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned on the station's history more than the handheld number, honestly.",
          "evidence_explanation": "Directly shows selective weight favoring the prior sensor-fault hypothesis over a disconfirming reading."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have.",
          "evidence_explanation": "Demonstrates discounting of a contradictory data point through a plausible but unconfirmed alternative explanation."
        }
      ],
      "correction_or_counterevidence": "The handheld reading was not ignored entirely and was logged. The participant also acknowledges he did not weight it as heavily as he maybe should have.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved passages mention confirmation bias in aviation incident reports but do not provide a specific mechanism or definition; the label is applied from general knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias", "Salience bias", "Affect heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to judge the likelihood of an event by the ease with which scenarios or examples come to mind, particularly vivid or emotional ones.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hold at refuge chamber and partial fire-response protocol",
      "decision_point_description": "Decision whether to hold the crew at the refuge chamber and trigger a partial fire-response protocol in response to a precautionary request.",
      "affected_reasoning_operation": "Risk perception and probability judgment about a fire scenario.",
      "bias_specific_mechanism": "A recent vivid safety briefing about a fatal underground fire became easily recalled and inflated the subjective plausibility of a fire despite the absence of supporting data.",
      "manifestation_in_interview": "The participant explicitly says the fatality briefing was front and center and that a fire scenario felt more plausible than it should have given what the data showed.",
      "effect_on_reasoning_or_decision": "It led to a 15-minute hold and a partial fire-response protocol even though no fire indicators existed; the hold was later judged unnecessary.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me.",
          "evidence_explanation": "Shows the vivid, recent fatal fire case was easily recalled and emotionally salient."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed.",
          "evidence_explanation": "Explicitly ties the recalled briefing to an inflated perceived plausibility of fire."
        }
      ],
      "correction_or_counterevidence": "The participant noted no smoke, no heat, flat CO2, and that fume-clearance delays were far more common. The decision was later found to be unnecessary.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved source supports the recency component of availability; the full availability heuristic label is applied from general knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Supports the recency/ease-of-recall component that made the recent safety briefing highly accessible.",
          "relevance_to_this_occurrence": "The recent fatality briefing was more available in memory, which contributed to the participant treating fire as more plausible than the data supported."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": ["Anchoring bias", "Insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The heuristic of making estimates by starting from an initial value and then adjusting insufficiently from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Revision of CO auto-cutoff setpoint on GS-14R",
      "decision_point_description": "Deciding whether and how far to revise the GS-14R CO auto-cutoff setpoint based on newer baseline data.",
      "affected_reasoning_operation": "Numeric estimation and threshold setting.",
      "bias_specific_mechanism": "The existing commissioning value of 100 ppm served as an anchor; despite newer survey data indicating a materially higher threshold was justified, the participant made only a small adjustment and remained close to the original number.",
      "manifestation_in_interview": "The participant explicitly reports keeping the new setpoint close to the old commissioning figure because the original number had been through proper review and felt like the number to stay near, even though the newer data pointed higher.",
      "effect_on_reasoning_or_decision": "The setpoint remained too low, causing repeated nuisance auto-cutoffs during normal diesel-heavy periods and operational friction.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher.",
          "evidence_explanation": "Explicitly demonstrates insufficient adjustment from the original commissioning figure as the anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested.",
          "evidence_explanation": "Shows the original anchor dominated the newer evidence."
        }
      ],
      "correction_or_counterevidence": "The participant said that if he had had time to run a full re-baseline he probably would have set it higher, and he partly attributed the decision to time constraints rather than confidence in the old number. Later nuisance trips led to discussion of a proper re-baseline.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved source directly supports the anchoring-and-adjustment mechanism and its characteristic insufficient adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "Supports the mechanism of starting from an initial answer and making insufficient adjustments.",
          "relevance_to_this_occurrence": "The 100 ppm commissioning setpoint was the initial answer; the newer survey data called for adjustment, but the participant's adjustment was insufficient."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Narrative fallacy",
      "alternative_labels": ["Illusory correlation", "Causal coherence bias"],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Incident closeout causal explanation",
      "supporting_interview_quote": "I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure.",
      "plausible_mechanism": "Preference for a coherent, complete multi-cause account over unresolved uncertainty, leading to a causal narrative without isolating the contributing factors.",
      "why_not_identified": "The transcript shows a plausible story-construction pattern, but it does not clearly evidence a bias-specific mechanism distinguishable from legitimate report-writing under time pressure and incomplete information. The participant also explicitly acknowledges that the alternative explanations were never separated out."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a self-report; no independent sensor, maintenance, or gas-log data were available to verify the engineering facts.",
    "Schedule pressure and time constraints from mine planning were present and may compete as non-bias explanations for some decisions, especially the quick closure and the preference for keeping production moving.",
    "Retrieved corpus passages were sparse and in places OCR-noisy; availability heuristic and confirmation bias labels were applied primarily from general knowledge, with retrieved support only for the recency/anchoring components."
  ]
}

