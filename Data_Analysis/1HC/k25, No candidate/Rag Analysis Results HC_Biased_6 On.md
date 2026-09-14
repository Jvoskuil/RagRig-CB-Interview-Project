# RAG Benchmark — 2026-09-09

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time this week of all weeks. Before we start, this is just for our internal process-improvement review — I'll ask you to walk me through a recent stretch of work, and there's no wrong answer. That okay? Participant: Sure, happy to. Lock week is a good time to talk about it, honestly, everything's still fresh. Interviewer: Great. Can you remind me of your role and what was on your plate? Participant: I'm the CRC for our site on the Phase III trial — the oncology drug study. I handle adverse event triage, case report form cleanup, and screening new referrals. That week we were seven days out from the interim data lock for the DSMB, so basically everything converged at once. Interviewer: Walk me through what that week looked like. Participant: Monday morning I got a lab flag on Participant 12 — an ALT elevation, elevated but not dramatically so, and the timeline relative to dosing wasn't clean. Could've been drug-related, could've been something else entirely, maybe even diet or an OTC medication he didn't mention. I had to assign a causality category for the AE report. Same day, I was also mid-reconciliation on Participant 07's case report forms — that one had been a slog for almost two weeks, lots of inconsistent entries between the source charts and the CRF. Then Wednesday a new referral came in for screening, and Thursday there was a multi-site coordinator call about verification procedures ahead of lock. So four distinct things, all against the same deadline. Interviewer: Let's start with Participant 12. What did you have in front of you? Participant: His ALT was elevated, but in a range where you genuinely can't tell just from the number whether it's the study drug. Our protocol has three buckets — related, possibly related, unrelated — for exactly this kind of situation. I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point. Interviewer: How did that shape the classification? Participant: I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed. Interviewer: What about the 'possibly related' option? Participant: Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side. Interviewer: What happened after? Participant: The PI actually asked me to go back and pull his full lab history and prior meds before finalizing it. Which, fair — I probably should've done that up front instead of after. Interviewer: Let's move to Participant 07. Participant: That one's been painful. I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records. Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that. Interviewer: What did you do with that discrepancy? Participant: I kept going. Twenty hours felt like too much to walk away from without one more push. And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up. So I dug in for another few hours trying to resolve it. Interviewer: Did you consider flagging it as a deviation instead? Participant: I did — that was one of the options on the table, along with getting a second reviewer to look before deciding. But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours. Interviewer: How did it turn out? Participant: The discrepancy wasn't resolvable from what we had. The source documents just didn't exist to fix it. So the extra time didn't change the outcome — we flagged it anyway, just later. Interviewer: Let's talk about the new referral on Wednesday. Participant: He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has. Interviewer: What did you do with that instinct? Participant: I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway. In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through. Interviewer: What happened when you did screen him? Participant: He met every inclusion criterion. Clean screen, no issues. Which doesn't tell you much either way about whether deprioritizing him was the right call — I just got lucky that lock week didn't cost us his enrollment. Interviewer: Last one — the coordinator call about verification. Participant: Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever. Interviewer: What made you switch? Participant: Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine. Interviewer: Any pushback since? Participant: The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond 'everyone else was doing it too.' Interviewer: If you could go back, what single piece of information would have changed any of these calls? Participant: For Participant 12, if I'd pulled his full history first instead of after, I might not have leaned so hard on that other case. For the verification switch, actual error-rate data would've mattered — I just didn't have it and didn't chase it down in time. Interviewer: What if that Monday meeting about the other participant's enzyme case had never come up? Participant: I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind. Interviewer: And if the Site Director's email had framed Participant 07 differently — say, just asking whether continued reconciliation was worth the time? Participant: I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have. Interviewer: Last one — if none of the other sites had mentioned switching methods on that call? Participant: I probably would've stuck with what we had. It's passed every audit. There wasn't really a problem to solve, other than speed.

