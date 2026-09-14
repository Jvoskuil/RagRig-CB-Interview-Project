# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the LumenKit evaluation, not whether the outcome was 'right.' Everything you share stays in the design systems research archive. Sound okay? Participant: Sounds good. Happy to walk through it — it's still fresh, honestly. Interviewer: Great. Can you remind me of your role and what triggered this whole evaluation? Participant: I lead design systems for the platform org — three designers, two engineers under me. Legal flagged that we needed to hit WCAG 2.2 AA across two customer-facing squads within about ten weeks, and our internal component library had known contrast and focus-state debt we hadn't prioritized. LumenKit came up because a couple of competitors use it and it's picked up some industry recognition. Interviewer: What was your goal going into the vendor demo? Participant: Mainly to see if we could shortcut months of remediation work by adopting something pre-built and compliant, given the clock we were on. Interviewer: Walk me through what happened, in order. Participant: The solutions engineer ran maybe forty minutes, almost all of it on their accordion component — the motion, the keyboard handling, the way it degraded gracefully. It was genuinely impressive, smoother than anything we'd built in-house. They mentioned the whole library ships with AA-compliant color defaults. After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down. We got a three-week sandbox with a limited component set, and both squad leads said they were interested but needed pricing before committing engineering time. Interviewer: Did you look closely at the color and elevation tokens before making that call? Participant: Not directly, no — we hadn't run our own contrast checks yet. But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape. That assumption is part of why I pushed for the broad pilot instead of testing component by component first. Interviewer: Let's move to the licensing decision. What did that look like? Participant: Procurement needed a tier recommendation within two weeks. Vendor offered three: Basic, five components, no support; Team, twelve components with limited support, priced not far below Enterprise; and Enterprise, the full library with dedicated support. I recommended Enterprise. Interviewer: What made Enterprise the clear choice? Participant: Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation — it was more that comparing the three side by side made Enterprise the only one that made sense. Interviewer: And the rollout timeline — how was that set? Participant: I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads. Interviewer: Had the two dependent squads confirmed they could hit a four-week window? Participant: Not formally, no. I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars. One of them came back shortly after saying their calendar genuinely couldn't accommodate that window — they had an unrelated release freeze I hadn't accounted for. Interviewer: What information would have changed your timeline call, looking back? Participant: Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first. Interviewer: Let's get to the audit. What came back? Participant: About seven weeks in, our internal accessibility audit found that several of LumenKit's color and elevation tokens failed contrast ratio requirements in three of five tested components. That was awkward, because I'd already told the VP and both squad leads that LumenKit would solve most of our contrast problems out of the box. Interviewer: What was your first read on that discrepancy? Participant: My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance. Part of why that explanation felt like the natural one to reach for first was that I'd already told the VP and both squad leads LumenKit would solve most of our contrast problems out of the box, so 'it's our theming, not their tokens' sat better with what I'd already said than the alternative did. I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities. Interviewer: What did you decide to do next? Participant: We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy. The legacy components already had remediated contrast values for those same screens, so that was sitting right there as an option. Interviewer: What made continuing the more attractive path versus reverting? Participant: Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked. Interviewer: Did the VP or squad leads react? Participant: The VP wanted a written explanation for the compliance file. One squad lead quietly reverted their branch back to the legacy component for the affected screens without waiting on my decision. Interviewer: That brings us to the final call. What were the options three weeks before the deadline? Participant: Expand LumenKit org-wide as we'd implemented it, adopt a hybrid — keep LumenKit's motion and layout components but source color and elevation tokens internally — or revert fully to legacy. Interviewer: How did the hybrid option evaluate against the others? Participant: On paper it addressed the token problem directly without throwing away the layout and motion integration work we'd already done. It was arguably the cleanest fix. Interviewer: So what did you recommend? Participant: I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup. Even with the hybrid's technical case being reasonably strong, sticking with what we already had running felt like the safer, known quantity this close to the deadline — everyone on both squads already understood how the current setup behaved, and that familiarity mattered more to me in the moment than moving to an arrangement that was objectively cleaner but still new to the team. Interviewer: If the audit had surfaced in week one instead of week seven, do you think that would have changed how you weighed the hours already spent? Participant: Probably — with less invested, reverting or pivoting to the hybrid would've felt like a much smaller loss. Interviewer: If the vendor demo had opened with contrast-ratio data instead of the accordion, would your initial pilot decision have gone differently? Participant: Possibly. If I'd seen the token-level numbers first, I might've scoped the pilot narrower before committing broadly. Interviewer: If procurement had only offered two tiers instead of three, would Enterprise still have been the obvious pick? Participant: Harder to say — I might have actually priced out Enterprise against our real component needs rather than against Team. Interviewer: Last one — starting over today, what would you keep, and what would you change? Participant: I'd keep the urgency and the willingness to bring in outside tooling under deadline pressure — that part was right. I'd change how early I locked in public commitments about what the library would solve, and I'd get squad confirmation on timelines before setting them rather than after. Interviewer: This has been really useful. Thanks for being so candid about the reasoning, not just the outcome. Participant: No problem — it's easier to see it laid out like this than it was living through it week to week.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.22s · gen 189.90s · total 194.7s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0275 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0234 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Hallihan_etal_DTM_12.pdf** — 0.0233 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0224 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
5. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0214 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
6. **Hallihan_etal_DTM_12.pdf** — 0.0212 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0207 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **Hallihan_etal_DTM_12.pdf** — 0.0203 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
9. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0194 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
10. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0194 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0178 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0174 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
13. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0172 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
14. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0172 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
15. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0171 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0168 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0167 (rrf) — _# ( " = 0 . 44 ) . Proc. ACM Hum.-Comput. Interact., Vol. 5, No. CSCW1, Article 188. Publication_
18. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0167 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs 1 Google Scholar(assessment done on Mar_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0166 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
20. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
21. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
22. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
23. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
24. **Hallihan_etal_DTM_12.pdf** — 0.0163 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0161 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0160 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
27. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0160 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
28. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0157 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
29. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0157 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs decisionmaking scenarios. We confirm ea_
30. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0157 (rrf) — _ligence analysis, evaluating visualizations thatthe task environment (e.g., Klayman & Ha, 1987; _
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
32. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0156 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
33. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
34. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0155 (rrf) — _# 4.2 Answering our RQs AI & SOCIETY the AI’s recommendation, provided as a second opinion, alig_
35. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0154 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
36. **Lyell Automation bias and verification complexity.pdf** — 0.0153 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
37. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
38. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0152 (rrf) — _## 1Introduction RQ3: Can explainability or transparency mitigate automation bias? RQ4: Is AI li_
39. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0152 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
40. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0152 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs opinions when presented with new eviden_
41. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0149 (rrf) — _# Cognitive Biases in Technical Communication The Sun k Cost Fallacy refers to t decisions that _
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
43. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study anchor. Anchoring bias is_
44. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0145 (rrf) — _motivation in mediating the eectiveness of XAI solutions. Therefore, beyond optimizing explanati_
45. **Hallihan_etal_DTM_12.pdf** — 0.0144 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
46. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0143 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study In the context of artifac_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
48. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0141 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0139 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
50. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0138 (rrf) — _# 188 To Trust or to Think on the AI compared to the simple explainable AI approaches. However, _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the interview transcript for affirmative evidence of cognitive biases in the participant's reasoning about LumenKit evaluation, vendor selection, timeline, audit interpretation, remediation, and final recommendation. Retrieved passages were used for mechanistic and terminological support where available."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "planning fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status quo bias",
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
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "anchoring effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which an initial value, impression, or starting point exerts disproportionate influence on subsequent judgments, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial pilot scope decision after vendor demo",
      "decision_point_description": "Whether to pilot the full LumenKit token set across both squads or run a narrower component-by-component test.",
      "affected_reasoning_operation": "Inference about the quality of the token layer and overall library, and the resulting scope decision",
      "bias_specific_mechanism": "The impressive accordion demo and industry recognition served as a strong initial positive anchor; the participant insufficiently adjusted this global quality impression when reasoning about the unverified color and elevation token layer before deciding to pilot broadly.",
      "manifestation_in_interview": "The participant stated they had not directly examined the color and elevation tokens or run contrast checks, yet inferred the token layer was probably similarly good because the accordion was well executed and competitors use LumenKit.",
      "effect_on_reasoning_or_decision": "The participant recommended a broad pilot of the full token set rather than a narrower component-by-component test, committing the organization more widely before token-level compliance was verified.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly, no — we hadn't run our own contrast checks yet. But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape. That assumption is part of why I pushed for the broad pilot instead of testing component by component first.",
          "evidence_explanation": "This quote shows an inference from a salient positive feature to an untested attribute, without direct evidence. That pattern is consistent with anchoring-and-adjustment: the initial positive impression was not sufficiently adjusted by token-specific uncertainty."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down.",
          "evidence_explanation": "This shows the operational consequence of the anchored inference: a broad commitment was made rather than a narrower test."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly. If I'd seen the token-level numbers first, I might've scoped the pilot narrower before committing broadly.",
          "evidence_explanation": "This counterfactual indicates that the order and initial anchor of the demonstration materially influenced the pilot scoping decision."
        }
      ],
      "correction_or_counterevidence": "There is a plausible non-bias explanation that relying on vendor claims and competitor adoption is ordinary inductive inference under time pressure. However, the participant explicitly identified the assumption as driving the broad pilot, and the counterfactual about seeing token-level data first supports an anchoring distortion.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Rastogi et al. supports anchoring bias and the anchoring-and-adjustment heuristic as a mechanism in decision-making, though not specifically in vendor demo evaluation.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Conclusions. In this work, we foreground the role of cognitive biases in the human-AI collaborative decisionmaking setting. Through literature in cognitive science and psychology, we explore several biases and present mathematical models of their eect on collaborative decisionmaking. We focus on anchoring bias and the associated anchoringandadjustment heuristic that is important towards optimizing team performance.",
          "mechanism_supported_by_source": "The source identifies anchoring bias and the associated anchoring-and-adjustment heuristic as a recognized cognitive mechanism in decision-making.",
          "relevance_to_this_occurrence": "The occurrence involves an initial positive vendor demonstration acting as an anchor, with insufficient adjustment before a broad commitment. The source validates anchoring-and-adjustment as a relevant bias mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "reference dependence",
        "contrast effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which an initial value, option set, or reference point exerts disproportionate influence on subsequent judgment, with insufficient adjustment to external benchmarks or absolute value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Procurement tier recommendation",
      "decision_point_description": "Selecting among Basic, Team, and Enterprise LumenKit licensing tiers and making a procurement recommendation within two weeks.",
      "affected_reasoning_operation": "Evaluation of pricing options and value relative to organizational component needs and external alternatives",
      "bias_specific_mechanism": "The vendor-presented three-tier structure, especially the unattractive Team price-point, served as an option-set anchor. The participant adjusted within this presented set by comparing Team to Enterprise, rather than independently benchmarking Enterprise against actual component needs or a scoped custom build.",
      "manifestation_in_interview": "The participant explicitly stated that Enterprise looked obviously better next to Team, and that they did not run Enterprise's cost against a custom build or actual component needs in isolation.",
      "effect_on_reasoning_or_decision": "Enterprise was recommended as the full-library tier without a direct cost-benefit comparison to the organization's real needs or non-vendor alternatives.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation — it was more that comparing the three side by side made Enterprise the only one that made sense.",
          "evidence_explanation": "This shows the decision was governed by relative comparison within the provided tier set rather than independent evaluation of absolute value or organizational needs, a hallmark of an anchoring/reference-point distortion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Harder to say — I might have actually priced out Enterprise against our real component needs rather than against Team.",
          "evidence_explanation": "The participant's counterfactual indicates that the presence of the third tier changed the evaluation frame, strengthening the interpretation that the vendor-provided option set anchored the analysis."
        }
      ],
      "correction_or_counterevidence": "Some relative comparison is rational in purchasing decisions, and Enterprise may genuinely have been a better value than Team. However, the participant acknowledged failing to evaluate against actual needs and indicated that fewer tiers would have changed the comparison process.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Rastogi et al. supports anchoring-and-adjustment generally; the retrieved passage does not specifically cover pricing-tier contrast effects.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Conclusions. In this work, we foreground the role of cognitive biases in the human-AI collaborative decisionmaking setting. Through literature in cognitive science and psychology, we explore several biases and present mathematical models of their eect on collaborative decisionmaking. We focus on anchoring bias and the associated anchoringandadjustment heuristic that is important towards optimizing team performance.",
          "mechanism_supported_by_source": "The source validates anchoring bias and insufficient adjustment as a decision-making mechanism.",
          "relevance_to_this_occurrence": "The participant's licensing evaluation was anchored by the vendor-provided tier structure and insufficiently adjusted to external reference points, consistent with the broad anchoring mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "planning fallacy",
      "alternative_labels": [
        "optimism bias",
        "overconfidence effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A forecasting bias in which individuals underestimate the time, costs, and risks of future actions while overestimating the likelihood of successful completion, often by focusing on an optimistic inside view rather than distributional or base-rate information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Rollout timeline setting",
      "decision_point_description": "Setting a four-week integration timeline and communicating it to the dependent squads without formal feasibility confirmation.",
      "affected_reasoning_operation": "Time estimation and resource/capacity judgment",
      "bias_specific_mechanism": "The participant adopted an optimistic inside view centered on personal daily involvement and the desired deadline, underestimating external scheduling constraints and failing to gather base-rate or calendrical information before committing to the timeline.",
      "manifestation_in_interview": "The participant set an aggressive four-week timeline, assumed hands-on management would overcome unknown existing release calendars, and later acknowledged that they asked squads to work toward the date rather than asking whether the date was feasible.",
      "effect_on_reasoning_or_decision": "The timeline proved infeasible for at least one squad, which reported an unrelated release freeze that had not been accounted for.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads.",
          "evidence_explanation": "This shows an optimistic, inside-view plan focused on personal involvement rather than an evidence-based assessment of squad capacity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not formally, no. I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars.",
          "evidence_explanation": "This is an explicit statement of overconfident forecasting: the participant assumed close management would overcome unknown and unexamined constraint information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first.",
          "evidence_explanation": "The participant identifies the failure to solicit base-rate feasibility information before committing to the plan, which is characteristic of the planning fallacy."
        }
      ],
      "correction_or_counterevidence": "This could partly be explained by missing scheduling information and ordinary decision-making under uncertainty. However, the explicit assumption that personal involvement would overcome unknown calendars, together with the later identified failure to ask about feasibility, supports a low-confidence planning fallacy classification.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided RAG context directly addresses the planning fallacy; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "motivated reasoning",
        "confirmatory bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's pre-existing beliefs, expectations, or prior public commitments, while insufficiently considering disconfirmatory evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of audit findings on color and elevation token failures",
      "decision_point_description": "Determining whether the audit failures reflected theming integration issues or non-compliant library tokens.",
      "affected_reasoning_operation": "Hypothesis evaluation and causal attribution of contradictory evidence",
      "bias_specific_mechanism": "The participant favored the explanation that the theming layer caused the failures because it was consistent with his prior public commitment that LumenKit would solve contrast problems. He did not request an independent re-test that could disconfirm the library-token explanation.",
      "manifestation_in_interview": "Upon learning the audit results, the participant's first interpretation was that these were implementation-specific edge cases, and he explicitly linked that interpretation to the fact that it sat better with what he had already told the VP and squad leads.",
      "effect_on_reasoning_or_decision": "The participant avoided an independent disconfirmatory test, potentially delaying recognition that vendor tokens themselves might be non-compliant.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance. Part of why that explanation felt like the natural one to reach for first was that I'd already told the VP and both squad leads LumenKit would solve most of our contrast problems out of the box, so 'it's our theming, not their tokens' sat better with what I'd already said than the alternative did. I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities.",
          "evidence_explanation": "This directly ties the preferred hypothesis to prior commitment and shows an absence of disconfirmatory testing, matching the core mechanism of confirmation bias."
        }
      ],
      "correction_or_counterevidence": "The vendor's documentation and the possibility of a theming interaction provided some legitimate technical basis for the initial interpretation. However, the participant's own stated reason was that the explanation aligned with prior statements, and no independent re-test was conducted.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Hallihan et al. provides direct support for confirmation bias leading designers to discount contradictory information and under-attend to disconfirmatory evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Results of this analysis led us to conclude that confirmation bias can lead designers to: • Ignore o r discount factual contradictory information",
          "mechanism_supported_by_source": "Confirmation bias can cause discounting or ignoring of contradictory information and insufficient attention to disconfirming evidence.",
          "relevance_to_this_occurrence": "The participant discounted the possibility that the library tokens were non-compliant and avoided disconfirmatory re-testing, consistent with this mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which irrecoverable prior investments in time, money, or effort are weighed in decisions about continuing a course of action, rather than evaluating only future costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Remediation decision after audit token failures",
      "decision_point_description": "Whether to continue refining the customized LumenKit tokens, pause, or fall back to legacy components after the audit identified contrast failures.",
      "affected_reasoning_operation": "Decision to continue versus switch after negative evidence",
      "bias_specific_mechanism": "The 40+ engineering hours already spent customizing tokens were treated as a reason to keep refining rather than as a sunk cost irrelevant to future choice. The prospect of writing off those hours increased commitment to the problematic path.",
      "manifestation_in_interview": "The participant decided to keep refining rather than reverting to legacy, partly because reverting would mean writing off hours already invested. They explicitly said it felt more efficient to push through than start over.",
      "effect_on_reasoning_or_decision": "Resources continued to be directed toward the problematic implementation despite the availability of legacy components with already remediated contrast values.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy.",
          "evidence_explanation": "Prior investment is explicitly used to justify continuation, which is the central sunk cost mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked.",
          "evidence_explanation": "The participant frames irrecoverable hours as a loss to avoid, influencing the continuation decision rather than comparing future costs and benefits of continuing versus reverting."
        }
      ],
      "correction_or_counterevidence": "Continuing refinement could also be justified if remaining fixes were expected to be cheaper than reverting. However, the participant's stated reasoning emphasized avoiding the write-off of past hours, which is the signature of sunk cost reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided RAG context directly addresses sunk cost fallacy or escalation of commitment; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "status quo bias",
      "alternative_labels": [
        "familiarity bias",
        "status quo preference"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A preference for the current state of affairs or existing arrangement, in which the disadvantages of change are overweighted relative to its benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final pre-deadline recommendation among expand, hybrid, or revert",
      "decision_point_description": "Three weeks before deadline, selecting whether to expand LumenKit as implemented, adopt a hybrid with internally sourced color and elevation tokens, or fully revert to legacy.",
      "affected_reasoning_operation": "Evaluation and selection among status quo, hybrid, and revert options",
      "bias_specific_mechanism": "The existing LumenKit implementation was disproportionately favored because it was the familiar, known quantity. The anticipated cognitive and operational cost of switching to a new arrangement was overweighted even though the hybrid option was acknowledged as objectively cleaner.",
      "manifestation_in_interview": "The participant recommended continuing with LumenKit tokens and all, explicitly stating that familiarity mattered more than moving to an arrangement that was objectively cleaner but new to the team.",
      "effect_on_reasoning_or_decision": "The final recommendation retained the problematic token setup rather than adopting the hybrid approach that would have addressed the token compliance problem directly.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup. Even with the hybrid's technical case being reasonably strong, sticking with what we already had running felt like the safer, known quantity this close to the deadline — everyone on both squads already understood how the current setup behaved, and that familiarity mattered more to me in the moment than moving to an arrangement that was objectively cleaner but still new to the team.",
          "evidence_explanation": "This directly shows the current state was preferred due to familiarity and perceived safety even while recognizing an alternative was objectively cleaner, which is the signature of status quo bias."
        }
      ],
      "correction_or_counterevidence": "Under deadline pressure, avoiding a new arrangement can be a defensible risk-management choice. However, the participant frames the preference as familiarity outweighing an objectively cleaner fix, indicating status quo bias rather than a purely technical trade-off.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided RAG context directly addresses status quo bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The available retrieved passages provided direct support only for anchoring bias and confirmation bias; planning fallacy, sunk cost fallacy, and status quo bias were classified using established general cognitive-science knowledge.",
    "The analysis is based on the participant's self-reported reasoning and may not capture all tacit influences on decision-making.",
    "Some judgments may reflect bounded rationality or defensible deadline risk management; confidence levels reflect this uncertainty."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the LumenKit evaluation, not whether the outcome was 'right.' Everything you share stays in the design systems research archive. Sound okay? Participant: Sounds good. Happy to walk through it — it's still fresh, honestly. Interviewer: Great. Can you remind me of your role and what triggered this whole evaluation? Participant: I lead design systems for the platform org — three designers, two engineers under me. Legal flagged that we needed to hit WCAG 2.2 AA across two customer-facing squads within about ten weeks, and our internal component library had known contrast and focus-state debt we hadn't prioritized. LumenKit came up because a couple of competitors use it and it's picked up some industry recognition. Interviewer: What was your goal going into the vendor demo? Participant: Mainly to see if we could shortcut months of remediation work by adopting something pre-built and compliant, given the clock we were on. Interviewer: Walk me through what happened, in order. Participant: The solutions engineer ran maybe forty minutes, almost all of it on their accordion component — the motion, the keyboard handling, the way it degraded gracefully. It was genuinely impressive, smoother than anything we'd built in-house. They mentioned the whole library ships with AA-compliant color defaults. After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down. We got a three-week sandbox with a limited component set, and both squad leads said they were interested but needed pricing before committing engineering time. Interviewer: Did you look closely at the color and elevation tokens before making that call? Participant: Not directly, no — we hadn't run our own contrast checks yet. But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape. That assumption is part of why I pushed for the broad pilot instead of testing component by component first. Interviewer: Let's move to the licensing decision. What did that look like? Participant: Procurement needed a tier recommendation within two weeks. Vendor offered three: Basic, five components, no support; Team, twelve components with limited support, priced not far below Enterprise; and Enterprise, the full library with dedicated support. I recommended Enterprise. Interviewer: What made Enterprise the clear choice? Participant: Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation — it was more that comparing the three side by side made Enterprise the only one that made sense. Interviewer: And the rollout timeline — how was that set? Participant: I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads. Interviewer: Had the two dependent squads confirmed they could hit a four-week window? Participant: Not formally, no. I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars. One of them came back shortly after saying their calendar genuinely couldn't accommodate that window — they had an unrelated release freeze I hadn't accounted for. Interviewer: What information would have changed your timeline call, looking back? Participant: Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first. Interviewer: Let's get to the audit. What came back? Participant: About seven weeks in, our internal accessibility audit found that several of LumenKit's color and elevation tokens failed contrast ratio requirements in three of five tested components. That was awkward, because I'd already told the VP and both squad leads that LumenKit would solve most of our contrast problems out of the box. Interviewer: What was your first read on that discrepancy? Participant: My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance. Part of why that explanation felt like the natural one to reach for first was that I'd already told the VP and both squad leads LumenKit would solve most of our contrast problems out of the box, so 'it's our theming, not their tokens' sat better with what I'd already said than the alternative did. I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities. Interviewer: What did you decide to do next? Participant: We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy. The legacy components already had remediated contrast values for those same screens, so that was sitting right there as an option. Interviewer: What made continuing the more attractive path versus reverting? Participant: Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked. Interviewer: Did the VP or squad leads react? Participant: The VP wanted a written explanation for the compliance file. One squad lead quietly reverted their branch back to the legacy component for the affected screens without waiting on my decision. Interviewer: That brings us to the final call. What were the options three weeks before the deadline? Participant: Expand LumenKit org-wide as we'd implemented it, adopt a hybrid — keep LumenKit's motion and layout components but source color and elevation tokens internally — or revert fully to legacy. Interviewer: How did the hybrid option evaluate against the others? Participant: On paper it addressed the token problem directly without throwing away the layout and motion integration work we'd already done. It was arguably the cleanest fix. Interviewer: So what did you recommend? Participant: I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup. Even with the hybrid's technical case being reasonably strong, sticking with what we already had running felt like the safer, known quantity this close to the deadline — everyone on both squads already understood how the current setup behaved, and that familiarity mattered more to me in the moment than moving to an arrangement that was objectively cleaner but still new to the team. Interviewer: If the audit had surfaced in week one instead of week seven, do you think that would have changed how you weighed the hours already spent? Participant: Probably — with less invested, reverting or pivoting to the hybrid would've felt like a much smaller loss. Interviewer: If the vendor demo had opened with contrast-ratio data instead of the accordion, would your initial pilot decision have gone differently? Participant: Possibly. If I'd seen the token-level numbers first, I might've scoped the pilot narrower before committing broadly. Interviewer: If procurement had only offered two tiers instead of three, would Enterprise still have been the obvious pick? Participant: Harder to say — I might have actually priced out Enterprise against our real component needs rather than against Team. Interviewer: Last one — starting over today, what would you keep, and what would you change? Participant: I'd keep the urgency and the willingness to bring in outside tooling under deadline pressure — that part was right. I'd change how early I locked in public commitments about what the library would solve, and I'd get squad confirmation on timelines before setting them rather than after. Interviewer: This has been really useful. Thanks for being so candid about the reasoning, not just the outcome. Participant: No problem — it's easier to see it laid out like this than it was living through it week to week.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.02s · gen 125.31s · total 129.7s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0275 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0234 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Hallihan_etal_DTM_12.pdf** — 0.0233 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0224 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
5. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0214 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
6. **Hallihan_etal_DTM_12.pdf** — 0.0212 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0207 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **Hallihan_etal_DTM_12.pdf** — 0.0203 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
9. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0194 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
10. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0194 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0178 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0174 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
13. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0172 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
14. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0172 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
15. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0171 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0168 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0167 (rrf) — _# ( " = 0 . 44 ) . Proc. ACM Hum.-Comput. Interact., Vol. 5, No. CSCW1, Article 188. Publication_
18. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0167 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs 1 Google Scholar(assessment done on Mar_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0166 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
20. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
21. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
22. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
23. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
24. **Hallihan_etal_DTM_12.pdf** — 0.0163 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0161 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0160 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
27. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0160 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
28. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0157 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
29. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0157 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs decisionmaking scenarios. We confirm ea_
30. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0157 (rrf) — _ligence analysis, evaluating visualizations thatthe task environment (e.g., Klayman & Ha, 1987; _
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
32. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0156 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
33. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
34. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0155 (rrf) — _# 4.2 Answering our RQs AI & SOCIETY the AI’s recommendation, provided as a second opinion, alig_
35. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0154 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
36. **Lyell Automation bias and verification complexity.pdf** — 0.0153 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
37. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
38. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0152 (rrf) — _## 1Introduction RQ3: Can explainability or transparency mitigate automation bias? RQ4: Is AI li_
39. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0152 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
40. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0152 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs opinions when presented with new eviden_
41. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0149 (rrf) — _# Cognitive Biases in Technical Communication The Sun k Cost Fallacy refers to t decisions that _
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
43. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study anchor. Anchoring bias is_
44. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0145 (rrf) — _motivation in mediating the eectiveness of XAI solutions. Therefore, beyond optimizing explanati_
45. **Hallihan_etal_DTM_12.pdf** — 0.0144 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
46. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0143 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study In the context of artifac_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
48. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0141 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0139 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
50. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0138 (rrf) — _# 188 To Trust or to Think on the AI compared to the simple explainable AI approaches. However, _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the participant's reasoning across vendor evaluation, procurement tier selection, timeline setting, audit interpretation, continuation decisions, and final rollout recommendation. Confidence reflects the explicitness of bias-specific mechanism evidence in the transcript."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "decoy effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "planning fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status quo bias",
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
      "bias_label": "halo effect",
      "alternative_labels": ["halo error", "overgeneralization from salient positive feature"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency for a salient positive impression in one dimension to spread to evaluations of unrelated or untested dimensions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-demo decision to recommend a broad LumenKit pilot without direct token-layer verification",
      "decision_point_description": "Participant chose to pilot the full token set across both squads rather than testing component by component or running contrast checks first.",
      "affected_reasoning_operation": "Generalization from observed component quality to untested accessibility compliance of the full token layer",
      "bias_specific_mechanism": "The impressive accordion demo, awards, and competitor adoption created a global positive evaluation that spread to the color and elevation token layer, reducing the perceived need for component-specific verification.",
      "manifestation_in_interview": "Participant cited the accordion's quality, awards, and competitor adoption as grounds for assuming token-layer compliance, despite not having run contrast checks.",
      "effect_on_reasoning_or_decision": "Drove a broad pilot recommendation based on assumed token-layer quality rather than direct token-level evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "They mentioned the whole library ships with AA-compliant color defaults. After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down.",
          "evidence_explanation": "The participant generalized from an overall quality impression to full-token-set adoption before direct compliance checks."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly, no — we hadn't run our own contrast checks yet. But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape. That assumption is part of why I pushed for the broad pilot instead of testing component by component first.",
          "evidence_explanation": "This explicitly links the positive impression of one component to an untested assumption about the token layer, which then shaped the broad pilot decision."
        }
      ],
      "correction_or_counterevidence": "Later the internal accessibility audit contradicted the token-compliance assumption, though this was not considered at the time of the initial pilot decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No suitable retrieved corpus passage was available for this bias label; the identification relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "decoy effect",
      "alternative_labels": ["asymmetric dominance effect", "attraction effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for one option is influenced by the presence of a dominated or unattractive alternative that makes the target option appear more favorable.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Procurement tier recommendation",
      "decision_point_description": "Selecting the Enterprise tier after comparing Basic, Team, and Enterprise side by side rather than evaluating Enterprise against actual needs or a scoped custom build.",
      "affected_reasoning_operation": "Comparative evaluation of procurement tiers",
      "bias_specific_mechanism": "The Team tier served as a relatively dominated option, priced near Enterprise with fewer components and weaker support, making Enterprise look more attractive by contrast and bypassing an isolated needs/cost analysis.",
      "manifestation_in_interview": "Participant explicitly said Team was a bad deal and that Enterprise looked obviously better next to it, while not pricing Enterprise against a scoped custom build or actual component needs.",
      "effect_on_reasoning_or_decision": "Enterprise was recommended as the obvious choice due to contextual comparison, not because it was independently assessed as the best fit.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation — it was more that comparing the three side by side made Enterprise the only one that made sense.",
          "evidence_explanation": "The reasoning explicitly depends on the unattractive middle option making Enterprise appear superior, rather than on an isolated assessment of Enterprise."
        }
      ],
      "correction_or_counterevidence": "When asked about a two-tier counterfactual, the participant acknowledged he might have priced out Enterprise against real component needs rather than against Team.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No suitable retrieved corpus passage was available for this bias label; the identification relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "planning fallacy",
      "alternative_labels": ["optimism bias", "inside view"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to underestimate time, costs, or risks of future actions while overestimating one's ability to control them, often by focusing on the specific plan rather than relevant external constraints.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Setting the four-week rollout timeline without first confirming squad capacity",
      "decision_point_description": "Participant set an aggressive four-week integration window and asked squads to work toward it rather than first asking whether the date was feasible.",
      "affected_reasoning_operation": "Timeline estimation and commitment",
      "bias_specific_mechanism": "The participant relied on an inside-view plan centered on personal hands-on management and daily synchronization, while neglecting external constraints such as existing squad release calendars and an unrelated release freeze.",
      "manifestation_in_interview": "Participant assumed daily management could overcome any conflicts and later learned that a squad calendar could not accommodate the window.",
      "effect_on_reasoning_or_decision": "Produced an infeasible timeline for at least one squad and avoided a feasibility check before setting the date.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads.",
          "evidence_explanation": "Shows an optimistic plan based on personal involvement rather than external capacity confirmation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars. One of them came back shortly after saying their calendar genuinely couldn't accommodate that window — they had an unrelated release freeze I hadn't accounted for.",
          "evidence_explanation": "Demonstrates overconfidence in managerial control and neglect of existing external constraints."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first.",
          "evidence_explanation": "Participants recognized the missing feasibility check that would have reduced planning optimism."
        }
      ],
      "correction_or_counterevidence": "Participant later acknowledged he should have asked each squad lead directly whether four weeks fit their commitments before setting the date.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No suitable retrieved corpus passage was available for this bias label; the identification relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["motivated reasoning", "congeniality bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to favor interpretations that support existing beliefs or prior commitments and to avoid or discount evidence that would disconfirm them.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation of the accessibility audit discrepancy",
      "decision_point_description": "Participant interpreted failed contrast ratios as implementation-specific theming edge cases rather than vendor noncompliance and did not seek an independent retest of out-of-box tokens.",
      "affected_reasoning_operation": "Causal attribution and evidence gathering after contradictory audit results",
      "bias_specific_mechanism": "The participant preferred a hypothesis consistent with his earlier public commitment that LumenKit would solve most contrast problems, and avoided the disconfirming test that would separate theming effects from vendor token failures.",
      "manifestation_in_interview": "Participant explicitly said the theming explanation felt natural because it sat better with what he had already told the VP and squad leads.",
      "effect_on_reasoning_or_decision": "The participant did not distinguish implementation effects from vendor noncompliance, preserving the prior narrative and shaping the next steps toward continued fixing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance.",
          "evidence_explanation": "Shows preference for an interpretation that protects the vendor and the prior rollout commitment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Part of why that explanation felt like the natural one to reach for first was that I'd already told the VP and both squad leads LumenKit would solve most of our contrast problems out of the box, so 'it's our theming, not their tokens' sat better with what I'd already said than the alternative did.",
          "evidence_explanation": "Explicitly ties the preferred explanation to consistency with a prior public commitment rather than to a neutral evaluation of evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities.",
          "evidence_explanation": "Demonstrates avoidance of a diagnostic test that could disconfirm the preferred explanation."
        }
      ],
      "correction_or_counterevidence": "A squad lead quietly reverted their branch back to the legacy component, and the audit contradicts the initial edge-case interpretation; however, the participant did not initially seek an independent retest.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Hallihan et al. passage directly supports the confirmation-bias mechanism of discounting contradictory information in design evaluation.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Results of this analysis led us to conclude that confirmation bias can lead designers to: • Ignore or discount factual contradictory information",
          "mechanism_supported_by_source": "The source links confirmation bias to ignoring or discounting factual contradictory information, which is the core pattern in the participant's preferred theming-edge-case explanation.",
          "relevance_to_this_occurrence": "The participant discounted the audit's contradictory contrast-ratio findings and avoided a disconfirming test of the vendor's out-of-box tokens."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": ["escalation of commitment", "sunk cost effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to continue an endeavor because of previously invested resources, even when continuing is not justified by expected future value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-audit decision to continue refining LumenKit tokens rather than revert to legacy",
      "decision_point_description": "Participant decided to keep refining after more than forty engineering hours instead of pausing or falling back to legacy components that already had remediated contrast values.",
      "affected_reasoning_operation": "Continuation versus disengagement decision",
      "bias_specific_mechanism": "The unrecoverable customization hours were treated as a reason to continue, making abandonment feel like a loss and continued refinement feel more efficient.",
      "manifestation_in_interview": "Participant explicitly cited writing off the hours already invested as a reason not to revert.",
      "effect_on_reasoning_or_decision": "Continued on a noncompliant path instead of using a ready legacy fallback.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy.",
          "evidence_explanation": "The decision to continue is explicitly tied to the prior investment of hours."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked.",
          "evidence_explanation": "Shows the sunk-cost mechanism: avoiding the perceived loss of writing off past effort."
        }
      ],
      "correction_or_counterevidence": "Participant acknowledged that if the audit had surfaced in week one, with less invested, reverting or pivoting would have felt like a smaller loss.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No suitable retrieved corpus passage was available for this bias label; the identification relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "status quo bias",
      "alternative_labels": ["familiarity bias", "default bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for the current or existing state over a change, even when an alternative is objectively stronger, because the current state feels safer or more familiar.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final recommendation among org-wide LumenKit, hybrid, and full revert three weeks before the deadline",
      "decision_point_description": "Participant recommended continuing largely with the current LumenKit implementation rather than switching to the hybrid token-sourcing arrangement.",
      "affected_reasoning_operation": "Option evaluation and final recommendation",
      "bias_specific_mechanism": "The existing setup's familiarity was weighted more heavily than the hybrid's technical fit; change aversion favored the known current state despite the hybrid being described as objectively cleaner.",
      "manifestation_in_interview": "Participant stated that sticking with the current setup felt safer and more known, and that familiarity mattered more than moving to a newer arrangement.",
      "effect_on_reasoning_or_decision": "The final recommendation favored the status quo over the technically stronger hybrid option.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup.",
          "evidence_explanation": "Shows the preference for the existing approach over the hybrid alternative."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Even with the hybrid's technical case being reasonably strong, sticking with what we already had running felt like the safer, known quantity this close to the deadline — everyone on both squads already understood how the current setup behaved, and that familiarity mattered more to me in the moment than moving to an arrangement that was objectively cleaner but still new to the team.",
          "evidence_explanation": "Explicitly weights familiarity and current-state safety over an acknowledged objectively cleaner alternative."
        }
      ],
      "correction_or_counterevidence": "No explicit correction in the transcript; the interviewer noted the hybrid option addressed the token problem directly and was arguably the cleanest fix.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No suitable retrieved corpus passage was available for this bias label; the identification relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a single self-report; reasoning is retrospective and may be reconstructed rather than a direct observation of decision-time cognition.",
    "Retrieved corpus support was available only for confirmation bias; other labels rely on general cognitive-science knowledge because the provided corpus did not contain directly supporting passages.",
    "Confidence values reflect the explicitness of bias-specific mechanism evidence in the transcript, not external validation or outcome data.",
    "The analysis does not infer a benchmark or judge the correctness of the decisions."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the LumenKit evaluation, not whether the outcome was 'right.' Everything you share stays in the design systems research archive. Sound okay? Participant: Sounds good. Happy to walk through it — it's still fresh, honestly. Interviewer: Great. Can you remind me of your role and what triggered this whole evaluation? Participant: I lead design systems for the platform org — three designers, two engineers under me. Legal flagged that we needed to hit WCAG 2.2 AA across two customer-facing squads within about ten weeks, and our internal component library had known contrast and focus-state debt we hadn't prioritized. LumenKit came up because a couple of competitors use it and it's picked up some industry recognition. Interviewer: What was your goal going into the vendor demo? Participant: Mainly to see if we could shortcut months of remediation work by adopting something pre-built and compliant, given the clock we were on. Interviewer: Walk me through what happened, in order. Participant: The solutions engineer ran maybe forty minutes, almost all of it on their accordion component — the motion, the keyboard handling, the way it degraded gracefully. It was genuinely impressive, smoother than anything we'd built in-house. They mentioned the whole library ships with AA-compliant color defaults. After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down. We got a three-week sandbox with a limited component set, and both squad leads said they were interested but needed pricing before committing engineering time. Interviewer: Did you look closely at the color and elevation tokens before making that call? Participant: Not directly, no — we hadn't run our own contrast checks yet. But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape. That assumption is part of why I pushed for the broad pilot instead of testing component by component first. Interviewer: Let's move to the licensing decision. What did that look like? Participant: Procurement needed a tier recommendation within two weeks. Vendor offered three: Basic, five components, no support; Team, twelve components with limited support, priced not far below Enterprise; and Enterprise, the full library with dedicated support. I recommended Enterprise. Interviewer: What made Enterprise the clear choice? Participant: Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation — it was more that comparing the three side by side made Enterprise the only one that made sense. Interviewer: And the rollout timeline — how was that set? Participant: I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads. Interviewer: Had the two dependent squads confirmed they could hit a four-week window? Participant: Not formally, no. I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars. One of them came back shortly after saying their calendar genuinely couldn't accommodate that window — they had an unrelated release freeze I hadn't accounted for. Interviewer: What information would have changed your timeline call, looking back? Participant: Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first. Interviewer: Let's get to the audit. What came back? Participant: About seven weeks in, our internal accessibility audit found that several of LumenKit's color and elevation tokens failed contrast ratio requirements in three of five tested components. That was awkward, because I'd already told the VP and both squad leads that LumenKit would solve most of our contrast problems out of the box. Interviewer: What was your first read on that discrepancy? Participant: My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance. Part of why that explanation felt like the natural one to reach for first was that I'd already told the VP and both squad leads LumenKit would solve most of our contrast problems out of the box, so 'it's our theming, not their tokens' sat better with what I'd already said than the alternative did. I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities. Interviewer: What did you decide to do next? Participant: We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy. The legacy components already had remediated contrast values for those same screens, so that was sitting right there as an option. Interviewer: What made continuing the more attractive path versus reverting? Participant: Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked. Interviewer: Did the VP or squad leads react? Participant: The VP wanted a written explanation for the compliance file. One squad lead quietly reverted their branch back to the legacy component for the affected screens without waiting on my decision. Interviewer: That brings us to the final call. What were the options three weeks before the deadline? Participant: Expand LumenKit org-wide as we'd implemented it, adopt a hybrid — keep LumenKit's motion and layout components but source color and elevation tokens internally — or revert fully to legacy. Interviewer: How did the hybrid option evaluate against the others? Participant: On paper it addressed the token problem directly without throwing away the layout and motion integration work we'd already done. It was arguably the cleanest fix. Interviewer: So what did you recommend? Participant: I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup. Even with the hybrid's technical case being reasonably strong, sticking with what we already had running felt like the safer, known quantity this close to the deadline — everyone on both squads already understood how the current setup behaved, and that familiarity mattered more to me in the moment than moving to an arrangement that was objectively cleaner but still new to the team. Interviewer: If the audit had surfaced in week one instead of week seven, do you think that would have changed how you weighed the hours already spent? Participant: Probably — with less invested, reverting or pivoting to the hybrid would've felt like a much smaller loss. Interviewer: If the vendor demo had opened with contrast-ratio data instead of the accordion, would your initial pilot decision have gone differently? Participant: Possibly. If I'd seen the token-level numbers first, I might've scoped the pilot narrower before committing broadly. Interviewer: If procurement had only offered two tiers instead of three, would Enterprise still have been the obvious pick? Participant: Harder to say — I might have actually priced out Enterprise against our real component needs rather than against Team. Interviewer: Last one — starting over today, what would you keep, and what would you change? Participant: I'd keep the urgency and the willingness to bring in outside tooling under deadline pressure — that part was right. I'd change how early I locked in public commitments about what the library would solve, and I'd get squad confirmation on timelines before setting them rather than after. Interviewer: This has been really useful. Thanks for being so candid about the reasoning, not just the outcome. Participant: No problem — it's easier to see it laid out like this than it was living through it week to week.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.25s · gen 145.37s · total 150.0s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0275 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0234 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Hallihan_etal_DTM_12.pdf** — 0.0233 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
4. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0224 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
5. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0214 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
6. **Hallihan_etal_DTM_12.pdf** — 0.0212 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0207 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **Hallihan_etal_DTM_12.pdf** — 0.0203 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
9. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0194 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
10. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0194 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0178 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0174 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
13. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0172 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
14. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0172 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
15. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0171 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0168 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
17. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0167 (rrf) — _# ( " = 0 . 44 ) . Proc. ACM Hum.-Comput. Interact., Vol. 5, No. CSCW1, Article 188. Publication_
18. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0167 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs 1 Google Scholar(assessment done on Mar_
19. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0166 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
20. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
21. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0164 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
22. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
23. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
24. **Hallihan_etal_DTM_12.pdf** — 0.0163 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
25. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0161 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0160 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
27. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0160 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
28. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0157 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
29. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0157 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs decisionmaking scenarios. We confirm ea_
30. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0157 (rrf) — _ligence analysis, evaluating visualizations thatthe task environment (e.g., Klayman & Ha, 1987; _
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
32. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0156 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
33. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
34. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0155 (rrf) — _# 4.2 Answering our RQs AI & SOCIETY the AI’s recommendation, provided as a second opinion, alig_
35. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0154 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
36. **Lyell Automation bias and verification complexity.pdf** — 0.0153 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
37. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
38. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0152 (rrf) — _## 1Introduction RQ3: Can explainability or transparency mitigate automation bias? RQ4: Is AI li_
39. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0152 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
40. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0152 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs opinions when presented with new eviden_
41. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0149 (rrf) — _# Cognitive Biases in Technical Communication The Sun k Cost Fallacy refers to t decisions that _
42. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0147 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
43. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study anchor. Anchoring bias is_
44. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0145 (rrf) — _motivation in mediating the eectiveness of XAI solutions. Therefore, beyond optimizing explanati_
45. **Hallihan_etal_DTM_12.pdf** — 0.0144 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
46. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0143 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study In the context of artifac_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
48. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0141 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0139 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
50. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0138 (rrf) — _# 188 To Trust or to Think on the AI compared to the simple explainable AI approaches. However, _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Mechanism-first analysis of participant reasoning episodes; only affirmative transcript evidence was classified as bias."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "decoy effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "planning fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status quo bias",
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
      "bias_label": "halo effect",
      "alternative_labels": [
        "halo bias",
        "generalization from global impression"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency for a salient positive impression in one dimension to influence evaluations of unrelated dimensions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial pilot scope decision after vendor accordion demo",
      "decision_point_description": "Choosing whether to pilot the full token set broadly or test component by component before committing.",
      "affected_reasoning_operation": "Assessment of LumenKit's unreviewed color and elevation token accessibility based on an impressive accordion demo and external prestige cues.",
      "bias_specific_mechanism": "A positive global quality impression from one well-executed component was overgeneralized to the unreviewed token layer, without direct token-level checks.",
      "manifestation_in_interview": "After the demo, the participant recommended broad pilot adoption, explicitly stating he assumed the token layer was good because the accordion was well executed and the product had awards and competitor adoption.",
      "effect_on_reasoning_or_decision": "Led to recommending a broad pilot across both squads rather than a narrower component-by-component test before independent contrast checks.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down.",
          "evidence_explanation": "Shows that the global quality impression from the demo directly shaped a broad adoption decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape.",
          "evidence_explanation": "Explicitly shows the inferential leap from accordion execution and external prestige to an untested token layer."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged he had not run contrast checks and the audit later disconfirmed token quality, but no debiasing occurred before the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addresses halo effect; classification rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "decoy effect",
      "alternative_labels": [
        "attraction effect",
        "asymmetric dominance effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A context effect where adding a dominated option makes the dominating option more attractive.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Procurement tier recommendation",
      "decision_point_description": "Selecting among Basic, Team, and Enterprise licensing tiers within a two-week procurement window.",
      "affected_reasoning_operation": "Evaluation of Enterprise's value compared only with the available tier set rather than against actual component needs or external build options.",
      "bias_specific_mechanism": "Team tier functioned as a dominated reference point; Enterprise's superiority to Team made it appear as the only sensible choice, displacing absolute-need or external-baseline evaluation.",
      "manifestation_in_interview": "The participant said Team was almost Enterprise money for a fraction of the components and worse support; he did not price Enterprise against a scoped custom build or actual needs in isolation.",
      "effect_on_reasoning_or_decision": "Recommended Enterprise without isolated cost-benefit analysis against actual component needs or scoped custom build alternatives.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation — it was more that comparing the three side by side made Enterprise the only one that made sense.",
          "evidence_explanation": "Shows local comparison against a dominated tier rather than an external baseline or actual need analysis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Harder to say — I might have actually priced out Enterprise against our real component needs rather than against Team.",
          "evidence_explanation": "In response to the interviewer's counterfactual, the participant acknowledges the three-option context influenced his evaluation."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction was present; the retrospective counterfactual shows awareness only in hindsight.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addresses the decoy effect; classification rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "planning fallacy",
      "alternative_labels": [
        "optimism bias",
        "overconfidence effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to underestimate time, risk, and constraints of future actions while overestimating the likelihood of successful completion.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Rollout timeline setting for integration",
      "decision_point_description": "Setting a four-week rollout window for two squads without formal feasibility confirmation.",
      "affected_reasoning_operation": "Forecasting whether both squads could accommodate the four-week integration timeline.",
      "bias_specific_mechanism": "Inside-view forecasting with over-reliance on personal oversight and daily management instead of consulting squad release calendars and existing constraints.",
      "manifestation_in_interview": "The participant set an aggressive four-week timeline, did not formally confirm squad capacity, and assumed hands-on management would overcome existing release calendars.",
      "effect_on_reasoning_or_decision": "The timeline was unrealistic for at least one squad, which had an unrelated release freeze; upfront feasibility was not assessed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads.",
          "evidence_explanation": "Shows the plan was based on the participant's own intended oversight rather than verified squad capacity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not formally, no. I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars. One of them came back shortly after saying their calendar genuinely couldn't accommodate that window — they had an unrelated release freeze I hadn't accounted for.",
          "evidence_explanation": "Explicitly demonstrates optimistic forecasting and failure to incorporate external constraints."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first.",
          "evidence_explanation": "Confirms that feasibility information was not sought before setting the timeline."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that asking squad leads directly before setting the date would have changed the timeline; no contemporaneous correction occurred.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addresses planning fallacy; classification rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "motivated reasoning",
        "biased assimilation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in ways that confirm existing beliefs or commitments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of internal accessibility audit findings",
      "decision_point_description": "Deciding how to explain audit evidence that LumenKit tokens failed contrast ratio requirements.",
      "affected_reasoning_operation": "Causal attribution of the audit failure to library non-compliance versus internal theming integration.",
      "bias_specific_mechanism": "The participant favored the explanation consistent with the vendor's compliance claim and his public commitment that LumenKit would solve contrast issues; he did not run an independent out-of-box token test that could disconfirm this.",
      "manifestation_in_interview": "He called the failures implementation-specific edge cases and attributed them to theming rather than the library itself, explicitly linking this to having already told the VP and squad leads that LumenKit would solve contrast issues.",
      "effect_on_reasoning_or_decision": "No independent re-test was requested; the path continued as if library tokens were compliant and the failures were due to internal theming.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance.",
          "evidence_explanation": "Shows selective interpretation favoring vendor compliance over the possibility of library non-compliance."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Part of why that explanation felt like the natural one to reach for first was that I'd already told the VP and both squad leads LumenKit would solve most of our contrast problems out of the box, so 'it's our theming, not their tokens' sat better with what I'd already said than the alternative did. I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities.",
          "evidence_explanation": "Explicitly ties the favored explanation to prior commitment and avoidance of a discriminating test."
        }
      ],
      "correction_or_counterevidence": "The audit itself was counterevidence that was rationalized rather than fully evaluated; no contemporaneous debiasing occurred.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Hallihan et al. supports confirmation bias in design evaluation, including discounting contradictory evidence and failure to consider disconfirming evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "c onclusions participants were asked to evaluate,  concluded that there was a significant amount of evidence  available to both support and reject the fixation The remaining four participants (4, 8, 10, & 16) concluded  that the fixation hypothesis was well supported by this data.  Participants 4 and 8 evaluated more confirmatory evidence  than disconfirmatory, and participants 10 and 16 evaluated  more disconfirmatory evidence than confirmatory. The later  case may be a result of tho se participants failing to evaluate the diagnostic value known consequence of confirmation bias",
          "mechanism_supported_by_source": "The retrieved passage links confirmation bias to biased evaluation of confirmatory versus disconfirmatory evidence.",
          "relevance_to_this_occurrence": "The participant discounted contradictory audit evidence and avoided an independent disconfirming test, consistent with confirmation bias."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to continue an endeavor once resources have been invested, even when future prospects are poor, because past costs are treated as losses to avoid.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision whether to continue customizing LumenKit tokens or revert to remediated legacy components",
      "decision_point_description": "After the audit revealed token failures and over forty engineering hours had already been spent.",
      "affected_reasoning_operation": "Choosing between continued refinement of failing LumenKit tokens and reverting to legacy components.",
      "bias_specific_mechanism": "The prior investment of over forty engineering hours was weighed as a reason not to switch, leading to continued investment in the failing path rather than using the already-remediated legacy fallback.",
      "manifestation_in_interview": "The participant said reverting would mean writing off hours already spent and felt it was more efficient to push through than start over.",
      "effect_on_reasoning_or_decision": "Continued refining LumenKit tokens instead of pausing or reverting, despite legacy components already having remediated contrast values.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy. The legacy components already had remediated contrast values for those same screens, so that was sitting right there as an option.",
          "evidence_explanation": "Shows the prior investment directly influenced the decision to continue despite a viable fallback."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked.",
          "evidence_explanation": "Explicitly frames past costs as a reason to avoid switching, which is the sunk cost mechanism."
        }
      ],
      "correction_or_counterevidence": "One squad lead quietly reverted their branch to legacy without waiting for the participant's decision, providing external counteraction; the participant's own decision remained continuation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addresses sunk cost fallacy; classification rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "status quo bias",
      "alternative_labels": [
        "familiarity bias",
        "default bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for the current state or familiar option over a change, even when alternatives are objectively better.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final recommendation among expand, hybrid, or full revert",
      "decision_point_description": "Three weeks before deadline, choosing whether to adopt hybrid token sourcing or continue the current LumenKit implementation.",
      "affected_reasoning_operation": "Evaluation of the hybrid option versus continuing the current implementation.",
      "bias_specific_mechanism": "The participant favored the existing implementation because it was familiar and operational, even though the hybrid was described as objectively cleaner and directly addressed the token problem.",
      "manifestation_in_interview": "The participant stated the hybrid was arguably the cleanest fix but recommended continuing the current setup because it felt safer and more familiar to the team.",
      "effect_on_reasoning_or_decision": "Recommended continuing the current LumenKit token setup rather than switching to the hybrid, despite the unresolved contrast problem.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "On paper it addressed the token problem directly without throwing away the layout and motion integration work we'd already done. It was arguably the cleanest fix.",
          "evidence_explanation": "Shows the alternative was recognized as technically strong."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Even with the hybrid's technical case being reasonably strong, sticking with what we already had running felt like the safer, known quantity this close to the deadline — everyone on both squads already understood how the current setup behaved, and that familiarity mattered more to me in the moment than moving to an arrangement that was objectively cleaner but still new to the team.",
          "evidence_explanation": "Explicitly places familiarity with the current state above the technical merits of the new option."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction; the participant later reflected on changing early commitments but did not identify this preference as biased.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly addresses status quo bias; classification rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial pilot scope after vendor demo order",
      "supporting_interview_quote": "If the vendor demo had opened with contrast-ratio data instead of the accordion, would your initial pilot decision have gone differently? Participant: Possibly. If I'd seen the token-level numbers first, I might've scoped the pilot narrower before committing broadly.",
      "plausible_mechanism": "The initial accordion demo may have served as an anchor for overall quality, influencing downstream scoping before token-level data were encountered.",
      "why_not_identified": "The primary actual inference is more exactly halo effect, generalizing from one attribute to another; the interview provides retrospective counterfactual rather than affirmative evidence of a separate numeric anchor-and-adjustment mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was sparse; only confirmation bias had direct retrieved support. Other bias labels rely on general cognitive-science knowledge.",
    "The transcript is retrospective self-report, so some mechanism classifications depend on the participant's own articulation of reasoning.",
    "Some decisions occurred under time pressure and organizational constraints; bias classifications were limited to mechanisms affirmatively evidenced in the reasoning."
  ]
}

