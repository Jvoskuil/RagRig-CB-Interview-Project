# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal process review, and that's fine with you? Participant: Yeah, that's fine. Interviewer: Great. Can you tell me your role and roughly how long you've been in it? Participant: I'm the senior systems administrator for network infrastructure. I've owned our remote-access stack — VPN concentrator, firewall, related ACLs — for about six years now. Small team, just me and one other engineer. Interviewer: Perfect. I'd like you to walk me through a specific incident — the VPN concentrator vulnerability from earlier this year. Just give me the whole story first, then we'll go back through it in detail. Participant: Sure. So the vendor disclosed a critical remote-code-execution CVE in our concentrator's firmware — a 9.8 on the CVSS scale, about as bad as it gets. Same day, they released a patch. I applied it within a few hours, tested it, no issues. That part was straightforward. The bigger question was what to do longer-term. We'd actually scoped a full move to a cloud-based Zero Trust setup about eight months earlier, but it got shelved — budget cycle, other priorities. When this CVE hit, leadership asked whether we should revisit that. I ended up recommending we stay on the concentrator, patched and hardened, rather than restart the migration project right then. Interviewer: And that decision stuck for how long? Participant: About two weeks, until I actually did start engaging vendors — Vendor A, a cloud SASE/ZTNA platform, and Vendor B, an on-prem replacement appliance. I went back and forth, ended up shortlisting Vendor A. Then I did some informal outreach to peers at other firms our size, learned a lot of them had already gone with Vendor A. That helped me commit. Migration got approved, and we scheduled the cutover. Vendor recommended a two-week parallel run where old and new systems operate side by side. I compressed that to one week based on how previous cutovers had gone for me. We had some rough days afterward — a subset of users with hybrid authentication had intermittent access failures for several days before we sorted it out. Interviewer: Let's build the timeline in order. What happened right after you applied the patch? Participant: It installed clean, no service interruption, users never noticed. Two days later the vendor put out a follow-up advisory saying they were seeing exploitation attempts in the wild against systems that hadn't patched yet. That validated the urgency, but we were already covered. Interviewer: And the vendor evaluation — how did that actually unfold once proposals came in? Participant: Vendor A's deck opened with a stat — 98% of their enterprise migrations completed without a reported incident. Vendor B's numbers came through an analyst report, phrased differently: 2% of their on-prem deployments had a post-install incident in year one. Cost and timeline were basically a wash between the two. A follow-up technical call later clarified those were actually describing the same rate, just worded differently. But by then I'd already shortlisted A. Interviewer: What did the peer-forum conversation add? Participant: I posted in a regional admin group, and the response was pretty clear — five of six comparable firms in our sector had already gone with Vendor A's platform. Nobody shared much detail about their own environments, though. One of those five later told me, in a follow-up call, that they'd had to roll back some legacy application integrations after their rollout. Interviewer: Let's slow down on decision one — patch and stay versus migrate immediately versus take the concentrator offline. Walk me through your reasoning there. Participant: Taking it fully offline wasn't realistic — that's our only remote-access path for twelve hundred people, including trading desk staff. Between patching-and-staying versus fast-tracking a full migration, I leaned toward staying. We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out. Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one. I'll admit, I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically. Interviewer: What information did you have in front of you at that moment, versus what you were recalling from memory? Participant: In front of me: the CVSS score, the patch itself, and honestly not much detail yet on real-world exploitation — that came two days later. What I was recalling was that other firm's incident, which I remembered in a lot of detail because it got so much attention at the time. I used that story more than the actual advisory language when I was framing the urgency internally. Interviewer: Moving to the vendor decision — what specifically made Vendor A stand out? Participant: Honestly, that 98% figure just read better. '98% success' sounds a lot more solid than '2% incident rate,' even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials. Interviewer: How much weight did the peer adoption numbers carry when you committed to Vendor A? Participant: A lot, probably more than I'd like to admit. Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable. Interviewer: And the parallel-run decision — why compress it to one week? Participant: We were down a person — my other engineer was out — and the vendor's two-week default felt like it assumed more hands than we had. I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record. Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call. Interviewer: What would have changed your decision at that last step? Participant: If I'd mapped out specifically how the new authentication flow differed from what I'd handled before, rather than just leaning on 'I've done this kind of thing before,' I might have kept the full two weeks or pushed the date until we were fully staffed. Interviewer: Last few questions. If the peer forum hadn't mentioned adoption numbers at all, do you think you'd have approached the vendor decision differently? Participant: Probably. I think I'd have leaned more on the technical call that reconciled the two vendors' statistics, and maybe pushed harder for referenceable environments similar to ours before committing. Interviewer: And if staffing had been full during the cutover? Participant: I might still have compressed the timeline — that instinct came from my own history with cutovers, not just the staffing gap. But I probably would've caught the authentication mismatch sooner if I'd had a second set of eyes free to dig into it. Interviewer: Anything you'd want more information on, if you were facing this again? Participant: A cleaner side-by-side of vendor stats up front, normalized to the same format, so wording doesn't do the persuading. And probably a harder look at how similar peer environments actually were to ours before treating their choice as a green light.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.51s · gen 128.20s · total 133.1s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0243 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0214 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0208 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0206 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0199 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
6. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0190 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
7. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0186 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
8. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0182 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0168 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
14. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
15. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0166 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0164 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0160 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
18. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0157 (rrf) — _### cKniff 2004 ; Radley et al., 2013 and reporting others about medication errors, and it foste_
19. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
20. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0157 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
22. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0156 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## Evolut ionary Cognitive Psychology that could sources (exertion in scouting out a landscape, _
24. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0154 (rrf) — _### cKniff has been rigorouslystudiedas a factorintechnology adoption (Gefen,Karahanna,& Straub,_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
27. **ijcma-08-2012-0064.pdf** — 0.0153 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
28. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0152 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
29. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0152 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
31. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0151 (rrf) — _# Appendix A. Survey Questionnaire • Incorporating personal elements such as phone numbers, birt_
32. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0149 (rrf) — _# f Space Flight by inadequate communication. One contributing facto this lack of communication _
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
34. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
39. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0142 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
40. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0142 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
41. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
43. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0139 (rrf) — _We embedded behavioral measures in all three of our games to assess shortand longterm effects an_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
45. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0137 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
46. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0137 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
47. **Hallihan_etal_DTM_12.pdf** — 0.0136 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
48. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0135 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0133 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
50. **Lyell Automation bias and verification complexity.pdf** — 0.0133 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Blind evaluation of a single CTA interview for affirmative, mechanism-grounded cognitive bias occurrences. Retrieved passages were reviewed but did not provide direct definitions or validations for the specific biases identified."
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
      "bias_label": "overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "status quo bias",
      "alternative_labels": ["default bias", "status quo preference"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to prefer the current state of affairs and to disproportionately weight staying with an existing system or approach over changing to an alternative, even when change may have benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision one: patch-and-stay versus fast-track migration after VPN concentrator CVE",
      "decision_point_description": "Whether to continue with the patched concentrator or restart the Zero Trust migration immediately after the CVE",
      "affected_reasoning_operation": "Evaluation of alternative courses of action and risk trade-offs",
      "bias_specific_mechanism": "Disproportionate weighting of the existing, familiar concentrator configuration and avoidance of an unfamiliar migration path, without formally comparing transition controls or rollback plans.",
      "manifestation_in_interview": "The participant explicitly states he did not work through the fast-tracked migration's rollback plan or transition controls and gave staying extra weight because it was the environment he already knew.",
      "effect_on_reasoning_or_decision": "He recommended remaining on the patched concentrator rather than restarting migration, framing the choice as known versus unknown and limiting formal evaluation of the alternative.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out.",
          "evidence_explanation": "This quote shows the participant explicitly gave extra weight to the existing system because of familiarity and did not evaluate the migration alternative in a structured way, which is the core status quo mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one.",
          "evidence_explanation": "This known-versus-unknown framing further demonstrates that the preference was driven by the current state being perceived as safer simply because it was current and familiar."
        }
      ],
      "correction_or_counterevidence": "There was a plausible operational rationale for avoiding a rushed migration: the VPN was the only remote-access path for 1,200 people, and taking it offline was unrealistic. However, this does not explain the admitted failure to compare transition controls or the extra weight given solely to familiarity.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly defines or validates status quo bias. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the frequency, likelihood, or importance of an event by the ease with which instances come to mind, allowing vivid or emotionally salient cases to disproportionately influence judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Urgency framing for immediate patch decision after CVE disclosure",
      "decision_point_description": "How to estimate and communicate the urgency of applying the vendor patch internally to leadership",
      "affected_reasoning_operation": "Risk perception and urgency communication",
      "bias_specific_mechanism": "A vivid, easily recalled peer-firm ransomware breach dominated the assessment of patch urgency, displacing the less vivid current advisory information available at the time.",
      "manifestation_in_interview": "The participant reports recalling the peer-firm breach in detail and using that story more than the actual advisory language when framing urgency internally.",
      "effect_on_reasoning_or_decision": "Leadership received an urgency message driven by a memorable historical incident rather than a calibrated reading of the current CVE advisory and patch information.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'll admit, I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically.",
          "evidence_explanation": "This quote shows a salient, emotionally vivid past incident was present in the participant's mind and directly shaped how he communicated urgency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "What I was recalling was that other firm's incident, which I remembered in a lot of detail because it got so much attention at the time. I used that story more than the actual advisory language when I was framing the urgency internally.",
          "evidence_explanation": "This explicitly confirms that recall of a memorable case, rather than the current advisory information, drove the urgency framing, consistent with the availability heuristic."
        }
      ],
      "correction_or_counterevidence": "The peer incident was topically relevant and may have been a legitimate illustrative communication example. However, the participant acknowledges using it more than the actual advisory language and recalls it in detail, indicating availability-based weighting rather than calibrated risk communication.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly defines or validates the availability heuristic. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "framing effect",
      "alternative_labels": ["attribute framing effect", "valence framing"],
      "taxonomy_status": "established_label",
      "bias_definition": "Evaluation of equivalent information changes depending on whether it is presented in a positive or negative frame, such as success versus failure rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor shortlisting decision between Vendor A and Vendor B",
      "decision_point_description": "Selecting a shortlisted vendor based on vendor materials and analyst reports",
      "affected_reasoning_operation": "Risk evaluation and vendor comparison",
      "bias_specific_mechanism": "Equivalent base rates framed as 98% success versus 2% incident rate were not normalized; the positive frame was treated as more favorable and colored subsequent interpretation of vendor materials.",
      "manifestation_in_interview": "The participant says the 98% figure 'just read better' and that he did not convert the two rates, accepting the framing at face value before the equivalence was clarified.",
      "effect_on_reasoning_or_decision": "Vendor A was shortlisted partly due to positive framing rather than objective comparison; Vendor B's equivalent rate was perceived as less attractive.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Vendor A's deck opened with a stat — 98% of their enterprise migrations completed without a reported incident. Vendor B's numbers came through an analyst report, phrased differently: 2% of their on-prem deployments had a post-install incident in year one. Cost and timeline were basically a wash between the two. A follow-up technical call later clarified those were actually describing the same rate, just worded differently. But by then I'd already shortlisted A.",
          "evidence_explanation": "This establishes that the two vendors presented mathematically equivalent information in different frames and that the participant had already acted before the equivalence was clarified."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, that 98% figure just read better. '98% success' sounds a lot more solid than '2% incident rate,' even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials.",
          "evidence_explanation": "This is a direct admission that the surface framing, rather than objective numerical comparison, influenced his evaluation of the vendors, which is the core mechanism of the framing effect."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized the equivalence and acknowledged the framing effect. This later recognition does not negate the original distortion because the shortlisting decision had already been made.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly defines or validates the framing effect. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bandwagon effect",
      "alternative_labels": ["social proof heuristic", "conformity bias", "herd behavior"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to adopt a belief, decision, or behavior because many others have adopted it, treating group adoption as strong evidence of correctness or safety.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final vendor commitment after peer outreach",
      "decision_point_description": "Committing to Vendor A after informal outreach to peer firms",
      "affected_reasoning_operation": "Evidence weighting in vendor selection and peer information use",
      "bias_specific_mechanism": "Number of peer adoptions served as a social-proof shortcut; the participant inferred risk acceptability from what similar firms did and did not investigate environmental mismatch.",
      "manifestation_in_interview": "Five of six peers using Vendor A was taken as a strong signal on its own, without probing legacy app footprint or reference environments.",
      "effect_on_reasoning_or_decision": "Peer adoption helped commit the participant to Vendor A despite missing peer environment detail and later learning one peer had rollback issues.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "A lot, probably more than I'd like to admit. Five out of six firms choosing the same platform felt like a strong signal on its own.",
          "evidence_explanation": "This quote shows the participant treated the count of peer adopters as intrinsically persuasive evidence for the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable.",
          "evidence_explanation": "This demonstrates the social-proof mechanism: the number of adopters substituted for direct assessment of fit with his own environment."
        }
      ],
      "correction_or_counterevidence": "Peer adoption can be a legitimate market signal in vendor selection. However, the participant admits not pushing on environmental fit, and one peer later disclosed rollback issues, indicating the consensus was treated as sufficient evidence of suitability.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly defines or validates the bandwagon effect. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence effect",
      "alternative_labels": ["overconfidence bias", "illusion of validity"],
      "taxonomy_status": "established_label",
      "bias_definition": "A person's subjective confidence in their judgment or ability is greater than objective accuracy, often fed by prior success and underestimation of uncertainty.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Parallel-run duration decision ahead of vendor cutover",
      "decision_point_description": "Whether to accept the vendor's two-week parallel-run default or compress it to one week",
      "affected_reasoning_operation": "Implementation planning and risk assessment under uncertainty",
      "bias_specific_mechanism": "Overgeneralization from three past successful cutovers to a materially different authentication architecture; overconfidence in one's ability to manage the transition with reduced staffing.",
      "manifestation_in_interview": "The participant compressed the parallel run to one week based on a personal track record and did not weigh the architectural difference or staffing gap until after problems arose.",
      "effect_on_reasoning_or_decision": "The cutover proceeded with a shorter safety window, and the participant himself links the failure to map the new authentication flow to the compressed timeline.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record.",
          "evidence_explanation": "This quote shows subjective confidence was grounded in limited prior successes rather than an evaluation of the current task's specific difficulty."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call.",
          "evidence_explanation": "This confirms the overconfidence mechanism: the participant generalized from past experience without adjusting for materially different conditions."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd mapped out specifically how the new authentication flow differed from what I'd handled before, rather than just leaning on 'I've done this kind of thing before,' I might have kept the full two weeks or pushed the date until we were fully staffed.",
          "evidence_explanation": "This links the biased reasoning directly to the planning decision and its potential alternative, reinforcing that the overconfidence effect influenced the schedule choice."
        }
      ],
      "correction_or_counterevidence": "There was a genuine staffing constraint, and prior cutover experience could be relevant to planning. However, the participant explicitly distinguishes the new authentication model and admits failing to weigh that difference.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly defines or validates the overconfidence effect. Classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "sunk cost fallacy",
      "alternative_labels": ["sunk cost effect"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision one: patch-and-stay versus fast-track migration",
      "supporting_interview_quote": "We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold.",
      "plausible_mechanism": "Past investment in the existing ACL and firewall configuration may have made abandoning the current system feel wasteful, independently contributing to the stay decision.",
      "why_not_identified": "The transcript emphasizes familiarity and known-versus-unknown preference rather than a clear concern about losing past investment. Status quo bias already accounts for the observed reasoning."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory search"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Vendor peer outreach after shortlisting Vendor A",
      "supporting_interview_quote": "Then I did some informal outreach to peers at other firms our size, learned a lot of them had already gone with Vendor A. That helped me commit.",
      "plausible_mechanism": "After shortlisting Vendor A, the participant may have sought or weighted peer information that supported that choice.",
      "why_not_identified": "No explicit evidence of a confirmatory search strategy, selective attention to disconfirming peer information at that time, or motivated reasoning beyond social proof. Peer outreach can be legitimate due diligence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus did not contain direct definitions or validations for the specific biases identified, so classifications rely on established cognitive-science knowledge rather than RAG passage support.",
    "Analysis is based on self-report from a single interview; there is no independent behavioral or outcome data.",
    "The interview includes retrospective reflections, but occurrences were assessed using information available to the participant at the time of each reasoning episode."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal process review, and that's fine with you? Participant: Yeah, that's fine. Interviewer: Great. Can you tell me your role and roughly how long you've been in it? Participant: I'm the senior systems administrator for network infrastructure. I've owned our remote-access stack — VPN concentrator, firewall, related ACLs — for about six years now. Small team, just me and one other engineer. Interviewer: Perfect. I'd like you to walk me through a specific incident — the VPN concentrator vulnerability from earlier this year. Just give me the whole story first, then we'll go back through it in detail. Participant: Sure. So the vendor disclosed a critical remote-code-execution CVE in our concentrator's firmware — a 9.8 on the CVSS scale, about as bad as it gets. Same day, they released a patch. I applied it within a few hours, tested it, no issues. That part was straightforward. The bigger question was what to do longer-term. We'd actually scoped a full move to a cloud-based Zero Trust setup about eight months earlier, but it got shelved — budget cycle, other priorities. When this CVE hit, leadership asked whether we should revisit that. I ended up recommending we stay on the concentrator, patched and hardened, rather than restart the migration project right then. Interviewer: And that decision stuck for how long? Participant: About two weeks, until I actually did start engaging vendors — Vendor A, a cloud SASE/ZTNA platform, and Vendor B, an on-prem replacement appliance. I went back and forth, ended up shortlisting Vendor A. Then I did some informal outreach to peers at other firms our size, learned a lot of them had already gone with Vendor A. That helped me commit. Migration got approved, and we scheduled the cutover. Vendor recommended a two-week parallel run where old and new systems operate side by side. I compressed that to one week based on how previous cutovers had gone for me. We had some rough days afterward — a subset of users with hybrid authentication had intermittent access failures for several days before we sorted it out. Interviewer: Let's build the timeline in order. What happened right after you applied the patch? Participant: It installed clean, no service interruption, users never noticed. Two days later the vendor put out a follow-up advisory saying they were seeing exploitation attempts in the wild against systems that hadn't patched yet. That validated the urgency, but we were already covered. Interviewer: And the vendor evaluation — how did that actually unfold once proposals came in? Participant: Vendor A's deck opened with a stat — 98% of their enterprise migrations completed without a reported incident. Vendor B's numbers came through an analyst report, phrased differently: 2% of their on-prem deployments had a post-install incident in year one. Cost and timeline were basically a wash between the two. A follow-up technical call later clarified those were actually describing the same rate, just worded differently. But by then I'd already shortlisted A. Interviewer: What did the peer-forum conversation add? Participant: I posted in a regional admin group, and the response was pretty clear — five of six comparable firms in our sector had already gone with Vendor A's platform. Nobody shared much detail about their own environments, though. One of those five later told me, in a follow-up call, that they'd had to roll back some legacy application integrations after their rollout. Interviewer: Let's slow down on decision one — patch and stay versus migrate immediately versus take the concentrator offline. Walk me through your reasoning there. Participant: Taking it fully offline wasn't realistic — that's our only remote-access path for twelve hundred people, including trading desk staff. Between patching-and-staying versus fast-tracking a full migration, I leaned toward staying. We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out. Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one. I'll admit, I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically. Interviewer: What information did you have in front of you at that moment, versus what you were recalling from memory? Participant: In front of me: the CVSS score, the patch itself, and honestly not much detail yet on real-world exploitation — that came two days later. What I was recalling was that other firm's incident, which I remembered in a lot of detail because it got so much attention at the time. I used that story more than the actual advisory language when I was framing the urgency internally. Interviewer: Moving to the vendor decision — what specifically made Vendor A stand out? Participant: Honestly, that 98% figure just read better. '98% success' sounds a lot more solid than '2% incident rate,' even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials. Interviewer: How much weight did the peer adoption numbers carry when you committed to Vendor A? Participant: A lot, probably more than I'd like to admit. Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable. Interviewer: And the parallel-run decision — why compress it to one week? Participant: We were down a person — my other engineer was out — and the vendor's two-week default felt like it assumed more hands than we had. I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record. Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call. Interviewer: What would have changed your decision at that last step? Participant: If I'd mapped out specifically how the new authentication flow differed from what I'd handled before, rather than just leaning on 'I've done this kind of thing before,' I might have kept the full two weeks or pushed the date until we were fully staffed. Interviewer: Last few questions. If the peer forum hadn't mentioned adoption numbers at all, do you think you'd have approached the vendor decision differently? Participant: Probably. I think I'd have leaned more on the technical call that reconciled the two vendors' statistics, and maybe pushed harder for referenceable environments similar to ours before committing. Interviewer: And if staffing had been full during the cutover? Participant: I might still have compressed the timeline — that instinct came from my own history with cutovers, not just the staffing gap. But I probably would've caught the authentication mismatch sooner if I'd had a second set of eyes free to dig into it. Interviewer: Anything you'd want more information on, if you were facing this again? Participant: A cleaner side-by-side of vendor stats up front, normalized to the same format, so wording doesn't do the persuading. And probably a harder look at how similar peer environments actually were to ours before treating their choice as a green light.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.38s · gen 136.52s · total 141.3s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0243 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0214 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0208 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0206 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0199 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
6. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0190 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
7. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0186 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
8. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0182 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0168 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
14. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
15. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0166 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0164 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0160 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
18. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0157 (rrf) — _### cKniff 2004 ; Radley et al., 2013 and reporting others about medication errors, and it foste_
19. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
20. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0157 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
22. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0156 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## Evolut ionary Cognitive Psychology that could sources (exertion in scouting out a landscape, _
24. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0154 (rrf) — _### cKniff has been rigorouslystudiedas a factorintechnology adoption (Gefen,Karahanna,& Straub,_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
27. **ijcma-08-2012-0064.pdf** — 0.0153 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
28. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0152 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
29. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0152 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
31. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0151 (rrf) — _# Appendix A. Survey Questionnaire • Incorporating personal elements such as phone numbers, birt_
32. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0149 (rrf) — _# f Space Flight by inadequate communication. One contributing facto this lack of communication _
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
34. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
39. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0142 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
40. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0142 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
41. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
43. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0139 (rrf) — _We embedded behavioral measures in all three of our games to assess shortand longterm effects an_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
45. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0137 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
46. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0137 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
47. **Hallihan_etal_DTM_12.pdf** — 0.0136 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
48. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0135 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0133 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
50. **Lyell Automation bias and verification complexity.pdf** — 0.0133 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first review of a single participant’s retrospective account of two connected decisions: patch-and-stay versus migrate after a critical VPN vulnerability, and vendor/platform implementation timeline. Only bias-specific mechanisms with affirmative interview evidence are reported."
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
      "bias_label": "status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "status quo bias",
      "alternative_labels": [
        "default bias",
        "familiarity bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A preference for the current state and an overvaluation of the incumbent option relative to alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to stay on patched concentrator versus fast-tracking migration",
      "decision_point_description": "Whether to recommend staying on the patched VPN concentrator or fast-tracking the previously scoped Zero Trust migration immediately after the critical CVE patch.",
      "affected_reasoning_operation": "Choice under uncertainty between maintaining the current system and migrating.",
      "bias_specific_mechanism": "The participant gave extra weight to the current VPN concentrator because it was familiar and known 'cold'; he did not formally evaluate the alternative migration's rollback or transition controls before recommending staying, and framed the migration as an unknown problem. This is a distinct current-state preference mechanism, not merely a resource or feasibility constraint.",
      "manifestation_in_interview": "The participant explicitly stated that he leaned toward staying because the existing environment was known to him and that he gave staying extra weight without working through the migration alternative.",
      "effect_on_reasoning_or_decision": "Led to recommending they stay on the concentrator, patched and hardened, rather than revisiting migration at that point.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Between patching-and-staying versus fast-tracking a full migration, I leaned toward staying. We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out. Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one.",
          "evidence_explanation": "The quote directly states that the current system's familiarity received extra weighting and that the alternative was not fully evaluated, which is the core mechanism of status quo bias."
        }
      ],
      "correction_or_counterevidence": "A short-term patch-and-stay response may have been partly defensible because taking the concentrator offline was described as operationally unrealistic; two weeks later the participant did engage vendors and the migration was ultimately approved.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derived from general knowledge; retrieved corpus support for this specific label was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive shortcut in which judgments of frequency, probability, or urgency are influenced by the ease or vividness with which instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Framing and communicating patch urgency to leadership",
      "decision_point_description": "How to internally communicate the urgency of patching the VPN concentrator before later real-world exploitation detail was available.",
      "affected_reasoning_operation": "Risk and urgency judgment and internal risk communication.",
      "bias_specific_mechanism": "The participant relied on a vivid, publicized peer-firm ransomware incident recalled from memory rather than on the current advisory language or abstract CVSS data when framing urgency. The vivid personal recollection was used as a mental benchmark for risk.",
      "manifestation_in_interview": "He said the peer breach was 'very much in my head' and that he used that story more than the actual advisory language when framing urgency internally.",
      "effect_on_reasoning_or_decision": "The recalled breach shaped how the participant communicated urgency to leadership, giving the patch message a vivid, potentially disproportionate emphasis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'll admit, I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically.",
          "evidence_explanation": "The participant openly links the vivid remembered peer incident to his urgency communication, which is the availability heuristic operating on a salient easily recalled case."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In front of me: the CVSS score, the patch itself, and honestly not much detail yet on real-world exploitation — that came two days later. What I was recalling was that other firm's incident, which I remembered in a lot of detail because it got so much attention at the time. I used that story more than the actual advisory language when I was framing the urgency internally.",
          "evidence_explanation": "This comparison shows the recalled incident outweighed the available abstract information when the participant constructed his urgency message."
        }
      ],
      "correction_or_counterevidence": "The urgency was later independently validated by a vendor advisory of active exploitation attempts, and the patch was already clearly indicated by the extreme CVSS score.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derived from general knowledge; retrieved corpus support for this specific label was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "framing effect",
      "alternative_labels": [
        "attribute framing",
        "valence framing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A decision bias in which equivalent information presented with different wording or valence leads to different evaluations or choices.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor shortlisting after comparing Vendor A and Vendor B statistics",
      "decision_point_description": "Whether to shortlist Vendor A or Vendor B after receiving proposals framed in success-rate versus incident-rate terms.",
      "affected_reasoning_operation": "Evaluation of vendor statistics and vendor shortlisting.",
      "bias_specific_mechanism": "The participant processed statistically equivalent vendor information according to its surface framing: '98% success' was more attractive than '2% incident rate,' and he did not normalize or convert the figures at the time.",
      "manifestation_in_interview": "He stated that the 98% figure 'just read better' and that he took the framing at face value.",
      "effect_on_reasoning_or_decision": "The positive framing colored his reading of Vendor A's materials and led to shortlisting Vendor A before recognizing the two statistics were equivalent.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, that 98% figure just read better. '98% success' sounds a lot more solid than '2% incident rate,' even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials.",
          "evidence_explanation": "This explicitly describes valence-based evaluation changing the participant's interpretation of equivalent statistics, which is the core mechanism of the framing effect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A follow-up technical call later clarified those were actually describing the same rate, just worded differently. But by then I'd already shortlisted A.",
          "evidence_explanation": "This reveals that the framing affected a decision before the equivalence was corrected, supporting a real effect on vendor shortlisting."
        }
      ],
      "correction_or_counterevidence": "A follow-up technical call later clarified the equivalence, but this occurred after the participant had already shortlisted Vendor A.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derived from general knowledge; retrieved corpus support for this specific label was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "bandwagon effect",
      "alternative_labels": [
        "social proof bias",
        "imitation heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to adopt a belief or decision because many others have adopted it, using majority behavior as evidence of quality or safety.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor A commitment after peer-forum adoption information",
      "decision_point_description": "Whether to commit to Vendor A after learning that five of six comparable peer firms had adopted its platform.",
      "affected_reasoning_operation": "Vendor commitment decision and assessment of fit with the organization.",
      "bias_specific_mechanism": "The participant treated the majority adoption of peer firms as a strong stand-alone signal of suitability and reduced scrutiny of whether those environments matched his own legacy application and authentication footprint.",
      "manifestation_in_interview": "He said the peer adoption numbers carried 'a lot' of weight and that he did not push hard on environmental differences because he inferred the risk was manageable from peer comfort.",
      "effect_on_reasoning_or_decision": "Peer adoption strengthened the participant's commitment to Vendor A and reduced investigation of whether vendor choices matched his own environment's requirements.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Five out of six comparable firms in our sector had already gone with Vendor A's platform. Nobody shared much detail about their own environments, though.",
          "evidence_explanation": "The majority behavior was available as a compelling signal without detailed environment-level comparison, creating conditions for social proof to substitute for fit analysis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A lot, probably more than I'd like to admit. Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable.",
          "evidence_explanation": "This explicitly connects majority adoption to the participant's lowered scrutiny of environmental mismatch, which is the core mechanism of the bandwagon effect."
        }
      ],
      "correction_or_counterevidence": "One peer later disclosed a rollback affecting legacy application integrations, suggesting the social proof was not fully diagnostic; however this detail appears to have arrived after the participant had already committed.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derived from general knowledge; retrieved corpus support for this specific label was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias",
        "similarity heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which the probability of an event or outcome is judged by its superficial similarity to a prototype or prior instances, while ignoring diagnostic base-rate or structural differences.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Parallel-run timeline compression decision",
      "decision_point_description": "Whether to retain the vendor-recommended two-week parallel run or compress it to one week.",
      "affected_reasoning_operation": "Parallel-run timeline planning and risk assessment.",
      "bias_specific_mechanism": "The participant judged the new authentication cutover by its resemblance to earlier successful cutovers and did not weigh a diagnostic difference: the new architecture used a different authentication model he did not already know well.",
      "manifestation_in_interview": "He said the compressed window felt reasonable based on his past cutover track record, then acknowledged he had not really weighed the different authentication model.",
      "effect_on_reasoning_or_decision": "Led to compressing the vendor-recommended two-week parallel run to one week, after which hybrid-authentication users experienced intermittent access failures.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record. Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call.",
          "evidence_explanation": "The participant used prior cutovers as representative of the current one while explicitly acknowledging he ignored a structurally diagnostic difference, which is the core mechanism of the representativeness heuristic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I might still have compressed the timeline — that instinct came from my own history with cutovers, not just the staffing gap.",
          "evidence_explanation": "This confirms the decision was driven by perceived similarity to his own prior experiences rather than solely by the external staffing constraint."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized the earlier cutovers were architecturally different and that a fuller mapping of the new authentication flow might have changed the timeline. Staffing shortage also contributed, but the participant stated the instinct came from his own history.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support available; the source links reliance on the representativeness heuristic to misjudgment.",
      "corpus_evidence": [
        {
          "source_identifier": "Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf",
          "paper_title": "Exploring Heuristics and Biases in Cybersecurity: A Factor Analysis of Social Engineering Vulnerabilities",
          "authors": "Greavu-Şerban et al.",
          "publication_year": "2025",
          "retrieved_passage_or_finding": "Thus, the representativeness heuristic that respondents relied on in their decisionmaking can lead to misjudgments regarding the level of safety [31].",
          "mechanism_supported_by_source": "The source identifies reliance on the representativeness heuristic as a cause of misjudgment.",
          "relevance_to_this_occurrence": "The participant judged a new, different authentication cutover by its resemblance to earlier cutovers and did not weigh a diagnostic difference, matching the representativeness-based misjudgment pattern."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": [
        "selective exposure",
        "congeniality bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Vendor selection peer-community validation",
      "supporting_interview_quote": "I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable.",
      "plausible_mechanism": "The participant may have used the peer forum to confirm an already favorable lean toward Vendor A and avoided disconfirming questions about environmental fit.",
      "why_not_identified": "The quote also fits a social-proof/bandwagon heuristic, and there is no clear statement that the participant sought or interpreted information to confirm a pre-existing preference rather than using majority adoption as a general risk signal."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Single participant retrospective self-report; bias mechanisms are inferred from the participant's own descriptions rather than independent behavioral measures.",
    "Retrieved corpus support was limited; most labels derive from general cognitive-science knowledge and are disclosed as such.",
    "Some mechanisms co-occur within the same broad decision context but are separated by distinct reasoning operations.",
    "The analysis does not presume that every biased mechanism produced a clearly wrong decision; some decisions may also have had defensible non-bias components."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal process review, and that's fine with you? Participant: Yeah, that's fine. Interviewer: Great. Can you tell me your role and roughly how long you've been in it? Participant: I'm the senior systems administrator for network infrastructure. I've owned our remote-access stack — VPN concentrator, firewall, related ACLs — for about six years now. Small team, just me and one other engineer. Interviewer: Perfect. I'd like you to walk me through a specific incident — the VPN concentrator vulnerability from earlier this year. Just give me the whole story first, then we'll go back through it in detail. Participant: Sure. So the vendor disclosed a critical remote-code-execution CVE in our concentrator's firmware — a 9.8 on the CVSS scale, about as bad as it gets. Same day, they released a patch. I applied it within a few hours, tested it, no issues. That part was straightforward. The bigger question was what to do longer-term. We'd actually scoped a full move to a cloud-based Zero Trust setup about eight months earlier, but it got shelved — budget cycle, other priorities. When this CVE hit, leadership asked whether we should revisit that. I ended up recommending we stay on the concentrator, patched and hardened, rather than restart the migration project right then. Interviewer: And that decision stuck for how long? Participant: About two weeks, until I actually did start engaging vendors — Vendor A, a cloud SASE/ZTNA platform, and Vendor B, an on-prem replacement appliance. I went back and forth, ended up shortlisting Vendor A. Then I did some informal outreach to peers at other firms our size, learned a lot of them had already gone with Vendor A. That helped me commit. Migration got approved, and we scheduled the cutover. Vendor recommended a two-week parallel run where old and new systems operate side by side. I compressed that to one week based on how previous cutovers had gone for me. We had some rough days afterward — a subset of users with hybrid authentication had intermittent access failures for several days before we sorted it out. Interviewer: Let's build the timeline in order. What happened right after you applied the patch? Participant: It installed clean, no service interruption, users never noticed. Two days later the vendor put out a follow-up advisory saying they were seeing exploitation attempts in the wild against systems that hadn't patched yet. That validated the urgency, but we were already covered. Interviewer: And the vendor evaluation — how did that actually unfold once proposals came in? Participant: Vendor A's deck opened with a stat — 98% of their enterprise migrations completed without a reported incident. Vendor B's numbers came through an analyst report, phrased differently: 2% of their on-prem deployments had a post-install incident in year one. Cost and timeline were basically a wash between the two. A follow-up technical call later clarified those were actually describing the same rate, just worded differently. But by then I'd already shortlisted A. Interviewer: What did the peer-forum conversation add? Participant: I posted in a regional admin group, and the response was pretty clear — five of six comparable firms in our sector had already gone with Vendor A's platform. Nobody shared much detail about their own environments, though. One of those five later told me, in a follow-up call, that they'd had to roll back some legacy application integrations after their rollout. Interviewer: Let's slow down on decision one — patch and stay versus migrate immediately versus take the concentrator offline. Walk me through your reasoning there. Participant: Taking it fully offline wasn't realistic — that's our only remote-access path for twelve hundred people, including trading desk staff. Between patching-and-staying versus fast-tracking a full migration, I leaned toward staying. We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out. Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one. I'll admit, I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically. Interviewer: What information did you have in front of you at that moment, versus what you were recalling from memory? Participant: In front of me: the CVSS score, the patch itself, and honestly not much detail yet on real-world exploitation — that came two days later. What I was recalling was that other firm's incident, which I remembered in a lot of detail because it got so much attention at the time. I used that story more than the actual advisory language when I was framing the urgency internally. Interviewer: Moving to the vendor decision — what specifically made Vendor A stand out? Participant: Honestly, that 98% figure just read better. '98% success' sounds a lot more solid than '2% incident rate,' even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials. Interviewer: How much weight did the peer adoption numbers carry when you committed to Vendor A? Participant: A lot, probably more than I'd like to admit. Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable. Interviewer: And the parallel-run decision — why compress it to one week? Participant: We were down a person — my other engineer was out — and the vendor's two-week default felt like it assumed more hands than we had. I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record. Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call. Interviewer: What would have changed your decision at that last step? Participant: If I'd mapped out specifically how the new authentication flow differed from what I'd handled before, rather than just leaning on 'I've done this kind of thing before,' I might have kept the full two weeks or pushed the date until we were fully staffed. Interviewer: Last few questions. If the peer forum hadn't mentioned adoption numbers at all, do you think you'd have approached the vendor decision differently? Participant: Probably. I think I'd have leaned more on the technical call that reconciled the two vendors' statistics, and maybe pushed harder for referenceable environments similar to ours before committing. Interviewer: And if staffing had been full during the cutover? Participant: I might still have compressed the timeline — that instinct came from my own history with cutovers, not just the staffing gap. But I probably would've caught the authentication mismatch sooner if I'd had a second set of eyes free to dig into it. Interviewer: Anything you'd want more information on, if you were facing this again? Participant: A cleaner side-by-side of vendor stats up front, normalized to the same format, so wording doesn't do the persuading. And probably a harder look at how similar peer environments actually were to ours before treating their choice as a green light.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.36s · gen 165.49s · total 170.3s_

**Retrieved** (ranked by store ranker):
1. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0243 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0214 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0208 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0206 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
5. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0199 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
6. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0190 (rrf) — _# 4. Results For the control group, ADE was 0.0223 (95% CI: \[ treated group, ADE was 0.0321 (95_
7. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0186 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
8. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0182 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0182 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
11. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
12. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0175 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0168 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
14. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
15. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0166 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0164 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0160 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
18. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0157 (rrf) — _### cKniff 2004 ; Radley et al., 2013 and reporting others about medication errors, and it foste_
19. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
20. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0157 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0156 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
22. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0156 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
23. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## Evolut ionary Cognitive Psychology that could sources (exertion in scouting out a landscape, _
24. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0154 (rrf) — _### cKniff has been rigorouslystudiedas a factorintechnology adoption (Gefen,Karahanna,& Straub,_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0154 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
26. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
27. **ijcma-08-2012-0064.pdf** — 0.0153 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
28. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0152 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
29. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0152 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
31. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0151 (rrf) — _# Appendix A. Survey Questionnaire • Incorporating personal elements such as phone numbers, birt_
32. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0149 (rrf) — _# f Space Flight by inadequate communication. One contributing facto this lack of communication _
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
34. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0147 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0145 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
37. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
38. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0143 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
39. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0142 (rrf) — _# 5. Discussions serve as an adaptive strategy when individuals face time constraints, albeit at_
40. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0142 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
41. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration tructed to be part_
42. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology that evalua action to ti on s are evaluate_
43. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0139 (rrf) — _We embedded behavioral measures in all three of our games to assess shortand longterm effects an_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review revolution began, which “introduced applied social psychology and managem_
45. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0137 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
46. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0137 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
47. **Hallihan_etal_DTM_12.pdf** — 0.0136 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
48. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0135 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration reported that in a_
49. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0133 (rrf) — _# Co nceptual Foundations of Evolut ionary Psychology Th e fact that the brain processes informa_
50. **Lyell Automation bias and verification complexity.pdf** — 0.0133 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Interview analyzed for positively evidenced cognitive-bias mechanisms affecting participant reasoning, judgment, communication, and decisions. The provided corpus was reviewed but did not contain direct support for the specific mechanisms identified; where corpus support was unavailable, widely established cognitive-science labels were used with disclosure."
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
      "bias_label": "Framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Status quo bias",
      "alternative_labels": ["status quo preference", "default bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Preferential weighting of the existing state over alternatives, with the risks and uncertainty of change overvalued relative to the known current state.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Recommendation to patch-and-stay rather than fast-track migration after CVE",
      "decision_point_description": "After the critical VPN concentrator CVE and patch, leadership asked whether to revisit the cloud Zero Trust migration; the participant recommended staying on the concentrator.",
      "affected_reasoning_operation": "Weighing the existing remote-access environment against a fast-tracked migration and recommending a course of action under uncertainty.",
      "bias_specific_mechanism": "Overweighting the incumbent system because it was highly familiar and known; avoiding detailed evaluation of the fast-track migration's rollback plan or transition controls; treating the current state as safer partly because it was the current state.",
      "manifestation_in_interview": "The participant explicitly says he gave staying extra weight because he knew the environment 'inside and out' and did not work through what a fast-tracked migration would have required. He framed moving off the current system as trading a known problem for an unknown one.",
      "effect_on_reasoning_or_decision": "The recommendation was anchored toward retaining the patched concentrator while the migration alternative was not seriously evaluated in that decision moment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I ended up recommending we stay on the concentrator, patched and hardened, rather than restart the migration project right then.",
          "evidence_explanation": "Establishes the decision episode and the outcome of the initial status-quo favoring recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold.",
          "evidence_explanation": "Shows the familiarity basis that the participant used to weight the incumbent system more heavily."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out. Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one.",
          "evidence_explanation": "Directly states the status quo mechanism: extra weight given to the current environment and avoidance of detailed evaluation of the alternative."
        }
      ],
      "correction_or_counterevidence": "There were legitimate operational grounds to keep the concentrator, including its role as the sole remote-access path and the clean patch. However, the participant's explicit attribution of extra weight to familiarity and failure to evaluate transition controls supports a distinct status quo mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The provided corpus did not contain direct retrieved support for status quo bias; the label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Framing effect",
      "alternative_labels": ["equivalence framing", "attribute framing"],
      "taxonomy_status": "established_label",
      "bias_definition": "Systematically different evaluation of equivalent information depending on whether it is presented in a positive or negative frame.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Shortlisting Vendor A during vendor comparison",
      "decision_point_description": "While comparing Vendor A and Vendor B proposals, equivalent vendor performance data were presented as 98% success versus 2% incident rate.",
      "affected_reasoning_operation": "Comparative vendor risk assessment and shortlisting decision.",
      "bias_specific_mechanism": "The participant evaluated the positively framed '98% success' as more reassuring than the negatively framed '2% incident rate' without converting them to a common metric; the favorable frame then colored interpretation of the vendor's remaining materials.",
      "manifestation_in_interview": "The participant states that the 98% figure 'read better' and that he did not perform the conversion at the time. He acknowledges taking the framing at face value, which influenced how he interpreted Vendor A's materials.",
      "effect_on_reasoning_or_decision": "Vendor A was shortlisted partly because the same statistical information was framed more attractively, before a later technical call clarified that the rates were equivalent.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went back and forth, ended up shortlisting Vendor A.",
          "evidence_explanation": "Identifies the decision outcome that the framing effect is alleged to have influenced."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Vendor A's deck opened with a stat — 98% of their enterprise migrations completed without a reported incident. Vendor B's numbers came through an analyst report, phrased differently: 2% of their on-prem deployments had a post-install incident in year one. Cost and timeline were basically a wash between the two.",
          "evidence_explanation": "Establishes that the two vendors were otherwise comparable and that the key performance information was equivalent but differently framed."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A follow-up technical call later clarified those were actually describing the same rate, just worded differently. But by then I'd already shortlisted A.",
          "evidence_explanation": "Shows that the equivalence was clarified only after the biased interpretation had already affected the shortlisting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, that 98% figure just read better. '98% success' sounds a lot more solid than '2% incident rate,' even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials.",
          "evidence_explanation": "Directly states the framing mechanism and its effect on the evaluation of Vendor A's materials."
        }
      ],
      "correction_or_counterevidence": "A later technical call clarified that the statistics described the same underlying rate, but this correction occurred only after the participant had already shortlisted Vendor A, so it did not neutralize the initial effect on the shortlist decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The provided corpus did not contain direct retrieved support for framing effects; the label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Bandwagon effect",
      "alternative_labels": ["social proof", "herd behavior"],
      "taxonomy_status": "established_label",
      "bias_definition": "Adopting a choice substantially because others have adopted it, while reducing independent analysis of fit to one's own situation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final commitment to Vendor A after peer adoption feedback",
      "decision_point_description": "After regional peer outreach showed five of six comparable firms had chosen Vendor A, the participant used this adoption signal to commit to Vendor A.",
      "affected_reasoning_operation": "Risk assessment and final vendor commitment decision.",
      "bias_specific_mechanism": "Treating majority peer adoption as a strong signal of suitability and risk manageability while reducing scrutiny of whether peer environments matched the participant's legacy application and authentication footprint.",
      "manifestation_in_interview": "The participant says the peer adoption numbers carried a lot of weight, that five of six firms felt like a strong signal on its own, and that he did not push hard on fit with his own environment.",
      "effect_on_reasoning_or_decision": "The final vendor commitment was reinforced by social proof, with insufficient independent evaluation of legacy-system compatibility before committing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Then I did some informal outreach to peers at other firms our size, learned a lot of them had already gone with Vendor A. That helped me commit.",
          "evidence_explanation": "Identifies peer adoption as a direct input into the commitment decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I posted in a regional admin group, and the response was pretty clear — five of six comparable firms in our sector had already gone with Vendor A's platform. Nobody shared much detail about their own environments, though.",
          "evidence_explanation": "Shows the social proof information and the absence of detailed environment-level comparison data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A lot, probably more than I'd like to admit. Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable.",
          "evidence_explanation": "Directly states the social proof mechanism: majority adoption was treated as risk-reducing evidence without close analysis of local fit."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably. I think I'd have leaned more on the technical call that reconciled the two vendors' statistics, and maybe pushed harder for referenceable environments similar to ours before committing.",
          "evidence_explanation": "Counterfactual admission that without the adoption signal, the decision process would have relied more on technical comparison and fit analysis."
        }
      ],
      "correction_or_counterevidence": "One of the five peers later disclosed rollback of some legacy application integrations, indicating the peer environments were not fully comparable. This information arrived only after the participant had committed.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The provided corpus did not contain direct retrieved support for bandwagon effect or social proof; the label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Overconfidence effect",
      "alternative_labels": ["overconfidence bias", "optimism bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Excessive confidence in one's own judgment or plan based on past success, leading to underestimation of risk in novel or dissimilar conditions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Compressing vendor-recommended two-week parallel run to one week",
      "decision_point_description": "During cutover planning, the participant reduced the vendor's two-week parallel-run recommendation to one week based on prior cutover history.",
      "affected_reasoning_operation": "Duration and risk planning for the system cutover.",
      "bias_specific_mechanism": "Overgeneralizing from three prior cutovers that had succeeded without a formal parallel-run phase, while failing to account for the new platform's different authentication model and reduced staffing.",
      "manifestation_in_interview": "The participant reports that previous cutovers had gone fine, so a compressed one-week window felt reasonable. He later acknowledges those cutovers were on familiar architecture and that he did not weigh the authentication-model difference when making the call.",
      "effect_on_reasoning_or_decision": "The one-week parallel run was selected rather than the vendor's recommended two weeks; the participant later associated this with rough days and intermittent access failures, though the decision itself is the bias-relevant outcome.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Vendor recommended a two-week parallel run where old and new systems operate side by side. I compressed that to one week based on how previous cutovers had gone for me.",
          "evidence_explanation": "Establishes the planning decision and its reliance on personal cutover history."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record. Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call.",
          "evidence_explanation": "Directly states the overgeneralization from prior success and failure to incorporate the novel task conditions into the planning judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd mapped out specifically how the new authentication flow differed from what I'd handled before, rather than just leaning on 'I've done this kind of thing before,' I might have kept the full two weeks or pushed the date until we were fully staffed.",
          "evidence_explanation": "Counterfactual admission that a less overconfident, more task-specific analysis could have changed the decision."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized the dissimilarity between the new authentication model and prior cutovers. Some access failures followed the compressed cutover, though this outcome alone is not treated as proof of bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The provided corpus did not contain direct retrieved support for overconfidence effect; the label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging urgency or risk by the ease with which salient instances come to mind, rather than by current diagnostic information or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Internal urgency framing around the VPN patch after CVE",
      "decision_point_description": "When explaining internally why the patch needed urgent action, the participant drew heavily on a vivid peer-firm ransomware breach from memory rather than the current advisory's limited real-world exploitation information.",
      "affected_reasoning_operation": "Risk perception and communication of urgency to leadership.",
      "bias_specific_mechanism": "The participant recalled a highly salient, emotionally charged prior breach and used that story more than the actual advisory language when framing the urgency of patching, allowing recall availability to substitute for current threat information.",
      "manifestation_in_interview": "The participant states that the peer-firm incident was very much in his head when explaining why the patch needed to happen quickly, and that he used the remembered story more than the advisory language.",
      "effect_on_reasoning_or_decision": "The urgency framing was shaped by a vivid remembered incident even though the current advisory did not yet contain detailed real-world exploitation information.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'll admit, I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically.",
          "evidence_explanation": "Shows that a vivid, easily recalled prior incident was active during the urgency communication."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In front of me: the CVSS score, the patch itself, and honestly not much detail yet on real-world exploitation — that came two days later. What I was recalling was that other firm's incident, which I remembered in a lot of detail because it got so much attention at the time. I used that story more than the actual advisory language when I was framing the urgency internally.",
          "evidence_explanation": "Directly states the availability mechanism: memory of the vivid incident outweighed current advisory information in the risk-communication framing."
        }
      ],
      "correction_or_counterevidence": "The vendor's follow-up advisory two days later provided real-world exploitation evidence, but this arrived after the initial urgency framing had already been influenced by the remembered breach.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The provided corpus did not contain direct retrieved support for availability heuristic; the label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on participant self-report and retrospective reflection; interpretations may be reconstructive.",
    "The provided RAG corpus did not directly support the specific biases identified, so labels rely on widely established cognitive-science knowledge rather than retrieved corpus passages.",
    "Objective records such as the original vendor proposals, peer forum details, and incident logs were not available to independently verify decision impact."
  ]
}

