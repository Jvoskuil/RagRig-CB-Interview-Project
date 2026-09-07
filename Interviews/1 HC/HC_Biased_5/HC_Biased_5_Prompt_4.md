Prompt 4 - Revision Prompt
You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary interview about your clinical decision-making, it's being recorded for research purposes only, and you can skip anything you'd rather not discuss. Can you tell me a bit about your role?

Participant: Sure. I'm an outpatient physical therapist, mostly orthopedic caseload — a lot of post-surgical knees and shoulders. I've been doing this about nine years. Right now I see somewhere between eleven and fourteen patients a day.

Interviewer: I'd like to focus on one case that stands out to you — something nonroutine, where you had to make some real judgment calls. Can you walk me through it?

Participant: Yeah, there's one that's been on my mind. Adult patient, competitive amateur soccer player, hamstring autograft ACL reconstruction. She was highly motivated — wanted to be back for preseason, which gave us roughly a sixteen-week runway before her insurance authorization would expire. So there was a real clock running the whole time. Around week eight, we did a strength check — quad index came out to 78% of the uninvolved side. Threshold for moving into plyometric loading is usually cited around 80 to 85%, so she was close but technically under. No pain, no swelling, moving well. I actually had a case a couple years back — different patient entirely, similar timeline — who progressed into plyometrics early and re-tore her graft. That one stuck with me. So at that checkpoint, I held her at the current loading level rather than bumping her into closed-chain, modified plyo work, even though her numbers were close and she was symptom-free. I told her we'd reassess in two weeks.

Interviewer: What happened next?

Participant: The surgeon's clearance for advanced loading came through a few days later, no structural concerns noted. She was frustrated — she'd been comparing notes with a teammate who'd had a faster progression somewhere else. Then over the next couple weeks she had three really clean sessions of single-leg hopping — pain-free, form was improving each time, no swelling afterward. We had the isokinetic dynamometer booked for a hop-symmetry test that week, since it's only in clinic two days a week and slots go fast. But I remember thinking, three good sessions in a row is unusual for this stage — felt like we were due for something to give, so I pushed the test back a week rather than run it as scheduled.

Interviewer: And the week after?

Participant: Fourth session, also fine. No setback. But pushing the test back did eat into the authorization window a bit more than I'd have liked.

Interviewer: Let's go back to that first checkpoint, week eight. What information did you have in front of you at that moment?

Participant: The 78% index, no pain, no effusion, and clearance was pending but I fully expected it to come through. Objectively she was close to threshold and asymptomatic.

Interviewer: What alternatives did you weigh?

Participant: I could've progressed her into the modified plyo work right then, held her flat and reassessed in two weeks like I did, or split the difference with a reduced-intensity subset. I chose to hold.

Interviewer: What was the deciding factor?

Participant: Honestly, that prior patient's graft failure. I know it's a different case, different graft type technically, but it was vivid enough that it colored how I read this one. If I'm being fully honest, the current patient's actual numbers supported at least a partial progression.

Interviewer: How confident were you in that call at the time?

Participant: Moderately. I could have justified either choice on paper, but that memory tipped me toward the more conservative one.

Interviewer: Moving to the hop-test delay — what was your reasoning in the moment?

Participant: There was no clinical red flag — no fatigue report, no swelling, PROMs were stable. It was really just this sense that things had gone smoothly for long enough that a dip felt likely. In hindsight, each session doesn't really owe you anything based on what came before it.

Interviewer: Did time pressure factor into that decision?

Participant: A little, in the sense that delaying cost us a slot, but the reasoning driving it wasn't the schedule — it was that instinct about the streak.

Interviewer: Let's move to the third checkpoint. What was happening there?

Participant: Around week twelve, she'd hit about 85% of her interim milestones. Case manager wanted my recommendation — keep her in twice-weekly clinic visits or transition to a home program. Her numbers genuinely could've supported either path; it wasn't a clear-cut read.

Interviewer: How did you present the options?

Participant: I told the case manager and the patient that if we stopped clinic visits now, she'd risk losing the strength gains she'd built up. That's really the framing I led with. I didn't spend much time on the flip side — that a structured home program with check-ins could just as easily consolidate her progress and build her independence. Looking back, I leaned on the "you'll lose what you've gained" language more than the actual data probably warranted, and that's largely what drove the recommendation to keep her in clinic.

