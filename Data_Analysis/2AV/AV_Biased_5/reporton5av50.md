# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a maintenance decision-making review, and that we can reference the tail number and event details generically without naming crew. Participant: That's fine, go ahead. Interviewer: Great. Can you tell me your role and how you came into this event? Participant: I'm the Director of Maintenance at our base station. I oversee line maintenance sign-offs, RTS certifications, and I'm the one who ultimately owns whether an aircraft goes back into the schedule. This one landed on my desk because it kept coming back. Interviewer: Walk me through what the issue looked like when you first became aware of it. Participant: We had a Hydraulic System B caution light show up on one of our E175s—momentary, cleared itself, crew wrote it up. Maintenance ran the BITE test, came back clean, no fault found. Classic CND. It happened three times over about two weeks. Each time, no fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL. The aircraft kept flying its line. Interviewer: What did you make of that pattern at the time? Participant: Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times. We had the holiday peak coming up and needed the airframe in rotation, so grounding it for an open-ended isolation hunt on a CND item felt like overkill at that point. Interviewer: Did the increasing duration register as significant to you? Participant: I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it. Interviewer: What happened next? Participant: Next flight day, it came back a fourth time, and this one ran about twelve seconds—longer than anything before—and the crew also noted a brief speed brake anomaly on the same leg. That's when my senior hydraulics engineer came to me and wanted to pull the aircraft and run the full fault isolation procedure out of the FIM. Interviewer: What did you decide at that point, and how did you get there? Participant: While we were talking about it, our OEM field rep happened to be at the hangar working a different tail. I flagged him down and asked what he thought. He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it. Interviewer: How did your engineer take that? Participant: He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week. Interviewer: What information did you weigh most heavily there, and what didn't you dig into? Participant: Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal. We reset the BITE and flew it two cycles without a recurrence. Interviewer: What came after that? Participant: A few days later, during an unrelated task, one of the techs was near the hydraulic pump and noticed some residue around the seal. Small amount, hadn't been documented before. That was new—nothing like that had shown up in any of the earlier CND checks. Interviewer: What did that change for you? Participant: It told us there might be an actual mechanical source rather than just a sensor quirk. At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job. Interviewer: Did the amount of work already done factor into that choice? Participant: I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over. Interviewer: After the seal replacement, what did you see? Participant: Leak check passed on the ground, static test showed no residue. Clean. Interviewer: What happened at the final sign-off? Participant: We needed the aircraft that afternoon for the holiday schedule, and we didn't have a test-flight crew available same-day. Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved. Interviewer: Given the aircraft's history—three CND events, the fourth longer one with the speed brake note, and the fact that the seal residue never really explained why the caution happened in flight in the first place—how sure were you that this was actually fixed? Participant: Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that. Interviewer: If you'd had a test-flight crew available that day, would that have changed your certainty? Participant: It would've been a nice extra data point, but I don't think it would've changed my decision to release it. Interviewer: Looking back across the whole event, is there a point where, with the same information you had then, you'd make a different call? Participant: Maybe the fourth event—the twelve-second one with the speed brake anomaly. If I'd leaned more toward my engineer's read there instead of the OEM rep's, we might have caught the seal issue earlier instead of a few days later. Interviewer: If the OEM rep hadn't been on-site that day, what do you think you'd have done instead? Participant: Probably would've let my engineer run the full isolation. Having an outside read available in the moment made it easy to go a different direction. Interviewer: Last one—if the seal residue had turned up before you'd started the component swaps, would the escalation decision have gone differently? Participant: Probably, yeah. Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.81s · gen 218.94s · total 223.1s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0275 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0263 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0248 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0247 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
5. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0243 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0240 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0238 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0223 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0214 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0208 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
11. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0194 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
12. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0192 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0185 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0183 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0182 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
17. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _## 16 5 Accidents & incidents Observed Expected The results of the chi 5.76 , p = .01 . The resu_
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
20. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0172 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0169 (rrf) — _# 18, 72% awareness to the outcome of the event 4.2.1 Relationship between flight crew experienc_
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0167 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0166 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
28. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0160 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
30. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0159 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0159 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
33. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0155 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _## Evolut ionary Cognitive Psychology | mals in Pleistocene caves, for instance, demonstrate one_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0151 (rrf) — _# f Space Flight relatively large set of possible systems that are v but not quite perfect, then_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
41. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0150 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
43. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
45. **Human_Cognitive_Bias_Identification_for.pdf** — 0.0145 (rrf) — _# Systems Situation and Environment precondition is that the aircraft preparing to land on a spe_
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
47. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0142 (rrf) — _# 188 | to the one in the | explanation condition). Informed by prior work that a slow algorithm_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Blind, conservative analysis of the interview transcript for affirmatively demonstrated cognitive bias mechanisms. Retrieved corpus used for canonical definitions and support only; not all identified biases were present in retrieved passages."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence effect",
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
      "bias_label": "anchoring and adjustment",
      "alternative_labels": ["anchoring", "anchoring and adjustment heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The anchoring and adjustment heuristic: people make estimates based on an initial answer, and subsequent adjustments from that initial value are typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth Hydraulic System B caution event with speed brake anomaly",
      "decision_point_description": "Whether to authorize the senior hydraulics engineer's request for full FIM fault isolation or proceed with the OEM-suggested BITE reset and return the aircraft to service.",
      "affected_reasoning_operation": "Hypothesis selection and evidence weighting",
      "bias_specific_mechanism": "The initial OEM hypothesis of a software/BITE quirk correctable by reset served as an anchor. The participant adjusted insufficiently from this initial answer despite contradictory evidence (the speed brake anomaly) and the senior engineer's request for full isolation, and he did not verify whether the recalled prior in-house case matched current flight hours or component batch.",
      "manifestation_in_interview": "The participant reported that after hearing the OEM rep and recalling a prior similar case, 'it felt like we already had the answer' and chose reset over full isolation. He also stated he did not check whether the old case matched the current one.",
      "effect_on_reasoning_or_decision": "The decision to hold off full isolation and keep the aircraft flying delayed identification of the mechanical source later indicated by pump seal residue.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.",
          "evidence_explanation": "Shows the initial reset hypothesis functioned as an anchor and directly shaped the decision to reject full isolation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
          "evidence_explanation": "Demonstrates insufficient adjustment/verification of the anchoring information and reliance on perceived similarity instead of diagnostic matching."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
          "evidence_explanation": "Explicitly records that contradictory information from the engineer was discounted relative to the anchor provided by the OEM rep's expertise."
        }
      ],
      "correction_or_counterevidence": "The senior engineer disagreed and requested full FIM isolation, citing the speed brake anomaly. This was counterevidence considered but not acted on. Later pump seal residue provided subsequent evidence of a mechanical source, but the biased anchoring was not corrected at the decision point.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved space flight verification/validation passage provides the canonical anchoring and adjustment mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.” [16]",
          "mechanism_supported_by_source": "Anchoring on an initial answer with insufficient subsequent adjustment.",
          "relevance_to_this_occurrence": "Directly explains how the participant's initial OEM/reset hypothesis anchored his final decision despite additional contradictory information."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["sunk cost fallacy", "escalation of commitment", "plan continuation"],
      "taxonomy_status": "established_label",
      "bias_definition": "Plan continuation bias is the tendency to continue an original plan or course of action despite cues indicating that the plan may be inappropriate or not working.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Discovery of hydraulic pump seal residue after prior troubleshooting",
      "decision_point_description": "Whether to continue the current incremental troubleshooting plan by replacing only the seal, or escalate to a full pump replacement after new evidence of a potential mechanical source.",
      "affected_reasoning_operation": "Escalation and repair scope decision",
      "bias_specific_mechanism": "Commitment to the existing incremental troubleshooting plan and prior investment of 14 hours made the participant continue the less extensive seal repair rather than escalate to a full pump replacement, even after new evidence suggested a mechanical source.",
      "manifestation_in_interview": "The participant explicitly stated the hours already spent factored into the choice, that full pump replacement would have made that prior work 'for nothing,' and that he preferred to 'finish what we'd started' rather than open a larger job.",
      "effect_on_reasoning_or_decision": "Produced a narrower repair action (seal replacement) than the available mechanical-source evidence might otherwise have warranted, preserving the current plan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job.",
          "evidence_explanation": "Describes continuation of the original plan after new residue evidence, with prior progress and time investment explicitly incorporated."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over.",
          "evidence_explanation": "Demonstrates the sunk-cost/commitment mechanism underlying the plan continuation bias."
        }
      ],
      "correction_or_counterevidence": "There were also legitimate operational constraints: the pump part was not on the shelf, full replacement meant additional downtime, and the residue appeared minor. These provide a partial non-bias explanation, but the explicit sunk-cost language indicates that prior investment directly influenced the decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved aviation cockpit corpus identifies plan continuation bias as an established bias influencing flight crew, including later-stage events.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "aircraft exited the runway during the final stages of flight continuation bias was found to have influenced the crew evidence to suppor t a relationship between RE events and plan continuation bias",
          "mechanism_supported_by_source": "Plan continuation bias influenced flight crew decision-making and was associated with continuing an existing course of action.",
          "relevance_to_this_occurrence": "Supports the use of plan continuation bias for the participant's continuation of the existing troubleshooting path despite new contradictory cues."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "overconfidence effect",
      "alternative_labels": ["overconfidence bias", "illusion of validity"],
      "taxonomy_status": "established_label",
      "bias_definition": "Overconfidence effect: subjective confidence in a judgment or decision exceeds what the available evidence objectively justifies.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final RTS sign-off after ground leak check passed",
      "decision_point_description": "Whether to release the aircraft into the holiday schedule without a test-flight crew after only ground-based leak and static checks.",
      "affected_reasoning_operation": "Risk assessment and release/certification judgment",
      "bias_specific_mechanism": "The participant expressed high subjective confidence that the repair was successful despite acknowledging that ground checks could not reproduce the in-flight condition that triggered the caution, and he indicated that even an additional test-flight data point would not have changed his release decision.",
      "manifestation_in_interview": "When asked how sure he was that the issue was fixed, the participant said he was 'Pretty sure' and treated the ground leak check as proof of a leak-based repair, while also acknowledging static testing was not the same environment as flight.",
      "effect_on_reasoning_or_decision": "The aircraft was released with a high degree of stated certainty despite a limited validation environment and an unresolved in-flight caution history.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that.",
          "evidence_explanation": "Shows subjective certainty coexisting with explicit knowledge that the available test did not reproduce the relevant condition, indicating confidence exceeding evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It would've been a nice extra data point, but I don't think it would've changed my decision to release it.",
          "evidence_explanation": "Further demonstrates overconfidence by saying even additional in-flight validation data would not have affected the release decision."
        }
      ],
      "correction_or_counterevidence": "A passed ground leak check and clean static test are standard maintenance verification evidence and may justify release under ordinary procedures. This provides a plausible non-bias explanation and restricts confidence to low.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly addressed overconfidence effect; classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": ["expectation bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Early interpretation of three intermittent Hydraulic System B caution messages",
      "supporting_interview_quote": "my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times.",
      "plausible_mechanism": "An early nuisance-signal hypothesis may have biased interpretation of increasing caution duration and absence of corroborating data as non-significant, consistent with confirmation or expectation bias.",
      "why_not_identified": "The transcript does not contain sufficiently explicit evidence that the participant selectively ignored contradictory information; the early assessment may also be a reasonable diagnostic probability under uncertainty and operational constraints."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "authority bias",
      "alternative_labels": ["expert deference"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Fourth Hydraulic System B caution event with speed brake anomaly",
      "supporting_interview_quote": "The OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
      "plausible_mechanism": "The participant may have over-weighted the OEM field representative's outside expertise relative to the internal senior engineer's recommendation.",
      "why_not_identified": "Relying on an OEM expert can be a legitimate professional heuristic, and the transcript does not provide sufficient independent evidence that this deference, rather than the anchoring mechanism already identified, was the operative distortion."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus is sparse and contains OCR imperfections; only available passages were used for support.",
    "The analysis relies on participant self-report during an interview, not direct observation of the original maintenance decisions.",
    "Some observed judgments may also be supported by standard maintenance heuristics, formal MEL constraints, or operational resource constraints, which were considered as competing explanations.",
    "No outcome data beyond the interview were available, so confidence ratings focus on mechanism presence rather than whether the decisions were objectively incorrect."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a maintenance decision-making review, and that we can reference the tail number and event details generically without naming crew. Participant: That's fine, go ahead. Interviewer: Great. Can you tell me your role and how you came into this event? Participant: I'm the Director of Maintenance at our base station. I oversee line maintenance sign-offs, RTS certifications, and I'm the one who ultimately owns whether an aircraft goes back into the schedule. This one landed on my desk because it kept coming back. Interviewer: Walk me through what the issue looked like when you first became aware of it. Participant: We had a Hydraulic System B caution light show up on one of our E175s—momentary, cleared itself, crew wrote it up. Maintenance ran the BITE test, came back clean, no fault found. Classic CND. It happened three times over about two weeks. Each time, no fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL. The aircraft kept flying its line. Interviewer: What did you make of that pattern at the time? Participant: Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times. We had the holiday peak coming up and needed the airframe in rotation, so grounding it for an open-ended isolation hunt on a CND item felt like overkill at that point. Interviewer: Did the increasing duration register as significant to you? Participant: I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it. Interviewer: What happened next? Participant: Next flight day, it came back a fourth time, and this one ran about twelve seconds—longer than anything before—and the crew also noted a brief speed brake anomaly on the same leg. That's when my senior hydraulics engineer came to me and wanted to pull the aircraft and run the full fault isolation procedure out of the FIM. Interviewer: What did you decide at that point, and how did you get there? Participant: While we were talking about it, our OEM field rep happened to be at the hangar working a different tail. I flagged him down and asked what he thought. He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it. Interviewer: How did your engineer take that? Participant: He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week. Interviewer: What information did you weigh most heavily there, and what didn't you dig into? Participant: Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal. We reset the BITE and flew it two cycles without a recurrence. Interviewer: What came after that? Participant: A few days later, during an unrelated task, one of the techs was near the hydraulic pump and noticed some residue around the seal. Small amount, hadn't been documented before. That was new—nothing like that had shown up in any of the earlier CND checks. Interviewer: What did that change for you? Participant: It told us there might be an actual mechanical source rather than just a sensor quirk. At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job. Interviewer: Did the amount of work already done factor into that choice? Participant: I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over. Interviewer: After the seal replacement, what did you see? Participant: Leak check passed on the ground, static test showed no residue. Clean. Interviewer: What happened at the final sign-off? Participant: We needed the aircraft that afternoon for the holiday schedule, and we didn't have a test-flight crew available same-day. Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved. Interviewer: Given the aircraft's history—three CND events, the fourth longer one with the speed brake note, and the fact that the seal residue never really explained why the caution happened in flight in the first place—how sure were you that this was actually fixed? Participant: Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that. Interviewer: If you'd had a test-flight crew available that day, would that have changed your certainty? Participant: It would've been a nice extra data point, but I don't think it would've changed my decision to release it. Interviewer: Looking back across the whole event, is there a point where, with the same information you had then, you'd make a different call? Participant: Maybe the fourth event—the twelve-second one with the speed brake anomaly. If I'd leaned more toward my engineer's read there instead of the OEM rep's, we might have caught the seal issue earlier instead of a few days later. Interviewer: If the OEM rep hadn't been on-site that day, what do you think you'd have done instead? Participant: Probably would've let my engineer run the full isolation. Having an outside read available in the moment made it easy to go a different direction. Interviewer: Last one—if the seal residue had turned up before you'd started the component swaps, would the escalation decision have gone differently? Participant: Probably, yeah. Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.72s · gen 209.84s · total 213.7s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0275 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0263 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0248 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0247 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
5. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0243 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0240 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0238 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0223 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0214 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0208 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
11. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0194 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
12. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0192 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0185 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0183 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0182 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
17. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _## 16 5 Accidents & incidents Observed Expected The results of the chi 5.76 , p = .01 . The resu_
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
20. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0172 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0169 (rrf) — _# 18, 72% awareness to the outcome of the event 4.2.1 Relationship between flight crew experienc_
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0167 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0166 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
28. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0160 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
30. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0159 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0159 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
33. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0155 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _## Evolut ionary Cognitive Psychology | mals in Pleistocene caves, for instance, demonstrate one_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0151 (rrf) — _# f Space Flight relatively large set of possible systems that are v but not quite perfect, then_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
41. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0150 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
43. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
45. **Human_Cognitive_Bias_Identification_for.pdf** — 0.0145 (rrf) — _# Systems Situation and Environment precondition is that the aircraft preparing to land on a spe_
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
47. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0142 (rrf) — _# 188 | to the one in the | explanation condition). Informed by prior work that a slow algorithm_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single interview analyzed for cognitive bias mechanisms in maintenance decision-making. Retrieved corpus passages supported confirmation bias, plan continuation bias, and anchoring/adjustment; overconfidence was classified from general cognitive-science knowledge because retrieved corpus support was not available for that label."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence bias",
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
      "confidence": "low",
      "bias_label": "anchoring and adjustment heuristic",
      "alternative_labels": [
        "anchoring bias",
        "anchoring and insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to make estimates or interpretations by starting from an initial value or impression and adjusting insufficiently in response to subsequent information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting the pattern of recurrent intermittent hydraulic caution lights",
      "decision_point_description": "Whether to treat the repeated caution-light events as a nuisance signal and continue monitoring, or to escalate investigation earlier.",
      "affected_reasoning_operation": "Diagnostic interpretation and monitoring decision under uncertainty",
      "bias_specific_mechanism": "The initial interpretation of the event as a likely nuisance signal/noisy sensor serves as an anchor. The participant explicitly notices the duration increasing from about two to five seconds but under-adjusts from the initial anchor because the absolute increase seems small and there is no corroborating fluid/pressure data.",
      "manifestation_in_interview": "The participant initially classified the intermittent caution lights as nuisance signals and then did not treat the increasing duration as a meaningful trend.",
      "effect_on_reasoning_or_decision": "Maintained the airframe in service and avoided earlier deeper isolation or grounding while the same issue continued to recur.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times.",
          "evidence_explanation": "This establishes the early 'nuisance signal' interpretation that becomes the anchor for later judgments."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it.",
          "evidence_explanation": "The participant notices disconfirming trend information but adjusts from the initial anchor only weakly, treating a small absolute increase as non-significant."
        }
      ],
      "correction_or_counterevidence": "The participant did notice the increase and kept monitoring; lack of fluid/pressure data and MEL constraints are legitimate non-bias factors.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support available for the anchoring and adjustment heuristic.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat... Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "Anchoring on an initial value with insufficient adjustment from subsequent information.",
          "relevance_to_this_occurrence": "The participant anchored on the initial nuisance-signal interpretation and under-adjusted after noticing the increasing durations."
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
        "expectation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's pre-existing beliefs or hypotheses while giving disproportionately less consideration to disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth caution event with speed brake anomaly and competing reset versus isolation paths",
      "decision_point_description": "Whether to pull the aircraft for full FIM fault isolation or perform the suggested reset and keep the aircraft flying.",
      "affected_reasoning_operation": "Evaluation of competing maintenance hypotheses and information weighting",
      "bias_specific_mechanism": "The participant selectively favors information consistent with the initial nuisance/BITE interpretation—the OEM representative's reset account and a remembered in-house case—while discounting the disconfirming speed brake anomaly and the senior engineer's recommendation for formal isolation. He also does not verify whether the remembered similar case actually matches the current one.",
      "manifestation_in_interview": "The participant described the OEM account and memory as feeling like 'we already had the answer' and chose the reset path over the engineer's formal fault isolation.",
      "effect_on_reasoning_or_decision": "The full FIM isolation was not run, the reset was performed, and the aircraft was kept flying; the mechanical leak was not identified until later.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.",
          "evidence_explanation": "This demonstrates preference for information consistent with the pre-existing sense that the problem was a known quirk rather than a mechanical fault."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
          "evidence_explanation": "The participant explicitly weighs an outside confirming opinion more heavily than the disconfirming anomaly and the engineer's formal-procedure recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
          "evidence_explanation": "This shows recall being used to confirm similarity without testing whether the past case was diagnostically equivalent."
        }
      ],
      "correction_or_counterevidence": "The senior engineer objected and recommended formal fault isolation; the OEM representative may have been a legitimate expert source. The decision may also have been influenced by operational pressure, but the stated reasoning shows selective weight toward confirming evidence.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support available for confirmation bias.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "the investigation found the visual cues available to the crew induced a state of confirmation bias which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft’s position.",
          "mechanism_supported_by_source": "Confirmation bias: using cues consistent with a pre-existing mental model and ignoring contradictory evidence.",
          "relevance_to_this_occurrence": "The participant favored the OEM reset account and remembered similar case while ignoring or discounting the speed brake anomaly and the engineer's formal isolation recommendation."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "sunk cost fallacy",
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an original plan or course of action despite cues or new evidence indicating that the plan should be changed, often related to sunk costs and escalation of commitment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Discovery of physical residue near the hydraulic pump and repair-scope decision",
      "decision_point_description": "Whether to escalate to full hydraulic pump replacement or continue the incremental seal-replacement path already underway.",
      "affected_reasoning_operation": "Escalation and repair-scope decision after new evidence of a mechanical source",
      "bias_specific_mechanism": "The participant continues the original incremental troubleshooting plan partly because substantial time and component replacements have already been invested. The sunk hours make the cost of switching to a larger repair feel wasteful, so the smaller seal replacement is selected despite evidence of a possible mechanical leak.",
      "manifestation_in_interview": "After residue was found, the participant decided to replace the seal and finish the started plan rather than open a bigger job, explicitly citing the hours already sunk.",
      "effect_on_reasoning_or_decision": "The participant chose the limited seal fix over full pump replacement, potentially delaying definitive resolution of the hydraulic problem.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job.",
          "evidence_explanation": "The participant explicitly links the decision to stay on the incremental path to the prior troubleshooting investment already made."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over.",
          "evidence_explanation": "This confirms that sunk costs and avoidance of lost prior work influenced the repair-scope decision."
        }
      ],
      "correction_or_counterevidence": "There were legitimate operational constraints: the part was not on the shelf, full pump replacement added downtime, and the residue was minor. The bias is identified because the participant himself says sunk hours factored into the choice.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support available for plan continuation bias.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "continuation bias was found to have influenced the crew evidence to suppor t a relationship between RE events and plan continuation bias",
          "mechanism_supported_by_source": "Plan continuation bias: continuing with an existing plan despite evidence or reasons to change it.",
          "relevance_to_this_occurrence": "The participant continued the incremental seal-fix path after new residue evidence rather than escalating to full pump replacement, partly because of hours already sunk."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "overconfidence bias",
      "alternative_labels": [
        "overconfidence effect",
        "illusion of validity"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The miscalibration of subjective confidence relative to objective evidence or accuracy, often producing greater certainty than is warranted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final RTS certification after seal replacement and ground checks",
      "decision_point_description": "Whether to sign the RTS certification and release the aircraft without a test flight.",
      "affected_reasoning_operation": "Release and reliability judgment under unresolved uncertainty",
      "bias_specific_mechanism": "The participant treats a passed ground leak check and static test as sufficient proof that the in-flight fault is resolved, even though he explicitly knows ground checks cannot reproduce the exact in-flight condition that triggered the caution. This suggests subjective confidence exceeds the evidential basis.",
      "manifestation_in_interview": "The participant stated he was 'pretty sure' the aircraft was fixed and that a test flight would not have changed his decision, despite acknowledging the ground test environment was not equivalent to the in-flight condition.",
      "effect_on_reasoning_or_decision": "The aircraft was signed off and released based on ground-test evidence that did not reproduce the triggering condition.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that.",
          "evidence_explanation": "The participant acknowledges a known evidentiary gap while still expressing high confidence and treating the passed leak check as proof."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It would've been a nice extra data point, but I don't think it would've changed my decision to release it.",
          "evidence_explanation": "This indicates that additional in-flight validation would not have reduced uncertainty enough to change the decision, suggesting confidence was already high on limited ground-test evidence."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the limitation of ground testing, and standard maintenance practice often accepts ground leak checks for seal replacements. The identification is based on the stated certainty relative to the acknowledged unresolved uncertainty.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism derived from general cognitive-science knowledge; retrieved corpus support was not available for overconfidence bias.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Fourth caution event: weighing the remembered in-house caution-light case against current evidence",
      "supporting_interview_quote": "I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
      "plausible_mechanism": "The ease of recalling a previous similar-sounding caution-light case may have inflated its relevance and likelihood, making the current event feel like the same issue without diagnostic verification.",
      "why_not_identified": "The memory was used alongside an OEM representative's independent account and may be ordinary pattern recognition; it is also embedded in the stronger confirmation-bias occurrence rather than clearly separable as an independent availability effect."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is self-reported and may omit contemporaneous reasoning details or reconstruct post-hoc justifications.",
    "Some findings coexist with legitimate operational constraints such as MEL rules, part availability, downtime pressure, and absent test-flight crew; bias was identified only where a distinct reasoning mechanism was stated or strongly implied.",
    "Retrieved corpus passages contain OCR artifacts and limited metadata.",
    "The overconfidence occurrence is supported by general cognitive-science knowledge rather than the retrieved corpus."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a maintenance decision-making review, and that we can reference the tail number and event details generically without naming crew. Participant: That's fine, go ahead. Interviewer: Great. Can you tell me your role and how you came into this event? Participant: I'm the Director of Maintenance at our base station. I oversee line maintenance sign-offs, RTS certifications, and I'm the one who ultimately owns whether an aircraft goes back into the schedule. This one landed on my desk because it kept coming back. Interviewer: Walk me through what the issue looked like when you first became aware of it. Participant: We had a Hydraulic System B caution light show up on one of our E175s—momentary, cleared itself, crew wrote it up. Maintenance ran the BITE test, came back clean, no fault found. Classic CND. It happened three times over about two weeks. Each time, no fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL. The aircraft kept flying its line. Interviewer: What did you make of that pattern at the time? Participant: Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times. We had the holiday peak coming up and needed the airframe in rotation, so grounding it for an open-ended isolation hunt on a CND item felt like overkill at that point. Interviewer: Did the increasing duration register as significant to you? Participant: I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it. Interviewer: What happened next? Participant: Next flight day, it came back a fourth time, and this one ran about twelve seconds—longer than anything before—and the crew also noted a brief speed brake anomaly on the same leg. That's when my senior hydraulics engineer came to me and wanted to pull the aircraft and run the full fault isolation procedure out of the FIM. Interviewer: What did you decide at that point, and how did you get there? Participant: While we were talking about it, our OEM field rep happened to be at the hangar working a different tail. I flagged him down and asked what he thought. He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it. Interviewer: How did your engineer take that? Participant: He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week. Interviewer: What information did you weigh most heavily there, and what didn't you dig into? Participant: Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal. We reset the BITE and flew it two cycles without a recurrence. Interviewer: What came after that? Participant: A few days later, during an unrelated task, one of the techs was near the hydraulic pump and noticed some residue around the seal. Small amount, hadn't been documented before. That was new—nothing like that had shown up in any of the earlier CND checks. Interviewer: What did that change for you? Participant: It told us there might be an actual mechanical source rather than just a sensor quirk. At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job. Interviewer: Did the amount of work already done factor into that choice? Participant: I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over. Interviewer: After the seal replacement, what did you see? Participant: Leak check passed on the ground, static test showed no residue. Clean. Interviewer: What happened at the final sign-off? Participant: We needed the aircraft that afternoon for the holiday schedule, and we didn't have a test-flight crew available same-day. Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved. Interviewer: Given the aircraft's history—three CND events, the fourth longer one with the speed brake note, and the fact that the seal residue never really explained why the caution happened in flight in the first place—how sure were you that this was actually fixed? Participant: Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that. Interviewer: If you'd had a test-flight crew available that day, would that have changed your certainty? Participant: It would've been a nice extra data point, but I don't think it would've changed my decision to release it. Interviewer: Looking back across the whole event, is there a point where, with the same information you had then, you'd make a different call? Participant: Maybe the fourth event—the twelve-second one with the speed brake anomaly. If I'd leaned more toward my engineer's read there instead of the OEM rep's, we might have caught the seal issue earlier instead of a few days later. Interviewer: If the OEM rep hadn't been on-site that day, what do you think you'd have done instead? Participant: Probably would've let my engineer run the full isolation. Having an outside read available in the moment made it easy to go a different direction. Interviewer: Last one—if the seal residue had turned up before you'd started the component swaps, would the escalation decision have gone differently? Participant: Probably, yeah. Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.72s · gen 221.54s · total 225.3s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0275 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0263 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0248 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0247 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
5. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0243 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0240 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0238 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0223 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0214 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0208 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
11. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0194 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
12. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0192 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0191 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0185 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0183 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0182 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
17. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _## 16 5 Accidents & incidents Observed Expected The results of the chi 5.76 , p = .01 . The resu_
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
20. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0172 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0169 (rrf) — _# 18, 72% awareness to the outcome of the event 4.2.1 Relationship between flight crew experienc_
23. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0167 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
24. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0166 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
25. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
28. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0160 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0159 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
30. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0159 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0159 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
33. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0155 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0153 (rrf) — _## Evolut ionary Cognitive Psychology | mals in Pleistocene caves, for instance, demonstrate one_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
37. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0152 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0151 (rrf) — _# f Space Flight relatively large set of possible systems that are v but not quite perfect, then_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
40. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
41. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0150 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
43. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
45. **Human_Cognitive_Bias_Identification_for.pdf** — 0.0145 (rrf) — _# Systems Situation and Environment precondition is that the aircraft preparing to land on a spe_
46. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 5. Discussion 5.4 The operating e nvironment Research by Leone place between the hours of on i_
47. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0142 (rrf) — _# 188 | to the one in the | explanation condition). Informed by prior work that a slow algorithm_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of the maintenance decision interview; only bias-specific mechanisms affirmatively evidenced by the transcript are classified."
  },
  "identified_bias_summary": [
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
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory information search", "confirmation/expectation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and weight information in ways that confirm an existing belief or favored hypothesis while underweighting contradictory information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth hydraulic caution event: reset-and-fly vs full fault isolation",
      "decision_point_description": "After the OEM field rep suggested a known BITE/software pattern and an in-house memory recalled a similar caution, the participant decided to defer his engineer's requested FIM fault isolation and keep the aircraft flying.",
      "affected_reasoning_operation": "Diagnostic hypothesis evaluation and information weighting",
      "bias_specific_mechanism": "The participant preferentially accepted and weighted hypothesis-consistent information (the OEM rep's software/BITE quirk report and the remembered in-house case) while discounting contradictory evidence (the longer 12-second event, the speed brake anomaly, and his engineer's recommendation for full isolation). He did not verify whether the remembered in-house case matched this event.",
      "manifestation_in_interview": "The participant reported that the OEM rep's account and the in-house memory made him feel he already had the answer, so he overruled the engineer's full-isolation request and did not check the earlier case for matches.",
      "effect_on_reasoning_or_decision": "The biased weighting produced a reset-and-fly decision rather than full fault isolation, delaying identification of a possible mechanical source and permitting continued operation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.",
          "evidence_explanation": "This shows the participant treating two confirmatory anecdotes as sufficient to resolve the diagnostic question, despite the absence of direct matching evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
          "evidence_explanation": "This shows the contradictory interpretation was acknowledged but weighted less than the confirmatory outside read."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
          "evidence_explanation": "This explicitly demonstrates selective acceptance of a remembered confirmatory case without verifying its similarity."
        }
      ],
      "correction_or_counterevidence": "The engineer disagreed and requested full FIM isolation; the OEM rep had fleet-wide model experience; the earlier CND checks had shown no fluid/pressure abnormality; and the aircraft flew two cycles after reset without recurrence. The participant later said that on the fourth event he might have leaned toward the engineer's read.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft’s position",
          "mechanism_supported_by_source": "The source describes confirmation bias in aviation as following confirmatory cues while ignoring contradictory evidence.",
          "relevance_to_this_occurrence": "The participant similarly followed confirmatory OEM and in-house anecdotal cues and ignored the contradictory speed-brake cue and engineer's full-isolation request."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["sunk cost fallacy", "escalation of commitment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an original plan or course of action despite new information or cues that should trigger reconsideration or a changed plan.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-residue discovery: seal-only repair vs full pump replacement",
      "decision_point_description": "After a technician found residue around the hydraulic pump seal, the participant decided to replace only the seal and continue the existing incremental troubleshooting path rather than escalate to full pump replacement.",
      "affected_reasoning_operation": "Repair-scope escalation decision under new mechanical evidence",
      "bias_specific_mechanism": "The participant continued the existing course because of invested resources and proximity to completion: fourteen hours of troubleshooting, already-swapped accumulator and sensor, and reluctance to make that work 'for nothing.' New evidence of a possible mechanical source did not trigger full replanning.",
      "manifestation_in_interview": "The participant explicitly said the hours already spent and the desire to avoid wasted work affected the decision, framing the seal fix as closing out the original plan rather than opening a larger job.",
      "effect_on_reasoning_or_decision": "The repair scope was narrowed to seal replacement instead of full pump replacement, potentially leaving a mechanical source insufficiently resolved.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job.",
          "evidence_explanation": "This shows the participant explicitly using prior investment and plan proximity to continue the existing plan despite a new mechanical cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over.",
          "evidence_explanation": "This is an explicit admission of sunk-cost reasoning influencing the escalation decision."
        }
      ],
      "correction_or_counterevidence": "Full pump replacement would have caused more downtime and the part was not on the shelf; the residue was minor; and the seal replacement later passed ground leak and static checks. These are legitimate operational considerations, but the explicit sunk-cost reasoning remains affirmatively present.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved source supports the plan-continuation label; the specific sunk-cost/escalation route is inferred from the transcript and general knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "a relationship between RE events and plan continuation bias",
          "mechanism_supported_by_source": "The source identifies plan continuation bias as a factor in aviation events involving continued courses of action.",
          "relevance_to_this_occurrence": "The participant similarly continued the existing maintenance plan after a new mechanical cue, with explicit sunk-cost and finish-the-plan reasoning."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "overconfidence effect",
      "alternative_labels": ["miscalibration", "illusion of validity"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "RTS sign-off after ground leak/static checks",
      "supporting_interview_quote": "I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that.",
      "plausible_mechanism": "Subjective certainty may have exceeded what the evidence warranted, given the unresolved in-flight trigger and lack of test flight.",
      "why_not_identified": "No objective outcome or calibration evidence is available; standard passed ground checks for RTS are a legitimate professional basis, and schedule constraints were present. This is plausible but below the affirmative mechanism-specific bar."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages mainly address flight-deck decision-making rather than maintenance decision-making, so labels were applied by analogy where mechanism matched.",
    "No post-RTS outcome data is available; therefore overconfidence or accuracy-based bias claims could not be affirmatively tested.",
    "Cognitive mechanisms are inferred from participant self-report, though the key quotes are explicit about the relevant reasoning."
  ]
}

