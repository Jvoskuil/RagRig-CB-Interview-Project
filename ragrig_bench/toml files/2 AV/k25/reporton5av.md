# RAG Benchmark — 2026-09-09

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a maintenance decision-making review, and that we can reference the tail number and event details generically without naming crew. Participant: That's fine, go ahead. Interviewer: Great. Can you tell me your role and how you came into this event? Participant: I'm the Director of Maintenance at our base station. I oversee line maintenance sign-offs, RTS certifications, and I'm the one who ultimately owns whether an aircraft goes back into the schedule. This one landed on my desk because it kept coming back. Interviewer: Walk me through what the issue looked like when you first became aware of it. Participant: We had a Hydraulic System B caution light show up on one of our E175s—momentary, cleared itself, crew wrote it up. Maintenance ran the BITE test, came back clean, no fault found. Classic CND. It happened three times over about two weeks. Each time, no fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL. The aircraft kept flying its line. Interviewer: What did you make of that pattern at the time? Participant: Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times. We had the holiday peak coming up and needed the airframe in rotation, so grounding it for an open-ended isolation hunt on a CND item felt like overkill at that point. Interviewer: Did the increasing duration register as significant to you? Participant: I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it. Interviewer: What happened next? Participant: Next flight day, it came back a fourth time, and this one ran about twelve seconds—longer than anything before—and the crew also noted a brief speed brake anomaly on the same leg. That's when my senior hydraulics engineer came to me and wanted to pull the aircraft and run the full fault isolation procedure out of the FIM. Interviewer: What did you decide at that point, and how did you get there? Participant: While we were talking about it, our OEM field rep happened to be at the hangar working a different tail. I flagged him down and asked what he thought. He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it. Interviewer: How did your engineer take that? Participant: He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week. Interviewer: What information did you weigh most heavily there, and what didn't you dig into? Participant: Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal. We reset the BITE and flew it two cycles without a recurrence. Interviewer: What came after that? Participant: A few days later, during an unrelated task, one of the techs was near the hydraulic pump and noticed some residue around the seal. Small amount, hadn't been documented before. That was new—nothing like that had shown up in any of the earlier CND checks. Interviewer: What did that change for you? Participant: It told us there might be an actual mechanical source rather than just a sensor quirk. At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job. Interviewer: Did the amount of work already done factor into that choice? Participant: I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over. Interviewer: After the seal replacement, what did you see? Participant: Leak check passed on the ground, static test showed no residue. Clean. Interviewer: What happened at the final sign-off? Participant: We needed the aircraft that afternoon for the holiday schedule, and we didn't have a test-flight crew available same-day. Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved. Interviewer: Given the aircraft's history—three CND events, the fourth longer one with the speed brake note, and the fact that the seal residue never really explained why the caution happened in flight in the first place—how sure were you that this was actually fixed? Participant: Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that. Interviewer: If you'd had a test-flight crew available that day, would that have changed your certainty? Participant: It would've been a nice extra data point, but I don't think it would've changed my decision to release it. Interviewer: Looking back across the whole event, is there a point where, with the same information you had then, you'd make a different call? Participant: Maybe the fourth event—the twelve-second one with the speed brake anomaly. If I'd leaned more toward my engineer's read there instead of the OEM rep's, we might have caught the seal issue earlier instead of a few days later. Interviewer: If the OEM rep hadn't been on-site that day, what do you think you'd have done instead? Participant: Probably would've let my engineer run the full isolation. Having an outside read available in the moment made it easy to go a different direction. Interviewer: Last one—if the seal residue had turned up before you'd started the component swaps, would the escalation decision have gone differently? Participant: Probably, yeah. Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.

