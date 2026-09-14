# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. Just to confirm, this is a cognitive task analysis interview—I'll ask about a specific turnaround you handled, and I'd like you to walk me through your reasoning as it happened, not just the outcome. Nothing here is evaluative of your performance. Can you tell me your role and roughly how long you've been doing it? Participant: Sure. I'm a load controller, been doing it about nine years now, mostly narrow-body combi ops. On a normal day I'm building load sheets, issuing loading instructions to the ramp, checking weight and balance against structural limits, and making sure the NOTOC is accurate before the captain gets it. This particular one was a standard 45-minute turnaround, nothing scheduled to be unusual about it. Interviewer: Walk me through what happened, from when you first got involved. Participant: I got the initial cargo manifest about an hour before departure. Mixed load—regular baggage, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what we usually put through, not on a pallet. Our load-control software generates an automatic load instruction—the ALI—and it put that machinery item into hold 3. The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated so they could start loading, because we were already tight on time. About twenty minutes later, after the ramp had loaded per that instruction, they called up and said the aircraft was sitting slightly tail-heavy on the jacks reading—not out of limits, just noticeably aft of where we'd expect for that load. Interviewer: What did you do at that point? Participant: I logged it and kept moving, because we still had the last-minute change to deal with. About that time, an LMC came in—roughly 380 kilos of mail plus six late bags that hadn't made the original manifest. The mail got assigned to hold 5, which is our aft bulk hold, smaller one. I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route—we'd had three similar ones, same ballpark, and none of those needed any redistribution. So I cleared it on that basis and moved to finalize the trim sheet. Interviewer: And the trim sheet—what informed that? Participant: I pulled up the dispatch log because I wanted a sanity check before signing off, given the tail-heavy reading from the ramp. I saw that the two previous flights on this same rotation—different tail numbers, one had gone to a different destination—had both needed aft trim adjustments. That, plus what the ramp had just told me, made me think the rotation itself was running tail-heavy that day, so I shifted some of the cargo distribution forward before finalizing, beyond what my own computed index actually called for. Interviewer: Let's slow down and go through each of these moments individually. Starting with the ALI and the machinery item—what specifically told you it was fine to issue as generated? Participant: Mainly just experience with the system. It's been accurate for months on this fleet, and we don't have time in a 45-minute turn to hand-check every ALI. I did register that the item was irregular, non-palletized, heavier than usual—that did cross my mind—but the system's had a good run, so I went with it. Interviewer: Was there a manual limits chart you could have checked against for that item specifically? Participant: There is one, for exactly this kind of non-standard cargo. I know it exists. I just didn't pull it that time. Interviewer: What would have made you stop and check it? Participant: If the system itself had flagged it somehow—like if it had kicked back a warning saying 'verify manually,' I'd have stopped. Since it didn't, I treated it the same as any other ALI. Interviewer: Moving to the LMC decision—what exactly did you compare when the mail and bags came in? Participant: Total weight against the week's pattern. That's the number I had readily in my head from the previous LMCs. Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs had gone? Participant: Not specifically, no. The earlier ones went into a forward hold, I believe—hold 2 typically. This one went aft into 5. I didn't run the index shift for that specific placement; I just used the weight comparison as my check. Interviewer: What would it have taken to run that index calculation directly instead? Participant: A couple of extra minutes with the trim computer, honestly. It wasn't unavailable—I just didn't feel it was necessary given how the weight lined up. Interviewer: Let's talk about the trim sheet redistribution. What was your reasoning connecting the two previous flights to this one? Participant: They were on the same rotation, back to back, both needed aft correction. Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift as a margin before I signed off. Interviewer: At the time, what did your own calculated index for this flight actually show? Participant: It was within the normal range on its own, forward of the aft limit with margin. The redistribution wasn't because my numbers were bad—it was more that I didn't fully trust that after seeing two prior aft trims. Interviewer: Did you look into why those two prior flights ran tail-heavy? Participant: Not at the time. I found out afterward one was a fuel imbalance and the other had extra catering loaded late. Different tails, different causes, nothing tying them to each other. Interviewer: Last one—the final sign-off. What was the situation there? Participant: Closeout figures were within limits, looked clean. But the ramp tally was one bag short of what the NOTOC and manifest showed. Small discrepancy, and we were right up against the slot. Interviewer: What did you decide, and what were you weighing? Participant: I signed and released with the figures as they stood. I weighed the delay risk—losing the slot—against a one-bag discrepancy that's usually a clerical miscount, not a safety issue on its own. It resolved itself afterward as a manifest correction; the weight and balance conclusion didn't change. I could see someone making the other call too, holding a few minutes to chase it down. It wasn't an easy one either way. Interviewer: Looking back across the whole sequence, how confident were you in each of those calls at the time versus now? Participant: The ALI and the LMC I was fairly confident on in the moment—maybe more than I'd be now, knowing how it played out. The trim redistribution I was less sure about even then; it felt more like caution than certainty. The final sign-off, I'm still not fully sure I made the 'right' call, but I don't think it was wrong given what I had. Interviewer: If the software had required a manual check for irregular cargo shapes before finalizing the ALI, do you think that changes how this played out? Participant: Probably, yes. If it forced me to open the manual chart, I would have caught the hold 3 placement issue before the ramp ever loaded it. Interviewer: And if the mail had gone into the usual forward hold instead of hold 5? Participant: Then the weight comparison I used would have actually been a fair proxy, because placement wouldn't have mattered much. It was really the aft location that made the comparison misleading, not the comparison itself. Interviewer: If you'd known upfront that the two prior tail-heavy events had unrelated causes, would you have redistributed the cargo the same way? Participant: No, I don't think I would have. I'd have trusted my own numbers for this flight instead of layering in a correction based on what happened to two other tails. Interviewer: Anything you'd do differently if this exact sequence happened again? Participant: Pull the manual chart for anything irregular regardless of the system's history, and separate what the current flight's numbers say from what the last couple of flights did, unless I actually know there's a shared cause. The last-minute change is the one I'd still have to think about—weight alone clearly wasn't the full picture that day.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.28s · gen 206.12s · total 210.9s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0279 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0270 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0250 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0233 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0221 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0215 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0212 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
9. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0201 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0195 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
12. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0191 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
15. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0179 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
17. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0178 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
18. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0176 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0168 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0163 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
27. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0162 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0153 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION the same as theirs. However, participants may conclude ci_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
33. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0150 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration et al., 1994; McGu_
34. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0150 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
37. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
38. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0147 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
40. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0143 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
44. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
45. **Hallihan_etal_DTM_12.pdf** — 0.0141 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
49. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0138 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0137 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first evaluation of the participant's reported load-control reasoning across ALI issuance, LMC clearance, trim redistribution, and final sign-off. Three bias occurrences were identified; one had direct retrieved corpus support."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "illusory correlation",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "automation bias",
        "complacency",
        "over-trust in automation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient monitoring or verification of automation-generated recommendations because of over-trust in the automated system, leading to under-sampling of information needed to detect errors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Issuance of the automated load instruction for the irregular machinery item",
      "decision_point_description": "Whether to issue the ALI as generated or manually verify the placement of a heavy, irregular, non-palletized machinery item before ramp loading.",
      "affected_reasoning_operation": "Verification of an automation-generated load instruction against manual cargo limits",
      "bias_specific_mechanism": "The participant accepted the system-generated instruction based on the system's stable history, despite noticing cargo features that specifically triggered a manual-check requirement. The tendency to rely on automation output substituted for an independent verification step.",
      "manifestation_in_interview": "The participant explicitly noted the irregular, non-palletized, heavier-than-usual item, knew a manual chart existed for exactly that kind of cargo, but did not open it because the system had been reliable and did not issue a warning.",
      "effect_on_reasoning_or_decision": "The ALI was issued as generated, so the ramp loaded the irregular item into hold 3 before the participant re-examined the placement.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated so they could start loading, because we were already tight on time.",
          "evidence_explanation": "Shows acceptance of the automation output based on prior reliability rather than task-specific verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did register that the item was irregular, non-palletized, heavier than usual—that did cross my mind—but the system's had a good run, so I went with it.",
          "evidence_explanation": "Shows that diagnostic cues were detected but overridden by system trust, which is the core automation-complacency mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There is one, for exactly this kind of non-standard cargo. I know it exists. I just didn't pull it that time.",
          "evidence_explanation": "Confirms that a manual verification resource was available and deliberately unused for this non-standard cargo."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the system itself had flagged it somehow—like if it had kicked back a warning saying 'verify manually,' I'd have stopped. Since it didn't, I treated it the same as any other ALI.",
          "evidence_explanation": "Demonstrates automation-dependent monitoring: manual verification is triggered only by the automation, not by the participant's own recognition of unusual cargo."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction occurred before ramp loading. In retrospect, the participant acknowledged that a forced manual check would likely have caught the hold 3 placement issue before loading.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Parasuraman and Manzey passage directly operationalizes complacency in automation use as insufficient verification of automation-generated recommendations.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman and Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation's diagnosis before accepting it. Participants were provided independent access to all relevant system information needed to verify the aid's diagnoses. However, participants sampling less information than that necessary to completely verify the aid's recommendation were regarded as showing complacent behavior.",
          "mechanism_supported_by_source": "Complacency is operationalized as sampling less information than necessary to verify an automation-generated recommendation.",
          "relevance_to_this_occurrence": "The participant accepted the ALI as generated without opening the manual chart for irregular cargo, matching under-verification of automation output."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "recency effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge whether an event is acceptable, frequent, or representative by the ease with which similar instances come to mind, thereby overweighting recent or salient examples and underweighting other diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "LMC clearance for 380 kg of mail plus six late bags assigned to hold 5",
      "decision_point_description": "Whether the new last-minute load assignment required a trim/index recalculation and redistribution.",
      "affected_reasoning_operation": "Assessment of load-change impact on weight and balance",
      "bias_specific_mechanism": "Recent LMCs of similar total weight were easily recalled and used as the comparator, while the diagnostic feature of aft-hold placement was not retrieved or integrated. Availability of similar-weight examples substituted for a placement-specific index calculation.",
      "manifestation_in_interview": "The participant compared total weight against the week's pattern because that number was readily in his head, and explicitly did not examine where hold 5 sat or run the index shift for that specific placement.",
      "effect_on_reasoning_or_decision": "The participant cleared the LMC without redistribution, treating the total weight comparison as sufficient even though the aft placement made that comparison misleading.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route—we'd had three similar ones, same ballpark, and none of those needed any redistribution. So I cleared it on that basis and moved to finalize the trim sheet.",
          "evidence_explanation": "Shows judgment based on similar readily available prior instances rather than an analysis of the current load's placement."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Total weight against the week's pattern. That's the number I had readily in my head from the previous LMCs.",
          "evidence_explanation": "Directly identifies the ease-of-recall basis for the comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not specifically, no. The earlier ones went into a forward hold, I believe—hold 2 typically. This one went aft into 5. I didn't run the index shift for that specific placement; I just used the weight comparison as my check.",
          "evidence_explanation": "Shows omission of a diagnostic feature, hold placement, that differentiated the current LMC from the recalled prior examples."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that if the mail had gone into the usual forward hold, the weight comparison would have been a fair proxy, and that the aft location made the comparison misleading. Time pressure and prior benign LMCs are contextual factors, but the identified mechanism is the selective reliance on easily recalled weight comparisons without placement-specific checking.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly operationalizes the availability heuristic. Classification relies on established general cognitive-science knowledge. Retrieved passages mention related recency effects but were not used as direct corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "illusory correlation",
      "alternative_labels": [
        "clustering illusion",
        "representativeness heuristic",
        "belief in the law of small numbers"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to perceive a relationship or causal pattern between events that are independent or insufficiently supported, often by over-weighting small runs or salient co-occurrences.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Trim sheet redistribution based on two prior aft-trim events",
      "decision_point_description": "Whether to add forward redistribution beyond the current calculated index because two previous flights on the same rotation had required aft trim.",
      "affected_reasoning_operation": "Causal inference about the current flight's trim needs from two prior flights",
      "bias_specific_mechanism": "Two consecutive aft-trim events on the same rotation were treated as evidence of a shared trend, despite different tail numbers, different destinations, and no investigation of causal mechanisms. This small run overrode the current flight's own calculated index.",
      "manifestation_in_interview": "The participant said two in a row felt like enough to infer the rotation was trending tail-heavy and added forward margin, even though the current computed index was within normal range.",
      "effect_on_reasoning_or_decision": "The participant made a redistribution not called for by the current flight's own numbers, based on an inferred pattern that later turned out to be absent.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "They were on the same rotation, back to back, both needed aft correction. Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift as a margin before I signed off.",
          "evidence_explanation": "Shows causal inference from a very small run of events, the core of illusory correlation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was within the normal range on its own, forward of the aft limit with margin. The redistribution wasn't because my numbers were bad—it was more that I didn't fully trust that after seeing two prior aft trims.",
          "evidence_explanation": "Confirms that the current flight-specific data did not drive the decision; the prior two events did."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at the time. I found out afterward one was a fuel imbalance and the other had extra catering loaded late. Different tails, different causes, nothing tying them to each other.",
          "evidence_explanation": "Shows the perceived relationship between the two prior events was not supported by identifiable shared causes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, I don't think I would have. I'd have trusted my own numbers for this flight instead of layering in a correction based on what happened to two other tails.",
          "evidence_explanation": "Counterfactual statement indicates that knowledge of unrelated causes would have removed the bias-driven redistribution."
        }
      ],
      "correction_or_counterevidence": "The participant later learned the two prior aft-trim events had independent causes: one fuel imbalance and one late-loaded catering. No shared cause linked them to the current flight, and the participant stated he would not have redistributed had he known this at the time. A cautious safety margin is a plausible alternative motive, but the explicit 'two in a row felt like enough' statement and later counterfactual support the identified causal-inference distortion.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly operationalizes illusory correlation. Classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "normalcy bias",
        "confirmation bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final sign-off with one-bag ramp tally discrepancy",
      "supporting_interview_quote": "I signed and released with the figures as they stood. I weighed the delay risk—losing the slot—against a one-bag discrepancy that's usually a clerical miscount, not a safety issue on its own.",
      "plausible_mechanism": "A possible plan-continuation or normalcy effect in which the slot deadline and the past pattern of clerical miscounts led the participant to continue toward release despite an abnormal discrepancy.",
      "why_not_identified": "The transcript shows explicit weighing of delay risk against discrepancy severity, and the discrepancy was later resolved as a manifest correction without changing the weight and balance conclusion. This is more consistent with ordinary decision-making under time pressure and uncertainty than with an affirmative cognitive distortion."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is retrospective self-report; recall processes may introduce narrative coherence or hindsight effects that are not directly observable as real-time cognitive biases.",
    "Two of the three identified occurrences, availability heuristic and illusory correlation, lack direct retrieved corpus support and rely on established cognitive-science taxonomy.",
    "No objective operational outcome data or independent behavioral observation were available to verify the operational consequences of the identified reasoning patterns.",
    "The final sign-off discrepancy was considered but assigned candidate status because the participant's explicit risk weighing and the post-hoc clerical resolution made a bias classification unsupported."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. Just to confirm, this is a cognitive task analysis interview—I'll ask about a specific turnaround you handled, and I'd like you to walk me through your reasoning as it happened, not just the outcome. Nothing here is evaluative of your performance. Can you tell me your role and roughly how long you've been doing it? Participant: Sure. I'm a load controller, been doing it about nine years now, mostly narrow-body combi ops. On a normal day I'm building load sheets, issuing loading instructions to the ramp, checking weight and balance against structural limits, and making sure the NOTOC is accurate before the captain gets it. This particular one was a standard 45-minute turnaround, nothing scheduled to be unusual about it. Interviewer: Walk me through what happened, from when you first got involved. Participant: I got the initial cargo manifest about an hour before departure. Mixed load—regular baggage, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what we usually put through, not on a pallet. Our load-control software generates an automatic load instruction—the ALI—and it put that machinery item into hold 3. The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated so they could start loading, because we were already tight on time. About twenty minutes later, after the ramp had loaded per that instruction, they called up and said the aircraft was sitting slightly tail-heavy on the jacks reading—not out of limits, just noticeably aft of where we'd expect for that load. Interviewer: What did you do at that point? Participant: I logged it and kept moving, because we still had the last-minute change to deal with. About that time, an LMC came in—roughly 380 kilos of mail plus six late bags that hadn't made the original manifest. The mail got assigned to hold 5, which is our aft bulk hold, smaller one. I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route—we'd had three similar ones, same ballpark, and none of those needed any redistribution. So I cleared it on that basis and moved to finalize the trim sheet. Interviewer: And the trim sheet—what informed that? Participant: I pulled up the dispatch log because I wanted a sanity check before signing off, given the tail-heavy reading from the ramp. I saw that the two previous flights on this same rotation—different tail numbers, one had gone to a different destination—had both needed aft trim adjustments. That, plus what the ramp had just told me, made me think the rotation itself was running tail-heavy that day, so I shifted some of the cargo distribution forward before finalizing, beyond what my own computed index actually called for. Interviewer: Let's slow down and go through each of these moments individually. Starting with the ALI and the machinery item—what specifically told you it was fine to issue as generated? Participant: Mainly just experience with the system. It's been accurate for months on this fleet, and we don't have time in a 45-minute turn to hand-check every ALI. I did register that the item was irregular, non-palletized, heavier than usual—that did cross my mind—but the system's had a good run, so I went with it. Interviewer: Was there a manual limits chart you could have checked against for that item specifically? Participant: There is one, for exactly this kind of non-standard cargo. I know it exists. I just didn't pull it that time. Interviewer: What would have made you stop and check it? Participant: If the system itself had flagged it somehow—like if it had kicked back a warning saying 'verify manually,' I'd have stopped. Since it didn't, I treated it the same as any other ALI. Interviewer: Moving to the LMC decision—what exactly did you compare when the mail and bags came in? Participant: Total weight against the week's pattern. That's the number I had readily in my head from the previous LMCs. Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs had gone? Participant: Not specifically, no. The earlier ones went into a forward hold, I believe—hold 2 typically. This one went aft into 5. I didn't run the index shift for that specific placement; I just used the weight comparison as my check. Interviewer: What would it have taken to run that index calculation directly instead? Participant: A couple of extra minutes with the trim computer, honestly. It wasn't unavailable—I just didn't feel it was necessary given how the weight lined up. Interviewer: Let's talk about the trim sheet redistribution. What was your reasoning connecting the two previous flights to this one? Participant: They were on the same rotation, back to back, both needed aft correction. Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift as a margin before I signed off. Interviewer: At the time, what did your own calculated index for this flight actually show? Participant: It was within the normal range on its own, forward of the aft limit with margin. The redistribution wasn't because my numbers were bad—it was more that I didn't fully trust that after seeing two prior aft trims. Interviewer: Did you look into why those two prior flights ran tail-heavy? Participant: Not at the time. I found out afterward one was a fuel imbalance and the other had extra catering loaded late. Different tails, different causes, nothing tying them to each other. Interviewer: Last one—the final sign-off. What was the situation there? Participant: Closeout figures were within limits, looked clean. But the ramp tally was one bag short of what the NOTOC and manifest showed. Small discrepancy, and we were right up against the slot. Interviewer: What did you decide, and what were you weighing? Participant: I signed and released with the figures as they stood. I weighed the delay risk—losing the slot—against a one-bag discrepancy that's usually a clerical miscount, not a safety issue on its own. It resolved itself afterward as a manifest correction; the weight and balance conclusion didn't change. I could see someone making the other call too, holding a few minutes to chase it down. It wasn't an easy one either way. Interviewer: Looking back across the whole sequence, how confident were you in each of those calls at the time versus now? Participant: The ALI and the LMC I was fairly confident on in the moment—maybe more than I'd be now, knowing how it played out. The trim redistribution I was less sure about even then; it felt more like caution than certainty. The final sign-off, I'm still not fully sure I made the 'right' call, but I don't think it was wrong given what I had. Interviewer: If the software had required a manual check for irregular cargo shapes before finalizing the ALI, do you think that changes how this played out? Participant: Probably, yes. If it forced me to open the manual chart, I would have caught the hold 3 placement issue before the ramp ever loaded it. Interviewer: And if the mail had gone into the usual forward hold instead of hold 5? Participant: Then the weight comparison I used would have actually been a fair proxy, because placement wouldn't have mattered much. It was really the aft location that made the comparison misleading, not the comparison itself. Interviewer: If you'd known upfront that the two prior tail-heavy events had unrelated causes, would you have redistributed the cargo the same way? Participant: No, I don't think I would have. I'd have trusted my own numbers for this flight instead of layering in a correction based on what happened to two other tails. Interviewer: Anything you'd do differently if this exact sequence happened again? Participant: Pull the manual chart for anything irregular regardless of the system's history, and separate what the current flight's numbers say from what the last couple of flights did, unless I actually know there's a shared cause. The last-minute change is the one I'd still have to think about—weight alone clearly wasn't the full picture that day.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.28s · gen 187.45s · total 192.0s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0279 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0270 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0250 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0233 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0221 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0215 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0212 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
9. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0201 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0195 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
12. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0191 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
15. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0179 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
17. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0178 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
18. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0176 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0168 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0163 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
27. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0162 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0153 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION the same as theirs. However, participants may conclude ci_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
33. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0150 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration et al., 1994; McGu_
34. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0150 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
37. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
38. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0147 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
40. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0143 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
44. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
45. **Hallihan_etal_DTM_12.pdf** — 0.0141 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
49. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0138 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0137 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focuses on the Participant's reasoning during a 45-minute turnaround as a load controller. Only reasoning episodes with affirmative evidence of a bias-specific mechanism are reported."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "clustering illusion",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation bias",
      "alternative_labels": [
        "automation-induced complacency",
        "automation misuse"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to accept automated output as correct and to reduce verification of that output, especially when the automation has been historically reliable.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Issuing the automated load instruction for irregular machinery",
      "decision_point_description": "Whether to manually verify the automated load instruction for a non-standard heavy machinery item before issuing it to the ramp",
      "affected_reasoning_operation": "Verification and acceptance of automated system output",
      "bias_specific_mechanism": "The historically reliable automated load instruction system created a low perceived need to verify its output. The absence of an automation warning was treated as sufficient evidence of correctness, and a manual check was omitted even though the cargo was known to be irregular.",
      "manifestation_in_interview": "The Participant noticed that the machinery item was irregular, non-palletized, and heavier than usual, knew a manual limits chart existed, but issued the ALI as generated because the system had a history of being accurate and did not flag the item.",
      "effect_on_reasoning_or_decision": "The Participant did not consult the manual chart and issued the ALI to the ramp as generated. He later states that a forced manual check would have caught the hold 3 placement issue before loading.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our load-control software generates an automatic load instruction—the ALI—and it put that machinery item into hold 3. The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated so they could start loading, because we were already tight on time.",
          "evidence_explanation": "This quote links acceptance of the automated output to the system's long reliability and time pressure, showing reduced verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did register that the item was irregular, non-palletized, heavier than usual—that did cross my mind—but the system's had a good run, so I went with it.",
          "evidence_explanation": "The Participant had a relevant cue that should trigger manual verification, but overrode it because of the automation's track record."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the system itself had flagged it somehow—like if it had kicked back a warning saying 'verify manually,' I'd have stopped. Since it didn't, I treated it the same as any other ALI.",
          "evidence_explanation": "The absence of an automation warning was treated as evidence of correctness, showing delegation of verification to the automation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There is one, for exactly this kind of non-standard cargo. I know it exists. I just didn't pull it that time.",
          "evidence_explanation": "The Participant knew a specific manual check was available and relevant, but still did not use it."
        }
      ],
      "correction_or_counterevidence": "Time pressure and a historically reliable automated system are legitimate reasons for not checking every ALI. However, the known irregular cargo feature made manual verification specifically relevant. The Participant later acknowledged that a forced manual check would have caught the placement issue.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support was available for the mechanism of automation-related complacency: operators sampling less information than needed to verify automated recommendations.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "any participant who accessed just the information appropriate to verify a given diagnosis before accepting it was regarded as showing noncomplacent (eutactic) behavior in interaction with the aid. However, participants sampling less information than that necessary to completely verify the aid’s recommendation were... the commission errors in this group seem to be attributable to a sort of lookingbutnotseeing effect, analogous to what in other contexts has been referred to as 'inattentional blindness'... and which also has been suggested to underlie complacency effects in supervisory control tasks.",
          "mechanism_supported_by_source": "Complacent interaction with automation involves sampling less information than necessary to verify automated recommendations; errors can occur even when relevant cues are available.",
          "relevance_to_this_occurrence": "The Participant under-sampled manual verification for an irregular cargo item because the automated system had been reliable and gave no warning, matching the automation-related complacency pattern."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "representativeness heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to judge the likelihood or acceptability of a current event by how easily similar instances come to mind, rather than by analyzing the specific features of the current problem.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Clearing the last-minute change without redistribution",
      "decision_point_description": "Whether a 380 kg mail/bag last-minute change assigned to aft hold 5 required an index shift or redistribution before finalizing",
      "affected_reasoning_operation": "Judgment of whether the current last-minute change was comparable to prior last-minute changes",
      "bias_specific_mechanism": "The Participant substituted the harder question—does this aft hold placement change the trim index?—with an easily recalled comparison of total weights from three recent last-minute changes. Because the weights appeared similar, he inferred no redistribution was needed.",
      "manifestation_in_interview": "The Participant compared total weight against the week's pattern, had those prior LMC weights readily in mind, and did not examine hold 5 placement or run an index shift for that specific placement.",
      "effect_on_reasoning_or_decision": "He cleared the last-minute change based on an incomplete weight comparison. He later agrees that if the mail had gone into a forward hold, the comparison would have been a fair proxy, but the aft location made the comparison misleading.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route—we'd had three similar ones, same ballpark, and none of those needed any redistribution. So I cleared it on that basis and moved to finalize the trim sheet.",
          "evidence_explanation": "The Participant inferred safety from similarity to recent cases based on total weight, without analyzing placement-specific effects."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Total weight against the week's pattern. That's the number I had readily in my head from the previous LMCs.",
          "evidence_explanation": "The phrase 'readily in my head' shows availability of recent examples driving the comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not specifically, no. The earlier ones went into a forward hold, I believe—hold 2 typically. This one went aft into 5. I didn't run the index shift for that specific placement; I just used the weight comparison as my check.",
          "evidence_explanation": "This shows the relevant distinguishing feature, placement, was not analyzed."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was really the aft location that made the comparison misleading, not the comparison itself.",
          "evidence_explanation": "The Participant later identifies the neglected feature that made the easy comparison inadequate."
        }
      ],
      "correction_or_counterevidence": "Time pressure and the fact that prior similar-weight LMCs had required no redistribution make the quick weight check a plausible practical heuristic. The Participant himself notes that the aft placement made the comparison misleading.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; label drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "clustering illusion",
      "alternative_labels": [
        "belief in the law of small numbers",
        "illusory correlation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to perceive a meaningful pattern or trend in a very small number of independent events.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Redistributing cargo forward before final trim sheet",
      "decision_point_description": "Whether to add a forward cargo shift beyond the computed index based on two prior flights with aft trim adjustments and a current ramp reading",
      "affected_reasoning_operation": "Causal inference about whether prior flights' aft trim issues indicated a rotation-wide trend affecting the current flight",
      "bias_specific_mechanism": "Two independent prior aft-trim events were treated as a meaningful sequence indicating that the rotation was running tail-heavy that day. This perceived pattern led to a correction beyond what the current flight's own computed index required.",
      "manifestation_in_interview": "The Participant saw two previous flights on the same rotation had required aft trim and concluded the rotation itself was trending tail-heavy. He did not investigate the causes at the time and shifted cargo forward beyond his own calculated index.",
      "effect_on_reasoning_or_decision": "He made a forward cargo redistribution before sign-off that he later says he would not have made if he had known the two previous events had unrelated causes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I saw that the two previous flights on this same rotation—different tail numbers, one had gone to a different destination—had both needed aft trim adjustments. That, plus what the ramp had just told me, made me think the rotation itself was running tail-heavy that day, so I shifted some of the cargo distribution forward before finalizing, beyond what my own computed index actually called for.",
          "evidence_explanation": "The Participant inferred a rotation-level cause from two independent past events and acted beyond the current flight's own computed index."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift as a margin before I signed off.",
          "evidence_explanation": "This explicitly shows small-sample pattern perception as the basis for action."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was within the normal range on its own, forward of the aft limit with margin. The redistribution wasn't because my numbers were bad—it was more that I didn't fully trust that after seeing two prior aft trims.",
          "evidence_explanation": "The current flight's own data did not indicate a needed correction; distrust arose from the perceived trend in two prior flights."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, I don't think I would have. I'd have trusted my own numbers for this flight instead of layering in a correction based on what happened to two other tails.",
          "evidence_explanation": "The counterfactual confirms the influence of the perceived pattern from two prior flights."
        }
      ],
      "correction_or_counterevidence": "The current ramp reading of slight tail-heaviness provided some independent reason for caution, and a forward shift may have been conservative. However, the Participant's explicit reliance on two prior unrelated flights as a trend is the identified mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; label drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus provided direct support for automation-related complacency, but not for the availability heuristic or clustering illusion labels, which were drawn from general cognitive-science knowledge.",
    "The analysis is based on a single retrospective self-report interview, so recall and self-presentation may influence the described reasoning.",
    "No objective performance outcome was used; the findings identify bias-specific mechanisms in the reported reasoning, not necessarily error or harm."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. Just to confirm, this is a cognitive task analysis interview—I'll ask about a specific turnaround you handled, and I'd like you to walk me through your reasoning as it happened, not just the outcome. Nothing here is evaluative of your performance. Can you tell me your role and roughly how long you've been doing it? Participant: Sure. I'm a load controller, been doing it about nine years now, mostly narrow-body combi ops. On a normal day I'm building load sheets, issuing loading instructions to the ramp, checking weight and balance against structural limits, and making sure the NOTOC is accurate before the captain gets it. This particular one was a standard 45-minute turnaround, nothing scheduled to be unusual about it. Interviewer: Walk me through what happened, from when you first got involved. Participant: I got the initial cargo manifest about an hour before departure. Mixed load—regular baggage, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what we usually put through, not on a pallet. Our load-control software generates an automatic load instruction—the ALI—and it put that machinery item into hold 3. The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated so they could start loading, because we were already tight on time. About twenty minutes later, after the ramp had loaded per that instruction, they called up and said the aircraft was sitting slightly tail-heavy on the jacks reading—not out of limits, just noticeably aft of where we'd expect for that load. Interviewer: What did you do at that point? Participant: I logged it and kept moving, because we still had the last-minute change to deal with. About that time, an LMC came in—roughly 380 kilos of mail plus six late bags that hadn't made the original manifest. The mail got assigned to hold 5, which is our aft bulk hold, smaller one. I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route—we'd had three similar ones, same ballpark, and none of those needed any redistribution. So I cleared it on that basis and moved to finalize the trim sheet. Interviewer: And the trim sheet—what informed that? Participant: I pulled up the dispatch log because I wanted a sanity check before signing off, given the tail-heavy reading from the ramp. I saw that the two previous flights on this same rotation—different tail numbers, one had gone to a different destination—had both needed aft trim adjustments. That, plus what the ramp had just told me, made me think the rotation itself was running tail-heavy that day, so I shifted some of the cargo distribution forward before finalizing, beyond what my own computed index actually called for. Interviewer: Let's slow down and go through each of these moments individually. Starting with the ALI and the machinery item—what specifically told you it was fine to issue as generated? Participant: Mainly just experience with the system. It's been accurate for months on this fleet, and we don't have time in a 45-minute turn to hand-check every ALI. I did register that the item was irregular, non-palletized, heavier than usual—that did cross my mind—but the system's had a good run, so I went with it. Interviewer: Was there a manual limits chart you could have checked against for that item specifically? Participant: There is one, for exactly this kind of non-standard cargo. I know it exists. I just didn't pull it that time. Interviewer: What would have made you stop and check it? Participant: If the system itself had flagged it somehow—like if it had kicked back a warning saying 'verify manually,' I'd have stopped. Since it didn't, I treated it the same as any other ALI. Interviewer: Moving to the LMC decision—what exactly did you compare when the mail and bags came in? Participant: Total weight against the week's pattern. That's the number I had readily in my head from the previous LMCs. Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs had gone? Participant: Not specifically, no. The earlier ones went into a forward hold, I believe—hold 2 typically. This one went aft into 5. I didn't run the index shift for that specific placement; I just used the weight comparison as my check. Interviewer: What would it have taken to run that index calculation directly instead? Participant: A couple of extra minutes with the trim computer, honestly. It wasn't unavailable—I just didn't feel it was necessary given how the weight lined up. Interviewer: Let's talk about the trim sheet redistribution. What was your reasoning connecting the two previous flights to this one? Participant: They were on the same rotation, back to back, both needed aft correction. Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift as a margin before I signed off. Interviewer: At the time, what did your own calculated index for this flight actually show? Participant: It was within the normal range on its own, forward of the aft limit with margin. The redistribution wasn't because my numbers were bad—it was more that I didn't fully trust that after seeing two prior aft trims. Interviewer: Did you look into why those two prior flights ran tail-heavy? Participant: Not at the time. I found out afterward one was a fuel imbalance and the other had extra catering loaded late. Different tails, different causes, nothing tying them to each other. Interviewer: Last one—the final sign-off. What was the situation there? Participant: Closeout figures were within limits, looked clean. But the ramp tally was one bag short of what the NOTOC and manifest showed. Small discrepancy, and we were right up against the slot. Interviewer: What did you decide, and what were you weighing? Participant: I signed and released with the figures as they stood. I weighed the delay risk—losing the slot—against a one-bag discrepancy that's usually a clerical miscount, not a safety issue on its own. It resolved itself afterward as a manifest correction; the weight and balance conclusion didn't change. I could see someone making the other call too, holding a few minutes to chase it down. It wasn't an easy one either way. Interviewer: Looking back across the whole sequence, how confident were you in each of those calls at the time versus now? Participant: The ALI and the LMC I was fairly confident on in the moment—maybe more than I'd be now, knowing how it played out. The trim redistribution I was less sure about even then; it felt more like caution than certainty. The final sign-off, I'm still not fully sure I made the 'right' call, but I don't think it was wrong given what I had. Interviewer: If the software had required a manual check for irregular cargo shapes before finalizing the ALI, do you think that changes how this played out? Participant: Probably, yes. If it forced me to open the manual chart, I would have caught the hold 3 placement issue before the ramp ever loaded it. Interviewer: And if the mail had gone into the usual forward hold instead of hold 5? Participant: Then the weight comparison I used would have actually been a fair proxy, because placement wouldn't have mattered much. It was really the aft location that made the comparison misleading, not the comparison itself. Interviewer: If you'd known upfront that the two prior tail-heavy events had unrelated causes, would you have redistributed the cargo the same way? Participant: No, I don't think I would have. I'd have trusted my own numbers for this flight instead of layering in a correction based on what happened to two other tails. Interviewer: Anything you'd do differently if this exact sequence happened again? Participant: Pull the manual chart for anything irregular regardless of the system's history, and separate what the current flight's numbers say from what the last couple of flights did, unless I actually know there's a shared cause. The last-minute change is the one I'd still have to think about—weight alone clearly wasn't the full picture that day.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.01s · gen 208.66s · total 212.9s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0279 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0270 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0250 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0233 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0221 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0215 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
7. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0212 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
9. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0201 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0200 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0195 (rrf) — _# 2 23 | of flight AFL212 (2010), which took off from a taxiway instead of a runway in VMC | | |_
12. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0191 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
14. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 5. Discussion however there was nothing to suggest that single bias affecting the flight crew._
15. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0179 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
17. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0178 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
18. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0176 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
20. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
21. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0168 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0164 (rrf) — _# 3. Methodology 4.1 Introduction This chapter examines the different characteristics associated_
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0163 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0163 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
27. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0162 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
28. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
29. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0153 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION the same as theirs. However, participants may conclude ci_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Duley, Westerman, _
32. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _# 5. Discussion A study b y Boeing contributed to a total of four accidents (2022) attributing t_
33. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0150 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration et al., 1994; McGu_
34. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0150 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 2. Literature Review Caldwell (2012) suggesting th at an increase in fatigue leads to an accep_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
37. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0148 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
38. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0147 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
40. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0143 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0143 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
44. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0142 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
45. **Hallihan_etal_DTM_12.pdf** — 0.0141 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
46. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _## 16 5 H 0 : Confirmation bias occurs in proportion to phases of flight. Table 21 - Observed an_
49. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0138 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0137 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of one CTA interview transcript for affirmatively evidenced cognitive bias mechanisms only; no experimental condition or intended bias count assumed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "illusory correlation",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation bias",
      "alternative_labels": [
        "automation-induced complacency",
        "overreliance on automation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Automation bias is the tendency to accept automated output as correct and fail to seek or use manual verification, especially when the automation has a history of reliability.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Issuing the automatic load instruction for the irregular machinery item",
      "decision_point_description": "Decision to issue the ALI as generated, without consulting the available manual limits chart for non-standard cargo.",
      "affected_reasoning_operation": "Verification of automated load-planning output against manual limits for irregular cargo",
      "bias_specific_mechanism": "Overtrust in the load-control software due to its long history of reliable performance, leading to reduced manual verification despite noticing that the item was irregular, non-palletized, and heavier than usual.",
      "manifestation_in_interview": "The participant accepted the software-generated hold 3 placement even though the cargo was unusual and a manual limits chart existed for exactly that kind of non-standard cargo.",
      "effect_on_reasoning_or_decision": "The irregular machinery item was loaded into hold 3 without manual verification, bypassing a check that the participant later said would have caught the hold 3 placement issue before ramp loading.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our load-control software generates an automatic load instruction—the ALI—and it put that machinery item into hold 3. The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated so they could start loading, because we were already tight on time.",
          "evidence_explanation": "This explicitly shows reliance on the automation's historical reliability as the reason for accepting its output without manual verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did register that the item was irregular, non-palletized, heavier than usual—that did cross my mind—but the system's had a good run, so I went with it.",
          "evidence_explanation": "This demonstrates that the relevant contrary cue was noticed, but was overridden by trust in the automated system."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There is one, for exactly this kind of non-standard cargo. I know it exists. I just didn't pull it that time.",
          "evidence_explanation": "This confirms that a manual check was available and known to the participant, but was not used."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the system itself had flagged it somehow—like if it had kicked back a warning saying 'verify manually,' I'd have stopped. Since it didn't, I treated it the same as any other ALI.",
          "evidence_explanation": "This shows that the absence of an automation prompt was treated as sufficient reason not to verify manually, a hallmark of automation bias."
        }
      ],
      "correction_or_counterevidence": "No in-the-moment correction occurred; later in the interview the participant acknowledged that a software-required manual check would likely have caught the hold 3 placement issue before loading.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Parasuraman and Manzey passage directly addresses automation complacency and reduced verification of automated recommendations.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": "2010",
          "retrieved_passage_or_finding": "This procedure allowed the investigators to assess the level of operator complacency in interaction with the aid by contrasting the actual information sampling behavior of operators with a \"normative model\" of optimal behavior. According to this logic, any participant who accessed just the information appropriate to verify a given diagnosis before accepting it was regarded as showing noncomplacent (eutactic) behavior in interaction with the aid. However, participants sampling less information than that necessary to completely verify the aid's recommendation were...",
          "mechanism_supported_by_source": "The source defines automation-related complacency as reduced verification of automated output relative to a normative standard. The participant's failure to check the manual chart reflects this reduced information sampling after encountering automated guidance.",
          "relevance_to_this_occurrence": "The participant accepted the ALI without using the available manual chart for irregular cargo, even though he noticed atypical cargo characteristics; the retrieved passage supports interpreting this as automation-related complacency or overreliance."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "retrieval fluency heuristic",
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Availability heuristic is the tendency to judge the likelihood, significance, or safety of an event based on how easily similar instances come to mind rather than on a full analysis of the current situation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Clearing the last-minute change assigned to aft hold 5",
      "decision_point_description": "Decision to clear the last-minute change based on total weight similarity to recent LMCs, without checking the placement-specific index shift.",
      "affected_reasoning_operation": "Assessing whether the last-minute cargo change required redistribution or trim correction",
      "bias_specific_mechanism": "The participant relied on easily recalled recent LMC weights from the same week and treated them as a sufficient comparison, substituting memory availability for a placement-specific index calculation.",
      "manifestation_in_interview": "The participant compared the current LMC total weight to three earlier similar-weight LMCs and cleared it, even though the current cargo was assigned to an aft hold while the earlier LMCs went to a forward hold.",
      "effect_on_reasoning_or_decision": "The LMC was cleared without detecting that aft placement made the weight-based comparison misleading, so a potentially important trim or redistribution check was skipped.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The mail got assigned to hold 5, which is our aft bulk hold, smaller one. I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route—we'd had three similar ones, same ballpark, and none of those needed any redistribution. So I cleared it on that basis and moved to finalize the trim sheet.",
          "evidence_explanation": "This shows the participant used the recent similar-weight LMCs as the benchmark for the current decision rather than computing the current placement-specific effect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Total weight against the week's pattern. That's the number I had readily in my head from the previous LMCs.",
          "evidence_explanation": "This explicitly indicates that easily recalled prior instances were the basis of the comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not specifically, no. The earlier ones went into a forward hold, I believe—hold 2 typically. This one went aft into 5. I didn't run the index shift for that specific placement; I just used the weight comparison as my check.",
          "evidence_explanation": "This confirms that the available information about placement was not incorporated into the reasoning, even though it was relevant."
        }
      ],
      "correction_or_counterevidence": "Later in the interview the participant acknowledged that the aft location made the weight comparison misleading and that weight alone was not the full picture.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed availability heuristic or retrieval fluency; the label is applied from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "illusory correlation",
      "alternative_labels": [
        "clustering illusion",
        "insensitivity to sample size"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Illusory correlation is the perception of a relationship between variables when no systematic relationship exists, often based on a small or unrepresentative set of co-occurring events.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Trim sheet redistribution based on two prior tail-heavy flights",
      "decision_point_description": "Decision to shift cargo forward beyond the computed index because two prior flights on the rotation had needed aft trim adjustment.",
      "affected_reasoning_operation": "Causal inference about the current aircraft's balance and load distribution",
      "bias_specific_mechanism": "The participant perceived a stable rotation-level tail-heavy trend from two independent events and treated that perceived trend as more meaningful than the current flight's own calculated index.",
      "manifestation_in_interview": "After seeing two previous flights on the same rotation need aft trim adjustments, the participant concluded the rotation itself was running tail-heavy and applied a forward cargo shift despite his own current-flight index being within normal limits.",
      "effect_on_reasoning_or_decision": "The participant redistributed cargo beyond what the current-flight calculation required, layering in a correction based on two unrelated prior flights rather than on the current aircraft's numbers.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I saw that the two previous flights on this same rotation—different tail numbers, one had gone to a different destination—had both needed aft trim adjustments. That, plus what the ramp had just told me, made me think the rotation itself was running tail-heavy that day, so I shifted some of the cargo distribution forward before finalizing, beyond what my own computed index actually called for.",
          "evidence_explanation": "This demonstrates the inference of a rotation-level trend from only two prior flights, despite notable differences such as tail number and destination."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift as a margin before I signed off.",
          "evidence_explanation": "This explicitly shows that a very small sample of two events was treated as sufficient evidence of a stable pattern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was within the normal range on its own, forward of the aft limit with margin. The redistribution wasn't because my numbers were bad—it was more that I didn't fully trust that after seeing two prior aft trims.",
          "evidence_explanation": "This confirms that the participant's own current-flight calculation did not support the adjustment, isolating the prior two events as the causal driver."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at the time. I found out afterward one was a fuel imbalance and the other had extra catering loaded late. Different tails, different causes, nothing tying them to each other.",
          "evidence_explanation": "This shows the perceived correlation was later disconfirmed, supporting that the two prior events were independent rather than rotation-level trend evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, I don't think I would have. I'd have trusted my own numbers for this flight instead of layering in a correction based on what happened to two other tails.",
          "evidence_explanation": "This counterfactual statement demonstrates that the biased inference from the two prior flights directly influenced the redistribution decision."
        }
      ],
      "correction_or_counterevidence": "The participant later learned that the two prior tail-heavy events had unrelated causes, and said he would not have redistributed the same way if he had known that at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addressed illusory correlation or clustering illusion; the label is applied from established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Single retrospective CTA transcript; self-reports may be affected by memory reconstruction and are not independent of hindsight.",
    "RAG context provided direct support for automation complacency but not for availability heuristic or illusory correlation.",
    "No experimental condition or ground truth was used to establish whether the final outcomes were incorrect; classifications rely on reported reasoning processes rather than outcomes."
  ]
}

