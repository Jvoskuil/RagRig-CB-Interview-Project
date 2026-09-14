# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a post-event learning review, not for disciplinary purposes, and you're free to skip anything you're not comfortable discussing. Can you start by telling me your role and what you were assigned that shift? Participant: Sure, no problem. I'm a field equipment operator, been doing this about eleven years now, mostly auxiliary systems. That shift I was assigned to restore AFW Pump Train B to service after maintenance had a check valve out for repair. Goal was straightforward: get the lineup verified, start the pump, run the post-maintenance test, and get it inside the surveillance window before the LCO clock ran out. Interviewer: Can you walk me through what happened, from the beginning? Participant: I got to the pump room after grabbing the surveillance procedure and the routine lineup checklist. I'd done this exact lineup more times than I can count, so I started working through it the way I always do, valve by valve, left side first, then across to the discharge header. Somewhere in there, the prior shift had mentioned during turnover that maintenance added an isolation valve downstream of the check valve for the repair, but it was just a quick verbal mention in passing, not something we sat down and reviewed. I kept moving through my normal sequence. When I got near where that valve should've been, I didn't stop to pull the work order attachment and check it — I just verified it looked roughly right and kept going. Found out afterward, when control room called down, that it wasn't lined up the way the updated paperwork called for. After we sorted that out, I started the pump. On startup, the bearing temperature RTD came up slightly above the normal band, not alarming, but above where I usually see it. My first thought honestly went back to the week before — we'd had a similar RTD on another pump throw a high reading that turned out to be a wiring fault, nothing physically wrong with the pump. So I figured this was probably the same kind of thing and didn't pull up the trend data right then. I just kept an eye on it informally and moved on with startup. A little later, doing my rounds near the pump coupling, I heard a pretty loud, intermittent knocking sound. That got my attention immediately, it's the kind of noise that makes you stop. I also noticed, if I think back on it, the temperature had drifted up a bit more on the local gauge, and there was a faint odor near the oil reservoir. But the noise was what stood out, so that's what I focused on and what I called up to the control room about. Interviewer: Let's slow down and go through the sequence again. What was the first point where you noticed something outside the routine? Participant: Really it was the turnover mention of the added valve, though at the time it didn't register as a big deal. Then the RTD reading on startup was the next thing. Then the noise during rounds. Then it all came together near the end when we had to decide whether to keep running or trip the train, with the surveillance window closing in under half an hour. Interviewer: Let's go through each of those decisions in more detail. Starting with the valve lineup — what information did you have in front of you at that point? Participant: I had the standard checklist, the verbal mention from turnover about the new valve, and technically the work order attachment was available if I'd gone looking for it. Interviewer: What made you proceed with the standard sequence instead of stopping to check the attachment? Participant: Honestly, it's just the sequence I run every time, it's second nature at this point. The mention at turnover registered, but it didn't trigger me to break from the pattern. I've done that lineup so many times the same way, my hands almost know it before my head catches up. Interviewer: Had you handled an added or modified valve in a lineup before? Participant: Occasionally, yeah, and usually turnover flags it clearly enough that I stop. This time it came up quick, almost an afterthought, and I didn't treat it any differently than a normal round. Interviewer: Moving to the bearing temperature reading — what sources of information did you check, and which did you not check? Participant: I checked the immediate RTD reading, which was slightly elevated. I did not pull the fifteen-minute trend from the plant computer, even though it was right there available. I relied more on remembering that other pump's issue from the week before. Interviewer: How confident were you that this was the same kind of issue? Participant: Confident enough to not escalate it right away, but not certain. If you'd asked me right then, I'd have said probably instrumentation again, but I couldn't have shown you data to back that up. Interviewer: Let's talk about the noise, temperature drift, and odor. What made you center your report on the noise? Participant: It's just impossible to ignore, it's loud, it's rhythmic, it sounds mechanical and wrong. The temperature drift was smaller and only visible if you were looking right at the local gauge, and the odor was faint enough that I almost second-guessed whether I was smelling anything at all. So naturally the noise is what I led with on the radio. Interviewer: Did you weigh the three cues equally before reporting? Participant: Not really equally, no. I mentioned the other two, but briefly, more like a footnote to the noise call. Interviewer: Now the final decision — continue running or trip and swap trains. What did that look like? Participant: We had maybe under thirty minutes left in the window. I had a partial picture — noise that turned out later to be a loose coupling guard, a temperature that had crept up some more, and that odor still there. Swapping trains meant coordination, paperwork, and possibly missing the window entirely. The Shift Technical Advisor was tied up on another issue. I put together what I had, decided it was workable, and kept the train running to finish the test on schedule. Interviewer: Did you consider pulling a full vibration spectrum or an oil sample before deciding? Participant: I thought about it, yeah. There probably was time if I'd pushed for it, but between the clock and coordinating with everyone else, I went with what I already had rather than chasing every possible check. Interviewer: Was there a quicker option available — say, a fast local vibration reading or a quick radio consultation with someone in the control room — that might have told you within a few minutes whether this was the loose guard or something developing in the bearing itself? Participant: Looking back, yeah, there probably was. A quick local vibration check wouldn't have taken long, and I could have gotten someone on the radio to sanity-check what I was seeing. I didn't actually ask whether that was doable in the moment — once I had the pieces I'd already gathered, it felt like enough to keep going, so I didn't stop to find out if a faster check could have fit inside the window. Interviewer: If the work order attachment had been physically handed to you at turnover instead of just mentioned, do you think anything would have changed? Participant: Probably. If it's in my hand, I'm looking at it. Verbal mentions in a busy turnover just don't stick the same way. Interviewer: If that other pump's false alarm hadn't happened the week before, would you have responded to the RTD differently? Participant: That's a fair question. I think I might have pulled the trend sooner instead of assuming it was the same story. Interviewer: If the knocking noise had been quieter, do you think the temperature trend would have gotten more attention? Participant: Probably, yeah. It's hard not to chase the loudest thing in the room first. Interviewer: Looking back, is there anything you'd do differently with the same information you had at the time? Participant: I'd probably slow down at the valve lineup regardless of how routine it feels, and I'd pull the trend data earlier instead of leaning on what happened last week. The bearing ended up needing unplanned maintenance for degrading lubrication, so there was more going on than I gave it credit for in the moment.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.50s · gen 229.44s · total 234.7s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0289 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0280 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0249 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0240 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0230 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
6. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0224 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0222 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0222 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0219 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
10. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0209 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0209 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0205 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
13. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0204 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
14. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0202 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0199 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0197 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0189 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
19. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0186 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
20. **Lyell Automation bias and verification complexity.pdf** — 0.0186 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
21. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0185 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
24. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0172 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0158 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
29. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0156 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
33. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
34. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0150 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
36. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0149 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
37. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
38. **Lyell Automation bias and verification complexity.pdf** — 0.0144 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
40. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0143 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0142 (rrf) — _## Uwe Dulleck, PhD | | randomly drawn from the discrete uniform distribution [0,1, 2, 3 … , 30]_
42. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0141 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
43. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 388 tasks as oppos_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
45. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0137 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0132 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
48. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0132 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Summary The studie_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0131 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
50. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0131 (rrf) — _## Uwe Dulleck, PhD | nurses often observe and incorporate nonverbal behaviors of patients | | |_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of a single post-event learning interview. The transcript was treated as the sole factual authority for identifying cognitive biases; retrieved passages were used only for terminology and mechanism validation. No experimental condition or counterfactual status was inferred."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "expectation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "salience bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "expectation bias",
      "alternative_labels": [
        "premature cognitive commitment",
        "routine bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to perceive, evaluate, or act on information in line with an existing expectation from prior experience, leading to incomplete verification of changed conditions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Valve lineup after maintenance modification",
      "decision_point_description": "After turnover mention of an added isolation valve, whether to stop and verify the work order attachment or continue the routine lineup sequence.",
      "affected_reasoning_operation": "verification and attention allocation",
      "bias_specific_mechanism": "The operator's highly practiced routine created a strong expectation that the lineup would be unchanged. This expectation reduced information seeking and led to superficial confirmation that the configuration 'looked roughly right' rather than checking the updated work order attachment.",
      "manifestation_in_interview": "The participant continued with the standard valve sequence despite recalling the verbal turnover mention of the added isolation valve and did not pull the available work order attachment.",
      "effect_on_reasoning_or_decision": "The valve was later found by the control room to be mislined relative to the updated paperwork, indicating that the operator's expectation-driven verification was inadequate.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd done this exact lineup more times than I can count, so I started working through it the way I always do, valve by valve, left side first, then across to the discharge header.",
          "evidence_explanation": "Shows that a highly practiced routine provided the prior expectation that shaped subsequent verification behavior."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I got near where that valve should've been, I didn't stop to pull the work order attachment and check it — I just verified it looked roughly right and kept going.",
          "evidence_explanation": "Demonstrates superficial verification consistent with expectation rather than active checking of updated information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, it's just the sequence I run every time, it's second nature at this point. The mention at turnover registered, but it didn't trigger me to break from the pattern. I've done that lineup so many times the same way, my hands almost know it before my head catches up.",
          "evidence_explanation": "Explicitly links the failure to check the modified valve to an expectation- and routine-driven pattern rather than a deliberate risk decision."
        }
      ],
      "correction_or_counterevidence": "The work order attachment was available but was not physically handed to the participant; the verbal turnover mention was brief. The participant also reports that on other occasions a clear turnover flag would have caused him to stop, indicating a contextual salience problem. However, the updated information was accessible and the modification was specifically mentioned, so the routine expectation was still the main distortion.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit-bias review names expectation bias among common cognitive biases in incident reports but does not provide a formal definition in the retrieved fragment. The Parasuraman and Manzey passage provides supporting mechanism language through premature cognitive commitment and mindless behavior from repeated exposure.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation , and in some cases multiple biases",
          "mechanism_supported_by_source": "Identifies expectation bias as a recognized cognitive bias in cockpit incident reports.",
          "relevance_to_this_occurrence": "Supports the use of the expectation bias label for a routine-based failure to adjust to a changed configuration."
        },
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation:  An Attentional Integration",
          "authors": "Parasuraman and Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Langer (1982) proposed that repeated exposure to the same experience leads people to engage in “automated” or “mindless” behavior.",
          "mechanism_supported_by_source": "Supports the mechanism of routine-driven, mindless behavior when a familiar procedure is repeated.",
          "relevance_to_this_occurrence": "Directly matches the participant's statement that the lineup was second nature and that he did not break from the pattern."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A judgment or probability estimate in which ease of recall of a salient prior instance strongly influences the assessment of the current situation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Bearing temperature RTD above normal band during pump startup",
      "decision_point_description": "Whether to pull the available 15-minute trend data and escalate the elevated RTD reading, or assume the reading reflected a repeat instrumentation fault and continue startup.",
      "affected_reasoning_operation": "diagnostic inference and information search",
      "bias_specific_mechanism": "The recent memory of a similar RTD high reading caused by a wiring fault was highly available and led the participant to infer the current elevated RTD was probably the same kind of instrumentation issue. This ease of recall substituted for obtaining diagnostic trend data.",
      "manifestation_in_interview": "The participant did not pull the available trend data and did not escalate, citing the prior week's similar RTD wiring fault as the reason.",
      "effect_on_reasoning_or_decision": "The decision to continue without trend analysis delayed recognition of degrading bearing lubrication, which later required unplanned maintenance.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought honestly went back to the week before — we'd had a similar RTD on another pump throw a high reading that turned out to be a wiring fault, nothing physically wrong with the pump. So I figured this was probably the same kind of thing and didn't pull up the trend data right then.",
          "evidence_explanation": "Explicitly shows that memory of a recent similar event drove the classification of the current reading and suppressed diagnostic information seeking."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Confident enough to not escalate it right away, but not certain. If you'd asked me right then, I'd have said probably instrumentation again, but I couldn't have shown you data to back that up.",
          "evidence_explanation": "Demonstrates that the judgment was based on recalled possibility rather than current system data, a hallmark of availability-based inference."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That's a fair question. I think I might have pulled the trend sooner instead of assuming it was the same story.",
          "evidence_explanation": "The participant's counterfactual supports the causal role of the recent prior event in shaping the hasty diagnostic assumption."
        }
      ],
      "correction_or_counterevidence": "The RTD reading was only slightly above the normal band and not alarming, so low urgency was reasonable. The prior wiring fault was also a genuine possible explanation. However, the participant did not check trend data that was readily available, and later acknowledged he could not support his assumption with data.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus specifically defines availability heuristic. The classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "salience bias",
      "alternative_labels": [
        "attentional bias",
        "vividness effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency for perceptually or emotionally prominent information to dominate attention and judgment over less salient but equally or more diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Rounds near pump coupling with noise, temperature drift, and odor",
      "decision_point_description": "Which cue to prioritize and emphasize when reporting the developing pump condition to the control room.",
      "affected_reasoning_operation": "cue weighting, attention allocation, and communication",
      "bias_specific_mechanism": "The loud, rhythmic knocking sound was highly salient and captured attention, while the smaller temperature drift and faint oil odor were less perceptually prominent. Cue weighting followed perceptual salience rather than diagnostic relevance.",
      "manifestation_in_interview": "The participant centered the report on the noise and mentioned the temperature drift and odor only briefly, as a footnote.",
      "effect_on_reasoning_or_decision": "The less salient temperature and lubrication-related cues were underweighted in the report and subsequent decision picture, contributing to delayed recognition of bearing lubrication degradation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I heard a pretty loud, intermittent knocking sound. That got my attention immediately, it's the kind of noise that makes you stop.",
          "evidence_explanation": "Identifies the loud knocking as the salient cue that dominated attention."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I also noticed, if I think back on it, the temperature had drifted up a bit more on the local gauge, and there was a faint odor near the oil reservoir. But the noise was what stood out, so that's what I focused on and what I called up to the control room about.",
          "evidence_explanation": "Shows that other cues were noticed but explicitly deprioritized based on their lower perceptual salience."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really equally, no. I mentioned the other two, but briefly, more like a footnote to the noise call.",
          "evidence_explanation": "Confirms unequal cue weighting in the communication."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. It's hard not to chase the loudest thing in the room first.",
          "evidence_explanation": "The participant himself describes the salience-driven attention allocation mechanism."
        }
      ],
      "correction_or_counterevidence": "The knocking noise was a real mechanical cue and was later attributed to a loose coupling guard, so prioritizing it was not irrational. The temperature drift and odor were subtle, so there is a plausible non-bias explanation for giving them less attention. This is why the confidence is low.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus specifically defines salience bias. The classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation error",
        "get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to continue with an original plan or course of action despite emerging cues that indicate the plan should be reassessed or changed.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final decision whether to continue running or trip and swap trains before the LCO window expired",
      "decision_point_description": "Whether to keep the train running to complete the test on schedule or stop and pursue additional checks or a train swap given the incomplete mechanical picture.",
      "affected_reasoning_operation": "risk assessment and decision under uncertainty",
      "bias_specific_mechanism": "Commitment to the original plan of restoring the train and finishing the test within the surveillance window led the participant to treat the partial information already gathered as sufficient and to avoid pursuing faster additional checks that could have disconfirmed the plan.",
      "manifestation_in_interview": "The participant decided the situation was workable and kept the train running, even though he had not checked whether a quick local vibration reading or radio consultation could have fit within the window.",
      "effect_on_reasoning_or_decision": "The train remained running with a developing bearing lubrication problem, and unplanned maintenance was later required. The decision was shaped by schedule completion rather than a fuller diagnostic picture.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We had maybe under thirty minutes left in the window. I had a partial picture — noise that turned out later to be a loose coupling guard, a temperature that had crept up some more, and that odor still there. Swapping trains meant coordination, paperwork, and possibly missing the window entirely. The Shift Technical Advisor was tied up on another issue. I put together what I had, decided it was workable, and kept the train running to finish the test on schedule.",
          "evidence_explanation": "Shows that schedule continuation and the burden of swapping trains shaped the decision to continue despite an acknowledged partial picture."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it, yeah. There probably was time if I'd pushed for it, but between the clock and coordinating with everyone else, I went with what I already had rather than chasing every possible check.",
          "evidence_explanation": "Confirms that additional diagnostic information was available in principle but was not pursued because continuation felt sufficient."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, yeah, there probably was. A quick local vibration check wouldn't have taken long, and I could have gotten someone on the radio to sanity-check what I was seeing. I didn't actually ask whether that was doable in the moment — once I had the pieces I'd already gathered, it felt like enough to keep going, so I didn't stop to find out if a faster check could have fit inside the window.",
          "evidence_explanation": "Demonstrates that the plan continuation mechanism, rather than an objective lack of feasible options, prevented additional information seeking."
        }
      ],
      "correction_or_counterevidence": "There was real schedule pressure with less than thirty minutes remaining, and swapping trains carried legitimate coordination burden. The Shift Technical Advisor was also occupied. These factors create a plausible time-pressure explanation, but the participant acknowledged that a faster diagnostic check was likely feasible and that he stopped considering alternatives once the existing picture felt sufficient.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit-bias review names plan continuation as a common cognitive bias in incident reports. The retrieved fragment does not provide a formal mechanism definition, but the label is directly supported.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation , and in some cases multiple biases",
          "mechanism_supported_by_source": "Identifies plan continuation as a recognized cognitive bias in incident reports.",
          "relevance_to_this_occurrence": "Supports the use of the plan continuation bias label for the decision to continue the original test despite incomplete and partly concerning diagnostic information."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was sparse and fragmented; several classifications rely on established general cognitive-science knowledge where no retrieved passage was available.",
    "The cockpit-bias source names expectation and plan continuation biases but does not supply detailed operational definitions in the retrieved fragments.",
    "Some cues and decisions may reflect interacting biases rather than fully separable mechanisms, so occurrence boundaries were assigned conservatively to the clearest mechanism.",
    "The interview is retrospective, so verbatim memory reports may be incomplete or reconstructed, though the analysis used only information available to the participant at the time."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a post-event learning review, not for disciplinary purposes, and you're free to skip anything you're not comfortable discussing. Can you start by telling me your role and what you were assigned that shift? Participant: Sure, no problem. I'm a field equipment operator, been doing this about eleven years now, mostly auxiliary systems. That shift I was assigned to restore AFW Pump Train B to service after maintenance had a check valve out for repair. Goal was straightforward: get the lineup verified, start the pump, run the post-maintenance test, and get it inside the surveillance window before the LCO clock ran out. Interviewer: Can you walk me through what happened, from the beginning? Participant: I got to the pump room after grabbing the surveillance procedure and the routine lineup checklist. I'd done this exact lineup more times than I can count, so I started working through it the way I always do, valve by valve, left side first, then across to the discharge header. Somewhere in there, the prior shift had mentioned during turnover that maintenance added an isolation valve downstream of the check valve for the repair, but it was just a quick verbal mention in passing, not something we sat down and reviewed. I kept moving through my normal sequence. When I got near where that valve should've been, I didn't stop to pull the work order attachment and check it — I just verified it looked roughly right and kept going. Found out afterward, when control room called down, that it wasn't lined up the way the updated paperwork called for. After we sorted that out, I started the pump. On startup, the bearing temperature RTD came up slightly above the normal band, not alarming, but above where I usually see it. My first thought honestly went back to the week before — we'd had a similar RTD on another pump throw a high reading that turned out to be a wiring fault, nothing physically wrong with the pump. So I figured this was probably the same kind of thing and didn't pull up the trend data right then. I just kept an eye on it informally and moved on with startup. A little later, doing my rounds near the pump coupling, I heard a pretty loud, intermittent knocking sound. That got my attention immediately, it's the kind of noise that makes you stop. I also noticed, if I think back on it, the temperature had drifted up a bit more on the local gauge, and there was a faint odor near the oil reservoir. But the noise was what stood out, so that's what I focused on and what I called up to the control room about. Interviewer: Let's slow down and go through the sequence again. What was the first point where you noticed something outside the routine? Participant: Really it was the turnover mention of the added valve, though at the time it didn't register as a big deal. Then the RTD reading on startup was the next thing. Then the noise during rounds. Then it all came together near the end when we had to decide whether to keep running or trip the train, with the surveillance window closing in under half an hour. Interviewer: Let's go through each of those decisions in more detail. Starting with the valve lineup — what information did you have in front of you at that point? Participant: I had the standard checklist, the verbal mention from turnover about the new valve, and technically the work order attachment was available if I'd gone looking for it. Interviewer: What made you proceed with the standard sequence instead of stopping to check the attachment? Participant: Honestly, it's just the sequence I run every time, it's second nature at this point. The mention at turnover registered, but it didn't trigger me to break from the pattern. I've done that lineup so many times the same way, my hands almost know it before my head catches up. Interviewer: Had you handled an added or modified valve in a lineup before? Participant: Occasionally, yeah, and usually turnover flags it clearly enough that I stop. This time it came up quick, almost an afterthought, and I didn't treat it any differently than a normal round. Interviewer: Moving to the bearing temperature reading — what sources of information did you check, and which did you not check? Participant: I checked the immediate RTD reading, which was slightly elevated. I did not pull the fifteen-minute trend from the plant computer, even though it was right there available. I relied more on remembering that other pump's issue from the week before. Interviewer: How confident were you that this was the same kind of issue? Participant: Confident enough to not escalate it right away, but not certain. If you'd asked me right then, I'd have said probably instrumentation again, but I couldn't have shown you data to back that up. Interviewer: Let's talk about the noise, temperature drift, and odor. What made you center your report on the noise? Participant: It's just impossible to ignore, it's loud, it's rhythmic, it sounds mechanical and wrong. The temperature drift was smaller and only visible if you were looking right at the local gauge, and the odor was faint enough that I almost second-guessed whether I was smelling anything at all. So naturally the noise is what I led with on the radio. Interviewer: Did you weigh the three cues equally before reporting? Participant: Not really equally, no. I mentioned the other two, but briefly, more like a footnote to the noise call. Interviewer: Now the final decision — continue running or trip and swap trains. What did that look like? Participant: We had maybe under thirty minutes left in the window. I had a partial picture — noise that turned out later to be a loose coupling guard, a temperature that had crept up some more, and that odor still there. Swapping trains meant coordination, paperwork, and possibly missing the window entirely. The Shift Technical Advisor was tied up on another issue. I put together what I had, decided it was workable, and kept the train running to finish the test on schedule. Interviewer: Did you consider pulling a full vibration spectrum or an oil sample before deciding? Participant: I thought about it, yeah. There probably was time if I'd pushed for it, but between the clock and coordinating with everyone else, I went with what I already had rather than chasing every possible check. Interviewer: Was there a quicker option available — say, a fast local vibration reading or a quick radio consultation with someone in the control room — that might have told you within a few minutes whether this was the loose guard or something developing in the bearing itself? Participant: Looking back, yeah, there probably was. A quick local vibration check wouldn't have taken long, and I could have gotten someone on the radio to sanity-check what I was seeing. I didn't actually ask whether that was doable in the moment — once I had the pieces I'd already gathered, it felt like enough to keep going, so I didn't stop to find out if a faster check could have fit inside the window. Interviewer: If the work order attachment had been physically handed to you at turnover instead of just mentioned, do you think anything would have changed? Participant: Probably. If it's in my hand, I'm looking at it. Verbal mentions in a busy turnover just don't stick the same way. Interviewer: If that other pump's false alarm hadn't happened the week before, would you have responded to the RTD differently? Participant: That's a fair question. I think I might have pulled the trend sooner instead of assuming it was the same story. Interviewer: If the knocking noise had been quieter, do you think the temperature trend would have gotten more attention? Participant: Probably, yeah. It's hard not to chase the loudest thing in the room first. Interviewer: Looking back, is there anything you'd do differently with the same information you had at the time? Participant: I'd probably slow down at the valve lineup regardless of how routine it feels, and I'd pull the trend data earlier instead of leaning on what happened last week. The bearing ended up needing unplanned maintenance for degrading lubrication, so there was more going on than I gave it credit for in the moment.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.58s · gen 234.63s · total 239.8s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0289 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0280 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0249 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0240 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0230 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
6. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0224 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0222 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0222 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0219 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
10. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0209 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0209 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0205 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
13. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0204 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
14. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0202 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0199 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0197 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0189 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
19. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0186 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
20. **Lyell Automation bias and verification complexity.pdf** — 0.0186 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
21. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0185 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
24. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0172 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0158 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
29. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0156 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
33. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
34. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0150 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
36. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0149 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
37. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
38. **Lyell Automation bias and verification complexity.pdf** — 0.0144 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
40. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0143 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0142 (rrf) — _## Uwe Dulleck, PhD | | randomly drawn from the discrete uniform distribution [0,1, 2, 3 … , 30]_
42. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0141 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
43. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 388 tasks as oppos_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
45. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0137 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0132 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
48. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0132 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Summary The studie_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0131 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
50. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0131 (rrf) — _## Uwe Dulleck, PhD | nurses often observe and incorporate nonverbal behaviors of patients | | |_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Focused on the participant's described reasoning during the shift: lineup verification after a maintenance-added valve, interpretation of an elevated bearing RTD, anomaly reporting during rounds, and the final continue-or-trip decision."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "premature cognitive commitment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "salience bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "premature cognitive commitment",
      "alternative_labels": ["mindless routine", "automated behavior", "routine-induced verification failure"],
      "taxonomy_status": "established_label",
      "bias_definition": "An attitude that develops when a person first encounters a device or task in a particular context and is then reinforced when reencountered the same way; repeated exposure leads to automated or mindless behavior.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Valve lineup following maintenance-added isolation valve",
      "decision_point_description": "Whether to stop and review the work order attachment for the added valve or continue the standard lineup sequence",
      "affected_reasoning_operation": "Attention and verification during procedural task",
      "bias_specific_mechanism": "Repeated exposure to the same lineup created a premature cognitive commitment, so the verbal change mention did not interrupt his automated sequence and he sampled less information than needed to verify the changed configuration.",
      "manifestation_in_interview": "He proceeded with his normal valve-by-valve sequence and verified the area only roughly rather than pulling the work order attachment.",
      "effect_on_reasoning_or_decision": "The added isolation valve was not verified against the updated paperwork and was later found mislined.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd done this exact lineup more times than I can count, so I started working through it the way I always do, valve by valve, left side first, then across to the discharge header.",
          "evidence_explanation": "Shows the repeated routine basis for his procedure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I got near where that valve should've been, I didn't stop to pull the work order attachment and check it — I just verified it looked roughly right and kept going.",
          "evidence_explanation": "Demonstrates incomplete verification of a changed component despite available work order information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, it's just the sequence I run every time, it's second nature at this point. The mention at turnover registered, but it didn't trigger me to break from the pattern. I've done that lineup so many times the same way, my hands almost know it before my head catches up.",
          "evidence_explanation": "Directly states the automated, mindless behavior and why the change cue did not disrupt it."
        }
      ],
      "correction_or_counterevidence": "The added valve was only mentioned verbally and in passing during turnover, so inadequate turnover communication and ordinary forgetting are plausible competing explanations.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and mechanism are taken directly from the retrieved Parasuraman and Manzey passage on premature cognitive commitment and mindless behavior.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman and Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Langer (1982) proposed that repeated exposure to the same experience leads people to engage in automated or mindless behavior. R. Parasuraman and colleagues (1993) therefore reasoned that automation that is unchanging in its reliability is more likely to induce complacency than is automation that varies. In this case, participants will be more likely to develop a premature cognitive commitment regarding the nature of the automation and its efficiency.",
          "mechanism_supported_by_source": "Repeated exposure to a stable routine produces automated or mindless behavior and a premature cognitive commitment, reducing information sampling and verification.",
          "relevance_to_this_occurrence": "Although the participant was not interacting with automation, the same mechanism of repeated exposure to a stable task led him not to verify the changed valve configuration."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": ["availability heuristic", "insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "People make estimates based on an initial answer or starting point and subsequently adjust from that anchor insufficiently.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting elevated bearing temperature RTD at startup",
      "decision_point_description": "Whether to investigate the elevated RTD trend or attribute it to the prior week's wiring fault and continue startup",
      "affected_reasoning_operation": "Diagnostic judgment and causal attribution",
      "bias_specific_mechanism": "The participant anchored on the immediately available previous case of a similar RTD wiring fault and did not sufficiently adjust or seek trend data to test the current reading.",
      "manifestation_in_interview": "He remembered the prior false alarm and concluded the current reading was probably instrumentation again without pulling the fifteen-minute trend.",
      "effect_on_reasoning_or_decision": "The RTD was not escalated initially; the bearing temperature later rose and the bearing required unplanned maintenance for degrading lubrication.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought honestly went back to the week before — we'd had a similar RTD on another pump throw a high reading that turned out to be a wiring fault, nothing physically wrong with the pump. So I figured this was probably the same kind of thing and didn't pull up the trend data right then.",
          "evidence_explanation": "Shows the prior event functioning as an initial anchor and the failure to seek current data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Confident enough to not escalate it right away, but not certain. If you'd asked me right then, I'd have said probably instrumentation again, but I couldn't have shown you data to back that up.",
          "evidence_explanation": "Demonstrates that he maintained the anchor despite lacking current supporting evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If that other pump's false alarm hadn't happened the week before, would you have responded to the RTD differently? That's a fair question. I think I might have pulled the trend sooner instead of assuming it was the same story.",
          "evidence_explanation": "The counterfactual supports the causal role of the previous event as the anchor for his judgment."
        }
      ],
      "correction_or_counterevidence": "He was not certain and kept an eye on it informally; the RTD was only slightly above normal, so a watch-and-wait response may also reflect ordinary uncertainty under a weak signal.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and mechanism are directly supported by the retrieved passage on anchoring and adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described by Tversky and Kahneman in 1974. In brief, people make estimates based on an initial answer, and adjustments from there based on additional information are typically insufficient. Although the phenomenon was initially described in terms of anchoring on initial values when arriving at numeric estimates, the results have been found to hold in more general cases.",
          "mechanism_supported_by_source": "An initial answer or starting point shapes the subsequent estimate, with insufficient adjustment.",
          "relevance_to_this_occurrence": "The participant anchored on the prior week's wiring-fault diagnosis and did not adjust sufficiently when the current RTD was elevated."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "salience bias",
      "alternative_labels": ["attentional bias", "salience effect", "vividness bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Salience bias occurs when perceptually or emotionally prominent information receives disproportionate weight or attention in judgment relative to less salient but potentially important information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reporting pump anomalies during rounds",
      "decision_point_description": "Whether to weigh noise, temperature drift, and odor equally in the report to the control room",
      "affected_reasoning_operation": "Cue weighting and communication decision",
      "bias_specific_mechanism": "The loud, rhythmic knocking sound captured attention disproportionately; he then led the report with the noise and treated the more subtle temperature drift and faint odor as footnotes, even though all were potentially relevant.",
      "manifestation_in_interview": "He stated that the noise stood out, focused on it, and mentioned the other cues only briefly rather than equally.",
      "effect_on_reasoning_or_decision": "The report emphasized the mechanical noise, which later turned out to be a loose coupling guard, while the degrading-lubrication cue from temperature and odor was underweighted.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I heard a pretty loud, intermittent knocking sound. That got my attention immediately, it's the kind of noise that makes you stop. I also noticed, if I think back on it, the temperature had drifted up a bit more on the local gauge, and there was a faint odor near the oil reservoir. But the noise was what stood out, so that's what I focused on and what I called up to the control room about.",
          "evidence_explanation": "Directly states that the salient noise drove focus and reporting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really equally, no. I mentioned the other two, but briefly, more like a footnote to the noise call.",
          "evidence_explanation": "Shows asymmetric weighting in his report."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the knocking noise had been quieter, do you think the temperature trend would have gotten more attention? Probably, yeah. It's hard not to chase the loudest thing in the room first.",
          "evidence_explanation": "Supports the salience mechanism by acknowledging that a quieter salient cue would have changed attention allocation."
        }
      ],
      "correction_or_counterevidence": "Loud mechanical noise is objectively important and may justify priority; the salience effect is inferred from his own description of underweighting other cues rather than from a clear decision error.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No suitable retrieved corpus passage specifically addressed salience or attentional capture; label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis", "continuation bias", "plan continuation error"],
      "taxonomy_status": "established_label",
      "bias_definition": "Plan continuation bias is the tendency to continue with an original plan or course of action despite indications that the plan should be reassessed or abandoned.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final decision to keep running or trip the train before surveillance window expired",
      "decision_point_description": "Whether to continue the post-maintenance test despite partial evidence of possible bearing or lubrication problems and a closing LCO window",
      "affected_reasoning_operation": "Decision to continue versus stop operation under uncertainty",
      "bias_specific_mechanism": "The participant was committed to completing the test within the surveillance window; he gathered partial information and treated it as sufficient to continue rather than reassessing the plan.",
      "manifestation_in_interview": "He decided the situation was workable and kept the train running to finish the test on schedule, without checking whether a faster local vibration reading or radio consultation could have fit into the window.",
      "effect_on_reasoning_or_decision": "The train continued running and the bearing degradation progressed, requiring unplanned maintenance.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We had maybe under thirty minutes left in the window. I had a partial picture — noise that turned out later to be a loose coupling guard, a temperature that had crept up some more, and that odor still there. Swapping trains meant coordination, paperwork, and possibly missing the window entirely.",
          "evidence_explanation": "Shows the cues and the pressure to complete the original plan within the window."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I put together what I had, decided it was workable, and kept the train running to finish the test on schedule.",
          "evidence_explanation": "Directly states continuation with the original plan despite partial diagnostic information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once I had the pieces I'd already gathered, it felt like enough to keep going, so I didn't stop to find out if a faster check could have fit inside the window.",
          "evidence_explanation": "Shows that he treated already-gathered information as sufficient and did not test whether safer, quicker checks were available."
        }
      ],
      "correction_or_counterevidence": "There was real time pressure, coordination burden, and limited advisory support; continuing may also reflect an operational trade-off rather than solely a cognitive bias.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit-cognition paper identifies plan continuation as a common cognitive bias in safety incidents, though the excerpt provides limited mechanism text.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation , and in some cases multiple biases ... plan continua runway excursions were the most common outcome.",
          "mechanism_supported_by_source": "The source supports plan continuation as a recognized cognitive bias associated with adverse outcomes, though it does not provide a full mechanism definition in the retrieved excerpt.",
          "relevance_to_this_occurrence": "The participant's continuation of the test schedule despite mounting anomalies matches the plan continuation pattern identified in the source."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a retrospective post-event account; later knowledge may color recall, but classifications are limited to reasoning described at the time.",
    "Salience bias was not supported by retrieved corpus passages and was classified using general cognitive-science knowledge.",
    "Differentiating bias from legitimate heuristic or time-pressured operational decision-making is inherently difficult.",
    "The retrieved sources were often partial excerpts rather than full texts, especially for plan continuation bias."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a post-event learning review, not for disciplinary purposes, and you're free to skip anything you're not comfortable discussing. Can you start by telling me your role and what you were assigned that shift? Participant: Sure, no problem. I'm a field equipment operator, been doing this about eleven years now, mostly auxiliary systems. That shift I was assigned to restore AFW Pump Train B to service after maintenance had a check valve out for repair. Goal was straightforward: get the lineup verified, start the pump, run the post-maintenance test, and get it inside the surveillance window before the LCO clock ran out. Interviewer: Can you walk me through what happened, from the beginning? Participant: I got to the pump room after grabbing the surveillance procedure and the routine lineup checklist. I'd done this exact lineup more times than I can count, so I started working through it the way I always do, valve by valve, left side first, then across to the discharge header. Somewhere in there, the prior shift had mentioned during turnover that maintenance added an isolation valve downstream of the check valve for the repair, but it was just a quick verbal mention in passing, not something we sat down and reviewed. I kept moving through my normal sequence. When I got near where that valve should've been, I didn't stop to pull the work order attachment and check it — I just verified it looked roughly right and kept going. Found out afterward, when control room called down, that it wasn't lined up the way the updated paperwork called for. After we sorted that out, I started the pump. On startup, the bearing temperature RTD came up slightly above the normal band, not alarming, but above where I usually see it. My first thought honestly went back to the week before — we'd had a similar RTD on another pump throw a high reading that turned out to be a wiring fault, nothing physically wrong with the pump. So I figured this was probably the same kind of thing and didn't pull up the trend data right then. I just kept an eye on it informally and moved on with startup. A little later, doing my rounds near the pump coupling, I heard a pretty loud, intermittent knocking sound. That got my attention immediately, it's the kind of noise that makes you stop. I also noticed, if I think back on it, the temperature had drifted up a bit more on the local gauge, and there was a faint odor near the oil reservoir. But the noise was what stood out, so that's what I focused on and what I called up to the control room about. Interviewer: Let's slow down and go through the sequence again. What was the first point where you noticed something outside the routine? Participant: Really it was the turnover mention of the added valve, though at the time it didn't register as a big deal. Then the RTD reading on startup was the next thing. Then the noise during rounds. Then it all came together near the end when we had to decide whether to keep running or trip the train, with the surveillance window closing in under half an hour. Interviewer: Let's go through each of those decisions in more detail. Starting with the valve lineup — what information did you have in front of you at that point? Participant: I had the standard checklist, the verbal mention from turnover about the new valve, and technically the work order attachment was available if I'd gone looking for it. Interviewer: What made you proceed with the standard sequence instead of stopping to check the attachment? Participant: Honestly, it's just the sequence I run every time, it's second nature at this point. The mention at turnover registered, but it didn't trigger me to break from the pattern. I've done that lineup so many times the same way, my hands almost know it before my head catches up. Interviewer: Had you handled an added or modified valve in a lineup before? Participant: Occasionally, yeah, and usually turnover flags it clearly enough that I stop. This time it came up quick, almost an afterthought, and I didn't treat it any differently than a normal round. Interviewer: Moving to the bearing temperature reading — what sources of information did you check, and which did you not check? Participant: I checked the immediate RTD reading, which was slightly elevated. I did not pull the fifteen-minute trend from the plant computer, even though it was right there available. I relied more on remembering that other pump's issue from the week before. Interviewer: How confident were you that this was the same kind of issue? Participant: Confident enough to not escalate it right away, but not certain. If you'd asked me right then, I'd have said probably instrumentation again, but I couldn't have shown you data to back that up. Interviewer: Let's talk about the noise, temperature drift, and odor. What made you center your report on the noise? Participant: It's just impossible to ignore, it's loud, it's rhythmic, it sounds mechanical and wrong. The temperature drift was smaller and only visible if you were looking right at the local gauge, and the odor was faint enough that I almost second-guessed whether I was smelling anything at all. So naturally the noise is what I led with on the radio. Interviewer: Did you weigh the three cues equally before reporting? Participant: Not really equally, no. I mentioned the other two, but briefly, more like a footnote to the noise call. Interviewer: Now the final decision — continue running or trip and swap trains. What did that look like? Participant: We had maybe under thirty minutes left in the window. I had a partial picture — noise that turned out later to be a loose coupling guard, a temperature that had crept up some more, and that odor still there. Swapping trains meant coordination, paperwork, and possibly missing the window entirely. The Shift Technical Advisor was tied up on another issue. I put together what I had, decided it was workable, and kept the train running to finish the test on schedule. Interviewer: Did you consider pulling a full vibration spectrum or an oil sample before deciding? Participant: I thought about it, yeah. There probably was time if I'd pushed for it, but between the clock and coordinating with everyone else, I went with what I already had rather than chasing every possible check. Interviewer: Was there a quicker option available — say, a fast local vibration reading or a quick radio consultation with someone in the control room — that might have told you within a few minutes whether this was the loose guard or something developing in the bearing itself? Participant: Looking back, yeah, there probably was. A quick local vibration check wouldn't have taken long, and I could have gotten someone on the radio to sanity-check what I was seeing. I didn't actually ask whether that was doable in the moment — once I had the pieces I'd already gathered, it felt like enough to keep going, so I didn't stop to find out if a faster check could have fit inside the window. Interviewer: If the work order attachment had been physically handed to you at turnover instead of just mentioned, do you think anything would have changed? Participant: Probably. If it's in my hand, I'm looking at it. Verbal mentions in a busy turnover just don't stick the same way. Interviewer: If that other pump's false alarm hadn't happened the week before, would you have responded to the RTD differently? Participant: That's a fair question. I think I might have pulled the trend sooner instead of assuming it was the same story. Interviewer: If the knocking noise had been quieter, do you think the temperature trend would have gotten more attention? Participant: Probably, yeah. It's hard not to chase the loudest thing in the room first. Interviewer: Looking back, is there anything you'd do differently with the same information you had at the time? Participant: I'd probably slow down at the valve lineup regardless of how routine it feels, and I'd pull the trend data earlier instead of leaning on what happened last week. The bearing ended up needing unplanned maintenance for degrading lubrication, so there was more going on than I gave it credit for in the moment.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.18s · gen 222.89s · total 227.5s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0289 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0280 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0249 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0240 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0230 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
6. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0224 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0222 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0222 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0219 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
10. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0209 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0209 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0205 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
13. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0204 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
14. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0202 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0199 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0197 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0189 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
19. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0186 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
20. **Lyell Automation bias and verification complexity.pdf** — 0.0186 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
21. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0185 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
24. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0172 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0167 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0158 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
29. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0156 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
33. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
34. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0150 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
36. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0149 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
37. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
38. **Lyell Automation bias and verification complexity.pdf** — 0.0144 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
40. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0143 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0142 (rrf) — _## Uwe Dulleck, PhD | | randomly drawn from the discrete uniform distribution [0,1, 2, 3 … , 30]_
42. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0141 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
43. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 388 tasks as oppos_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
45. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0137 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0132 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
48. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0132 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Summary The studie_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0131 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
50. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0131 (rrf) — _## Uwe Dulleck, PhD | nurses often observe and incorporate nonverbal behaviors of patients | | |_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first analysis of a post-event CTA interview; only transcript-evidenced cognitive biases are reported, with retrieved passages used where topically and mechanistically relevant."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "premature cognitive commitment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "salience bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "premature cognitive commitment",
      "alternative_labels": [
        "mindless behavior",
        "expectation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive attitude formed during early exposure to a task or device and reinforced by repeated experience, leading to automated or mindless processing that fails to re-evaluate changed conditions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-maintenance valve lineup verification",
      "decision_point_description": "The participant continued the standard lineup sequence rather than stopping to pull the work order attachment and verify the newly added isolation valve.",
      "affected_reasoning_operation": "Verification and attention to updated work order for a modified valve lineup",
      "bias_specific_mechanism": "Repeated exposure to the same valve lineup created a premature cognitive commitment and mindless automatic processing, so the verbal turnover mention of the added valve did not interrupt the practiced sequence.",
      "manifestation_in_interview": "The participant recalled receiving a verbal mention of an added isolation valve but did not consult the work order attachment. He described the sequence as second nature and said the mention did not trigger him to break from the pattern.",
      "effect_on_reasoning_or_decision": "The valve was not lined up according to the updated paperwork, requiring later correction and delaying the post-maintenance test.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd done this exact lineup more times than I can count, so I started working through it the way I always do, valve by valve, left side first, then across to the discharge header.",
          "evidence_explanation": "Establishes the highly practiced routine that set the occasion for mindless sequence-following."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I got near where that valve should've been, I didn't stop to pull the work order attachment and check it — I just verified it looked roughly right and kept going.",
          "evidence_explanation": "Shows the critical verification step was skipped despite the available work order attachment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, it's just the sequence I run every time, it's second nature at this point. The mention at turnover registered, but it didn't trigger me to break from the pattern.",
          "evidence_explanation": "Directly links the routine automaticity to the failure to interrupt the standard pattern even after the changed condition was mentioned."
        }
      ],
      "correction_or_counterevidence": "The participant noted the turnover mention was quick and verbal rather than formally reviewed, and that normally a clearly flagged modification would have caused him to stop; this is a plausible communication/situational explanation, though the automaticity mechanism is also clearly present.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Parasuraman and Manzey material directly describes premature cognitive commitment and mindless behavior from repeated exposure, supporting the mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Langer's (1989) concept of “premature cognitive commitment,” defined as an attitude that develops when a person first encounters a device in a particular context and that is then reinforced when the device is reencountered in the same way. Langer (1982) proposed that repeated exposure to the same experience leads people to engage in “automated” or “mindless” behavior.",
          "mechanism_supported_by_source": "The source supports the mechanism that repeated exposure to a routine can produce automated, mindless behavior and premature cognitive commitment.",
          "relevance_to_this_occurrence": "The participant's description of the lineup as second nature and his failure to shift attention to the changed valve match this repeated-exposure/mindless-processing mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood or cause of an event by the ease with which similar instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation of elevated bearing temperature RTD",
      "decision_point_description": "When the pump bearing RTD read slightly above normal on startup, the participant attributed the reading to an instrumentation problem rather than pulling trend data for the current pump.",
      "affected_reasoning_operation": "Causal diagnosis and probability judgment for an elevated bearing temperature",
      "bias_specific_mechanism": "A recent similar RTD fault from the prior week was highly available in memory, so the participant judged the current elevated reading as likely the same kind of instrumentation issue without checking current trend data.",
      "manifestation_in_interview": "The participant immediately recalled another pump's recent wiring fault and concluded this was probably instrumentation again. He did not pull the available fifteen-minute trend and described himself as confident enough not to escalate, though not certain.",
      "effect_on_reasoning_or_decision": "The elevated bearing temperature was not investigated or escalated at that time; the bearing later required unplanned maintenance for degrading lubrication.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "On startup, the bearing temperature RTD came up slightly above the normal band, not alarming, but above where I usually see it. My first thought honestly went back to the week before — we'd had a similar RTD on another pump throw a high reading that turned out to be a wiring fault, nothing physically wrong with the pump. So I figured this was probably the same kind of thing and didn't pull up the trend data right then.",
          "evidence_explanation": "Explicitly shows that a recent similar instance came to mind, shaped the causal judgment, and led to not checking current data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Confident enough to not escalate it right away, but not certain. If you'd asked me right then, I'd have said probably instrumentation again, but I couldn't have shown you data to back that up.",
          "evidence_explanation": "Demonstrates the judgment was made from recalled similarity rather than supporting data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I might have pulled the trend sooner instead of assuming it was the same story.",
          "evidence_explanation": "Supports the causal link between the prior week's easily recalled false alarm and the current assumption."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged uncertainty and noted he could not support the judgment with data. He also informally kept an eye on the reading; later temperature drift and odor suggested a real bearing issue, but that information emerged later.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported availability heuristic; this occurrence relies on the widely established label from general knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "salience bias",
      "alternative_labels": [
        "attentional bias to salient cues",
        "salience effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to over-weight or attend disproportionately to prominent, vivid, or noticeable stimuli relative to less salient but potentially important information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reporting of abnormal pump cues during rounds",
      "decision_point_description": "After noticing knocking noise, elevated temperature, and faint odor, the participant chose to make the loud noise the central finding in his report to the control room.",
      "affected_reasoning_operation": "Cue integration and communication of abnormal plant indications",
      "bias_specific_mechanism": "The loud, rhythmic mechanical noise was perceptually dominant, so it captured attention and received disproportionate weight in the participant's appraisal and report while the smaller temperature drift and faint odor were relegated to brief footnotes.",
      "manifestation_in_interview": "The participant described the noise as impossible to ignore, acknowledged he did not weigh the three cues equally, and said temperature and odor were mentioned only briefly as a footnote to the noise call. He later agreed that a quieter noise would likely have led to more attention to the temperature trend.",
      "effect_on_reasoning_or_decision": "The control room received a report organized mainly around the loud mechanical noise, potentially delaying recognition of the bearing lubrication problem indicated by the temperature and odor cues.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But the noise was what stood out, so that's what I focused on and what I called up to the control room about.",
          "evidence_explanation": "Shows the salient cue became the focus of attention and reporting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It's just impossible to ignore, it's loud, it's rhythmic, it sounds mechanical and wrong. The temperature drift was smaller and only visible if you were looking right at the local gauge, and the odor was faint enough that I almost second-guessed whether I was smelling anything at all. So naturally the noise is what I led with on the radio.",
          "evidence_explanation": "Demonstrates the perceptual prominence of the noise, rather than a formal diagnostic comparison, drove the reporting emphasis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really equally, no. I mentioned the other two, but briefly, more like a footnote to the noise call.",
          "evidence_explanation": "Confirms the unequal weighting of cues in the report."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. It's hard not to chase the loudest thing in the room first.",
          "evidence_explanation": "Supports the salience mechanism operating on attention allocation."
        }
      ],
      "correction_or_counterevidence": "The noise was a real mechanical problem, later identified as a loose coupling guard, so focusing on it was not entirely erroneous; this provides a plausible non-bias explanation and justifies low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported salience bias; this occurrence relies on the widely established label from general knowledge.",
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
      "bias_definition": "A tendency to continue with an original plan or course of action despite cues, warnings, or evidence suggesting the need to change course or gather more information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final continue-vs-trip decision with surveillance window closing",
      "decision_point_description": "With under 30 minutes left in the surveillance window and an incomplete diagnostic picture, the participant decided to keep the pump running rather than stop to gather further data or trip/swap trains.",
      "affected_reasoning_operation": "Go/no-go decision and diagnostic information search under time pressure",
      "bias_specific_mechanism": "Commitment to completing the post-maintenance test on schedule and the closing LCO window produced a continuation set; the participant treated the information he already had as sufficient and did not pursue available, faster checks that could have disconfirmed his workability judgment.",
      "manifestation_in_interview": "The participant described keeping the train running to finish the test on schedule, acknowledged he considered vibration spectrum or oil sample checks but went with what he already had, and later said a quick local vibration check probably could have fit but he did not ask because the pieces already gathered felt like enough.",
      "effect_on_reasoning_or_decision": "The train was kept running on an incomplete picture; the bearing subsequently needed unplanned maintenance for degrading lubrication.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We had maybe under thirty minutes left in the window. I had a partial picture — noise that turned out later to be a loose coupling guard, a temperature that had crept up some more, and that odor still there. Swapping trains meant coordination, paperwork, and possibly missing the window entirely. The Shift Technical Advisor was tied up on another issue. I put together what I had, decided it was workable, and kept the train running to finish the test on schedule.",
          "evidence_explanation": "Shows continuation of the original test schedule despite an acknowledged partial diagnostic picture."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it, yeah. There probably was time if I'd pushed for it, but between the clock and coordinating with everyone else, I went with what I already had rather than chasing every possible check.",
          "evidence_explanation": "Demonstrates a satisficing decision to continue rather than use potentially diagnostic checks."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A quick local vibration check wouldn't have taken long, and I could have gotten someone on the radio to sanity-check what I was seeing. I didn't actually ask whether that was doable in the moment — once I had the pieces I'd already gathered, it felt like enough to keep going, so I didn't stop to find out if a faster check could have fit inside the window.",
          "evidence_explanation": "Strongly indicates premature closure and continuation with the existing plan rather than testing the assumption that the available information was sufficient."
        }
      ],
      "correction_or_counterevidence": "The STA was unavailable and the surveillance window created real time pressure, so the participant faced genuine operational constraints. However, the transcript also shows he did not test whether a faster check could fit, which supports the plan continuation mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage provided a clear definition of plan continuation bias; this occurrence relies on the widely established label from general knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was sparse for several labels; availability heuristic, salience bias, and plan continuation bias are classified using general-knowledge labels rather than retrieved passages.",
    "Some findings have plausible competing non-bias explanations such as weak turnover communication for the valve lineup and genuine time pressure for the final decision; confidence levels reflect these alternatives.",
    "The analysis is based on a single post-event recall account, so judgments are limited to the participant's described reasoning and may not capture real-time cognition exhaustively."
  ]
}

