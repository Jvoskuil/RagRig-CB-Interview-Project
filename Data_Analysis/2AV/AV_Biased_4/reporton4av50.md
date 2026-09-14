# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. As we discussed, this is a confidential debrief for training research purposes — I'll ask about a specific check ride, and I'd like you to walk me through what happened as concretely as you can. Nothing here goes into your personnel file. Sound okay? Participant: Sure, happy to talk through it. It was a Line Check, OPC cycle, on one of our senior widebody captains — guy's got probably twenty-two thousand hours, most of it on type. I was in the jump seat as the TRE. Interviewer: What was the flight supposed to accomplish, and what was your role exactly? Participant: Standard revenue flight, but I'm there to evaluate his technical handling and CRM for his recurrent check. First officer was PM. My job is to observe, grade, and intervene only if safety requires it. Interviewer: Take me through what actually happened, from the start. Participant: Before we even got to the airplane, I saw the tech log had two previous write-ups — ADIRU 2 miscompare, both times it cleared on its own, maintenance found nothing conclusive, and it came back MEL'd as okay to fly. So going in, I already had that context. We did the walk-around, briefed, nothing unusual. Departure was normal. Climbing out through about FL250, we got a brief ADIRU disagree indication on the EICAS — flickered for maybe ten seconds and went away. No checklist triggered automatically, so it wasn't like the system was demanding we do anything. Then in cruise, it came back, but this time it showed up as a disagreement between the captain's and first officer's airspeed and altitude tapes. That's more attention-getting because now you've got two primary displays disagreeing with each other, not just an internal comparator flag. The captain worked through it — cross-checked against the standby instruments, talked the FO through what he was seeing, and the indications came back together within a couple minutes. Rest of the flight was uneventful. Normal approach, normal landing. Interviewer: And afterward? Participant: I wrote up my report. Graded the captain's overall performance. A colleague of mine, another TRE, looked at the write-up informally and asked whether I'd been a little quick to wave things off given the fault's history. I pushed back on that. Then a few days later maintenance found an intermittent connector fault in the ADIRU wiring bay — that's likely what caused all three episodes. So there was an actual physical problem the whole time, it just wasn't consistent enough to nail down on the ground. Interviewer: Let's go back to that pre-departure moment. What went through your mind when you saw the tech log entries? Participant: Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further. Interviewer: Did you consider asking for another maintenance look before departure? Participant: Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going. Interviewer: What would have had to be different on paper for you to hold the flight? Participant: If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than 'checked, no fault found,' that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved. Interviewer: Move to the climb, when the flag flickered again. Walk me through that moment specifically. Participant: We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports. Interviewer: What alternative did you weigh at that point? Participant: Leveling off and running the full non-normal procedure, get maintenance control on the radio. I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting. Interviewer: How confident were you in that read at the time? Participant: Pretty confident, honestly. I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample. Interviewer: Let's talk about cruise, when the airspeed and altitude displays actually disagreed between the two pilots' instruments. What did you observe the captain do, and how did you evaluate it? Participant: He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either. Interviewer: How did you grade that? Participant: I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order. Interviewer: If a first-year captain had handled it the identical way, would you have graded it the same? Participant: Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work. Interviewer: Last one — the conversation with your colleague afterward. He suggested your calls that day might have been shaped by the crew's clean history. How did you respond to that? Participant: I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built. Interviewer: Is there anything that would change your mind about that day, looking back? Participant: If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made. Interviewer: Last question. If you ran this exact flight again with exactly the same information you had at the time, what would you do differently? Participant: Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.68s · gen 227.92s · total 231.8s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0296 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0289 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0275 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0272 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0265 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
6. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0202 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0200 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0199 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
9. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0193 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0186 (rrf) — _# 18, 72% It is interesting to observe that the CP, and in 1 bot h CP and FO had the same total _
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0184 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0177 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
16. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0175 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
17. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 18, 72% Overall, the data on flight crew experience does not suggest that having lower experie_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0172 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
20. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0172 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0170 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
22. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0168 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _# 18, 72% awareness to the outcome of the event 4.2.1 Relationship between flight crew experienc_
24. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0166 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 18, 72% t o their initial flight training and flight crew will often obtain various type ratin_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0165 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
27. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0164 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
30. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0156 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
33. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0155 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _## 16 5 | very low; 3 first officers (13.6%) and 2 captains (8.3%) | | , which suggests that dur_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
40. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 2 23 him to act precipitately leading to a number of mistakes, such as omissions in verificati_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0137 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
50. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0134 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "The transcript was assessed for affirmative, mechanism-grounded evidence of cognitive bias in the participant TRE's pre-departure reasoning, in-flight evaluation, and debrief reflections. Retrieved aviation human-factors passages were used where directly relevant."
  },
  "identified_bias_summary": [
    {
      "bias_label": "bias_blind_spot",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation_bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo_effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation_bias",
      "alternative_labels": [
        "expectation_bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in a way that confirms one's existing mental model or hypothesis while discounting contradictory evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-departure and climb interpretation of intermittent ADIRU fault",
      "decision_point_description": "Whether to treat the recurring ADIRU flag as benign and continue the climb rather than leveling off, consulting maintenance, or running the full non-normal procedure.",
      "affected_reasoning_operation": "Interpretation of ambiguous fault indications and risk assessment",
      "bias_specific_mechanism": "The participant formed a mental model from two prior self-clearing write-ups that the ADIRU fault was benign and self-contained. When the fault recurred in flight, he interpreted the transient EICAS flag and later display disagreement as confirming that model, used the limited prior history as justification to continue, and downgraded the possibility that an airborne recurrence was disconfirming evidence of an unresolved intermittent fault.",
      "manifestation_in_interview": "The participant describes the pre-departure history as making further inspection unnecessary and then describes the climb flag as 'there it is again, exactly like the tech log said.' Later he states the three brief occurrences felt like a clear pattern rather than a limited sample.",
      "effect_on_reasoning_or_decision": "Reduced vigilance and led to continuing the climb rather than pausing or running the non-normal checklist; the interim interpretation was treated as confirmation of a benign pattern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further.",
          "evidence_explanation": "Shows the formation of a benign prior belief from limited prior events and a reduced inclination to seek disconfirming maintenance evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.",
          "evidence_explanation": "Directly demonstrates assimilation of an ambiguous in-flight fault into the prior benign pattern and a decision to continue based on that interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.",
          "evidence_explanation": "Confirms the confidence arose from subjective pattern perception rather than statistically or diagnostically robust evidence."
        }
      ],
      "correction_or_counterevidence": "Maintenance had previously cleared the aircraft under the MEL, no checklist auto-triggered, and the participant did consider leveling off and consulting maintenance. These are legitimate operational factors and create a partial non-bias explanation. Later maintenance found an intermittent connector fault, but this was unknown at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved aviation-focused paper directly describes confirmation bias in cockpit events as interpretation of available cues as supporting the crew's mental model and ignoring evidence that would contradict the aircraft state.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "the investigation found that the visual cues available to the crew induced a state of confirmation bias which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft’s position.",
          "mechanism_supported_by_source": "Confirmation bias operates by using cues consistent with an existing mental model and ignoring contradictory evidence.",
          "relevance_to_this_occurrence": "The participant similarly interpreted the recurring ADIRU fault cues as consistent with his benign mental model and discounted the possibility that the airborne fault was contradictory evidence of an unresolved problem."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "halo_effect",
      "alternative_labels": [
        "halo_error"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A global positive impression of a person influences judgments about specific, unrelated attributes or behaviors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of captain's handling of in-flight ADIRU disagreement",
      "decision_point_description": "Whether to grade the captain's non-QRH standby-instrument response as satisfactory despite incomplete procedural verification.",
      "affected_reasoning_operation": "Performance evaluation and grading of technical/procedural behavior",
      "bias_specific_mechanism": "The participant's broad favorable impression of the captain's experience and track record generalized to the specific evaluation of procedural compliance. He explicitly weighted the captain's time on type and calm behavior more heavily than a step-by-step verification of the QRH, and stated that the same performance by a junior captain would be graded less generously.",
      "manifestation_in_interview": "The participant graded the captain satisfactory after he bypassed the QRH in favor of standby instruments from memory, saying the captain's track record does a lot of the work and that a first-year captain would not have received the same grade.",
      "effect_on_reasoning_or_decision": "Produced a person-dependent evaluative standard and likely lenient grade for a specific procedural deviation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either.",
          "evidence_explanation": "Establishes the specific behavioral target: the captain did not follow the QRH procedure in order."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order.",
          "evidence_explanation": "Shows that the global experience factor outweighed object-level procedural verification in the evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.",
          "evidence_explanation": "Directly demonstrates differential grading based on a global impression of the captain rather than identical performance."
        }
      ],
      "correction_or_counterevidence": "Expert pilots sometimes use memory-based cross-checks efficiently, and the fault resolved; however, the participant's own contrast with a junior captain indicates the standard was influenced by person-level reputation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly validated the halo effect. The classification relies on established general cognitive-science knowledge of the halo effect as an evaluation bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bias_blind_spot",
      "alternative_labels": [
        "bias_blindness"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize cognitive biases in others while failing to recognize one's own susceptibility to the same or similar biases.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to colleague's debrief feedback",
      "decision_point_description": "Whether to accept or reject the suggestion that his evaluations were shaped by the crew's clean history and his prior beliefs.",
      "affected_reasoning_operation": "Self-assessment of bias susceptibility and integration of peer feedback",
      "bias_specific_mechanism": "In response to peer feedback, the participant exempted himself from cognitive bias by citing his structured process and long record of no incidents, while attributing the same kind of bias risk to less experienced check-airmen. This self-other asymmetry is the defining mechanism of the bias blind spot.",
      "manifestation_in_interview": "He says the suggestion did not apply to him, that such bias is more of a risk for someone earlier in their check-airman career, and that he trusts the process he has built.",
      "effect_on_reasoning_or_decision": "Foreclosed corrective reflection and reduced the likelihood that peer feedback would update his evaluation standard.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.",
          "evidence_explanation": "Directly shows self-exemption from bias and attribution of bias susceptibility to a less experienced group, without engaging with the specific evidence."
        }
      ],
      "correction_or_counterevidence": "A structured process and extensive experience may reduce some errors, but they do not confer immunity; the use of a clean record as proof of objectivity is part of the biased reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly validated the bias blind spot. The classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "outcome_bias",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Retrospective reassessment of the same-day decisions",
      "supporting_interview_quote": "If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made.",
      "plausible_mechanism": "The participant's willingness to revise his evaluation appears partly contingent on a severe outcome—complete failure—rather than solely on the quality of the in-the-moment decision process.",
      "why_not_identified": "The participant also states that the ambiguous outcome does not prove the calls were right, so the evidence is mixed and insufficient to establish outcome bias affirmatively."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is self-reported and retrospective, so the analysis relies on the participant's description of his own cognition.",
    "Some retrieved passages concern aviation accident and incident reports rather than check-airman evaluation, so generalization to this evaluation context is indirect.",
    "The corpus provides direct support for confirmation bias, but support for halo effect and bias blind spot is absent and relies on established general cognitive-science knowledge.",
    "The boundaries between confirmation bias, expectation bias, and normalcy/plan-continuation bias overlap; a conservative separation was used to avoid over-counting."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. As we discussed, this is a confidential debrief for training research purposes — I'll ask about a specific check ride, and I'd like you to walk me through what happened as concretely as you can. Nothing here goes into your personnel file. Sound okay? Participant: Sure, happy to talk through it. It was a Line Check, OPC cycle, on one of our senior widebody captains — guy's got probably twenty-two thousand hours, most of it on type. I was in the jump seat as the TRE. Interviewer: What was the flight supposed to accomplish, and what was your role exactly? Participant: Standard revenue flight, but I'm there to evaluate his technical handling and CRM for his recurrent check. First officer was PM. My job is to observe, grade, and intervene only if safety requires it. Interviewer: Take me through what actually happened, from the start. Participant: Before we even got to the airplane, I saw the tech log had two previous write-ups — ADIRU 2 miscompare, both times it cleared on its own, maintenance found nothing conclusive, and it came back MEL'd as okay to fly. So going in, I already had that context. We did the walk-around, briefed, nothing unusual. Departure was normal. Climbing out through about FL250, we got a brief ADIRU disagree indication on the EICAS — flickered for maybe ten seconds and went away. No checklist triggered automatically, so it wasn't like the system was demanding we do anything. Then in cruise, it came back, but this time it showed up as a disagreement between the captain's and first officer's airspeed and altitude tapes. That's more attention-getting because now you've got two primary displays disagreeing with each other, not just an internal comparator flag. The captain worked through it — cross-checked against the standby instruments, talked the FO through what he was seeing, and the indications came back together within a couple minutes. Rest of the flight was uneventful. Normal approach, normal landing. Interviewer: And afterward? Participant: I wrote up my report. Graded the captain's overall performance. A colleague of mine, another TRE, looked at the write-up informally and asked whether I'd been a little quick to wave things off given the fault's history. I pushed back on that. Then a few days later maintenance found an intermittent connector fault in the ADIRU wiring bay — that's likely what caused all three episodes. So there was an actual physical problem the whole time, it just wasn't consistent enough to nail down on the ground. Interviewer: Let's go back to that pre-departure moment. What went through your mind when you saw the tech log entries? Participant: Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further. Interviewer: Did you consider asking for another maintenance look before departure? Participant: Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going. Interviewer: What would have had to be different on paper for you to hold the flight? Participant: If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than 'checked, no fault found,' that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved. Interviewer: Move to the climb, when the flag flickered again. Walk me through that moment specifically. Participant: We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports. Interviewer: What alternative did you weigh at that point? Participant: Leveling off and running the full non-normal procedure, get maintenance control on the radio. I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting. Interviewer: How confident were you in that read at the time? Participant: Pretty confident, honestly. I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample. Interviewer: Let's talk about cruise, when the airspeed and altitude displays actually disagreed between the two pilots' instruments. What did you observe the captain do, and how did you evaluate it? Participant: He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either. Interviewer: How did you grade that? Participant: I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order. Interviewer: If a first-year captain had handled it the identical way, would you have graded it the same? Participant: Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work. Interviewer: Last one — the conversation with your colleague afterward. He suggested your calls that day might have been shaped by the crew's clean history. How did you respond to that? Participant: I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built. Interviewer: Is there anything that would change your mind about that day, looking back? Participant: If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made. Interviewer: Last question. If you ran this exact flight again with exactly the same information you had at the time, what would you do differently? Participant: Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.69s · gen 204.05s · total 207.8s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0296 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0289 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0275 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0272 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0265 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
6. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0202 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0200 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0199 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
9. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0193 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0186 (rrf) — _# 18, 72% It is interesting to observe that the CP, and in 1 bot h CP and FO had the same total _
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0184 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0177 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
16. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0175 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
17. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 18, 72% Overall, the data on flight crew experience does not suggest that having lower experie_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0172 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
20. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0172 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0170 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
22. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0168 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _# 18, 72% awareness to the outcome of the event 4.2.1 Relationship between flight crew experienc_
24. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0166 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 18, 72% t o their initial flight training and flight crew will often obtain various type ratin_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0165 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
27. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0164 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
30. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0156 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
33. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0155 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _## 16 5 | very low; 3 first officers (13.6%) and 2 captains (8.3%) | | , which suggests that dur_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
40. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 2 23 him to act precipitately leading to a number of mistakes, such as omissions in verificati_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0137 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
50. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0134 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the TRE/participant's reported reasoning during a line check debrief for evidence of cognitive biases. Retrieved corpus passages supported anchoring-and-adjustment and confirmation-bias labels; halo effect, bias blind spot, and outcome bias labels derive from general knowledge because no adequate retrieved corpus support was available for those specific labels."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "bias blind spot",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "outcome bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring bias",
        "anchoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which an initial value or starting point exerts excessive influence on subsequent estimates, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-departure review of tech log write-ups",
      "decision_point_description": "Deciding whether to conduct another maintenance look before departure",
      "affected_reasoning_operation": "Risk assessment and safety disposition before flight",
      "bias_specific_mechanism": "The participant's risk estimate was anchored by the two prior self-cleared write-ups and the existing maintenance disposition. He treated the maintenance history as a stable baseline and did not sufficiently adjust away from that anchor when considering whether the intermittent fault might still be unresolved.",
      "manifestation_in_interview": "The participant repeatedly described the prior history as making the fault seem like a known quantity and a non-issue, and said the history itself felt like the justification for going.",
      "effect_on_reasoning_or_decision": "The participant did not seek another maintenance look before departure and proceeded with the flight based on the prior self-clearing pattern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further.",
          "evidence_explanation": "This shows the participant treating the prior maintenance history as the central reference point for the current risk estimate, with little adjustment toward the possibility that an intermittent physical fault remained."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The history itself felt like the justification for going.",
          "evidence_explanation": "This directly states that the pre-existing pattern functioned as the decision anchor rather than triggering a fresh risk assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved.",
          "evidence_explanation": "This shows insufficient adjustment away from the initial interpretation, even though a non-conclusive intermittent fault could still be unresolved."
        }
      ],
      "correction_or_counterevidence": "The participant did briefly consider asking for another maintenance check, and the aircraft had been released under the MEL after prior maintenance review, which is a legitimate operational basis for proceeding. However, the subjective weight placed on the history as justification is consistent with anchoring.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and mechanism are supported by the retrieved corpus passage on anchoring and adjustment; see corpus_evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive Bias in the Verification and Validation of Space Flight Systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described by Tversky and Kahneman in 1974... In brief, it has been observed that people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, 'adjustments are typically insufficient.'",
          "mechanism_supported_by_source": "Initial values anchor subsequent estimates, and adjustments away from those anchors tend to be insufficient.",
          "relevance_to_this_occurrence": "The participant's pre-departure risk estimate was anchored by the prior maintenance disposition and self-clearing history, and his adjustment away from that anchor was insufficient when deciding whether the intermittent ADIRU fault required further attention."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "selective evidence interpretation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's pre-existing beliefs or expectations, while giving disproportionately little weight to disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Climb interpretation of brief ADIRU disagree flag",
      "decision_point_description": "Deciding whether to level off and run a full non-normal procedure",
      "affected_reasoning_operation": "Interpretation of an in-flight warning and escalation decision",
      "bias_specific_mechanism": "The participant interpreted an ambiguous new in-flight event as matching the prior benign pattern and used that interpretation to support continuing the climb, rather than treating the event as evidence that could disconfirm the assumed self-resolving pattern.",
      "manifestation_in_interview": "The participant described the first thought as 'there it is again, exactly like the tech log said' and told the captain to keep the climb going because it was 'the same thing we saw on the ground reports.'",
      "effect_on_reasoning_or_decision": "The participant did not level off or run the full non-normal procedure during the climb, treating the brief flag as confirmation of the prior benign pattern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.",
          "evidence_explanation": "This shows the participant fitting the new warning into the existing mental model rather than treating it as a fresh or potentially disconfirming signal."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting.",
          "evidence_explanation": "The participant uses the prior pattern as the dominant evidence against escalation, illustrating selective weighting of confirmatory history over the current flightdeck indication."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.",
          "evidence_explanation": "The participant recognizes retrospectively that a limited sample was overinterpreted as a clear pattern, which supports the presence of confirmatory interpretation at the time."
        }
      ],
      "correction_or_counterevidence": "The brief flag did clear, and no checklist auto-triggered, so some operational caution in pausing the climb may be legitimate. The captain also cross-checked standby instruments during the later cruise event. These are non-bias explanations for limited escalation, but they do not explain away the confirmation-based interpretation of the climb event.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and mechanism are supported by the retrieved corpus passage on confirmation bias in cockpit events; see corpus_evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit: A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "The crew's confirmation bias was supported by being able to visually identify cues that supported their mental model... which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft's position.",
          "mechanism_supported_by_source": "Operators interpret ambiguous cues as consistent with an existing mental model and ignore contradictory evidence, a confirmation-bias mechanism.",
          "relevance_to_this_occurrence": "The participant interpreted the brief climb EICAS disagree as matching the previous self-clearing episodes and used that interpretation to continue the climb rather than pursue disconfirming checks."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "halo effect",
      "alternative_labels": [
        "halo error",
        "experience-based leniency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which a global positive impression of a person influences judgments about specific, relatively unrelated traits or behaviors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-cruise grading of captain's non-checklist instrument cross-check",
      "decision_point_description": "Assigning a grade to the captain's handling of the instrument disagreement",
      "affected_reasoning_operation": "Performance evaluation of procedure adherence",
      "bias_specific_mechanism": "The participant's evaluation of the captain's specific QRH-compliance behavior was dominated by a global positive impression of the captain's extensive experience and calm performance, leading to a more lenient grade without verifying each checklist item.",
      "manifestation_in_interview": "The participant explicitly said he weighted the captain's time on type and real-time standby cross-check more heavily than a step-by-step review of the QRH sequence, and said he would not have graded a first-year captain the same way.",
      "effect_on_reasoning_or_decision": "The participant graded the captain's handling as satisfactory despite not verifying each QRH item in order, and acknowledged a double standard based on experience and track record.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order.",
          "evidence_explanation": "This shows the participant using the captain's global experience and calmness as a basis for grading a specific procedural behavior, while not verifying the specific procedural element."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.",
          "evidence_explanation": "This directly reveals a double standard: the same behavior would be graded more harshly for a less experienced captain, indicating the evaluation is influenced by the captain's halo rather than only the technical performance."
        }
      ],
      "correction_or_counterevidence": "The captain's experience and the real-time standby cross-check may be legitimately relevant to overall CRM and handling judgment. However, the participant's stated failure to verify each QRH item and the explicit difference for a first-year captain suggest the specific procedural grade was influenced by the halo effect.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The label 'halo effect' derives from general knowledge; no adequate retrieved corpus support for this specific label was available.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "bias blind spot",
      "alternative_labels": [
        "blind spot bias",
        "bias blindness"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize the influence of cognitive biases in others while failing to recognize their influence on one's own judgments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to colleague's feedback about possible bias",
      "decision_point_description": "Deciding whether to accept or reject the colleague's suggestion that the participant's calls may have been biased",
      "affected_reasoning_operation": "Self-assessment of susceptibility to bias",
      "bias_specific_mechanism": "The participant denied that the colleague's bias concern applied to him, attributing the risk to less experienced check airmen and citing his own structured process and incident-free record as protective factors.",
      "manifestation_in_interview": "The participant said the concern did not apply to him, described it as a risk for someone earlier in their check-airman career, and said he trusted the process he had built.",
      "effect_on_reasoning_or_decision": "The participant rejected the colleague's feedback and did not reconsider whether his decisions that day had been influenced by bias.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.",
          "evidence_explanation": "This is a clear expression of bias blind spot: the participant sees bias as a risk for less experienced others but not for himself, despite having just described decision processes consistent with several biases."
        }
      ],
      "correction_or_counterevidence": "A structured process and a long incident-free record may support some confidence, and the colleague's comment was informal. However, those factors do not rule out bias, and the participant's categorical self-exemption is the hallmark of the bias blind spot.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The label 'bias blind spot' derives from general knowledge; no adequate retrieved corpus support for this specific label was available.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "outcome bias",
      "alternative_labels": [
        "outcome effect",
        "resulting bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to evaluate the quality of a decision based on its outcome rather than on the quality of the reasoning process at the time the decision was made.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Retrospective assessment of decisions after intermittent connector fault found",
      "decision_point_description": "Deciding whether later maintenance findings and outcome change the evaluation of the participant's earlier decisions",
      "affected_reasoning_operation": "Retrospective evaluation of decision quality",
      "bias_specific_mechanism": "The participant indicated that his retrospective evaluation would change if the outcome had been more severe, implying that decision quality was being judged partly by the actual outcome rather than by the information and reasoning available at the time.",
      "manifestation_in_interview": "The participant said a complete failure would 'reframe everything,' while the fact that the flight stayed borderline and landed normally meant the later finding did not prove anything about his prior calls.",
      "effect_on_reasoning_or_decision": "The participant maintained that his prior decisions were largely justified and said he would probably not change much, partly because the actual outcome remained non-catastrophic.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made.",
          "evidence_explanation": "This suggests the participant's assessment of his prior decisions would have been affected by the severity of the outcome, a pattern consistent with outcome bias. The non-catastrophic outcome is treated as weak evidence against reconsidering the calls."
        }
      ],
      "correction_or_counterevidence": "The participant also expresses a legitimate epistemic caution: a later best-fit finding does not establish exactly how the intermittent fault would have behaved or proved the earlier decisions wrong. The outcome-bias interpretation is therefore less direct than the other findings.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The label 'outcome bias' derives from general knowledge; no adequate retrieved corpus support for this specific label was available.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on a single self-report interview and does not include independent flight-deck observation or flight data.",
    "Some retrieved corpus passages are partial snippets, and the available corpus support was not specific to every bias label.",
    "Several decisions may also have legitimate operational explanations, such as MEL release, no auto checklist trigger, and standard dispatcher constraints.",
    "The outcome-bias occurrence is indirect and is assigned low confidence because a plausible non-bias explanation exists for the participant's retrospective caution."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. As we discussed, this is a confidential debrief for training research purposes — I'll ask about a specific check ride, and I'd like you to walk me through what happened as concretely as you can. Nothing here goes into your personnel file. Sound okay? Participant: Sure, happy to talk through it. It was a Line Check, OPC cycle, on one of our senior widebody captains — guy's got probably twenty-two thousand hours, most of it on type. I was in the jump seat as the TRE. Interviewer: What was the flight supposed to accomplish, and what was your role exactly? Participant: Standard revenue flight, but I'm there to evaluate his technical handling and CRM for his recurrent check. First officer was PM. My job is to observe, grade, and intervene only if safety requires it. Interviewer: Take me through what actually happened, from the start. Participant: Before we even got to the airplane, I saw the tech log had two previous write-ups — ADIRU 2 miscompare, both times it cleared on its own, maintenance found nothing conclusive, and it came back MEL'd as okay to fly. So going in, I already had that context. We did the walk-around, briefed, nothing unusual. Departure was normal. Climbing out through about FL250, we got a brief ADIRU disagree indication on the EICAS — flickered for maybe ten seconds and went away. No checklist triggered automatically, so it wasn't like the system was demanding we do anything. Then in cruise, it came back, but this time it showed up as a disagreement between the captain's and first officer's airspeed and altitude tapes. That's more attention-getting because now you've got two primary displays disagreeing with each other, not just an internal comparator flag. The captain worked through it — cross-checked against the standby instruments, talked the FO through what he was seeing, and the indications came back together within a couple minutes. Rest of the flight was uneventful. Normal approach, normal landing. Interviewer: And afterward? Participant: I wrote up my report. Graded the captain's overall performance. A colleague of mine, another TRE, looked at the write-up informally and asked whether I'd been a little quick to wave things off given the fault's history. I pushed back on that. Then a few days later maintenance found an intermittent connector fault in the ADIRU wiring bay — that's likely what caused all three episodes. So there was an actual physical problem the whole time, it just wasn't consistent enough to nail down on the ground. Interviewer: Let's go back to that pre-departure moment. What went through your mind when you saw the tech log entries? Participant: Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further. Interviewer: Did you consider asking for another maintenance look before departure? Participant: Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going. Interviewer: What would have had to be different on paper for you to hold the flight? Participant: If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than 'checked, no fault found,' that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved. Interviewer: Move to the climb, when the flag flickered again. Walk me through that moment specifically. Participant: We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports. Interviewer: What alternative did you weigh at that point? Participant: Leveling off and running the full non-normal procedure, get maintenance control on the radio. I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting. Interviewer: How confident were you in that read at the time? Participant: Pretty confident, honestly. I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample. Interviewer: Let's talk about cruise, when the airspeed and altitude displays actually disagreed between the two pilots' instruments. What did you observe the captain do, and how did you evaluate it? Participant: He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either. Interviewer: How did you grade that? Participant: I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order. Interviewer: If a first-year captain had handled it the identical way, would you have graded it the same? Participant: Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work. Interviewer: Last one — the conversation with your colleague afterward. He suggested your calls that day might have been shaped by the crew's clean history. How did you respond to that? Participant: I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built. Interviewer: Is there anything that would change your mind about that day, looking back? Participant: If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made. Interviewer: Last question. If you ran this exact flight again with exactly the same information you had at the time, what would you do differently? Participant: Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.78s · gen 281.27s · total 285.2s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0296 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0289 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0275 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0272 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0265 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
6. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0202 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0200 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0199 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
9. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0193 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0186 (rrf) — _# 18, 72% It is interesting to observe that the CP, and in 1 bot h CP and FO had the same total _
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0184 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0177 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
16. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0175 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
17. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 18, 72% Overall, the data on flight crew experience does not suggest that having lower experie_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0172 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
20. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0172 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0170 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
22. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0168 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _# 18, 72% awareness to the outcome of the event 4.2.1 Relationship between flight crew experienc_
24. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0166 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 18, 72% t o their initial flight training and flight crew will often obtain various type ratin_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0165 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
27. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0164 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
30. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0156 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
33. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0155 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _## 16 5 | very low; 3 first officers (13.6%) and 2 captains (8.3%) | | , which suggests that dur_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
37. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
40. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 2 23 him to act precipitately leading to a number of mistakes, such as omissions in verificati_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0137 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# Foreword | F | ch | osen field, and fantasized about a day when it would satisfy the curiosity_
50. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0134 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focused on the participant's reported reasoning, decisions, and evaluation as a TRE during a check ride. Bias findings were limited to the participant's own affirmatively evidenced reasoning operations; the first officer's cognition was only reported second-hand and was not used to infer bias."
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
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Outcome bias",
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
        "Anchoring heuristic",
        "Insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information when making judgments, with insufficient adjustment from later information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-departure decision not to request additional maintenance after reviewing recurrent ADIRU write-ups",
      "decision_point_description": "Whether to hold the flight for another maintenance look or accept the existing MEL release",
      "affected_reasoning_operation": "Risk assessment and decision to depart",
      "bias_specific_mechanism": "The participant anchored on the initial maintenance disposition ('checked, no fault found') and the two prior self-clearing events. Later evidence that the same intermittent fault was recurring did not produce sufficient adjustment away from that initial benign anchor.",
      "manifestation_in_interview": "The participant described the recurrent ADIRU write-ups as a known quantity and said the history itself felt like justification for going. He briefly considered another maintenance check but dismissed it based on the prior no-fault-found disposition.",
      "effect_on_reasoning_or_decision": "He decided not to seek another maintenance look before departure, treating the unresolved recurring fault as a non-issue.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further.",
          "evidence_explanation": "This shows the initial maintenance/MEL release functioning as an anchor for judging the current safety of the recurring fault."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going.",
          "evidence_explanation": "This demonstrates insufficient adjustment away from the earlier checks despite the recurrence, with the prior history dominating the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than 'checked, no fault found,' that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved.",
          "evidence_explanation": "This shows the initial no-fault-found category and self-clearing pattern became the baseline for his risk judgment."
        }
      ],
      "correction_or_counterevidence": "He briefly considered another maintenance look; after the fact, maintenance found an intermittent connector fault, which he acknowledges.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved space-flight-systems passage directly supports the anchoring and adjustment heuristic.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The retrieved passage describes anchoring and adjustment as the finding that people make estimates based on an initial answer and then adjust from there based on additional information, with adjustments typically being insufficient.",
          "mechanism_supported_by_source": "The source explains the cognitive mechanism of anchoring and insufficient adjustment.",
          "relevance_to_this_occurrence": "The participant's initial MEL/no-fault-found disposition functioned as an anchor, and later recurrent symptoms did not sufficiently shift his risk assessment."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Expectation bias",
        "Positive test strategy"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms one's pre-existing beliefs or hypotheses, while giving disproportionately less consideration to alternative possibilities.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "In-flight interpretation of recurrent ADIRU disagree indications",
      "decision_point_description": "Whether to treat the climb and cruise ADIRU indications as benign recurrences or as new warning signs requiring interruption",
      "affected_reasoning_operation": "Diagnostic interpretation of new system indications",
      "bias_specific_mechanism": "The participant interpreted each new ADIRU occurrence as confirming an existing mental model that the fault was benign and self-limiting. He focused on matching features to the prior pattern rather than actively evaluating the disconfirming possibility that an intermittent fault could be worsening.",
      "manifestation_in_interview": "He reported that when the climb flag appeared he thought 'there it is again' and told the captain to keep climbing. He described three brief occurrences as feeling like a clear pattern rather than a limited sample.",
      "effect_on_reasoning_or_decision": "This reinforced his decision not to pause or run the full non-normal procedure and led him to minimize the later cruise disagreement.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.",
          "evidence_explanation": "This shows selective matching of the new event to the prior benign type rather than considering an alternative explanation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting.",
          "evidence_explanation": "The prior self-resolving pattern was used as confirming evidence against the alternative hypothesis that the fault warranted interruption."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.",
          "evidence_explanation": "This retrospectively acknowledges that a small consistent sample was over-read as diagnostic, consistent with confirmation-based pattern interpretation."
        }
      ],
      "correction_or_counterevidence": "He later acknowledges that three brief occurrences were not enough to know what an intermittent fault would do next; maintenance subsequently found an intermittent connector fault.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved aviation incident-analysis passage explicitly discusses confirmation bias in flight-deck interpretation.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit: A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "The retrieved passage describes flight crew confirmation bias as being supported by visual cues that matched their mental model and led them to ignore other evidence, such as aircraft instruments, that would contradict the aircraft's position.",
          "mechanism_supported_by_source": "The source describes confirmation bias as the use of supporting cues to preserve an existing mental model while ignoring contradictory evidence.",
          "relevance_to_this_occurrence": "Similarly, the participant used the earlier tech-log pattern as supporting evidence for his mental model that the ADIRU indications were benign, while underweighting the possibility that the intermittent fault was unresolved."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Halo effect",
      "alternative_labels": [
        "Experience-based leniency",
        "Expertise halo"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for an evaluator's overall positive impression of a person to influence judgments about specific attributes or behavior.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Grading the captain's cruise ADIRU response",
      "decision_point_description": "Whether to grade the captain's non-standard use of standby instruments and omission of ordered QRH review as satisfactory",
      "affected_reasoning_operation": "Performance evaluation",
      "bias_specific_mechanism": "A positive global impression of the captain based on his extensive experience and calm demeanor caused the participant to overweight those positive attributes when judging a specific procedural deficiency and to decline to verify compliance step-by-step.",
      "manifestation_in_interview": "The participant graded the captain satisfactory, explicitly stating he weighted extensive time on type and the real-time standby cross-check more heavily than ordered QRH review. He admitted he would not have been as generous to a first-year captain.",
      "effect_on_reasoning_or_decision": "The evaluation of a specific non-standard action was softened, and the participant did not check whether all QRH items had been met in order.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved.",
          "evidence_explanation": "This establishes the specific behavior being evaluated: a deviation from ordered QRH use."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order.",
          "evidence_explanation": "This shows the evaluator's global positive impression of the captain influencing the scoring of a specific procedural omission."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.",
          "evidence_explanation": "This demonstrates differential treatment based on the captain's experience track record, a signature of the halo effect."
        }
      ],
      "correction_or_counterevidence": "He acknowledged he would have graded a first-year captain differently, but he framed this as appropriate calibration to experience rather than as bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly supported halo effect; the label is assigned from established cognitive science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Bias blind spot",
      "alternative_labels": [
        "Illusion of objectivity"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize cognitive biases in others while failing to see their influence on oneself, often accompanied by the belief that one's own judgments are objective.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to a colleague's suggestion that the crew's history shaped his decisions",
      "decision_point_description": "Whether to accept or reject the possibility that his own calls were influenced by the crew's clean history",
      "affected_reasoning_operation": "Self-assessment of susceptibility to bias",
      "bias_specific_mechanism": "The participant recognized the risk in other, less experienced check airmen but denied it applied to himself, attributing his own immunity to his structured process and long record. This is a classic bias blind spot: detecting bias in others while failing to recognize it in oneself.",
      "manifestation_in_interview": "He told the colleague he did not think the bias applied to him, said such bias was more of a risk for earlier-career check airmen, and said he trusted his own process.",
      "effect_on_reasoning_or_decision": "This closed off updating or revision of his earlier judgments and deflected the colleague's challenge.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident.",
          "evidence_explanation": "This shows explicit denial that the bias could apply to him, with his own experience used as evidence of immunity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.",
          "evidence_explanation": "This demonstrates the asymmetry of recognizing the bias in others while exempting himself."
        }
      ],
      "correction_or_counterevidence": "The interviewer directly offered the colleague's challenge as a disconfirming perspective, but the participant rejected it.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly supported bias blind spot; the label is assigned from established cognitive science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Outcome bias",
      "alternative_labels": [
        "Outcome-dependent evaluation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the quality of a decision based primarily on its outcome rather than on the information and reasoning available at the time of the decision.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Retrospective evaluation of the day's decisions after learning the connector fault diagnosis",
      "decision_point_description": "Whether later outcome information should change his assessment of the decisions made during the flight",
      "affected_reasoning_operation": "Retrospective evaluation of prior decisions",
      "bias_specific_mechanism": "The participant evaluated the validity of his earlier calls by imagining a worse outcome, stating that complete failure of the connector fault would have reframed everything. This makes his retrospective assessment outcome-dependent rather than based primarily on the information available at the time.",
      "manifestation_in_interview": "He said a complete failure of the connector fault would reframe everything, but because the fault remained intermittent and borderline, he concluded that none of the evidence proved anything about his calls.",
      "effect_on_reasoning_or_decision": "This preserved his original decision assessment and reduced his motivation to revisit the quality of his earlier reasoning.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made.",
          "evidence_explanation": "This shows the evaluation of his prior decisions varying with the outcome rather than being anchored to the information available at the time of those decisions."
        }
      ],
      "correction_or_counterevidence": "No correction is present; the interviewer's next question about rerunning the flight with the same information does not challenge the outcome-dependent framing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly supported outcome bias; the label is assigned from established cognitive science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Continuation bias",
        "Get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Climb-phase decision to continue after ADIRU disagree indication",
      "supporting_interview_quote": "I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.",
      "plausible_mechanism": "The participant continued the original climb plan despite a new warning, possibly due to plan continuation tendency and the prior benign pattern.",
      "why_not_identified": "The evidence does not clearly distinguish this mechanism from a reasonable low-severity decision under uncertainty. The warning was brief, self-clearing, and triggered no checklist, so the conservative identification bar was not met."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Insensitivity to sample size",
      "alternative_labels": [
        "Belief in the law of small numbers",
        "Representativeness heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Interpretation of three similar ADIRU events as a reliable pattern",
      "supporting_interview_quote": "In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.",
      "plausible_mechanism": "The participant may have drawn a strong generalization from a small, non-random sample of transient events.",
      "why_not_identified": "This mechanism is closely intertwined with the identified confirmation bias and lacks a clearly separable effect on a distinct decision; reporting it separately would risk double-counting the same reasoning episode."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a self-report, so the participant's recall may be reconstructive.",
    "Retrieved corpus support for some labels, including halo effect, bias blind spot, and outcome bias, was not available in the provided passages; those labels rest on general cognitive science knowledge.",
    "The first officer's cognition was only reported second-hand and was not used to infer bias.",
    "The retrieved aviation passage was partially fragmented, so only its substantive content was summarized rather than quoted in full."
  ]
}

