# RAG Benchmark — 2026-09-13

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief for our exercise-design case-study library — I'll be asking about a specific project you led, how the decisions actually unfolded, not whether they were 'right' in hindsight. Everything stays de-identified. Sound okay? Participant: Sure, happy to walk through it. This is the Riverbend Rising full-scale exercise, right? That one's still pretty fresh for me. Interviewer: Exactly. Can you start by describing the assignment and what success would've looked like? Participant: I was handed the FSE build in early spring — simulate a levee failure and flash-flood evacuation, get it HSEEP-compliant, and use it to validate EOC escalation procedures before the seasonal flood window opened. Success meant a full exercise day, a usable Controller-Evaluator handbook, and an AAR that actually told the Director something new about our capability gaps. Interviewer: Give me the incident account — how did the project actually go, start to finish? Participant: We'd run something similar back in 2019 — smaller footprint, two of us on it, and we mostly reused an existing scenario shell. That one took about six weeks start to finish. This time I was solo, and the scope was bigger: a brand-new levee-failure module built off updated Army Corps dam-break modeling, plus coordination across the regional EOC, the school district, and municipal police and fire. Deadline was fixed at ten weeks because of the flood-risk calendar. I scoped the build assuming it'd track pretty close to the 2019 timeline — figured I knew the process well enough to move fast. About four weeks in, I was still building the custom hydrology module and waiting on sign-off from three different agencies, and a status check showed we'd already slipped two weeks. From there it became a scramble — severity calibration with the advisory committee, a fight over which training injects we could actually finish, and a last push on the handbook right up against the deadline. Interviewer: Let's reconstruct that chronologically. What did you know at each stage, and what changed as you learned more? Participant: At kickoff I had the 2019 numbers in my head and the new Corps data in hand, but I hadn't yet mapped out how much longer three-agency coordination would take versus one shell reused solo. Once the schedule slipped, I knew severity calibration and the advisory committee conversation were coming up next, and I could already tell we wouldn't have time to fully build every kind of training material — so the inject decision became a resource fight. By the time I got to the handbook, the clock was the dominant fact. Interviewer: Let's slow down on the first real decision — scoping the build timeline. Walk me through it. Participant: Right, so going in, I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much. I remember telling the Director I could deliver in the same general window even though I was down to one person and building the hydrology piece essentially from scratch. Interviewer: What made you confident the compressed schedule would hold? Participant: Honestly, mostly that I'd done a version of this before and it worked out then. I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead. Interviewer: What information would have changed that estimate? Participant: If I'd actually broken out hours for three-agency sign-off separately instead of folding it into 'coordination,' I probably would've padded the schedule more. I didn't do that breakdown until after the slip showed up. Interviewer: Still in that same phase — you also had a choice about which scenario format to build from. What drove that? Participant: Yeah, there was a newer modular design format some of the stakeholders floated, supposedly better suited to multi-agency exercises. But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in. Interviewer: Did you compare how the two formats actually performed for training outcomes? Participant: Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure. Interviewer: Let's move to the severity decision. What was on the table? Participant: The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years. There was real pressure to keep the scenario grounded in something the community would find plausible. Interviewer: How did you weigh the modeling against that history? Participant: I ended up scaling the peak severity down toward the more familiar flood level. The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face. Interviewer: Around that same time, you were part of an AAR review for a peer's exercise. What happened there? Participant: Right, a planner in another county got flagged for an unrealistically mild scenario — didn't stress escalation procedures at all. In that discussion I was pretty clear it looked like a planning gap on their end. I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time. Interviewer: Did you apply the same scrutiny to your own severity choice that you applied to theirs? Participant: Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard. Interviewer: Third decision point — the training injects. What were the options? Participant: We only had production time to fully build one category. Option one was photo and video clips of levee overtopping — dramatic, but slow to produce. Option two was the data packages — stream gauge readouts, GIS flow-rate shapefiles — less visually interesting but more specific for EOC modeling decisions. Interviewer: Which did you prioritize, and why? Participant: I put most of the remaining time into the photo and video injects. Past surveys showed people remember those vividly — I figured that made them the more effective training tool. Interviewer: Did you weigh how well each format supported the actual operational decisions evaluators would need to make? Participant: Less than I probably should have, in retrospect. The reasoning at the time was really centered on impact and recall, not on whether the flow-rate specifics would be there when people needed them. Interviewer: Last decision point — the Controller-Evaluator handbook. What went into that? Participant: I've been doing this fifteen years, and I've used the same shorthand and scoring conventions across a lot of exercises. Time was short, so I kept the handbook concise — standard terminology, no glossary. Interviewer: Was there any indication a glossary might be needed? Participant: There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left. Interviewer: Looking back across all four decisions — if you'd had two more weeks, what would you have done differently? Participant: Probably built in a real contingency buffer up front instead of assuming the old timeline would hold, and maybe split production time more evenly between the visual and data injects. Interviewer: And if a different planner had taken over halfway through? Participant: They might have pushed harder on the severity call, given the modeling was pretty clear. And they might not have carried the same assumptions I had about what 'obvious' means in the handbook, since they wouldn't have fifteen years of the same habits behind them. Interviewer: Anything you'd flag as uncertain even now? Participant: Whether the milder scenario actually undercut the escalation testing, or whether it was just a rough exercise day for other reasons — I genuinely don't know. Same with the handbook; the scoring inconsistencies could've come from a dozen things, not just the shorthand. Interviewer: That's a good place to stop. Thanks for the detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.22s · gen 147.03s · total 152.1s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0288 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0270 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
3. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0246 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0240 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0236 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0221 (rrf) — _We embedded behavioral measures in all three of our games to assess shortand longterm effects an_
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0219 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0203 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0201 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0199 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0191 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0190 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **Hallihan_etal_DTM_12.pdf** — 0.0182 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
14. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0181 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
16. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0174 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
17. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0172 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
18. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
19. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0171 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
20. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0171 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
21. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0170 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
22. **Hallihan_etal_DTM_12.pdf** — 0.0168 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
23. **Hallihan_etal_DTM_12.pdf** — 0.0166 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
24. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0165 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
25. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
27. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
29. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0158 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
30. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0158 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
31. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _development, a series of events must occur; even when the individual likelihood of success for e_
32. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0156 (rrf) — _# an action Cognitive biases can have a direct impact on how evacuation decisionmaking is unders_
33. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0155 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
34. **Hallihan_etal_DTM_12.pdf** — 0.0154 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
35. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0154 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
36. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0152 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
39. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0150 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
41. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
42. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
43. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
44. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0145 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
46. **Lyell Automation bias and verification complexity.pdf** — 0.0143 (rrf) — _# # – – – – – – – – – – – ### ### – P ¼ .031 ### > .05 ## < .001 DDS ( 31 ) 29 general practi- M_
47. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0143 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
48. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0143 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
49. **Hallihan_etal_DTM_12.pdf** — 0.0143 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
50. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0142 (rrf) — _# an action tem, additional external cues can interrupt the process—effectively starting the who_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Blinded, mechanism-first review of a single exercise-design debrief for affirmative, transcript-grounded cognitive bias occurrences; retrieved corpus used where directly supportive."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Bias blind spot",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Curse of knowledge",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Normalcy bias",
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
      "confidence": "moderate",
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": ["Anchoring bias", "Anchoring-and-adjustment heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value as an anchor and to make insufficient adjustments from that anchor when forming an estimate or judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scoping the full-scale exercise build timeline",
      "decision_point_description": "Estimating the project timeline and resource needs for the Riverbend Rising FSE based partly on the earlier 2019 exercise.",
      "affected_reasoning_operation": "Timeline estimation and resource planning",
      "bias_specific_mechanism": "The participant used the 2019 six-week, two-person, reused-shell project as the baseline anchor and adjusted only slightly for a larger scope, solo staffing, new hydrology modeling, and three-agency coordination, despite explicitly considering a schedule pad but rejecting it.",
      "manifestation_in_interview": "The participant treated the prior project timeline as roughly the baseline and compressed new content into the existing window rather than disaggregating new coordination and development work.",
      "effect_on_reasoning_or_decision": "Produced an unrealistically compressed schedule estimate that had slipped two weeks by the four-week status check.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much.",
          "evidence_explanation": "Shows the prior project serving as an anchor and an explicitly small adjustment despite materially different scope."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead.",
          "evidence_explanation": "Demonstrates insufficient adjustment from the anchor: a buffer was considered but not adopted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd actually broken out hours for three-agency sign-off separately instead of folding it into 'coordination,' I probably would've padded the schedule more. I didn't do that breakdown until after the slip showed up.",
          "evidence_explanation": "Confirms that the omitted decomposition contributed to under-adjustment from the anchor."
        }
      ],
      "correction_or_counterevidence": "Using a similar past project as a baseline can be a legitimate planning heuristic, and the deadline constrained planning. However, the participant's own account indicates the anchor was not sufficiently adjusted for known scope differences, and the slip was later recognized.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus supports anchoring-and-adjustment as a recognized cognitive mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Supports anchoring-and-adjustment as a recognized heuristic affecting judgment and adjustment under constraints.",
          "relevance_to_this_occurrence": "Validates the anchoring-and-adjustment mechanism, though the original domain was AI-assisted decision-making."
        },
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Tversky and Kahneman put it, “adjustments are typically insufficient.”",
          "mechanism_supported_by_source": "Provides the canonical diagnostic criterion of insufficient adjustment from an initial value.",
          "relevance_to_this_occurrence": "Directly supports the core mechanism producing the compressed timeline estimate."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Status quo bias",
      "alternative_labels": ["Default bias", "Familiarity preference"],
      "taxonomy_status": "established_label",
      "bias_definition": "A preference for the current or previous state of affairs, often driven by familiarity or comfort, leading to a decision not to switch even when alternatives may be better.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scenario format selection",
      "decision_point_description": "Choosing between the legacy exercise template and a newer modular design format for the FSE.",
      "affected_reasoning_operation": "Design option selection and evidence evaluation",
      "bias_specific_mechanism": "Familiarity and comfort with the legacy template drove selection, and the participant did not formally compare the modular format on training outcomes.",
      "manifestation_in_interview": "The participant chose the legacy template for the third cycle because it was known, fast, and comfortable, and acknowledged making no formal performance comparison.",
      "effect_on_reasoning_or_decision": "Locked the exercise build into the legacy format, potentially forgoing a format that stakeholders suggested was better suited to multi-agency coordination.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in.",
          "evidence_explanation": "Directly identifies familiarity and comfort as decision factors favoring the status quo."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure.",
          "evidence_explanation": "Shows the choice was not based on comparative outcome evidence, with preference anchored to the existing template."
        }
      ],
      "correction_or_counterevidence": "Under a fixed deadline, reusing a known template can be a reasonable time-saving heuristic, and no data were presented showing the modular format was better. This plausible non-bias explanation lowers confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported status quo bias; classification relies on established cognitive-science knowledge of status quo preference.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Normalcy bias",
      "alternative_labels": ["Availability heuristic", "Disaster risk underestimation"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to underestimate the likelihood or severity of a hazardous event because it has not occurred recently or within personal or community experience, producing a false sense of normality.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Flood severity calibration",
      "decision_point_description": "Setting the peak severity of the levee-failure scenario in light of updated Army Corps modeling and local flood history.",
      "affected_reasoning_operation": "Risk assessment and scenario severity calibration",
      "bias_specific_mechanism": "The local absence of catastrophic flooding for over forty years made the modeled high-severity scenario feel abstract and implausible, so the participant scaled peak severity down toward the more familiar flood level.",
      "manifestation_in_interview": "The participant acknowledged that the forty-year point shaped his thinking and led to reducing peak severity despite modeling indicating higher catastrophic risk.",
      "effect_on_reasoning_or_decision": "Potentially understated the exercise scenario severity, which could weaken EOC escalation testing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years.",
          "evidence_explanation": "Establishes the conflict between model-based risk information and historically normal local experience."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I ended up scaling the peak severity down toward the more familiar flood level. The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face.",
          "evidence_explanation": "Shows historical absence and familiarity directly influenced the severity judgment, overriding or discounting the model."
        }
      ],
      "correction_or_counterevidence": "Keeping scenarios plausible for the community can be a legitimate exercise-design goal, and advisory-committee pressure also contributed. The participant later expressed genuine uncertainty about whether the milder scenario undercut escalation testing.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved cockpit-safety corpus supports the false-sense-of-normality mechanism, though the domain differs.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "possibly one of the more alarming takes from the data was the apparent false sense of normality that cognitive bias appears to create in the cockpit.",
          "mechanism_supported_by_source": "Supports the presence of a false sense of normality as a cognitive-bias-driven distortion in safety-critical settings.",
          "relevance_to_this_occurrence": "Analogous mechanism of underestimating unlikely but severe operational risk because of perceived normality."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Bias blind spot",
      "alternative_labels": ["Asymmetric self-scrutiny"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize the impact of biases or errors in others' judgment while failing to recognize the same biases or errors in one's own judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Peer AAR review and self-assessment during severity calibration",
      "decision_point_description": "Evaluating a peer's unrealistically mild scenario while the participant was concurrently making a similar severity decision in his own exercise.",
      "affected_reasoning_operation": "Self-assessment and comparative scrutiny of reasoning quality",
      "bias_specific_mechanism": "The participant readily identified a planning gap in a peer's mild scenario but did not apply the same scrutiny to his own concurrent severity choice, apparently exempting his own reasoning from the same standard.",
      "manifestation_in_interview": "He reported being clear that the peer's scenario reflected a planning gap but was not worried about the same problem in his own build, and he admitted not applying the same scrutiny.",
      "effect_on_reasoning_or_decision": "Reduced the likelihood of detecting the potential severity error in his own exercise at the moment it mattered.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "In that discussion I was pretty clear it looked like a planning gap on their end. I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time.",
          "evidence_explanation": "Demonstrates asymmetric application of scrutiny to another's reasoning while exempting self."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard.",
          "evidence_explanation": "Explicitly admits not applying the same critical standard to his own concurrent decision."
        }
      ],
      "correction_or_counterevidence": "The participant was under time pressure and focused on the peer-review task; however, the asymmetry was acknowledged directly in the transcript.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported bias blind spot; classification relies on established cognitive-science knowledge of asymmetric bias recognition.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Curse of knowledge",
      "alternative_labels": ["Expert blind spot", "False consensus effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Difficulty in taking the perspective of less-informed others because one's own knowledge is treated as transparent, standard, or obvious.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Controller-Evaluator handbook development",
      "decision_point_description": "Deciding whether to include a glossary and clearer explanations for evaluators outside core emergency management.",
      "affected_reasoning_operation": "Perspective-taking and communication design",
      "bias_specific_mechanism": "The participant's fifteen years of experience and familiar shorthand made terms feel standard to him, so the need for a glossary seemed unnecessary, even though prior feedback had identified clarity gaps for outside evaluators.",
      "manifestation_in_interview": "He kept the handbook concise with standard terminology and no glossary because the terms felt standard to him, despite informal AAR feedback requesting clearer explanations.",
      "effect_on_reasoning_or_decision": "Potentially reduced handbook usability and contributed to observed scoring inconsistencies among non-core EM evaluators.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left.",
          "evidence_explanation": "Shows his own familiarity was used to estimate others' understanding, discounting documented need for clearer explanations."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And they might not have carried the same assumptions I had about what 'obvious' means in the handbook, since they wouldn't have fifteen years of the same habits behind them.",
          "evidence_explanation": "Retrospective recognition that his expert assumptions were not shared by outsiders, consistent with curse of knowledge."
        }
      ],
      "correction_or_counterevidence": "Time compression near the deadline was real and could partially explain the omission; however, the participant also cited perceived standardness of the terms, not solely time pressure.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported curse of knowledge; classification relies on established cognitive-science knowledge of expert perspective-taking failure.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Salience bias",
      "alternative_labels": ["Availability heuristic", "Vividness effect"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Training inject production priority",
      "supporting_interview_quote": "Past surveys showed people remember those vividly — I figured that made them the more effective training tool.",
      "plausible_mechanism": "Vivid photo and video injects may have been overweighted relative to less salient but operationally specific data packages because memorability and vividness were used as a proxy for training effectiveness.",
      "why_not_identified": "The participant cited past survey evidence for recall, and prioritizing engaging training material can be a reasonable instructional design decision. The transcript does not clearly establish that the weighting distorted judgment rather than reflecting a defensible training objective."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus does not cover all identified biases; several classifications rely on established cognitive-science criteria without direct corpus support.",
    "The interview is a single self-reported retrospective account, which may be subject to memory or presentation effects.",
    "No independent outcome data were available to verify the operational consequences of the identified biased decisions.",
    "Interviewer follow-up wording may have shaped participant retrospection, although occurrence classifications required direct mechanism evidence."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief for our exercise-design case-study library — I'll be asking about a specific project you led, how the decisions actually unfolded, not whether they were 'right' in hindsight. Everything stays de-identified. Sound okay? Participant: Sure, happy to walk through it. This is the Riverbend Rising full-scale exercise, right? That one's still pretty fresh for me. Interviewer: Exactly. Can you start by describing the assignment and what success would've looked like? Participant: I was handed the FSE build in early spring — simulate a levee failure and flash-flood evacuation, get it HSEEP-compliant, and use it to validate EOC escalation procedures before the seasonal flood window opened. Success meant a full exercise day, a usable Controller-Evaluator handbook, and an AAR that actually told the Director something new about our capability gaps. Interviewer: Give me the incident account — how did the project actually go, start to finish? Participant: We'd run something similar back in 2019 — smaller footprint, two of us on it, and we mostly reused an existing scenario shell. That one took about six weeks start to finish. This time I was solo, and the scope was bigger: a brand-new levee-failure module built off updated Army Corps dam-break modeling, plus coordination across the regional EOC, the school district, and municipal police and fire. Deadline was fixed at ten weeks because of the flood-risk calendar. I scoped the build assuming it'd track pretty close to the 2019 timeline — figured I knew the process well enough to move fast. About four weeks in, I was still building the custom hydrology module and waiting on sign-off from three different agencies, and a status check showed we'd already slipped two weeks. From there it became a scramble — severity calibration with the advisory committee, a fight over which training injects we could actually finish, and a last push on the handbook right up against the deadline. Interviewer: Let's reconstruct that chronologically. What did you know at each stage, and what changed as you learned more? Participant: At kickoff I had the 2019 numbers in my head and the new Corps data in hand, but I hadn't yet mapped out how much longer three-agency coordination would take versus one shell reused solo. Once the schedule slipped, I knew severity calibration and the advisory committee conversation were coming up next, and I could already tell we wouldn't have time to fully build every kind of training material — so the inject decision became a resource fight. By the time I got to the handbook, the clock was the dominant fact. Interviewer: Let's slow down on the first real decision — scoping the build timeline. Walk me through it. Participant: Right, so going in, I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much. I remember telling the Director I could deliver in the same general window even though I was down to one person and building the hydrology piece essentially from scratch. Interviewer: What made you confident the compressed schedule would hold? Participant: Honestly, mostly that I'd done a version of this before and it worked out then. I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead. Interviewer: What information would have changed that estimate? Participant: If I'd actually broken out hours for three-agency sign-off separately instead of folding it into 'coordination,' I probably would've padded the schedule more. I didn't do that breakdown until after the slip showed up. Interviewer: Still in that same phase — you also had a choice about which scenario format to build from. What drove that? Participant: Yeah, there was a newer modular design format some of the stakeholders floated, supposedly better suited to multi-agency exercises. But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in. Interviewer: Did you compare how the two formats actually performed for training outcomes? Participant: Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure. Interviewer: Let's move to the severity decision. What was on the table? Participant: The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years. There was real pressure to keep the scenario grounded in something the community would find plausible. Interviewer: How did you weigh the modeling against that history? Participant: I ended up scaling the peak severity down toward the more familiar flood level. The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face. Interviewer: Around that same time, you were part of an AAR review for a peer's exercise. What happened there? Participant: Right, a planner in another county got flagged for an unrealistically mild scenario — didn't stress escalation procedures at all. In that discussion I was pretty clear it looked like a planning gap on their end. I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time. Interviewer: Did you apply the same scrutiny to your own severity choice that you applied to theirs? Participant: Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard. Interviewer: Third decision point — the training injects. What were the options? Participant: We only had production time to fully build one category. Option one was photo and video clips of levee overtopping — dramatic, but slow to produce. Option two was the data packages — stream gauge readouts, GIS flow-rate shapefiles — less visually interesting but more specific for EOC modeling decisions. Interviewer: Which did you prioritize, and why? Participant: I put most of the remaining time into the photo and video injects. Past surveys showed people remember those vividly — I figured that made them the more effective training tool. Interviewer: Did you weigh how well each format supported the actual operational decisions evaluators would need to make? Participant: Less than I probably should have, in retrospect. The reasoning at the time was really centered on impact and recall, not on whether the flow-rate specifics would be there when people needed them. Interviewer: Last decision point — the Controller-Evaluator handbook. What went into that? Participant: I've been doing this fifteen years, and I've used the same shorthand and scoring conventions across a lot of exercises. Time was short, so I kept the handbook concise — standard terminology, no glossary. Interviewer: Was there any indication a glossary might be needed? Participant: There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left. Interviewer: Looking back across all four decisions — if you'd had two more weeks, what would you have done differently? Participant: Probably built in a real contingency buffer up front instead of assuming the old timeline would hold, and maybe split production time more evenly between the visual and data injects. Interviewer: And if a different planner had taken over halfway through? Participant: They might have pushed harder on the severity call, given the modeling was pretty clear. And they might not have carried the same assumptions I had about what 'obvious' means in the handbook, since they wouldn't have fifteen years of the same habits behind them. Interviewer: Anything you'd flag as uncertain even now? Participant: Whether the milder scenario actually undercut the escalation testing, or whether it was just a rough exercise day for other reasons — I genuinely don't know. Same with the handbook; the scoring inconsistencies could've come from a dozen things, not just the shorthand. Interviewer: That's a good place to stop. Thanks for the detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.03s · gen 133.77s · total 138.2s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0288 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0270 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
3. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0246 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0240 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0236 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0221 (rrf) — _We embedded behavioral measures in all three of our games to assess shortand longterm effects an_
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0219 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0203 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0201 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0199 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0191 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0190 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **Hallihan_etal_DTM_12.pdf** — 0.0182 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
14. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0181 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
16. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0174 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
17. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0172 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
18. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
19. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0171 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
20. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0171 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
21. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0170 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
22. **Hallihan_etal_DTM_12.pdf** — 0.0168 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
23. **Hallihan_etal_DTM_12.pdf** — 0.0166 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
24. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0165 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
25. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
27. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
29. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0158 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
30. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0158 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
31. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _development, a series of events must occur; even when the individual likelihood of success for e_
32. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0156 (rrf) — _# an action Cognitive biases can have a direct impact on how evacuation decisionmaking is unders_
33. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0155 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
34. **Hallihan_etal_DTM_12.pdf** — 0.0154 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
35. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0154 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
36. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0152 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
39. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0150 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
41. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
42. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
43. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
44. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0145 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
46. **Lyell Automation bias and verification complexity.pdf** — 0.0143 (rrf) — _# # – – – – – – – – – – – ### ### – P ¼ .031 ### > .05 ## < .001 DDS ( 31 ) 29 general practi- M_
47. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0143 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
48. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0143 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
49. **Hallihan_etal_DTM_12.pdf** — 0.0143 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
50. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0142 (rrf) — _# an action tem, additional external cues can interrupt the process—effectively starting the who_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Focused on the participant's reported reasoning during the exercise-design project, including timeline scoping, scenario format selection, severity calibration, peer AAR comparison, inject prioritization, and handbook design."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "bias blind spot",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "curse of knowledge",
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
      "bias_label": "anchoring and adjustment heuristic",
      "alternative_labels": ["anchoring bias", "insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "Estimates are made starting from an initial value or anchor, with subsequent adjustments typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial scoping of the full-scale exercise build timeline",
      "decision_point_description": "Estimating the schedule and contingency for the Riverbend Rising full-scale exercise build.",
      "affected_reasoning_operation": "Timeline estimation and planning under uncertainty",
      "bias_specific_mechanism": "The 2019 six-week project served as the initial baseline; the participant adjusted only slightly for a larger solo multi-agency build and did not break out new coordination requirements before committing to the compressed window.",
      "manifestation_in_interview": "The participant explicitly reports treating the 2019 project as the baseline and only adjusting a little, then chose not to add a contingency buffer.",
      "effect_on_reasoning_or_decision": "The schedule was set too close to the old timeline, contributing to an early two-week slip.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right, so going in, I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much.",
          "evidence_explanation": "The participant identifies the 2019 timeline as the initial anchor and reports only a small adjustment despite larger scope and solo staffing."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, mostly that I'd done a version of this before and it worked out then. I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead.",
          "evidence_explanation": "This shows reliance on the prior successful timeline and insufficient adjustment via omitting a contingency buffer."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd actually broken out hours for three-agency sign-off separately instead of folding it into 'coordination,' I probably would've padded the schedule more. I didn't do that breakdown until after the slip showed up.",
          "evidence_explanation": "The lack of decomposition of new coordination work supports the idea that adjustment from the anchor was insufficient."
        }
      ],
      "correction_or_counterevidence": "Real solo staffing, larger scope, and a fixed flood-risk calendar created genuine schedule pressure; however, the participant's own account shows the new coordination work was not decomposed before committing to the timeline.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Corpus support from a retrieved passage on anchoring and adjustment is available.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described by Tversky and Kahneman in 1974... people make estimates based on an initial answer, and adjustments from there based on additional information... 'adjustments are typically insufficient.'",
          "mechanism_supported_by_source": "Initial answers anchor estimates and later adjustments are insufficient.",
          "relevance_to_this_occurrence": "The participant used the 2019 six-week timeline as an initial answer and adjusted only slightly for the new module, matching the anchoring-and-insufficient-adjustment pattern."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "status quo bias",
      "alternative_labels": ["default bias", "preference for familiar default"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to prefer the current or familiar option and avoid change, even when an alternative may be more suitable.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scenario design format selection",
      "decision_point_description": "Choosing between the legacy scenario template and a newer modular design format.",
      "affected_reasoning_operation": "Option evaluation and design choice",
      "bias_specific_mechanism": "The legacy template was the established default; the participant chose it because it was known, fast, and comfortable, without formally comparing the modular alternative's training outcomes.",
      "manifestation_in_interview": "The participant reports going with the legacy template for the third cycle because it is comfortable and familiar, despite a stakeholder-suggested modular alternative.",
      "effect_on_reasoning_or_decision": "The project retained the legacy format, potentially forgoing a format better suited to multi-agency exercise needs.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, there was a newer modular design format some of the stakeholders floated, supposedly better suited to multi-agency exercises. But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in.",
          "evidence_explanation": "The selection invoked familiarity and comfort with the existing template rather than a comparative assessment of suitability."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure.",
          "evidence_explanation": "A lack of data could have been resolved or weighed, but the stated reason was ease and familiarity with the old structure."
        }
      ],
      "correction_or_counterevidence": "The participant had no data showing the modular format was superior, and time pressure made the known template a reasonable choice; this is not a bias if the legacy format was simply more efficient.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was unavailable; label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judgments about likelihood or severity are influenced by the ease with which relevant examples come to mind rather than by complete model or base-rate information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scenario peak severity calibration",
      "decision_point_description": "Deciding whether to follow updated Corps modeling toward a catastrophic severity or scale the scenario toward a familiar flood level.",
      "affected_reasoning_operation": "Risk and scenario severity calibration",
      "bias_specific_mechanism": "The repeated, easily recalled local fact that catastrophic flooding had not been seen in over forty years made the modeled catastrophic case feel abstract and implausible, pulling peak severity downward despite updated model data.",
      "manifestation_in_interview": "The participant says the forty-year point came up a lot and shaped his thinking, leading him to scale severity down toward the familiar flood level.",
      "effect_on_reasoning_or_decision": "The scenario may have under-stressed EOC escalation procedures because the severity was scaled toward recalled local history instead of model risk.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years.",
          "evidence_explanation": "The contrast shows model data being weighed against a salient historical absence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I ended up scaling the peak severity down toward the more familiar flood level. The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face.",
          "evidence_explanation": "The explicit statement that the local-history point shaped his thinking toward familiarity supports an availability mechanism in the severity estimate."
        }
      ],
      "correction_or_counterevidence": "Community plausibility and local risk communication are legitimate exercise-design considerations; the participant also voices residual uncertainty about severity, so the bias is not the only possible explanation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was unavailable; label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bias blind spot",
      "alternative_labels": ["asymmetric bias detection"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to recognize cognitive biases or planning failures in others while failing to recognize the same biases in one's own reasoning.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Peer AAR review during own severity decision",
      "decision_point_description": "Reviewing another planner's unrealistically mild scenario while simultaneously making his own severity calibration decision.",
      "affected_reasoning_operation": "Comparative judgment and self-monitoring",
      "bias_specific_mechanism": "The participant applied a critical standard to another planner's mild scenario but did not apply the same scrutiny to his own simultaneously occurring severity decision.",
      "manifestation_in_interview": "He reports flagging the peer's mild scenario as a planning gap but not worrying about the same flaw in his own build at that exact time.",
      "effect_on_reasoning_or_decision": "His own severity decision was insulated from the critical standard he applied to the peer, reducing the chance of catching a similar error.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right, a planner in another county got flagged for an unrealistically mild scenario — didn't stress escalation procedures at all. In that discussion I was pretty clear it looked like a planning gap on their end. I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time.",
          "evidence_explanation": "The asymmetry is explicit: he detects a mild-scenario gap in another planner's work but does not apply the same concern to himself."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard.",
          "evidence_explanation": "This directly confirms an asymmetric application of scrutiny."
        }
      ],
      "correction_or_counterevidence": "The peer's scenario may have been objectively flawed; without full details, the participant's external criticism could be justified. The bias is the failure to self-monitor, not the criticism itself.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was unavailable; label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judgments about effectiveness are influenced by salient, easily recalled examples or vividness rather than by decision-relevant analysis.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Training inject production prioritization",
      "decision_point_description": "Choosing whether to prioritize visual media injects or data packages under limited production time.",
      "affected_reasoning_operation": "Resource allocation and training-inject selection",
      "bias_specific_mechanism": "Salient memory of past survey recall for visual materials made visual injects seem more effective; the participant judged effectiveness by impact and recall rather than by whether the injects supported the evaluators' operational decisions.",
      "manifestation_in_interview": "The participant allocated most remaining time to photo/video injects because people remember them vividly, while acknowledging the data packages were more specific for EOC modeling decisions.",
      "effect_on_reasoning_or_decision": "Data packages were underbuilt, potentially leaving operational decision-support information missing during the exercise.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I put most of the remaining time into the photo and video injects. Past surveys showed people remember those vividly — I figured that made them the more effective training tool.",
          "evidence_explanation": "Vividness and recall drove the judgment of effectiveness."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Less than I probably should have, in retrospect. The reasoning at the time was really centered on impact and recall, not on whether the flow-rate specifics would be there when people needed them.",
          "evidence_explanation": "The participant confirms that operational decision support was underweighted relative to impact and recall."
        }
      ],
      "correction_or_counterevidence": "Recall and engagement are plausible training-effectiveness criteria, so prioritizing visual injects was not necessarily biased; the concern is the neglect of operational decision relevance.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was unavailable; label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "curse of knowledge",
      "alternative_labels": ["curse of expertise"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency for knowledgeable people to assume that others share their knowledge or that familiar terminology and conventions are equally clear to others.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Controller-Evaluator handbook design",
      "decision_point_description": "Deciding whether to include clearer explanations or a glossary for evaluators outside core emergency management.",
      "affected_reasoning_operation": "Communication design and assumption about audience knowledge",
      "bias_specific_mechanism": "Fifteen years of using the same shorthand and scoring conventions made the participant perceive the terminology as standard and self-evident; he underweighted past informal feedback requesting clearer explanations for outsiders.",
      "manifestation_in_interview": "The participant kept the handbook concise with standard terminology and no glossary, saying the terms felt standard to him despite prior AAR feedback for clearer explanations.",
      "effect_on_reasoning_or_decision": "The handbook likely remained less accessible to evaluators outside core EM, contributing to scoring inconsistencies.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've been doing this fifteen years, and I've used the same shorthand and scoring conventions across a lot of exercises. Time was short, so I kept the handbook concise — standard terminology, no glossary.",
          "evidence_explanation": "The participant's expertise and time pressure led to relying on familiar shorthand without additional explanation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left.",
          "evidence_explanation": "Past feedback indicates a known audience knowledge gap, but the participant's own familiarity with the terms led him not to prioritize the glossary."
        }
      ],
      "correction_or_counterevidence": "Time was short and core EM evaluators may not need a glossary; not prioritizing explanatory material under deadline pressure could be a resource decision rather than bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was unavailable; label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages were sparse and directly supported only the anchoring occurrence; other labels derive from general cognitive-science taxonomy rather than retrieved corpus support.",
    "The analysis is based on participant self-report and a retrospective debrief rather than direct observation of the decisions.",
    "Several decisions also reflect objective time, staffing, and resource constraints, which are not treated as biases unless a distinct mechanism was evidenced."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief for our exercise-design case-study library — I'll be asking about a specific project you led, how the decisions actually unfolded, not whether they were 'right' in hindsight. Everything stays de-identified. Sound okay? Participant: Sure, happy to walk through it. This is the Riverbend Rising full-scale exercise, right? That one's still pretty fresh for me. Interviewer: Exactly. Can you start by describing the assignment and what success would've looked like? Participant: I was handed the FSE build in early spring — simulate a levee failure and flash-flood evacuation, get it HSEEP-compliant, and use it to validate EOC escalation procedures before the seasonal flood window opened. Success meant a full exercise day, a usable Controller-Evaluator handbook, and an AAR that actually told the Director something new about our capability gaps. Interviewer: Give me the incident account — how did the project actually go, start to finish? Participant: We'd run something similar back in 2019 — smaller footprint, two of us on it, and we mostly reused an existing scenario shell. That one took about six weeks start to finish. This time I was solo, and the scope was bigger: a brand-new levee-failure module built off updated Army Corps dam-break modeling, plus coordination across the regional EOC, the school district, and municipal police and fire. Deadline was fixed at ten weeks because of the flood-risk calendar. I scoped the build assuming it'd track pretty close to the 2019 timeline — figured I knew the process well enough to move fast. About four weeks in, I was still building the custom hydrology module and waiting on sign-off from three different agencies, and a status check showed we'd already slipped two weeks. From there it became a scramble — severity calibration with the advisory committee, a fight over which training injects we could actually finish, and a last push on the handbook right up against the deadline. Interviewer: Let's reconstruct that chronologically. What did you know at each stage, and what changed as you learned more? Participant: At kickoff I had the 2019 numbers in my head and the new Corps data in hand, but I hadn't yet mapped out how much longer three-agency coordination would take versus one shell reused solo. Once the schedule slipped, I knew severity calibration and the advisory committee conversation were coming up next, and I could already tell we wouldn't have time to fully build every kind of training material — so the inject decision became a resource fight. By the time I got to the handbook, the clock was the dominant fact. Interviewer: Let's slow down on the first real decision — scoping the build timeline. Walk me through it. Participant: Right, so going in, I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much. I remember telling the Director I could deliver in the same general window even though I was down to one person and building the hydrology piece essentially from scratch. Interviewer: What made you confident the compressed schedule would hold? Participant: Honestly, mostly that I'd done a version of this before and it worked out then. I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead. Interviewer: What information would have changed that estimate? Participant: If I'd actually broken out hours for three-agency sign-off separately instead of folding it into 'coordination,' I probably would've padded the schedule more. I didn't do that breakdown until after the slip showed up. Interviewer: Still in that same phase — you also had a choice about which scenario format to build from. What drove that? Participant: Yeah, there was a newer modular design format some of the stakeholders floated, supposedly better suited to multi-agency exercises. But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in. Interviewer: Did you compare how the two formats actually performed for training outcomes? Participant: Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure. Interviewer: Let's move to the severity decision. What was on the table? Participant: The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years. There was real pressure to keep the scenario grounded in something the community would find plausible. Interviewer: How did you weigh the modeling against that history? Participant: I ended up scaling the peak severity down toward the more familiar flood level. The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face. Interviewer: Around that same time, you were part of an AAR review for a peer's exercise. What happened there? Participant: Right, a planner in another county got flagged for an unrealistically mild scenario — didn't stress escalation procedures at all. In that discussion I was pretty clear it looked like a planning gap on their end. I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time. Interviewer: Did you apply the same scrutiny to your own severity choice that you applied to theirs? Participant: Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard. Interviewer: Third decision point — the training injects. What were the options? Participant: We only had production time to fully build one category. Option one was photo and video clips of levee overtopping — dramatic, but slow to produce. Option two was the data packages — stream gauge readouts, GIS flow-rate shapefiles — less visually interesting but more specific for EOC modeling decisions. Interviewer: Which did you prioritize, and why? Participant: I put most of the remaining time into the photo and video injects. Past surveys showed people remember those vividly — I figured that made them the more effective training tool. Interviewer: Did you weigh how well each format supported the actual operational decisions evaluators would need to make? Participant: Less than I probably should have, in retrospect. The reasoning at the time was really centered on impact and recall, not on whether the flow-rate specifics would be there when people needed them. Interviewer: Last decision point — the Controller-Evaluator handbook. What went into that? Participant: I've been doing this fifteen years, and I've used the same shorthand and scoring conventions across a lot of exercises. Time was short, so I kept the handbook concise — standard terminology, no glossary. Interviewer: Was there any indication a glossary might be needed? Participant: There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left. Interviewer: Looking back across all four decisions — if you'd had two more weeks, what would you have done differently? Participant: Probably built in a real contingency buffer up front instead of assuming the old timeline would hold, and maybe split production time more evenly between the visual and data injects. Interviewer: And if a different planner had taken over halfway through? Participant: They might have pushed harder on the severity call, given the modeling was pretty clear. And they might not have carried the same assumptions I had about what 'obvious' means in the handbook, since they wouldn't have fifteen years of the same habits behind them. Interviewer: Anything you'd flag as uncertain even now? Participant: Whether the milder scenario actually undercut the escalation testing, or whether it was just a rough exercise day for other reasons — I genuinely don't know. Same with the handbook; the scoring inconsistencies could've come from a dozen things, not just the shorthand. Interviewer: That's a good place to stop. Thanks for the detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.30s · gen 169.33s · total 174.0s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0288 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0270 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
3. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0246 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0240 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0236 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
6. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0221 (rrf) — _We embedded behavioral measures in all three of our games to assess shortand longterm effects an_
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0219 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0203 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0201 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0199 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0191 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0190 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
13. **Hallihan_etal_DTM_12.pdf** — 0.0182 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
14. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0181 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
16. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0174 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
17. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0172 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
18. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
19. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0171 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
20. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0171 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
21. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0170 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
22. **Hallihan_etal_DTM_12.pdf** — 0.0168 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
23. **Hallihan_etal_DTM_12.pdf** — 0.0166 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
24. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0165 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
25. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
27. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0158 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
29. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0158 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
30. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0158 (rrf) — _2. Do I need to take protective action? If the answer is ‘‘yes’’, then, the individual/group dec_
31. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _development, a series of events must occur; even when the individual likelihood of success for e_
32. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0156 (rrf) — _# an action Cognitive biases can have a direct impact on how evacuation decisionmaking is unders_
33. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0155 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
34. **Hallihan_etal_DTM_12.pdf** — 0.0154 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
35. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0154 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
36. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0152 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
39. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0150 (rrf) — _# 6 Discussion Lessons learned. We now discuss some of the lessons learned from the results obta_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
41. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
42. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
43. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
44. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0145 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
46. **Lyell Automation bias and verification complexity.pdf** — 0.0143 (rrf) — _# # – – – – – – – – – – – ### ### – P ¼ .031 ### > .05 ## < .001 DDS ( 31 ) 29 general practi- M_
47. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0143 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
48. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0143 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
49. **Hallihan_etal_DTM_12.pdf** — 0.0143 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
50. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0142 (rrf) — _# an action tem, additional external cues can interrupt the process—effectively starting the who_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first analysis of participant reasoning episodes in a CTA debrief; no experimental condition or expected bias count assumed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Bias blind spot",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Curse of knowledge",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Salience bias",
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
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment heuristic", "Anchoring effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value as a reference point and to make insufficient adjustments from that anchor when forming an estimate or decision.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial timeline scoping",
      "decision_point_description": "Estimating the project timeline and deciding whether to add a contingency buffer after receiving the expanded scope.",
      "affected_reasoning_operation": "Schedule estimation and planning judgment",
      "bias_specific_mechanism": "The participant anchored on the 2019 six-week, two-person, reused-shell project as the baseline and adjusted only slightly for expanded scope, solo staffing, and new hydrology modeling, without separately estimating the added coordination workload.",
      "manifestation_in_interview": "The participant reported treating the 2019 timeline as roughly the baseline and compressing new content into the existing window despite being solo and building a new module from scratch; the schedule later slipped two weeks.",
      "effect_on_reasoning_or_decision": "Produced an under-scoped timeline and no formal contingency buffer, contributing to a two-week slip and later scramble.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right, so going in, I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much.",
          "evidence_explanation": "Shows reliance on prior project as an anchor and only minor adjustment for known differences."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead.",
          "evidence_explanation": "Demonstrates insufficient adjustment away from the anchor despite recognizing an option to pad."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd actually broken out hours for three-agency sign-off separately instead of folding it into 'coordination,' I probably would've padded the schedule more.",
          "evidence_explanation": "Identifies the missing decomposition that would have corrected the anchored estimate, showing the mechanism affected the estimate."
        }
      ],
      "correction_or_counterevidence": "The participant recognized after the slip that a separate three-agency sign-off breakout would have led to more schedule padding; this was retrospective rather than a contemporaneous correction.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages from two sources directly describe anchoring-and-adjustment as an initial estimate with insufficient adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Document: Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": null,
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source describes anchoring and adjustment as a time-accuracy tradeoff and documents insufficient adjustment away from an anchor.",
          "relevance_to_this_occurrence": "The participant used an initial 2019 baseline and adjusted insufficiently for a larger scope, matching the anchoring-and-adjustment pattern."
        },
        {
          "source_identifier": "Document: Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information",
          "mechanism_supported_by_source": "The source explains that estimates begin with an initial answer and adjustments are typically insufficient, particularly in engineering estimates.",
          "relevance_to_this_occurrence": "The participant began with the previous project timeline as the initial answer and did not sufficiently adjust for the new module and solo staffing."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Status quo bias",
      "alternative_labels": ["Default bias", "Familiarity heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to prefer the current or previous state over change, even when an alternative may be better suited, often due to comfort, familiarity, or default effects.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scenario format selection",
      "decision_point_description": "Choosing between a newer modular design format and the legacy template for the exercise build.",
      "affected_reasoning_operation": "Evaluation and selection of scenario design format",
      "bias_specific_mechanism": "The participant favored the legacy template because it was familiar, fast, and comfortable, and did not formally compare it with the newer modular format, reflecting a status quo preference rather than an evidentiary comparison.",
      "manifestation_in_interview": "The participant selected the legacy template for the third cycle, citing comfort and ease rather than data about training effectiveness, and acknowledged not formally comparing the modular format.",
      "effect_on_reasoning_or_decision": "The choice locked the build into the legacy format and foreclosed the potential multi-agency readiness benefits of the modular design without formal evaluation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in.",
          "evidence_explanation": "Shows the decision was driven by familiarity and comfort with the existing format rather than a comparative evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure.",
          "evidence_explanation": "Confirms the absence of outcome data and reinforces that prior knowledge of the old structure was decisive."
        }
      ],
      "correction_or_counterevidence": "The participant cited speed and task knowledge, which could also represent a legitimate efficiency heuristic under time pressure; this competing explanation is why confidence is low.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supports status quo bias; this label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the probability, frequency, or plausibility of an event by how easily examples or associations come to mind, causing over- or under-weighting of risks.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Severity calibration",
      "decision_point_description": "Deciding whether to keep the catastrophic peak severity indicated by Corps modeling or scale it down toward more familiar flood levels.",
      "affected_reasoning_operation": "Risk severity calibration and plausibility assessment",
      "bias_specific_mechanism": "The participant judged the catastrophic flood scenario as less plausible because local examples of such severity were not available in memory, so he downscaled peak severity despite updated modeling.",
      "manifestation_in_interview": "The advisory committee’s forty-year no-event history became a repeated reference, and the participant explicitly said this shaped his thinking toward a familiar, less catastrophic flood level.",
      "effect_on_reasoning_or_decision": "The exercise was centered on a milder flood scenario that may not have fully stressed escalation procedures.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years.",
          "evidence_explanation": "Shows that the absence of readily recalled local events competed with and influenced the modeling-based risk assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face.",
          "evidence_explanation": "Demonstrates that the availability of local examples directly shaped the plausibility judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I ended up scaling the peak severity down toward the more familiar flood level.",
          "evidence_explanation": "Shows the effect of the availability-driven reasoning on the final severity decision."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged uncertainty whether the milder scenario undercut escalation testing, but no contemporaneous correction occurred.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supports availability heuristic; this label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Bias blind spot",
      "alternative_labels": ["Asymmetric self-assessment", "Bias blindspot"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize cognitive biases or planning gaps in others more readily than in one's own concurrent reasoning.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Peer AAR review and self-evaluation",
      "decision_point_description": "Evaluating a peer's unrealistically mild scenario and whether to apply the same scrutiny to his own severity choice.",
      "affected_reasoning_operation": "Self-evaluation and comparative judgment",
      "bias_specific_mechanism": "The participant readily identified a planning gap in a peer's exercise but did not apply the same severity-calibration standard to his own concurrent decision, reflecting asymmetric bias detection.",
      "manifestation_in_interview": "While discussing a peer's flag, the participant called it a planning gap but admitted he was not worried about the same failure in his own build even though he was mid-decision on severity.",
      "effect_on_reasoning_or_decision": "Reduced the likelihood of self-correction on the severity decision and allowed the availability-driven downscaling to proceed unchecked.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "In that discussion I was pretty clear it looked like a planning gap on their end.",
          "evidence_explanation": "Demonstrates ready detection of a planning gap in another planner."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time.",
          "evidence_explanation": "Shows the failure to apply the same standard to his own comparable risk."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard.",
          "evidence_explanation": "Explicitly confirms the asymmetric scrutiny mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant eventually recognized the asymmetry during the interview, but there was no contemporaneous self-check.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supports bias blind spot; this label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Salience bias",
      "alternative_labels": ["Vividness effect", "Salience heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overweight salient, vivid, or emotionally engaging information when making judgments or allocating resources.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Training inject prioritization",
      "decision_point_description": "Deciding whether to allocate limited production time to photo/video injects or data packages.",
      "affected_reasoning_operation": "Allocation of training production resources",
      "bias_specific_mechanism": "The participant used the vividness and memorability of photo/video injects as a proxy for training effectiveness, weighted impact and recall heavily, and under-weighted the operational decision-specific information provided by data packages.",
      "manifestation_in_interview": "The participant chose photo/video injects because past surveys showed people remember them vividly, and acknowledged the reasoning centered on impact and recall rather than operational flow-rate specifics.",
      "effect_on_reasoning_or_decision": "Most remaining production time went to visually vivid injects, leaving less support for EOC modeling decisions that evaluators may have needed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I put most of the remaining time into the photo and video injects. Past surveys showed people remember those vividly — I figured that made them the more effective training tool.",
          "evidence_explanation": "Shows that recalled vividness/memorability drove the judgment of effectiveness."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The reasoning at the time was really centered on impact and recall, not on whether the flow-rate specifics would be there when people needed them.",
          "evidence_explanation": "Confirms the treatment of vividness/recall as the dominant criterion and neglect of operational decision-support value."
        }
      ],
      "correction_or_counterevidence": "The participant had past survey evidence about recall, so the effect may also involve a plausible deliberate prioritization of engagement; this competing explanation is why confidence is low.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supports salience bias; this label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Curse of knowledge",
      "alternative_labels": ["Curse of expertise", "Expert blind spot", "False consensus effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a knowledgeable person to assume that others have the same background knowledge or that expert shorthand is more understandable than it is.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Controller-Evaluator handbook design",
      "decision_point_description": "Deciding whether to add explanations or a glossary for evaluators outside core emergency management.",
      "affected_reasoning_operation": "Estimation of audience comprehension / communication design",
      "bias_specific_mechanism": "The participant's fifteen years of experience with the same shorthand made the terms feel standard and self-explanatory, so he did not add a glossary despite prior feedback requesting clearer explanations.",
      "manifestation_in_interview": "The participant kept the handbook concise with standard terminology and no glossary, although past AAR feedback had informally asked for clearer explanations for evaluators outside core EM.",
      "effect_on_reasoning_or_decision": "The handbook likely remained less accessible to non-core evaluators, contributing to possible scoring inconsistencies.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've been doing this fifteen years, and I've used the same shorthand and scoring conventions across a lot of exercises. Time was short, so I kept the handbook concise — standard terminology, no glossary.",
          "evidence_explanation": "Shows the expert's perspective and the resulting decision to omit a glossary."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left.",
          "evidence_explanation": "Demonstrates the curse of knowledge: despite audience feedback, his own expert sense of standard terminology overrode the need for explanation."
        }
      ],
      "correction_or_counterevidence": "The prior AAR feedback was a warning rather than a correction; the participant explicitly did not prioritize it because the terms felt standard.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supports curse of knowledge; this label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieval corpus provided direct support mainly for anchoring; labels for availability heuristic, status quo bias, bias blind spot, salience bias, and curse of knowledge rest on general cognitive-science knowledge rather than retrieved passages.",
    "Analysis is based on a single retrospective participant account; no independent documentation of decisions or outcomes was available.",
    "Retrieved corpus snippets contain OCR artifacts and limited topical coverage."
  ]
}

