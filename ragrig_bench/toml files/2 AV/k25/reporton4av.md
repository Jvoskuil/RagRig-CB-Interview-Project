# RAG Benchmark — 2026-09-09

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. As we discussed, this is a confidential debrief for training research purposes — I'll ask about a specific check ride, and I'd like you to walk me through what happened as concretely as you can. Nothing here goes into your personnel file. Sound okay? Participant: Sure, happy to talk through it. It was a Line Check, OPC cycle, on one of our senior widebody captains — guy's got probably twenty-two thousand hours, most of it on type. I was in the jump seat as the TRE. Interviewer: What was the flight supposed to accomplish, and what was your role exactly? Participant: Standard revenue flight, but I'm there to evaluate his technical handling and CRM for his recurrent check. First officer was PM. My job is to observe, grade, and intervene only if safety requires it. Interviewer: Take me through what actually happened, from the start. Participant: Before we even got to the airplane, I saw the tech log had two previous write-ups — ADIRU 2 miscompare, both times it cleared on its own, maintenance found nothing conclusive, and it came back MEL'd as okay to fly. So going in, I already had that context. We did the walk-around, briefed, nothing unusual. Departure was normal. Climbing out through about FL250, we got a brief ADIRU disagree indication on the EICAS — flickered for maybe ten seconds and went away. No checklist triggered automatically, so it wasn't like the system was demanding we do anything. Then in cruise, it came back, but this time it showed up as a disagreement between the captain's and first officer's airspeed and altitude tapes. That's more attention-getting because now you've got two primary displays disagreeing with each other, not just an internal comparator flag. The captain worked through it — cross-checked against the standby instruments, talked the FO through what he was seeing, and the indications came back together within a couple minutes. Rest of the flight was uneventful. Normal approach, normal landing. Interviewer: And afterward? Participant: I wrote up my report. Graded the captain's overall performance. A colleague of mine, another TRE, looked at the write-up informally and asked whether I'd been a little quick to wave things off given the fault's history. I pushed back on that. Then a few days later maintenance found an intermittent connector fault in the ADIRU wiring bay — that's likely what caused all three episodes. So there was an actual physical problem the whole time, it just wasn't consistent enough to nail down on the ground. Interviewer: Let's go back to that pre-departure moment. What went through your mind when you saw the tech log entries? Participant: Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further. Interviewer: Did you consider asking for another maintenance look before departure? Participant: Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going. Interviewer: What would have had to be different on paper for you to hold the flight? Participant: If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than 'checked, no fault found,' that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved. Interviewer: Move to the climb, when the flag flickered again. Walk me through that moment specifically. Participant: We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports. Interviewer: What alternative did you weigh at that point? Participant: Leveling off and running the full non-normal procedure, get maintenance control on the radio. I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting. Interviewer: How confident were you in that read at the time? Participant: Pretty confident, honestly. I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample. Interviewer: Let's talk about cruise, when the airspeed and altitude displays actually disagreed between the two pilots' instruments. What did you observe the captain do, and how did you evaluate it? Participant: He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either. Interviewer: How did you grade that? Participant: I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order. Interviewer: If a first-year captain had handled it the identical way, would you have graded it the same? Participant: Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work. Interviewer: Last one — the conversation with your colleague afterward. He suggested your calls that day might have been shaped by the crew's clean history. How did you respond to that? Participant: I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built. Interviewer: Is there anything that would change your mind about that day, looking back? Participant: If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made. Interviewer: Last question. If you ran this exact flight again with exactly the same information you had at the time, what would you do differently? Participant: Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.