Interviewer: Did the patient respond to that?

Participant: She went along with it, but she mentioned afterward that the way I put it made her anxious about stopping, more than she felt the numbers alone would've justified.

Interviewer: Let's talk about discharge, around week sixteen. What did the picture look like then?

Participant: Strong. Hop symmetry index at 88%, quad index at 91%. Genuinely some of the best numbers I'd seen on my caseload that year. Surgeon wanted my recommendation on return-to-sport clearance.

Interviewer: What did you tell the patient?

Participant: I told her she was very likely to get back to competitive play injury-free — I said it pretty directly, based on how strong her numbers were compared to other patients I'd worked with.

Interviewer: What alternatives did you consider at that point?

Participant: Full clearance outright, clearance with a structured sport-specific reconditioning phase and closer monitoring, or delaying for another functional movement screen. I went with full clearance.

Interviewer: She asked you something specific at that point, right?

Participant: Yeah, she asked what her actual chances were of re-injuring it once she got back to playing. I answered in terms of her numbers — how strong her hop symmetry and quad index were relative to threshold. I didn't really bring in anything about how often athletes in general re-injure after this kind of surgery when they go back to cutting and pivoting sports. In hindsight, that's relevant information I have some familiarity with, and I didn't raise it.

Interviewer: What would have needed to be different for you to answer that differently?

Participant: If she'd asked more pointedly, "compared to other patients in general," I probably would've brought in more of that broader picture. But she asked about her chances, and I answered about her.

Interviewer: Looking back across the whole case, if insurance had allowed unlimited visits, would anything have changed?

Participant: Probably the pacing at that third checkpoint — less pressure to frame things one way or another, more room to just let the home program idea breathe.

Interviewer: If this had been a recreational walker instead of a competitive athlete, would your discharge conversation have gone differently?

Participant: Almost certainly softer, less urgency, and I think I'd have been more inclined to caveat the outcome rather than state it so plainly.

Interviewer: Any final reflection you'd offer a colleague facing a similar case?

