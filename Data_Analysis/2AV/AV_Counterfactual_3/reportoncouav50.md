# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just so you know, I'll ask you to walk through a specific turnaround and explain your thinking as it unfolded, not just what ended up happening. Can you tell me your role and a bit about your background? Participant: Sure. I've been a load controller about nine years, mostly narrow-body combi work. Normally I build the load sheet, issue the loading instruction to the ramp, check weight and balance against structural limits, and finalize the NOTOC for the captain. This one wasn't a normal turn, though—the inbound aircraft came in late, so instead of our usual 45 minutes on the ground, we were looking at more like 30 before the slot. Interviewer: How did that change things going in? Participant: Right away I knew I'd be compressing steps I'd normally spread out a bit more. Nothing about the flight itself was unusual—same route, same aircraft type—it was just less time to work with. Interviewer: Walk me through what happened. Participant: I got the cargo manifest with about 30 minutes left. Mixed load—regular bags, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what typically goes through, not palletized. Our load-control software generates an automatic load instruction, and it put that machinery item into hold 3. That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately. About fifteen minutes later, the ramp called and said the aircraft was sitting slightly tail-heavy—not out of limits, just aft of where you'd expect. Interviewer: What did you do with that? Participant: Logged it and kept going, because right then an LMC came in—about 380 kilos of mail plus six late bags that missed the original manifest. That mail got assigned to hold 5, our aft bulk hold. With the time we had left, I looked at the total weight, saw it was in line with the LMCs we'd been getting all week on this route—three similar ones, same range, none of those needed redistribution—and cleared it on that basis so I could move to the trim sheet. Interviewer: And the trim sheet itself? Participant: I pulled the dispatch log for a quick check, given the tail-heavy call from the ramp. Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required. Interviewer: Let's go through each of those moments in more detail. Starting with the ALI and the machinery item—what specifically told you it was fine to run with as generated? Participant: Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me. Interviewer: Was there a manual chart you could have checked against for that kind of cargo? Participant: There is, for exactly that situation. I know where it is. I just didn't reach for it that day. Interviewer: What would have made you stop and pull it? Participant: If we'd had the full 45, probably. Or if the system itself had thrown some kind of flag saying this needs manual sign-off. Neither of those happened, so I treated it like any other ALI. Interviewer: On the LMC—what exactly did you compare when the mail and bags came in? Participant: Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest. Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs went? Participant: No, not specifically. The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it. Interviewer: What would it have taken to run that calculation directly? Participant: A few extra minutes at the trim computer. It wasn't unavailable to me. I just didn't think it was worth the time against the schedule we were on. Interviewer: On the trim sheet redistribution—how did you connect the two previous flights to this one? Participant: They were on the same rotation, back to back, and both needed aft correction. Two in a row felt like it meant something about how the rotation was running that day, so I built in a forward shift before signing off, and honestly, with the time we had left, I didn't feel like there was room to dig into it further. Interviewer: What did your own calculated index for this flight show on its own? Participant: It was fine—within the normal forward range with margin. The redistribution wasn't because my numbers were bad. It was more that seeing two prior aft trims made me not fully trust it, and I didn't have the minutes to sit with that discomfort. Interviewer: Did you find out afterward why those two flights ran tail-heavy? Participant: Yeah—one was a fuel imbalance, the other had extra catering loaded late. Different tails, unrelated causes. Nothing tying them to each other or to this flight. Interviewer: Last one—the final sign-off. What was the situation? Participant: Closeout figures looked clean, within limits. But the ramp tally was one bag short of the NOTOC and manifest. Small discrepancy, and the slot was closing faster than a normal turn would allow. Interviewer: What did you decide, and what were you weighing? Participant: I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself. It turned out to be a manifest correction afterward—the weight and balance conclusion didn't change. I can see someone holding a couple minutes to chase it down instead. Neither call feels obviously wrong to me. Interviewer: How confident were you in each of these at the time, versus now? Participant: The ALI and the LMC, fairly confident in the moment, more than I'd be now looking back. The trim redistribution, less sure even then—it felt like caution more than certainty. The sign-off, I'm still not positive I made the better call, but I don't think it was unreasonable given the time. Interviewer: If you'd had the full 45 minutes instead of 30, would you have handled the machinery cargo differently? Participant: Probably, yes. I think I'd have pulled the manual chart. The shorter window is what pushed me to just trust the system's history instead. Interviewer: If the mail had gone to the usual forward hold instead of hold 5? Participant: Then the weight comparison would've actually held up fine, since placement wouldn't have mattered as much. It was the aft location that made that comparison misleading, not the comparison itself. Interviewer: If you'd known upfront the two prior tail-heavy events were unrelated, would you have redistributed the same way? Participant: No. I'd have trusted my own numbers for this flight instead of layering in a correction based on two other tails. Interviewer: Anything you'd do differently facing this same sequence again, under the same shortened window? Participant: Pull the manual chart for anything irregular no matter how tight the clock is, and keep this flight's numbers separate from what happened on previous ones unless I actually know there's a shared cause. The LMC piece I'd still have to think through—weight alone wasn't the full story that day, and less time made that easier to miss, not harder.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.88s · gen 188.48s · total 192.7s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0287 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0278 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0269 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0260 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0255 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0229 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0228 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0218 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0197 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0196 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0190 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
13. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0189 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
15. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0181 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0178 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0175 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
20. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0172 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
22. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0169 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0166 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
28. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
29. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0161 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration et al., 1994; McGu_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
32. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0158 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration complacency? Three_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
34. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0154 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
36. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0154 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
37. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0153 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
38. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0153 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
40. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
41. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0149 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
42. **Hallihan_etal_DTM_12.pdf** — 0.0149 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
44. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0147 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
47. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
50. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first examination of a single load-control turnaround interview. Only affirmative, transcript-supported bias-specific distortions are classified; time pressure alone was not treated as a bias."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "automation bias",
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
      "confidence": "moderate",
      "bias_label": "automation bias",
      "alternative_labels": ["automation complacency", "automation-induced complacency"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to over-rely on automated system output and omit sufficient independent verification, even when situational cues or unusual-case indicators suggest that verification is warranted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Issuing the automatic load instruction for irregular machinery",
      "decision_point_description": "Whether to accept the system-generated placement of an irregular, heavier-than-typical machinery item in hold 3 and issue the ALI immediately, or to stop and hand-verify using the manual chart under 30-minute time pressure.",
      "affected_reasoning_operation": "Verification and oversight of automated decision support; evidence weighting",
      "bias_specific_mechanism": "The participant cued on the load-control system's long history of reliability and the immediate time pressure. This overtrust suppressed manual verification for a non-routine cargo item, even though a manual chart existed for exactly that situation and the participant had noticed the item was irregular.",
      "manifestation_in_interview": "The participant noticed the machinery was irregular, not palletized, and heavier than usual, but issued the ALI as generated without pulling the available manual chart. He stated that he treated it like any other ALI because the system had been reliable and time was short.",
      "effect_on_reasoning_or_decision": "A potentially unusual and safety-relevant cargo placement was accepted without independent verification, allowing the automated system output to bypass the situation-specific manual check.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately.",
          "evidence_explanation": "This shows the automation was accepted largely because of reliability history and time pressure, rather than independent verification of the specific generated instruction."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me.",
          "evidence_explanation": "The participant explicitly noticed the unusual cargo attributes but still deferred to the automated output; this is direct evidence of automation overtrust."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There is, for exactly that situation. I know where it is. I just didn't reach for it that day.",
          "evidence_explanation": "A situation-specific manual verification aid was available and known, but was not used, reinforcing that the omission was one of decision-making rather than tool unavailability."
        }
      ],
      "correction_or_counterevidence": "Time compression was a real contextual constraint, and the automated system had a genuine record of reliability. However, the participant acknowledged that the cargo's unusual features registered and that a specific manual chart existed. The bias-specific distortion is that the system's history and time pressure prematurely closed the decision to verify, despite the irregular-cargo cue.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved source supports reduced verification of automated recommendations due to complacency or automation reliance.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it. Participants were provided independent access (via mouse click) to all relevant system information (e.g., tank levels, flow rates at different valves, history graphs displaying the time course of system parameters), needed to verify the aid’s diagnoses. This procedure allowed the investigators to assess the level of operator complacency in interaction with the aid by contrasting the actual information sampling behavior of operators with a “normative model” of optimal behavior. According to this logic, any participant who accessed just the information appropriate to verify a given diagnosis before accepting it was regarded as showing noncomplacent (eutactic) behavior in interaction with the aid. However, participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "Operators may sample less information than necessary to verify an automated recommendation, reflecting complacency in human-automation interaction.",
          "relevance_to_this_occurrence": "The participant accepted a system-generated ALI without consulting the available manual check for an irregular item, thereby sampling less verification information than the situation warranted."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment heuristic", "insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "People make estimates or decisions based on an initial value or prior example and adjust insufficiently from that reference point, even when later information requires a larger adjustment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Clearing the late-mail and baggage LMC",
      "decision_point_description": "Whether to clear a 380 kg mail plus six late bags LMC assigned to aft hold 5 based solely on total-weight similarity to recent LMCs, or to compute the actual index shift for the aft placement.",
      "affected_reasoning_operation": "Weight comparison and aircraft balance index adjustment",
      "bias_specific_mechanism": "The participant anchored on the total weight of three similar LMCs from the same week and used that prior value as sufficient evidence for clearance. He failed to adjust for the materially different placement: earlier LMCs went forward into hold 2, while this LMC went aft into hold 5. The participant later acknowledged that the aft location made the comparison misleading.",
      "manifestation_in_interview": "He cleared the LMC because the total weight matched recent examples, without running the index shift for the specific aft hold placement, even though the trim computer was available.",
      "effect_on_reasoning_or_decision": "The load was cleared in an aft hold without computing the actual balance consequence, allowing a placement-sensitive distribution change to be treated as harmless based on total weight alone.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That mail got assigned to hold 5, our aft bulk hold. With the time we had left, I looked at the total weight, saw it was in line with the LMCs we'd been getting all week on this route—three similar ones, same range, none of those needed redistribution—and cleared it on that basis so I could move to the trim sheet.",
          "evidence_explanation": "This shows the decision was made by comparing total weight to prior examples rather than evaluating the new aft-hold placement itself."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest.",
          "evidence_explanation": "The anchor was the available recent total-weight value, which was used because it was easy to access."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not specifically. The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it.",
          "evidence_explanation": "This directly demonstrates the failure to adjust for the different hold location after anchoring on previous similar weights."
        }
      ],
      "correction_or_counterevidence": "Time pressure was a real factor, and total weight was the fastest available check. However, the trim computer was available and the participant later identified that the aft placement made the comparison misleading. The specific distortion is anchoring on prior similar weights and insufficient adjustment for the different aircraft location.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved source supports the anchoring-and-adjustment mechanism, including its sensitivity to time pressure.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoring-and-adjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoring-and-adjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The anchoring-and-adjustment heuristic is documented as a resource-rational tradeoff; less time is associated with less adjustment away from an initial anchor.",
          "relevance_to_this_occurrence": "The participant used prior similar LMC weights as an anchor under time pressure and did not adjust for the aft-hold placement, matching the documented mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["selective evidence weighting", "hypothesis confirmation"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms one's prior beliefs or expectations, while giving disproportionately less weight to contradictory evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Trim sheet redistribution after tail-heavy call",
      "decision_point_description": "Whether to trust the current flight's calculated index, which was within normal forward range with margin, or to apply an extra forward shift based on the ramp report and two previous flights on the rotation.",
      "affected_reasoning_operation": "Interpretation of multiple sources of evidence; causal inference about current aircraft balance state",
      "bias_specific_mechanism": "The participant formed a prior expectation that the rotation was running tail-heavy from the ramp report. He then treated two prior same-rotation flights requiring aft trim as confirmatory evidence about this specific flight, while discounting his own current-flight index that was within normal forward range and required no additional correction.",
      "manifestation_in_interview": "The participant shifted cargo forward beyond what his own index required after seeing two previous flights with aft trim corrections. He stated that seeing two prior aft trims made him not fully trust his own numbers.",
      "effect_on_reasoning_or_decision": "A non-required forward redistribution was applied after discounting valid current-flight data, potentially introducing a new balance departure under time pressure.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required.",
          "evidence_explanation": "This shows the participant using prior flights as confirmatory evidence for a rotation-level tail-heavy expectation, despite the current flight's own index not requiring the shift."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was fine—within the normal forward range with margin. The redistribution wasn't because my numbers were bad. It was more that seeing two prior aft trims made me not fully trust it, and I didn't have the minutes to sit with that discomfort.",
          "evidence_explanation": "This confirms that contradictory evidence from the current flight was available, but was discounted in favor of the prior expectation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. I'd have trusted my own numbers for this flight instead of layering in a correction based on two other tails.",
          "evidence_explanation": "This counterfactual statement directly links the biased redistribution to the confirmatory interpretation of the previous two flights rather than to the actual current-flight data."
        }
      ],
      "correction_or_counterevidence": "At the moment of decision, the participant did not yet know the two prior events had unrelated causes. Time pressure also made it harder to sit with the discomfort created by the disconfirmatory current-flight index. Nevertheless, the current-flight index was available and contradicted the tail-heavy rotation hypothesis; the bias-specific distortion was the selective weighting of prior confirmatory cases over current disconfirmatory data.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved cockpit study explicitly describes confirmation bias in flight crew, including ignoring contradictory aircraft instruments in favor of cues supporting a mental model.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC conditions, found that the crew’s confirmation bias was supported by being able to visually identify cues that supported their mental model such as yellow markers on the taxiway which were perceived to be yellow runway markers. Similarly for flight Comair 5191 (2006) which took off from the incorrect runway in darkness and VMC conditions, the investigation found that the visual cues available to the crew induced a state of confirmation bias which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft’s position.",
          "mechanism_supported_by_source": "Confirmation bias led operators to favor cues consistent with a prior mental model and ignore contradictory evidence, including aircraft instruments.",
          "relevance_to_this_occurrence": "The participant similarly favored prior-flight cues and the ramp report consistent with a tail-heavy rotation while discounting his own current-flight index, which was the equivalent of the contradictory instrument evidence."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "normalization of deviance",
      "alternative_labels": ["normalcy bias", "minor-discrepancy normalization"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final sign-off with one-bag discrepancy",
      "supporting_interview_quote": "I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself.",
      "plausible_mechanism": "A one-bag discrepancy was treated as a mundane miscount rather than as a signal requiring reconciliation, which could reflect normalization of a small deviation under schedule pressure.",
      "why_not_identified": "The transcript shows an explicit risk tradeoff rather than an unexamined dismissal or gradual erosion of precaution. The participant considered the delay risk and the usual harmlessness of such discrepancies, and ordinary decision-making under uncertainty plus time pressure are sufficient non-bias explanations."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a retrospective self-report, and some reasoning may be rationalized after the fact.",
    "Time pressure was a cross-cutting contextual factor across all decisions, requiring care to separate bias-specific mechanisms from adaptive compression of procedures.",
    "Corpus support for some characteristics was limited to retrieved passages on aviation and automation; not all established bias mechanisms had perfectly matched empirical sources.",
    "The analysis is limited to the transcript evidence and does not infer experimental condition, benchmark status, or counterfactual design."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just so you know, I'll ask you to walk through a specific turnaround and explain your thinking as it unfolded, not just what ended up happening. Can you tell me your role and a bit about your background? Participant: Sure. I've been a load controller about nine years, mostly narrow-body combi work. Normally I build the load sheet, issue the loading instruction to the ramp, check weight and balance against structural limits, and finalize the NOTOC for the captain. This one wasn't a normal turn, though—the inbound aircraft came in late, so instead of our usual 45 minutes on the ground, we were looking at more like 30 before the slot. Interviewer: How did that change things going in? Participant: Right away I knew I'd be compressing steps I'd normally spread out a bit more. Nothing about the flight itself was unusual—same route, same aircraft type—it was just less time to work with. Interviewer: Walk me through what happened. Participant: I got the cargo manifest with about 30 minutes left. Mixed load—regular bags, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what typically goes through, not palletized. Our load-control software generates an automatic load instruction, and it put that machinery item into hold 3. That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately. About fifteen minutes later, the ramp called and said the aircraft was sitting slightly tail-heavy—not out of limits, just aft of where you'd expect. Interviewer: What did you do with that? Participant: Logged it and kept going, because right then an LMC came in—about 380 kilos of mail plus six late bags that missed the original manifest. That mail got assigned to hold 5, our aft bulk hold. With the time we had left, I looked at the total weight, saw it was in line with the LMCs we'd been getting all week on this route—three similar ones, same range, none of those needed redistribution—and cleared it on that basis so I could move to the trim sheet. Interviewer: And the trim sheet itself? Participant: I pulled the dispatch log for a quick check, given the tail-heavy call from the ramp. Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required. Interviewer: Let's go through each of those moments in more detail. Starting with the ALI and the machinery item—what specifically told you it was fine to run with as generated? Participant: Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me. Interviewer: Was there a manual chart you could have checked against for that kind of cargo? Participant: There is, for exactly that situation. I know where it is. I just didn't reach for it that day. Interviewer: What would have made you stop and pull it? Participant: If we'd had the full 45, probably. Or if the system itself had thrown some kind of flag saying this needs manual sign-off. Neither of those happened, so I treated it like any other ALI. Interviewer: On the LMC—what exactly did you compare when the mail and bags came in? Participant: Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest. Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs went? Participant: No, not specifically. The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it. Interviewer: What would it have taken to run that calculation directly? Participant: A few extra minutes at the trim computer. It wasn't unavailable to me. I just didn't think it was worth the time against the schedule we were on. Interviewer: On the trim sheet redistribution—how did you connect the two previous flights to this one? Participant: They were on the same rotation, back to back, and both needed aft correction. Two in a row felt like it meant something about how the rotation was running that day, so I built in a forward shift before signing off, and honestly, with the time we had left, I didn't feel like there was room to dig into it further. Interviewer: What did your own calculated index for this flight show on its own? Participant: It was fine—within the normal forward range with margin. The redistribution wasn't because my numbers were bad. It was more that seeing two prior aft trims made me not fully trust it, and I didn't have the minutes to sit with that discomfort. Interviewer: Did you find out afterward why those two flights ran tail-heavy? Participant: Yeah—one was a fuel imbalance, the other had extra catering loaded late. Different tails, unrelated causes. Nothing tying them to each other or to this flight. Interviewer: Last one—the final sign-off. What was the situation? Participant: Closeout figures looked clean, within limits. But the ramp tally was one bag short of the NOTOC and manifest. Small discrepancy, and the slot was closing faster than a normal turn would allow. Interviewer: What did you decide, and what were you weighing? Participant: I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself. It turned out to be a manifest correction afterward—the weight and balance conclusion didn't change. I can see someone holding a couple minutes to chase it down instead. Neither call feels obviously wrong to me. Interviewer: How confident were you in each of these at the time, versus now? Participant: The ALI and the LMC, fairly confident in the moment, more than I'd be now looking back. The trim redistribution, less sure even then—it felt like caution more than certainty. The sign-off, I'm still not positive I made the better call, but I don't think it was unreasonable given the time. Interviewer: If you'd had the full 45 minutes instead of 30, would you have handled the machinery cargo differently? Participant: Probably, yes. I think I'd have pulled the manual chart. The shorter window is what pushed me to just trust the system's history instead. Interviewer: If the mail had gone to the usual forward hold instead of hold 5? Participant: Then the weight comparison would've actually held up fine, since placement wouldn't have mattered as much. It was the aft location that made that comparison misleading, not the comparison itself. Interviewer: If you'd known upfront the two prior tail-heavy events were unrelated, would you have redistributed the same way? Participant: No. I'd have trusted my own numbers for this flight instead of layering in a correction based on two other tails. Interviewer: Anything you'd do differently facing this same sequence again, under the same shortened window? Participant: Pull the manual chart for anything irregular no matter how tight the clock is, and keep this flight's numbers separate from what happened on previous ones unless I actually know there's a shared cause. The LMC piece I'd still have to think through—weight alone wasn't the full story that day, and less time made that easier to miss, not harder.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.91s · gen 271.81s · total 276.0s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0287 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0278 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0269 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0260 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0255 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0229 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0228 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0218 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0197 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0196 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0190 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
13. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0189 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
15. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0181 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0178 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0175 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
20. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0172 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
22. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0169 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0166 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
28. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
29. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0161 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration et al., 1994; McGu_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
32. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0158 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration complacency? Three_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
34. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0154 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
36. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0154 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
37. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0153 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
38. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0153 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
40. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
41. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0149 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
42. **Hallihan_etal_DTM_12.pdf** — 0.0149 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
44. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0147 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
47. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
50. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a load controller's reasoning during a time-compressed aircraft turnaround, focusing on load-sheet, LMC, trim, and sign-off decisions under schedule pressure."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "automation complacency",
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
      "bias_label": "automation complacency",
      "alternative_labels": ["automation bias", "overreliance on automation", "automation-induced complacency"],
      "taxonomy_status": "established_label",
      "bias_definition": "A form of overtrust in automation in which an operator verifies or samples less information than needed before accepting an automated recommendation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Issuing the automatic load instruction for an irregular cargo item without manual verification",
      "decision_point_description": "Deciding whether to accept the system-generated ALI placing the irregular machinery item in hold 3 or to manually verify it with an available chart.",
      "affected_reasoning_operation": "Verification and cross-checking of an automated load-planning output",
      "bias_specific_mechanism": "Historical reliability of the load-control software, combined with time pressure, reduced the participant's verification behavior. He registered the cargo as irregular and heavier than usual, but accepted the automated placement without consulting the manual chart.",
      "manifestation_in_interview": "The participant noticed that the machinery item was irregular, not on a pallet, and heavier than usual, but issued the ALI as generated because the system had been reliable and manual verification felt too time-consuming.",
      "effect_on_reasoning_or_decision": "The irregular cargo was loaded according to the unverified automated instruction; the aircraft was later reported as sitting slightly tail-heavy, though not out of limits.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately.",
          "evidence_explanation": "Shows acceptance of an automated output based on system reliability and time pressure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me.",
          "evidence_explanation": "Demonstrates that atypical cargo cues were noticed but did not trigger verification, consistent with automation complacency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There is, for exactly that situation. I know where it is. I just didn't reach for it that day.",
          "evidence_explanation": "Confirms that a manual verification resource was available and accessible, but was not used."
        }
      ],
      "correction_or_counterevidence": "The automated system may indeed have been reliable, and accepting it under severe time pressure could be resource-rational. The later tail-heavy report was not out of limits, but the bias concerns reduced verification, not the eventual safety outcome.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label supported by retrieved passage on complacency in automation use; the passage operationalizes complacency as reduced verification of automated recommendations.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it. Participants were provided independent access (via mouse click) to all relevant system information (e.g., tank levels, flow rates at different valves, history graphs displaying the time course of system parameters), needed to verify the aid’s diagnoses. This procedure allowed the investigators to assess the level of operator complacency in interaction with the aid by contrasting the actual information sampling behavior of operators with a “normative model” of optimal behavior.",
          "mechanism_supported_by_source": "Complacency is operationalized as sampling less information than necessary to verify an automated recommendation before accepting it.",
          "relevance_to_this_occurrence": "The participant had a manual chart available to verify the automated ALI but did not consult it, matching the reduced-verification pattern described in the retrieved passage."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": ["anchoring bias", "insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to make estimates or decisions by starting from an accessible initial value and then adjusting insufficiently from that anchor, especially under time constraints.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Clearing a last-minute LMC placed in the aft hold 5",
      "decision_point_description": "Deciding whether the 380 kg of mail plus six late bags assigned to hold 5 required index recalculation or redistribution.",
      "affected_reasoning_operation": "Assessment of load placement and moment-index consequences",
      "bias_specific_mechanism": "The participant anchored on the total weight of recent prior LMCs and used it as a sufficient reference, then insufficiently adjusted for the new LMC's different hold placement, specifically aft hold 5 versus forward hold 2, under time pressure.",
      "manifestation_in_interview": "He checked only total weight against the week's prior LMCs and did not run the index shift for the aft placement, even though he knew the placement differed.",
      "effect_on_reasoning_or_decision": "The aft hold 5 LMC was cleared without a placement-specific moment calculation; the participant later acknowledged that the weight comparison was misleading for an aft location.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest.",
          "evidence_explanation": "Shows that the participant used prior LMC total weight as the accessible anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it.",
          "evidence_explanation": "Explicitly shows insufficient adjustment for placement difference from the anchor comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the mail had gone to the usual forward hold instead of hold 5? Then the weight comparison would've actually held up fine, since placement wouldn't have mattered as much. It was the aft location that made that comparison misleading, not the comparison itself.",
          "evidence_explanation": "The participant later recognizes that the anchor comparison was not appropriate for the aft placement."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized that the comparison failed because of aft placement, not total weight. The decision may also reflect ordinary time-pressure triage, but the explicit use of prior LMC total weight and absence of placement-specific adjustment supports the anchoring mechanism.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passage on anchoring-and-adjustment under time pressure is used to support the mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringand-adjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Under tighter time, people are less likely to sufficiently adjust away from an initial anchor.",
          "relevance_to_this_occurrence": "The participant used prior LMC total weight as an initial reference and, with the time squeeze, did not adjust for the new aft placement."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["expectation bias", "selective information weighting"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms a pre-existing hypothesis while giving disproportionately less weight to contradictory evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Adding a forward cargo shift to the trim sheet after two prior aft trim corrections",
      "decision_point_description": "Deciding whether this flight's trim should be adjusted beyond its own calculated index based on two previous flights on the same rotation.",
      "affected_reasoning_operation": "Inference about the current aircraft's trim state and required load distribution",
      "bias_specific_mechanism": "After the ramp reported a tail-heavy condition, the participant formed the hypothesis that the rotation was running tail-heavy. He then gave weight to two prior aft trim events as confirming that hypothesis and distrusted his own current-flight index, which contradicted it.",
      "manifestation_in_interview": "He shifted cargo forward beyond what his own index required after seeing two previous aft trims, even though his calculated index was within the normal forward range with margin.",
      "effect_on_reasoning_or_decision": "He overrode an objective current-flight trim calculation and applied a forward correction based on unrelated prior flights. He later said he would have trusted his own numbers had he known the prior causes were unrelated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required.",
          "evidence_explanation": "Shows prior events being used to support the tail-heavy hypothesis and override the current flight's own index."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "They were on the same rotation, back to back, and both needed aft correction. Two in a row felt like it meant something about how the rotation was running that day, so I built in a forward shift before signing off, and honestly, with the time we had left, I didn't feel like there was room to dig into it further.",
          "evidence_explanation": "Demonstrates that a short sequence of prior events was treated as meaningful and used to justify the forward shift."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was fine—within the normal forward range with margin. The redistribution wasn't because my numbers were bad. It was more that seeing two prior aft trims made me not fully trust it, and I didn't have the minutes to sit with that discomfort.",
          "evidence_explanation": "Shows contradictory current-flight information was discounted after encountering the prior confirming examples."
        }
      ],
      "correction_or_counterevidence": "Later information revealed the two prior aft trims had unrelated causes: one fuel imbalance and one late catering load. The participant said he would have trusted his own numbers if he had known this. A cautious response to the ramp's tail-heavy report is a plausible non-bias alternative, but the participant explicitly attributed the shift to the two prior events and distrust of his own index.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label supported by retrieved aviation discussion of confirmation bias; the passage describes ignoring contradictory instrument-like evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "Similarly for flight Comair 5191 (2006) which took off from the incorrect runway in darkness and VMC conditions, the investigation found that the visual cues available to the crew induced a state of confirmation bias which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft’s position.",
          "mechanism_supported_by_source": "Confirmation bias can cause operators to overweigh cues consistent with their mental model and ignore contradictory instrument or index evidence.",
          "relevance_to_this_occurrence": "The participant treated prior aft trim events as confirming the rotation was tail-heavy and distrusted his own index, analogous to ignoring contradicting aircraft instruments."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis", "continuation bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final sign-off with a one-bag ramp tally discrepancy under slot pressure",
      "supporting_interview_quote": "I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself.",
      "plausible_mechanism": "The participant may have minimized a minor discrepancy because he was committed to preserving the departure slot, a form of plan continuation under time pressure.",
      "why_not_identified": "The transcript shows explicit deliberation about delay risk versus safety. The discrepancy was minor, routine, and ultimately did not affect weight and balance. There is insufficient affirmative evidence of a bias-specific mechanism rather than ordinary risk judgment."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on participant self-report after the event; recall may be reconstructed.",
    "The retrieved corpus is limited and not specifically about ground operations or load control, so its relevance is by analogy rather than direct task match.",
    "Time pressure and operational constraints are strong contextual factors; the analysis attempts to isolate bias-specific mechanisms but cannot rule out resource-rational tradeoffs.",
    "No objective benchmark or experimental condition was used; poor operational outcomes are not treated as evidence of bias by themselves."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just so you know, I'll ask you to walk through a specific turnaround and explain your thinking as it unfolded, not just what ended up happening. Can you tell me your role and a bit about your background? Participant: Sure. I've been a load controller about nine years, mostly narrow-body combi work. Normally I build the load sheet, issue the loading instruction to the ramp, check weight and balance against structural limits, and finalize the NOTOC for the captain. This one wasn't a normal turn, though—the inbound aircraft came in late, so instead of our usual 45 minutes on the ground, we were looking at more like 30 before the slot. Interviewer: How did that change things going in? Participant: Right away I knew I'd be compressing steps I'd normally spread out a bit more. Nothing about the flight itself was unusual—same route, same aircraft type—it was just less time to work with. Interviewer: Walk me through what happened. Participant: I got the cargo manifest with about 30 minutes left. Mixed load—regular bags, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what typically goes through, not palletized. Our load-control software generates an automatic load instruction, and it put that machinery item into hold 3. That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately. About fifteen minutes later, the ramp called and said the aircraft was sitting slightly tail-heavy—not out of limits, just aft of where you'd expect. Interviewer: What did you do with that? Participant: Logged it and kept going, because right then an LMC came in—about 380 kilos of mail plus six late bags that missed the original manifest. That mail got assigned to hold 5, our aft bulk hold. With the time we had left, I looked at the total weight, saw it was in line with the LMCs we'd been getting all week on this route—three similar ones, same range, none of those needed redistribution—and cleared it on that basis so I could move to the trim sheet. Interviewer: And the trim sheet itself? Participant: I pulled the dispatch log for a quick check, given the tail-heavy call from the ramp. Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required. Interviewer: Let's go through each of those moments in more detail. Starting with the ALI and the machinery item—what specifically told you it was fine to run with as generated? Participant: Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me. Interviewer: Was there a manual chart you could have checked against for that kind of cargo? Participant: There is, for exactly that situation. I know where it is. I just didn't reach for it that day. Interviewer: What would have made you stop and pull it? Participant: If we'd had the full 45, probably. Or if the system itself had thrown some kind of flag saying this needs manual sign-off. Neither of those happened, so I treated it like any other ALI. Interviewer: On the LMC—what exactly did you compare when the mail and bags came in? Participant: Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest. Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs went? Participant: No, not specifically. The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it. Interviewer: What would it have taken to run that calculation directly? Participant: A few extra minutes at the trim computer. It wasn't unavailable to me. I just didn't think it was worth the time against the schedule we were on. Interviewer: On the trim sheet redistribution—how did you connect the two previous flights to this one? Participant: They were on the same rotation, back to back, and both needed aft correction. Two in a row felt like it meant something about how the rotation was running that day, so I built in a forward shift before signing off, and honestly, with the time we had left, I didn't feel like there was room to dig into it further. Interviewer: What did your own calculated index for this flight show on its own? Participant: It was fine—within the normal forward range with margin. The redistribution wasn't because my numbers were bad. It was more that seeing two prior aft trims made me not fully trust it, and I didn't have the minutes to sit with that discomfort. Interviewer: Did you find out afterward why those two flights ran tail-heavy? Participant: Yeah—one was a fuel imbalance, the other had extra catering loaded late. Different tails, unrelated causes. Nothing tying them to each other or to this flight. Interviewer: Last one—the final sign-off. What was the situation? Participant: Closeout figures looked clean, within limits. But the ramp tally was one bag short of the NOTOC and manifest. Small discrepancy, and the slot was closing faster than a normal turn would allow. Interviewer: What did you decide, and what were you weighing? Participant: I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself. It turned out to be a manifest correction afterward—the weight and balance conclusion didn't change. I can see someone holding a couple minutes to chase it down instead. Neither call feels obviously wrong to me. Interviewer: How confident were you in each of these at the time, versus now? Participant: The ALI and the LMC, fairly confident in the moment, more than I'd be now looking back. The trim redistribution, less sure even then—it felt like caution more than certainty. The sign-off, I'm still not positive I made the better call, but I don't think it was unreasonable given the time. Interviewer: If you'd had the full 45 minutes instead of 30, would you have handled the machinery cargo differently? Participant: Probably, yes. I think I'd have pulled the manual chart. The shorter window is what pushed me to just trust the system's history instead. Interviewer: If the mail had gone to the usual forward hold instead of hold 5? Participant: Then the weight comparison would've actually held up fine, since placement wouldn't have mattered as much. It was the aft location that made that comparison misleading, not the comparison itself. Interviewer: If you'd known upfront the two prior tail-heavy events were unrelated, would you have redistributed the same way? Participant: No. I'd have trusted my own numbers for this flight instead of layering in a correction based on two other tails. Interviewer: Anything you'd do differently facing this same sequence again, under the same shortened window? Participant: Pull the manual chart for anything irregular no matter how tight the clock is, and keep this flight's numbers separate from what happened on previous ones unless I actually know there's a shared cause. The LMC piece I'd still have to think through—weight alone wasn't the full story that day, and less time made that easier to miss, not harder.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.84s · gen 240.79s · total 244.8s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0287 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0278 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0269 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0260 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0255 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0229 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
8. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0228 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0218 (rrf) — _# 1. Introduction th On the evening of 7 board was on final approach to runway 28 Right in San F_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0197 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0196 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0190 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
13. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0189 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 5. Discussion lower flying experience does not necessari it was found to affect highly experie_
15. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0181 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
16. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0178 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0177 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0176 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
19. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0175 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
20. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0172 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
22. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
23. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0169 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0166 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
28. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
29. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0161 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
30. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration et al., 1994; McGu_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0159 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
32. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0158 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration complacency? Three_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
34. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0154 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
35. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
36. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0154 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
37. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0153 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
38. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0153 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
40. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
41. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0149 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
42. **Hallihan_etal_DTM_12.pdf** — 0.0149 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
44. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0147 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
45. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
47. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
50. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed for affirmative, mechanism-specific cognitive bias occurrences; time pressure, operational constraints, and ordinary risk trade-offs were not classified as bias unless a distinct bias-specific mechanism was present."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "hot-hand fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "automation bias",
        "automation-induced complacency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "An automation-related bias in which an operator trusts the automated system enough to reduce or skip independent verification, even when task-specific cues warrant checking.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Issuing ALI with irregular machinery item as generated",
      "decision_point_description": "Participant accepted the software-generated ALI placing an irregular, heavier-than-usual machinery item into hold 3 without consulting the available manual chart.",
      "affected_reasoning_operation": "Verification of an automated load-planning recommendation",
      "bias_specific_mechanism": "The load-control system's long reliability generated high trust; when the participant noticed the cargo was irregular and unusual, that cue did not trigger the available manual verification, so the automated output was accepted as sufficient.",
      "manifestation_in_interview": "The participant explicitly noted the irregular, non-palletized, heavier item but issued the ALI as generated, citing system history and time pressure; he acknowledged he knew where the manual chart was but did not reach for it.",
      "effect_on_reasoning_or_decision": "The automated placement was not independently checked before issue; the ramp later reported an unexpectedly aft condition, though no out-of-limits condition was described for this specific decision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our load-control software generates an automatic load instruction, and it put that machinery item into hold 3. That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately.",
          "evidence_explanation": "Shows acceptance of automated output based on system reliability rather than independent verification of an unusual item."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me.",
          "evidence_explanation": "Demonstrates the mechanism: an anomalous cue triggered only a passing acknowledgment, not the available manual check, because of trust in the system plus time pressure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There is, for exactly that situation. I know where it is. I just didn't reach for it that day.",
          "evidence_explanation": "Confirms a situation-specific manual check was available and deliberately not used, consistent with automation complacency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If we'd had the full 45, probably. Or if the system itself had thrown some kind of flag saying this needs manual sign-off. Neither of those happened, so I treated it like any other ALI.",
          "evidence_explanation": "Reveals reliance on the automation to flag its own need for verification rather than initiating verification from task cues."
        }
      ],
      "correction_or_counterevidence": "No pre-decision correction occurred; the participant later said he would pull the manual chart for irregular cargo even under the short window.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman; Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Participants were provided independent access (via mouse click) to all relevant system information ... needed to verify the aid’s diagnoses. This procedure allowed the investigators to assess the level of operator complacency in interaction with the aid by contrasting the actual information sampling behavior of operators with a normative model of optimal behavior. According to this logic, any participant who accessed just the information appropriate to verify a given diagnosis before accepting it was regarded as showing noncomplacent (eutactic) behavior in interaction with the aid. However, participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "The passage defines complacency in automation use as sampling less information than necessary to verify an automated aid's recommendation.",
          "relevance_to_this_occurrence": "The participant had access to manual verification information but did not sample it, matching the source's operational definition of automation complacency."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which an initial value or prior reference point influences judgment, with adjustment away from that anchor insufficient for the current problem.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Clearing aft hold 5 LMC based on prior LMC total weights",
      "decision_point_description": "Participant cleared a last-minute change placing 380 kg of mail plus late bags into aft hold 5 without recalculating the index shift, because total weight resembled three recent LMCs that had gone into forward hold 2.",
      "affected_reasoning_operation": "Assessment of LMC-related load redistribution and weight-and-balance clearance",
      "bias_specific_mechanism": "The participant anchored on the total weight of recent LMCs, treating it as the decisive reference, and did not adjust for the different aft hold placement; the index shift for this specific placement was never run.",
      "manifestation_in_interview": "The participant explicitly compared total weight to prior LMCs, said that number was fastest to check, and acknowledged he did not look at hold 5 placement or run the index-shift calculation.",
      "effect_on_reasoning_or_decision": "The LMC was cleared on the basis of weight similarity alone; the participant later agreed the aft location made the comparison misleading, meaning the placement-specific balance effect was overlooked.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "With the time we had left, I looked at the total weight, saw it was in line with the LMCs we'd been getting all week on this route—three similar ones, same range, none of those needed redistribution—and cleared it on that basis so I could move to the trim sheet.",
          "evidence_explanation": "Shows acceptance based on similarity to recent LMC total weights rather than the current placement's balance effect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest.",
          "evidence_explanation": "Identifies the anchor explicitly as the readily available prior LMC total weight."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not specifically. The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it.",
          "evidence_explanation": "Demonstrates insufficient adjustment: the differing placement was noted but not incorporated into the calculation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the mail had gone to the usual forward hold instead of hold 5? Then the weight comparison would've actually held up fine, since placement wouldn't have mattered as much. It was the aft location that made that comparison misleading, not the comparison itself.",
          "evidence_explanation": "Confirms the critical missing variable was placement; the similarity-based comparison was misleading."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged weight alone was not the full story and that the aft placement made the comparison misleading.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The passage supports the idea that under time constraints people adjust insufficiently away from an initial reference point, consistent with anchoring-and-adjustment.",
          "relevance_to_this_occurrence": "The participant was anchored to prior LMC total weight and, under time pressure, did not sufficiently adjust for the new aft hold placement."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "hot-hand fallacy",
      "alternative_labels": [
        "belief in small numbers",
        "representativeness heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to infer that a short run of outcomes reflects a systematic underlying cause and will continue, even when the events are independent.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Forward redistribution based on two prior tail-heavy flights",
      "decision_point_description": "Participant shifted cargo forward beyond what the current flight's own index required after seeing that two prior flights on the rotation had needed aft trim correction.",
      "affected_reasoning_operation": "Assessment of whether the current flight required manual trim correction",
      "bias_specific_mechanism": "The participant treated two prior, unrelated aft-trim events as a meaningful pattern for the current rotation, overriding his own valid index with a forward correction.",
      "manifestation_in_interview": "The participant stated that 'two in a row felt like it meant something' about the rotation and that seeing the prior aft trims made him not fully trust his own numbers.",
      "effect_on_reasoning_or_decision": "An unnecessary forward redistribution was performed beyond what the index required; the participant later said he would not have done so if he had known the two prior events were unrelated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required.",
          "evidence_explanation": "Shows the causal leap from two prior events to a current rotation-level pattern, overriding the current flight's index."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Two in a row felt like it meant something about how the rotation was running that day, so I built in a forward shift before signing off, and honestly, with the time we had left, I didn't feel like there was room to dig into it further.",
          "evidence_explanation": "Explicitly describes the small-sample inference mechanism behind the redistribution."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was fine—within the normal forward range with margin. The redistribution wasn't because my numbers were bad. It was more that seeing two prior aft trims made me not fully trust it, and I didn't have the minutes to sit with that discomfort.",
          "evidence_explanation": "Shows that valid current-flight data were overridden by the two-prior-event pattern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. I'd have trusted my own numbers for this flight instead of layering in a correction based on two other tails.",
          "evidence_explanation": "Counterfactual confirms that the redistribution was caused by the prior tails rather than the current flight's data."
        }
      ],
      "correction_or_counterevidence": "Afterward, the participant learned the two prior tail-heavy events had unrelated causes—fuel imbalance and late catering—and said he would not have redistributed if he had known.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly supported hot-hand fallacy; this label is applied from established cognitive-science knowledge and is disclosed as not retrieval-grounded.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-there-itis",
        "normalization of deviance"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final sign-off with one-bag ramp tally discrepancy",
      "supporting_interview_quote": "I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself.",
      "plausible_mechanism": "Slot closure and plan-continuation momentum may have led to normalizing the one-bag discrepancy as routine rather than chasing it down.",
      "why_not_identified": "The participant explicitly weighed delay risk against discrepancy severity and later reported the discrepancy did not change weight-and-balance; no bias-specific mechanism is clearly evidenced beyond an ordinary time-pressured risk judgment."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus was sparse and did not provide direct support for hot-hand fallacy; that label is based on general cognitive-science knowledge.",
    "The transcript does not provide independent verification of the actual weight-and-balance consequences for every decision, though participant-reported outcomes were used where available.",
    "Time pressure is pervasive across the interview and was separated from bias mechanisms by requiring explicit evidence of a distinctive cognitive operation."
  ]
}