_ranker=rrf · t=0.04 · k=25 → 25 in context · 8192 ctx · emb 3.08s · gen 228.92s · total 234.3s_

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

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the participant's reasoning about the pre-departure ADIRU fault history, in-flight ADIRU indications, assessment of the observed captain's performance, and response to a colleague's feedback. Retrieved corpus material provided direct support for anchoring/confirmation mechanisms; other identified biases rely on established cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring_and_adjustment",
      "identified_occurrence_count": 1
    },
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
    },
    {
      "bias_label": "overconfidence_effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring_and_adjustment",
      "alternative_labels": ["anchoring", "anchoring_heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to form an estimate or risk judgment from an initial reference point, and then adjust insufficiently in response to later information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-departure review of the ADIRU 2 miscompare tech log entry",
      "decision_point_description": "Whether to request another maintenance inspection before accepting the aircraft despite two prior self-clearing ADIRU 2 miscompare write-ups.",
      "affected_reasoning_operation": "Pre-flight risk assessment and go/no-go decision",
      "bias_specific_mechanism": "The participant used the existing maintenance release and the two prior self-clearing events as an anchor: the aircraft was a 'documented, dispositioned item.' From that anchor, he adjusted his estimate of unresolved-fault risk upward only minimally, interpreting the history itself as evidence that no further inspection was needed.",
      "manifestation_in_interview": "He treated the prior no-fault-found maintenance release and two benign outcomes as a stable, known quantity, and explicitly said the history felt like the justification for going.",
      "effect_on_reasoning_or_decision": "He decided not to seek another maintenance look before departure and proceeded with the flight, discounting the possibility of an unresolved intermittent wiring fault.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further.",
          "evidence_explanation": "Demonstrates an initial judgment strongly based on the prior maintenance disposition and the two self-clearing events."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going.",
          "evidence_explanation": "Shows that the initial no-fault/history anchor persisted and was used as the primary justification for not seeking further inspection."
        }
      ],
      "correction_or_counterevidence": "Relying on an MEL release and existing maintenance action is procedurally legitimate, and the lack of a new hard symptom is a plausible non-bias explanation. The bias evidence is that the participant subjectively converted the repeated self-clearing history into a 'known quantity' and used that anchor as the positive reason to proceed.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved verification-and-validation source provides an operational definition of anchoring and adjustment, validating the mechanism of insufficient adjustment from an initial value.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, \"adjustments are typically insufficient.\"",
          "mechanism_supported_by_source": "Defines anchoring on an initial answer and the typical insufficient adjustment from that anchor.",
          "relevance_to_this_occurrence": "Supports the classification of the participant's reliance on the initial maintenance release and benign history as an anchor from which he insufficiently adjusted his risk estimate."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation_bias",
      "alternative_labels": ["positive_test_strategy", "confirmatory_hypothesis_testing"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's existing beliefs or hypotheses, while giving disproportionately less consideration to disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "In-flight ADIRU disagree indication during climb",
      "decision_point_description": "Whether to continue the climb or level off, run the full non-normal procedure, and contact maintenance control.",
      "affected_reasoning_operation": "Interpretation of an ambiguous in-flight caution indication and decision to continue",
      "bias_specific_mechanism": "The participant fitted the novel in-flight caution to his prior mental model of a self-clearing benign pattern. He used the new occurrence as confirmation of the existing pattern rather than as possible disconfirming evidence that the underlying fault was unresolved and potentially significant.",
      "manifestation_in_interview": "When the disagree flag appeared during climb, he immediately categorized it as 'exactly like the tech log said' and directed the crew to continue the climb, while dismissing the alternative of leveling off as overreaction.",
      "effect_on_reasoning_or_decision": "He avoided interrupting the climb and initiating a full non-normal procedure or maintenance-control consultation, leaving a possible unresolved intermittent fault without real-time escalation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.",
          "evidence_explanation": "Shows immediate interpretation of the new signal as fitting the prior pattern, rather than as independent evidence about an unresolved fault."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Leveling off and running the full non-normal procedure, get maintenance control on the radio. I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting.",
          "evidence_explanation": "Shows that a disconfirming/escalation alternative was considered but dismissed because it did not fit the prior self-resolving pattern."
        }
      ],
      "correction_or_counterevidence": "No automatic checklist trigger and a transient, self-clearing indication may lawfully support a non-escalation decision under standard operating practice. The bias is identifiable in the participant's explicit pattern-fitting and failure to treat the recurrence as potential evidence against the benign-pattern hypothesis.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit-cognitive-bias source directly describes confirmation bias in aviation as the use of cues that support an existing mental model while ignoring contradictory evidence, and the verification-and-validation source describes positive test strategy.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC conditions, found that the crew’s confirmation bias was supported by being able to visually identify cues that supported their mental model such as yellow markers on the taxiway which were perceived to be yellow runway markers.",
          "mechanism_supported_by_source": "Describes confirmation bias as evidence being interpreted to support an existing mental model while contradictory evidence is ignored.",
          "relevance_to_this_occurrence": "Directly supports the participant's use of the self-clearing fault history as a mental model into which the climb indication was assimilated."
        },
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The strategy employed by most participants is known positive test strategy (PTS).",
          "mechanism_supported_by_source": "Identifies positive test strategy as testing hypotheses through confirming cases rather than falsifying alternatives.",
          "relevance_to_this_occurrence": "Supports the classification of the participant's repeated pattern-matching as a positive-test, confirmation-oriented strategy."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence_effect",
      "alternative_labels": ["overconfidence_bias", "miscalibration"],
      "taxonomy_status": "established_label",
      "bias_definition": "A miscalibration between subjective confidence and objective accuracy, in which a person overestimates the correctness or predictive value of a judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Confidence evaluation during the climb ADIRU disagree indication",
      "decision_point_description": "Whether to trust the initial interpretation strongly enough to forgo escalation.",
      "affected_reasoning_operation": "Confidence calibration and real-time probabilistic assessment",
      "bias_specific_mechanism": "The participant expressed high subjective confidence in the benign-pattern interpretation based on only two prior ground occurrences and one brief in-flight occurrence. He later acknowledged that three brief occurrences were not sufficient to know what an intermittent wiring fault would do next, indicating that his confidence at the time was miscalibrated relative to the evidentiary base.",
      "manifestation_in_interview": "He said he was 'pretty confident' and felt he had 'already seen this movie,' treating a limited sample as a clear and reliable pattern.",
      "effect_on_reasoning_or_decision": "High but poorly calibrated confidence reduced the perceived need for escalation and made the alternative of leveling off seem like overreaction.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Pretty confident, honestly. I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching.",
          "evidence_explanation": "Demonstrates high subjective confidence based on only three occurrence data points."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.",
          "evidence_explanation": "Explicitly reveals a gap between the confidence experienced at the time and the limited informational base."
        }
      ],
      "correction_or_counterevidence": "The confidence judgment was made under real-time operational uncertainty, and some degree of reliance on prior behavior is normal. The bias is supported because the participant himself later distinguishes between the felt clarity of the pattern and the insufficient sample.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed overconfidence or miscalibration. This classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "halo_effect",
      "alternative_labels": ["halo_error", "experience_halo"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a positive impression or characteristic in one domain to influence judgments or evaluations in another domain.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Grading the captain's handling of the in-flight airspeed/altitude disagreement in cruise",
      "decision_point_description": "Whether to grade the captain's failure to follow the QRH in order as satisfactory or to mark procedural non-compliance.",
      "affected_reasoning_operation": "Performance evaluation and grading judgment",
      "bias_specific_mechanism": "The captain's extensive flight hours, type experience, and calm handling created a positive global impression that generalized into the participant's judgment of procedural compliance. The participant explicitly weighed the captain's seniority and real-time cross-check more heavily than step-by-step QRH verification.",
      "manifestation_in_interview": "He graded the captain satisfactory despite observing that the captain did not work through the QRH in order, and he stated that a first-year captain with identical behavior would not have been graded as generously.",
      "effect_on_reasoning_or_decision": "The participant assigned a satisfactory grade and did not verify each item in the checklist sequence, granting seniority-based leniency for procedural non-compliance.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order.",
          "evidence_explanation": "Shows that seniority and type experience dominated the evaluation of procedural compliance."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.",
          "evidence_explanation": "Demonstrates differential grading standards for identical behavior based on the captain's experience and reputation."
        }
      ],
      "correction_or_counterevidence": "Holistic evaluation of a captain's calm and successful handling of an abnormality can be professionally relevant, and experience may legitimately inform a TRE's global assessment. The bias is indicated because the participant explicitly shifted the procedural standard for identical behavior based on seniority rather than objective checklist adherence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed halo effect or experience-based evaluation bias. This classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bias_blind_spot",
      "alternative_labels": ["bias blind spot", "asymmetric_self_assessment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize cognitive biases more readily in others than in oneself.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to a colleague's suggestion that the clean history may have biased the day's calls",
      "decision_point_description": null,
      "affected_reasoning_operation": "Self-assessment and evaluation of feedback about one's own judgment",
      "bias_specific_mechanism": "When challenged about whether the crew's clean history had biased his calls, the participant categorically denied that this could apply to him and attributed such risk to less experienced check airmen. This asymmetric attribution prevented him from updating his self-assessment.",
      "manifestation_in_interview": "He stated that the bias risk was more relevant to someone earlier in their check-airman career, while his own structured process and clean record made him exempt.",
      "effect_on_reasoning_or_decision": "He dismissed corrective peer feedback and reinforced confidence in his initial decisions rather than reconsidering whether pattern recognition had influenced him.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.",
          "evidence_explanation": "Shows explicit self-exemption from bias while attributing the same risk to less experienced colleagues."
        }
      ],
      "correction_or_counterevidence": "A structured process and extensive experience can legitimately reduce error risk, and confidence in one's professional process is not inherently biased. The bias blind spot is evidenced by the categorical self-exemption and asymmetric attribution of susceptibility to others.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed the bias blind spot. This classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan_continuation_bias",
      "alternative_labels": ["continuation_bias", "get-there-itis"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Climb and cruise decisions to continue despite repeated ADIRU indications",
      "supporting_interview_quote": "I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.",
      "plausible_mechanism": "The participant may have continued the original flight plan despite accumulating evidence of an unresolved intermittent fault, consistent with plan continuation pressure.",
      "why_not_identified": "The evidence is more parsimoniously explained by confirmation bias and standard operational practice; it does not demonstrate a distinct goal-directed continuation mechanism independent from the interpretation of the warnings as familiar and benign."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "outcome_bias",
      "alternative_labels": ["result_effect"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Retrospective evaluation of the day's decisions after learning of the intermittent connector fault",
      "supporting_interview_quote": "If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made.",
      "plausible_mechanism": "The participant may have judged the quality of his earlier decisions by the benign final outcome rather than by the information available and the decision process at the time.",
      "why_not_identified": "This occurred as retrospective self-justification and was not a discrete operational decision being made at the time; it is less clearly a distinct bias than the other identified occurrences."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based solely on a self-reported debrief transcript without independent flight data, cockpit voice recordings, checklist records, or maintenance documentation.",
    "Some identified biases rely on general cognitive-science knowledge because the retrieved corpus did not contain direct support for every label.",
    "Several identified mechanisms overlap; the analysis separated them only where distinct distortion processes were evidenced.",
    "The presence of legitimate operational procedures and the absence of a bad outcome do not rule out bias, but they provide plausible non-bias explanations that limit confidence."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. As we discussed, this is a confidential debrief for training research purposes — I'll ask about a specific check ride, and I'd like you to walk me through what happened as concretely as you can. Nothing here goes into your personnel file. Sound okay? Participant: Sure, happy to talk through it. It was a Line Check, OPC cycle, on one of our senior widebody captains — guy's got probably twenty-two thousand hours, most of it on type. I was in the jump seat as the TRE. Interviewer: What was the flight supposed to accomplish, and what was your role exactly? Participant: Standard revenue flight, but I'm there to evaluate his technical handling and CRM for his recurrent check. First officer was PM. My job is to observe, grade, and intervene only if safety requires it. Interviewer: Take me through what actually happened, from the start. Participant: Before we even got to the airplane, I saw the tech log had two previous write-ups — ADIRU 2 miscompare, both times it cleared on its own, maintenance found nothing conclusive, and it came back MEL'd as okay to fly. So going in, I already had that context. We did the walk-around, briefed, nothing unusual. Departure was normal. Climbing out through about FL250, we got a brief ADIRU disagree indication on the EICAS — flickered for maybe ten seconds and went away. No checklist triggered automatically, so it wasn't like the system was demanding we do anything. Then in cruise, it came back, but this time it showed up as a disagreement between the captain's and first officer's airspeed and altitude tapes. That's more attention-getting because now you've got two primary displays disagreeing with each other, not just an internal comparator flag. The captain worked through it — cross-checked against the standby instruments, talked the FO through what he was seeing, and the indications came back together within a couple minutes. Rest of the flight was uneventful. Normal approach, normal landing. Interviewer: And afterward? Participant: I wrote up my report. Graded the captain's overall performance. A colleague of mine, another TRE, looked at the write-up informally and asked whether I'd been a little quick to wave things off given the fault's history. I pushed back on that. Then a few days later maintenance found an intermittent connector fault in the ADIRU wiring bay — that's likely what caused all three episodes. So there was an actual physical problem the whole time, it just wasn't consistent enough to nail down on the ground. Interviewer: Let's go back to that pre-departure moment. What went through your mind when you saw the tech log entries? Participant: Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further. Interviewer: Did you consider asking for another maintenance look before departure? Participant: Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going. Interviewer: What would have had to be different on paper for you to hold the flight? Participant: If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than 'checked, no fault found,' that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved. Interviewer: Move to the climb, when the flag flickered again. Walk me through that moment specifically. Participant: We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports. Interviewer: What alternative did you weigh at that point? Participant: Leveling off and running the full non-normal procedure, get maintenance control on the radio. I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting. Interviewer: How confident were you in that read at the time? Participant: Pretty confident, honestly. I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample. Interviewer: Let's talk about cruise, when the airspeed and altitude displays actually disagreed between the two pilots' instruments. What did you observe the captain do, and how did you evaluate it? Participant: He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either. Interviewer: How did you grade that? Participant: I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order. Interviewer: If a first-year captain had handled it the identical way, would you have graded it the same? Participant: Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work. Interviewer: Last one — the conversation with your colleague afterward. He suggested your calls that day might have been shaped by the crew's clean history. How did you respond to that? Participant: I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built. Interviewer: Is there anything that would change your mind about that day, looking back? Participant: If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made. Interviewer: Last question. If you ran this exact flight again with exactly the same information you had at the time, what would you do differently? Participant: Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.

_ranker=rrf · t=0.04 · k=25 → 25 in context · 8192 ctx · emb 1.94s · gen 155.41s · total 159.4s_

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

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a single training-research debrief about a line check. The participant is the TRE/evaluator; statements reflect both in-the-moment decisions and retrospective self-assessment."
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
      "bias_label": "Halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Illusion of validity",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": ["anchoring bias", "anchoring"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely heavily on an initial value or reference point and to make insufficient adjustments away from it when new information emerges.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-departure tech-log review and decision to proceed",
      "decision_point_description": "Whether to request another maintenance inspection before departure based on two prior self-cleared ADIRU write-ups.",
      "affected_reasoning_operation": "Risk assessment and diagnostic interpretation",
      "bias_specific_mechanism": "The documented maintenance history of two self-clearing ADIRU events became an initial reference point; the participant treated the fault as a known quantity and underadjusted to later ambiguous in-flight symptoms.",
      "manifestation_in_interview": "The participant described the prior write-ups as a 'known quantity' and said the self-clearing pattern made the fault feel like a non-issue rather than an unresolved intermittent problem.",
      "effect_on_reasoning_or_decision": "He decided not to seek another maintenance inspection before departure and later interpreted the climb-phase flicker through the same anchored frame.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening.",
          "evidence_explanation": "This quote shows the initial reference point: two prior self-clearing events and a maintenance release were treated as sufficient to characterize the fault as benign and predictable."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than 'checked, no fault found,' that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved.",
          "evidence_explanation": "This quote shows the anchoring effect: the past self-clearing behavior dominated the assessment, while the unresolved intermittent nature of the fault was not treated as diagnostically important."
        }
      ],
      "correction_or_counterevidence": "The participant did briefly consider requesting another maintenance look and later considered leveling off and running the full non-normal procedure during the climb, but both alternatives were rejected using the same anchored pattern.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label and mechanism are supported by a retrieved passage on the anchoring and adjustment heuristic.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "People make estimates based on an initial value and adjust insufficiently from it when additional information becomes available.",
          "relevance_to_this_occurrence": "The participant used the prior maintenance history as an initial known-quantity anchor and did not sufficiently adjust his assessment when new ADIRU symptoms appeared during the flight."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Illusion of validity",
      "alternative_labels": ["overconfidence effect", "overconfidence bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to experience high confidence in a judgment based on a consistent but statistically insufficient or unrepresentative sample of evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Climb-phase interpretation of brief ADIRU flicker",
      "decision_point_description": "Whether to interrupt the climb and run the full non-normal procedure for a brief ADIRU disagree indication.",
      "affected_reasoning_operation": "Pattern recognition and confidence calibration",
      "bias_specific_mechanism": "Three brief, consistent-looking occurrences were treated as a reliable pattern, inflating subjective confidence beyond what the small, intermittent sample could diagnostically support.",
      "manifestation_in_interview": "The participant reported feeling he had 'basically already seen this movie' from two ground events and one air event, and said he was 'pretty confident' in that read at the time.",
      "effect_on_reasoning_or_decision": "He did not interrupt the climb or run the full non-normal procedure, treating the brief flicker as a known self-resolving pattern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.",
          "evidence_explanation": "This quote explicitly contrasts the high subjective confidence at the time with the statistically weak sample size, demonstrating the illusion of validity mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Pretty confident, honestly.",
          "evidence_explanation": "This statement indicates the participant's subjective confidence was high despite the limited and intermittent evidence base."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that three brief occurrences were not enough to know what an intermittent wiring fault would do next, but this was retrospective awareness rather than an in-the-moment correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the illusion-of-validity label was not available; this label derives from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Halo effect",
      "alternative_labels": ["halo bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a general positive impression of a person to influence evaluations of that person's specific attributes, behaviors, or performance.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Grading the captain's cruise-phase handling of the airspeed/altitude disagreement",
      "decision_point_description": "Whether to grade the captain's non-normal handling as satisfactory despite not verifying the QRH procedure item-by-item.",
      "affected_reasoning_operation": "Performance evaluation",
      "bias_specific_mechanism": "The participant's global positive impression of the captain—large amount of time on type, calm demeanor, and track record—spilled over into the evaluation of a specific procedural lapse, leading to leniency and reduced verification.",
      "manifestation_in_interview": "The participant said he weighted the captain's extensive type experience and real-time standby cross-check more heavily than a step-by-step QRH sequence check, and said he would have graded a first-year captain less generously for identical behavior.",
      "effect_on_reasoning_or_decision": "The captain was graded satisfactory without item-by-item QRH verification, and the participant applied a different standard based on the captain's seniority and experience.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order.",
          "evidence_explanation": "This quote shows the halo mechanism: a general favorable impression of the captain's experience and calmness influenced the specific evaluation of his non-normal procedure handling."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.",
          "evidence_explanation": "This quote demonstrates the differential evaluation standard based on the captain's overall record, rather than solely on the observed handling."
        }
      ],
      "correction_or_counterevidence": "The captain did perform a real-time standby instrument cross-check and communicated calmly with the first officer, so not all aspects of the satisfactory grade were unsupported. However, the participant also stated he did not verify each QRH item had been handled in order.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the halo-effect label was not available; this label derives from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Bias blind spot",
      "alternative_labels": ["bias blindness"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize cognitive biases in others while failing to recognize their influence on one's own judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to colleague feedback after the check ride",
      "decision_point_description": "Whether to accept the colleague's suggestion that the participant's judgments might have been shaped by the crew's clean history.",
      "affected_reasoning_operation": "Self-assessment of susceptibility to bias",
      "bias_specific_mechanism": "The participant exempted himself from bias risk by citing his structured process and track record, while attributing that risk to less experienced check airmen.",
      "manifestation_in_interview": "When confronted with the possibility that his decisions were shaped by the crew's clean history, the participant denied it applied to him and said it was more of a risk for someone earlier in their check-airman career.",
      "effect_on_reasoning_or_decision": "The participant dismissed the colleague's feedback and did not reconsider whether his prior judgments had been affected by history, experience, or anchor-like reasoning.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.",
          "evidence_explanation": "This quote shows the classic bias blind spot pattern: recognizing bias as a risk for less experienced others while denying personal susceptibility."
        }
      ],
      "correction_or_counterevidence": "Having a structured process and long record may genuinely reduce certain errors, so the rejection is not entirely baseless. However, the explicit distribution of bias risk to less experienced examiners while exempting himself is the distinctive bias mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the bias-blind-spot label was not available; this label derives from established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single, retrospective self-report interview without independent flight data or check-ride records.",
    "Retrieved corpus support was available for the anchoring-and-adjustment occurrence; the other labels rely on established cognitive-science knowledge without corpus support.",
    "The participant's retrospective framing may influence the inferred mechanisms, particularly for in-the-moment confidence and interpretation decisions."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. As we discussed, this is a confidential debrief for training research purposes — I'll ask about a specific check ride, and I'd like you to walk me through what happened as concretely as you can. Nothing here goes into your personnel file. Sound okay? Participant: Sure, happy to talk through it. It was a Line Check, OPC cycle, on one of our senior widebody captains — guy's got probably twenty-two thousand hours, most of it on type. I was in the jump seat as the TRE. Interviewer: What was the flight supposed to accomplish, and what was your role exactly? Participant: Standard revenue flight, but I'm there to evaluate his technical handling and CRM for his recurrent check. First officer was PM. My job is to observe, grade, and intervene only if safety requires it. Interviewer: Take me through what actually happened, from the start. Participant: Before we even got to the airplane, I saw the tech log had two previous write-ups — ADIRU 2 miscompare, both times it cleared on its own, maintenance found nothing conclusive, and it came back MEL'd as okay to fly. So going in, I already had that context. We did the walk-around, briefed, nothing unusual. Departure was normal. Climbing out through about FL250, we got a brief ADIRU disagree indication on the EICAS — flickered for maybe ten seconds and went away. No checklist triggered automatically, so it wasn't like the system was demanding we do anything. Then in cruise, it came back, but this time it showed up as a disagreement between the captain's and first officer's airspeed and altitude tapes. That's more attention-getting because now you've got two primary displays disagreeing with each other, not just an internal comparator flag. The captain worked through it — cross-checked against the standby instruments, talked the FO through what he was seeing, and the indications came back together within a couple minutes. Rest of the flight was uneventful. Normal approach, normal landing. Interviewer: And afterward? Participant: I wrote up my report. Graded the captain's overall performance. A colleague of mine, another TRE, looked at the write-up informally and asked whether I'd been a little quick to wave things off given the fault's history. I pushed back on that. Then a few days later maintenance found an intermittent connector fault in the ADIRU wiring bay — that's likely what caused all three episodes. So there was an actual physical problem the whole time, it just wasn't consistent enough to nail down on the ground. Interviewer: Let's go back to that pre-departure moment. What went through your mind when you saw the tech log entries? Participant: Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further. Interviewer: Did you consider asking for another maintenance look before departure? Participant: Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going. Interviewer: What would have had to be different on paper for you to hold the flight? Participant: If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than 'checked, no fault found,' that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved. Interviewer: Move to the climb, when the flag flickered again. Walk me through that moment specifically. Participant: We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports. Interviewer: What alternative did you weigh at that point? Participant: Leveling off and running the full non-normal procedure, get maintenance control on the radio. I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting. Interviewer: How confident were you in that read at the time? Participant: Pretty confident, honestly. I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample. Interviewer: Let's talk about cruise, when the airspeed and altitude displays actually disagreed between the two pilots' instruments. What did you observe the captain do, and how did you evaluate it? Participant: He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either. Interviewer: How did you grade that? Participant: I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order. Interviewer: If a first-year captain had handled it the identical way, would you have graded it the same? Participant: Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work. Interviewer: Last one — the conversation with your colleague afterward. He suggested your calls that day might have been shaped by the crew's clean history. How did you respond to that? Participant: I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built. Interviewer: Is there anything that would change your mind about that day, looking back? Participant: If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made. Interviewer: Last question. If you ran this exact flight again with exactly the same information you had at the time, what would you do differently? Participant: Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.

