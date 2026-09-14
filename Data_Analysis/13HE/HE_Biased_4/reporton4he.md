# RAG Benchmark — 2026-09-13

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'll ask you to walk me through a specific incident in detail, and there are no right or wrong answers. Everything's for internal learning purposes. Can you tell me your current role and how long you've been in it? Participant: Sure. I'm the ventilation engineer for the underground section — mainly responsible for the primary and auxiliary fan systems, the VOD setup, and gas monitoring across the active levels. I've been in this role about six years, underground ventilation for closer to eleven overall. Interviewer: Good. Let's start with the incident itself. What happened? Participant: This was during a shift where we had a scheduled production blast on 14 Level. Standard round, nothing unusual planned. About thirty minutes after blast clearance time, one of our gas stations — GS-14R, out in the return airway — started reading CO at 280 ppm. Baseline after a blast like that is usually under 50 ppm once the primary fan's had time to clear it. So that number stood out immediately. Interviewer: What went through your mind when you saw that? Participant: Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again. I pulled the telemetry log to check the trend, and it had spiked pretty sharply rather than climbing gradually, which is more consistent with a dust or particulate interference pattern than a genuine gas buildup, in my experience. Interviewer: Was there any other information available to you at that point? Participant: Yes — the gas monitoring technician had taken a handheld multi-gas detector reading out at the return airway around the same time, and that came back at 190 ppm. Lower than the station reading, but still well above baseline. No maintenance ticket had confirmed a fault on GS-14R yet either — that hadn't been checked this shift. Interviewer: How did you weigh those two numbers against each other? Participant: I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule. Interviewer: Did you consider getting a second confirmatory reading, or requesting a recalibration check before deciding? Participant: I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward. Interviewer: What happened next? Participant: Re-entry went ahead. About twenty minutes later, the shift boss called me — one of the crew wanted to hold at the refuge chamber a few extra minutes before heading further in, just as a precaution. Nothing specific triggering it, more a gut feeling. Interviewer: What was your reasoning at that point? Participant: That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe. Interviewer: Was there anything in the data at that point pointing toward fire specifically? Participant: Not really, no. No smoke reports, no heat, and the secondary gas trends weren't showing anything unusual — CO2 was flat. Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed. I didn't want to be the one who waved people through if there was any chance it was something bigger. Interviewer: How did that play out? Participant: No fire indicators ever showed up. We eventually put it down to a longer-than-usual round that took a bit more time to clear than normal. The fifteen-minute hold turned out to be unnecessary, though nobody complained about the extra caution. Interviewer: Let's move to the threshold question. What came up there? Participant: Later that shift, the mine planning superintendent asked whether we should revise the CO auto-cutoff setpoint on GS-14R before ramping the LHD fleet back up fully. Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now. Interviewer: Did you have newer data available? Participant: We did, and it was actually pretty usable. The recent baseline surveys had shown ambient CO trending noticeably higher under current depth and fleet conditions — enough that during normal diesel-heavy periods we were regularly running close to or past the old setting without anything else flagging as hazardous. A couple of us had even talked informally about a materially higher interim figure being more realistic given those numbers. We hadn't done a formal re-baseline since the fleet expanded two years ago, but the recent surveys were solid enough to work from for an interim call. Interviewer: What did you decide? Participant: I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher. I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested. Interviewer: How did that work out afterward? Participant: Not great, if I'm honest. Over the following shifts the auto-cutoff started tripping more often during normal diesel-heavy periods — nothing hazardous, just operational friction, alarms going off during routine LHD movement. We've since talked about doing the full re-baseline properly. Interviewer: Last decision point — the incident closeout. Walk me through that. Participant: The safety officer wanted a closing narrative before full production resumed. By that point we had three things on the table: the sensor's drift history, the LHD fleet idling near the loading point during the relevant window, and the fact that the round itself ran a bit long. None of those had been tested individually — we hadn't isolated the sensor alone, or the fleet alone, to see which one actually explained the spike. Interviewer: How did you write it up? Participant: I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure. Mine planning was waiting on that closure to greenlight full resumption, so I didn't push for a separate follow-up test. Interviewer: Looking back, is there another explanation that fits those same facts just as well? Participant: In principle, sure — it could've leaned more on the fleet, or more on the clearance delay, and the sensor could've been almost incidental. We never separated them out to check. But at the time, the combined account was what went into the record, and it's what mine planning worked from. Interviewer: If the handheld reading that morning had come back much higher than the station reading, would your first call have changed? Participant: Probably, yes. If it had matched or exceeded the station number, I'd have taken it more seriously as a real hazard rather than sensor noise. Interviewer: And if you'd had time to run a full re-baseline before setting the threshold? Participant: I'd have set it higher, most likely, based on the newer survey data. Time was the constraint there, not confidence in the old number. Interviewer: How much would you say the schedule pressure from mine planning shaped your decisions that day? Participant: More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.46s · gen 205.60s · total 211.8s_

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
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first review of the interview transcript for affirmatively evidenced cognitive biases. Retrieved corpus passages were used only where they supplied operational definitions, mechanism descriptions, or diagnostic validation."
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
      "bias_label": "narrative fallacy",
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
        "selective evidence weighting",
        "myside bias",
        "confirmatory bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or hypotheses, while underweighting contradictory evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation and re-entry decision after GS-14R CO spike",
      "decision_point_description": "Deciding whether the elevated CO readings indicated a genuine hazard or sensor interference, and whether to allow scheduled re-entry.",
      "affected_reasoning_operation": "Evidence weighting and diagnostic interpretation under uncertainty",
      "bias_specific_mechanism": "Prior belief that GS-14R was a nuisance sensor, based on previous false spikes, caused the participant to favor station history and the sharp-spike telemetry pattern as confirmatory while discounting the conflicting handheld reading of 190 ppm as likely calibration drift. This produced premature closure on a sensor-noise explanation.",
      "manifestation_in_interview": "The participant explicitly states that the station's history was fresh and that he leaned on it more than the handheld number. He did not obtain a second confirmatory reading or maintenance check before approving re-entry.",
      "effect_on_reasoning_or_decision": "Reduced the participant's weighting of the elevated handheld reading that conflicted with the sensor-fault hypothesis and supported moving forward with scheduled re-entry rather than delaying for verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again.",
          "evidence_explanation": "Shows activation of a prior sensor-fault expectation before full evaluation of the current evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule.",
          "evidence_explanation": "Explicitly documents selective weighting: the participant favored the history-consistent sensor-error hypothesis and discounted the elevated handheld reading, then made a consequential re-entry decision."
        }
      ],
      "correction_or_counterevidence": "The station did have a documented history of dust interference, and no maintenance check had yet confirmed a fault, so sensor error was a plausible hypothesis. The participant also logged the handheld reading rather than ignoring it, and later admitted he should have weighted it more.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support for confirmation bias was not provided in the retrieved passages; classification relies on established cognitive-science definitions.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "salience heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments of frequency or probability are influenced by the ease with which examples come to mind, so vivid or recent events are over-weighted in risk assessment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to hold crew at refuge chamber and partially trigger fire-response protocol",
      "decision_point_description": "Whether to grant or deny a precautionary hold when no fire-specific indicators were present.",
      "affected_reasoning_operation": "Subjective probability estimation and risk assessment of a fire scenario",
      "bias_specific_mechanism": "A recent vivid safety briefing about an underground fire fatality became cognitively available and elevated the perceived plausibility of a fire scenario, despite flat CO2, no smoke, no heat, and a known more common alternative explanation of fume-clearance delay.",
      "manifestation_in_interview": "The participant states that the fatality briefing was front and center when the hold request was raised, and that the briefing made a fire scenario feel more plausible than the current data actually showed.",
      "effect_on_reasoning_or_decision": "Increased caution and triggered partial fire-response protocols based on the recall of a vivid case rather than on current gas, heat, or smoke evidence; the hold later proved unnecessary.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe.",
          "evidence_explanation": "Shows a recent, emotionally vivid case becoming salient and directly shaping the decision to hold and trigger the fire protocol."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed. I didn't want to be the one who waved people through if there was any chance it was something bigger.",
          "evidence_explanation": "The participant explicitly acknowledges that the availability of the fire-fatality case distorted his subjective probability of a fire relative to the objective data."
        }
      ],
      "correction_or_counterevidence": "The hold was precautionary and low-cost, and acting cautiously on a crew's gut feeling under uncertainty can be reasonable. However, the participant explicitly attributes the elevated fire plausibility to the vivid briefing rather than to current data, and acknowledges the data did not support that scenario.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support for the availability heuristic was not provided in the retrieved passages; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring heuristic",
        "anchor and insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The heuristic of making an estimate by starting from an initial value or reference point and adjusting insufficiently, even when new information indicates that a larger adjustment is warranted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Revision of GS-14R CO auto-cutoff setpoint",
      "decision_point_description": "Whether to raise the CO auto-cutoff setpoint based on newer baseline surveys and current fleet/depth conditions, and by how much.",
      "affected_reasoning_operation": "Quantitative threshold estimation and adjustment of a safety-related automatic cutoff",
      "bias_specific_mechanism": "The original commissioning value of 100 ppm served as an anchor. Recent surveys and operational experience suggested materially higher values, but the participant made only a minor adjustment and treated the original figure as basically sound rather than moving toward the interim value indicated by the newer data.",
      "manifestation_in_interview": "The participant acknowledged that newer baseline data supported a higher setting, but he stayed close to the original reviewed figure, producing repeated operational trips during normal diesel-heavy periods.",
      "effect_on_reasoning_or_decision": "The setpoint remained too low for current operating conditions, causing increased alarms and operational friction during routine LHD movement.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now.",
          "evidence_explanation": "Identifies the original anchor value and acknowledges that operating conditions had changed materially."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher. I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested.",
          "evidence_explanation": "Shows insufficient adjustment from the anchoring value despite acknowledging that newer data pointed toward a higher figure."
        }
      ],
      "correction_or_counterevidence": "The participant cited time pressure and lack of a formal re-baseline as reasons for not adopting the higher interim value, and he later stated that with time he would have set it higher. These are partial non-bias constraints, but the recent surveys were described as usable for an interim call, and the decision to remain near the anchor rather than make a larger interim adjustment is consistent with insufficient adjustment.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus contained a dedicated description of anchoring and adjustment, directly supporting the mechanism of insufficient adjustment from an initial value.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Anchoring and Adjustment  The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.” [16]",
          "mechanism_supported_by_source": "The source describes anchoring and adjustment as insufficient adjustment from an initial value when additional information is available.",
          "relevance_to_this_occurrence": "Matches the participant retaining the 100 ppm commissioning threshold as the base value and making only a small adjustment despite newer data indicating a higher setting."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "narrative fallacy",
      "alternative_labels": [
        "coherence bias",
        "story bias",
        "explanatory coherence bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to create or accept a coherent explanatory narrative from available facts and to overestimate its completeness or likelihood, even when alternative causal accounts are not ruled out.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Incident closeout causal explanation",
      "decision_point_description": "Writing the closing narrative and operative cause for the gas spike before full production resumed.",
      "affected_reasoning_operation": "Causal attribution and explanatory closure under uncertainty",
      "bias_specific_mechanism": "The participant combined three untested candidate causes into a single clean, complete composite account that covered all logged facts, and treated that composite as the operative cause without isolating or testing any individual factor.",
      "manifestation_in_interview": "He acknowledged that each possible factor was untested and that another explanation could fit the same facts equally well, but the combined narrative was adopted because it read as clean and complete and because mine planning needed closure.",
      "effect_on_reasoning_or_decision": "Produced a causally overconfident closure narrative that guided production resumption, without follow-up testing to discriminate among the candidate causes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure.",
          "evidence_explanation": "Shows narrative completeness and coherence being used as the basis for an operative cause despite the components being untested."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In principle, sure — it could've leaned more on the fleet, or more on the clearance delay, and the sensor could've been almost incidental. We never separated them out to check. But at the time, the combined account was what went into the record, and it's what mine planning worked from.",
          "evidence_explanation": "Acknowledges that alternative accounts fit the same facts and no isolation testing was performed, indicating overconfidence in the composite narrative."
        }
      ],
      "correction_or_counterevidence": "Time and production pressure for closure, and a practical need to provide an explanatory account with available information, partially explain the behavior. The bias is the subjective certainty derived from narrative coherence despite explicitly recognizing untested competing explanations.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support for narrative fallacy was not provided in the retrieved passages; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation error",
        "get-there-itis",
        "continuation bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial re-entry go/no-go decision and later schedule-pressure decisions",
      "supporting_interview_quote": "I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward.",
      "plausible_mechanism": "Production schedule pressure and the original plan to resume re-entry may have biased the participant toward continuing the planned sequence while downplaying ambiguous hazard information.",
      "why_not_identified": "The transcript does not clearly separate this from the confirmation bias in interpreting the readings or from ordinary organizational/time-pressure constraints. The participant's explicit final statement about schedule pressure is global rather than tied to a discrete bias-specific distortion in a single decision."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview transcript is a single retrospective self-report; participant memory and self-presentation may affect evidence quality.",
    "The retrieved corpus is limited and mostly aviation/automation-focused; several classified biases rely on general cognitive-science knowledge rather than retrieved passages.",
    "Some episodes contain overlapping pressures such as production schedule, time constraints, and sensor history, making it difficult to isolate single mechanisms.",
    "Confidence levels reflect the strength of transcript evidence, but causal field judgments are inherently inferential."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'll ask you to walk me through a specific incident in detail, and there are no right or wrong answers. Everything's for internal learning purposes. Can you tell me your current role and how long you've been in it? Participant: Sure. I'm the ventilation engineer for the underground section — mainly responsible for the primary and auxiliary fan systems, the VOD setup, and gas monitoring across the active levels. I've been in this role about six years, underground ventilation for closer to eleven overall. Interviewer: Good. Let's start with the incident itself. What happened? Participant: This was during a shift where we had a scheduled production blast on 14 Level. Standard round, nothing unusual planned. About thirty minutes after blast clearance time, one of our gas stations — GS-14R, out in the return airway — started reading CO at 280 ppm. Baseline after a blast like that is usually under 50 ppm once the primary fan's had time to clear it. So that number stood out immediately. Interviewer: What went through your mind when you saw that? Participant: Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again. I pulled the telemetry log to check the trend, and it had spiked pretty sharply rather than climbing gradually, which is more consistent with a dust or particulate interference pattern than a genuine gas buildup, in my experience. Interviewer: Was there any other information available to you at that point? Participant: Yes — the gas monitoring technician had taken a handheld multi-gas detector reading out at the return airway around the same time, and that came back at 190 ppm. Lower than the station reading, but still well above baseline. No maintenance ticket had confirmed a fault on GS-14R yet either — that hadn't been checked this shift. Interviewer: How did you weigh those two numbers against each other? Participant: I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule. Interviewer: Did you consider getting a second confirmatory reading, or requesting a recalibration check before deciding? Participant: I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward. Interviewer: What happened next? Participant: Re-entry went ahead. About twenty minutes later, the shift boss called me — one of the crew wanted to hold at the refuge chamber a few extra minutes before heading further in, just as a precaution. Nothing specific triggering it, more a gut feeling. Interviewer: What was your reasoning at that point? Participant: That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe. Interviewer: Was there anything in the data at that point pointing toward fire specifically? Participant: Not really, no. No smoke reports, no heat, and the secondary gas trends weren't showing anything unusual — CO2 was flat. Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed. I didn't want to be the one who waved people through if there was any chance it was something bigger. Interviewer: How did that play out? Participant: No fire indicators ever showed up. We eventually put it down to a longer-than-usual round that took a bit more time to clear than normal. The fifteen-minute hold turned out to be unnecessary, though nobody complained about the extra caution. Interviewer: Let's move to the threshold question. What came up there? Participant: Later that shift, the mine planning superintendent asked whether we should revise the CO auto-cutoff setpoint on GS-14R before ramping the LHD fleet back up fully. Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now. Interviewer: Did you have newer data available? Participant: We did, and it was actually pretty usable. The recent baseline surveys had shown ambient CO trending noticeably higher under current depth and fleet conditions — enough that during normal diesel-heavy periods we were regularly running close to or past the old setting without anything else flagging as hazardous. A couple of us had even talked informally about a materially higher interim figure being more realistic given those numbers. We hadn't done a formal re-baseline since the fleet expanded two years ago, but the recent surveys were solid enough to work from for an interim call. Interviewer: What did you decide? Participant: I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher. I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested. Interviewer: How did that work out afterward? Participant: Not great, if I'm honest. Over the following shifts the auto-cutoff started tripping more often during normal diesel-heavy periods — nothing hazardous, just operational friction, alarms going off during routine LHD movement. We've since talked about doing the full re-baseline properly. Interviewer: Last decision point — the incident closeout. Walk me through that. Participant: The safety officer wanted a closing narrative before full production resumed. By that point we had three things on the table: the sensor's drift history, the LHD fleet idling near the loading point during the relevant window, and the fact that the round itself ran a bit long. None of those had been tested individually — we hadn't isolated the sensor alone, or the fleet alone, to see which one actually explained the spike. Interviewer: How did you write it up? Participant: I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure. Mine planning was waiting on that closure to greenlight full resumption, so I didn't push for a separate follow-up test. Interviewer: Looking back, is there another explanation that fits those same facts just as well? Participant: In principle, sure — it could've leaned more on the fleet, or more on the clearance delay, and the sensor could've been almost incidental. We never separated them out to check. But at the time, the combined account was what went into the record, and it's what mine planning worked from. Interviewer: If the handheld reading that morning had come back much higher than the station reading, would your first call have changed? Participant: Probably, yes. If it had matched or exceeded the station number, I'd have taken it more seriously as a real hazard rather than sensor noise. Interviewer: And if you'd had time to run a full re-baseline before setting the threshold? Participant: I'd have set it higher, most likely, based on the newer survey data. Time was the constraint there, not confidence in the old number. Interviewer: How much would you say the schedule pressure from mine planning shaped your decisions that day? Participant: More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.06s · gen 197.00s · total 201.5s_

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
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a single interview transcript for cognitive-bias occurrences, using retrieved corpus passages where available and general cognitive-science knowledge where disclosed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring bias",
        "anchoring-and-adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to begin with an initial anchor or starting point and then adjust from it based on additional information, with the adjustment typically being insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting the elevated GS-14R CO reading and deciding whether to proceed with re-entry",
      "decision_point_description": "Whether the 280 ppm station reading indicated a real gas hazard or a sensor artifact, and whether re-entry should proceed on schedule.",
      "affected_reasoning_operation": "Causal diagnosis and information weighting",
      "bias_specific_mechanism": "The participant anchored on the station's prior false-alarm history as the likely explanation for the elevated reading and adjusted insufficiently away from that initial sensor-fault hypothesis when the handheld reading came back at 190 ppm, a value still well above baseline.",
      "manifestation_in_interview": "The participant explicitly said he leaned on the station's history more than the handheld number and that he did not weight the handheld reading as heavily as he perhaps should have.",
      "effect_on_reasoning_or_decision": "He concluded the reading was probably another sensor issue and allowed re-entry to proceed on schedule rather than seeking confirmatory testing or delaying the re-entry.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again.",
          "evidence_explanation": "This shows the initial anchor: the station's recent history immediately supplied the sensor-fault hypothesis before other information was fully weighed."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule.",
          "evidence_explanation": "This quote directly demonstrates anchoring and insufficient adjustment: the prior history served as the starting point, and the contradictory but still elevated handheld reading was under-weighted."
        }
      ],
      "correction_or_counterevidence": "The handheld reading was lower than the station reading but still well above baseline, which meant some caution remained warranted. Schedule pressure was also mentioned, but the participant's own description supports an anchoring mechanism in the interpretation of the readings.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus provides a definition and mechanism for the anchoring-and-adjustment heuristic and notes that the phenomenon generalizes beyond numerical estimates.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Anchoring and Adjustment: people make estimates based on an initial answer, and adjustments from there based on additional information are typically insufficient; the phenomenon has been found to hold in more general cases beyond numerical estimates.",
          "mechanism_supported_by_source": "Initial anchor plus insufficient adjustment from additional information.",
          "relevance_to_this_occurrence": "The participant's initial sensor-fault hypothesis from station history served as the anchor, and the 190 ppm handheld reading was additional information that did not produce sufficient adjustment away from that anchor."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "recency effect",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or plausibility of an event by the ease with which instances or similar events come to mind, so that recent, vivid, or emotionally salient events are over-weighted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Responding to the shift boss's request to hold crew at the refuge chamber",
      "decision_point_description": "Whether to hold crew and partially trigger the fire-response protocol despite no fire-specific data.",
      "affected_reasoning_operation": "Probability and plausibility judgment about fire versus routine fume-clearance delay",
      "bias_specific_mechanism": "A recent, emotionally vivid safety briefing about a fatal underground fire remained highly accessible in memory and inflated the subjective plausibility of a fire scenario, even though site-specific data did not indicate fire and the participant knew fume-clearance delay was a more common explanation.",
      "manifestation_in_interview": "The participant said the fire briefing 'stuck with me' and was 'front and center,' and acknowledged that a fire scenario felt more plausible than it probably should have given the actual data.",
      "effect_on_reasoning_or_decision": "He approved the hold request and partially triggered the fire-response protocol as a precaution despite no smoke, no heat, and flat secondary gas readings.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe.",
          "evidence_explanation": "The recent vivid briefing increased the mental accessibility of a fire scenario and directly influenced the decision to hold crew and trigger the fire-response protocol."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. No smoke reports, no heat, and the secondary gas trends weren't showing anything unusual — CO2 was flat. Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed.",
          "evidence_explanation": "This explicitly contrasts the data with the participant's subjective plausibility judgment, confirming that memory accessibility from the recent briefing outweighed the objective site data."
        }
      ],
      "correction_or_counterevidence": "The participant accurately noted the absence of smoke, heat, and abnormal secondary gas trends, and acknowledged that fume-clearance delay was more common. The extra caution was not unreasonable, but the stated shift in plausibility indicates availability-based over-weighting.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus provided only partial support: a passage describes the recency effect, or the tendency to remember recent events more clearly. The full availability-probability mechanism label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Enhanced recall of recent events increases their mental accessibility.",
          "relevance_to_this_occurrence": "The recent fatal-fire briefing was more accessible in memory and therefore over-influenced the participant's judgment about the fire scenario."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring bias",
        "anchoring-and-adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to begin with an initial anchor or starting point and then adjust from it based on additional information, with the adjustment typically being insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Revising the CO auto-cutoff setpoint on GS-14R",
      "decision_point_description": "Whether to raise the CO auto-cutoff threshold from the old commissioning value of 100 ppm toward the level suggested by newer baseline surveys.",
      "affected_reasoning_operation": "Threshold and numeric estimate revision",
      "bias_specific_mechanism": "The original commissioning value of 100 ppm served as an anchor; despite usable newer survey data suggesting a materially higher interim threshold, the participant made only a small adjustment and treated the old number as essentially sound.",
      "manifestation_in_interview": "The participant said the commissioning number 'just felt like the number to stay near' and that he made a small adjustment but largely kept the setpoint close to the original figure despite newer data pointing higher.",
      "effect_on_reasoning_or_decision": "The setpoint remained close to 100 ppm, later causing operational friction through frequent auto-cutoff trips during normal diesel-heavy periods and delaying a fuller re-baselining.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now.",
          "evidence_explanation": "This establishes the original threshold as the anchor, even though its original conditions were acknowledged to be outdated."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher.",
          "evidence_explanation": "This shows insufficient adjustment from the original commissioning anchor despite newer information suggesting a larger change was appropriate."
        }
      ],
      "correction_or_counterevidence": "The participant stated later that if he had had time to run a full re-baseline he would have set the threshold higher, and that time was the constraint rather than confidence in the old number. This introduces time pressure as a competing or contributing explanation, so confidence is moderate rather than high.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus provides a definition and mechanism for anchoring-and-adjustment and supports its application beyond purely numerical contexts.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Anchoring and Adjustment: people make estimates based on an initial answer, and adjustments from there based on additional information are typically insufficient; the phenomenon has been found to hold in more general cases beyond numerical estimates.",
          "mechanism_supported_by_source": "Initial anchor plus insufficient adjustment from additional information.",
          "relevance_to_this_occurrence": "The original commissioning value anchored the threshold revision, and the newer survey data did not produce a sufficient adjustment away from that anchor."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "narrative fallacy",
      "alternative_labels": [
        "conjunction fallacy",
        "coherence bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Incident closeout causal explanation",
      "supporting_interview_quote": "I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure.",
      "plausible_mechanism": "A coherent multi-cause narrative was preferred over an untested, isolated-cause account; the attractiveness of a complete story may have substituted for empirical separation of the three factors.",
      "why_not_identified": "The interview suggests a possible coherence or story preference, but the decision to avoid follow-up testing is also strongly tied to closure and time pressure. In addition, no corpus support for this label was available, and the mechanism is plausible but not affirmatively isolated."
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
      "possible_decision_episode_label": "Proceeding with re-entry after anomalous CO reading",
      "supporting_interview_quote": "delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward.",
      "plausible_mechanism": "Commitment to the original re-entry schedule may have biased acceptance of the sensor-fault explanation and reduced willingness to wait for confirmation.",
      "why_not_identified": "The behavior overlaps substantially with the anchoring-and-adjustment interpretation and is partly attributable to mine-schedule pressure; a distinct plan-continuation mechanism is not clearly separated in the interview."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages are limited and sometimes provide only label-level or partial support; some mechanisms rely on general cognitive-science knowledge disclosed in corpus_support_note.",
    "Single-interview analysis cannot determine base rates or normative correctness of the participant's judgments.",
    "Time pressure and organizational constraints are present and may compete with cognitive-bias explanations for some decisions.",
    "Findings are based on the participant's retrospective report, not direct observation of real-time cognition."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'll ask you to walk me through a specific incident in detail, and there are no right or wrong answers. Everything's for internal learning purposes. Can you tell me your current role and how long you've been in it? Participant: Sure. I'm the ventilation engineer for the underground section — mainly responsible for the primary and auxiliary fan systems, the VOD setup, and gas monitoring across the active levels. I've been in this role about six years, underground ventilation for closer to eleven overall. Interviewer: Good. Let's start with the incident itself. What happened? Participant: This was during a shift where we had a scheduled production blast on 14 Level. Standard round, nothing unusual planned. About thirty minutes after blast clearance time, one of our gas stations — GS-14R, out in the return airway — started reading CO at 280 ppm. Baseline after a blast like that is usually under 50 ppm once the primary fan's had time to clear it. So that number stood out immediately. Interviewer: What went through your mind when you saw that? Participant: Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again. I pulled the telemetry log to check the trend, and it had spiked pretty sharply rather than climbing gradually, which is more consistent with a dust or particulate interference pattern than a genuine gas buildup, in my experience. Interviewer: Was there any other information available to you at that point? Participant: Yes — the gas monitoring technician had taken a handheld multi-gas detector reading out at the return airway around the same time, and that came back at 190 ppm. Lower than the station reading, but still well above baseline. No maintenance ticket had confirmed a fault on GS-14R yet either — that hadn't been checked this shift. Interviewer: How did you weigh those two numbers against each other? Participant: I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule. Interviewer: Did you consider getting a second confirmatory reading, or requesting a recalibration check before deciding? Participant: I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward. Interviewer: What happened next? Participant: Re-entry went ahead. About twenty minutes later, the shift boss called me — one of the crew wanted to hold at the refuge chamber a few extra minutes before heading further in, just as a precaution. Nothing specific triggering it, more a gut feeling. Interviewer: What was your reasoning at that point? Participant: That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe. Interviewer: Was there anything in the data at that point pointing toward fire specifically? Participant: Not really, no. No smoke reports, no heat, and the secondary gas trends weren't showing anything unusual — CO2 was flat. Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed. I didn't want to be the one who waved people through if there was any chance it was something bigger. Interviewer: How did that play out? Participant: No fire indicators ever showed up. We eventually put it down to a longer-than-usual round that took a bit more time to clear than normal. The fifteen-minute hold turned out to be unnecessary, though nobody complained about the extra caution. Interviewer: Let's move to the threshold question. What came up there? Participant: Later that shift, the mine planning superintendent asked whether we should revise the CO auto-cutoff setpoint on GS-14R before ramping the LHD fleet back up fully. Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now. Interviewer: Did you have newer data available? Participant: We did, and it was actually pretty usable. The recent baseline surveys had shown ambient CO trending noticeably higher under current depth and fleet conditions — enough that during normal diesel-heavy periods we were regularly running close to or past the old setting without anything else flagging as hazardous. A couple of us had even talked informally about a materially higher interim figure being more realistic given those numbers. We hadn't done a formal re-baseline since the fleet expanded two years ago, but the recent surveys were solid enough to work from for an interim call. Interviewer: What did you decide? Participant: I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher. I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested. Interviewer: How did that work out afterward? Participant: Not great, if I'm honest. Over the following shifts the auto-cutoff started tripping more often during normal diesel-heavy periods — nothing hazardous, just operational friction, alarms going off during routine LHD movement. We've since talked about doing the full re-baseline properly. Interviewer: Last decision point — the incident closeout. Walk me through that. Participant: The safety officer wanted a closing narrative before full production resumed. By that point we had three things on the table: the sensor's drift history, the LHD fleet idling near the loading point during the relevant window, and the fact that the round itself ran a bit long. None of those had been tested individually — we hadn't isolated the sensor alone, or the fleet alone, to see which one actually explained the spike. Interviewer: How did you write it up? Participant: I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure. Mine planning was waiting on that closure to greenlight full resumption, so I didn't push for a separate follow-up test. Interviewer: Looking back, is there another explanation that fits those same facts just as well? Participant: In principle, sure — it could've leaned more on the fleet, or more on the clearance delay, and the sensor could've been almost incidental. We never separated them out to check. But at the time, the combined account was what went into the record, and it's what mine planning worked from. Interviewer: If the handheld reading that morning had come back much higher than the station reading, would your first call have changed? Participant: Probably, yes. If it had matched or exceeded the station number, I'd have taken it more seriously as a real hazard rather than sensor noise. Interviewer: And if you'd had time to run a full re-baseline before setting the threshold? Participant: I'd have set it higher, most likely, based on the newer survey data. Time was the constraint there, not confidence in the old number. Interviewer: How much would you say the schedule pressure from mine planning shaped your decisions that day? Participant: More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.04s · gen 210.34s · total 214.8s_

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
    "analysis_scope_note": "Analysis restricted to affirmative transcript evidence of bias-specific mechanisms. Operational time/schedule pressure was not classified as bias unless a distinct cognitive mechanism was separately evidenced."
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
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory bias", "positive test bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and weight information in ways that confirm an existing hypothesis or belief while underweighting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of elevated CO reading at GS-14R and re-entry decision",
      "decision_point_description": "Whether to treat the 280 ppm GS-14R CO reading as a sensor anomaly and proceed with re-entry on schedule.",
      "affected_reasoning_operation": "Hypothesis-guided weighting and interpretation of gas-monitoring evidence",
      "bias_specific_mechanism": "The participant formed an early sensor-error hypothesis from station history, interpreted the telemetry spike as consistent with dust/particulate interference, and discounted the still-elevated handheld reading by invoking possible calibration drift instead of obtaining a confirmatory check or maintenance verification.",
      "manifestation_in_interview": "The participant reported initially thinking 'that station again,' then differentially weighed the station history over the 190 ppm handheld reading, explicitly saying he did not weight the handheld as heavily as he should have.",
      "effect_on_reasoning_or_decision": "It permitted re-entry on schedule instead of treating the elevated readings as a potential gas hazard requiring further verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again.",
          "evidence_explanation": "Shows an initial sensor-error hypothesis was formed from prior station-specific experience before full evaluation of current gas data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I pulled the telemetry log to check the trend, and it had spiked pretty sharply rather than climbing gradually, which is more consistent with a dust or particulate interference pattern than a genuine gas buildup, in my experience.",
          "evidence_explanation": "Demonstrates hypothesis-consistent interpretation of ambiguous trend information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have.",
          "evidence_explanation": "Directly shows differential weighting favoring the prior sensor-error belief and discounting a still-above-baseline disconfirming reading."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule.",
          "evidence_explanation": "Links the biased interpretation to the re-entry decision."
        }
      ],
      "correction_or_counterevidence": "The handheld reading remained well above baseline at 190 ppm, and no maintenance ticket had confirmed a GS-14R fault that shift, so disconfirming data were available but not given decision-altering weight. The participant later acknowledged he 'didn't weight it as heavily as maybe I should have,' though this was retrospective.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a mechanism-level definition of confirmation bias; the label is applied from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or importance of an event by the ease with which salient instances come to mind, rather than by base rates or current evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to hold crew at the refuge chamber and partially trigger fire-response protocol",
      "decision_point_description": "Whether to grant the precautionary hold request and partly trigger fire-response despite no fire-specific data.",
      "affected_reasoning_operation": "Probability estimation of a possible underground fire",
      "bias_specific_mechanism": "A recent emotionally salient safety-briefing fatality involving delayed fire detection was highly available and inflated the subjective plausibility of a fire scenario, leading to a fire-response decision even though current gas trends did not indicate fire and the participant knew fume-clearance delay was far more common.",
      "manifestation_in_interview": "The participant stated that the prior fire fatality case 'was sort of front and center' and that a fire scenario felt more plausible than warranted by the data while acknowledging fume-clearance delays were the far more common explanation.",
      "effect_on_reasoning_or_decision": "It produced a precautionary hold and partial fire-response protocol activation; no fire indicators appeared and the hold was later deemed unnecessary.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me.",
          "evidence_explanation": "Identifies the salient prior case that became easily available in memory."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe.",
          "evidence_explanation": "Directly links the available prior case to the precautionary fire-response decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed.",
          "evidence_explanation": "Shows the participant knowingly overweighed the salient fire case relative to the base-rate/fume-clearance explanation and current data."
        }
      ],
      "correction_or_counterevidence": "Current data did not specifically indicate fire: no smoke, no heat, flat CO2. The outcome showed no fire indicators and the hold was unnecessary.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a definition or mechanism-level support for the availability heuristic; the label is applied from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value or reference point and to make insufficient adjustments away from it when new information warrants a larger change.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Revision of GS-14R CO auto-cutoff setpoint",
      "decision_point_description": "Whether to keep the CO auto-cutoff threshold close to the original 100 ppm commissioning setpoint or adjust it toward the materially higher level supported by recent baseline surveys.",
      "affected_reasoning_operation": "Numerical threshold estimation and adjustment from an established reference value",
      "bias_specific_mechanism": "The original 100 ppm commissioning setpoint served as an anchor; although recent baseline surveys supported a materially higher interim threshold, the participant made only a small adjustment and treated the original reviewed value as basically sound instead of adjusting sufficiently.",
      "manifestation_in_interview": "The participant said the commissioning number 'felt like the number to stay near' and that he treated the existing figure as sound with a minor tweak rather than moving it to where the interim numbers suggested.",
      "effect_on_reasoning_or_decision": "The threshold remained too low for current depth/fleet conditions, causing recurring operational trips during normal diesel-heavy periods and delaying an appropriate re-baseline.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now.",
          "evidence_explanation": "Identifies the original numeric anchor and its outdated basis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The recent baseline surveys had shown ambient CO trending noticeably higher under current depth and fleet conditions — enough that during normal diesel-heavy periods we were regularly running close to or past the old setting without anything else flagging as hazardous.",
          "evidence_explanation": "Shows that newer data justified a larger adjustment away from the anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher.",
          "evidence_explanation": "Demonstrates the anchor retaining influence despite discrepant evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested.",
          "evidence_explanation": "Shows insufficient adjustment from the initial anchor in the actual threshold decision."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the outcome was 'not great,' and that recent baseline data had supported a materially higher figure; a proper re-baseline was later considered.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from the space-flight systems paper explicitly describes anchoring and adjustment and insufficient adjustment from an initial value.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.” [16]",
          "mechanism_supported_by_source": "Anchoring and adjustment: initial values affect estimates, and adjustments from them are typically insufficient.",
          "relevance_to_this_occurrence": "The participant's retention of the old 100 ppm commissioning threshold, with only a minor tweak despite newer data, matches this insufficient-adjustment pattern."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "narrative fallacy",
      "alternative_labels": ["coherence bias", "story bias"],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Incident closeout causal narrative",
      "supporting_interview_quote": "I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure.",
      "plausible_mechanism": "A coherent, complete causal narrative may have increased confidence in an untested combined explanation and reduced the perceived need for follow-up isolation tests.",
      "why_not_identified": "Not identified because the transcript also gives schedule pressure and closure requirements as plausible non-bias reasons for not pursuing separate follow-up testing; no distinct coherence-driven mechanism is unequivocally evidenced."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis"],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision to proceed with scheduled re-entry after discrepant CO readings",
      "supporting_interview_quote": "I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule.",
      "plausible_mechanism": "A bias toward continuing the planned re-entry despite unresolved discrepancy between fixed and handheld readings.",
      "why_not_identified": "Not identified because the participant's sensor-error interpretation provides an evidence-based rationale for continuation; the transcript does not clearly show a distinct plan-continuation mechanism independent of that interpretation."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus snippets are sparse and partly garbled; several established bias labels rely on general cognitive-science knowledge rather than retrieved corpus support.",
    "Schedule pressure from mine planning is present as a competing operational explanation for some decisions and was not classified as bias unless a distinct cognitive mechanism was shown.",
    "The transcript is a single retrospective account, so some causal links between reported thought processes and actual decisions may be reconstructed."
  ]
}

