# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a internal case review on decision-making during admissions, and that I can ask follow-up questions as we go. Participant: Sure, that's fine. Happy to walk through it. Interviewer: Great. Can you tell me your role on the team during this admission? Participant: I was the attending on the general medicine service. I had a resident covering with me, and we picked up this patient on hospital day one after she came in for something unrelated and ended up with a new finding on her monitor. Interviewer: And what was your overall goal for her care during the stay? Participant: Mainly to get her diagnosis sorted out and make sure we sent her home with a safe, appropriate plan. She was 78, otherwise fairly independent, living with her daughter nearby. Interviewer: Can you walk me through what happened, from the diagnosis to discharge? Participant: She came in and the admission ECG showed she was in atrial fibrillation, which nobody had picked up before — persistent, not paroxysmal. That obviously changes the calculus for stroke prevention. Her CHA2DS2-VASc came out to 4, so her annual stroke risk if left untreated is meaningful. Her HAS-BLED was 2, which is moderate, not a red flag. Pharmacy checked and there were no interactions with the DOAC we'd typically use. But she'd had a fall about three weeks before admission — mechanical, tripped on a rug at home, no head strike, no fracture, fully worked up at the time. Still, when I saw 'fall' in the history, that gave me pause about starting a blood thinner right away. I told the team we'd hold off and get a formal fall-risk assessment first before committing to anything. Then on day two, one of the nurses mentioned, sort of in passing, that a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation. Understandably, that got around the unit, and my patient's daughter had heard a version of it too. She was in the room a lot and got increasingly anxious every time anticoagulation came up. Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated. That pushed our timeline back a day. By day three the CT was normal, and physical therapy had cleared her fall risk as low with a walker. So on paper the numbers were now clearly in favor of starting treatment. I remember standing at the nurses' station with the resident and just picturing what it would be like if we started her on this drug and then she had a major bleed — the conversation with the daughter, explaining that decision, how that would sit with all of us. It wasn't just that it would be bad; it felt like the kind of thing I'd still be replaying weeks later, something that would sit over the whole team and not really lift for a long time. That feeling seemed heavier to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge. Then on day four, right before discharge, she got a small bruise at her IV site — unrelated, since she wasn't even on anticoagulation yet. It didn't change anything about the plan; we finalized the discharge summary without a firm start plan, just a note to follow up as an outpatient. Interviewer: Let's slow down and go through each of those moments. At the first point, right after diagnosis — what stood out to you most? Participant: Honestly, the fall. Clinically I knew the scores favored treatment, but a recent fall in an older patient just registers as a flag. I didn't want to be the one who started a blood thinner and then she fell again and bled into her head. Interviewer: What alternatives did you consider there? Participant: We could have started the DOAC immediately since the scores supported it, or started a lower empirical dose. I chose to wait for a formal PT evaluation instead, even though the fall itself had already been worked up and looked mechanical. Interviewer: What was the main basis for waiting rather than starting treatment that day? Participant: I suppose not wanting to be the direct cause of a bad outcome. Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number. Interviewer: At the second point, with the daughter's anxiety and the CT — what were you trying to accomplish? Participant: Mostly to de-escalate the family's fear so we could have a productive conversation. In hindsight, I could have just walked through her individual numbers with the daughter instead of ordering imaging that wasn't clinically indicated. But it felt like having a normal scan in hand would make the conversation easier. Interviewer: How much time pressure did you feel making that call? Participant: Some — we were already tight on discharge planning, and adding a CT meant another day. But I felt like skipping that step would leave the family conversation unresolved. Interviewer: Move to the third point — after the CT came back normal and fall risk was cleared. What was going through your mind there? Participant: That's the one I keep coming back to. The data at that point was pretty clean — low fall risk, normal imaging, scores favoring treatment. But I remember describing to the resident, almost involuntarily, this scenario of her bleeding on a drug I'd started, and picturing it as something that wouldn't really fade — like it would color how the family saw us and how I thought about the case for a long stretch afterward. It wasn't really about the probability anymore. I decided to leave it for the outpatient team. Interviewer: What alternatives were on the table then? Participant: Starting it right there before discharge, starting a lower dose with a firm two-week follow-up, or deferring entirely, which is what I did. Interviewer: Had you handled a similar case before that shaped this decision? Participant: Not directly with this patient, but the ward story about the other patient's bleed was fresh in everyone's mind that week. Interviewer: At the fourth point, the bruise at discharge — how did that factor in? Participant: It didn't really change the clinical picture, since she wasn't even on the medication yet. We noted it and moved on. We sent her out with a follow-up appointment that ended up being three weeks out, later than the two-week window we'd wanted. Interviewer: If the fall-risk assessment had come back before your first decision instead of after, would you have decided differently? Participant: Probably, yes. If I'd had that clearance up front, I likely would have started treatment on day one instead of waiting. Interviewer: If the other patient's bleeding event had never come up on the ward, do you think this admission would have gone differently? Participant: It's hard to say for certain, but I think the family conversation would have been calmer. Interviewer: Looking back, what would you tell a colleague facing a similar case? Participant: I'd say make sure the fall workup happens early, not as an afterthought, and try to separate the family's emotional reaction from the actual numbers in front of you. It's easy to let the picture of a bad outcome sit with you well past the moment, even when the data has already shifted.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.65s · gen 205.17s · total 209.0s_