_ranker=rrf · t=0.04 · k=25 → 25 in context · 8192 ctx · emb 1.95s · gen 137.53s · total 142.1s_

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

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first analysis of a single CTA interview transcript. Only biases affirmatively evidenced by the participant's reported reasoning and evaluation are classified."
  },
  "identified_bias_summary": [
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
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["positive test strategy", "confirmatory reasoning"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or expectations, while giving disproportionately little weight to disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of recurrent ADIRU write-ups and in-flight ADIRU disagree events as a benign self-clearing pattern",
      "decision_point_description": "Pre-departure decision not to request further maintenance and climb decision not to level off or run the full non-normal procedure after the brief ADIRU disagree",
      "affected_reasoning_operation": "Inference and causal interpretation of ambiguous fault evidence",
      "bias_specific_mechanism": "The participant used the prior maintenance history as a template, treated each new ambiguous occurrence as confirmation of that template, and did not actively seek or weight evidence that could disconfirm the benign self-clearing interpretation, such as recurrence itself or maintenance's inability to find a conclusive fault.",
      "manifestation_in_interview": "He described the two prior write-ups as evidence that the fault was known and self-resolving; during the climb he immediately classified the flicker as the same thing from the tech log; he later admitted that three brief occurrences were treated as a clear pattern at the time.",
      "effect_on_reasoning_or_decision": "He did not hold the flight or request another maintenance look before departure; he told the captain to keep the climb going instead of running the full non-normal procedure; this framing likely carried into his later favorable grading of the captain's handling.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further.",
          "evidence_explanation": "Shows he adopted the prior benign pattern as a settled interpretation and discounted the need for further investigation, demonstrating confirmation of the existing maintenance disposition."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.",
          "evidence_explanation": "He interpreted the new in-flight fault as confirming the prior self-clearing pattern rather than as potentially disconfirming evidence that the fault persisted and could worsen."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.",
          "evidence_explanation": "Explicitly distinguishes his limited sample from the felt certainty of a pattern, showing confirmatory pattern recognition rather than falsification-based reasoning."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged in hindsight that three brief occurrences are not enough to predict an intermittent wiring fault; however, he did not correct the earlier in-flight decisions at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus included confirmation bias in aviation accident analysis.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "the crew's confirmation bias was supported by being able to visually identify cues that supported their mental model... led them to ignore other evidence... that would contradict the aircraft's position.",
          "mechanism_supported_by_source": "Confirmation bias involves using cues consistent with a pre-existing mental model while ignoring contradicting evidence.",
          "relevance_to_this_occurrence": "The participant likewise used cues consistent with the tech-log pattern of a self-clearing fault to support a benign interpretation and did not pursue evidence that would contradict that interpretation."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "halo effect",
      "alternative_labels": ["experience bias", "status-based evaluation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a positive global impression of a person, such as their experience or seniority, to influence judgments about specific behaviors or performance, producing overly favorable evaluations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Grading the captain's response to the cruise airspeed/altitude disagreement",
      "decision_point_description": "The participant decided to grade the captain's handling as satisfactory despite not verifying each QRH item in order and despite identifying a procedural deviation.",
      "affected_reasoning_operation": "Performance evaluation and grading judgment",
      "bias_specific_mechanism": "The participant generalized from the captain's high experience and calm demeanor to a favorable overall evaluation, weighting the captain's seniority and real-time cross-check more heavily than the procedural standard, and explicitly indicating a junior captain would have been assessed more strictly.",
      "manifestation_in_interview": "He said he weighted the captain's extensive time on type and real-time standby cross-check more heavily than a step-by-step QRH review, did not verify each item, and admitted he would not grade a first-year captain the same way.",
      "effect_on_reasoning_or_decision": "The captain received a satisfactory grade despite not following the QRH procedure in order, because experience and track record were allowed to compensate for procedural deviation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order.",
          "evidence_explanation": "This shows the evaluation was shaped by a global high-experience impression and that procedural verification was de-emphasized."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.",
          "evidence_explanation": "Directly demonstrates the halo mechanism: identical behavior would be graded differently based on the captain's seniority and track record."
        }
      ],
      "correction_or_counterevidence": "No correction is present; the participant explicitly endorsed the differential standard when prompted.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus did not provide a specific passage on halo effect; this label is assigned from established cognitive-science knowledge, not from retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bias blind spot",
      "alternative_labels": ["self-assessment bias", "asymmetric bias attribution"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize the influence of biases in others while failing to see their influence on one's own judgments and decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to colleague's suggestion that the participant's calls were shaped by the crew's clean history",
      "decision_point_description": "The participant rejected the colleague's feedback and attributed bias susceptibility to less experienced check-airmen while claiming himself to be insulated by a structured process and clean record.",
      "affected_reasoning_operation": "Self-assessment and evaluation of one's own judgment processes",
      "bias_specific_mechanism": "The participant applied a double standard: he treated bias as a plausible risk for less experienced check-airmen but not for himself, using his structured process and history of uneventful check rides as evidence of personal immunity rather than examining the specific judgments in question.",
      "manifestation_in_interview": "When a colleague suggested his calls that day might have been shaped by the crew's clean history, the participant said it did not apply to him and described bias as more of a risk for someone earlier in their check-airman career.",
      "effect_on_reasoning_or_decision": "He dismissed the feedback rather than examining it, maintaining confidence in his prior decisions and his own evaluative process.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.",
          "evidence_explanation": "This quote explicitly shows asymmetric attribution of bias susceptibility to less experienced others and claims personal immunity based on prior success."
        }
      ],
      "correction_or_counterevidence": "No correction is present; the participant maintained this stance at the end, though he did acknowledge he might log the climb flicker more formally.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus did not provide a specific passage on bias blind spot; this label is assigned from established cognitive-science knowledge, not from retrieved evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "outcome bias",
      "alternative_labels": ["result-based evaluation"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-flight reflection after learning the connector fault was later found by maintenance",
      "supporting_interview_quote": "If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made.",
      "plausible_mechanism": "The participant may be evaluating the quality or implications of his earlier decisions partly by the eventual outcome, treating the benign outcome as reducing the diagnostic value of the later maintenance finding.",
      "why_not_identified": "The statement is somewhat guarded; he says the outcome does not prove anything either way, so it is less clear that he is affirmatively using the outcome to judge decision quality. It therefore remains below the threshold for identification."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus coverage was limited and did not address all identified labels; for halo effect and bias blind spot, labels rest on general knowledge with disclosure.",
    "Single-interview transcript; causal inference is limited to the participant's self-report.",
    "No independent behavioral observation or flight data were available to verify the participant's descriptions."
  ]
}