_ranker=rrf · t=0.04 · k=25 → 25 in context · 8192 ctx · emb 1.98s · gen 260.82s · total 265.2s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0249 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0246 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0242 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
5. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0237 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
6. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0201 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0199 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0191 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
9. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
10. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0191 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
11. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0188 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
12. **Hallihan_etal_DTM_12.pdf** — 0.0183 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
13. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0173 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
14. **Hallihan_etal_DTM_12.pdf** — 0.0173 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0173 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0173 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0163 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
21. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0163 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
23. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
25. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis covers the participant's described reasoning episodes during the week before data lock. Interviewer questions and counterfactual prompts are used only to clarify the participant's reported reasoning; no bias is inferred solely from the interviewer's questions."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
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
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "recency effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Cognitive shortcut in which judgments are influenced by the ease with which examples or comparisons come to mind, rather than by a complete evaluation of the relevant evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Classifying Participant 12's ALT elevation causality",
      "decision_point_description": "Assigning a causality category for the adverse event report for Participant 12.",
      "affected_reasoning_operation": "Causality classification of an adverse event",
      "bias_specific_mechanism": "A recent, vivid case from Monday's team meeting was highly accessible in memory and became the spontaneous comparison point, reducing scrutiny of Participant 12's own medication and dosing timeline.",
      "manifestation_in_interview": "The participant said the recent unrelated enzyme-bump case was the first thing that came to mind and that he leaned on it more than the file-based evidence warranted.",
      "effect_on_reasoning_or_decision": "He initially leaned toward classifying Participant 12's elevation as unrelated and spent less time reviewing the participant's own history and dosing timeline than he otherwise would have.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.",
          "evidence_explanation": "This shows a recent, purely recalled case becoming the initial comparison point for the current judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed.",
          "evidence_explanation": "The participant explicitly contrasts vividness/recency with similarity and describes reduced analysis of the current participant's own file."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind.",
          "evidence_explanation": "The counterfactual further supports that memory accessibility, not clinical similarity, was the operative comparison mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that 'possibly related' was technically best supported by the data, and the PI asked him to pull the full lab history and prior medications before finalizing. Thus the availability-driven lean may have been corrected before final classification.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The specific label 'availability heuristic' is from general cognitive science; the retrieved corpus supports the related recency-accessibility mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly. For example, as participants use a device, they become more familiar the Priming and Recency Effect.",
          "mechanism_supported_by_source": "Recent events are more accessible in memory and can influence later reports or judgments.",
          "relevance_to_this_occurrence": "The participant relied on a recent Monday-meeting case because it was fresh and vivid, which then reduced his review of Participant 12's own history."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "sunk cost effect",
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to continue an endeavor because of previously invested resources, even though those sunk costs should not influence forward-looking decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Deciding whether to continue reconciling Participant 07 after a large new discrepancy",
      "decision_point_description": "Whether to continue reconciliation, flag the discrepancy as a deviation, or obtain a second reviewer.",
      "affected_reasoning_operation": "Decision to continue investing effort in reconciliation",
      "bias_specific_mechanism": "The participant treated approximately twenty hours of past irrecoverable work as a reason to keep going, making stopping feel like wasting everything already done.",
      "manifestation_in_interview": "The participant said twenty hours felt like too much to walk away from and that stopping would waste the work already put in.",
      "effect_on_reasoning_or_decision": "He spent additional hours trying to resolve the discrepancy and delayed flagging it or formally deciding whether it should be treated as a deviation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data.",
          "evidence_explanation": "This establishes the large sunk investment that later influenced the continuation decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I kept going. Twenty hours felt like too much to walk away from without one more push.",
          "evidence_explanation": "The participant states directly that past time investment drove continued effort."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did — that was one of the options on the table, along with getting a second reviewer to look before deciding. But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours.",
          "evidence_explanation": "The alternative was considered but rejected partly because stopping felt like wasting prior effort."
        }
      ],
      "correction_or_counterevidence": "The participant did consider flagging as a deviation or obtaining a second reviewer. The discrepancy ultimately was not resolvable, so the additional time did not change the outcome.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No directly relevant retrieved passage was available for the sunk cost fallacy; the label derives from general cognitive science.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "framing effect",
      "alternative_labels": [
        "loss aversion",
        "loss-framing bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Systematic change in judgment or choice caused by presenting equivalent information as a loss or gain rather than by differences in the underlying facts.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Responding to a new discrepancy in Participant 07 reconciliation after the Site Director's email",
      "decision_point_description": "Whether to continue reconciliation or to flag the discrepancy as a deviation.",
      "affected_reasoning_operation": "Evaluation of whether continued reconciliation was justified",
      "bias_specific_mechanism": "The Site Director framed the situation as a potential loss of a fifth of the evaluable per-protocol population; this loss frame made avoiding that loss feel more important than it might have under a neutral frame.",
      "manifestation_in_interview": "The participant reported that the losing-a-fifth framing stuck with him and changed the decision from being about hours to being about what they would be giving up.",
      "effect_on_reasoning_or_decision": "The loss-framed wording strengthened his decision to continue digging into the discrepancy rather than stopping or flagging it earlier.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that.",
          "evidence_explanation": "This introduces the loss frame that the participant himself identifies as having affected his reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up.",
          "evidence_explanation": "The participant directly reports that the loss framing altered the subjective weight of the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Framed as a loss, it felt heavier than it maybe should have.",
          "evidence_explanation": "This retrospective assessment explicitly identifies the framing effect on his judgment."
        }
      ],
      "correction_or_counterevidence": "The risk of losing evaluable participants was a genuine operational concern, so the frame was not entirely irrelevant. However, the participant's own account indicates that the loss framing affected his decision beyond the neutral facts.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No directly relevant retrieved passage was available for framing or loss aversion; the label derives from general cognitive science.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging likelihood or category fit by resemblance to a typical prototype, while ignoring objective criteria or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Prioritizing a new screening referral based on initial demographic picture",
      "decision_point_description": "Whether to screen the new referral promptly or place him lower in the queue.",
      "affected_reasoning_operation": "Judgment of likely trial eligibility and screening priority",
      "bias_specific_mechanism": "The participant judged the referral's likely fit by resemblance to the typical enrolled-patient prototype—older with multiple comorbidities—rather than by the objective eligibility criteria.",
      "manifestation_in_interview": "The participant said his first reaction was that the younger, active referral probably was not a good fit 'just based on the picture of him' and because he did not match the pattern of patients usually seen.",
      "effect_on_reasoning_or_decision": "He placed the referral lower in the screening queue despite the actual eligibility criteria being objective and unrelated to age or comorbidity count.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him.",
          "evidence_explanation": "The participant explicitly used resemblance to the typical patient prototype as the basis for an initial eligibility judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway. In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through.",
          "evidence_explanation": "This confirms that the deprioritization was based on pattern resemblance rather than the objective eligibility criteria."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that the eligibility criteria were objective and did not include age or comorbidity count. The referral later met every inclusion criterion, though the participant noted this did not fully resolve whether deprioritizing was an error at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus explicitly mentions representativeness bias in clinical decision support and supports the label.",
      "corpus_evidence": [
        {
          "source_identifier": "Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "a description of a clinical  manipulation to encourage  representativeness bias",
          "mechanism_supported_by_source": "Clinical decision tasks can provoke representativeness bias, in which judgments are driven by resemblance to a targeted diagnostic prototype.",
          "relevance_to_this_occurrence": "The participant judged the referral's likely eligibility by resemblance to the typical enrolled-patient prototype rather than by objective criteria."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "bandwagon effect",
      "alternative_labels": [
        "social proof",
        "conformity bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to adopt a belief or practice because many others have adopted it, independent of validated evidence on whether it is correct or effective.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Switching to a quicker source data verification approach after the multi-site coordinator call",
      "decision_point_description": "Whether to switch from the current source data verification method to the quicker method used by other sites.",
      "affected_reasoning_operation": "Method selection for source data verification",
      "bias_specific_mechanism": "The participant inferred that the new method was acceptable because most other sites had already adopted it, without seeking or receiving error-rate or validation data.",
      "manifestation_in_interview": "Hearing that other sites had switched made the participant feel behind; he did not chase validation data and later explained the switch by saying everyone else was doing it.",
      "effect_on_reasoning_or_decision": "He changed verification methods without a documented rationale, despite the existing method having passed audits without findings.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever.",
          "evidence_explanation": "This sets up the social-proof situation: adoption by others was visible, but no validation data supported the new method."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.",
          "evidence_explanation": "The participant directly states that majority adoption, not evidence, drove his switch."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond 'everyone else was doing it too.'",
          "evidence_explanation": "This confirms the absence of an evidence-based rationale and highlights social-proof reasoning."
        }
      ],
      "correction_or_counterevidence": "The existing method had a clean audit history, suggesting there was no performance problem to repair. The monitor later questioned the undocumented change.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No directly relevant retrieved passage was available for the bandwagon effect; the label derives from general cognitive science.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Need for closure",
      "alternative_labels": [
        "satisficing",
        "effort avoidance"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Choosing between 'possibly related' and 'unrelated' for Participant 12's ALT elevation",
      "supporting_interview_quote": "But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.",
      "plausible_mechanism": "The participant may have prematurely selected a definitive category because the ambiguous, better-supported category felt harder to close out.",
      "why_not_identified": "The stated rationale emphasizes workload and administrative burden, so a resource-constraint or motivational explanation competes with a distinct cognitive-bias mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on retrospective self-report rather than direct observation of decisions or performance outcomes.",
    "Sunk cost, framing, and bandwagon labels rely on general cognitive-science taxonomy because directly relevant retrieved corpus passages were unavailable.",
    "The interview contains counterfactual reasoning by the participant, which is used here only as supportive clarification of his stated mechanisms, not as independent behavioral evidence.",
    "Distinguishing availability from general vividness or recency is limited by the self-report format."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time this week of all weeks. Before we start, this is just for our internal process-improvement review — I'll ask you to walk me through a recent stretch of work, and there's no wrong answer. That okay? Participant: Sure, happy to. Lock week is a good time to talk about it, honestly, everything's still fresh. Interviewer: Great. Can you remind me of your role and what was on your plate? Participant: I'm the CRC for our site on the Phase III trial — the oncology drug study. I handle adverse event triage, case report form cleanup, and screening new referrals. That week we were seven days out from the interim data lock for the DSMB, so basically everything converged at once. Interviewer: Walk me through what that week looked like. Participant: Monday morning I got a lab flag on Participant 12 — an ALT elevation, elevated but not dramatically so, and the timeline relative to dosing wasn't clean. Could've been drug-related, could've been something else entirely, maybe even diet or an OTC medication he didn't mention. I had to assign a causality category for the AE report. Same day, I was also mid-reconciliation on Participant 07's case report forms — that one had been a slog for almost two weeks, lots of inconsistent entries between the source charts and the CRF. Then Wednesday a new referral came in for screening, and Thursday there was a multi-site coordinator call about verification procedures ahead of lock. So four distinct things, all against the same deadline. Interviewer: Let's start with Participant 12. What did you have in front of you? Participant: His ALT was elevated, but in a range where you genuinely can't tell just from the number whether it's the study drug. Our protocol has three buckets — related, possibly related, unrelated — for exactly this kind of situation. I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point. Interviewer: How did that shape the classification? Participant: I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed. Interviewer: What about the 'possibly related' option? Participant: Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side. Interviewer: What happened after? Participant: The PI actually asked me to go back and pull his full lab history and prior meds before finalizing it. Which, fair — I probably should've done that up front instead of after. Interviewer: Let's move to Participant 07. Participant: That one's been painful. I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records. Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that. Interviewer: What did you do with that discrepancy? Participant: I kept going. Twenty hours felt like too much to walk away from without one more push. And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up. So I dug in for another few hours trying to resolve it. Interviewer: Did you consider flagging it as a deviation instead? Participant: I did — that was one of the options on the table, along with getting a second reviewer to look before deciding. But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours. Interviewer: How did it turn out? Participant: The discrepancy wasn't resolvable from what we had. The source documents just didn't exist to fix it. So the extra time didn't change the outcome — we flagged it anyway, just later. Interviewer: Let's talk about the new referral on Wednesday. Participant: He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has. Interviewer: What did you do with that instinct? Participant: I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway. In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through. Interviewer: What happened when you did screen him? Participant: He met every inclusion criterion. Clean screen, no issues. Which doesn't tell you much either way about whether deprioritizing him was the right call — I just got lucky that lock week didn't cost us his enrollment. Interviewer: Last one — the coordinator call about verification. Participant: Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever. Interviewer: What made you switch? Participant: Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine. Interviewer: Any pushback since? Participant: The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond 'everyone else was doing it too.' Interviewer: If you could go back, what single piece of information would have changed any of these calls? Participant: For Participant 12, if I'd pulled his full history first instead of after, I might not have leaned so hard on that other case. For the verification switch, actual error-rate data would've mattered — I just didn't have it and didn't chase it down in time. Interviewer: What if that Monday meeting about the other participant's enzyme case had never come up? Participant: I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind. Interviewer: And if the Site Director's email had framed Participant 07 differently — say, just asking whether continued reconciliation was worth the time? Participant: I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have. Interviewer: Last one — if none of the other sites had mentioned switching methods on that call? Participant: I probably would've stuck with what we had. It's passed every audit. There wasn't really a problem to solve, other than speed.

_ranker=rrf · t=0.04 · k=25 → 25 in context · 8192 ctx · emb 1.98s · gen 319.53s · total 323.8s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0249 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0246 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0242 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
5. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0237 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
6. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0201 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0199 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0191 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
9. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
10. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0191 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
11. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0188 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
12. **Hallihan_etal_DTM_12.pdf** — 0.0183 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
13. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0173 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
14. **Hallihan_etal_DTM_12.pdf** — 0.0173 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0173 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0173 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0163 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
21. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0163 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
23. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
25. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis limited to affirmative transcript evidence of bias-specific mechanisms; retrieved passages used for conceptual grounding only."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Loss aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge frequency, likelihood, or category fit based on the ease with which relevant examples come to mind, over-weighting vivid or recent instances.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 12 AE causality classification",
      "decision_point_description": "Assigning the AE causality category (related, possibly related, or unrelated) for Participant 12's ALT elevation.",
      "affected_reasoning_operation": "Causal classification and comparison to prior participant cases",
      "bias_specific_mechanism": "A recent, vivid team-meeting case about another participant's enzyme bump was mentally available and used as the primary comparison point, reducing attention to Participant 12's own medication and dosing timeline.",
      "manifestation_in_interview": "The participant reports that the recent conversation came to mind first and that he leaned on it more than was warranted, even though it was not the most similar case.",
      "effect_on_reasoning_or_decision": "The participant leaned toward 'unrelated' for Participant 12 instead of giving equal weight to the objectively supported 'possibly related' category and before fully reviewing the participant's own history.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.",
          "evidence_explanation": "Shows a recent salient case was retrieved first and used as a comparison point for the current case."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed.",
          "evidence_explanation": "Explicitly names vividness/ease of recall as the driver of over-reliance on the other case, which is the mechanism of availability."
        }
      ],
      "correction_or_counterevidence": "The PI asked the participant to pull Participant 12's full lab history and prior medications before finalizing, and the participant acknowledged he should have done that earlier. The participant also stated that 'possibly related' was what the data supported best.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported availability heuristic; label assigned from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Sunk cost fallacy",
      "alternative_labels": ["Escalation of commitment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an endeavor because of prior invested time, effort, or resources, even when those costs cannot be recovered and future justification is weak.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 CRF reconciliation discrepancy handling",
      "decision_point_description": "Choosing whether to continue trying to resolve a serious dosing-record discrepancy versus flagging it as a deviation or obtaining second review.",
      "affected_reasoning_operation": "Escalation/perpetuation decision under adverse new evidence",
      "bias_specific_mechanism": "The participant treated the already-spent twenty hours as a reason to continue, although those hours were irrecoverable and could not improve the likelihood that missing source data would materialize.",
      "manifestation_in_interview": "The participant reports that stopping felt like wasting the prior work, and that he continued for several more hours rather than flagging the discrepancy.",
      "effect_on_reasoning_or_decision": "He invested additional hours in an ultimately unresolvable reconciliation and delayed the deviation flag and second-review option.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records.",
          "evidence_explanation": "Establishes a large prior time investment as the context for the continuation decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I kept going. Twenty hours felt like too much to walk away from without one more push.",
          "evidence_explanation": "The prior investment is used directly as the reason not to stop."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours.",
          "evidence_explanation": "Shows the irrecoverable prior work was weighed as a loss that motivated further investment, a core feature of sunk cost reasoning."
        }
      ],
      "correction_or_counterevidence": "The participant considered flagging the discrepancy as a deviation and obtaining a second reviewer. The discrepancy ultimately proved unresolvable and was flagged anyway, so the extra effort did not change the outcome.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported sunk cost fallacy; label assigned from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Loss aversion",
      "alternative_labels": ["Framing effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to weigh losses more heavily than equivalent gains, so that decisions change when outcomes are framed as losses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 reconciliation continuation decision under loss-framed site communication",
      "decision_point_description": "How strongly to persist on the reconciliation after the Site Director's email framed stopping as losing a fifth of the per-protocol population.",
      "affected_reasoning_operation": "Valuation of continued effort versus stopping",
      "bias_specific_mechanism": "The 'losing a fifth' wording made continuation an aversive loss, and the participant explicitly says the loss framing made the decision feel heavier than a neutral framing would have.",
      "manifestation_in_interview": "The participant reports that the loss-framed email stuck with him and that he would probably have stopped sooner if it had been framed as a neutral question about whether continued work was worth the time.",
      "effect_on_reasoning_or_decision": "The loss-framed communication increased persistence on an unsuccessful reconciliation beyond what a neutral or gain-framed formulation would likely have produced.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up.",
          "evidence_explanation": "Shows the loss-frame language was disproportionately influential in how the participant weighed the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have.",
          "evidence_explanation": "Directly states that the loss framing changed the perceived weight of stopping and likely affected the decision to persist."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized that the framing affected him more than it objectively should have, and the discrepancy was eventually flagged; however, this recognition came after the additional effort.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported loss aversion; label assigned from established behavioral-decision knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": ["Representativeness bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge probability or category membership by similarity to a prototype or typical example rather than by objective criteria or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "New referral screening prioritization",
      "decision_point_description": "Prioritizing the new referral in the screening queue based on initial impression of fit.",
      "affected_reasoning_operation": "Eligibility screening and queue prioritization",
      "bias_specific_mechanism": "The participant compared the referral to the prototype of the typical enrolled patient (older with multiple comorbidities) and judged him unlikely to qualify, despite eligibility criteria being objective and not based on that prototype.",
      "manifestation_in_interview": "The participant states his first reaction was based on the patient's picture and that he deprioritized him because he did not match the pattern of typical participants.",
      "effect_on_reasoning_or_decision": "The referral was placed lower in the queue and screening was delayed; he happened to meet all inclusion criteria when screened.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions.",
          "evidence_explanation": "Shows the participant immediately assessed the candidate against a prototype rather than the objective eligibility criteria."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has.",
          "evidence_explanation": "Acknowledges that the initial judgment was based on a picture/prototype and explicitly contrasts it with objective criteria."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway.",
          "evidence_explanation": "Demonstrates that the prototype-based judgment changed the screening behavior and not merely a passing thought."
        }
      ],
      "correction_or_counterevidence": "He met every inclusion criterion when screened; the participant also stated in hindsight that the deprioritization was not based on the actual criteria but on the pattern he was used to seeing.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "A retrieved clinical decision-support source references representativeness bias in clinical judgment, supporting the use of the label, though it does not provide a formal definition.",
      "corpus_evidence": [
        {
          "source_identifier": "Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf",
          "paper_title": "Mitigating cognitive bias with clinical decision support systems: an experimental study",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "a description of a clinical  manipulation to encourage  representativeness bias",
          "mechanism_supported_by_source": "The source treats representativeness bias as a bias that can be encouraged in clinical-case judgment, which supports classifying prototype-based clinical screening decisions under this label.",
          "relevance_to_this_occurrence": "The participant used a typical-patient prototype rather than objective clinical-trial eligibility criteria, consistent with representativeness-based judgment."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Bandwagon effect",
      "alternative_labels": ["Social proof bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to adopt a behavior or belief because many others are doing so, often without critically evaluating independent evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Source data verification method switch before data lock",
      "decision_point_description": "Switching to a quicker source data verification approach after hearing other sites had adopted it.",
      "affected_reasoning_operation": "Evaluation of verification methods and adoption decision",
      "bias_specific_mechanism": "The majority behavior of other sites was used as evidence that the new method was acceptable, replacing the need for validation data or documented rationale.",
      "manifestation_in_interview": "The participant reports that hearing most other sites had switched made staying with the old method feel like being behind, and that he switched without seeking error-rate data.",
      "effect_on_reasoning_or_decision": "The site switched methods without documented rationale or validation data, despite its existing method having passed every audit.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever.",
          "evidence_explanation": "Shows the decision context contained social information about others' behavior but no independent validation data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.",
          "evidence_explanation": "Attributes the decision to the number of other sites adopting the method rather than to independent evidence of accuracy or reliability."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have a great answer beyond 'everyone else was doing it too.'",
          "evidence_explanation": "Confirms the absence of independent justification and the social-source basis for the switch."
        }
      ],
      "correction_or_counterevidence": "The monitor later asked why the method was changed without documented rationale, and the participant could not provide a non-social justification.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported the bandwagon effect; label assigned from established social-influence knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Need for closure",
      "alternative_labels": ["Ambiguity aversion"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Participant 12 AE causality classification",
      "supporting_interview_quote": "But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.",
      "plausible_mechanism": "A motivational preference for a definite, closable classification may have made the participant avoid the ambiguous 'possibly related' category.",
      "why_not_identified": "The statement could also reflect ordinary workload management or uncertainty under time pressure, and the transcript does not show a bias-specific need-for-closure mechanism separate from the availability heuristic already identified."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus fragments were sparse and not directly specific to every identified label; some labels rely on established general knowledge.",
    "Transcripts are self-reports and may understate or rationalize decisions, though findings are based on explicit stated mechanisms."
  ]
}

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time this week of all weeks. Before we start, this is just for our internal process-improvement review — I'll ask you to walk me through a recent stretch of work, and there's no wrong answer. That okay? Participant: Sure, happy to. Lock week is a good time to talk about it, honestly, everything's still fresh. Interviewer: Great. Can you remind me of your role and what was on your plate? Participant: I'm the CRC for our site on the Phase III trial — the oncology drug study. I handle adverse event triage, case report form cleanup, and screening new referrals. That week we were seven days out from the interim data lock for the DSMB, so basically everything converged at once. Interviewer: Walk me through what that week looked like. Participant: Monday morning I got a lab flag on Participant 12 — an ALT elevation, elevated but not dramatically so, and the timeline relative to dosing wasn't clean. Could've been drug-related, could've been something else entirely, maybe even diet or an OTC medication he didn't mention. I had to assign a causality category for the AE report. Same day, I was also mid-reconciliation on Participant 07's case report forms — that one had been a slog for almost two weeks, lots of inconsistent entries between the source charts and the CRF. Then Wednesday a new referral came in for screening, and Thursday there was a multi-site coordinator call about verification procedures ahead of lock. So four distinct things, all against the same deadline. Interviewer: Let's start with Participant 12. What did you have in front of you? Participant: His ALT was elevated, but in a range where you genuinely can't tell just from the number whether it's the study drug. Our protocol has three buckets — related, possibly related, unrelated — for exactly this kind of situation. I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point. Interviewer: How did that shape the classification? Participant: I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed. Interviewer: What about the 'possibly related' option? Participant: Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side. Interviewer: What happened after? Participant: The PI actually asked me to go back and pull his full lab history and prior meds before finalizing it. Which, fair — I probably should've done that up front instead of after. Interviewer: Let's move to Participant 07. Participant: That one's been painful. I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records. Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that. Interviewer: What did you do with that discrepancy? Participant: I kept going. Twenty hours felt like too much to walk away from without one more push. And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up. So I dug in for another few hours trying to resolve it. Interviewer: Did you consider flagging it as a deviation instead? Participant: I did — that was one of the options on the table, along with getting a second reviewer to look before deciding. But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours. Interviewer: How did it turn out? Participant: The discrepancy wasn't resolvable from what we had. The source documents just didn't exist to fix it. So the extra time didn't change the outcome — we flagged it anyway, just later. Interviewer: Let's talk about the new referral on Wednesday. Participant: He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has. Interviewer: What did you do with that instinct? Participant: I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway. In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through. Interviewer: What happened when you did screen him? Participant: He met every inclusion criterion. Clean screen, no issues. Which doesn't tell you much either way about whether deprioritizing him was the right call — I just got lucky that lock week didn't cost us his enrollment. Interviewer: Last one — the coordinator call about verification. Participant: Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever. Interviewer: What made you switch? Participant: Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine. Interviewer: Any pushback since? Participant: The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond 'everyone else was doing it too.' Interviewer: If you could go back, what single piece of information would have changed any of these calls? Participant: For Participant 12, if I'd pulled his full history first instead of after, I might not have leaned so hard on that other case. For the verification switch, actual error-rate data would've mattered — I just didn't have it and didn't chase it down in time. Interviewer: What if that Monday meeting about the other participant's enzyme case had never come up? Participant: I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind. Interviewer: And if the Site Director's email had framed Participant 07 differently — say, just asking whether continued reconciliation was worth the time? Participant: I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have. Interviewer: Last one — if none of the other sites had mentioned switching methods on that call? Participant: I probably would've stuck with what we had. It's passed every audit. There wasn't really a problem to solve, other than speed.

