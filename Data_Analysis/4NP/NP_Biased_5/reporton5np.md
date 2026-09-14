# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm trying to understand your reasoning process during the AFW procedure revision, not evaluating performance. Everything stays de-identified in my notes. Sound okay? Participant: Sure, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me what this revision was for and why it came up? Participant: So we had a design change package come through — the legacy analog level transmitter on one of the AFW trains got swapped for a new digital unit. Different response curve, different failure modes than what the old EOP steps were written around. My job was to update the Emergency Operating Procedure sequence so the initiation steps matched the new instrumentation, get it through V&V and human-factors review, and have it ready before the outage window opened. We had about three days. Interviewer: What was your main objective going in? Participant: Get an accurate, defensible procedure revision done on time. Accurate matters obviously, but the deadline was real — outage planning had already built the implementation window around this, so slipping it wasn't really an option without a whole scheduling conversation nobody wanted to have. Interviewer: Walk me through the incident from the beginning. Participant: Right when I started, an industry OE report landed in my queue — a transmitter failure at another station involving a new digital level transmitter. My first reaction was, okay, this is directly relevant, new digital unit, level transmitter, similar failure. I started pulling language from it into my draft pretty quickly. It was only later, when I looped in the I&C engineer who'd actually executed our design change, that he pointed out the OE unit used a different sensing technology than ours — different vendor family entirely. So the applicability wasn't as clean as I'd assumed. From there I moved into drafting the actual verification steps. The new transmitter needed a two-point calibration check that the old analog unit never required. I've written a lot of these AFW revisions over the years, so I built the verification section using the template sequence I normally use. That went to peer review, and the reviewer caught that the calibration check wasn't in there at all — I'd basically carried over the old pattern without building it fresh around the new requirement. Interviewer: What happened next? Participant: I had to set validation criteria — basically, what surveillance test data to use as the benchmark for confirming the new steps work as intended. We've got five years of AFW surveillance history, but I also had a test from two weeks earlier on a different, unrelated procedure that happened to use a similar-looking verification form. That one was fresh in my head, so I anchored the validation criteria around it. Turned out later, when someone did a fuller data pull, that some of the older historical tests actually covered operating conditions closer to this transmitter's actual fault signature than the recent one did. Interviewer: And the final stretch? Participant: Last day, deadline under 24 hours out. I wanted to check the OE database more thoroughly, but part of it was locked because of a concurrent audit. So I worked off what I had — control room log, my own notes — and judged that was enough to close it out. I did a mental run-through of the failure modes and figured we'd covered the main ones, so I signed off and sent it to the approval board. They came back afterward asking for a supplemental risk note because there was a failure mode the draft hadn't addressed. Interviewer: Let's go back to that OE report moment. What specifically made you decide it applied to your transmitter? Participant: Honestly, the framing — 'new digital level transmitter failure' — matched our situation closely enough that it registered as the same kind of event. I didn't stop to verify the sensing technology before I started drafting around it. In hindsight I probably should've asked the I&C engineer first, but it read as applicable on its face. Interviewer: What alternatives did you consider there? Participant: I could've tabled it as low relevance until I confirmed equivalence, or gone straight to the I&C engineer before touching the draft. I didn't do either — I just moved forward with incorporating it. Interviewer: On the verification steps — what sources did you actually rely on when drafting? Participant: Mostly my own prior work. I've done this enough times that I have a rhythm to how these sections get built. I did have the design change package open, but I wrote the structure first and meant to reconcile it against the specific requirements after — that reconciliation step is where the calibration check got missed. Interviewer: Was consulting the I&C engineer before drafting ever on the table? Participant: It was an option. I just didn't think I needed it at that stage — this felt like standard territory. Interviewer: How did you decide which historical test data to weight most heavily for the validation criteria? Participant: The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes. In hindsight, the older data had more operating conditions represented. Interviewer: When time got short at the end, how did you decide the draft was ready to submit? Participant: I looked at what was actually accessible — the control room log, my notes — and it felt like enough to call it done. The audit had the fuller OE records locked up, and requesting an extension felt like it would just push the whole outage schedule, so I didn't pursue that. On the risk side, I ran through the failure modes I could recall from the design package, felt like the major ones were addressed, and made the call that residual risk was acceptable. Interviewer: Did escalating to the Shift Technical Advisor come up as an option? Participant: It did cross my mind, but I didn't think the open question was significant enough to escalate at the time. Interviewer: If you'd had another full day for the OE report review, would you have handled that differently? Participant: Probably — I'd have gotten the I&C engineer's read on technical equivalence before drafting anything, rather than after. Interviewer: If the audit hadn't locked the database, what would you have checked? Participant: I'd have wanted to search for any other OE items involving this exact transmitter model, and cross-check the failure-mode list more completely instead of relying on memory. Interviewer: Looking back, is there a point you'd have wanted a second set of eyes earlier? Participant: Probably right after the OE report came in, before I started building language around it. Interviewer: How confident were you in that final risk judgment at the time, compared to now? Participant: At the time, reasonably confident — it felt sufficient given what I had access to. Now, knowing the board found a gap, I'd say I was more confident than the evidence actually supported. Interviewer: That's really helpful. Thanks for walking through all of that in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.83s · gen 239.84s · total 243.9s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0305 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0292 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0263 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0239 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0222 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0210 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0206 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
12. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0206 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
13. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0202 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
14. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0188 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0182 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
16. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0180 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
17. **Hallihan_etal_DTM_12.pdf** — 0.0180 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
18. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0179 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
19. **Lyell Automation bias and verification complexity.pdf** — 0.0177 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
20. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0177 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
21. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
24. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0164 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
25. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
28. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
29. **Hallihan_etal_DTM_12.pdf** — 0.0158 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
30. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
32. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0155 (rrf) — _# Cognitive Bias in the Verification and Validation o This research was carried out at the Jet P_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0155 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
34. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0154 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
35. **Hallihan_etal_DTM_12.pdf** — 0.0154 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
36. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0154 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
37. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0154 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
38. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0154 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0154 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
41. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
44. **Hallihan_etal_DTM_12.pdf** — 0.0147 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0146 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Blind to experimental condition; evaluated the transcript for affirmatively demonstrated cognitive bias mechanisms, using retrieved corpus material only where it directly supported a label, definition, or mechanism."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Einstellung effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Recency effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": [
        "Representativeness bias",
        "Similarity heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A judgment shortcut in which an object or event is categorized or evaluated based on its surface similarity to a prototypical case rather than on diagnostic, structural, or statistical features.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial OE report applicability assessment",
      "decision_point_description": "Deciding whether the incoming industry operating experience report was relevant enough to use in the draft before verifying technical equivalence.",
      "affected_reasoning_operation": "Categorization and relevance judgment",
      "bias_specific_mechanism": "The participant evaluated the incoming OE report as applicable based on surface wording and event framing, particularly the phrase 'new digital level transmitter failure,' rather than on diagnostic technical attributes such as sensing technology or vendor family. This similarity match triggered a rapid relevance judgment and drafting action before verification.",
      "manifestation_in_interview": "The participant described the OE report as 'directly relevant' and began pulling language from it into the draft quickly, only later learning from the I&C engineer that the OE unit used a different sensing technology and vendor family.",
      "effect_on_reasoning_or_decision": "It caused potentially inapplicable OE language to be incorporated into the draft, requiring later correction by the I&C engineer.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right when I started, an industry OE report landed in my queue — a transmitter failure at another station involving a new digital level transmitter. My first reaction was, okay, this is directly relevant, new digital unit, level transmitter, similar failure. I started pulling language from it into my draft pretty quickly.",
          "evidence_explanation": "Shows immediate surface-similarity classification and premature drafting action before verifying technical equivalence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the framing — 'new digital level transmitter failure' — matched our situation closely enough that it registered as the same kind of event. I didn't stop to verify the sensing technology before I started drafting around it.",
          "evidence_explanation": "Explicitly identifies surface framing as the cue for relevance and confirms that diagnostic technical attributes were not verified first."
        }
      ],
      "correction_or_counterevidence": "The I&C engineer later pointed out that the OE unit used a different sensing technology and vendor family; the participant acknowledged that applicability was not as clean as initially assumed. Time pressure was present but does not explain the failure to verify technical equivalence before drafting.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a definition or mechanism for representativeness or similarity-based categorization. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Einstellung effect",
      "alternative_labels": [
        "Mental set",
        "Habit interference",
        "Negative transfer"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for an existing successful solution method, routine, or mental set to persist and inhibit the generation of new task-appropriate procedures when task demands change.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Verification section drafting",
      "decision_point_description": "Choosing how to structure the verification section for the new digital transmitter.",
      "affected_reasoning_operation": "Procedure construction and generation of task-specific steps",
      "bias_specific_mechanism": "The participant's repeated prior experience writing AFW revisions created a routinized template or mental set. When the design change introduced a new two-point calibration check, he defaulted to the old verification structure and did not build the section freshly around the new requirement, resulting in omission of the calibration check.",
      "manifestation_in_interview": "The participant stated that he built the verification section using the template sequence he normally used and that he had carried over the old pattern rather than building it fresh around the new calibration requirement.",
      "effect_on_reasoning_or_decision": "The draft verification section omitted the required two-point calibration check, requiring peer-review correction.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "From there I moved into drafting the actual verification steps. The new transmitter needed a two-point calibration check that the old analog unit never required. I've written a lot of these AFW revisions over the years, so I built the verification section using the template sequence I normally use.",
          "evidence_explanation": "Indicates prior routine and template use dominated construction of the new verification section."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That went to peer review, and the reviewer caught that the calibration check wasn't in there at all — I'd basically carried over the old pattern without building it fresh around the new requirement.",
          "evidence_explanation": "Demonstrates habitual carryover of the old procedure pattern and omission of the new requirement."
        }
      ],
      "correction_or_counterevidence": "The omission was caught by peer review before final implementation. A possible non-bias explanation is incomplete reconciliation under workload or time pressure, but the participant explicitly links the error to reliance on his usual template.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a definition or mechanism for the Einstellung effect or mental set. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Recency effect",
      "alternative_labels": [
        "Availability heuristic",
        "Serial-position recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for recent experiences or information to be more available in memory and therefore to exert disproportionate influence on subsequent judgments or choices.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Validation criteria selection",
      "decision_point_description": "Selecting historical test data to use as the benchmark for validation criteria.",
      "affected_reasoning_operation": "Evidence weighting and benchmark selection",
      "bias_specific_mechanism": "A two-week-old test from an unrelated procedure was highly accessible because the participant had looked at it recently. This recency-driven accessibility made it appear to be a reasonable proxy, so it was selected as the validation benchmark without systematic comparison against the larger five-year historical data set.",
      "manifestation_in_interview": "The participant described the recent test as 'fresh in my head' and 'top of mind' and reported not systematically comparing it with older historical tests that were later found more relevant.",
      "effect_on_reasoning_or_decision": "Validation criteria were anchored to a less relevant recent test, while older historical tests with closer operating conditions were underweighted or ignored.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We've got five years of AFW surveillance history, but I also had a test from two weeks earlier on a different, unrelated procedure that happened to use a similar-looking verification form. That one was fresh in my head, so I anchored the validation criteria around it.",
          "evidence_explanation": "Shows recency and salience of the two-week-old test directly influenced benchmark selection."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes.",
          "evidence_explanation": "Confirms the choice was driven by recent exposure and accessibility rather than a systematic evaluation of diagnostic relevance."
        }
      ],
      "correction_or_counterevidence": "A later fuller data pull showed older historical tests covered operating conditions closer to the transmitter's actual fault signature, and the participant acknowledged this in hindsight.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved usability-testing source provides a definition of the recency effect, supporting the mechanism of recent events being more memorable and influencing judgment.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "The source describes recency as a memory accessibility effect in which recent events are more clearly remembered and can therefore bias subsequent reports or judgments.",
          "relevance_to_this_occurrence": "The participant explicitly used the recent two-week-old test because it was 'fresh in my head' and 'top of mind,' consistent with recency-based accessibility rather than diagnostic relevance."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Overconfidence bias",
        "Miscalibration of confidence"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to have greater confidence in one's judgments, knowledge, or risk assessments than is warranted by the available evidence or achieved accuracy.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final readiness and risk sign-off",
      "decision_point_description": "Deciding whether the draft was ready for submission and whether residual risk was acceptable under deadline and access constraints.",
      "affected_reasoning_operation": "Risk assessment and self-monitoring/judgment calibration",
      "bias_specific_mechanism": "With incomplete access to the OE database and a deadline, the participant relied on mental recall of failure modes, judged the accessible information sufficient, and declined to escalate or request an extension. Subjective confidence in the completeness of the risk review exceeded the evidentiary basis.",
      "manifestation_in_interview": "The participant signed off after a mental run-through of failure modes and later stated he was more confident than the evidence supported. Escalating to the Shift Technical Advisor crossed his mind but was not pursued.",
      "effect_on_reasoning_or_decision": "The procedure was submitted without a supplemental risk note, and the approval board later identified an unaddressed failure mode.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "On the risk side, I ran through the failure modes I could recall from the design package, felt like the major ones were addressed, and made the call that residual risk was acceptable.",
          "evidence_explanation": "Shows a subjective completeness judgment based on recall, supporting the overconfidence mechanism in the final risk decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At the time, reasonably confident — it felt sufficient given what I had access to. Now, knowing the board found a gap, I'd say I was more confident than the evidence actually supported.",
          "evidence_explanation": "Direct self-assessment of miscalibration between confidence and the actual evidential basis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It did cross my mind, but I didn't think the open question was significant enough to escalate at the time.",
          "evidence_explanation": "Indicates the overconfident judgment also suppressed an available escalation path."
        }
      ],
      "correction_or_counterevidence": "The approval board later requested a supplemental risk note after finding an unaddressed failure mode. Locked database access and deadline pressure are contextual constraints, but the overconfidence occurred in the calibration of subjective confidence to the information the participant did have.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a definition or mechanism for overconfidence or confidence miscalibration. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring and insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Validation criteria selection",
      "supporting_interview_quote": "The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes.",
      "plausible_mechanism": "The recent test may have served as an initial anchor for validation criteria, with insufficient adjustment toward the older historical dataset.",
      "why_not_identified": "The transcript more directly supports a recency/availability mechanism for why the recent test was selected; anchoring is plausible but not as distinctly evidenced."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Plan continuation error",
        "Get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final submission under deadline",
      "supporting_interview_quote": "The audit had the fuller OE records locked up, and requesting an extension felt like it would just push the whole outage schedule, so I didn't pursue that.",
      "plausible_mechanism": "Commitment to the existing implementation timeline may have reduced willingness to request an extension or escalate despite an open risk question.",
      "why_not_identified": "Time pressure and audit lock are strong structural constraints; the transcript does not clearly demonstrate a distinct plan-continuation cognitive mechanism independent of those constraints."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview transcript contains only self-reported reasoning; no behavioral, eye-tracking, process, or design-change telemetry was available.",
    "Retrieved corpus support was limited and did not cover all identified bias labels.",
    "Several decisions occurred under schedule and access constraints, so bias attributions are conservative and probabilistic."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm trying to understand your reasoning process during the AFW procedure revision, not evaluating performance. Everything stays de-identified in my notes. Sound okay? Participant: Sure, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me what this revision was for and why it came up? Participant: So we had a design change package come through — the legacy analog level transmitter on one of the AFW trains got swapped for a new digital unit. Different response curve, different failure modes than what the old EOP steps were written around. My job was to update the Emergency Operating Procedure sequence so the initiation steps matched the new instrumentation, get it through V&V and human-factors review, and have it ready before the outage window opened. We had about three days. Interviewer: What was your main objective going in? Participant: Get an accurate, defensible procedure revision done on time. Accurate matters obviously, but the deadline was real — outage planning had already built the implementation window around this, so slipping it wasn't really an option without a whole scheduling conversation nobody wanted to have. Interviewer: Walk me through the incident from the beginning. Participant: Right when I started, an industry OE report landed in my queue — a transmitter failure at another station involving a new digital level transmitter. My first reaction was, okay, this is directly relevant, new digital unit, level transmitter, similar failure. I started pulling language from it into my draft pretty quickly. It was only later, when I looped in the I&C engineer who'd actually executed our design change, that he pointed out the OE unit used a different sensing technology than ours — different vendor family entirely. So the applicability wasn't as clean as I'd assumed. From there I moved into drafting the actual verification steps. The new transmitter needed a two-point calibration check that the old analog unit never required. I've written a lot of these AFW revisions over the years, so I built the verification section using the template sequence I normally use. That went to peer review, and the reviewer caught that the calibration check wasn't in there at all — I'd basically carried over the old pattern without building it fresh around the new requirement. Interviewer: What happened next? Participant: I had to set validation criteria — basically, what surveillance test data to use as the benchmark for confirming the new steps work as intended. We've got five years of AFW surveillance history, but I also had a test from two weeks earlier on a different, unrelated procedure that happened to use a similar-looking verification form. That one was fresh in my head, so I anchored the validation criteria around it. Turned out later, when someone did a fuller data pull, that some of the older historical tests actually covered operating conditions closer to this transmitter's actual fault signature than the recent one did. Interviewer: And the final stretch? Participant: Last day, deadline under 24 hours out. I wanted to check the OE database more thoroughly, but part of it was locked because of a concurrent audit. So I worked off what I had — control room log, my own notes — and judged that was enough to close it out. I did a mental run-through of the failure modes and figured we'd covered the main ones, so I signed off and sent it to the approval board. They came back afterward asking for a supplemental risk note because there was a failure mode the draft hadn't addressed. Interviewer: Let's go back to that OE report moment. What specifically made you decide it applied to your transmitter? Participant: Honestly, the framing — 'new digital level transmitter failure' — matched our situation closely enough that it registered as the same kind of event. I didn't stop to verify the sensing technology before I started drafting around it. In hindsight I probably should've asked the I&C engineer first, but it read as applicable on its face. Interviewer: What alternatives did you consider there? Participant: I could've tabled it as low relevance until I confirmed equivalence, or gone straight to the I&C engineer before touching the draft. I didn't do either — I just moved forward with incorporating it. Interviewer: On the verification steps — what sources did you actually rely on when drafting? Participant: Mostly my own prior work. I've done this enough times that I have a rhythm to how these sections get built. I did have the design change package open, but I wrote the structure first and meant to reconcile it against the specific requirements after — that reconciliation step is where the calibration check got missed. Interviewer: Was consulting the I&C engineer before drafting ever on the table? Participant: It was an option. I just didn't think I needed it at that stage — this felt like standard territory. Interviewer: How did you decide which historical test data to weight most heavily for the validation criteria? Participant: The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes. In hindsight, the older data had more operating conditions represented. Interviewer: When time got short at the end, how did you decide the draft was ready to submit? Participant: I looked at what was actually accessible — the control room log, my notes — and it felt like enough to call it done. The audit had the fuller OE records locked up, and requesting an extension felt like it would just push the whole outage schedule, so I didn't pursue that. On the risk side, I ran through the failure modes I could recall from the design package, felt like the major ones were addressed, and made the call that residual risk was acceptable. Interviewer: Did escalating to the Shift Technical Advisor come up as an option? Participant: It did cross my mind, but I didn't think the open question was significant enough to escalate at the time. Interviewer: If you'd had another full day for the OE report review, would you have handled that differently? Participant: Probably — I'd have gotten the I&C engineer's read on technical equivalence before drafting anything, rather than after. Interviewer: If the audit hadn't locked the database, what would you have checked? Participant: I'd have wanted to search for any other OE items involving this exact transmitter model, and cross-check the failure-mode list more completely instead of relying on memory. Interviewer: Looking back, is there a point you'd have wanted a second set of eyes earlier? Participant: Probably right after the OE report came in, before I started building language around it. Interviewer: How confident were you in that final risk judgment at the time, compared to now? Participant: At the time, reasonably confident — it felt sufficient given what I had access to. Now, knowing the board found a gap, I'd say I was more confident than the evidence actually supported. Interviewer: That's really helpful. Thanks for walking through all of that in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.73s · gen 217.57s · total 221.3s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0305 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0292 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0263 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0239 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0222 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0210 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0206 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
12. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0206 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
13. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0202 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
14. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0188 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0182 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
16. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0180 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
17. **Hallihan_etal_DTM_12.pdf** — 0.0180 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
18. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0179 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
19. **Lyell Automation bias and verification complexity.pdf** — 0.0177 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
20. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0177 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
21. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
24. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0164 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
25. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
28. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
29. **Hallihan_etal_DTM_12.pdf** — 0.0158 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
30. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
32. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0155 (rrf) — _# Cognitive Bias in the Verification and Validation o This research was carried out at the Jet P_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0155 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
34. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0154 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
35. **Hallihan_etal_DTM_12.pdf** — 0.0154 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
36. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0154 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
37. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0154 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
38. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0154 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0154 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
41. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
44. **Hallihan_etal_DTM_12.pdf** — 0.0147 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0146 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the participant's reasoning during the AFW procedure revision. Only mechanisms with affirmative interview evidence were classified; situational constraints such as deadline pressure and database lockout were treated as context, not as bias by themselves."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias",
        "superficial similarity judgment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which an event or object is judged by its superficial similarity to a prototype or category rather than by diagnostic or base-rate information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Judging applicability of an industry OE report to the local digital level transmitter",
      "decision_point_description": "Whether to treat the incoming OE report as directly applicable before drafting procedure language",
      "affected_reasoning_operation": "Similarity judgment and relevance assessment",
      "bias_specific_mechanism": "The participant judged the OE report as applicable based on a surface-level match ('new digital level transmitter failure') and did not check the diagnostic feature, sensing technology/vendor family, before using the report as drafting input.",
      "manifestation_in_interview": "The participant reported that the OE report read as applicable 'on its face' and was incorporated quickly; the I&C engineer later identified a disqualifying technical difference.",
      "effect_on_reasoning_or_decision": "Led to premature use of a non-equivalent OE report as a source for procedure language, requiring later correction.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right when I started, an industry OE report landed in my queue — a transmitter failure at another station involving a new digital level transmitter. My first reaction was, okay, this is directly relevant, new digital unit, level transmitter, similar failure. I started pulling language from it into my draft pretty quickly.",
          "evidence_explanation": "Shows immediate superficial similarity-based relevance judgment and action before verifying technical equivalence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the framing — 'new digital level transmitter failure' — matched our situation closely enough that it registered as the same kind of event. I didn't stop to verify the sensing technology before I started drafting around it.",
          "evidence_explanation": "Explicitly describes prototype matching and omission of diagnostic verification, which is the core representativeness mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I could've tabled it as low relevance until I confirmed equivalence, or gone straight to the I&C engineer before touching the draft. I didn't do either — I just moved forward with incorporating it.",
          "evidence_explanation": "Confirms the participant considered more diagnostic alternatives but proceeded on the superficial similarity judgment."
        }
      ],
      "correction_or_counterevidence": "The I&C engineer later pointed out the OE unit used a different sensing technology and vendor family; the participant acknowledged in hindsight that he should have asked first. Time pressure and a plausible surface match are non-bias contributors.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the representativeness heuristic label was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and insufficient adjustment",
        "mental set",
        "Einstellung effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "An initial mental model, value, or structure exerts disproportionate influence on a subsequent judgment or construction, with insufficient adjustment away from the anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Drafting the AFW verification section for the new digital transmitter",
      "decision_point_description": "How to construct the verification steps after the transmitter change introduced a new two-point calibration check",
      "affected_reasoning_operation": "Procedure construction and generation of verification steps",
      "bias_specific_mechanism": "A highly practiced prior template for AFW verification sections served as the initial structure and was not adequately adjusted to the new requirement, so the novel calibration check was omitted.",
      "manifestation_in_interview": "The participant wrote the verification section from his usual template, intending to reconcile it against the design change package later; peer review found the required calibration check missing.",
      "effect_on_reasoning_or_decision": "Produced an incomplete draft that carried over the old pattern and missed the new two-point calibration check.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The new transmitter needed a two-point calibration check that the old analog unit never required. I've written a lot of these AFW revisions over the years, so I built the verification section using the template sequence I normally use.",
          "evidence_explanation": "States that a new requirement existed and that the participant defaulted to a familiar prior template, which is the anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly my own prior work. I've done this enough times that I have a rhythm to how these sections get built. I did have the design change package open, but I wrote the structure first and meant to reconcile it against the specific requirements after — that reconciliation step is where the calibration check got missed.",
          "evidence_explanation": "Shows an initial structure was generated from prior work and the insufficient adjustment occurred at reconciliation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That went to peer review, and the reviewer caught that the calibration check wasn't in there at all — I'd basically carried over the old pattern without building it fresh around the new requirement.",
          "evidence_explanation": "Explicitly summarizes the anchor-derived omission."
        }
      ],
      "correction_or_counterevidence": "Peer review caught the omission, and the participant acknowledged carrying over the old pattern. Possible non-bias contributors include time pressure, high task familiarity, and expert automaticity.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the anchoring bias label was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "recency effect",
      "alternative_labels": [
        "availability heuristic",
        "recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for recent information to be more accessible in memory and to disproportionately influence judgment or choice.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selecting validation criteria and benchmark surveillance data",
      "decision_point_description": "Which test data to use as the benchmark for confirming that the revised procedure worked as intended",
      "affected_reasoning_operation": "Weighting and selection of historical test data for validation criteria",
      "bias_specific_mechanism": "A two-week-old test was highly accessible because of recent exposure, and the participant treated it as a reasonable proxy without systematically comparing it against the five-year surveillance history or the transmitter's specific fault modes.",
      "manifestation_in_interview": "The participant said the recent test was 'fresh in my head' and 'top of mind' and used it to anchor the validation criteria; a later fuller data pull showed older tests were more relevant.",
      "effect_on_reasoning_or_decision": "Validation criteria were initially built around a less relevant recent test rather than more diagnostic historical data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We've got five years of AFW surveillance history, but I also had a test from two weeks earlier on a different, unrelated procedure that happened to use a similar-looking verification form. That one was fresh in my head, so I anchored the validation criteria around it.",
          "evidence_explanation": "The participant explicitly identifies recent exposure as the reason the unrelated test influenced the validation criteria; the colloquial 'anchored' reflects reliance on that accessible recent example."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes.",
          "evidence_explanation": "Directly describes recency-driven accessibility and the absence of systematic comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, the older data had more operating conditions represented.",
          "evidence_explanation": "Confirms that the recent test was less relevant, showing the biasing effect on the selection."
        }
      ],
      "correction_or_counterevidence": "A later fuller data pull revealed older historical tests were more relevant. Non-bias contributors include time pressure and the use of a similar-looking form as a heuristic proxy.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support from Natesan et al. was available for the recency effect label.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": "Natesan et al.",
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly. For example, as participants use a device, they become more familiar the Priming and Recency Effect.",
          "mechanism_supported_by_source": "Recent events are remembered more clearly and can influence judgments depending on timing and recent exposure.",
          "relevance_to_this_occurrence": "The participant stated the two-week-old test was 'fresh in my head' and 'top of mind' and used it as a proxy instead of systematically comparing older data, matching the retrieved recency effect definition."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence effect",
      "alternative_labels": [
        "overconfidence bias",
        "miscalibration"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Subjective confidence in a judgment exceeds the evidential support for, or accuracy of, that judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final readiness and residual risk judgment before approval board submission",
      "decision_point_description": "Whether the draft was complete and residual risk was acceptable under deadline and with the OE database partially locked",
      "affected_reasoning_operation": "Risk judgment and decision to submit",
      "bias_specific_mechanism": "The participant relied on the information he could access and recall, generating a subjective sense of completeness and confidence that exceeded the available evidence; he later acknowledged being more confident than the evidence supported.",
      "manifestation_in_interview": "The participant judged that major failure modes were addressed from memory, did not escalate, and submitted the draft; the approval board later requested a supplemental risk note for an unaddressed failure mode.",
      "effect_on_reasoning_or_decision": "Led to signing off and submitting without a supplemental risk note, which the approval board later required.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at what was actually accessible — the control room log, my notes — and it felt like enough to call it done. The audit had the fuller OE records locked up, and requesting an extension felt like it would just push the whole outage schedule, so I didn't pursue that.",
          "evidence_explanation": "Shows confidence based on limited accessible information and a decision to proceed rather than escalate or request more time."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "On the risk side, I ran through the failure modes I could recall from the design package, felt like the major ones were addressed, and made the call that residual risk was acceptable.",
          "evidence_explanation": "Indicates a subjective completeness judgment based on memory recall, feeding the confidence in residual risk acceptability."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At the time, reasonably confident — it felt sufficient given what I had access to. Now, knowing the board found a gap, I'd say I was more confident than the evidence actually supported.",
          "evidence_explanation": "Explicitly describes miscalibration between the participant's confidence at the time and the evidential support."
        }
      ],
      "correction_or_counterevidence": "The approval board subsequently identified an unaddressed failure mode and required a supplemental risk note. Contextual factors such as time pressure and the locked OE database are recognized non-bias contributors.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the overconfidence effect label was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Analysis is based on a single retrospective interview, so causal inference about cognitive mechanisms is limited.",
    "Some labels, including representativeness heuristic, anchoring bias, and overconfidence effect, rely on general cognitive-science knowledge because the retrieved corpus did not directly support them.",
    "Time pressure, task familiarity, inaccessible database, and expert automaticity are plausible non-bias contributors that were considered where present.",
    "The participant's retrospective statements about what he 'would have' done with more time were treated as counterfactual reflections, not as primary evidence of bias."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm trying to understand your reasoning process during the AFW procedure revision, not evaluating performance. Everything stays de-identified in my notes. Sound okay? Participant: Sure, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me what this revision was for and why it came up? Participant: So we had a design change package come through — the legacy analog level transmitter on one of the AFW trains got swapped for a new digital unit. Different response curve, different failure modes than what the old EOP steps were written around. My job was to update the Emergency Operating Procedure sequence so the initiation steps matched the new instrumentation, get it through V&V and human-factors review, and have it ready before the outage window opened. We had about three days. Interviewer: What was your main objective going in? Participant: Get an accurate, defensible procedure revision done on time. Accurate matters obviously, but the deadline was real — outage planning had already built the implementation window around this, so slipping it wasn't really an option without a whole scheduling conversation nobody wanted to have. Interviewer: Walk me through the incident from the beginning. Participant: Right when I started, an industry OE report landed in my queue — a transmitter failure at another station involving a new digital level transmitter. My first reaction was, okay, this is directly relevant, new digital unit, level transmitter, similar failure. I started pulling language from it into my draft pretty quickly. It was only later, when I looped in the I&C engineer who'd actually executed our design change, that he pointed out the OE unit used a different sensing technology than ours — different vendor family entirely. So the applicability wasn't as clean as I'd assumed. From there I moved into drafting the actual verification steps. The new transmitter needed a two-point calibration check that the old analog unit never required. I've written a lot of these AFW revisions over the years, so I built the verification section using the template sequence I normally use. That went to peer review, and the reviewer caught that the calibration check wasn't in there at all — I'd basically carried over the old pattern without building it fresh around the new requirement. Interviewer: What happened next? Participant: I had to set validation criteria — basically, what surveillance test data to use as the benchmark for confirming the new steps work as intended. We've got five years of AFW surveillance history, but I also had a test from two weeks earlier on a different, unrelated procedure that happened to use a similar-looking verification form. That one was fresh in my head, so I anchored the validation criteria around it. Turned out later, when someone did a fuller data pull, that some of the older historical tests actually covered operating conditions closer to this transmitter's actual fault signature than the recent one did. Interviewer: And the final stretch? Participant: Last day, deadline under 24 hours out. I wanted to check the OE database more thoroughly, but part of it was locked because of a concurrent audit. So I worked off what I had — control room log, my own notes — and judged that was enough to close it out. I did a mental run-through of the failure modes and figured we'd covered the main ones, so I signed off and sent it to the approval board. They came back afterward asking for a supplemental risk note because there was a failure mode the draft hadn't addressed. Interviewer: Let's go back to that OE report moment. What specifically made you decide it applied to your transmitter? Participant: Honestly, the framing — 'new digital level transmitter failure' — matched our situation closely enough that it registered as the same kind of event. I didn't stop to verify the sensing technology before I started drafting around it. In hindsight I probably should've asked the I&C engineer first, but it read as applicable on its face. Interviewer: What alternatives did you consider there? Participant: I could've tabled it as low relevance until I confirmed equivalence, or gone straight to the I&C engineer before touching the draft. I didn't do either — I just moved forward with incorporating it. Interviewer: On the verification steps — what sources did you actually rely on when drafting? Participant: Mostly my own prior work. I've done this enough times that I have a rhythm to how these sections get built. I did have the design change package open, but I wrote the structure first and meant to reconcile it against the specific requirements after — that reconciliation step is where the calibration check got missed. Interviewer: Was consulting the I&C engineer before drafting ever on the table? Participant: It was an option. I just didn't think I needed it at that stage — this felt like standard territory. Interviewer: How did you decide which historical test data to weight most heavily for the validation criteria? Participant: The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes. In hindsight, the older data had more operating conditions represented. Interviewer: When time got short at the end, how did you decide the draft was ready to submit? Participant: I looked at what was actually accessible — the control room log, my notes — and it felt like enough to call it done. The audit had the fuller OE records locked up, and requesting an extension felt like it would just push the whole outage schedule, so I didn't pursue that. On the risk side, I ran through the failure modes I could recall from the design package, felt like the major ones were addressed, and made the call that residual risk was acceptable. Interviewer: Did escalating to the Shift Technical Advisor come up as an option? Participant: It did cross my mind, but I didn't think the open question was significant enough to escalate at the time. Interviewer: If you'd had another full day for the OE report review, would you have handled that differently? Participant: Probably — I'd have gotten the I&C engineer's read on technical equivalence before drafting anything, rather than after. Interviewer: If the audit hadn't locked the database, what would you have checked? Participant: I'd have wanted to search for any other OE items involving this exact transmitter model, and cross-check the failure-mode list more completely instead of relying on memory. Interviewer: Looking back, is there a point you'd have wanted a second set of eyes earlier? Participant: Probably right after the OE report came in, before I started building language around it. Interviewer: How confident were you in that final risk judgment at the time, compared to now? Participant: At the time, reasonably confident — it felt sufficient given what I had access to. Now, knowing the board found a gap, I'd say I was more confident than the evidence actually supported. Interviewer: That's really helpful. Thanks for walking through all of that in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.68s · gen 204.43s · total 208.2s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0305 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0292 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0263 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0239 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
5. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0233 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
6. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0222 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0213 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0210 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0206 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
12. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0206 (rrf) — _# f Space Flight identified with near certainty the proximal cause o failure. In addition to elu_
13. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0202 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
14. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0188 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
15. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0182 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
16. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0180 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
17. **Hallihan_etal_DTM_12.pdf** — 0.0180 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
18. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0179 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
19. **Lyell Automation bias and verification complexity.pdf** — 0.0177 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
20. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0177 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
21. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0176 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
22. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0174 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
23. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0165 (rrf) — _# Acknowledgements First and foremost, I would like to thank my parents, Brenda and Kevin , who _
24. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0164 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
25. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0164 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0162 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
28. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0161 (rrf) — _## Uwe Dulleck, PhD fi c Assessment was ap- (ESI) \[ 19\]. Heuristics can be bene fi cial in per_
29. **Hallihan_etal_DTM_12.pdf** — 0.0158 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
30. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
31. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
32. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0155 (rrf) — _# Cognitive Bias in the Verification and Validation o This research was carried out at the Jet P_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0155 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
34. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0154 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
35. **Hallihan_etal_DTM_12.pdf** — 0.0154 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
36. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0154 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
37. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0154 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization correct conclusions, _
38. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0154 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0154 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0151 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
41. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0151 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
44. **Hallihan_etal_DTM_12.pdf** — 0.0147 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0146 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
47. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0142 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first analysis of participant reasoning during an AFW procedure revision; only transcript-affirmed bias mechanisms are classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "overconfidence bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging relevance or category membership by resemblance to a salient prototype rather than by diagnostically relevant underlying features.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial assessment of OE report relevance",
      "decision_point_description": "Deciding whether to incorporate the new digital-transmitter OE report into the draft before verifying technical equivalence.",
      "affected_reasoning_operation": "Similarity-based categorization of an operational event as applicable",
      "bias_specific_mechanism": "Salient surface framing, 'new digital level transmitter failure,' activated a same-category prototype and led to a premature applicability judgment without checking underlying sensing technology or vendor family.",
      "manifestation_in_interview": "The participant saw the OE report as directly relevant based on surface similarity, began drafting from it, and only later learned from the I&C engineer that the OE unit used a different sensing technology and vendor family.",
      "effect_on_reasoning_or_decision": "It led to incorporating OE language into the draft before technical equivalence was confirmed, requiring later correction by the I&C engineer and creating rework in the revision process.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right when I started, an industry OE report landed in my queue — a transmitter failure at another station involving a new digital level transmitter. My first reaction was, okay, this is directly relevant, new digital unit, level transmitter, similar failure. I started pulling language from it into my draft pretty quickly.",
          "evidence_explanation": "Shows immediate similarity-based relevance judgment and drafting action before verification of technical equivalence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the framing — 'new digital level transmitter failure' — matched our situation closely enough that it registered as the same kind of event. I didn't stop to verify the sensing technology before I started drafting around it.",
          "evidence_explanation": "Explicitly identifies surface framing as the basis for same-category judgment and acknowledges failure to verify the diagnostically relevant underlying feature."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I could've tabled it as low relevance until I confirmed equivalence, or gone straight to the I&C engineer before touching the draft. I didn't do either — I just moved forward with incorporating it.",
          "evidence_explanation": "Demonstrates that alternative verification pathways were available and that the biased similarity judgment directly shaped the decision to proceed."
        }
      ],
      "correction_or_counterevidence": "Later, the I&C engineer who executed the design change pointed out the OE unit used a different sensing technology and vendor family; the participant acknowledged in hindsight that he should have checked technical equivalence first.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported the representativeness heuristic; the label rests on established cognitive-science knowledge and is not represented as retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "recency effect",
      "alternative_labels": [
        "recency bias",
        "availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overweight or more clearly recall recently encountered information relative to older information, independent of its diagnostic relevance.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of historical test data for validation criteria",
      "decision_point_description": "Choosing which historical test data to use as the benchmark for validating the revised AFW procedure.",
      "affected_reasoning_operation": "Weighting and selection of historical test data for validation benchmarking",
      "bias_specific_mechanism": "A recent, top-of-mind test form from an unrelated procedure was used as a proxy and anchor because it was fresh in memory, without systematic comparison against the larger five-year historical dataset.",
      "manifestation_in_interview": "The participant anchored validation criteria around a two-week-old test from a different, unrelated procedure because it was 'fresh in my head,' rather than systematically comparing it with older AFW surveillance data.",
      "effect_on_reasoning_or_decision": "The validation criteria were built around less relevant recent data, while a later fuller data pull indicated that older historical tests more closely matched the transmitter's actual fault signature.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We've got five years of AFW surveillance history, but I also had a test from two weeks earlier on a different, unrelated procedure that happened to use a similar-looking verification form. That one was fresh in my head, so I anchored the validation criteria around it. Turned out later, when someone did a fuller data pull, that some of the older historical tests actually covered operating conditions closer to this transmitter's actual fault signature than the recent one did.",
          "evidence_explanation": "Shows temporal recency and top-of-mind salience caused the recent test to outweigh the broader historical dataset, with later evidence confirming the older tests were more relevant."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes. In hindsight, the older data had more operating conditions represented.",
          "evidence_explanation": "Explicitly attributes the selection to recent exposure and top-of-mind availability, and confirms the absence of a systematic relevance comparison."
        }
      ],
      "correction_or_counterevidence": "A later fuller data pull found that older historical tests covered operating conditions closer to the transmitter's actual fault signature; the participant acknowledged in hindsight that the older data had more relevant operating conditions represented.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Defines the recency effect as a memory bias favoring recent events.",
          "relevance_to_this_occurrence": "The participant's use of a recent, top-of-mind test from an unrelated procedure over older more relevant historical data instantiates the recency effect in validation benchmark selection."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "overconfidence bias",
      "alternative_labels": [
        "overconfidence effect",
        "calibration bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A miscalibration between subjective confidence and objective evidence, leading a person to overestimate the completeness or accuracy of a judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final readiness and risk judgment before submission",
      "decision_point_description": "Deciding that the draft was complete and residual risk acceptable without full database access or escalation.",
      "affected_reasoning_operation": "Risk assessment and sufficiency judgment under incomplete information",
      "bias_specific_mechanism": "Subjective confidence in the completeness of recalled failure modes and accessible records exceeded the available evidence, leading to a judgment that residual risk was acceptable without further information retrieval or escalation.",
      "manifestation_in_interview": "With the OE database partly locked and under time pressure, the participant relied on accessible notes and recalled failure modes, judged the major failure modes addressed, and signed off; the board later identified a gap.",
      "effect_on_reasoning_or_decision": "The participant submitted the procedure revision without a supplemental risk note or escalation; the approval board subsequently identified an unaddressed failure mode and required supplemental risk documentation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at what was actually accessible — the control room log, my notes — and it felt like enough to call it done. The audit had the fuller OE records locked up, and requesting an extension felt like it would just push the whole outage schedule, so I didn't pursue that. On the risk side, I ran through the failure modes I could recall from the design package, felt like the major ones were addressed, and made the call that residual risk was acceptable.",
          "evidence_explanation": "Shows the participant treated accessible records and memory-based failure-mode review as sufficient, and directly acted on that confidence by signing off."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At the time, reasonably confident — it felt sufficient given what I had access to. Now, knowing the board found a gap, I'd say I was more confident than the evidence actually supported.",
          "evidence_explanation": "Explicitly states that at-the-time confidence exceeded the available evidence, which is the core miscalibration of overconfidence."
        }
      ],
      "correction_or_counterevidence": "The approval board subsequently identified an unaddressed failure mode and asked for a supplemental risk note; the participant now judges his earlier confidence as exceeding the evidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported overconfidence bias; the label rests on established cognitive-science knowledge and is not represented as retrieved evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "mental set",
      "alternative_labels": [
        "Einstellung effect",
        "default bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Drafting verification steps for the new digital transmitter",
      "supporting_interview_quote": "I've written a lot of these AFW revisions over the years, so I built the verification section using the template sequence I normally use. That went to peer review, and the reviewer caught that the calibration check wasn't in there at all — I'd basically carried over the old pattern without building it fresh around the new requirement.",
      "plausible_mechanism": "A strong pre-existing response pattern for AFW verification sections led to automatic reuse of the old analog template, causing omission of the new two-point calibration check.",
      "why_not_identified": "Could not be affirmatively distinguished from ordinary skill-based omission or procedure/documentation error under time pressure; the transcript does not show sufficient bias-specific mechanism beyond reliance on a familiar template, and peer review caught the omission before final approval."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus coverage was sparse and did not include direct passages for representativeness heuristic or overconfidence bias; those labels rely on established general knowledge with disclosure.",
    "The interview is retrospective self-report; while statements were used conservatively, memory and hindsight may color some explanations.",
    "Some decision episodes, such as template reuse, were treated as candidates rather than identified biases because ordinary skill-based omission could not be ruled out."
  ]
}

