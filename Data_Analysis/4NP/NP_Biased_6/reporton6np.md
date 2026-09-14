# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm looking to understand how you actually reasoned through the feedwater heater trend during the ascension test, not to evaluate your performance. Everything stays de-identified for training and procedure review purposes. Sound okay? Participant: Yeah, that's fine. I figured this was coming after the work order got written up. Interviewer: Good, let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend? Participant: Sure. We were about three hours into the ascension test, sitting around 90 percent power, working toward the dispatch commitment at end of shift. I was at the controls, doing my normal rounds on the trend recorders, and I caught that heater 1B outlet temperature had crept up about three degrees over maybe twenty minutes. Train 1A was steady, no issue there. No alarm, nothing outside our Tech Spec limit. My first thought honestly was, 'here we go again' — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it. Interviewer: What was going through your head at that point, in terms of goals and pressures? Participant: Main thing was getting to a hundred percent within the dispatch window — we had about two hours of slack at that point. I wasn't in a panic, but I was aware the schedule mattered. And with the calibration history sitting right there in my head, the drift didn't feel like something new. It felt like the same story playing out again. Interviewer: Let's reconstruct the timeline a bit before we get into the decisions themselves. After you first noticed the drift, what happened next? Participant: I logged it as consistent with the prior calibration pattern and kept going with the ascension sequence. About fifteen minutes later the trend was still creeping, still shallow, still inside limits. Then a bit after that — maybe forty minutes in total — a maintenance tech doing an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. Shortly after that call, the trend recorder actually started flattening out as we approached the final ascension step. Interviewer: Okay, let's go through this decision by decision. First one: when you saw that initial drift, what alternatives did you actually consider? Participant: There were really two options. Either treat it as the same calibration issue from last cycle and just keep trending, or treat it as something new and call for an independent instrument check, maybe get I&C down there. I went with the first. Interviewer: What made you settle on that one? Participant: The pattern matched what we'd seen before — small, slow rise, no other train affected, no alarm. When something lines up that cleanly with a known cause, it's hard not to read it that way. I didn't really see a strong reason to go pull I&C off what they were doing for something that already had an explanation on file. Interviewer: Did you consider what it would take to rule that explanation out? Participant: Not really, no. I suppose I could've asked for a quick independent check on the sensor loop, but at the time it seemed like it would've been overkill given what I was looking at. I didn't go back and check whether the specific signature we saw last cycle — the way that fault crept in — actually matched what I was seeing on 1B. I just saw 'same sensor, same shape' and moved on, since I was already treating it as the same event. Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available where you could've briefed the STA before continuing. What went into that call? Participant: The STA was right there, actually, just hadn't said anything to him yet about it. I remember thinking it 'felt manageable' — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing. Interviewer: Was the dispatch window part of that calculation? Participant: A little, yeah. Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet. Interviewer: Right after that, the technician's infrared call came in. Walk me through how you weighed that against what you were seeing on the trend recorder. Participant: That's the one I've gone back and forth on since. His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue. I had that graph in front of me continuously — I'd been watching it for almost an hour. His reading was a single handheld measurement, called in over the radio, and once the call ended I honestly wasn't holding it in my head the same way — my eyes kept going back to the display in front of me, not to what he'd said. Interviewer: How did you end up weighting the two? Participant: I leaned toward the trend data. Partly because it was the instrument I trust for that parameter, and partly because, honestly, he doesn't spend his day reading control room trends the way we do — his experience is more hands-on with the equipment itself, not with interpreting these signatures. I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off, but I also didn't stop to double-check my own read of the trend line the same way — I just logged his call as likely noise from the handheld device rather than something that changed my read on the situation. Interviewer: Did anything about that reasoning give you pause? Participant: A little, yeah. He's not wrong about heat exchangers — that's literally his specialty, probably more relevant to shell heating than what I look at day to day. But in the moment, my trend line just felt like the stronger evidence, and honestly there's something about hearing it from another operator — someone who sees the plant the way we see it in here — that would've landed differently than a radio call from the field, even with the same words. Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed rather than hold? Participant: At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle. Time was getting tighter on the dispatch commitment too. I didn't loop back to the technician's earlier call at that point — my attention was on the ascension step itself and whether the number in front of me supported moving forward. Given what I was looking at right then, it seemed like enough to go. Interviewer: Did you consider requesting a hold for independent verification before that step? Participant: I thought about it briefly, but between the schedule and what the trend was showing, it didn't seem necessary at the time. Interviewer: How much uncertainty did you feel across all of this? Participant: Some, especially after the tech's call. But nothing that crossed into 'this violates a limit' territory, so it stayed more like background noise than something driving the decisions. Interviewer: Let's close with a couple of hypotheticals. If that infrared call had come from another licensed operator instead of a maintenance tech, do you think you'd have weighed it differently? Participant: Probably, yeah. I think I'd have taken it more seriously right away rather than filing it as likely noise. Interviewer: And if the trend had kept climbing instead of flattening near the final step? Participant: Then I think I would've held and called the STA in properly. The flattening is honestly what let me feel okay proceeding. Interviewer: Last one — looking back, is there a point where, with the same information you had, you might've made a different call? Participant: Maybe the second one. I could've just briefed the STA early and let him weigh in, even without hard evidence something was wrong. It wouldn't have cost us much time, and it would've gotten another set of eyes on it before things went further. Interviewer: That's helpful, thank you. I think that covers everything I needed.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.06s · gen 328.69s · total 335.0s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0288 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0262 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0255 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0249 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0244 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0227 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
8. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0224 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0209 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0197 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0192 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
14. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0185 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0183 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
16. **Lyell Automation bias and verification complexity.pdf** — 0.0180 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
17. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0180 (rrf) — _# 3Results On this point, Rezazade Mehrizi et al. (2023) investigated how AI explainability tool_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
19. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0173 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0169 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0163 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0162 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0161 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
26. **Hallihan_etal_DTM_12.pdf** — 0.0157 (rrf) — _A: I’m thinking that the penguin’s feet really looks like the scrubber, I’m not really sure of t_
27. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
31. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
33. **Hallihan_etal_DTM_12.pdf** — 0.0154 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
34. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0153 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
36. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
37. **Lyell Automation bias and verification complexity.pdf** — 0.0150 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
39. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
41. **Hallihan_etal_DTM_12.pdf** — 0.0148 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
42. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0148 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
43. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0146 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias TOWARD A SYN THESIS OF COGNITIV_
44. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0146 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
47. **Hallihan_etal_DTM_12.pdf** — 0.0139 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0136 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0135 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "The transcript was treated as the sole factual authority for identifying biased reasoning. Retrieved literature was used mainly for label-level validation because the supplied passages are fragmentary and often do not provide full diagnostic definitions."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 2
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "hypothesis-confirming bias",
        "myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's existing hypothesis or prior belief while giving less weight to alternatives or disconfirming detail.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial classification of heater 1B outlet temperature drift",
      "decision_point_description": "Whether to treat the initial three-degree drift as a recurrence of the prior calibration deviation or as a new fault requiring independent instrument verification.",
      "affected_reasoning_operation": "Diagnosis and hypothesis-consistent evidence interpretation",
      "bias_specific_mechanism": "A prior calibration deviation on the same sensor was immediately salient, generating the hypothesis that the current drift was the same issue. The participant then read the ambiguous trend as fitting that known cause and did not seek disconfirming detail, such as whether the current signature actually matched the previous fault signature.",
      "manifestation_in_interview": "The participant reported thinking 'here we go again' and selected the calibration-deviation explanation without checking whether the specific prior signature matched the current trend.",
      "effect_on_reasoning_or_decision": "He did not call for an independent instrument check and continued the ascension sequence with an unverified but hypothesis-consistent explanation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought honestly was, 'here we go again' — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it.",
          "evidence_explanation": "Shows an existing prior event shaping the initial diagnostic hypothesis before disconfirming detail was sought."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The pattern matched what we'd seen before — small, slow rise, no other train affected, no alarm. When something lines up that cleanly with a known cause, it's hard not to read it that way. I didn't really see a strong reason to go pull I&C off what they were doing for something that already had an explanation on file.",
          "evidence_explanation": "Demonstrates pattern-matching to a known cause and dismissing the alternative of independent verification because a preferred explanation was already available."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go back and check whether the specific signature we saw last cycle — the way that fault crept in — actually matched what I was seeing on 1B. I just saw 'same sensor, same shape' and moved on, since I was already treating it as the same event.",
          "evidence_explanation": "Directly shows failure to seek diagnostic detail that could disconfirm the preferred calibration-recurrence hypothesis."
        }
      ],
      "correction_or_counterevidence": "The trend was still within limits and the prior calibration history was a legitimate hypothesis, not a fabricated one. However, the participant did not test the hypothesis against the prior fault signature before proceeding.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved O'Connor cockpit-bias source supplies label-level support for confirmation bias as an operational cognitive bias, but the supplied passage does not provide a formal mechanistic definition.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "The source identifies 'confirmation, expectation, and plan continuation' as common cognitive biases in aviation incident reports.",
          "mechanism_supported_by_source": "Supports confirmation bias as a recognized operational bias, though the supplied passage does not elaborate its cognitive mechanism.",
          "relevance_to_this_occurrence": "Labels confirmation bias as a plausible classification for an operator interpreting ambiguous plant data as consistent with a known prior cause."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation error",
        "get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an original plan or course of action despite emerging cues, uncertainty, or changing conditions that suggest the plan should be paused or reconsidered.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Discretionary hold-point decision before briefing the STA",
      "decision_point_description": "Whether to use an available hold point to brief the STA or continue the ascension sequence while the temperature trend was still rising slightly.",
      "affected_reasoning_operation": "Risk assessment and go/no-go decision under schedule pressure",
      "bias_specific_mechanism": "The dispatch window and momentum of the ascension sequence increased the attractiveness of continuing the original plan. The participant used a quick affective 'gut check' rather than formal hold-point criteria and deferred briefing the STA despite an unresolved trend.",
      "manifestation_in_interview": "The participant described the situation as 'manageable' and chose to keep momentum going rather than formally brief the STA.",
      "effect_on_reasoning_or_decision": "He continued the ascension sequence without an independent review at a discretionary hold point.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The STA was right there, actually, just hadn't said anything to him yet about it. I remember thinking it 'felt manageable' — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing.",
          "evidence_explanation": "Shows schedule pressure and momentum leading to an intuitive continuation decision instead of formal hold-point review."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A little, yeah. Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet.",
          "evidence_explanation": "Explicitly links the decision against stopping to schedule pace rather than to formal diagnostic assurance."
        }
      ],
      "correction_or_counterevidence": "The trend was still within limits and slowly rising, so continuing was not a rule violation. The participant also planned to mention the issue later, which partially mitigates, but does not eliminate, the biased deferral of review.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved O'Connor cockpit-bias source supplies label-level support for plan continuation bias, but the supplied passage does not detail its mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "The source identifies 'confirmation, expectation, and plan continuation' as common cognitive biases in aviation incident reports.",
          "mechanism_supported_by_source": "Supports plan continuation as a recognized operational bias, though the supplied passage does not elaborate its cognitive mechanism.",
          "relevance_to_this_occurrence": "Relevant to continued ascension progress despite an unresolved trend and schedule pressure."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "biased assimilation",
        "hypothesis-confirming evidence weighting"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to favor information that supports an already formed hypothesis and to discount, explain away, or avoid seeking information that disconfirms it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of maintenance technician's infrared scanner report",
      "decision_point_description": "Whether to treat the technician's report of localized 1B heater shell heating as disconfirming evidence for the calibration-deviation hypothesis or as handheld-device noise.",
      "affected_reasoning_operation": "Evidence weighting and integration of conflicting information",
      "bias_specific_mechanism": "Rather than treating the localized heating report as a cue that the calibration-deviation story might be incomplete, the participant rationalized it as ambient heat or scan-angle inconsistency. He did not request a second scan or baseline check, preserving the original hypothesis and discounting a potentially disconfirming operational signal.",
      "manifestation_in_interview": "He acknowledged that localized heating differed from simple sensor drift but still leaned toward the trend data and logged the infrared call as likely noise.",
      "effect_on_reasoning_or_decision": "The contradictory infrared report was not used to revise the situation assessment, and no follow-up scan or baseline check was requested.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue.",
          "evidence_explanation": "Shows recognition of a mismatched feature while still favoring the hypothesis-consistent trend display."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned toward the trend data. Partly because it was the instrument I trust for that parameter, and partly because, honestly, he doesn't spend his day reading control room trends the way we do — his experience is more hands-on with the equipment itself, not with interpreting these signatures. I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off, but I also didn't stop to double-check my own read of the trend line the same way — I just logged his call as likely noise from the handheld device rather than something that changed my read on the situation.",
          "evidence_explanation": "Demonstrates selective discounting of a disconfirming report and absence of disconfirmatory follow-up."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He's not wrong about heat exchangers — that's literally his specialty, probably more relevant to shell heating than what I look at day to day. But in the moment, my trend line just felt like the stronger evidence, and honestly there's something about hearing it from another operator — someone who sees the plant the way we see it in here — that would've landed differently than a radio call from the field, even with the same words.",
          "evidence_explanation": "Acknowledges the disconfirming report's relevance but still treats it as weaker than the hypothesis-consistent trend data."
        }
      ],
      "correction_or_counterevidence": "A single handheld infrared reading is legitimately less reliable than a continuously observed control-room trend, and the participant's caution about over-weighting it was not inherently unreasonable. However, the appropriate resolution would have been to obtain additional data; instead, he explained the report away.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved O'Connor source provides label-level support for confirmation bias, but the supplied passage does not provide detailed diagnostic criteria.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "The source identifies 'confirmation, expectation, and plan continuation' as common cognitive biases in aviation incident reports.",
          "mechanism_supported_by_source": "Supports confirmation bias as a recognized operational bias, though the supplied passage does not elaborate its cognitive mechanism.",
          "relevance_to_this_occurrence": "Relevant to the participant's discounting of an infrared report that conflicted with his existing calibration-deviation hypothesis."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation error",
        "get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an original plan or course of action despite unresolved conflicting information or uncertainty because the plan is already in motion and time pressure favors continuing.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final ascension step decision near 100 percent power",
      "decision_point_description": "Whether to hold for independent verification before the final step to 100 percent power or proceed based on the flattening trend and schedule pressure.",
      "affected_reasoning_operation": "Final go/no-go decision under conflicting prior information",
      "bias_specific_mechanism": "Schedule pressure and the momentum of the final ascension step narrowed attention toward the current trend display. The participant did not loop back to the unresolved infrared report and treated the flattening trend as sufficient to continue.",
      "manifestation_in_interview": "The participant proceeded without revisiting the technician's infrared call, citing the flattening trend and tighter dispatch timing.",
      "effect_on_reasoning_or_decision": "He made the final ascension step without independent verification or reconsideration of the earlier conflicting infrared report.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle. Time was getting tighter on the dispatch commitment too. I didn't loop back to the technician's earlier call at that point — my attention was on the ascension step itself and whether the number in front of me supported moving forward. Given what I was looking at right then, it seemed like enough to go.",
          "evidence_explanation": "Shows schedule pressure and plan momentum associated with not reconsidering the unresolved conflicting report."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it briefly, but between the schedule and what the trend was showing, it didn't seem necessary at the time.",
          "evidence_explanation": "Directly links the final decision to schedule and current trend rather than to a formal resolution of prior uncertainty."
        }
      ],
      "correction_or_counterevidence": "The flattening trend was a legitimate positive indicator, and the plant remained within limits. Therefore, a rational evidence-based decision to proceed is also plausible, which lowers confidence in this occurrence.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved O'Connor source provides label-level support for plan continuation bias, but the supplied passage does not detail its mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "The source identifies 'confirmation, expectation, and plan continuation' as common cognitive biases in aviation incident reports.",
          "mechanism_supported_by_source": "Supports plan continuation as a recognized operational bias, though the supplied passage does not elaborate its cognitive mechanism.",
          "relevance_to_this_occurrence": "Relevant to continuing the final ascension step under schedule pressure despite unresolved conflicting information."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved O'Connor passages are fragmentary and mention bias labels rather than providing detailed diagnostic criteria or mechanistic definitions.",
    "The analysis is based on retrospective self-report during a single interview, not direct observation of the operating environment or objective outcome data.",
    "No normative model of optimal information sampling was available, so classifications are based on the participant's described reasoning and the presence of bias-specific mechanisms.",
    "Single-interview data cannot independently establish causal links between the inferred cognitive mechanisms and operational outcomes."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm looking to understand how you actually reasoned through the feedwater heater trend during the ascension test, not to evaluate your performance. Everything stays de-identified for training and procedure review purposes. Sound okay? Participant: Yeah, that's fine. I figured this was coming after the work order got written up. Interviewer: Good, let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend? Participant: Sure. We were about three hours into the ascension test, sitting around 90 percent power, working toward the dispatch commitment at end of shift. I was at the controls, doing my normal rounds on the trend recorders, and I caught that heater 1B outlet temperature had crept up about three degrees over maybe twenty minutes. Train 1A was steady, no issue there. No alarm, nothing outside our Tech Spec limit. My first thought honestly was, 'here we go again' — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it. Interviewer: What was going through your head at that point, in terms of goals and pressures? Participant: Main thing was getting to a hundred percent within the dispatch window — we had about two hours of slack at that point. I wasn't in a panic, but I was aware the schedule mattered. And with the calibration history sitting right there in my head, the drift didn't feel like something new. It felt like the same story playing out again. Interviewer: Let's reconstruct the timeline a bit before we get into the decisions themselves. After you first noticed the drift, what happened next? Participant: I logged it as consistent with the prior calibration pattern and kept going with the ascension sequence. About fifteen minutes later the trend was still creeping, still shallow, still inside limits. Then a bit after that — maybe forty minutes in total — a maintenance tech doing an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. Shortly after that call, the trend recorder actually started flattening out as we approached the final ascension step. Interviewer: Okay, let's go through this decision by decision. First one: when you saw that initial drift, what alternatives did you actually consider? Participant: There were really two options. Either treat it as the same calibration issue from last cycle and just keep trending, or treat it as something new and call for an independent instrument check, maybe get I&C down there. I went with the first. Interviewer: What made you settle on that one? Participant: The pattern matched what we'd seen before — small, slow rise, no other train affected, no alarm. When something lines up that cleanly with a known cause, it's hard not to read it that way. I didn't really see a strong reason to go pull I&C off what they were doing for something that already had an explanation on file. Interviewer: Did you consider what it would take to rule that explanation out? Participant: Not really, no. I suppose I could've asked for a quick independent check on the sensor loop, but at the time it seemed like it would've been overkill given what I was looking at. I didn't go back and check whether the specific signature we saw last cycle — the way that fault crept in — actually matched what I was seeing on 1B. I just saw 'same sensor, same shape' and moved on, since I was already treating it as the same event. Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available where you could've briefed the STA before continuing. What went into that call? Participant: The STA was right there, actually, just hadn't said anything to him yet about it. I remember thinking it 'felt manageable' — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing. Interviewer: Was the dispatch window part of that calculation? Participant: A little, yeah. Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet. Interviewer: Right after that, the technician's infrared call came in. Walk me through how you weighed that against what you were seeing on the trend recorder. Participant: That's the one I've gone back and forth on since. His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue. I had that graph in front of me continuously — I'd been watching it for almost an hour. His reading was a single handheld measurement, called in over the radio, and once the call ended I honestly wasn't holding it in my head the same way — my eyes kept going back to the display in front of me, not to what he'd said. Interviewer: How did you end up weighting the two? Participant: I leaned toward the trend data. Partly because it was the instrument I trust for that parameter, and partly because, honestly, he doesn't spend his day reading control room trends the way we do — his experience is more hands-on with the equipment itself, not with interpreting these signatures. I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off, but I also didn't stop to double-check my own read of the trend line the same way — I just logged his call as likely noise from the handheld device rather than something that changed my read on the situation. Interviewer: Did anything about that reasoning give you pause? Participant: A little, yeah. He's not wrong about heat exchangers — that's literally his specialty, probably more relevant to shell heating than what I look at day to day. But in the moment, my trend line just felt like the stronger evidence, and honestly there's something about hearing it from another operator — someone who sees the plant the way we see it in here — that would've landed differently than a radio call from the field, even with the same words. Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed rather than hold? Participant: At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle. Time was getting tighter on the dispatch commitment too. I didn't loop back to the technician's earlier call at that point — my attention was on the ascension step itself and whether the number in front of me supported moving forward. Given what I was looking at right then, it seemed like enough to go. Interviewer: Did you consider requesting a hold for independent verification before that step? Participant: I thought about it briefly, but between the schedule and what the trend was showing, it didn't seem necessary at the time. Interviewer: How much uncertainty did you feel across all of this? Participant: Some, especially after the tech's call. But nothing that crossed into 'this violates a limit' territory, so it stayed more like background noise than something driving the decisions. Interviewer: Let's close with a couple of hypotheticals. If that infrared call had come from another licensed operator instead of a maintenance tech, do you think you'd have weighed it differently? Participant: Probably, yeah. I think I'd have taken it more seriously right away rather than filing it as likely noise. Interviewer: And if the trend had kept climbing instead of flattening near the final step? Participant: Then I think I would've held and called the STA in properly. The flattening is honestly what let me feel okay proceeding. Interviewer: Last one — looking back, is there a point where, with the same information you had, you might've made a different call? Participant: Maybe the second one. I could've just briefed the STA early and let him weigh in, even without hard evidence something was wrong. It wouldn't have cost us much time, and it would've gotten another set of eyes on it before things went further. Interviewer: That's helpful, thank you. I think that covers everything I needed.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.62s · gen 284.66s · total 291.0s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0288 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0262 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0255 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0249 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0244 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0227 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
8. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0224 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0209 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0197 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0192 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
14. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0185 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0183 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
16. **Lyell Automation bias and verification complexity.pdf** — 0.0180 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
17. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0180 (rrf) — _# 3Results On this point, Rezazade Mehrizi et al. (2023) investigated how AI explainability tool_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
19. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0173 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0169 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0163 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0162 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0161 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
26. **Hallihan_etal_DTM_12.pdf** — 0.0157 (rrf) — _A: I’m thinking that the penguin’s feet really looks like the scrubber, I’m not really sure of t_
27. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
31. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
33. **Hallihan_etal_DTM_12.pdf** — 0.0154 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
34. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0153 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
36. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
37. **Lyell Automation bias and verification complexity.pdf** — 0.0150 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
39. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
41. **Hallihan_etal_DTM_12.pdf** — 0.0148 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
42. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0148 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
43. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0146 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias TOWARD A SYN THESIS OF COGNITIV_
44. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0146 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
47. **Hallihan_etal_DTM_12.pdf** — 0.0139 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0136 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0135 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a single cognitive task analysis interview about reasoning during a feedwater heater temperature trend in an ascension test."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
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
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "Anchoring bias",
        "Anchoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The anchoring and adjustment heuristic: people form an estimate or interpretation based on an initial value or explanation, and subsequent adjustments from that anchor are typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial classification of heater 1B outlet temperature drift",
      "decision_point_description": "Choosing whether to interpret the drift as a known calibration issue versus treating it as something new and requesting an independent instrument check.",
      "affected_reasoning_operation": "Differential diagnosis / classification under uncertainty",
      "bias_specific_mechanism": "The prior-cycle calibration issue served as an available initial interpretation and anchor for the new temperature drift; the participant then compared only superficial features such as 'same sensor, same shape' and did not sufficiently adjust or verify that anchor.",
      "manifestation_in_interview": "The participant immediately categorized the drift as the same calibration deviation from the prior cycle, treated the pattern match as sufficient, and explicitly acknowledged not checking whether the prior fault signature actually matched the current trend.",
      "effect_on_reasoning_or_decision": "The participant selected the known-calibration explanation, logged the drift as consistent with the prior pattern, and did not call for an independent I&C check.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought honestly was, 'here we go again' — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it.",
          "evidence_explanation": "This shows the prior calibration event immediately becoming the initial interpretation for the new drift."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When something lines up that cleanly with a known cause, it's hard not to read it that way. I didn't really see a strong reason to go pull I&C off what they were doing for something that already had an explanation on file.",
          "evidence_explanation": "The participant treats superficial pattern match with a known cause as sufficient and does not actively seek evidence that would rule that explanation out."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go back and check whether the specific signature we saw last cycle — the way that fault crept in — actually matched what I was seeing on 1B. I just saw 'same sensor, same shape' and moved on, since I was already treating it as the same event.",
          "evidence_explanation": "This explicitly demonstrates insufficient adjustment away from the initial calibration anchor, even though the diagnostic signature had not been verified."
        }
      ],
      "correction_or_counterevidence": "Later in the interview, the participant acknowledged that he could have briefed the STA early and gotten another set of eyes, but this was retrospective and did not correct the initial classification.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label and mechanism are supported by a retrieved passage on anchoring and adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974 ... In brief, it has been obser people make estimates based on an initial answer, and adjustments from there based on additional information ... 'adjustments are typic insufficient.'",
          "mechanism_supported_by_source": "People form estimates based on an initial answer or anchor and subsequently adjust insufficiently from that anchor.",
          "relevance_to_this_occurrence": "The participant's initial calibration diagnosis anchored his reading of the new trend, and he made only a superficial comparison rather than sufficiently adjusting or verifying that initial interpretation."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Plan continuation error",
        "Get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an original course of action despite changing conditions or cues that suggest the plan should be reassessed or slowed.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Discretionary hold-point and final ascension step decisions",
      "decision_point_description": "Choosing whether to brief or hold for STA review as the trend continued and later flattened before the final power ascension step.",
      "affected_reasoning_operation": "Go/no-go continuation decision under uncertainty",
      "bias_specific_mechanism": "Commitment to reaching 100 percent power within the dispatch window, plus the momentum of the ascension sequence, led the participant to assess anomalous cues as manageable and to bypass formal hold-point review rather than reassessing the plan.",
      "manifestation_in_interview": "The participant described the situation as 'manageable,' did not formally work through hold-point criteria, and cited schedule pressure and the flattening trend as reasons to continue without looping back to the earlier conflicting infrared report.",
      "effect_on_reasoning_or_decision": "The participant did not brief the STA at the discretionary hold point and did not request a hold for independent verification before the final ascension step.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Main thing was getting to a hundred percent within the dispatch window — we had about two hours of slack at that point. I wasn't in a panic, but I was aware the schedule mattered.",
          "evidence_explanation": "This establishes the original plan and schedule commitment that later influenced continuation decisions."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking it 'felt manageable' — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing.",
          "evidence_explanation": "The participant used a quick gut check instead of formal hold-point criteria and explicitly chose to maintain momentum rather than stop for review."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A little, yeah. Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet.",
          "evidence_explanation": "This directly links the dispatch window and pace preservation to the decision not to stop."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle. Time was getting tighter on the dispatch commitment too. I didn't loop back to the technician's earlier call at that point — my attention was on the ascension step itself and whether the number in front of me supported moving forward. Given what I was looking at right then, it seemed like enough to go.",
          "evidence_explanation": "The participant continued the original ascension plan and did not reassess the conflicting field report as time pressure increased."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The flattening is honestly what let me feel okay proceeding.",
          "evidence_explanation": "The participant used the flattening trend as sufficient justification to proceed rather than applying a formal hold decision."
        }
      ],
      "correction_or_counterevidence": "The participant stated that if the trend had kept climbing near the final step, he would have held and called the STA in properly, and he retrospectively acknowledged he could have briefed the STA early.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus mentioned plan continuation as a bias in operational incidents but did not provide a sufficient definition or mechanism; the label is used from general cognitive-science and aviation-human-factors knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Expectation bias",
        "Selective information processing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior belief or hypothesis, while giving less weight to disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of maintenance technician's infrared field report",
      "decision_point_description": "Deciding whether the infrared reading changed the working diagnosis of sensor calibration drift.",
      "affected_reasoning_operation": "Evidence interpretation and information weighting",
      "bias_specific_mechanism": "The participant gave greater weight to the continuously observed trend recorder data that fit the calibration hypothesis and discounted a conflicting field-specialist report as likely noise without checking it, thereby preserving the existing interpretation.",
      "manifestation_in_interview": "The participant contrasted the technician's reading unfavorably with the trend recorder, attributed the field reading to ambient heat or scan-angle inconsistency, and did not request a second scan or re-check his own trend interpretation.",
      "effect_on_reasoning_or_decision": "The infrared evidence did not change the participant's working diagnosis or prompt independent verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue.",
          "evidence_explanation": "The participant recognized the conflicting information but immediately contrasted it with trend data that confirmed his prior calibration hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I had that graph in front of me continuously — I'd been watching it for almost an hour. His reading was a single handheld measurement, called in over the radio, and once the call ended I honestly wasn't holding it in my head the same way — my eyes kept going back to the display in front of me, not to what he'd said.",
          "evidence_explanation": "The participant's attention and trust remained with the confirming trend display, while the disconfirming field report was not mentally retained or weighted equally."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off, but I also didn't stop to double-check my own read of the trend line the same way — I just logged his call as likely noise from the handheld device rather than something that changed my read on the situation.",
          "evidence_explanation": "This shows one-sided skeptical treatment of the disconfirming field report while the confirming trend interpretation was not subjected to the same scrutiny."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that the technician's specialty was probably more relevant to shell heating and that a report from another licensed operator would likely have been taken more seriously, but this awareness did not correct the in-the-moment information weighting.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus did not provide a sufficient definition or mechanism for confirmation bias; the label is used from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Only one interview transcript was analyzed; no independent outcome or procedure data were available.",
    "The retrieved scientific passages were sparse for some labels, especially plan continuation bias and confirmation bias, so those labels rely on general cognitive-science and human-factors knowledge.",
    "The interview is retrospective and de-identified; it may omit contextual details that would affect interpretation of the reasoning."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm looking to understand how you actually reasoned through the feedwater heater trend during the ascension test, not to evaluate your performance. Everything stays de-identified for training and procedure review purposes. Sound okay? Participant: Yeah, that's fine. I figured this was coming after the work order got written up. Interviewer: Good, let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend? Participant: Sure. We were about three hours into the ascension test, sitting around 90 percent power, working toward the dispatch commitment at end of shift. I was at the controls, doing my normal rounds on the trend recorders, and I caught that heater 1B outlet temperature had crept up about three degrees over maybe twenty minutes. Train 1A was steady, no issue there. No alarm, nothing outside our Tech Spec limit. My first thought honestly was, 'here we go again' — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it. Interviewer: What was going through your head at that point, in terms of goals and pressures? Participant: Main thing was getting to a hundred percent within the dispatch window — we had about two hours of slack at that point. I wasn't in a panic, but I was aware the schedule mattered. And with the calibration history sitting right there in my head, the drift didn't feel like something new. It felt like the same story playing out again. Interviewer: Let's reconstruct the timeline a bit before we get into the decisions themselves. After you first noticed the drift, what happened next? Participant: I logged it as consistent with the prior calibration pattern and kept going with the ascension sequence. About fifteen minutes later the trend was still creeping, still shallow, still inside limits. Then a bit after that — maybe forty minutes in total — a maintenance tech doing an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. Shortly after that call, the trend recorder actually started flattening out as we approached the final ascension step. Interviewer: Okay, let's go through this decision by decision. First one: when you saw that initial drift, what alternatives did you actually consider? Participant: There were really two options. Either treat it as the same calibration issue from last cycle and just keep trending, or treat it as something new and call for an independent instrument check, maybe get I&C down there. I went with the first. Interviewer: What made you settle on that one? Participant: The pattern matched what we'd seen before — small, slow rise, no other train affected, no alarm. When something lines up that cleanly with a known cause, it's hard not to read it that way. I didn't really see a strong reason to go pull I&C off what they were doing for something that already had an explanation on file. Interviewer: Did you consider what it would take to rule that explanation out? Participant: Not really, no. I suppose I could've asked for a quick independent check on the sensor loop, but at the time it seemed like it would've been overkill given what I was looking at. I didn't go back and check whether the specific signature we saw last cycle — the way that fault crept in — actually matched what I was seeing on 1B. I just saw 'same sensor, same shape' and moved on, since I was already treating it as the same event. Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available where you could've briefed the STA before continuing. What went into that call? Participant: The STA was right there, actually, just hadn't said anything to him yet about it. I remember thinking it 'felt manageable' — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing. Interviewer: Was the dispatch window part of that calculation? Participant: A little, yeah. Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet. Interviewer: Right after that, the technician's infrared call came in. Walk me through how you weighed that against what you were seeing on the trend recorder. Participant: That's the one I've gone back and forth on since. His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue. I had that graph in front of me continuously — I'd been watching it for almost an hour. His reading was a single handheld measurement, called in over the radio, and once the call ended I honestly wasn't holding it in my head the same way — my eyes kept going back to the display in front of me, not to what he'd said. Interviewer: How did you end up weighting the two? Participant: I leaned toward the trend data. Partly because it was the instrument I trust for that parameter, and partly because, honestly, he doesn't spend his day reading control room trends the way we do — his experience is more hands-on with the equipment itself, not with interpreting these signatures. I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off, but I also didn't stop to double-check my own read of the trend line the same way — I just logged his call as likely noise from the handheld device rather than something that changed my read on the situation. Interviewer: Did anything about that reasoning give you pause? Participant: A little, yeah. He's not wrong about heat exchangers — that's literally his specialty, probably more relevant to shell heating than what I look at day to day. But in the moment, my trend line just felt like the stronger evidence, and honestly there's something about hearing it from another operator — someone who sees the plant the way we see it in here — that would've landed differently than a radio call from the field, even with the same words. Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed rather than hold? Participant: At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle. Time was getting tighter on the dispatch commitment too. I didn't loop back to the technician's earlier call at that point — my attention was on the ascension step itself and whether the number in front of me supported moving forward. Given what I was looking at right then, it seemed like enough to go. Interviewer: Did you consider requesting a hold for independent verification before that step? Participant: I thought about it briefly, but between the schedule and what the trend was showing, it didn't seem necessary at the time. Interviewer: How much uncertainty did you feel across all of this? Participant: Some, especially after the tech's call. But nothing that crossed into 'this violates a limit' territory, so it stayed more like background noise than something driving the decisions. Interviewer: Let's close with a couple of hypotheticals. If that infrared call had come from another licensed operator instead of a maintenance tech, do you think you'd have weighed it differently? Participant: Probably, yeah. I think I'd have taken it more seriously right away rather than filing it as likely noise. Interviewer: And if the trend had kept climbing instead of flattening near the final step? Participant: Then I think I would've held and called the STA in properly. The flattening is honestly what let me feel okay proceeding. Interviewer: Last one — looking back, is there a point where, with the same information you had, you might've made a different call? Participant: Maybe the second one. I could've just briefed the STA early and let him weigh in, even without hard evidence something was wrong. It wouldn't have cost us much time, and it would've gotten another set of eyes on it before things went further. Interviewer: That's helpful, thank you. I think that covers everything I needed.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.36s · gen 396.96s · total 401.8s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0288 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0262 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0255 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0249 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0244 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0227 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
8. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0224 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0209 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0197 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0192 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
14. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0185 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0183 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
16. **Lyell Automation bias and verification complexity.pdf** — 0.0180 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
17. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0180 (rrf) — _# 3Results On this point, Rezazade Mehrizi et al. (2023) investigated how AI explainability tool_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
19. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0173 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0169 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0163 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0162 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0161 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
26. **Hallihan_etal_DTM_12.pdf** — 0.0157 (rrf) — _A: I’m thinking that the penguin’s feet really looks like the scrubber, I’m not really sure of t_
27. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0157 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0155 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
31. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
33. **Hallihan_etal_DTM_12.pdf** — 0.0154 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
34. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0153 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
36. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
37. **Lyell Automation bias and verification complexity.pdf** — 0.0150 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
39. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
41. **Hallihan_etal_DTM_12.pdf** — 0.0148 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
42. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0148 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
43. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0146 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias TOWARD A SYN THESIS OF COGNITIV_
44. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0146 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
47. **Hallihan_etal_DTM_12.pdf** — 0.0139 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
49. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0136 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0135 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of participant reasoning during an ascension test feedwater heater trend. Only transcript-affirmed bias-specific mechanisms are classified; operational constraints such as dispatch schedule or within-limit readings are not treated as biases absent a distinct mechanism."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and Adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation Bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "In-group Bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Plan Continuation Bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring and Adjustment",
      "alternative_labels": ["Anchoring bias", "Anchoring heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information and to make insufficient adjustments from that anchor when later information arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial attribution of 1B heater outlet temperature drift",
      "decision_point_description": "When the participant noticed the 1B outlet temperature rise, he chose to classify it as the prior calibration deviation rather than as a new or unknown fault.",
      "affected_reasoning_operation": "Causal attribution and subsequent evidence weighting",
      "bias_specific_mechanism": "The prior calibration deviation on the exact sensor served as an anchor; the participant matched the current slow, small rise to that known event and did not sufficiently adjust away from the anchor when later evidence diverged.",
      "manifestation_in_interview": "The participant immediately recalled the previous calibration issue, interpreted the drift as the same story, did not compare the specific prior fault signature, and declined an independent instrument check.",
      "effect_on_reasoning_or_decision": "He selected the calibration-failure explanation, kept trending without independent verification, and later evaluated conflicting evidence through that anchored frame.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought honestly was, 'here we go again' — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it.",
          "evidence_explanation": "Shows the prior calibration issue immediately activated as the initial explanation and anchor for the current signal."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The pattern matched what we'd seen before — small, slow rise, no other train affected, no alarm. When something lines up that cleanly with a known cause, it's hard not to read it that way.",
          "evidence_explanation": "The participant explicitly anchored on the pattern matching a known cause rather than testing whether the current signature actually matched the prior fault."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I just saw 'same sensor, same shape' and moved on, since I was already treating it as the same event.",
          "evidence_explanation": "Shows insufficient adjustment/verification: the current event was assimilated to the anchor without checking the specific signature."
        }
      ],
      "correction_or_counterevidence": null,
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved passage directly describes the anchoring-and-adjustment mechanism and its typical insufficient adjustment; the label is well established.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "Describes anchoring as relying on an initial answer with typically insufficient adjustments from additional information.",
          "relevance_to_this_occurrence": "The participant relied on the prior calibration explanation as the initial answer and made insufficient adjustments despite later inconsistent infrared evidence."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Plan Continuation Bias",
      "alternative_labels": ["Get-there-itis", "Plan continuation"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an established plan or action sequence in the face of cues that suggest a reassessment or hold may be warranted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision not to hold or brief the STA before continuing ascension",
      "decision_point_description": "At a discretionary hold point and again before the final step to 100 percent, the participant chose to continue without a formal hold or immediate STA brief.",
      "affected_reasoning_operation": "Go/no-go continuation judgment",
      "bias_specific_mechanism": "The momentum of the ongoing ascension plan and dispatch schedule led the participant to keep moving even though the drift and the technician's infrared report remained unresolved.",
      "manifestation_in_interview": "The participant did not work through hold-point criteria formally, used a quick gut check, and cited slowing pace and schedule as reasons not to brief or hold.",
      "effect_on_reasoning_or_decision": "The STA was not briefed at the discretionary point and independent verification was not requested before the final power step.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking it 'felt manageable' — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing.",
          "evidence_explanation": "Shows the active ascension plan and schedule generated momentum; the participant explicitly chose to continue and defer briefing rather than use the hold point."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet.",
          "evidence_explanation": "Demonstrates that preserving the plan's pace influenced the decision not to brief, above a formal reassessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it briefly, but between the schedule and what the trend was showing, it didn't seem necessary at the time.",
          "evidence_explanation": "At the final decision point, the schedule and the existing plan continued to drive the go decision rather than resolving the open IR report."
        }
      ],
      "correction_or_counterevidence": "The temperature remained within technical limits and the participant was under a real dispatch commitment; both are legitimate operational factors that could support non-biased continuation. The bias-specific mechanism is seen in the explicit momentum and pace-preservation reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus mentions plan continuation in aviation incidents but does not provide a mechanism-level definition; the label is applied from general knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation Bias",
      "alternative_labels": ["Expectation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, favor, and recall information in ways that confirm one's existing belief or hypothesis while discounting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Weighing the maintenance technician's infrared report against the trend recorder",
      "decision_point_description": "After the technician reported elevated shell temperature, the participant had to decide whether to update his situation model or dismiss the report.",
      "affected_reasoning_operation": "Evidence evaluation and hypothesis updating",
      "bias_specific_mechanism": "The participant evaluated new information according to the already-adopted calibration-failure hypothesis: the smooth trend was treated as confirmatory, while the localized heating report was recast as ambient heat or scan-angle noise without a repeat scan or baseline check.",
      "manifestation_in_interview": "He described the trend shape as exactly the calibration pattern and logged the infrared call as likely noise rather than changing his read on the situation.",
      "effect_on_reasoning_or_decision": "The contradictory field report was not used to revise the situation model, and the participant proceeded toward the final ascension step without additional verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue.",
          "evidence_explanation": "The participant recognizes the disconfirming nature of the report but immediately counterweights it with information that fits his existing calibration hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off",
          "evidence_explanation": "Instead of testing the disconfirming report, he generated an alternative explanation that preserved the calibration belief and dismissed the evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle.",
          "evidence_explanation": "The flattening trend was interpreted selectively as confirmation of the calibration narrative, reinforcing the decision to proceed."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that the technician's specialty was relevant ('He's not wrong about heat exchangers — that's literally his specialty'), but this recognition did not change the weighting of the evidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus mentions confirmation bias in cockpit incidents but lacks a mechanism-level passage for this occurrence; the label is applied from general knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "In-group Bias",
      "alternative_labels": ["In-group favoritism"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to assign greater credibility or weight to information from individuals perceived as members of one's own group than to out-group members, even when content is held constant.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Credibility weighting of the maintenance technician's infrared call",
      "decision_point_description": "The participant had to determine how much weight to give to a field technician's report relative to how he would weigh the same report from another licensed operator.",
      "affected_reasoning_operation": "Source credibility assessment and evidence weight assignment",
      "bias_specific_mechanism": "The participant downgraded the technician's report partly because the technician was outside the control-room/operator group; he stated that the same words from another operator would have landed differently.",
      "manifestation_in_interview": "He cited the technician's lack of control-room trend interpretation experience and later confirmed that an operator source would have been taken more seriously 'even with the same words.'",
      "effect_on_reasoning_or_decision": "The perceived source group contributed to writing off the infrared report as likely noise without follow-up verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Partly because it was the instrument I trust for that parameter, and partly because, honestly, he doesn't spend his day reading control room trends the way we do — his experience is more hands-on with the equipment itself, not with interpreting these signatures.",
          "evidence_explanation": "Shows credibility assigned based on group/role category rather than solely on the physical evidence content."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "honestly there's something about hearing it from another operator — someone who sees the plant the way we see it in here — that would've landed differently than a radio call from the field, even with the same words.",
          "evidence_explanation": "Explicitly identifies a source-group effect on the weight he would give to identical information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. I think I'd have taken it more seriously right away rather than filing it as likely noise.",
          "evidence_explanation": "Confirms the differential response to the same information depending on the source's group membership."
        }
      ],
      "correction_or_counterevidence": "The participant noted the technician's relevant hands-on specialty, and some role-based credibility difference could reflect legitimate task-relevant expertise; however, the explicit same-words/operator statement indicates group membership itself affected weighting.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage provided a definition or mechanism for group/source-based credibility bias; the label is applied from general knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages are partially OCR-garbled and sparse; several labels rely on general cognitive-science knowledge with disclosure.",
    "The analysis is limited to the participant's self-reported reasoning; no independent behavioral or outcome data were available.",
    "Speaker attribution is clear, but source credibility and schedule-pressure findings depend on retrospective self-report."
  ]
}