_ranker=rrf · t=0.04 · k=25 → 25 in context · 8192 ctx · emb 3.23s · gen 260.44s · total 266.2s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0249 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0246 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0242 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
5. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0237 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
6. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0201 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0199 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0191 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
9. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
10. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0191 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
11. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0188 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
12. **Hallihan_etal_DTM_12.pdf** — 0.0183 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
13. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0173 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
14. **Hallihan_etal_DTM_12.pdf** — 0.0173 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0173 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0173 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0163 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
21. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0163 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
23. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
25. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of the interview transcript for affirmatively demonstrated cognitive biases. Retrieved corpus passages were used only where they directly supported a label or domain relevance; no experimental condition was inferred."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
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
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood, relevance, or diagnostic weight of an event or category by the ease with which examples come to mind, rather than by objective similarity or complete evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 12 ALT causality classification",
      "decision_point_description": "Assigning a causality category—related, possibly related, or unrelated—for Participant 12's ALT elevation in an adverse event report.",
      "affected_reasoning_operation": "causal classification and evidence weighting",
      "bias_specific_mechanism": "A recent, vivid discussion about a different participant's enzyme elevation became highly accessible in memory. It was used as the primary comparison point, displacing less immediately available but more diagnostic information from Participant 12's own chart.",
      "manifestation_in_interview": "The participant stated that the recent team meeting about another participant was the first thing that came to mind and that he leaned on that case because it was vivid, not because it was the most similar case.",
      "effect_on_reasoning_or_decision": "The participant leaned toward classifying Participant 12's ALT elevation as unrelated, despite acknowledging that the ambiguous data actually supported 'possibly related' more strongly.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.",
          "evidence_explanation": "Directly shows a mentally available recent case becoming the comparison point before a full file review."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file.",
          "evidence_explanation": "The participant explicitly identifies a distortion: the classification was driven by vividness and accessibility rather than diagnostic fit."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind.",
          "evidence_explanation": "The counterfactual confirms that the accessible example, not intrinsic case features, altered the review process."
        }
      ],
      "correction_or_counterevidence": "The PI later asked the participant to pull the full lab history and prior medications before finalizing, but the initial classification was already influenced by the available comparison case.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support was unavailable for this specific bias; classification relies on established cognitive-science knowledge of the availability heuristic.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": ["escalation of commitment", "sunk cost effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an endeavor because of previously invested resources such as time, effort, or money, even when current evidence favors stopping or changing course.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 CRF reconciliation discrepancy",
      "decision_point_description": "Whether to continue trying to resolve a large dosing record discrepancy or stop and flag it as a deviation and/or obtain a second review.",
      "affected_reasoning_operation": "resource allocation and continuation decision",
      "bias_specific_mechanism": "The previous roughly twenty hours of reconciliation effort made stopping feel like wasting already sunk resources, driving additional hours of work despite explicit alternative options such as flagging the deviation or getting a second reviewer.",
      "manifestation_in_interview": "The participant stated that twenty hours felt like too much to walk away from and that stopping felt like it would waste everything already done.",
      "effect_on_reasoning_or_decision": "The participant continued working for additional hours even though the discrepancy ultimately could not be resolved and was later flagged as a deviation anyway.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data.",
          "evidence_explanation": "Establishes the substantial prior investment that became the basis for continued commitment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Twenty hours felt like too much to walk away from without one more push.",
          "evidence_explanation": "Explicitly shows sunk cost reasoning: the prior investment, rather than current evidence, drove the decision to continue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours.",
          "evidence_explanation": "Confirms that avoiding the perceived waste of prior effort influenced the continuation decision."
        }
      ],
      "correction_or_counterevidence": "The participant did consider flagging the discrepancy or getting a second reviewer, but the sunk cost reaction operated before those alternatives were pursued. The extra time did not change the outcome.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support was unavailable for this specific bias; classification relies on established cognitive-science knowledge of the sunk cost fallacy and escalation of commitment.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "framing effect",
      "alternative_labels": ["loss aversion", "valence framing"],
      "taxonomy_status": "established_label",
      "bias_definition": "The influence on judgment and choice caused by whether options or outcomes are presented in terms of losses versus gains, even when the underlying information is equivalent.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 CRF reconciliation discrepancy",
      "decision_point_description": "Whether continued reconciliation was worth additional time after the Site Director's email framed the situation as a potential loss of evaluable participants.",
      "affected_reasoning_operation": "risk and effort evaluation",
      "bias_specific_mechanism": "The Site Director's email cast the decision as avoiding a loss—losing one-fifth of the evaluable per-protocol population—rather than as a neutral evaluation of whether continued reconciliation was worthwhile. The participant adopted this loss frame, making stopping feel heavier than it otherwise might have.",
      "manifestation_in_interview": "The participant reported that the 'losing a fifth of our population' framing stuck with him and changed the decision from being mainly about hours to being about what would be given up.",
      "effect_on_reasoning_or_decision": "The loss frame contributed to the participant's choice to keep working. He later said he might have stopped sooner under a neutral framing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that.",
          "evidence_explanation": "Shows the decision was explicitly introduced through a loss-oriented frame."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up.",
          "evidence_explanation": "The participant explicitly reports that the loss framing altered his evaluation of the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have.",
          "evidence_explanation": "The counterfactual directly supports that the loss framing, rather than only operational content, affected the choice."
        }
      ],
      "correction_or_counterevidence": "There was a real operational concern about losing evaluable participants, but the participant's own account indicates the loss framing affected him beyond the underlying information.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support was unavailable for this specific bias; classification relies on established cognitive-science knowledge of framing effects and loss aversion.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": ["representativeness bias", "prototype heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging likelihood, suitability, or category membership based on similarity to a prototype or stereotype, rather than on objective diagnostic criteria or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Wednesday new referral screening prioritization",
      "decision_point_description": "Prioritizing a new referral for screening during lock week.",
      "affected_reasoning_operation": "probability judgment and triage decision",
      "bias_specific_mechanism": "The participant evaluated the new referral by resemblance to the typical enrolled patient prototype—older with two or three comorbidities—even though the formal eligibility criteria did not include age or comorbidity count. This prototype mismatch led to a lower subjective belief that the referral would qualify.",
      "manifestation_in_interview": "The participant said his first reaction was that the patient probably was not a good fit based on the picture of him, and that this was not based on anything in the actual eligibility criteria but on not matching the pattern he was used to seeing.",
      "effect_on_reasoning_or_decision": "The referral was placed lower in the screening queue. The patient later met every inclusion criterion.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like.",
          "evidence_explanation": "Shows the reasoning was anchored to a typical-patient prototype rather than formal criteria."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has.",
          "evidence_explanation": "Explicitly contrasts an objective evidentiary standard with the participant's prototype-based initial judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through.",
          "evidence_explanation": "Confirms the decision was representativeness-driven rather than criteria-driven."
        }
      ],
      "correction_or_counterevidence": "The patient was eventually screened and met every inclusion criterion. The participant noted that this did not retrospectively prove the deprioritization was correct.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus explicitly named representativeness bias in a clinical decision support research context, providing label validation for this occurrence.",
      "corpus_evidence": [
        {
          "source_identifier": "Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf",
          "paper_title": "Mitigating cognitive bias with clinical decision support systems: an experimental study",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "a description of a clinical manipulation to encourage representativeness bias and Josephson (Richie a way that the participant increases the chance of tion presented in the targeted diagnosis.",
          "mechanism_supported_by_source": "The source explicitly refers to representativeness bias as a target for clinical decision support research, validating the established label and clinical relevance.",
          "relevance_to_this_occurrence": "Supports the use of the representativeness bias label in a clinical screening judgment context that mirrors the participant's prototype-based referral triage reasoning."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "bandwagon effect",
      "alternative_labels": ["social proof", "conformity bias", "herd behavior"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive-social influence in which people adopt a practice, judgment, or belief because many others appear to be doing so, often without independently evaluating the supporting evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Thursday multi-site coordinator call: source data verification method switch",
      "decision_point_description": "Whether to switch from the site's audit-clean source data verification approach to a quicker method already adopted by other sites.",
      "affected_reasoning_operation": "evidence evaluation and adoption decision",
      "bias_specific_mechanism": "The number of other sites adopting the quicker method served as social proof. This made the participant feel behind and led him to switch without seeking error-rate data or documenting an independent rationale.",
      "manifestation_in_interview": "The participant reported that hearing most other sites had moved made staying with the old method feel like being behind, and that he did not look for validation data before switching.",
      "effect_on_reasoning_or_decision": "The site changed verification methods without a documented rationale, and the monitor later questioned the decision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster.",
          "evidence_explanation": "Identifies the social information that triggered the adoption decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.",
          "evidence_explanation": "Shows the bandwagon mechanism: adoption followed perceived consensus rather than independent evidence review."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond 'everyone else was doing it too.'",
          "evidence_explanation": "Confirms the lack of an independent rationale beyond social proof."
        }
      ],
      "correction_or_counterevidence": "The monitor's challenge came after the fact. There is no evidence in the transcript that the participant sought validation data before switching.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Corpus support was unavailable for this specific bias; classification relies on established cognitive-science knowledge of the bandwagon effect and social proof.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "ambiguity aversion",
      "alternative_labels": ["need for closure", "need for cognitive closure"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Participant 12 ALT causality classification",
      "supporting_interview_quote": "Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.",
      "plausible_mechanism": "Avoidance of an ambiguous, burdensome causality category may have pushed the participant toward a more definitive 'unrelated' classification.",
      "why_not_identified": "The transcript clearly shows motivational pressure toward closure, but it is difficult to separate this from ordinary deadline-driven workload management and from the already-identified availability heuristic. A distinct, bias-specific distortion is plausible but not sufficiently isolated for a positive identification."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is retrospective self-report; findings depend on the participant's recall and articulation of past reasoning.",
    "No independent verification of the reported decisions, records, or outcomes was available.",
    "Retrieved corpus support was limited and uneven; several classifications rely on established cognitive-science knowledge rather than supplied passages.",
    "Some decision episodes contain multiple interacting biases, making mechanism separation partly interpretive, though each reported occurrence was tied to explicit transcript evidence."
  ]
}