Participant: Just to keep checking whether what's driving a call is the patient in front of you, or something you're carrying in from somewhere else — a past case, a good run of sessions, whatever it is. It's not always obvious in the moment which one it is.}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Risk Tolerance/aversion",
        "occurrences": 1,
        "mechanism_constraint": "Must be driven by an emotionally salient unrelated prior case rather than this patient's own objective data."
      },
      {
        "bias": "Loss/gain Framing effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a loss-framed presentation of the clinic-vs-home-program choice measurably tilting the recommendation under ambiguous data."
      },
      {
        "bias": "Gambler's Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must involve treating a short streak of good sessions as making a decline statistically 'due,' absent a fatigue indicator."
      },
      {
        "bias": "Base-Rate neglect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve omitting known population-level re-injury statistics when directly asked about risk, in favor of only individual data."
      },
      {
        "bias": "Optimism Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve overestimating this specific patient's favorable outcome based on personal comparative impression rather than test data alone."
      }
    ],
    "target_bias_names": [
      "Risk Tolerance/aversion",
      "Loss/gain Framing effect",
      "Gambler's Fallacy",
      "Base-Rate neglect",
      "Optimism Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Risk Tolerance/aversion", "requested_occurrences": 1},
      {"bias": "Loss/gain Framing effect", "requested_occurrences": 1},
      {"bias": "Gambler's Fallacy", "requested_occurrences": 1},
      {"bias": "Base-Rate neglect", "requested_occurrences": 1},
      {"bias": "Optimism Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Risk Tolerance/aversion"},
      {"instance_id": "cb_02", "bias": "Gambler's Fallacy"},
      {"instance_id": "cb_03", "bias": "Loss/gain Framing effect"},
      {"instance_id": "cb_04", "bias": "Optimism Bias"},
      {"instance_id": "cb_05", "bias": "Base-Rate neglect"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Risk Tolerance/aversion", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Gambler's Fallacy", "decision_point": 2},
      {"instance_id": "cb_03", "bias": "Loss/gain Framing effect", "decision_point": 3},
      {"instance_id": "cb_04", "bias": "Optimism Bias", "decision_point": 4},
      {"instance_id": "cb_05", "bias": "Base-Rate neglect", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Risk Tolerance/aversion",
        "mechanism": "Progression decision driven by an emotionally salient unrelated prior re-injury case rather than this patient's near-threshold strength index and pain-free status.",
        "affected_reasoning_operation": "Risk-weighting under uncertainty for a progression decision",
        "evidence_source": "PT's own retrospective account citing the unrelated prior patient as primary justification",
        "distinctiveness_requirement": "Only instance tied to progression timing at decision point 1; sourced from a recalled unrelated case, not from streak reasoning or framing."
      },
      {
        "instance_id": "cb_02",
        "bias": "Gambler's Fallacy",
        "mechanism": "Interpreting three consecutive pain-free sessions as making a decline 'due' soon, absent any fatigue indicator, and delaying testing on that basis.",
        "affected_reasoning_operation": "Short-run outcome prediction from a streak of session results",
        "evidence_source": "PT's stated reasoning for delaying the scheduled hop test at decision point 2",
        "distinctiveness_requirement": "Only instance involving streak-based reversion reasoning; distinct from cb_01 (recalled case) and cb_04 (personal comparative ranking)."
      },
      {
        "instance_id": "cb_03",
        "bias": "Loss/gain Framing effect",
        "mechanism": "Recommendation to continue clinic visits is driven by loss-framed language ('losing gains') rather than a balanced read of ambiguous functional data.",
        "affected_reasoning_operation": "Recommendation formulation under an ambiguous decision boundary",
        "evidence_source": "PT's account of how she framed the clinic-vs-home-program choice to the case manager and patient at decision point 3",
        "distinctiveness_requirement": "Only instance concerning framing of a recommendation; independent of streak or comparative-ranking evidence."
      },
      {
        "instance_id": "cb_04",
        "bias": "Optimism Bias",
        "mechanism": "Overestimating this specific patient's chance of injury-free return based on her scores being 'among the best' the PT has personally seen, rather than calibrated probability.",
        "affected_reasoning_operation": "Individual outcome prediction from personal comparative impression",
        "evidence_source": "PT's direct statement of confidence to the patient at decision point 4, anchored on personal caseload comparison",
        "distinctiveness_requirement": "Concerns individual-level probability estimate; distinct from cb_05, which concerns omission of population statistics."
      },
      {
        "instance_id": "cb_05",
        "bias": "Base-Rate neglect",
        "mechanism": "Omitting known population-level ACL re-injury incidence statistics when the patient directly asks about re-injury risk, relying solely on individual test thresholds.",
        "affected_reasoning_operation": "Risk disclosure integrating population data with individual clearance decision",
        "evidence_source": "PT's answer to the patient's direct question about re-injury chances at decision point 4",
        "distinctiveness_requirement": "Concerns omission of population-level statistical information; distinct from cb_04's individual-impression-based optimism, occurring in response to a different probe (patient's direct question) within the same decision point."
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Risk Tolerance/aversion", "strength": "subtle"},
      {"instance_id": "cb_02", "bias": "Gambler's Fallacy", "strength": "subtle"},
      {"instance_id": "cb_03", "bias": "Loss/gain Framing effect", "strength": "moderate"},
      {"instance_id": "cb_04", "bias": "Optimism Bias", "strength": "subtle"},
      {"instance_id": "cb_05", "bias": "Base-Rate neglect", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Biased_5",
    "domain_id": "HC",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across distinct decision points where mechanism fit allowed (DP1-DP3 one bias each); DP4 received two biases (Optimism Bias and Base-Rate neglect) because both mechanistically belong to the discharge/clearance moment, but each was anchored to a different evidence source (personal comparative impression vs. omitted population statistics) and a different probe (spontaneous statement vs. direct patient question), satisfying the distinct-evidence-source requirement for co-located instances.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "HC_Biased_5",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Outpatient orthopedic physical therapy and post-operative ACL rehabilitation",
    "role": "Outpatient physical therapist managing return-to-sport progression after hamstring-autograft ACL reconstruction",
    "objective": "Make progression, visit-frequency, and return-to-sport recommendations while balancing functional test results, patient goals, insurance constraints, and re-injury risk",
    "incident_type": "A time-constrained ACL rehabilitation case involving four linked clinical decision checkpoints",
    "confidence": 0.99
  },
  "structure_audit": {
    "estimated_word_count": 1215,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "At week eight, the therapist decides whether to progress a near-threshold, asymptomatic patient into modified plyometric loading.",
        "evidence_before": [
          "Quad index of 78% of the uninvolved side",
          "Typical progression threshold cited as 80% to 85%",
          "No pain, swelling, or movement concerns",
          "Surgeon clearance was pending but expected",
          "A vivid prior case involved a different patient who progressed early and re-tore a graft"
        ],
        "evidence_after": [
          "The patient remains at the existing loading level",
          "Reassessment is scheduled for two weeks later",
          "Surgeon clearance subsequently arrives without structural concerns"
        ],
        "goals_constraints": [
          "Return for competitive soccer preseason",
          "Approximately sixteen-week insurance authorization window",
          "Need to manage graft and reinjury risk"
        ],
        "alternatives": [
          "Progress immediately into modified plyometric work",
          "Hold current loading and reassess",
          "Use a reduced-intensity subset of plyometric work"
        ],
        "decision_basis": "The therapist explicitly states that the emotionally vivid prior graft failure colored interpretation of the current patient's near-threshold but favorable objective presentation.",
        "time_pressure": "The impending insurance authorization expiration creates a meaningful but non-determinative schedule constraint.",
        "uncertainty": "The patient is below the stated numeric threshold but close to it and clinically asymptomatic; either a partial progression or a hold could be justified."
      },
      {
        "id": 2,
        "summary": "After three pain-free, improving single-leg hopping sessions, the therapist delays a scheduled hop-symmetry test.",
        "evidence_before": [
          "Three clean sessions with improving form",
          "No pain, swelling, fatigue report, or PROM deterioration",
          "The dynamometer test is scheduled during a limited clinic availability window"
        ],
        "evidence_after": [
          "The hop test is delayed by one week",
          "A fourth session is also uneventful",
          "The delay consumes additional authorization time"
        ],
        "goals_constraints": [
          "Assess hop symmetry",
          "Use a scarce testing slot",
          "Avoid premature testing or an anticipated setback"
        ],
        "alternatives": [
          "Run the hop-symmetry test as scheduled",
          "Delay the test by one week"
        ],
        "decision_basis": "The therapist states that an unusually smooth short run made a decline feel statistically due, despite no clinical fatigue or deterioration indicator.",
        "time_pressure": "The delayed test risks loss of a scarce testing slot and further compresses the authorization window.",
        "uncertainty": "There is no identified clinical indicator of imminent decline; the prediction is based on the streak itself."
      },
      {
        "id": 3,
        "summary": "Around week twelve, the therapist recommends either continuing twice-weekly clinic visits or transitioning to a structured home program.",
        "evidence_before": [
          "The patient has reached approximately 85% of interim milestones",
          "Functional numbers could support either continued clinic care or home programming",
          "The case manager requests a recommendation",
          "Insurance authorization remains limited"
        ],
        "evidence_after": [
          "The therapist recommends continuing clinic visits",
          "The patient agrees but reports anxiety induced by the presentation of the choice"
        ],
        "goals_constraints": [
          "Maintain gains and support return-to-sport preparation",
          "Build patient independence",
          "Use limited authorized visits appropriately"
        ],
        "alternatives": [
          "Continue twice-weekly clinic visits",
          "Transition to a structured home program with check-ins"
        ],
        "decision_basis": "The therapist leads with the prospect of losing gains and gives limited attention to the potentially equivalent benefits of a structured home program under ambiguous data.",
        "time_pressure": "The authorization window influences the context, although the therapist reports that framing rather than scheduling primarily drove the recommendation.",
        "uncertainty": "Neither option is clearly superior on the functional evidence available."
      },
      {
        "id": 4,
        "summary": "At discharge around week sixteen, the therapist recommends full return-to-sport clearance and answers the patient's direct question about reinjury risk.",
        "evidence_before": [
          "Hop symmetry index of 88%",
          "Quad index of 91%",
          "The therapist regards these as among the strongest results in the therapist's caseload that year",
          "Return-to-sport in soccer entails cutting and pivoting demands",
          "The therapist reports familiarity with broader ACL reinjury information"
        ],
        "evidence_after": [
          "The therapist recommends full clearance rather than monitored phased clearance or additional testing",
          "The therapist tells the patient she is very likely to return to competitive play injury-free",
          "The patient receives an individualized metric-based answer rather than an answer integrating broader reinjury incidence"
        ],
        "goals_constraints": [
          "Provide a clinically appropriate clearance recommendation",
          "Communicate reinjury risk accurately",
          "Balance strong functional test performance against sport-specific reinjury exposure"
        ],
        "alternatives": [
          "Full clearance",
          "Clearance with sport-specific reconditioning and closer monitoring",
          "Delay clearance for another functional movement screen",
          "Provide an individualized risk explanation integrated with population-level reinjury information"
        ],
        "decision_basis": "Full clearance and a highly favorable prognosis are grounded in strong metrics and personal caseload comparison; when directly asked about reinjury probability, the therapist uses only individualized metrics and omits known broader incidence information.",
        "time_pressure": "The patient is approaching preseason and the end of the authorization window, although neither is presented as the direct basis for the risk answer.",
        "uncertainty": "Strong test scores do not by themselves establish a calibrated probability of injury-free competitive return."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "cb_01",
      "bias": "Risk Tolerance/aversion",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "I actually had a case a couple years back — different patient entirely, similar timeline — who progressed into plyometrics early and re-tore her graft. That one stuck with me... I know it's a different case, different graft type technically, but it was vivid enough that it colored how I read this one.",
      "evidence_location": "Week-eight progression discussion; participant's explanation of the deciding factor after alternatives are elicited",
      "mechanism": "The therapist gives disproportionate risk weight to a vivid, unrelated adverse prior case and chooses the more conservative progression option despite acknowledging that the present patient's objective data supported at least partial progression.",
      "strength": "moderate",
      "confidence": 0.93,
      "plausible_nonbias_explanation": "A therapist may reasonably become more cautious after observing graft failure, especially near a published progression threshold. However, the participant explicitly distinguishes the prior case from the current patient and states that the memory, rather than the current evidence, tipped the decision.",
      "additional_evidence_needed": "None for occurrence validation. A clearer statement that the prior event felt more probable than objective data indicated would strengthen the risk-aversion characterization, but is not necessary.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, participant answers describing the prior graft failure and the deciding factor",
        "current_defect": "None material; the episode has a distinct decision, an identified evidence-weighting distortion, and an adequate non-bias contrast.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The 78% quad index",
          "Absence of pain and swelling",
          "The distinct unrelated prior graft-failure memory",
          "The acknowledgement that partial progression was supportable"
        ],
        "avoid_creating": [
          "A second unrelated-case episode elsewhere",
          "A shift into unsupported causal claims that early progression itself caused the prior graft failure"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_02",
      "bias": "Gambler's Fallacy",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 2,
      "supporting_quote": "Three good sessions in a row is unusual for this stage — felt like we were due for something to give, so I pushed the test back a week rather than run it as scheduled... In hindsight, each session doesn't really owe you anything based on what came before it.",
      "evidence_location": "Hop-test delay discussion and retrospective explanation of the therapist's reasoning",
      "mechanism": "The therapist treats a short sequence of favorable, independent session outcomes as making an unfavorable reversal due, then changes the testing decision on that basis despite the absence of fatigue, swelling, pain, or deteriorating patient-reported outcomes.",
      "strength": "strong",
      "confidence": 0.98,
      "plausible_nonbias_explanation": "Delaying a test can be prudent if clinical fatigue, instability, pain, poor form, or recovery concerns are present. The interview explicitly rules out those indicators and attributes the delay to the streak-based expectation.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 2, participant's explanation for postponing the scheduled hop test",
        "current_defect": "None; the reasoning mechanism and the absence of an alternative clinical trigger are explicit.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "Three clean sessions",
          "The lack of fatigue and other red flags",
          "The delayed testing decision",
          "The participant's corrective retrospective reflection"
        ],
        "avoid_creating": [
          "A separate availability-based explanation for the delay",
          "A legitimate medical justification that would undermine the streak-based mechanism"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_03",
      "bias": "Loss/gain Framing effect",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "If we stopped clinic visits now, she'd risk losing the strength gains she'd built up. That's really the framing I led with. I didn't spend much time on the flip side... I leaned on the 'you'll lose what you've gained' language more than the actual data probably warranted, and that's largely what drove the recommendation to keep her in clinic.",
      "evidence_location": "Week-twelve clinic-versus-home-program recommendation discussion",
      "mechanism": "Under explicitly ambiguous functional evidence, the therapist presents the choice predominantly as avoiding loss rather than as an equivalent choice that could produce gains in independence and consolidation; the therapist reports that this framing materially tilted the recommendation.",
      "strength": "strong",
      "confidence": 0.97,
      "plausible_nonbias_explanation": "Continued supervised rehabilitation can be clinically appropriate. The bias evidence rests not on the recommendation itself but on the acknowledged asymmetric presentation and the admission that it drove the recommendation more than the underlying data warranted.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, participant's account of presenting the clinic-versus-home-program options",
        "current_defect": "None; the interview directly establishes both asymmetric framing and decision influence.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "Ambiguity of the functional data",
          "The loss-oriented wording",
          "The viable structured-home-program alternative",
          "The patient's reported anxiety response"
        ],
        "avoid_creating": [
          "A false claim that the patient had no meaningful choice",
          "An additional unrelated bias mechanism in the visit-frequency decision"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_04",
      "bias": "Optimism Bias",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 4,
      "supporting_quote": "I told her she was very likely to get back to competitive play injury-free... based on how strong her numbers were compared to other patients I'd worked with.",
      "evidence_location": "Discharge and full-clearance recommendation discussion",
      "mechanism": "The intended mechanism is an overconfident favorable prediction for this patient based on personal comparative impression. The text supports a highly favorable prediction and use of personal caseload comparison, but it does not independently establish that the prediction is overestimated, poorly calibrated, or insufficiently supported by the unusually strong objective scores.",
      "strength": "weak",
      "confidence": 0.76,
      "plausible_nonbias_explanation": "An 88% hop symmetry index and 91% quad index, combined with otherwise strong recovery, may reasonably support a favorable individualized prognosis. Personal clinical comparison can be relevant experiential evidence rather than optimism bias.",
      "additional_evidence_needed": "A subtle cue showing that the therapist converts a favorable comparative impression into a stronger probability claim than the evidence warrants, such as acknowledging that the scores do not predict injury-free play with that level of certainty or that the therapist discounted a relevant residual risk factor.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_reasoning_revision",
        "location": "Decision point 4, immediately after the participant explains saying the patient was very likely to return injury-free",
        "current_defect": "The transcript establishes confidence but not the unjustified overestimation required for optimism bias. Strong test scores and personal experience can support a favorable prognosis.",
        "minimal_change_instruction": "Add one brief participant statement that the personal 'best numbers' impression led her to treat injury-free return as more certain than she could actually justify from those scores, while retaining that the scores were objectively strong. For example, have her note that she translated 'better than most patients I have seen' into 'very likely injury-free' even though those measures did not warrant that certainty for cutting sport.",
        "preserve": [
          "The 88% hop symmetry index",
          "The 91% quad index",
          "The full-clearance choice",
          "The distinction between the favorable-prognosis statement and the later base-rate omission",
          "The participant's personal caseload comparison"
        ],
        "avoid_creating": [
          "A second base-rate-neglect instance in the spontaneous clearance statement",
          "A new hindsight-only explanation without contemporaneous reasoning",
          "A claim that strong functional scores have no clinical relevance"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_05",
      "bias": "Base-Rate neglect",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 4,
      "supporting_quote": "She asked what her actual chances were of re-injuring it once she got back to playing. I answered in terms of her numbers... I didn't really bring in anything about how often athletes in general re-injure after this kind of surgery... In hindsight, that's relevant information I have some familiarity with, and I didn't raise it.",
      "evidence_location": "Discharge discussion; response to the patient's direct question about chance of reinjury",
      "mechanism": "When asked directly for an actual reinjury-risk estimate, the therapist selects only individualized threshold and test information while omitting known, relevant population-level reinjury incidence information that should inform a calibrated risk disclosure.",
      "strength": "moderate",
      "confidence": 0.92,
      "plausible_nonbias_explanation": "An individualized risk question appropriately calls for patient-specific data, and population rates cannot by themselves determine an individual's risk. The omission is bias-relevant because the therapist acknowledges knowing that broader data were relevant yet provides only the individualized favorable indicators.",
      "additional_evidence_needed": "None for a moderate supported occurrence. Actual numerical base-rate data are unnecessary; the therapist's reported familiarity with relevant population information and omission in response to the direct probability question are sufficient.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 4, participant's account of answering the patient's direct reinjury-risk question",
        "current_defect": "None material; this is distinct from the optimism episode because it concerns evidence omission during risk disclosure rather than the basis for the initial favorable prognosis.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The patient's direct request for actual reinjury chances",
          "The therapist's metric-only answer",
          "The therapist's stated familiarity with relevant population information",
          "The separate probe and evidence trace from cb_04"
        ],
        "avoid_creating": [
          "A numerical population statistic that is unsupported or falsely precise",
          "A second, separate population-information omission at another decision point"
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Risk Tolerance/aversion",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Loss/gain Framing effect",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Gambler's Fallacy",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Base-Rate neglect",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Optimism Bias",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "Availability heuristic",
      "decision_point": 1,
      "supporting_quote": "That one stuck with me... it was vivid enough that it colored how I read this one.",
      "mechanism": "A memorable prior graft failure becomes disproportionately influential in judging the current patient's progression risk.",
      "confidence": 0.86,
      "status": "candidate",
      "plausible_nonbias_explanation": "The same evidence trace is already necessary to support the requested risk-aversion occurrence. It is best treated as the cognitive route through the intended risk-weighting distortion, not counted as a separate accidental occurrence.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Overconfidence",
      "decision_point": 4,
      "supporting_quote": "I told her she was very likely to get back to competitive play injury-free.",
      "mechanism": "The therapist states a strong confidence claim about an uncertain patient-specific athletic outcome.",
      "confidence": 0.66,
      "status": "weak",
      "plausible_nonbias_explanation": "The patient has strong functional indices and a favorable clinical presentation; the text does not show a calibration benchmark or demonstrate that the expressed confidence exceeded what the evidence supported.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "The patient has a competitive preseason goal and a sixteen-week insurance authorization window.",
      "location": "Initial case description and later reflections",
      "why_not_bias": "These are real organizational and motivational constraints. Time pressure may shape choices without itself showing distorted information processing."
    },
    {
      "cue": "The surgeon's advanced-loading clearance arrives with no structural concerns.",
      "location": "Following decision point 1",
      "why_not_bias": "This is relevant clinical information and does not itself establish that the earlier hold was irrational or biased."
    },
    {
      "cue": "The therapist delays testing and subsequently observes another uneventful session.",
      "location": "Decision point 2 outcome",
      "why_not_bias": "The unfavorable practical consequence of delay does not prove bias. The supported bias rests on the contemporaneous streak-based reasoning, not on the fact that no setback occurred."
    },
    {
      "cue": "The patient compares her progression to a teammate's progression elsewhere.",
      "location": "Between decision points 1 and 2",
      "why_not_bias": "Peer comparison can create frustration but does not show that the therapist adopted an anchoring, conformity, or comparison-based bias."
    },
    {
      "cue": "The therapist uses thresholds and functional scores in clearance reasoning.",
      "location": "Decision points 1 and 4",
      "why_not_bias": "Use of quantitative clinical criteria is generally appropriate. The audit concerns disproportionate reliance, omission of relevant information, or unsupported certainty, not score use itself."
    },
    {
      "cue": "The therapist reflects differently on an unlimited-insurance counterfactual and a recreational-walker hypothetical.",
      "location": "Closing reflections",
      "why_not_bias": "These are explicit hypothetical reflections about constraints and patient goals. They do not supply evidence of a distinct cognitive bias in the original decisions."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "The vivid prior graft-failure case tipped the therapist toward holding progression.",
        "evidence": "The therapist explicitly identifies the prior case as the deciding factor and says it colored interpretation of the present case.",
        "assessment": "Moderately supported self-reported causal attribution; it identifies a decision mechanism but cannot establish the objective appropriateness of the alternative progression."
      },
      {
        "claim": "Loss-framed language largely drove the recommendation to continue clinic visits.",
        "evidence": "The therapist states that the loss-oriented framing, more than the data, drove the recommendation; the patient also reports increased anxiety after hearing it.",
        "assessment": "Moderately supported for the therapist's recommendation through self-report. The evidence does not establish that framing alone caused the patient's agreement because insurance, trust, and clinical context remain possible contributors."
      },
      {
        "claim": "Delaying the test ate into the authorization window.",
        "evidence": "The therapist directly reports that the one-week postponement consumed additional time in the limited authorization period.",
        "assessment": "Strong operational causal link within the narrated schedule, though no quantitative consequence is specified."
      }
    ],
    "correlation_causation_risks": [
      {
        "risk": "The earlier prior patient's re-tear may be implicitly associated with early progression, but the transcript does not establish that early plyometric progression caused that failure.",
        "mitigation": "Treat the prior outcome only as a salient memory influencing the current therapist's risk weighting, not as evidence about clinical causality."
      },
      {
        "risk": "Strong hop and quadriceps indices are associated with favorable function but do not alone prove an injury-free return-to-sport outcome.",
        "mitigation": "Do not infer that full clearance or the favorable prediction was objectively wrong solely from missing population-risk information."
      }
    ],
    "counterfactual_present": true,
    "changed_variable": "Insurance authorization availability is hypothetically changed from a limited sixteen-week window to unlimited visits.",
    "held_constant": [
      "The patient and rehabilitation progress are implicitly held constant",
      "The third decision point remains clinic care versus home programming"
    ],
    "causal_coherence": "moderate",
    "explanation": "The insurance counterfactual is coherent as a reflective probe about whether authorization pressure influenced visit-frequency framing. It is not a formal paired-scenario counterfactual in the hidden specification, and it changes only a stated constraint rather than testing the causal mechanisms of the target biases. The recreational-walker hypothetical is a separate case-type change and should not be used as causal evidence about the original case."
  },
  "quality_scores": {
    "occupational_realism": 87,
    "cta_fidelity": 91,
    "bias_separability": 88,
    "bias_subtlety": 84,
    "control_fidelity": 100,
    "counterfactual_fidelity": 82,
    "narrative_coherence": 91,
    "naturalness": 85,
    "hidden_label_integrity": 94,
    "overall_quality": 87
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 4,
    "requested_occurrence_total": 5,
    "missing_occurrence_total": 1,
    "accidental_occurrence_total": 0,
    "priority": "low",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Retain the four-decision-point chronology and the outpatient ACL-rehabilitation setting.",
      "Do not add additional target-bias episodes or alter the already distinct evidence traces for risk aversion, gambler's fallacy, framing, and base-rate neglect.",
      "Repair only the discharge prognosis language so it establishes unwarranted confidence rather than merely a clinically plausible favorable judgment.",
      "Keep optimism bias distinct from base-rate neglect: the former must concern overconfident interpretation of favorable patient-specific evidence, while the latter remains the omission of relevant population-level information when answering the direct risk question.",
      "Do not turn retrospective reflection into a textbook label or an explicit bias diagnosis."
    ],
    "revision_order": [
      {
        "instance_id": "cb_04",
        "action": "Add one subtle local statement showing that the therapist's personal comparative impression inflated the certainty of the injury-free prediction beyond what the otherwise strong test results could support."
      }
    ]
  },
  "failure_flags": [
    {
      "flag": "OPTIMISM_MECHANISM_UNDERDETERMINED",
      "severity": "medium",
      "description": "The intended optimism-bias instance contains confidence and favorable comparison but lacks evidence that the confidence was unjustifiably elevated rather than a reasonable conclusion from strong functional data."
    }
  ]
}}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
