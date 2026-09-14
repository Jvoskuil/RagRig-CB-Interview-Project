# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for an internal reliability-process review, not a safety investigation into you personally — we're trying to understand how these calls actually get made in practice. That okay with you? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me your role and how this particular case landed on your desk? Participant: Sure. I'm a reliability engineer in Maintenance Control. Part of my job is watching for repetitive write-ups across the fleet and deciding when something crosses from 'normal noise' into something that needs a formal corrective action. This one came up because tail 738 logged a third APU bleed air valve write-up inside 45 flight days. Two earlier ones had been closed out as operational check normal, no parts changed, which is pretty typical — a lot of these clear on the bench. Interviewer: Walk me through the incident from the beginning, in your own words. Participant: So the third write-up on 738 is what actually got my attention, because three in that short a window is unusual even though our fleet-wide removal rate for that valve was still sitting inside the OEM's published MTBUR. Nothing screamed 'fleet problem' yet — it looked like it could just be a stubborn individual aircraft. I opened a focused review on that tail rather than calling it a fleet issue outright, and I put a flag on it so I'd get pinged if anything similar showed up elsewhere. Two days later it did — tail 712 logged a lower-severity version of basically the same complaint. That's when line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility we had an intermittent fault that ground checks weren't catching. At that point I pulled the two tails' component histories together and found they shared the same valve batch lot number. That felt like a real thread to pull. Interviewer: What did you do with that lot-number connection? Participant: Company policy is we don't like repeated MEL carryover on the same defect — dispatching with the APU inoperative under MEL is allowed, but doing it leg after leg on the same fault is a flag in itself. Neither aircraft had had an actual in-flight consequence; both faults were caught on the ground. So grounding both outright felt like more than the evidence supported at that point. I put an interim restriction on — one leg of MEL carryover maximum, then it has to be addressed — on both tails, and opened a formal root-cause investigation tied to that lot number. Interviewer: What came back from that investigation? Participant: The vendor quality engineer confirmed that lot had a documented seal-material change about six months earlier. That's a real, traceable cause — not a guess. And our in-house teardown of the valve we'd pulled off 738 showed seal degradation that was consistent with exactly that material change. So by that point I had two independent lines — vendor documentation and physical teardown — pointing at the same thing. Interviewer: Let's slow down on that moment, because I want to understand what happened next. What were you weighing? Participant: Right, so this is the part before I finalized anything for the Reliability Control Board. I had ten days to the RCB deadline. The vendor's lot documentation and our own teardown already lined up on the seal material as the cause, and honestly I'd already decided in my own head that the corrective action was going to be a lot-bounded replacement — that part felt settled. But there was still an option to send the valve out to an external metallurgical lab for an independent composition assay, on top of what I already had. Interviewer: And what did you decide? Participant: I sent it out anyway. I'd basically landed on the lot-based replacement regardless of what came back — I wasn't holding the recommendation open pending that result. I think I just wanted a third, fully independent source in the file alongside the vendor's own account of their material, so the package read as more thorough when it went to the board. I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway. Interviewer: At the time you sent it out, was there anything the assay could tell you that would have changed which corrective action you recommended? Participant: Not really, no. The recommendation was already written in my head — vendor records and physical teardown agreed, and that's what the corrective action request was going to be built on either way. I think I was after the reassurance of having one more test in the folder more than anything that would've moved the decision itself. Interviewer: What happened with the deadline? Participant: We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results, even though the recommendation itself wasn't really pending on anything. When the assay results did eventually land, they confirmed the same seal-material change the vendor had already told us about — nothing new in it. Interviewer: Let's move to the final decision — what you actually recommended once everything was in. Participant: Once the root cause was locked down, the OEM tech rep raised the idea of a broader design review of the valve seal spec generally, as a longer-term option. But that's a slow, separate track. What I had in front of me was a specific, bounded problem: one vendor lot, identifiable serial ranges. I wrote the corrective action request to replace valves from that lot specifically, not a fleet-wide swap of every valve regardless of lot, and not just deferring to wait on the OEM's broader review. Interviewer: Why bounded to the lot rather than fleet-wide? Participant: Because a fleet-wide replacement would have pulled serviceable, unaffected valves for no reason — that's cost and downtime with no reliability benefit. The evidence pointed specifically at that lot, so that's what I scoped the action to. Interviewer: What happened after you submitted it? Participant: RCB approved the lot-based campaign. Both tails got their valves replaced, and there haven't been further events on either aircraft since. The OEM's broader design review got pushed into a separate long-term study, which is still open as far as I know. Interviewer: Looking back at the whole sequence — is there a point where, with hindsight, you'd handle it differently? Participant: The one thing I go back and forth on is the external lab. I already knew the recommendation wasn't going to move based on what it found — I'd have submitted the same lot-based request either way. Knowing that now, I probably should have just submitted on the original ten-day timeline using the vendor and teardown evidence and let the RCB approve on that, rather than holding the whole submission for a test that was only ever going to restate what I already had. Interviewer: If the assay had come back showing something different from the vendor's account — a different degradation mechanism, say — what would you have done? Participant: I'd have flagged it and opened a separate follow-up investigation into whether the lot-based campaign needed a second look. But that would've come after the fact — I wasn't planning to hold up this submission on that possibility, since I'd already committed to the lot-based recommendation before the assay went out. Interviewer: And if this exact pattern showed up again on a different fleet type — same lot-based signature, same timeline pressure — would you send it out for independent lab work again? Participant: Probably not on the same timeline, honestly. I think I'd ask myself earlier on whether the extra data was likely to change the recommendation I'd already reached or just make the file look better, and weigh that against the deadline more explicitly than I did this time. Interviewer: That's a good place to stop. Thanks for the detail — this is exactly the kind of reconstruction we needed. Participant: No problem. Happy to follow up if anything else comes to mind.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.02s · gen 167.89s · total 173.4s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0245 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0241 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0237 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0221 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0203 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0200 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0199 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
10. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0197 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
11. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0193 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0193 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0192 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0190 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
16. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0189 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
17. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0186 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
18. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0184 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0184 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
22. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
23. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0174 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
24. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0172 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
25. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0170 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
26. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0168 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
27. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0164 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
28. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0162 (rrf) — _# Results d along with the results. occur during incidents and accidents? in the reports. ssocia_
29. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0162 (rrf) — _# f Space Flight write location pointer to not get updated correctly the C&DH side. Subsequent r_
30. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0161 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0159 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
34. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0154 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
37. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
38. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0150 (rrf) — _# Cognitive Biases in Technical Communication The Sun k Cost Fallacy refers to t decisions that _
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
42. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0144 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization 5.4 Limitations 154 b_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
44. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0143 (rrf) — _## BMC Medical Ethics Open Access - - - - - - - - - Cognitive bias and its consequences for ethi_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
46. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0141 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
47. **Hallihan_etal_DTM_12.pdf** — 0.0141 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "The transcript was assessed for affirmatively demonstrated cognitive biases in the participant's decision-making. One occurrence met the threshold: the decision to obtain and wait for an external lab assay that the participant stated could not affect the corrective-action recommendation."
  },
  "identified_bias_summary": [
    {
      "bias_label": "information bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "information bias",
      "alternative_labels": [
        "information-seeking bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek additional information even when that information cannot materially alter the current decision or action, often driven by a desire for reassurance, completeness, or perceived thoroughness rather than by diagnostic value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to send APU bleed air valve for external metallurgical assay and defer the RCB submission",
      "decision_point_description": "After the vendor documentation and teardown already supported a lot-bounded replacement, the participant decided whether to commission an independent external composition assay, knowing its turnaround would miss the RCB deadline.",
      "affected_reasoning_operation": "Information acquisition and timing of recommendation finalization",
      "bias_specific_mechanism": "The participant sought an extra test for reassurance and file completeness despite explicitly concluding that the result would not change the corrective-action recommendation, causing the submission to be delayed past the deadline without a decision-relevant reason.",
      "manifestation_in_interview": "The participant sent the valve for external lab testing after already deciding the lot-based replacement, described the test as being more about reassurance and thoroughness than moving the decision, and then missed the RCB cycle because the submission was held for a result he said was not really pending.",
      "effect_on_reasoning_or_decision": "The formal recommendation missed the ten-day RCB deadline and was delayed to submit-pending-lab-results, even though the recommendation was not substantively contingent on the lab result.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I sent it out anyway. I'd basically landed on the lot-based replacement regardless of what came back — I wasn't holding the recommendation open pending that result. I think I just wanted a third, fully independent source in the file alongside the vendor's own account of their material, so the package read as more thorough when it went to the board. I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway.",
          "evidence_explanation": "This quote shows he acquired additional information while explicitly aware that the decision was already made and that doing so would force a deadline miss; the stated motive was file thoroughness, not decision modification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. The recommendation was already written in my head — vendor records and physical teardown agreed, and that's what the corrective action request was going to be built on either way. I think I was after the reassurance of having one more test in the folder more than anything that would've moved the decision itself.",
          "evidence_explanation": "This is direct evidence that the extra information did not have decision-relevant value to him; the search was reassurance-driven, which is the core information-bias mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results, even though the recommendation itself wasn't really pending on anything.",
          "evidence_explanation": "This demonstrates the distorting consequence: submission was delayed for an informational input that was not logically required for the recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I already knew the recommendation wasn't going to move based on what it found — I'd have submitted the same lot-based request either way. Knowing that now, I probably should have just submitted on the original ten-day timeline using the vendor and teardown evidence and let the RCB approve on that, rather than holding the whole submission for a test that was only ever going to restate what I already had.",
          "evidence_explanation": "This retrospective acknowledgment reinforces that the extra test was non-decision-relevant and that its main effect was avoidable submission delay."
        }
      ],
      "correction_or_counterevidence": "A plausible non-bias explanation is that independent third-party verification can be a legitimate risk-management or board-assurance practice even when engineering conclusions are already formed. However, the participant explicitly states that the lab result would not have changed the recommendation and that the delay was avoidable; the demonstrated cost was a missed RCB cycle.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved passages discuss confirmation bias, expectation bias, plan continuation, availability, representativeness, and anchoring, but none defines or validates the specific mechanism of information bias, namely seeking non-decision-relevant information for reassurance and delaying action. The classification therefore relies on established general cognitive-science knowledge, not on the supplied RAG corpus.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Forming and finalizing the lot-bounded replacement recommendation",
      "supporting_interview_quote": "I'd already decided in my own head that the corrective action was going to be a lot-bounded replacement — that part felt settled. But there was still an option to send the valve out to an external metallurgical lab for an independent composition assay, on top of what I already had.",
      "plausible_mechanism": "A pre-existing commitment to the lot-based explanation may have motivated seeking confirmatory or incremental assurance rather than genuine disconfirmation.",
      "why_not_identified": "The transcript does not show selective avoidance, distortion, or discounting of disconfirming evidence; the participant ordered an independent assay capable of returning a different result and stated that a different result would trigger a follow-up. Thus classic confirmation bias is not affirmatively demonstrated."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on self-reported interview testimony rather than direct behavioral observation or decision records.",
    "The label 'information bias' was not present in the retrieved RAG passages, so corpus-based validation was unavailable for this occurrence.",
    "A plausible non-bias explanation, namely professional preference for independent corroboration or board-ready documentation, cannot be entirely excluded, which limits confidence.",
    "The retrieved corpus primarily addressed aviation and space-flight verification biases and did not provide a formal operational definition for reassurance-driven information seeking."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for an internal reliability-process review, not a safety investigation into you personally — we're trying to understand how these calls actually get made in practice. That okay with you? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me your role and how this particular case landed on your desk? Participant: Sure. I'm a reliability engineer in Maintenance Control. Part of my job is watching for repetitive write-ups across the fleet and deciding when something crosses from 'normal noise' into something that needs a formal corrective action. This one came up because tail 738 logged a third APU bleed air valve write-up inside 45 flight days. Two earlier ones had been closed out as operational check normal, no parts changed, which is pretty typical — a lot of these clear on the bench. Interviewer: Walk me through the incident from the beginning, in your own words. Participant: So the third write-up on 738 is what actually got my attention, because three in that short a window is unusual even though our fleet-wide removal rate for that valve was still sitting inside the OEM's published MTBUR. Nothing screamed 'fleet problem' yet — it looked like it could just be a stubborn individual aircraft. I opened a focused review on that tail rather than calling it a fleet issue outright, and I put a flag on it so I'd get pinged if anything similar showed up elsewhere. Two days later it did — tail 712 logged a lower-severity version of basically the same complaint. That's when line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility we had an intermittent fault that ground checks weren't catching. At that point I pulled the two tails' component histories together and found they shared the same valve batch lot number. That felt like a real thread to pull. Interviewer: What did you do with that lot-number connection? Participant: Company policy is we don't like repeated MEL carryover on the same defect — dispatching with the APU inoperative under MEL is allowed, but doing it leg after leg on the same fault is a flag in itself. Neither aircraft had had an actual in-flight consequence; both faults were caught on the ground. So grounding both outright felt like more than the evidence supported at that point. I put an interim restriction on — one leg of MEL carryover maximum, then it has to be addressed — on both tails, and opened a formal root-cause investigation tied to that lot number. Interviewer: What came back from that investigation? Participant: The vendor quality engineer confirmed that lot had a documented seal-material change about six months earlier. That's a real, traceable cause — not a guess. And our in-house teardown of the valve we'd pulled off 738 showed seal degradation that was consistent with exactly that material change. So by that point I had two independent lines — vendor documentation and physical teardown — pointing at the same thing. Interviewer: Let's slow down on that moment, because I want to understand what happened next. What were you weighing? Participant: Right, so this is the part before I finalized anything for the Reliability Control Board. I had ten days to the RCB deadline. The vendor's lot documentation and our own teardown already lined up on the seal material as the cause, and honestly I'd already decided in my own head that the corrective action was going to be a lot-bounded replacement — that part felt settled. But there was still an option to send the valve out to an external metallurgical lab for an independent composition assay, on top of what I already had. Interviewer: And what did you decide? Participant: I sent it out anyway. I'd basically landed on the lot-based replacement regardless of what came back — I wasn't holding the recommendation open pending that result. I think I just wanted a third, fully independent source in the file alongside the vendor's own account of their material, so the package read as more thorough when it went to the board. I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway. Interviewer: At the time you sent it out, was there anything the assay could tell you that would have changed which corrective action you recommended? Participant: Not really, no. The recommendation was already written in my head — vendor records and physical teardown agreed, and that's what the corrective action request was going to be built on either way. I think I was after the reassurance of having one more test in the folder more than anything that would've moved the decision itself. Interviewer: What happened with the deadline? Participant: We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results, even though the recommendation itself wasn't really pending on anything. When the assay results did eventually land, they confirmed the same seal-material change the vendor had already told us about — nothing new in it. Interviewer: Let's move to the final decision — what you actually recommended once everything was in. Participant: Once the root cause was locked down, the OEM tech rep raised the idea of a broader design review of the valve seal spec generally, as a longer-term option. But that's a slow, separate track. What I had in front of me was a specific, bounded problem: one vendor lot, identifiable serial ranges. I wrote the corrective action request to replace valves from that lot specifically, not a fleet-wide swap of every valve regardless of lot, and not just deferring to wait on the OEM's broader review. Interviewer: Why bounded to the lot rather than fleet-wide? Participant: Because a fleet-wide replacement would have pulled serviceable, unaffected valves for no reason — that's cost and downtime with no reliability benefit. The evidence pointed specifically at that lot, so that's what I scoped the action to. Interviewer: What happened after you submitted it? Participant: RCB approved the lot-based campaign. Both tails got their valves replaced, and there haven't been further events on either aircraft since. The OEM's broader design review got pushed into a separate long-term study, which is still open as far as I know. Interviewer: Looking back at the whole sequence — is there a point where, with hindsight, you'd handle it differently? Participant: The one thing I go back and forth on is the external lab. I already knew the recommendation wasn't going to move based on what it found — I'd have submitted the same lot-based request either way. Knowing that now, I probably should have just submitted on the original ten-day timeline using the vendor and teardown evidence and let the RCB approve on that, rather than holding the whole submission for a test that was only ever going to restate what I already had. Interviewer: If the assay had come back showing something different from the vendor's account — a different degradation mechanism, say — what would you have done? Participant: I'd have flagged it and opened a separate follow-up investigation into whether the lot-based campaign needed a second look. But that would've come after the fact — I wasn't planning to hold up this submission on that possibility, since I'd already committed to the lot-based recommendation before the assay went out. Interviewer: And if this exact pattern showed up again on a different fleet type — same lot-based signature, same timeline pressure — would you send it out for independent lab work again? Participant: Probably not on the same timeline, honestly. I think I'd ask myself earlier on whether the extra data was likely to change the recommendation I'd already reached or just make the file look better, and weigh that against the deadline more explicitly than I did this time. Interviewer: That's a good place to stop. Thanks for the detail — this is exactly the kind of reconstruction we needed. Participant: No problem. Happy to follow up if anything else comes to mind.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.90s · gen 159.83s · total 163.9s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0245 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0241 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0237 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0221 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0203 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0200 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0199 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
10. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0197 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
11. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0193 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0193 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0192 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0190 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
16. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0189 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
17. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0186 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
18. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0184 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0184 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
22. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
23. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0174 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
24. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0172 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
25. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0170 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
26. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0168 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
27. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0164 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
28. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0162 (rrf) — _# Results d along with the results. occur during incidents and accidents? in the reports. ssocia_
29. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0162 (rrf) — _# f Space Flight write location pointer to not get updated correctly the C&DH side. Subsequent r_
30. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0161 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0159 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
34. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0154 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
37. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
38. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0150 (rrf) — _# Cognitive Biases in Technical Communication The Sun k Cost Fallacy refers to t decisions that _
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
42. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0144 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization 5.4 Limitations 154 b_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
44. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0143 (rrf) — _## BMC Medical Ethics Open Access - - - - - - - - - Cognitive bias and its consequences for ethi_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
46. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0141 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
47. **Hallihan_etal_DTM_12.pdf** — 0.0141 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis focused on the reliability engineer's decision to commission an external metallurgical assay after already reaching a corrective-action recommendation, despite knowing the assay would not alter that recommendation and would cause a missed Reliability Control Board deadline."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Information bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Information bias",
      "alternative_labels": [
        "Non-instrumental information seeking",
        "Information-seeking bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek or collect additional information even when it cannot materially affect the decision or action at hand, often because more information seems reassuring or thorough.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to send the valve for an external composition assay despite an already-settled recommendation and a known deadline conflict",
      "decision_point_description": "Choosing whether to commission an independent external lab assay before the Reliability Control Board deadline, or to proceed with the existing vendor-documentation and teardown evidence.",
      "affected_reasoning_operation": "Information-gathering and evidence-collection decision under deadline",
      "bias_specific_mechanism": "The participant collected an additional piece of evidence even though he had already determined which corrective action he would recommend and stated that the new evidence would not change that recommendation. The value assigned to reassurance and a more thorough file overshadowed the cost of missing the decision deadline.",
      "manifestation_in_interview": "The participant reported that the recommendation was already settled in his mind before the external lab option, but he sent the valve out anyway. He knew the lab turnaround would blow the RCB deadline, and he later acknowledged the assay result would not have changed the corrective action request.",
      "effect_on_reasoning_or_decision": "The formal corrective-action submission missed the Reliability Control Board cycle and was held as pending lab results even though the recommendation itself was not pending on those results. The eventual assay only restated the existing cause.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd already decided in my own head that the corrective action was going to be a lot-bounded replacement — that part felt settled. But there was still an option to send the valve out to an external metallurgical lab for an independent composition assay, on top of what I already had.",
          "evidence_explanation": "This shows the decision was already made before the additional test was commissioned, establishing that the new information was unlikely to be decision-relevant."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I sent it out anyway. I'd basically landed on the lot-based replacement regardless of what came back — I wasn't holding the recommendation open pending that result. I think I just wanted a third, fully independent source in the file alongside the vendor's own account of their material, so the package read as more thorough when it went to the board. I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway.",
          "evidence_explanation": "The participant explicitly says the extra test was not going to change the recommendation and that he knew it would cause a deadline miss, yet he still ordered it, which is the core information-bias pattern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. The recommendation was already written in my head — vendor records and physical teardown agreed, and that's what the corrective action request was going to be built on either way. I think I was after the reassurance of having one more test in the folder more than anything that would've moved the decision itself.",
          "evidence_explanation": "This directly supports the mechanism: the information was sought for reassurance rather than for its potential to alter the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results, even though the recommendation itself wasn't really pending on anything. When the assay results did eventually land, they confirmed the same seal-material change the vendor had already told us about — nothing new in it.",
          "evidence_explanation": "This shows the actual effect: delayed submission and a result that provided no new decision-relevant information."
        }
      ],
      "correction_or_counterevidence": "Plausible non-bias explanations include legitimate engineering documentation norms, a desire for an independent audit trail for reliability-board credibility, and organizational expectations for third-party verification. The participant later recognized that the lab test was unnecessary for the decision and said he would weigh decision relevance against deadlines more explicitly in future.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage provided an adequate definition or mechanism specific to information bias. The label and mechanism are drawn from general cognitive-science and decision-making taxonomy rather than the supplied corpus.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passage directly addressed information bias, so the label relies on general cognitive-science knowledge.",
    "The analysis is based on a single retrospective self-report, so bias-relevant reasoning is inferred from the participant's own description rather than independent observation.",
    "The missed deadline may also have been shaped by organizational workflow or documentation practices, although the participant's own rationale supports information bias."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for an internal reliability-process review, not a safety investigation into you personally — we're trying to understand how these calls actually get made in practice. That okay with you? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me your role and how this particular case landed on your desk? Participant: Sure. I'm a reliability engineer in Maintenance Control. Part of my job is watching for repetitive write-ups across the fleet and deciding when something crosses from 'normal noise' into something that needs a formal corrective action. This one came up because tail 738 logged a third APU bleed air valve write-up inside 45 flight days. Two earlier ones had been closed out as operational check normal, no parts changed, which is pretty typical — a lot of these clear on the bench. Interviewer: Walk me through the incident from the beginning, in your own words. Participant: So the third write-up on 738 is what actually got my attention, because three in that short a window is unusual even though our fleet-wide removal rate for that valve was still sitting inside the OEM's published MTBUR. Nothing screamed 'fleet problem' yet — it looked like it could just be a stubborn individual aircraft. I opened a focused review on that tail rather than calling it a fleet issue outright, and I put a flag on it so I'd get pinged if anything similar showed up elsewhere. Two days later it did — tail 712 logged a lower-severity version of basically the same complaint. That's when line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility we had an intermittent fault that ground checks weren't catching. At that point I pulled the two tails' component histories together and found they shared the same valve batch lot number. That felt like a real thread to pull. Interviewer: What did you do with that lot-number connection? Participant: Company policy is we don't like repeated MEL carryover on the same defect — dispatching with the APU inoperative under MEL is allowed, but doing it leg after leg on the same fault is a flag in itself. Neither aircraft had had an actual in-flight consequence; both faults were caught on the ground. So grounding both outright felt like more than the evidence supported at that point. I put an interim restriction on — one leg of MEL carryover maximum, then it has to be addressed — on both tails, and opened a formal root-cause investigation tied to that lot number. Interviewer: What came back from that investigation? Participant: The vendor quality engineer confirmed that lot had a documented seal-material change about six months earlier. That's a real, traceable cause — not a guess. And our in-house teardown of the valve we'd pulled off 738 showed seal degradation that was consistent with exactly that material change. So by that point I had two independent lines — vendor documentation and physical teardown — pointing at the same thing. Interviewer: Let's slow down on that moment, because I want to understand what happened next. What were you weighing? Participant: Right, so this is the part before I finalized anything for the Reliability Control Board. I had ten days to the RCB deadline. The vendor's lot documentation and our own teardown already lined up on the seal material as the cause, and honestly I'd already decided in my own head that the corrective action was going to be a lot-bounded replacement — that part felt settled. But there was still an option to send the valve out to an external metallurgical lab for an independent composition assay, on top of what I already had. Interviewer: And what did you decide? Participant: I sent it out anyway. I'd basically landed on the lot-based replacement regardless of what came back — I wasn't holding the recommendation open pending that result. I think I just wanted a third, fully independent source in the file alongside the vendor's own account of their material, so the package read as more thorough when it went to the board. I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway. Interviewer: At the time you sent it out, was there anything the assay could tell you that would have changed which corrective action you recommended? Participant: Not really, no. The recommendation was already written in my head — vendor records and physical teardown agreed, and that's what the corrective action request was going to be built on either way. I think I was after the reassurance of having one more test in the folder more than anything that would've moved the decision itself. Interviewer: What happened with the deadline? Participant: We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results, even though the recommendation itself wasn't really pending on anything. When the assay results did eventually land, they confirmed the same seal-material change the vendor had already told us about — nothing new in it. Interviewer: Let's move to the final decision — what you actually recommended once everything was in. Participant: Once the root cause was locked down, the OEM tech rep raised the idea of a broader design review of the valve seal spec generally, as a longer-term option. But that's a slow, separate track. What I had in front of me was a specific, bounded problem: one vendor lot, identifiable serial ranges. I wrote the corrective action request to replace valves from that lot specifically, not a fleet-wide swap of every valve regardless of lot, and not just deferring to wait on the OEM's broader review. Interviewer: Why bounded to the lot rather than fleet-wide? Participant: Because a fleet-wide replacement would have pulled serviceable, unaffected valves for no reason — that's cost and downtime with no reliability benefit. The evidence pointed specifically at that lot, so that's what I scoped the action to. Interviewer: What happened after you submitted it? Participant: RCB approved the lot-based campaign. Both tails got their valves replaced, and there haven't been further events on either aircraft since. The OEM's broader design review got pushed into a separate long-term study, which is still open as far as I know. Interviewer: Looking back at the whole sequence — is there a point where, with hindsight, you'd handle it differently? Participant: The one thing I go back and forth on is the external lab. I already knew the recommendation wasn't going to move based on what it found — I'd have submitted the same lot-based request either way. Knowing that now, I probably should have just submitted on the original ten-day timeline using the vendor and teardown evidence and let the RCB approve on that, rather than holding the whole submission for a test that was only ever going to restate what I already had. Interviewer: If the assay had come back showing something different from the vendor's account — a different degradation mechanism, say — what would you have done? Participant: I'd have flagged it and opened a separate follow-up investigation into whether the lot-based campaign needed a second look. But that would've come after the fact — I wasn't planning to hold up this submission on that possibility, since I'd already committed to the lot-based recommendation before the assay went out. Interviewer: And if this exact pattern showed up again on a different fleet type — same lot-based signature, same timeline pressure — would you send it out for independent lab work again? Participant: Probably not on the same timeline, honestly. I think I'd ask myself earlier on whether the extra data was likely to change the recommendation I'd already reached or just make the file look better, and weigh that against the deadline more explicitly than I did this time. Interviewer: That's a good place to stop. Thanks for the detail — this is exactly the kind of reconstruction we needed. Participant: No problem. Happy to follow up if anything else comes to mind.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.93s · gen 135.49s · total 139.6s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0245 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0241 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
3. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0237 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0221 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0203 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0200 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0199 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
10. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0197 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
11. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0193 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0193 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0192 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0192 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0190 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
16. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0189 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
17. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0186 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
18. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0184 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0184 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
22. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
23. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0174 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
24. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0172 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
25. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0170 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
26. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0168 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
27. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0164 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
28. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0162 (rrf) — _# Results d along with the results. occur during incidents and accidents? in the reports. ssocia_
29. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0162 (rrf) — _# f Space Flight write location pointer to not get updated correctly the C&DH side. Subsequent r_
30. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0161 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
31. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0159 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
34. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0154 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
37. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
38. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0150 (rrf) — _# Cognitive Biases in Technical Communication The Sun k Cost Fallacy refers to t decisions that _
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0148 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
42. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0144 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization 5.4 Limitations 154 b_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
44. **Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf** — 0.0143 (rrf) — _## BMC Medical Ethics Open Access - - - - - - - - - Cognitive bias and its consequences for ethi_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0142 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
46. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0141 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
47. **Hallihan_etal_DTM_12.pdf** — 0.0141 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology tureofth pl icit, forcing the reader to de_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative, mechanism-first assessment of the interview transcript for affirmatively evidenced cognitive biases; retrieved passages were reviewed but not used as corpus support because they did not define the mechanism for the identified occurrence."
  },
  "identified_bias_summary": [
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
      "alternative_labels": ["myside bias", "confirmatory information-seeking"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports an already-established belief or decision, while giving insufficient weight to disconfirmatory or decision-relevant information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to send APU bleed air valve for external laboratory assay before the RCB deadline",
      "decision_point_description": "After vendor documentation and in-house teardown had already converged on a lot-specific seal-material root cause, the participant chose whether to send the valve for an independent external composition assay despite a known three-week turnaround that would miss the RCB deadline.",
      "affected_reasoning_operation": "Information search and evidence acquisition",
      "bias_specific_mechanism": "Confirmatory information-seeking: the participant sought an additional independent test primarily for reassurance and file completeness after having already committed to the lot-bounded replacement recommendation. The test's potential disconfirmatory value was not allowed to alter the pending recommendation, and the participant did not treat it as decision-relevant before authorizing the delay-causing test.",
      "manifestation_in_interview": "The participant stated that the lot-based corrective action was already settled before ordering the external assay, that the recommendation would be submitted either way, and that the extra test was sought for reassurance and to make the package read as more thorough. He knew the test would miss the RCB deadline and sent it anyway, which caused the submission to slip.",
      "effect_on_reasoning_or_decision": "The participant authorized a costly and time-consuming confirmatory test that was not needed to make the recommendation. As a result, the finalized recommendation missed the RCB cycle and was delayed as submit-pending-lab-results, although the eventual assay merely confirmed the existing vendor and teardown finding.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd already decided in my own head that the corrective action was going to be a lot-bounded replacement — that part felt settled. But there was still an option to send the valve out to an external metallurgical lab for an independent composition assay, on top of what I already had.",
          "evidence_explanation": "This shows the participant had reached a conclusion before ordering the additional test, framing the assay as supplementary rather than decision-driving."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I sent it out anyway. I'd basically landed on the lot-based replacement regardless of what came back — I wasn't holding the recommendation open pending that result.",
          "evidence_explanation": "This directly demonstrates that the test result was not going to affect the recommendation, yet he still authorized the test."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I was after the reassurance of having one more test in the folder more than anything that would've moved the decision itself.",
          "evidence_explanation": "This is an explicit statement of confirmatory reassurance-seeking rather than decision-relevant information gathering."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway.",
          "evidence_explanation": "This shows the participant knowingly accepted a deadline miss for a test he had already indicated would not change the recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results, even though the recommendation itself wasn't really pending on anything.",
          "evidence_explanation": "This confirms the concrete consequence: the recommendation was delayed by the confirmatory test even though no substantive decision point remained open."
        }
      ],
      "correction_or_counterevidence": "The participant later reflected retrospectively that he probably should have submitted on the original ten-day timeline and that in future he would explicitly weigh whether extra data would change the recommendation or only improve the file; however, this reflection occurred after the biased test decision and did not prevent the deadline slip.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved passages mention confirmation bias in aviation and engineering-reliability contexts, but they do not provide a definitional mechanism or diagnostic pattern for this occurrence. The label is therefore assigned from established general cognitive-science knowledge, with no retrieved corpus evidence used.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": ["escalation of commitment", "get-there-itis"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Proceeding with external lab assay despite known deadline impact",
      "supporting_interview_quote": "I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway.",
      "plausible_mechanism": "Continuing with an intended course of action despite a known negative timeline cue and lack of decision relevance.",
      "why_not_identified": "The timeline cue was known before the decision to send the assay, and the participant's own explanation attributes the action to confirmatory reassurance-seeking rather than to an ongoing plan that persisted after new adverse information emerged; therefore a separate plan-continuation mechanism is not affirmatively evidenced."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieval context was sparse and did not supply a formal mechanism definition for confirmation bias.",
    "Analysis is based entirely on participant self-report; there are no independent operational or maintenance records to cross-check the described decision process."
  ]
}

