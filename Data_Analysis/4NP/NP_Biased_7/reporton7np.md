# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operations learning file, not a disciplinary review — anything you share is for process improvement. Can you state your role and how long you've been on this unit? Participant: Sure. I'm a process control operator on the catalytic reforming unit, been on this board for about six years, refinery for eleven. I run the DCS console during my shift — feed rates, heater duty, reactor temps, that kind of thing. Interviewer: Good. Let's start broad — walk me through the incident from the beginning. Participant: It started right at shift handover, early morning. I'd just sat down at the console when the high-temperature alarm came up on the feed heater outlet. Annunciator panel lit up red, audible tone too. Honestly, my first thought was 'here we go again' — that specific alarm point has been a headache for a month, and those past calls came to mind pretty fast. I want to say it's fired eleven times in the past few weeks, and every one I could remember got chalked up to instrument drift on that thermocouple. I didn't pull the actual log to check the dates or whether those prior trips looked like this one — the pattern in my head felt strong enough on its own. So I acknowledged it, silenced the tone, and kept going with handover. Interviewer: Did you check anything else at that point? Participant: Not right away, no. I was focused on the panel itself — it's the loudest thing in the room when it goes off. There was actually a pressure-differential trend creeping up on one of the other screens, but it's a quieter kind of alarm, just a slow line drifting upward, no flashing, nothing urgent-looking. I didn't pull that screen up until later in the shift. Interviewer: Okay, let's keep going chronologically. What happened during the handover conversation itself? Participant: Night operator gave me the rundown — said the unit had been 'stable, unremarkable' for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value. There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but I mostly wrote it off just because it was a few days old — didn't go back and check whether that drift had actually stopped or just wasn't showing up in the last four hours. It felt like old news at that point since the recent hours looked clean. Interviewer: And then? Participant: Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run. Interviewer: What happened after the increase? Participant: Outlet temperature climbed further than I expected. Then the field operator called in from a walkdown and mentioned some heat shimmer near the firebox — visually noticeable, he said, not normal. That's when it started feeling like more than a nuisance alarm. Interviewer: Let's go back and unpack that first decision — acknowledging the alarm as nuisance. What information did you actually have in front of you at that moment? Participant: The alarm itself, my memory of that alarm going off a lot recently, and that pressure trend I mentioned, which I hadn't really looked at yet. Interviewer: What alternatives did you consider? Participant: I could've dispatched the field guy right then to verify the thermocouple independently, or pulled up the pressure trend side by side before acknowledging. I didn't do either — the history just made it feel like a formality. Interviewer: How confident were you in that read? Participant: Pretty confident, honestly. Maybe overconfident looking back. Eleven-for-eleven is a strong pattern in your head, even if I hadn't actually gone back through the log to confirm it. Interviewer: Moving to the feed increase decision — what alternatives were on the table? Participant: I could've delayed the increase and gone back through the multi-day trend log, or looped in the process engineer before touching setpoints. Neither felt necessary given how clean the last few hours looked. Interviewer: When you ran the sequence, were you consciously deciding it was the right call, or was it more automatic? Participant: If I'm honest, automatic. It's muscle memory at this point. I wasn't sitting there weighing pros and cons — I was just executing the steps I always execute for a feed bump. Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind? Participant: The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template. At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing. Interviewer: Did the current data support either of those comparisons specifically? Participant: Looking back, not entirely. The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach. And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event. Interviewer: What alternatives existed at that point? Participant: I could've treated it as a new case entirely and pulled fresh heater-specific data before picking a diagnostic path, or requested an independent instrument check to compare against both remembered precedents. Interviewer: Let's talk about the final decision, with the regeneration window closing in. Participant: Under ninety minutes left. Temps and pressure still climbing but not at trip setpoints yet. I had the standard checklist for heater excursions, and I could've paused everything to escalate fully to the process engineer, but that's a twenty-to-thirty-minute conversation minimum, and the clock was working against us. Interviewer: How did you decide? Participant: I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast. Interviewer: What was the outcome? Participant: It did stabilize the immediate trend, which was the priority. Root cause wasn't fully addressed though — a later review flagged another corrective step on that same checklist that probably would've hit the underlying issue better. Wasn't wrong exactly, just not the most complete answer. Interviewer: If the alarm's history had been different — say, no prior nuisance trips at all — would you have handled that first moment the same way? Participant: No, honestly no. If that alarm had been clean before, I'd have jumped on the pressure trend immediately instead of treating it as background noise. Interviewer: What single piece of information, if you'd had it earlier, would have changed the most for you? Participant: Probably the pressure-differential trend, pulled up right alongside the alarm at the very start. That would've reframed the whole thing much sooner instead of it building quietly in the background. Interviewer: And if you'd had more time before the regeneration window closed? Participant: I'd have gone through more of the checklist options side by side, maybe gotten the engineer on the line even for ten minutes. It wasn't that I thought the first option was definitely best — it was available and it worked well enough given the clock. Interviewer: Anything else stand out looking back? Participant: Just that a lot of small, reasonable-feeling calls stacked up into something bigger than any one of them looked like at the time. Nothing felt like a wrong decision in the moment. Interviewer: That's a good place to close. Thanks for walking through this in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.75s · gen 383.17s · total 388.4s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0307 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0261 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0247 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0241 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0221 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0220 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0214 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0209 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0201 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0200 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0199 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
14. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0180 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
16. **Lyell Automation bias and verification complexity.pdf** — 0.0179 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0174 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
19. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0170 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
21. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0169 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
23. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0165 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
24. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0161 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0160 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0159 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
30. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0154 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
31. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0154 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
32. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0152 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
33. **Lyell Automation bias and verification complexity.pdf** — 0.0150 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
36. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0147 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
37. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0145 (rrf) — _# Cognitive Biases Within Decision Making 475 Perception Attentiveness Comprehension Credibility_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0144 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0141 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Summary The studie_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
42. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0140 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0138 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 382 operators purp_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0137 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0136 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - an earlier obser_
47. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0136 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0135 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
50. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0134 (rrf) — _# 476 Fire Technology 2019 | Perception Attentiveness Comprehension Credibility Personalization _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single-interview diagnostic review based on transcript evidence. Retrieved corpus passages were used to support mechanism definitions where available; unsupported classifications are noted."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "confirmation bias",
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
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "ease of recall"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood or significance of a current event based on how easily similar instances come to mind rather than on objective evidence or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial high-temperature alarm classification at shift handover",
      "decision_point_description": "Whether to classify the feed heater outlet high-temperature alarm as a familiar nuisance instrument-drift alarm versus a new deviation requiring immediate investigation.",
      "affected_reasoning_operation": "Diagnostic/likelihood assessment under uncertainty; attention allocation",
      "bias_specific_mechanism": "The operator judged the alarm as another nuisance trip based on the ease and vividness with which prior similar alarm episodes came to mind, without consulting the actual log or current pressure-differential trend.",
      "manifestation_in_interview": "On alarm onset, the participant immediately recalled repeated past nuisance trips, said the pattern in his head felt strong enough, and acknowledged and silenced the alarm without checking other indications.",
      "effect_on_reasoning_or_decision": "The alarm was treated as a formality and the developing pressure-differential/feed issue was not examined early, delaying more accurate diagnosis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was 'here we go again' — that specific alarm point has been a headache for a month, and those past calls came to mind pretty fast.",
          "evidence_explanation": "Shows that memory retrieval of recent similar alarms drove the initial classification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I want to say it's fired eleven times in the past few weeks, and every one I could remember got chalked up to instrument drift on that thermocouple. I didn't pull the actual log to check the dates or whether those prior trips looked like this one — the pattern in my head felt strong enough on its own.",
          "evidence_explanation": "Demonstrates reliance on the strength and ease of recall rather than objective verification of the log or current features."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I could've dispatched the field guy right then to verify the thermocouple independently, or pulled up the pressure trend side by side before acknowledging. I didn't do either — the history just made it feel like a formality.",
          "evidence_explanation": "Shows that the recalled history crowded out more direct diagnostic actions."
        }
      ],
      "correction_or_counterevidence": "Later in the interview the participant acknowledged overconfidence and said that if the alarm had no prior nuisance history he would have checked the pressure trend immediately.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus does not define or operationalize the availability heuristic. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory bias", "myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's existing beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Handover integration and assessment of unit stability",
      "decision_point_description": "Whether to accept the night operator's stable/unremarkable report and recent clean trend as sufficient, or investigate the older unresolved heater-duty drift note.",
      "affected_reasoning_operation": "Evidence weighting and belief updating",
      "bias_specific_mechanism": "The participant selectively accepted and weighted information consistent with the view that the unit was stable while discounting an older unresolved drift note as old news without checking whether the drift had actually resolved.",
      "manifestation_in_interview": "The participant accepted the night operator's stable report at face value because it matched the immediate trend, while dismissing a prior unresolved drift note solely because it was a few days old.",
      "effect_on_reasoning_or_decision": "Reinforced the normalcy assumption and left the unresolved drift unexplored before proceeding with the feed increase.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Night operator gave me the rundown — said the unit had been 'stable, unremarkable' for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value.",
          "evidence_explanation": "Shows accepting information because it fit the participant's current normality view."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but I mostly wrote it off just because it was a few days old — didn't go back and check whether that drift had actually stopped or just wasn't showing up in the last four hours. It felt like old news at that point since the recent hours looked clean.",
          "evidence_explanation": "Shows selective discounting of contradictory evidence without investigation."
        }
      ],
      "correction_or_counterevidence": "No immediate correction before the feed increase; the participant later reflected that a lot of small, reasonable-feeling calls stacked up, but the transcript does not show the drift note being checked at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Parasuraman and Manzey passage explicitly references confirmation bias as discounting contradictory information in favor of a dominant interpretation.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Clearly, the automatically generated warning must have led the pilots to either ignore (or discount) the contradicting information available from other displays and engine indicators or to believe that it would be in line with the warning, as in a confirmation bias effect.",
          "mechanism_supported_by_source": "Confirmation bias as discounting contradictory information in favor of a dominant interpretation.",
          "relevance_to_this_occurrence": "Supports the classification of selective discounting of the older drift note while accepting the stable report."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": ["representativeness bias", "similarity heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the probability of an event or diagnosis by how similar it is to a prototype or remembered example, often while ignoring base rates or distinguishing diagnostic features.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Diagnostic hypothesis selection after the field operator's heat-shimmer report",
      "decision_point_description": "Whether to apply the remembered compressor surge response template or evaluate the current case on its own current diagnostic features.",
      "affected_reasoning_operation": "Diagnostic hypothesis generation and selection",
      "bias_specific_mechanism": "The current symptoms resembled a prior compressor surge event, so the participant treated the representativeness match as sufficient to pull the same response template and did not initially check for a defining feature mismatch, namely the absence of the compressor vibration signature.",
      "manifestation_in_interview": "The participant stated that the presentation reminded him of a compressor surge event and that he did not stop to check for the distinct vibration signature before leaning toward the surge-response approach.",
      "effect_on_reasoning_or_decision": "Directed diagnostic action toward a possibly inappropriate remembered template and delayed a fresh, data-driven assessment of the current case.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template.",
          "evidence_explanation": "Shows similarity to a remembered event driving response-template selection."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach.",
          "evidence_explanation": "Shows ignoring a diagnostic feature mismatch in favor of the representative remembered pattern."
        }
      ],
      "correction_or_counterevidence": "Later engineering review pointed out that the current data did not support the surge comparison, and the participant acknowledged the missing marker.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus does not operationalize the representativeness heuristic. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "salience bias", "vividness effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood or significance of an event based on how easily instances come to mind, especially when the event is vivid, recent, or frequently rehearsed.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Diagnostic hypothesis likelihood after the field operator's heat-shimmer report",
      "decision_point_description": "Whether to treat tube rupture as more likely based on how memorable and socially available the prior event was versus current diagnostic markers.",
      "affected_reasoning_operation": "Likelihood estimation and diagnostic hypothesis weighing",
      "bias_specific_mechanism": "The participant judged the tube-rupture explanation as more likely because the event was repeatedly discussed and therefore easily retrieved, even though the current data lacked its specific markers.",
      "manifestation_in_interview": "The participant stated that the tube-rupture incident felt like the more likely explanation just because it is the one people bring up in every shift briefing, and later acknowledged that the specific failure markers were not present.",
      "effect_on_reasoning_or_decision": "Distorted the likelihood estimate, contributing to diagnostic narrowing based on a salient past incident rather than current evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing.",
          "evidence_explanation": "Shows likelihood being inferred from social rehearsal and memorability rather than from current diagnostic data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event.",
          "evidence_explanation": "Confirms the operative mechanism was memorability/salience rather than diagnostic fit."
        }
      ],
      "correction_or_counterevidence": "Later engineering review noted the absence of tube-rupture markers, and the participant acknowledged that the current data did not support the comparison.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus does not define or operationalize the availability heuristic. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": ["plan continuation", "get-there-itis"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Proceeding with the feed rate increase despite the earlier alarm and unresolved drift note",
      "supporting_interview_quote": "Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run.",
      "plausible_mechanism": "A tendency to continue an existing plan or sequence despite cues suggesting that reconsideration is needed.",
      "why_not_identified": "The behavior is strongly tied to routine procedural execution and schedule pressure; the transcript does not establish a distinct plan-continuation distortion beyond habitual or normal operational practice."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "satisficing",
      "alternative_labels": ["urgency-induced narrowing", "time-pressure satisficing"],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final checklist selection under regeneration-window time pressure",
      "supporting_interview_quote": "I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast.",
      "plausible_mechanism": "Time pressure produced a satisficing threshold in which the first workable option was selected rather than comparing alternatives.",
      "why_not_identified": "The transcript attributes the choice explicitly to time pressure and workability, and the exclusion criteria treat time compression without a distinct cognitive distortion as ordinary bounded rationality."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "overconfidence effect",
      "alternative_labels": ["overprecision"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial alarm classification",
      "supporting_interview_quote": "Pretty confident, honestly. Maybe overconfident looking back. Eleven-for-eleven is a strong pattern in your head, even if I hadn't actually gone back through the log to confirm it.",
      "plausible_mechanism": "Subjective confidence in the nuisance-alarm explanation exceeded the objective basis because the remembered pattern had not been verified against the log.",
      "why_not_identified": "Overconfidence is intertwined with the availability heuristic in this episode; transcript evidence is stronger for availability as the specific mechanism than for a separate miscalibration process."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Limited to a single interview transcript without independent verification of system logs or operational outcomes.",
    "Retrospective self-report may include memory reconstruction or hindsight.",
    "The retrieved corpus was sparse and did not cover all candidate mechanisms; some classifications rely on general cognitive-science knowledge.",
    "Some identified occurrences are lower confidence where non-bias explanations remain plausible."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operations learning file, not a disciplinary review — anything you share is for process improvement. Can you state your role and how long you've been on this unit? Participant: Sure. I'm a process control operator on the catalytic reforming unit, been on this board for about six years, refinery for eleven. I run the DCS console during my shift — feed rates, heater duty, reactor temps, that kind of thing. Interviewer: Good. Let's start broad — walk me through the incident from the beginning. Participant: It started right at shift handover, early morning. I'd just sat down at the console when the high-temperature alarm came up on the feed heater outlet. Annunciator panel lit up red, audible tone too. Honestly, my first thought was 'here we go again' — that specific alarm point has been a headache for a month, and those past calls came to mind pretty fast. I want to say it's fired eleven times in the past few weeks, and every one I could remember got chalked up to instrument drift on that thermocouple. I didn't pull the actual log to check the dates or whether those prior trips looked like this one — the pattern in my head felt strong enough on its own. So I acknowledged it, silenced the tone, and kept going with handover. Interviewer: Did you check anything else at that point? Participant: Not right away, no. I was focused on the panel itself — it's the loudest thing in the room when it goes off. There was actually a pressure-differential trend creeping up on one of the other screens, but it's a quieter kind of alarm, just a slow line drifting upward, no flashing, nothing urgent-looking. I didn't pull that screen up until later in the shift. Interviewer: Okay, let's keep going chronologically. What happened during the handover conversation itself? Participant: Night operator gave me the rundown — said the unit had been 'stable, unremarkable' for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value. There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but I mostly wrote it off just because it was a few days old — didn't go back and check whether that drift had actually stopped or just wasn't showing up in the last four hours. It felt like old news at that point since the recent hours looked clean. Interviewer: And then? Participant: Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run. Interviewer: What happened after the increase? Participant: Outlet temperature climbed further than I expected. Then the field operator called in from a walkdown and mentioned some heat shimmer near the firebox — visually noticeable, he said, not normal. That's when it started feeling like more than a nuisance alarm. Interviewer: Let's go back and unpack that first decision — acknowledging the alarm as nuisance. What information did you actually have in front of you at that moment? Participant: The alarm itself, my memory of that alarm going off a lot recently, and that pressure trend I mentioned, which I hadn't really looked at yet. Interviewer: What alternatives did you consider? Participant: I could've dispatched the field guy right then to verify the thermocouple independently, or pulled up the pressure trend side by side before acknowledging. I didn't do either — the history just made it feel like a formality. Interviewer: How confident were you in that read? Participant: Pretty confident, honestly. Maybe overconfident looking back. Eleven-for-eleven is a strong pattern in your head, even if I hadn't actually gone back through the log to confirm it. Interviewer: Moving to the feed increase decision — what alternatives were on the table? Participant: I could've delayed the increase and gone back through the multi-day trend log, or looped in the process engineer before touching setpoints. Neither felt necessary given how clean the last few hours looked. Interviewer: When you ran the sequence, were you consciously deciding it was the right call, or was it more automatic? Participant: If I'm honest, automatic. It's muscle memory at this point. I wasn't sitting there weighing pros and cons — I was just executing the steps I always execute for a feed bump. Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind? Participant: The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template. At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing. Interviewer: Did the current data support either of those comparisons specifically? Participant: Looking back, not entirely. The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach. And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event. Interviewer: What alternatives existed at that point? Participant: I could've treated it as a new case entirely and pulled fresh heater-specific data before picking a diagnostic path, or requested an independent instrument check to compare against both remembered precedents. Interviewer: Let's talk about the final decision, with the regeneration window closing in. Participant: Under ninety minutes left. Temps and pressure still climbing but not at trip setpoints yet. I had the standard checklist for heater excursions, and I could've paused everything to escalate fully to the process engineer, but that's a twenty-to-thirty-minute conversation minimum, and the clock was working against us. Interviewer: How did you decide? Participant: I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast. Interviewer: What was the outcome? Participant: It did stabilize the immediate trend, which was the priority. Root cause wasn't fully addressed though — a later review flagged another corrective step on that same checklist that probably would've hit the underlying issue better. Wasn't wrong exactly, just not the most complete answer. Interviewer: If the alarm's history had been different — say, no prior nuisance trips at all — would you have handled that first moment the same way? Participant: No, honestly no. If that alarm had been clean before, I'd have jumped on the pressure trend immediately instead of treating it as background noise. Interviewer: What single piece of information, if you'd had it earlier, would have changed the most for you? Participant: Probably the pressure-differential trend, pulled up right alongside the alarm at the very start. That would've reframed the whole thing much sooner instead of it building quietly in the background. Interviewer: And if you'd had more time before the regeneration window closed? Participant: I'd have gone through more of the checklist options side by side, maybe gotten the engineer on the line even for ten minutes. It wasn't that I thought the first option was definitely best — it was available and it worked well enough given the clock. Interviewer: Anything else stand out looking back? Participant: Just that a lot of small, reasonable-feeling calls stacked up into something bigger than any one of them looked like at the time. Nothing felt like a wrong decision in the moment. Interviewer: That's a good place to close. Thanks for walking through this in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.10s · gen 359.58s · total 364.9s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0307 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0261 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0247 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0241 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0221 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0220 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0214 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0209 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0201 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0200 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0199 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
14. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0180 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
16. **Lyell Automation bias and verification complexity.pdf** — 0.0179 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0174 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
19. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0170 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
21. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0169 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
23. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0165 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
24. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0161 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0160 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0159 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
30. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0154 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
31. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0154 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
32. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0152 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
33. **Lyell Automation bias and verification complexity.pdf** — 0.0150 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
36. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0147 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
37. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0145 (rrf) — _# Cognitive Biases Within Decision Making 475 Perception Attentiveness Comprehension Credibility_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0144 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0141 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Summary The studie_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
42. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0140 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0138 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 382 operators purp_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0137 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0136 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - an earlier obser_
47. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0136 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0135 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
50. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0134 (rrf) — _# 476 Fire Technology 2019 | Perception Attentiveness Comprehension Credibility Personalization _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Mechanism-first analysis of a single incident debrief, focusing on reasoning episodes from alarm acknowledgment through diagnostic and checklist decisions."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "Premature cognitive commitment",
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
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or frequency of an event based on how easily relevant instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Alarm acknowledgment at shift handover",
      "decision_point_description": "Whether to treat the high-temperature alarm as a nuisance and continue without verification.",
      "affected_reasoning_operation": "Probability judgment about alarm validity and decision to acknowledge/silence the alarm",
      "bias_specific_mechanism": "Easily recalled past nuisance alarms on the same point made the 'nuisance alarm' interpretation highly available, leading the participant to judge the current alarm as another nuisance and truncate verification.",
      "manifestation_in_interview": "The participant cited the alarm history coming to mind quickly and a strong in-head pattern of eleven prior nuisance trips, while acknowledging he did not check the log or the pressure trend.",
      "effect_on_reasoning_or_decision": "He acknowledged and silenced the alarm and continued with handover rather than checking the pressure-differential trend or dispatching a field check.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was 'here we go again' — that specific alarm point has been a headache for a month, and those past calls came to mind pretty fast.",
          "evidence_explanation": "The participant explicitly traces the nuisance interpretation to how quickly past alarm instances came to mind, which is the retrieval-ease mechanism of the availability heuristic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I want to say it's fired eleven times in the past few weeks, and every one I could remember got chalked up to instrument drift on that thermocouple. I didn't pull the actual log to check the dates or whether those prior trips looked like this one — the pattern in my head felt strong enough on its own.",
          "evidence_explanation": "The reliance on a remembered pattern rather than actual log verification shows recall-based likelihood judgment, not an analytic use of verified history."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Eleven-for-eleven is a strong pattern in your head, even if I hadn't actually gone back through the log to confirm it.",
          "evidence_explanation": "This reinforces that the subjective strength of the remembered pattern drove confidence despite the absence of objective verification."
        }
      ],
      "correction_or_counterevidence": "No immediate correction before silencing the alarm. Later the participant acknowledged possible overconfidence and said a clean alarm history would have led him to check the pressure trend immediately.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derived from general cognitive-science knowledge; the retrieved passages did not provide direct support for the availability heuristic.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "anchoring heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to make estimates based on an initial value or assessment and to adjust insufficiently in light of additional information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Assessment of unit status during handover",
      "decision_point_description": "Whether to incorporate the older board-log drift note into the current unit assessment.",
      "affected_reasoning_operation": "Integration of night-operator handover information with prior board-log information",
      "bias_specific_mechanism": "The night operator's 'stable, unremarkable' report and the matching clean immediate trend served as an anchor; the older unresolved drift note was then discounted without sufficient adjustment or verification of whether the drift had stopped.",
      "manifestation_in_interview": "The participant took the stable report at face value because it matched what he was seeing, then wrote off an older unresolved drift note mainly because it was a few days old.",
      "effect_on_reasoning_or_decision": "He did not check whether the unresolved heater-duty drift had actually stopped, leaving a potentially important trend unaddressed before the feed increase.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Night operator gave me the rundown — said the unit had been 'stable, unremarkable' for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value.",
          "evidence_explanation": "This quote establishes the initial 'stable' assessment that anchored the participant's current picture of the unit."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but I mostly wrote it off just because it was a few days old — didn't go back and check whether that drift had actually stopped or just wasn't showing up in the last four hours. It felt like old news at that point since the recent hours looked clean.",
          "evidence_explanation": "The participant adjusted insufficiently from the initial stable assessment by dismissing the older unresolved drift note, even though he had not verified whether the condition had resolved."
        }
      ],
      "correction_or_counterevidence": "The recent hours did look clean, so prioritizing recent information was not wholly unreasonable; however, the unresolved note was not verified before being discounted.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Mechanism is directly supported by the retrieved passage on anchoring and adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The document describes the anchoring and adjustment heuristic as making estimates based on an initial answer and adjusting from there based on additional information, with adjustments typically being insufficient.",
          "mechanism_supported_by_source": "Anchoring on an initial value or assessment and insufficient adjustment from subsequent information.",
          "relevance_to_this_occurrence": "The stable night-operator report and clean immediate trend acted as an initial assessment, and the older drift note was not sufficiently used to update that assessment."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Premature cognitive commitment",
      "alternative_labels": [
        "mindless behavior",
        "automated behavior"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A premature cognitive commitment is an attitude that develops when a person first encounters a device or context and is reinforced through repeated exposure, leading to automated or mindless behavior.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Feed rate increase before regeneration window",
      "decision_point_description": "Whether to execute the standard feed-increase sequence or reconsider it in light of the earlier alarm and drift note.",
      "affected_reasoning_operation": "Decision to run the standard feed-increase sequence despite new warning signals",
      "bias_specific_mechanism": "Repeated execution of the feed-increase sequence produced automated/mindless behavior, so the participant selected and executed the routine without active reconsideration of the alarm and drift note.",
      "manifestation_in_interview": "The participant described the sequence as automatic and based on muscle memory, explicitly saying he was not weighing pros and cons.",
      "effect_on_reasoning_or_decision": "He ran the feed-increase sequence without reconsidering it, after which outlet temperature climbed further than expected.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run.",
          "evidence_explanation": "This shows the routine was selected because it was the familiar standard sequence, not because it was deliberately re-evaluated for the current conditions."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, automatic. It's muscle memory at this point. I wasn't sitting there weighing pros and cons — I was just executing the steps I always execute for a feed bump.",
          "evidence_explanation": "The participant explicitly describes automatic, mindless execution, consistent with repeated-exposure automated behavior."
        }
      ],
      "correction_or_counterevidence": "The sequence was a standard procedure and familiarity-based execution may be normal in routine operations; however, the participant himself noted he did not reconsider it despite the earlier warning signs.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Mechanism is directly supported by the retrieved passage on premature cognitive commitment and mindless behavior.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Langer's concept of 'premature cognitive commitment,' defined as an attitude that develops when a person first encounters a device in a particular context and that is then reinforced when the device is reencountered in the same way. Repeated exposure to the same experience leads people to engage in 'automated' or 'mindless' behavior.",
          "mechanism_supported_by_source": "Repeated exposure can produce automated or mindless behavior, reducing deliberate re-evaluation of routine actions.",
          "relevance_to_this_occurrence": "The participant's repeated execution of the feed-increase sequence made that choice automatic, so new warning signals did not prompt reconsideration."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or frequency of an event based on how easily relevant or vivid instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Diagnostic response after heat shimmer report",
      "decision_point_description": "Which prior incident template to use for diagnosis after the field operator reported heat shimmer.",
      "affected_reasoning_operation": "Diagnostic reasoning and selection of a response template",
      "bias_specific_mechanism": "Vivid, memorable, and widely discussed prior incidents came readily to mind and dominated the likelihood judgment and diagnostic template selection, crowding out current case-specific data.",
      "manifestation_in_interview": "The participant leaned toward the surge-response approach from a remembered event and judged the dramatic tube-rupture incident as more likely because it was the one people repeatedly discussed.",
      "effect_on_reasoning_or_decision": "He leaned toward the remembered surge-response approach without checking for the distinct vibration signature, and judged the tube-rupture explanation as likely even though its specific markers were not present.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template.",
          "evidence_explanation": "The participant's diagnostic template selection was driven by a readily retrieved prior event rather than by checking current case-specific markers."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing.",
          "evidence_explanation": "This is a clear statement that the judged likelihood of the tube-rupture explanation was driven by the event's memorability and repeated discussion, not by current data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach. And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event.",
          "evidence_explanation": "The participant retrospectively recognizes that memorable prior events dominated despite the absence of distinguishing features, supporting an availability mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged the mismatch with the surge event's vibration signature and reported that the engineer said the tube-rupture markers were absent; however, this recognition came after the diagnostic leaning had already occurred.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derived from general cognitive-science knowledge; the retrieved passages did not provide direct support for the availability heuristic.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Checklist selection under regeneration-window time pressure",
      "supporting_interview_quote": "I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast.",
      "plausible_mechanism": "The first workable checklist option may have served as an anchor, truncating search for and adjustment to later checklist options.",
      "why_not_identified": "The participant explicitly attributed the limited comparison to time pressure and did not claim the first option was best; satisficing under operational time constraints is a strong competing explanation."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective self-report, without independent DCS log, alarm records, or behavioral verification.",
    "The retrieved corpus did not contain direct support for the availability heuristic, so those two occurrences rely on general cognitive-science taxonomy.",
    "Operational time pressure and standard work procedures provide plausible non-bias explanations for some reasoning episodes, particularly the final checklist selection."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operations learning file, not a disciplinary review — anything you share is for process improvement. Can you state your role and how long you've been on this unit? Participant: Sure. I'm a process control operator on the catalytic reforming unit, been on this board for about six years, refinery for eleven. I run the DCS console during my shift — feed rates, heater duty, reactor temps, that kind of thing. Interviewer: Good. Let's start broad — walk me through the incident from the beginning. Participant: It started right at shift handover, early morning. I'd just sat down at the console when the high-temperature alarm came up on the feed heater outlet. Annunciator panel lit up red, audible tone too. Honestly, my first thought was 'here we go again' — that specific alarm point has been a headache for a month, and those past calls came to mind pretty fast. I want to say it's fired eleven times in the past few weeks, and every one I could remember got chalked up to instrument drift on that thermocouple. I didn't pull the actual log to check the dates or whether those prior trips looked like this one — the pattern in my head felt strong enough on its own. So I acknowledged it, silenced the tone, and kept going with handover. Interviewer: Did you check anything else at that point? Participant: Not right away, no. I was focused on the panel itself — it's the loudest thing in the room when it goes off. There was actually a pressure-differential trend creeping up on one of the other screens, but it's a quieter kind of alarm, just a slow line drifting upward, no flashing, nothing urgent-looking. I didn't pull that screen up until later in the shift. Interviewer: Okay, let's keep going chronologically. What happened during the handover conversation itself? Participant: Night operator gave me the rundown — said the unit had been 'stable, unremarkable' for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value. There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but I mostly wrote it off just because it was a few days old — didn't go back and check whether that drift had actually stopped or just wasn't showing up in the last four hours. It felt like old news at that point since the recent hours looked clean. Interviewer: And then? Participant: Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run. Interviewer: What happened after the increase? Participant: Outlet temperature climbed further than I expected. Then the field operator called in from a walkdown and mentioned some heat shimmer near the firebox — visually noticeable, he said, not normal. That's when it started feeling like more than a nuisance alarm. Interviewer: Let's go back and unpack that first decision — acknowledging the alarm as nuisance. What information did you actually have in front of you at that moment? Participant: The alarm itself, my memory of that alarm going off a lot recently, and that pressure trend I mentioned, which I hadn't really looked at yet. Interviewer: What alternatives did you consider? Participant: I could've dispatched the field guy right then to verify the thermocouple independently, or pulled up the pressure trend side by side before acknowledging. I didn't do either — the history just made it feel like a formality. Interviewer: How confident were you in that read? Participant: Pretty confident, honestly. Maybe overconfident looking back. Eleven-for-eleven is a strong pattern in your head, even if I hadn't actually gone back through the log to confirm it. Interviewer: Moving to the feed increase decision — what alternatives were on the table? Participant: I could've delayed the increase and gone back through the multi-day trend log, or looped in the process engineer before touching setpoints. Neither felt necessary given how clean the last few hours looked. Interviewer: When you ran the sequence, were you consciously deciding it was the right call, or was it more automatic? Participant: If I'm honest, automatic. It's muscle memory at this point. I wasn't sitting there weighing pros and cons — I was just executing the steps I always execute for a feed bump. Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind? Participant: The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template. At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing. Interviewer: Did the current data support either of those comparisons specifically? Participant: Looking back, not entirely. The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach. And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event. Interviewer: What alternatives existed at that point? Participant: I could've treated it as a new case entirely and pulled fresh heater-specific data before picking a diagnostic path, or requested an independent instrument check to compare against both remembered precedents. Interviewer: Let's talk about the final decision, with the regeneration window closing in. Participant: Under ninety minutes left. Temps and pressure still climbing but not at trip setpoints yet. I had the standard checklist for heater excursions, and I could've paused everything to escalate fully to the process engineer, but that's a twenty-to-thirty-minute conversation minimum, and the clock was working against us. Interviewer: How did you decide? Participant: I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast. Interviewer: What was the outcome? Participant: It did stabilize the immediate trend, which was the priority. Root cause wasn't fully addressed though — a later review flagged another corrective step on that same checklist that probably would've hit the underlying issue better. Wasn't wrong exactly, just not the most complete answer. Interviewer: If the alarm's history had been different — say, no prior nuisance trips at all — would you have handled that first moment the same way? Participant: No, honestly no. If that alarm had been clean before, I'd have jumped on the pressure trend immediately instead of treating it as background noise. Interviewer: What single piece of information, if you'd had it earlier, would have changed the most for you? Participant: Probably the pressure-differential trend, pulled up right alongside the alarm at the very start. That would've reframed the whole thing much sooner instead of it building quietly in the background. Interviewer: And if you'd had more time before the regeneration window closed? Participant: I'd have gone through more of the checklist options side by side, maybe gotten the engineer on the line even for ten minutes. It wasn't that I thought the first option was definitely best — it was available and it worked well enough given the clock. Interviewer: Anything else stand out looking back? Participant: Just that a lot of small, reasonable-feeling calls stacked up into something bigger than any one of them looked like at the time. Nothing felt like a wrong decision in the moment. Interviewer: That's a good place to close. Thanks for walking through this in detail.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 3.07s · gen 327.92s · total 333.3s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0307 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0261 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0247 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0241 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0221 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
6. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0220 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
7. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0214 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0209 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
9. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0203 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
10. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0201 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0200 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0199 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0183 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
14. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0180 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
16. **Lyell Automation bias and verification complexity.pdf** — 0.0179 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0174 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
18. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0174 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
19. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0170 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0170 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration models.” R. Parasu_
21. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0169 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
22. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0165 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Factors Influencin_
23. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0165 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
24. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0161 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
25. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0160 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
26. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
27. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0159 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
29. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0157 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
30. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0154 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
31. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0154 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
32. **Muratat Influence of Cognitive Biases in Distorting Decision Making and.pdf** — 0.0152 (rrf) — _# Bias in Decision Making (DM) Safety 2015 , 1 our judgments by transferring our feelings or bel_
33. **Lyell Automation bias and verification complexity.pdf** — 0.0150 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
34. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
36. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0147 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
37. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0145 (rrf) — _# Cognitive Biases Within Decision Making 475 Perception Attentiveness Comprehension Credibility_
38. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0144 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 2. Literature Review From a flight crew perspective, the phenomen something either in the flig_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0141 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration Summary The studie_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
42. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0140 (rrf) — _M. Kinateder Received: 25 August 2017/ Abstract. During a fire evacuation, once an individual pe_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0138 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 382 operators purp_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0137 (rrf) — _# f Space Flight undesirable ones. These are precisely the condition induce a confirmation bias._
46. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0136 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - an earlier obser_
47. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0136 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
48. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0135 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
50. **Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf** — 0.0134 (rrf) — _# 476 Fire Technology 2019 | Perception Attentiveness Comprehension Credibility Personalization _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first screening of a voluntary operations debrief transcript; only bias-specific reasoning with affirmative transcript evidence was classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 2
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
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or significance of an event by the ease with which relevant instances come to mind rather than by systematically verifying the current evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial high-temperature alarm classification",
      "decision_point_description": "Whether to acknowledge the feed-heater outlet high-temperature alarm as a nuisance instrument-drift event or to investigate it immediately.",
      "affected_reasoning_operation": "Alarm interpretation and response prioritization",
      "bias_specific_mechanism": "Readily recalled recent nuisance alarm instances were used as the primary basis for classifying the current alarm; the remembered pattern felt sufficiently diagnostic, so the participant did not consult the actual alarm log or the co-located pressure-differential trend.",
      "manifestation_in_interview": "The participant reported that past alarm events came to mind quickly, estimated 'eleven' prior trips from memory, and acknowledged/silenced the alarm without checking the log or the visible pressure-differential trend.",
      "effect_on_reasoning_or_decision": "The initial alarm was treated as background nuisance, delaying investigation of a developing pressure/thermal issue until later field evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was 'here we go again' — that specific alarm point has been a headache for a month, and those past calls came to mind pretty fast.",
          "evidence_explanation": "Shows that readily recalled past alarm instances immediately framed the current alarm."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I want to say it's fired eleven times in the past few weeks, and every one I could remember got chalked up to instrument drift on that thermocouple. I didn't pull the actual log to check the dates or whether those prior trips looked like this one — the pattern in my head felt strong enough on its own.",
          "evidence_explanation": "Demonstrates that the participant relied on remembered instances instead of available log and trend data to conclude the alarm was another nuisance trip."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If that alarm had been clean before, I'd have jumped on the pressure trend immediately instead of treating it as background noise.",
          "evidence_explanation": "Counterfactual statement directly links the prior recall-based alarm history to the reduced urgency at the initial alarm."
        }
      ],
      "correction_or_counterevidence": "Later field report of heat shimmer, continued temperature climb, and the participant's subsequent statement that it began to feel like more than a nuisance alarm served as a delayed correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not provide a specific availability-heuristic definition; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which an initial value or impression serves as an anchor and subsequent adjustments away from that anchor are typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Handover assessment of unit stability",
      "decision_point_description": "Whether to accept the night operator's 'stable, unremarkable' handover as sufficient or to review the older unresolved heater-duty drift note.",
      "affected_reasoning_operation": "Situation assessment and integration of recent and historical trend information",
      "bias_specific_mechanism": "The immediate handover and recent four-hour trend served as an anchor; the older log note about unresolved upward heater-duty drift should have prompted adjustment, but the participant treated it as old news without checking whether it had actually resolved.",
      "manifestation_in_interview": "The participant accepted the night operator's stable report and current immediate trend at face value and dismissed an older unresolved drift note because of its age, rather than reconciling it with the recent clean hours.",
      "effect_on_reasoning_or_decision": "He formed an unduly stable picture of the unit, which contributed to proceeding with the feed increase without reviewing multi-day trends.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Night operator gave me the rundown — said the unit had been 'stable, unremarkable' for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value.",
          "evidence_explanation": "Shows acceptance of the handover and immediate-trend signal as the initial anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but I mostly wrote it off just because it was a few days old — didn't go back and check whether that drift had actually stopped or just wasn't showing up in the last four hours.",
          "evidence_explanation": "Demonstrates insufficient adjustment away from the initial stable anchor when encountering an older unresolved-drift note."
        }
      ],
      "correction_or_counterevidence": "No immediate correction; later review and engineer input led to fuller reevaluation of the heater-duty drift.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passage provided direct definitional support for the anchoring-and-adjustment mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "Defines anchoring-and-adjustment and notes that adjustment from an initial anchor is typically insufficient.",
          "relevance_to_this_occurrence": "The participant anchored on the stable handover report and recent clean trend, then made an insufficient adjustment when exposed to the older unresolved heater-duty drift note."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "similarity heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood of a diagnosis or the appropriateness of a response by the similarity of the current situation to a past or prototypical case, often without sufficiently weighting diagnostic feature mismatches.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-shimmer diagnostic response selection",
      "decision_point_description": "Whether to adopt the prior compressor-surge response template or to evaluate the current heater symptoms independently.",
      "affected_reasoning_operation": "Causal diagnosis and response-template selection",
      "bias_specific_mechanism": "The combination of current cues was matched to a remembered compressor-surge event; this similarity triggered retrieval of a prior response template, and the participant did not check for a defining feature—compressor vibration—that was absent in the current situation.",
      "manifestation_in_interview": "The participant explicitly said the situation reminded him of a compressor surge event, pulled the same response template, and later acknowledged he did not check for the defining vibration signature.",
      "effect_on_reasoning_or_decision": "It pulled diagnostic and response planning toward a previous incident template rather than a fresh analysis of the current heater-specific data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template.",
          "evidence_explanation": "Shows similarity-based retrieval and action selection from a past case."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach.",
          "evidence_explanation": "Demonstrates the representativeness failure to incorporate a diagnostic feature mismatch before adopting the prior template."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged the missing vibration signature and that the current data did not specifically support the surge template.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not provide a specific representativeness-heuristic definition; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "salience bias",
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging an event as more likely or present because it is easily recalled or especially vivid and memorable, rather than because current diagnostic evidence supports it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-shimmer causal-likelihood comparison",
      "decision_point_description": "Whether the tube-rupture failure mode was the likely explanation for the current heater symptoms.",
      "affected_reasoning_operation": "Diagnostic likelihood judgment",
      "bias_specific_mechanism": "The dramatic, frequently discussed tube-rupture incident was highly available in memory; its memorability and rehearsal in shift briefings were used as a cue to likelihood, while current diagnostic markers for that failure mode were not initially checked.",
      "manifestation_in_interview": "The participant judged the tube-rupture case as more likely because it is discussed often, and later acknowledged that none of the specific markers for that failure mode were actually present.",
      "effect_on_reasoning_or_decision": "The tube-rupture hypothesis felt more probable than current evidence warranted, influencing the diagnostic path.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing.",
          "evidence_explanation": "Shows the participant using ease of recall and social rehearsal of a salient event as a likelihood cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event.",
          "evidence_explanation": "Explicitly states that memorability substituted for actual diagnostic evidence."
        }
      ],
      "correction_or_counterevidence": "An engineer later pointed out that specific tube-rupture markers were absent; the participant acknowledged this in retrospect.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not provide a specific availability-heuristic definition; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Feed-rate increase execution",
      "supporting_interview_quote": "Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run.",
      "plausible_mechanism": "Continuing the original schedule-driven plan despite accumulating cues that a deeper review may be warranted.",
      "why_not_identified": "Strong competing non-bias explanation: execution of a well-trained standard procedure under a production and regeneration-window schedule, without clear evidence of an isolated plan-continuation reasoning mechanism."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "satisficing",
      "alternative_labels": [
        "need for closure"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final checklist selection under regeneration-window time pressure",
      "supporting_interview_quote": "I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast.",
      "plausible_mechanism": "Selecting the first acceptable option rather than comparing alternatives under time pressure.",
      "why_not_identified": "External time pressure and operational constraints provide a sufficient non-bias explanation; no distinct bias-specific cognitive mechanism was affirmatively isolated."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a retrospective self-report, so cognitive mechanisms are inferred from the participant's explicit descriptions rather than direct observation.",
    "Retrieved corpus coverage was sparse and contained OCR noise; not all identified heuristics had direct corpus support, requiring disclosure of general-knowledge labels.",
    "Some closely related mechanisms, such as availability, recency, and alarm complacency, are difficult to fully separate within a single unfolding incident."
  ]
}