_ranker=rrf · t=0.04 · k=25 → 25 in context · 8192 ctx · emb 1.87s · gen 224.81s · total 229.2s_

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

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the participant's maintenance decision-making narrative for affirmative cognitive bias mechanisms using retrieved corpus definitions. Candidate patterns that were plausible but insufficiently evidenced are listed separately."
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
      "confidence": "moderate",
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "Anchoring heuristic",
        "Insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "People make estimates based on an initial value and adjust insufficiently from that anchor when new information arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation of intermittent hydraulic caution light pattern",
      "decision_point_description": "Whether to ground the aircraft or pursue an open-ended fault isolation hunt after repeated momentary Hydraulic System B caution messages.",
      "affected_reasoning_operation": "Trend interpretation and probabilistic updating of failure risk",
      "bias_specific_mechanism": "The initial 'nuisance signal' diagnosis served as an anchor; as event durations increased from two to three to five seconds, the participant under-adjusted from that initial assessment and rationalized the change as not serious.",
      "manifestation_in_interview": "The participant interpreted three short CND events as sensor noise and explicitly dismissed the lengthening durations as not meaningful in absolute terms.",
      "effect_on_reasoning_or_decision": "The under-adjustment delayed escalation and set a low-suspicion baseline, leading the participant to continue flying the aircraft rather than initiate fuller fault isolation earlier.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times.",
          "evidence_explanation": "This establishes the initial 'nuisance signal' estimate that functioned as the anchor for later interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it.",
          "evidence_explanation": "This demonstrates insufficient adjustment from the initial anchor despite trend-relevant information that event durations were increasing."
        }
      ],
      "correction_or_counterevidence": "Counterevidence at the time included increasing event duration and a recurring hydraulic caution message. The participant later encountered a fourth, longer event with a speed brake anomaly and eventually seal residue indicating a mechanical source, suggesting the initial low-suspicion interpretation was too stable.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus provides the canonical anchoring-and-adjustment mechanism: estimates are shaped by initial values and subsequent adjustment is typically insufficient.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, “adjustments are typically insufficient.” [16]",
          "mechanism_supported_by_source": "Initial values anchor estimates, and later adjustment from those anchors is typically insufficient.",
          "relevance_to_this_occurrence": "The participant's initial nuisance-signal assessment anchored his reading of the increasing event durations, and he under-adjusted rather than revising the risk estimate materially."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmation heuristic",
        "Myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth event decision after speed brake anomaly and OEM consult",
      "decision_point_description": "Whether to follow the senior engineer's recommendation for full FIM fault isolation or accept the OEM representative's reset hypothesis and continue flying.",
      "affected_reasoning_operation": "Evidence weighting and information search during diagnostic decision-making",
      "bias_specific_mechanism": "The participant selectively weighted confirmatory evidence from an OEM field representative and a remembered in-house case that matched his existing 'no serious mechanical fault' view, while not investigating whether the old case actually matched and discounting the engineer's contradictory speed-brake concern.",
      "manifestation_in_interview": "When the OEM representative and an in-house memory supported a software/BITE quirk explanation, the participant felt 'we already had the answer' and halted the formal fault isolation despite the engineer's objection.",
      "effect_on_reasoning_or_decision": "The participant overrode the senior engineer's formal fault-isolation recommendation and returned the aircraft to service after a reset and two cycles without recurrence, rather than pursuing a more thorough mechanical investigation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.",
          "evidence_explanation": "This shows the participant accepting confirmatory evidence and ending the search for a mechanical explanation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
          "evidence_explanation": "This demonstrates selective use of confirmatory prior cases and a failure to examine disconfirming mismatch details."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
          "evidence_explanation": "This shows that a conflicting professional judgment was available but was deprioritized in favor of the explanation consistent with the participant's prior view."
        }
      ],
      "correction_or_counterevidence": "The senior engineer cited the speed brake anomaly as a reason to run the full isolation. Later seal residue revealed a mechanical source, and the participant retrospectively acknowledged that leaning toward the engineer's read might have caught the issue earlier.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved aviation safety corpus provides an operational example of confirmation bias: crew ignored conflicting instruments when prior visual cues supported their mental model.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "Similarly for flight Comair 5191 (2006) which took off from the incorrect runway in darkness and VMC conditions, the investigation found that the visual cues available to the crew induced a state of confirmation bias which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft’s position.",
          "mechanism_supported_by_source": "Confirmation bias causes people to ignore evidence that contradicts an emerging mental model or expected interpretation.",
          "relevance_to_this_occurrence": "The participant ignored contradictory evidence from the speed brake anomaly and the engineer's concern while favoring confirmatory OEM and in-house memories."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Sunk cost fallacy",
        "Escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an original plan or course of action despite evidence or cues that suggest changing course.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-residue repair scope decision",
      "decision_point_description": "Whether to continue the incremental seal replacement plan or escalate to full pump replacement after discovering hydraulic pump residue.",
      "affected_reasoning_operation": "Escalation of commitment and repair resource allocation",
      "bias_specific_mechanism": "Sunk hours and progress on the existing troubleshooting path increased commitment to continuing that path, making escalation to a larger pump replacement appear less attractive than the narrower seal fix.",
      "manifestation_in_interview": "After discovering residue that suggested a mechanical source, the participant decided to replace only the seal and finish the existing plan, partly because fourteen hours had already been sunk into troubleshooting and component swaps.",
      "effect_on_reasoning_or_decision": "The participant chose the narrower seal repair over full pump replacement, preserving the current plan rather than escalating to a more complete mechanical fix.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job.",
          "evidence_explanation": "This shows the participant explicitly reasoning that accumulated time and progress on the original plan justified continuing rather than changing course."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over.",
          "evidence_explanation": "This demonstrates sunk-cost logic affecting the repair escalation decision."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that if the seal residue had been found before the component swaps, full pump replacement would likely have appeared to be the right call, indicating that the invested effort influenced the post-residue choice.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus supports the 'plan continuation bias' label in aviation decision-making; the excerpt does not include a full formal definition, so the sunk-cost/escalation mechanism is characterized using general cognitive-science knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "This continuation bias, in that it appears to occur in frequently during runway excursions on landing, after longer duties and at the latter stages of flight.",
          "mechanism_supported_by_source": "Aviation accident data associate plan continuation bias with continuing a course of action during later stages and critical events.",
          "relevance_to_this_occurrence": "The participant continued the existing repair plan after new residue evidence, consistent with plan continuation rather than switching to a larger maintenance intervention."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Availability heuristic",
      "alternative_labels": [
        "Ease of recall"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Fourth event decision to accept OEM representative's reset hypothesis",
      "supporting_interview_quote": "Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.",
      "plausible_mechanism": "The easily recalled OEM-reported pattern and the in-house case may have inflated the judged likelihood of a software/BITE quirk and truncated search for disconfirming details.",
      "why_not_identified": "The evidence more clearly supports confirmation bias because the participant selectively favored a hypothesis-consistent memory and failed to check mismatches; independent availability-driven distortion is not separately established."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Overestimation of certainty",
        "Illusion of validity"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final RTS certification after seal replacement",
      "supporting_interview_quote": "Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that.",
      "plausible_mechanism": "Stated high confidence in the repair despite an unresolved gap between ground test conditions and the in-flight failure condition may reflect overestimation of diagnostic certainty.",
      "why_not_identified": "The transcript lacks sufficient evidence of a distinct distorted probability calibration; the decision could reflect a standard maintenance proof norm combined with operational and resource constraints."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus excerpts are fragmented; definitions for confirmation bias and anchoring are present, but plan continuation bias support is primarily label-level rather than a formal mechanism definition.",
    "The analysis is based on a single interview narrative and does not include outcome data after the final RTS certification.",
    "Some mechanisms, such as confirmation bias, availability, and anchoring, overlap in diagnostic reasoning; boundary decisions were made conservatively.",
    "The analysis is blind to experimental conditions and does not infer design intent or benchmark expectations."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a maintenance decision-making review, and that we can reference the tail number and event details generically without naming crew. Participant: That's fine, go ahead. Interviewer: Great. Can you tell me your role and how you came into this event? Participant: I'm the Director of Maintenance at our base station. I oversee line maintenance sign-offs, RTS certifications, and I'm the one who ultimately owns whether an aircraft goes back into the schedule. This one landed on my desk because it kept coming back. Interviewer: Walk me through what the issue looked like when you first became aware of it. Participant: We had a Hydraulic System B caution light show up on one of our E175s—momentary, cleared itself, crew wrote it up. Maintenance ran the BITE test, came back clean, no fault found. Classic CND. It happened three times over about two weeks. Each time, no fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL. The aircraft kept flying its line. Interviewer: What did you make of that pattern at the time? Participant: Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times. We had the holiday peak coming up and needed the airframe in rotation, so grounding it for an open-ended isolation hunt on a CND item felt like overkill at that point. Interviewer: Did the increasing duration register as significant to you? Participant: I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it. Interviewer: What happened next? Participant: Next flight day, it came back a fourth time, and this one ran about twelve seconds—longer than anything before—and the crew also noted a brief speed brake anomaly on the same leg. That's when my senior hydraulics engineer came to me and wanted to pull the aircraft and run the full fault isolation procedure out of the FIM. Interviewer: What did you decide at that point, and how did you get there? Participant: While we were talking about it, our OEM field rep happened to be at the hangar working a different tail. I flagged him down and asked what he thought. He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it. Interviewer: How did your engineer take that? Participant: He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week. Interviewer: What information did you weigh most heavily there, and what didn't you dig into? Participant: Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal. We reset the BITE and flew it two cycles without a recurrence. Interviewer: What came after that? Participant: A few days later, during an unrelated task, one of the techs was near the hydraulic pump and noticed some residue around the seal. Small amount, hadn't been documented before. That was new—nothing like that had shown up in any of the earlier CND checks. Interviewer: What did that change for you? Participant: It told us there might be an actual mechanical source rather than just a sensor quirk. At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job. Interviewer: Did the amount of work already done factor into that choice? Participant: I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over. Interviewer: After the seal replacement, what did you see? Participant: Leak check passed on the ground, static test showed no residue. Clean. Interviewer: What happened at the final sign-off? Participant: We needed the aircraft that afternoon for the holiday schedule, and we didn't have a test-flight crew available same-day. Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved. Interviewer: Given the aircraft's history—three CND events, the fourth longer one with the speed brake note, and the fact that the seal residue never really explained why the caution happened in flight in the first place—how sure were you that this was actually fixed? Participant: Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that. Interviewer: If you'd had a test-flight crew available that day, would that have changed your certainty? Participant: It would've been a nice extra data point, but I don't think it would've changed my decision to release it. Interviewer: Looking back across the whole event, is there a point where, with the same information you had then, you'd make a different call? Participant: Maybe the fourth event—the twelve-second one with the speed brake anomaly. If I'd leaned more toward my engineer's read there instead of the OEM rep's, we might have caught the seal issue earlier instead of a few days later. Interviewer: If the OEM rep hadn't been on-site that day, what do you think you'd have done instead? Participant: Probably would've let my engineer run the full isolation. Having an outside read available in the moment made it easy to go a different direction. Interviewer: Last one—if the seal residue had turned up before you'd started the component swaps, would the escalation decision have gone differently? Participant: Probably, yeah. Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.

_ranker=rrf · t=0.04 · k=25 → 25 in context · 8192 ctx · emb 2.05s · gen 199.10s · total 203.5s_

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

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the Director of Maintenance's retrospective account for reasoning processes in maintenance decision-making. Identifications are based on affirmative evidence of bias-specific mechanisms in the participant's statements."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmation trap",
        "hypothesis-biased information search"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, favor, and recall information in ways that confirm one's existing belief or hypothesis while giving disproportionately less weight to contradicting evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Choosing between the OEM/reset recommendation and full fault isolation after the fourth caution event",
      "decision_point_description": "Decision to hold off on full FIM fault isolation, perform a reset, and continue flying after the senior hydraulics engineer requested formal fault isolation.",
      "affected_reasoning_operation": "Information search, evidence weighting, and fault diagnosis",
      "bias_specific_mechanism": "The participant had formed the view that the intermittent cautions were probably a nuisance/sensor quirk. He then privileged information consistent with that hypothesis, including the OEM rep's software/BITE quirk account and an undifferentiated remembered in-house case, while failing to systematically evaluate contradicting evidence such as the longer 12-second event and the speed brake anomaly.",
      "manifestation_in_interview": "The participant treated the OEM rep's matching pattern and the in-house memory as sufficient to settle the diagnosis, declined the full isolation, and acknowledged not checking whether the old case actually matched this aircraft.",
      "effect_on_reasoning_or_decision": "It led him to categorize the event as a likely known/benign quirk, withhold full fault isolation, reset the system, and continue flying rather than pursue the formal diagnostic procedure.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.",
          "evidence_explanation": "This shows the participant treating confirmatory information as sufficient to resolve the diagnosis and override the engineer's request for formal isolation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
          "evidence_explanation": "This explicitly demonstrates selective information gathering and reliance on a felt similarity rather than verification of whether the prior case actually supported the current hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
          "evidence_explanation": "This shows contradictory evidence and a dissenting recommendation from the senior engineer being discounted in favor of the confirmatory external account."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that if the OEM rep had not been present he probably would have let the engineer run the full isolation, and that following the engineer's read at the fourth event might have caught the seal issue earlier. However, that retrospective recognition does not negate the confirmatory reasoning at the time. Relying on an OEM field rep was not inherently unreasonable; the bias is evidenced by the participant's failure to check whether the in-house case matched and by discounting the contradictory speed-brake cue.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved aviation cognitive bias material supports the confirmation bias mechanism: operators favor cues consistent with their mental model and ignore contradictory evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The investigation found that the visual cues available to the crew induced a state of confirmation bias which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft's position.",
          "mechanism_supported_by_source": "Confirmation bias can lead operators to ignore evidence that contradicts their current mental model while relying on cues that support it.",
          "relevance_to_this_occurrence": "The participant similarly relied on the OEM rep's and in-house accounts that matched the nuisance/sensor-quirk mental model while discounting the engineer's contradictory concern about the speed brake anomaly and the longer caution duration."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "plan continuation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue a course of action because of previously invested resources such as time, effort, or money, even when current evidence suggests that a different course would be more appropriate.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Escalation decision after discovery of hydraulic pump seal residue",
      "decision_point_description": "Whether to replace only the seal and complete the existing incremental troubleshooting path or to escalate to a full pump replacement after residue was found.",
      "affected_reasoning_operation": "Repair escalation choice and resource allocation",
      "bias_specific_mechanism": "The participant treated previously invested troubleshooting hours as a reason to continue the current repair plan rather than treating those hours as sunk costs irrelevant to the forward-looking decision.",
      "manifestation_in_interview": "After discovering residue that suggested an actual mechanical source, the participant decided to replace only the seal and finish the existing plan partly because the team had already spent fourteen hours troubleshooting and was most of the way through the incremental plan.",
      "effect_on_reasoning_or_decision": "It reduced the likelihood of escalating to a full pump replacement despite new evidence of a possible mechanical source, potentially prolonging exposure to an unresolved defect.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job.",
          "evidence_explanation": "This shows the amount of time already spent and progress on the current plan influencing the choice not to escalate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over.",
          "evidence_explanation": "This is explicit sunk-cost language: the participant treats prior effort as wasted if the plan changes, which is the core mechanism of the sunk cost fallacy."
        }
      ],
      "correction_or_counterevidence": "There were also practical constraints, including lack of a pump part on the shelf, downtime pressure, and the residue being minor. These could support the seal-only decision on non-biased grounds. However, the participant explicitly stated that sunk hours factored into the decision, and later said that if the residue had appeared before the component swaps, full pump replacement would have looked more obviously like the right call.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the specific label 'sunk cost fallacy' was unavailable; this label is applied from general cognitive-science knowledge. The retrieved aviation corpus mentions plan continuation bias but without sufficient mechanism detail to provide primary support for this occurrence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "overconfidence bias",
      "alternative_labels": [
        "overconfidence effect",
        "certitude bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A person's subjective confidence in a judgment or decision is greater than the objective evidence or accuracy warrants.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final RTS sign-off after ground leak check",
      "decision_point_description": "Decision to sign the RTS certification and release the aircraft without a test flight after ground leak and static checks passed.",
      "affected_reasoning_operation": "Confidence judgment and release decision",
      "bias_specific_mechanism": "The participant acknowledged that ground static testing could not reproduce the exact in-flight condition that triggered the caution, yet he treated the passed ground leak check as proof that the repair had worked and expressed high confidence in release.",
      "manifestation_in_interview": "He signed the RTS certification and told the operations desk he was confident the issue was resolved, despite knowing the ground checks did not replicate the in-flight trigger environment.",
      "effect_on_reasoning_or_decision": "It increased readiness to release the aircraft and reduced perceived need for a test flight or further hold despite an acknowledged evidential gap.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved.",
          "evidence_explanation": "This shows high confidence leading directly to release."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that.",
          "evidence_explanation": "The participant explicitly recognizes a limitation in the evidence but maintains high confidence, which is consistent with overconfidence bias."
        }
      ],
      "correction_or_counterevidence": "A passed leak check is standard evidence for a leak-based repair, and operational constraints such as holiday scheduling and lack of a test-flight crew may have made the release decision reasonable. This is a borderline instance, so the overconfidence attribution is low confidence rather than high or moderate.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for overconfidence bias was unavailable; this label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Interpreting the increasing duration of intermittent hydraulic caution events",
      "supporting_interview_quote": "I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it.",
      "plausible_mechanism": "The initial nuisance-signal/sensor-noise diagnosis may have served as an anchor, with the later longer durations being interpreted as insufficient to require a substantial change in assessment.",
      "why_not_identified": "The participant also gave legitimate evidential reasons for not escalating, including no fluid loss and no pressure data. There is no clear statement that an initial value anchored the later interpretation specifically."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": [
        "ease-of-recall heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Use of an in-house memory to support the reset decision",
      "supporting_interview_quote": "One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
      "plausible_mechanism": "The easily recalled past caution-light case may have inflated the judged probability that the current fault was the same benign issue.",
      "why_not_identified": "This overlaps with the identified confirmation bias. The selective reliance on a matching memory was already captured as confirmation bias, and a separable availability effect is not sufficiently established in the transcript."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "authority bias",
      "alternative_labels": [
        "expert authority effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Choosing the OEM representative's reset recommendation over the senior engineer's full isolation recommendation",
      "supporting_interview_quote": "But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
      "plausible_mechanism": "The OEM field rep's expert or authority status may have led the participant to overweight his opinion relative to the senior engineer's on-site contradictory concern.",
      "why_not_identified": "Relying on an OEM representative can be a reasonable use of outside expertise. The transcript does not clearly show that authority status, rather than confirmatory information search, was the driving mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective interview, so the participant's post hoc explanations may differ from in-the-moment reasoning.",
    "Some occurrences have plausible non-biased explanations; low-confidence findings and candidates are marked accordingly.",
    "The retrieved corpus is aviation-focused and OCR quality is imperfect, limiting the precision of some source passages.",
    "Several mechanisms overlap, particularly confirmation bias and availability, and were separated only where the transcript supported distinct reasoning operations."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a maintenance decision-making review, and that we can reference the tail number and event details generically without naming crew. Participant: That's fine, go ahead. Interviewer: Great. Can you tell me your role and how you came into this event? Participant: I'm the Director of Maintenance at our base station. I oversee line maintenance sign-offs, RTS certifications, and I'm the one who ultimately owns whether an aircraft goes back into the schedule. This one landed on my desk because it kept coming back. Interviewer: Walk me through what the issue looked like when you first became aware of it. Participant: We had a Hydraulic System B caution light show up on one of our E175s—momentary, cleared itself, crew wrote it up. Maintenance ran the BITE test, came back clean, no fault found. Classic CND. It happened three times over about two weeks. Each time, no fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL. The aircraft kept flying its line. Interviewer: What did you make of that pattern at the time? Participant: Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times. We had the holiday peak coming up and needed the airframe in rotation, so grounding it for an open-ended isolation hunt on a CND item felt like overkill at that point. Interviewer: Did the increasing duration register as significant to you? Participant: I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it. Interviewer: What happened next? Participant: Next flight day, it came back a fourth time, and this one ran about twelve seconds—longer than anything before—and the crew also noted a brief speed brake anomaly on the same leg. That's when my senior hydraulics engineer came to me and wanted to pull the aircraft and run the full fault isolation procedure out of the FIM. Interviewer: What did you decide at that point, and how did you get there? Participant: While we were talking about it, our OEM field rep happened to be at the hangar working a different tail. I flagged him down and asked what he thought. He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it. Interviewer: How did your engineer take that? Participant: He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week. Interviewer: What information did you weigh most heavily there, and what didn't you dig into? Participant: Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal. We reset the BITE and flew it two cycles without a recurrence. Interviewer: What came after that? Participant: A few days later, during an unrelated task, one of the techs was near the hydraulic pump and noticed some residue around the seal. Small amount, hadn't been documented before. That was new—nothing like that had shown up in any of the earlier CND checks. Interviewer: What did that change for you? Participant: It told us there might be an actual mechanical source rather than just a sensor quirk. At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job. Interviewer: Did the amount of work already done factor into that choice? Participant: I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over. Interviewer: After the seal replacement, what did you see? Participant: Leak check passed on the ground, static test showed no residue. Clean. Interviewer: What happened at the final sign-off? Participant: We needed the aircraft that afternoon for the holiday schedule, and we didn't have a test-flight crew available same-day. Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved. Interviewer: Given the aircraft's history—three CND events, the fourth longer one with the speed brake note, and the fact that the seal residue never really explained why the caution happened in flight in the first place—how sure were you that this was actually fixed? Participant: Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that. Interviewer: If you'd had a test-flight crew available that day, would that have changed your certainty? Participant: It would've been a nice extra data point, but I don't think it would've changed my decision to release it. Interviewer: Looking back across the whole event, is there a point where, with the same information you had then, you'd make a different call? Participant: Maybe the fourth event—the twelve-second one with the speed brake anomaly. If I'd leaned more toward my engineer's read there instead of the OEM rep's, we might have caught the seal issue earlier instead of a few days later. Interviewer: If the OEM rep hadn't been on-site that day, what do you think you'd have done instead? Participant: Probably would've let my engineer run the full isolation. Having an outside read available in the moment made it easy to go a different direction. Interviewer: Last one—if the seal residue had turned up before you'd started the component swaps, would the escalation decision have gone differently? Participant: Probably, yeah. Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.

_ranker=rrf · t=0.04 · k=25 → 25 in context · 8192 ctx · emb 2.11s · gen 293.59s · total 298.4s_

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

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of the Director of Maintenance's narrative for affirmatively evidenced cognitive biases in maintenance decision-making; retrieved corpus passages were used to ground confirmation and plan continuation labels only."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Overconfidence effect",
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
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Myside bias",
        "Selective information search"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and rely on information in ways that confirm an existing hypothesis or desired conclusion while underweighting or failing to check disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth hydraulic caution assessment and reset-vs-isolation decision",
      "decision_point_description": "After the fourth hydraulic caution, now longer and accompanied by a speed brake anomaly, the participant decided to reset the BITE and return the aircraft to service rather than run the full fault isolation procedure requested by the senior hydraulics engineer.",
      "affected_reasoning_operation": "Evaluation of diagnostic evidence and information search for fault cause",
      "bias_specific_mechanism": "The participant formed an early benign 'nuisance signal' hypothesis and then preferentially weighted OEM and in-house recollections that supported that hypothesis while not verifying whether the prior case actually matched and while discounting the speed-brake anomaly and engineer's disconfirming input.",
      "manifestation_in_interview": "The participant described the repeated cautions as probably a nuisance signal, then when the engineer wanted full isolation the participant solicited the OEM rep, received a benign reset explanation, and combined it with an unmatched in-house memory to decide 'we already had the answer.'",
      "effect_on_reasoning_or_decision": "The confirmatory evaluation led to a reset-and-continue decision instead of full fault isolation, delaying discovery of the mechanical seal leak and allowing the aircraft to continue flying.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times.",
          "evidence_explanation": "Shows the pre-existing benign hypothesis that later biased the search for and interpretation of diagnostic information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.",
          "evidence_explanation": "Shows that confirmatory OEM and memory information was treated as sufficient to set aside the more rigorous disconfirming procedure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
          "evidence_explanation": "Demonstrates failure to seek disconfirming information about a potentially misleading analogy, a hallmark of confirmation-biased reasoning."
        }
      ],
      "correction_or_counterevidence": "Counterevidence was present: the senior hydraulics engineer objected and believed the speed brake anomaly changed the picture, and the participant acknowledged he did not verify the in-house case match. This input did not alter the reset decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved aviation report describes confirmation bias leading crews to ignore evidence that contradicts an initial mental model.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "Similarly for flight Comair 5191 (2006) which took off from the incorrect runway in darkness and VMC conditions, the investigation found that the visual cues available to the crew induced a state of confirmation bias which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft’s position.",
          "mechanism_supported_by_source": "Confirmation bias can lead decision-makers to ignore disconfirming evidence and act on information supporting an existing interpretation.",
          "relevance_to_this_occurrence": "The participant acted on OEM and in-house information supporting a benign interpretation while ignoring contradictory evidence such as the speed brake anomaly and the engineer's request for full isolation, paralleling the source mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Sunk cost fallacy",
        "Escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an established course of action even after new evidence or cues indicate that changing course may be more appropriate.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-residue repair escalation decision",
      "decision_point_description": "After a technician found hydraulic pump seal residue, the participant decided to replace only the seal and finish the existing incremental troubleshooting path rather than escalate to full pump replacement.",
      "affected_reasoning_operation": "Choice of repair escalation strategy after new mechanical evidence",
      "bias_specific_mechanism": "The participant weighted sunk time and effort on the existing troubleshooting path heavily and continued that path despite new evidence of a possible mechanical source that might warrant full pump replacement; this is an escalation of commitment grounded in sunk cost.",
      "manifestation_in_interview": "The participant noted fourteen hours already spent, component swaps already performed, and said the seal fix would close it out 'without starting over' rather than opening a bigger job.",
      "effect_on_reasoning_or_decision": "The decision maintained the incremental plan rather than escalating to full pump replacement, potentially addressing only a symptom or partial source while preserving prior sunk effort.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan.",
          "evidence_explanation": "Shows that accumulated effort on the original path became a salient factor in the repair decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job.",
          "evidence_explanation": "Directly demonstrates continuing the established plan after new residue evidence rather than shifting to a more comprehensive repair."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing.",
          "evidence_explanation": "Shows sunk-cost reasoning: avoiding abandonment of prior work rather than choosing the action best supported by the new evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.",
          "evidence_explanation": "The counterfactual acknowledges that the prior investment altered the escalation decision, strengthening the plan-continuation interpretation."
        }
      ],
      "correction_or_counterevidence": "The participant later explicitly recognized in a counterfactual that without the already-spent hours, full pump replacement would have been the more obvious choice, which is self-corroborating rather than a correction.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved aviation documents mention plan continuation bias as a repeated pattern in accident and incident sequences.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "plan continuation bias, in that it appears to occur in frequently during runway excursions on  landing, after longer duties and at the latter stages of flight.",
          "mechanism_supported_by_source": "Plan continuation bias is documented in aviation as continuing with an existing plan rather than discontinuing or changing course.",
          "relevance_to_this_occurrence": "The participant continued the established incremental repair plan despite new residue evidence, consistent with the documented plan-continuation pattern."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Overconfidence bias",
        "Overprecision"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A systematic tendency to have greater subjective confidence in a judgment or decision than the available evidence or objective accuracy warrants.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final RTS certification following seal replacement",
      "decision_point_description": "After the seal replacement passed a ground leak check and static test, the participant signed the return-to-service certification and told ops he was confident the fault was resolved.",
      "affected_reasoning_operation": "Airworthiness evaluation and return-to-service certification",
      "bias_specific_mechanism": "The participant treated a passed ground leak check as sufficient proof of in-flight fault resolution even while acknowledging that static testing could not reproduce the in-flight caution or explain the original intermittent hydraulic caution sequence, and stated a test flight would not have changed his decision.",
      "manifestation_in_interview": "The participant was 'pretty sure' the repaired aircraft was fixed, signed the RTS, and said having a test-flight crew available would not have changed his certainty or decision.",
      "effect_on_reasoning_or_decision": "The aircraft was certified as resolved without a test flight or reproduction of the original in-flight failure condition, reflecting greater confidence in the ground-test evidence than the diagnostic limitations supported.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved.",
          "evidence_explanation": "Shows the high-confidence certification decision based on limited ground testing."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that.",
          "evidence_explanation": "Explicitly acknowledges the inferential gap between the ground test and the in-flight failure while still treating the passed check as proof."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It would've been a nice extra data point, but I don't think it would've changed my decision to release it.",
          "evidence_explanation": "Indicates high subjective confidence that additional in-flight validation would not alter the decision, consistent with overconfidence."
        }
      ],
      "correction_or_counterevidence": "Operational constraints were present: holiday schedule and no same-day test-flight crew. These contextual factors may partially explain the RTS timing, but the participant's explicitly stated certainty and statement that a test flight would not change the decision support a distinct overconfidence mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported overconfidence effect; the label rests on general cognitive-science knowledge and the explicit transcript evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Representativeness heuristic",
      "alternative_labels": [
        "Availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Fourth-event reset-vs-isolation decision",
      "supporting_interview_quote": "One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back.",
      "plausible_mechanism": "The participant judged the current fault as the same as a recalled prior case based on superficial similarity without checking flight hours or component batch.",
      "why_not_identified": "The transcript evidence does not cleanly separate this similarity/recall influence from confirmation bias; it may be a component of confirmatory search rather than an independent representativeness effect, and no retrieved corpus passage specifically supports it."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieval support for overconfidence effect was unavailable; that label rests on general cognitive-science knowledge.",
    "The transcript contains operational constraints such as holiday schedule, no same-day test-flight crew, and unavailable pump parts that are not classified as biases but contribute context.",
    "Early diagnostic comments about CND events could reflect ordinary uncertainty, so they were not classified separately from the more clearly evidenced confirmation-bias episode."
  ]
}