**Retrieved** (ranked by store ranker):
1. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0328 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
2. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0214 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
3. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0210 (rrf) — _# decisionmaking examined the relationship between nurses' bias to healthcare disparities. In th_
4. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0184 (rrf) — _## Uwe Dulleck, PhD revealed that if a patient was having lower abdominal pain with a temperatur_
5. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0182 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
6. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0181 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
7. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0181 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0178 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0172 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0168 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
11. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0167 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
12. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0164 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
13. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0164 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
15. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0163 (rrf) — _# decisionmaking black and white elder simulated patients with end- Emergency nurses' and physic_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0163 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
17. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _# to Dangers from Humans speed, brute strength, sensory acuity, and apparent det allies to attac_
18. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0163 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
19. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0160 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
20. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0155 (rrf) — _# 4on patient outcomes in the emergency department: A scoping We used the eligibility and exclus_
21. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0154 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
22. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0154 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias TOWARD A SYN THESIS OF COGNITIV_
23. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0154 (rrf) — _## Uwe Dulleck, PhD ical decisionmaking \[ The fi ndings of our study have signi patient health _
24. **Journal of Forensic Sciences - 2021 - Dror - Cognitive bias in forensic pathology decisions.pdf** — 0.0153 (rrf) — _# 4.2 \| Materials 45, 39 were between 46– Participants read a vignette describing a not straigh_
25. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0150 (rrf) — _## BMC Medical Ethics Open Access incapacitated patient. ey list ve main biases related to infor_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
27. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0146 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
28. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0143 (rrf) — _## BMC Medical Ethics Open Access - - - - - - - - - Cognitive bias and its consequences for ethi_
29. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
30. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0142 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
31. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0142 (rrf) — _# decisionmaking Barnato et al., 2011 ; Green et al., et al., 2015 ; Maina et al., 2018 ; Saposn_
32. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0142 (rrf) — _# fi cation 8 demonstrating human biases in clinical interpretation. Participants were randomize_
33. **Journal of Forensic Sciences - 2021 - Dror - Cognitive bias in forensic pathology decisions.pdf** — 0.0141 (rrf) — _# 4.3 \| Procedure FIGURE 3 With identical medical findings, the proportion of forensic patholog_
34. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0141 (rrf) — _# So This is it? d with sufficient clari , 2003; Berger to bridge the gap is it that we retrieve_
35. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0137 (rrf) — _# fi cation Physicians engaged with the AI to inquire about evidence supporting clinical decisio_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0135 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
38. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0135 (rrf) — _# decisionmaking The five articles that explored emergency nurses were focused on the triage nur_
39. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0134 (rrf) — _# Clinical decisionmaking: Cognitive biases and heuristics in triage decisions in the emergency _
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0134 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0134 (rrf) — _# American Journal of Emergency Medicine journal homepage: abstract Background: source usage. Su_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0134 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0133 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
44. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0129 (rrf) — _## Elliott RN, PhD 1 Faculty of Health, School of Nursing and Midwifery, University of Technolog_
45. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0129 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs | Option 7 : Very likely opinion B | | _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0129 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
47. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0129 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
48. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0128 (rrf) — _# 6.2 Analysis of the structural model people make mistakes and errors occur. Errors can be redu_
49. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0128 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
50. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0127 (rrf) — _# Appendix D: Fitting the Gaussian channel This Appendix shows how to convert a Gaussian channel_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the attending physician's self-reported admission decisions for affirmatively demonstrated cognitive biases, using transcript evidence as the primary ground and retrieved passages for mechanism grounding."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Omission bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability bias",
      "alternative_labels": [
        "availability heuristic",
        "recency effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which people estimate the probability or importance of an event by the ease with which relevant examples come to mind; salient recent cases can distort clinical risk perception.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Ordering head CT after family anxiety about another patient's anticoagulation-related bleed",
      "decision_point_description": "Whether to order a head CT before discharge to reassure the patient's daughter despite no clinical indication.",
      "affected_reasoning_operation": "Diagnostic testing decision and risk perception",
      "bias_specific_mechanism": "A recent fatal anticoagulation-related GI bleed on the same ward made bleeding risk cognitively available and emotionally salient; the participant ordered an unindicated head CT primarily to manage the resulting family anxiety rather than because clinical evidence had changed.",
      "manifestation_in_interview": "The participant explicitly linked the ward story about another patient's bleeding death to the daughter's anxiety and to ordering a CT that he acknowledged was not medically indicated.",
      "effect_on_reasoning_or_decision": "The salient recent bleeding case shifted management toward non-indicated imaging and delayed discharge planning by one day, even though clinical status had not changed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Then on day two, one of the nurses mentioned, sort of in passing, that a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation. Understandably, that got around the unit, and my patient's daughter had heard a version of it too. She was in the room a lot and got increasingly anxious every time anticoagulation came up. Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated.",
          "evidence_explanation": "This quote directly links the recent fatal bleed to the decision to order an unindicated CT, showing that salient recent information—not clinical probability—drove the diagnostic action."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But it felt like having a normal scan in hand would make the conversation easier.",
          "evidence_explanation": "This confirms the imaging decision was aimed at emotional reassurance and conversation management, consistent with availability-driven anxiety rather than clinical indication."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly with this patient, but the ward story about the other patient's bleed was fresh in everyone's mind that week.",
          "evidence_explanation": "This directly states the recency and salience of the bleeding case, a key condition for availability-based risk overestimation."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged in hindsight that he could have walked through the patient's individual numbers with the daughter instead of ordering imaging that was not clinically indicated.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf",
          "paper_title": null,
          "authors": "Uwe Dulleck, PhD",
          "publication_year": "2025",
          "retrieved_passage_or_finding": "The retrieved source identifies availability and anchoring as two dominant heuristics among emergency triage nurses and emergency physicians when making complex decisions under risk and uncertainty.",
          "mechanism_supported_by_source": "The source supports the view that availability operates as a dominant heuristic in clinical decisions under risk and uncertainty, making salient examples disproportionately influential in risk judgments.",
          "relevance_to_this_occurrence": "The participant's response to a recent nearby anticoagulation-related bleed matches the availability mechanism: the ease of recalling that event inflated bleeding concern and prompted an unindicated CT."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Omission bias",
      "alternative_labels": [
        "anticipatory regret",
        "omission-commission asymmetry",
        "affect heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge harmful actions as worse than equally harmful omissions, leading to a preference for inaction even when the expected benefits of acting outweigh the expected harms.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Deferring anticoagulation after normal CT and low fall-risk clearance",
      "decision_point_description": "Whether to start a DOAC before discharge, start a lower dose with close follow-up, or defer entirely to the outpatient team.",
      "affected_reasoning_operation": "Risk-benefit weighting and treatment decision under uncertainty",
      "bias_specific_mechanism": "The participant vividly imagined a major bleed caused by an anticoagulant he started and anticipated long-lasting regret and blame; harmful action felt heavier to carry than inaction, so he deferred treatment even though clinical data and risk scores favored starting.",
      "manifestation_in_interview": "The participant described picturing a bleeding scenario and concluded that this feeling outweighed the probability-based case for treatment, then explicitly decided to leave the decision to the outpatient team.",
      "effect_on_reasoning_or_decision": "The patient was discharged without a firm anticoagulation start plan despite CHA2DS2-VASc 4, moderate HAS-BLED, normal head CT, and PT-cleared low fall risk; follow-up was later than intended.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The data at that point was pretty clean — low fall risk, normal imaging, scores favoring treatment. But I remember describing to the resident, almost involuntarily, this scenario of her bleeding on a drug I'd started, and picturing it as something that wouldn't really fade — like it would color how the family saw us and how I thought about the case for a long stretch afterward. It wasn't really about the probability anymore. I decided to leave it for the outpatient team.",
          "evidence_explanation": "This quote directly demonstrates an omission-commission asymmetry: the participant acknowledges the data favored treatment but chose inaction because the imagined harm from acting felt more emotionally powerful than the probability-based case for treating."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That feeling seemed heavier to carry than just not starting it.",
          "evidence_explanation": "This explicitly compares the weighted emotional burden of causing harm by commission against the burden of omission, the core mechanism of omission bias."
        }
      ],
      "correction_or_counterevidence": "Later advice to a colleague suggested separating family emotional reactions from the actual numbers, implying recognition that the emotional picture had influenced decision-making beyond the data.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided RAG context directly defines omission bias or commission-omission asymmetry; classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Omission bias",
      "alternative_labels": [
        "anticipated regret",
        "risk aversion"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial decision to withhold anticoagulation pending formal fall-risk assessment",
      "supporting_interview_quote": "I didn't want to be the one who started a blood thinner and then she fell again and bled into her head.",
      "plausible_mechanism": "A commission-omission asymmetry may have made the bleeding risk from an active prescription feel more blameworthy than stroke risk from withholding treatment, contributing to the initial delay.",
      "why_not_identified": "Recent fall in a 78-year-old is a clinically legitimate fall-risk factor, and obtaining a formal fall-risk assessment before starting anticoagulation is a bounded rational precaution; the evidence is too ambiguous to establish cognitive distortion at this first decision point."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Single interview relying on retrospective self-report may be influenced by hindsight and self-presentation, though the participant describes contemporaneous reasoning.",
    "The retrieved corpus did not contain direct material on omission bias, so that classification relies on general cognitive-science knowledge rather than provided retrieval evidence.",
    "The analysis is limited to the reasoning episodes the participant chose to describe; system-level, team, and family influences are inferred from those descriptions only."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a internal case review on decision-making during admissions, and that I can ask follow-up questions as we go. Participant: Sure, that's fine. Happy to walk through it. Interviewer: Great. Can you tell me your role on the team during this admission? Participant: I was the attending on the general medicine service. I had a resident covering with me, and we picked up this patient on hospital day one after she came in for something unrelated and ended up with a new finding on her monitor. Interviewer: And what was your overall goal for her care during the stay? Participant: Mainly to get her diagnosis sorted out and make sure we sent her home with a safe, appropriate plan. She was 78, otherwise fairly independent, living with her daughter nearby. Interviewer: Can you walk me through what happened, from the diagnosis to discharge? Participant: She came in and the admission ECG showed she was in atrial fibrillation, which nobody had picked up before — persistent, not paroxysmal. That obviously changes the calculus for stroke prevention. Her CHA2DS2-VASc came out to 4, so her annual stroke risk if left untreated is meaningful. Her HAS-BLED was 2, which is moderate, not a red flag. Pharmacy checked and there were no interactions with the DOAC we'd typically use. But she'd had a fall about three weeks before admission — mechanical, tripped on a rug at home, no head strike, no fracture, fully worked up at the time. Still, when I saw 'fall' in the history, that gave me pause about starting a blood thinner right away. I told the team we'd hold off and get a formal fall-risk assessment first before committing to anything. Then on day two, one of the nurses mentioned, sort of in passing, that a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation. Understandably, that got around the unit, and my patient's daughter had heard a version of it too. She was in the room a lot and got increasingly anxious every time anticoagulation came up. Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated. That pushed our timeline back a day. By day three the CT was normal, and physical therapy had cleared her fall risk as low with a walker. So on paper the numbers were now clearly in favor of starting treatment. I remember standing at the nurses' station with the resident and just picturing what it would be like if we started her on this drug and then she had a major bleed — the conversation with the daughter, explaining that decision, how that would sit with all of us. It wasn't just that it would be bad; it felt like the kind of thing I'd still be replaying weeks later, something that would sit over the whole team and not really lift for a long time. That feeling seemed heavier to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge. Then on day four, right before discharge, she got a small bruise at her IV site — unrelated, since she wasn't even on anticoagulation yet. It didn't change anything about the plan; we finalized the discharge summary without a firm start plan, just a note to follow up as an outpatient. Interviewer: Let's slow down and go through each of those moments. At the first point, right after diagnosis — what stood out to you most? Participant: Honestly, the fall. Clinically I knew the scores favored treatment, but a recent fall in an older patient just registers as a flag. I didn't want to be the one who started a blood thinner and then she fell again and bled into her head. Interviewer: What alternatives did you consider there? Participant: We could have started the DOAC immediately since the scores supported it, or started a lower empirical dose. I chose to wait for a formal PT evaluation instead, even though the fall itself had already been worked up and looked mechanical. Interviewer: What was the main basis for waiting rather than starting treatment that day? Participant: I suppose not wanting to be the direct cause of a bad outcome. Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number. Interviewer: At the second point, with the daughter's anxiety and the CT — what were you trying to accomplish? Participant: Mostly to de-escalate the family's fear so we could have a productive conversation. In hindsight, I could have just walked through her individual numbers with the daughter instead of ordering imaging that wasn't clinically indicated. But it felt like having a normal scan in hand would make the conversation easier. Interviewer: How much time pressure did you feel making that call? Participant: Some — we were already tight on discharge planning, and adding a CT meant another day. But I felt like skipping that step would leave the family conversation unresolved. Interviewer: Move to the third point — after the CT came back normal and fall risk was cleared. What was going through your mind there? Participant: That's the one I keep coming back to. The data at that point was pretty clean — low fall risk, normal imaging, scores favoring treatment. But I remember describing to the resident, almost involuntarily, this scenario of her bleeding on a drug I'd started, and picturing it as something that wouldn't really fade — like it would color how the family saw us and how I thought about the case for a long stretch afterward. It wasn't really about the probability anymore. I decided to leave it for the outpatient team. Interviewer: What alternatives were on the table then? Participant: Starting it right there before discharge, starting a lower dose with a firm two-week follow-up, or deferring entirely, which is what I did. Interviewer: Had you handled a similar case before that shaped this decision? Participant: Not directly with this patient, but the ward story about the other patient's bleed was fresh in everyone's mind that week. Interviewer: At the fourth point, the bruise at discharge — how did that factor in? Participant: It didn't really change the clinical picture, since she wasn't even on the medication yet. We noted it and moved on. We sent her out with a follow-up appointment that ended up being three weeks out, later than the two-week window we'd wanted. Interviewer: If the fall-risk assessment had come back before your first decision instead of after, would you have decided differently? Participant: Probably, yes. If I'd had that clearance up front, I likely would have started treatment on day one instead of waiting. Interviewer: If the other patient's bleeding event had never come up on the ward, do you think this admission would have gone differently? Participant: It's hard to say for certain, but I think the family conversation would have been calmer. Interviewer: Looking back, what would you tell a colleague facing a similar case? Participant: I'd say make sure the fall workup happens early, not as an afterthought, and try to separate the family's emotional reaction from the actual numbers in front of you. It's easy to let the picture of a bad outcome sit with you well past the moment, even when the data has already shifted.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.63s · gen 272.12s · total 275.8s_

**Retrieved** (ranked by store ranker):
1. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0328 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
2. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0214 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
3. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0210 (rrf) — _# decisionmaking examined the relationship between nurses' bias to healthcare disparities. In th_
4. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0184 (rrf) — _## Uwe Dulleck, PhD revealed that if a patient was having lower abdominal pain with a temperatur_
5. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0182 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
6. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0181 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
7. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0181 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0178 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0172 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0168 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
11. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0167 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
12. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0164 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
13. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0164 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
15. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0163 (rrf) — _# decisionmaking black and white elder simulated patients with end- Emergency nurses' and physic_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0163 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
17. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _# to Dangers from Humans speed, brute strength, sensory acuity, and apparent det allies to attac_
18. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0163 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
19. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0160 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
20. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0155 (rrf) — _# 4on patient outcomes in the emergency department: A scoping We used the eligibility and exclus_
21. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0154 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
22. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0154 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias TOWARD A SYN THESIS OF COGNITIV_
23. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0154 (rrf) — _## Uwe Dulleck, PhD ical decisionmaking \[ The fi ndings of our study have signi patient health _
24. **Journal of Forensic Sciences - 2021 - Dror - Cognitive bias in forensic pathology decisions.pdf** — 0.0153 (rrf) — _# 4.2 \| Materials 45, 39 were between 46– Participants read a vignette describing a not straigh_
25. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0150 (rrf) — _## BMC Medical Ethics Open Access incapacitated patient. ey list ve main biases related to infor_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
27. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0146 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
28. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0143 (rrf) — _## BMC Medical Ethics Open Access - - - - - - - - - Cognitive bias and its consequences for ethi_
29. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
30. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0142 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
31. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0142 (rrf) — _# decisionmaking Barnato et al., 2011 ; Green et al., et al., 2015 ; Maina et al., 2018 ; Saposn_
32. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0142 (rrf) — _# fi cation 8 demonstrating human biases in clinical interpretation. Participants were randomize_
33. **Journal of Forensic Sciences - 2021 - Dror - Cognitive bias in forensic pathology decisions.pdf** — 0.0141 (rrf) — _# 4.3 \| Procedure FIGURE 3 With identical medical findings, the proportion of forensic patholog_
34. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0141 (rrf) — _# So This is it? d with sufficient clari , 2003; Berger to bridge the gap is it that we retrieve_
35. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0137 (rrf) — _# fi cation Physicians engaged with the AI to inquire about evidence supporting clinical decisio_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0135 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
38. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0135 (rrf) — _# decisionmaking The five articles that explored emergency nurses were focused on the triage nur_
39. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0134 (rrf) — _# Clinical decisionmaking: Cognitive biases and heuristics in triage decisions in the emergency _
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0134 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0134 (rrf) — _# American Journal of Emergency Medicine journal homepage: abstract Background: source usage. Su_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0134 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0133 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
44. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0129 (rrf) — _## Elliott RN, PhD 1 Faculty of Health, School of Nursing and Midwifery, University of Technolog_
45. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0129 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs | Option 7 : Very likely opinion B | | _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0129 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
47. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0129 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
48. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0128 (rrf) — _# 6.2 Analysis of the structural model people make mistakes and errors occur. Errors can be redu_
49. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0128 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
50. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0127 (rrf) — _# Appendix D: Fitting the Gaussian channel This Appendix shows how to convert a Gaussian channel_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focuses on the attending participant's self-reported reasoning at three decision points during the admission: the initial anticoagulation decision, the day-2 head CT decision after family anxiety, and the final day-3 decision to defer anticoagulation."
  },
  "identified_bias_summary": [
    {
      "bias_label": "affect heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "omission bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "omission bias",
      "alternative_labels": ["action-omission asymmetry", "omission preference"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge harmful omissions as less blameworthy than harmful commissions, even when the balance of expected benefits and risks favors action, leading to a preference for inaction to avoid being the direct cause of harm.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial day-1 anticoagulation start decision after new atrial fibrillation diagnosis",
      "decision_point_description": "Choice between starting a DOAC immediately because CHA2DS2-VASc and HAS-BLED supported treatment versus withholding anticoagulation to obtain a formal fall-risk assessment first.",
      "affected_reasoning_operation": "Risk-benefit weighting and treatment initiation decision",
      "bias_specific_mechanism": "Action-omission asymmetry: harms from commission, such as starting an anticoagulant and causing a bleed, are treated as more blameworthy than harms from omission, such as stroke from not starting anticoagulation, even when the participant recognizes the net benefit favors action.",
      "manifestation_in_interview": "The participant repeatedly framed withholding as the more conservative and safer choice, not because the probabilities favored it, but because starting treatment could make him feel directly responsible for a bleed.",
      "effect_on_reasoning_or_decision": "Led to withholding a guideline-supported anticoagulant on day 1 and delaying the stroke-prevention decision pending fall-risk assessment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Still, when I saw 'fall' in the history, that gave me pause about starting a blood thinner right away. I told the team we'd hold off and get a formal fall-risk assessment first before committing to anything.",
          "evidence_explanation": "Shows that the initial decision was to withhold treatment, with the fall history treated as a reason for caution despite the overall risk-benefit data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't want to be the one who started a blood thinner and then she fell again and bled into her head.",
          "evidence_explanation": "Directly expresses the commission-avoidance mechanism: the concern is not only clinical risk, but being the direct cause of a bad outcome."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number.",
          "evidence_explanation": "Demonstrates that the decision favored omission despite awareness that the numerical benefit of treatment was larger, a key feature of omission bias."
        }
      ],
      "correction_or_counterevidence": "Fall is a recognized bleeding-risk factor and obtaining formal fall-risk assessment before starting anticoagulation can be clinically prudent; however, the participant himself notes that the fall had already been fully worked up and that the stroke risk reduction was the larger number.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "General knowledge label; retrieved corpus support specific to omission bias was not available.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the probability or importance of an event by the ease with which examples come to mind, with recent, vivid, or emotionally salient cases disproportionately influencing reasoning and decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-2 imaging decision during family anxiety after ward anticoagulation-bleed story",
      "decision_point_description": "Decision to order a head CT despite no clinical indication, partly to reassure the patient's daughter after a recent ward death from anticoagulation-related GI bleeding.",
      "affected_reasoning_operation": "Testing and communication decision under uncertainty and family anxiety",
      "bias_specific_mechanism": "Ease of recall/salience: a recent, vivid, emotionally charged ward death from anticoagulation-related bleeding made that complication more available, increasing attention to bleeding risk and prompting defensive testing.",
      "manifestation_in_interview": "The participant ordered a not-clinically-indicated head CT specifically in the context of a recent ward story about a fatal anticoagulation-related bleed, with no change in the patient's clinical status.",
      "effect_on_reasoning_or_decision": "Led to a non-indicated head CT, added a day to the admission, and reinforced bleeding-focused attention over stroke-risk reasoning.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Then on day two, one of the nurses mentioned, sort of in passing, that a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation. Understandably, that got around the unit, and my patient's daughter had heard a version of it too.",
          "evidence_explanation": "Establishes that a recent, vivid fatal bleeding case was salient in the clinical environment and shaped the family's emotional response."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated.",
          "evidence_explanation": "Shows that the test was ordered despite no clinical indication, linking the decision to the emotional/fear context created by the salient ward story."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly with this patient, but the ward story about the other patient's bleed was fresh in everyone's mind that week.",
          "evidence_explanation": "Directly indicates the recency and vividness of the bleeding example, which is the core driver of the availability heuristic."
        }
      ],
      "correction_or_counterevidence": "Ordering imaging to address family anxiety may have been a deliberate communication strategy rather than a biased personal probability estimate; the participant explicitly acknowledges the test was not clinically indicated, which weakens the inference that his own probability judgment was distorted.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "One retrieved passage provides general support for availability as a common clinical heuristic under uncertainty, though it does not define the mechanism in detail.",
      "corpus_evidence": [
        {
          "source_identifier": "Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf",
          "paper_title": "Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf",
          "authors": "Uwe Dulleck, PhD",
          "publication_year": null,
          "retrieved_passage_or_finding": "align with previous research, suggesting that availability and anchorfastpaced environment such as the ED, availability and anchoring are ing are two dominant heuristics among emergency triage nurses. Betw o main heuristics that are profoundly used by emergency physicians yond this, we found that negative framing bias was also prevalent and nurses when making complex decisions under risk and uncertainty among triage nurses.",
          "mechanism_supported_by_source": "Availability is identified as a dominant heuristic in clinical decision-making under risk and uncertainty.",
          "relevance_to_this_occurrence": "The interview shows a recent, vivid ward bleeding case entering clinical decision-making through family anxiety and a non-indicated CT, consistent with availability-based influence."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "affect heuristic",
      "alternative_labels": ["anticipatory regret", "impact bias", "affective forecasting"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to make judgments or decisions based on immediate or anticipated emotional feelings rather than on deliberative probability and utility analysis, allowing imagined affect-laden outcomes to dominate reasoning.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-3 final anticoagulation decision after normal CT and physical therapy fall-risk clearance",
      "decision_point_description": "Choice between starting anticoagulation before discharge, starting a lower dose with follow-up, or deferring to the outpatient team after updated data favored treatment.",
      "affected_reasoning_operation": "Final treatment decision after updated risk information",
      "bias_specific_mechanism": "Affective/emotional weighting: an imagined future major bleed and anticipated prolonged guilt/regret dominate the decision, overriding the quantitative risk-benefit assessment.",
      "manifestation_in_interview": "The participant described picturing a future bleed on a drug he started as something that would not fade, and stated that the decision was no longer about probability, then deferred treatment.",
      "effect_on_reasoning_or_decision": "Led to deferring anticoagulation to the outpatient team despite normal imaging and low fall-risk clearance, resulting in no firm treatment start at discharge.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The data at that point was pretty clean — low fall risk, normal imaging, scores favoring treatment. But I remember describing to the resident, almost involuntarily, this scenario of her bleeding on a drug I'd started, and picturing it as something that wouldn't really fade — like it would color how the family saw us and how I thought about the case for a long stretch afterward. It wasn't really about the probability anymore. I decided to leave it for the outpatient team.",
          "evidence_explanation": "Shows that an emotionally vivid imagined bleed, rather than the updated clinical probabilities, drove the final deferral decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That feeling seemed heavier to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge.",
          "evidence_explanation": "Explicitly describes a comparison of emotional weight rather than clinical benefit-risk, and links that feeling to the decision to not start treatment."
        }
      ],
      "correction_or_counterevidence": "Considering patient/family values and the emotional burden on the team is not inherently biased; shared decision-making can legitimately weigh such factors, but the participant's own statement that it was no longer about probability supports a bias-specific mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "General knowledge label; retrieved corpus support specific to affect heuristic or affective forecasting was not available.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring",
      "alternative_labels": ["anchoring and adjustment"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial day-1 anticoagulation decision after new AF diagnosis",
      "supporting_interview_quote": "Honestly, the fall. Clinically I knew the scores favored treatment, but a recent fall in an older patient just registers as a flag.",
      "plausible_mechanism": "The fall history may have served as an initial reference point, drawing disproportionate attention to bleeding risk despite later evidence that the fall was mechanical and fully worked up.",
      "why_not_identified": "The fall was clinically relevant for bleeding risk, and obtaining formal PT evaluation was a reasonable step; the stronger affirmed mechanisms are omission bias and affect-driven risk aversion rather than anchoring on an irrelevant value."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages are limited and partly OCR-garbled; no formal definitions for omission bias or affect heuristic were present.",
    "Single interview transcript and self-report data limit causal attribution of bias; the analysis relies on the participant's retrospective account rather than direct observation.",
    "Availability heuristic identification is low confidence because the CT decision may have been a deliberate communication strategy rather than a distortion of the participant's own probability estimate."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a internal case review on decision-making during admissions, and that I can ask follow-up questions as we go. Participant: Sure, that's fine. Happy to walk through it. Interviewer: Great. Can you tell me your role on the team during this admission? Participant: I was the attending on the general medicine service. I had a resident covering with me, and we picked up this patient on hospital day one after she came in for something unrelated and ended up with a new finding on her monitor. Interviewer: And what was your overall goal for her care during the stay? Participant: Mainly to get her diagnosis sorted out and make sure we sent her home with a safe, appropriate plan. She was 78, otherwise fairly independent, living with her daughter nearby. Interviewer: Can you walk me through what happened, from the diagnosis to discharge? Participant: She came in and the admission ECG showed she was in atrial fibrillation, which nobody had picked up before — persistent, not paroxysmal. That obviously changes the calculus for stroke prevention. Her CHA2DS2-VASc came out to 4, so her annual stroke risk if left untreated is meaningful. Her HAS-BLED was 2, which is moderate, not a red flag. Pharmacy checked and there were no interactions with the DOAC we'd typically use. But she'd had a fall about three weeks before admission — mechanical, tripped on a rug at home, no head strike, no fracture, fully worked up at the time. Still, when I saw 'fall' in the history, that gave me pause about starting a blood thinner right away. I told the team we'd hold off and get a formal fall-risk assessment first before committing to anything. Then on day two, one of the nurses mentioned, sort of in passing, that a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation. Understandably, that got around the unit, and my patient's daughter had heard a version of it too. She was in the room a lot and got increasingly anxious every time anticoagulation came up. Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated. That pushed our timeline back a day. By day three the CT was normal, and physical therapy had cleared her fall risk as low with a walker. So on paper the numbers were now clearly in favor of starting treatment. I remember standing at the nurses' station with the resident and just picturing what it would be like if we started her on this drug and then she had a major bleed — the conversation with the daughter, explaining that decision, how that would sit with all of us. It wasn't just that it would be bad; it felt like the kind of thing I'd still be replaying weeks later, something that would sit over the whole team and not really lift for a long time. That feeling seemed heavier to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge. Then on day four, right before discharge, she got a small bruise at her IV site — unrelated, since she wasn't even on anticoagulation yet. It didn't change anything about the plan; we finalized the discharge summary without a firm start plan, just a note to follow up as an outpatient. Interviewer: Let's slow down and go through each of those moments. At the first point, right after diagnosis — what stood out to you most? Participant: Honestly, the fall. Clinically I knew the scores favored treatment, but a recent fall in an older patient just registers as a flag. I didn't want to be the one who started a blood thinner and then she fell again and bled into her head. Interviewer: What alternatives did you consider there? Participant: We could have started the DOAC immediately since the scores supported it, or started a lower empirical dose. I chose to wait for a formal PT evaluation instead, even though the fall itself had already been worked up and looked mechanical. Interviewer: What was the main basis for waiting rather than starting treatment that day? Participant: I suppose not wanting to be the direct cause of a bad outcome. Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number. Interviewer: At the second point, with the daughter's anxiety and the CT — what were you trying to accomplish? Participant: Mostly to de-escalate the family's fear so we could have a productive conversation. In hindsight, I could have just walked through her individual numbers with the daughter instead of ordering imaging that wasn't clinically indicated. But it felt like having a normal scan in hand would make the conversation easier. Interviewer: How much time pressure did you feel making that call? Participant: Some — we were already tight on discharge planning, and adding a CT meant another day. But I felt like skipping that step would leave the family conversation unresolved. Interviewer: Move to the third point — after the CT came back normal and fall risk was cleared. What was going through your mind there? Participant: That's the one I keep coming back to. The data at that point was pretty clean — low fall risk, normal imaging, scores favoring treatment. But I remember describing to the resident, almost involuntarily, this scenario of her bleeding on a drug I'd started, and picturing it as something that wouldn't really fade — like it would color how the family saw us and how I thought about the case for a long stretch afterward. It wasn't really about the probability anymore. I decided to leave it for the outpatient team. Interviewer: What alternatives were on the table then? Participant: Starting it right there before discharge, starting a lower dose with a firm two-week follow-up, or deferring entirely, which is what I did. Interviewer: Had you handled a similar case before that shaped this decision? Participant: Not directly with this patient, but the ward story about the other patient's bleed was fresh in everyone's mind that week. Interviewer: At the fourth point, the bruise at discharge — how did that factor in? Participant: It didn't really change the clinical picture, since she wasn't even on the medication yet. We noted it and moved on. We sent her out with a follow-up appointment that ended up being three weeks out, later than the two-week window we'd wanted. Interviewer: If the fall-risk assessment had come back before your first decision instead of after, would you have decided differently? Participant: Probably, yes. If I'd had that clearance up front, I likely would have started treatment on day one instead of waiting. Interviewer: If the other patient's bleeding event had never come up on the ward, do you think this admission would have gone differently? Participant: It's hard to say for certain, but I think the family conversation would have been calmer. Interviewer: Looking back, what would you tell a colleague facing a similar case? Participant: I'd say make sure the fall workup happens early, not as an afterthought, and try to separate the family's emotional reaction from the actual numbers in front of you. It's easy to let the picture of a bad outcome sit with you well past the moment, even when the data has already shifted.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.78s · gen 230.60s · total 234.5s_

**Retrieved** (ranked by store ranker):
1. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0328 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
2. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0214 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
3. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0210 (rrf) — _# decisionmaking examined the relationship between nurses' bias to healthcare disparities. In th_
4. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0184 (rrf) — _## Uwe Dulleck, PhD revealed that if a patient was having lower abdominal pain with a temperatur_
5. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0182 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
6. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0181 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
7. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0181 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
8. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0178 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0172 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0168 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
11. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0167 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
12. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0164 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
13. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0164 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
15. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0163 (rrf) — _# decisionmaking black and white elder simulated patients with end- Emergency nurses' and physic_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0163 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
17. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0163 (rrf) — _# to Dangers from Humans speed, brute strength, sensory acuity, and apparent det allies to attac_
18. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0163 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
19. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0160 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
20. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0155 (rrf) — _# 4on patient outcomes in the emergency department: A scoping We used the eligibility and exclus_
21. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0154 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
22. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0154 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias TOWARD A SYN THESIS OF COGNITIV_
23. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0154 (rrf) — _## Uwe Dulleck, PhD ical decisionmaking \[ The fi ndings of our study have signi patient health _
24. **Journal of Forensic Sciences - 2021 - Dror - Cognitive bias in forensic pathology decisions.pdf** — 0.0153 (rrf) — _# 4.2 \| Materials 45, 39 were between 46– Participants read a vignette describing a not straigh_
25. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0150 (rrf) — _## BMC Medical Ethics Open Access incapacitated patient. ey list ve main biases related to infor_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0148 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_
27. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0146 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
28. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0143 (rrf) — _## BMC Medical Ethics Open Access - - - - - - - - - Cognitive bias and its consequences for ethi_
29. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
30. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0142 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
31. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0142 (rrf) — _# decisionmaking Barnato et al., 2011 ; Green et al., et al., 2015 ; Maina et al., 2018 ; Saposn_
32. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0142 (rrf) — _# fi cation 8 demonstrating human biases in clinical interpretation. Participants were randomize_
33. **Journal of Forensic Sciences - 2021 - Dror - Cognitive bias in forensic pathology decisions.pdf** — 0.0141 (rrf) — _# 4.3 \| Procedure FIGURE 3 With identical medical findings, the proportion of forensic patholog_
34. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0141 (rrf) — _# So This is it? d with sufficient clari , 2003; Berger to bridge the gap is it that we retrieve_
35. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0137 (rrf) — _# fi cation Physicians engaged with the AI to inquire about evidence supporting clinical decisio_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0135 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
38. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0135 (rrf) — _# decisionmaking The five articles that explored emergency nurses were focused on the triage nur_
39. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0134 (rrf) — _# Clinical decisionmaking: Cognitive biases and heuristics in triage decisions in the emergency _
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0134 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0134 (rrf) — _# American Journal of Emergency Medicine journal homepage: abstract Background: source usage. Su_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0134 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0133 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
44. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0129 (rrf) — _## Elliott RN, PhD 1 Faculty of Health, School of Nursing and Midwifery, University of Technolog_
45. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0129 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs | Option 7 : Very likely opinion B | | _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0129 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
47. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0129 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
48. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0128 (rrf) — _# 6.2 Analysis of the structural model people make mistakes and errors occur. Errors can be redu_
49. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0128 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
50. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0127 (rrf) — _# Appendix D: Fitting the Gaussian channel This Appendix shows how to convert a Gaussian channel_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of participant-reported clinical reasoning during a retrospective admission case review; only participant reasoning and decisions are evaluated for bias occurrences."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Omission bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "Availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the frequency or probability of an event by the ease with which relevant examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Anticoagulation risk perception and head CT ordering after ward GI-bleed story",
      "decision_point_description": "After a nurse mentioned a recent nearby patient death from GI bleeding on anticoagulation, the participant ordered a non-indicated head CT and later deferred anticoagulation despite low fall risk and normal CT.",
      "affected_reasoning_operation": "Risk perception and decision to order diagnostic imaging",
      "bias_specific_mechanism": "A recent, emotionally vivid ward death from anticoagulation-related GI bleeding made bleeding complications highly available, increasing their salience and perceived relevance despite unchanged clinical indicators.",
      "manifestation_in_interview": "The participant linked the ward bleed story to the decision process, ordered an unindicated head CT after the story circulated, and described the story as 'fresh in everyone's mind' when explaining what shaped the decision.",
      "effect_on_reasoning_or_decision": "The availability of the recent bleed case amplified bleeding-related concern, contributing to a non-indicated head CT and supporting continued anticoagulation deferral even after objective fall-risk and imaging results were reassuring.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Then on day two, one of the nurses mentioned, sort of in passing, that a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation. Understandably, that got around the unit, and my patient's daughter had heard a version of it too.",
          "evidence_explanation": "Establishes a recent, emotionally vivid anticoagulation-bleed case that was easily recalled on the unit."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated.",
          "evidence_explanation": "Shows that a non-clinical, emotionally salient factor, not objective clinical change, drove an unindicated action after the bleed story spread."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly with this patient, but the ward story about the other patient's bleed was fresh in everyone's mind that week.",
          "evidence_explanation": "Directly links the recent bleed story to the decision process, consistent with availability influencing risk judgment."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged clinically nothing had changed and the CT was not really indicated; HAS-BLED was moderate, and the CT ultimately came back normal.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support identified availability as a dominant heuristic in clinical decisions under risk and uncertainty, consistent with this occurrence.",
      "corpus_evidence": [
        {
          "source_identifier": "Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2025",
          "retrieved_passage_or_finding": "align with previous research, suggesting that availability and anchor- ing are two dominant heuristics among emergency triage nurses. Betw o main heuristics that are profoundly used by emergency physicians yond this, we found that negative framing bias was also prevalent and nurses when making complex decisions under risk and uncertainty among triage nurses.",
          "mechanism_supported_by_source": "Availability is described as a dominant heuristic in clinical decision making under risk and uncertainty.",
          "relevance_to_this_occurrence": "The participant's anticoagulation decision occurred under risk and followed a recent, easily recalled anticoagulation-bleed case, consistent with availability influencing risk perception."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Omission bias",
      "alternative_labels": [
        "Omission-commission asymmetry",
        "Anticipated regret"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge harmful commissions as worse than equally harmful omissions and to prefer inaction as a result.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Anticoagulation initiation and final deferral for newly diagnosed atrial fibrillation",
      "decision_point_description": "Initial decision to hold anticoagulation pending fall-risk assessment, and later decision to defer entirely after physical therapy cleared fall risk and head CT was normal.",
      "affected_reasoning_operation": "Risk-benefit judgment and anticoagulation decision",
      "bias_specific_mechanism": "Anticipatory regret and asymmetric weighting of harmful commissions versus omissions made withholding or deferring anticoagulation feel safer than starting it, even though the objective stroke-risk reduction outweighed bleeding risk.",
      "manifestation_in_interview": "The participant explicitly said he did not want to be the direct cause of a bad outcome and that withholding felt more conservative despite the resident noting the stroke risk reduction was larger; later he pictured a major bleed on a drug he started as heavier to carry than not starting it.",
      "effect_on_reasoning_or_decision": "Anticoagulation was not started during admission; the patient was discharged without a firm start plan and with follow-up later than desired, despite CHA2DS2-VASc 4, HAS-BLED 2, low fall risk after PT, and normal head CT.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't want to be the one who started a blood thinner and then she fell again and bled into her head.",
          "evidence_explanation": "Shows anticipated regret about a harmful commission, not solely objective risk, driving the initial conservative choice."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I suppose not wanting to be the direct cause of a bad outcome. Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number.",
          "evidence_explanation": "Explicitly contrasts commission harm with omission and acknowledges withholding was preferred despite objective risk data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember standing at the nurses' station with the resident and just picturing what it would be like if we started her on this drug and then she had a major bleed — the conversation with the daughter, explaining that decision, how that would sit with all of us. It wasn't just that it would be bad; it felt like the kind of thing I'd still be replaying weeks later, something that would sit over the whole team and not really lift for a long time. That feeling seemed heavier to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge.",
          "evidence_explanation": "Demonstrates mental simulation and anticipated regret about a harmful commission, which led to final deferral despite favorable data."
        }
      ],
      "correction_or_counterevidence": "The resident explicitly noted the stroke risk reduction was the larger number; physical therapy cleared fall risk as low; the head CT was normal; and the participant himself acknowledged the scores favored treatment. These did not shift the omission preference.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage addressed omission bias directly; the label and mechanism rest on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Commission bias",
      "alternative_labels": [
        "Action bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision to order non-indicated head CT for family reassurance",
      "supporting_interview_quote": "Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated.",
      "plausible_mechanism": "External emotional and family pressure to act made non-indicated imaging feel like the best way to resolve anxiety.",
      "why_not_identified": "The participant appeared aware that the CT was not clinically indicated and framed it as a deliberate communication strategy rather than an unconscious distortion; the transcript does not directly show that his clinical risk/benefit judgment was biased rather than consciously accommodating family anxiety."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on a retrospective self-report, so recall and self-presentation may affect the narrated reasoning.",
    "Retrieved corpus support for omission bias was unavailable; that occurrence uses a general-knowledge established label with disclosure."
  ]
}

