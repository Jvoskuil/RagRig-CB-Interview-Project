You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary interview about your clinical decision-making, it's being recorded for research purposes only, and you can skip anything you'd rather not discuss. Can you tell me a bit about your role?

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

Participant: I told her she was very likely to get back to competitive play injury-free — I said it pretty directly, based on how strong her numbers were compared to other patients I'd worked with. Looking back, I think I took "better than most patients I've seen" and turned it into "very likely injury-free" more firmly than those two scores alone could really back up for someone returning to a cutting-and-pivoting sport.

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

Participant: Just to keep checking whether what's driving a call is the patient in front of you, or something you're carrying in from somewhere else — a past case, a good run of sessions, whatever it is. It's not always obvious in the moment which one it is.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HC_Biased_5",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Physical Therapist with outpatients",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The ACL Return-to-Sport Progression",
    "scenario_summary_internal": "An outpatient orthopedic physical therapist manages a 16-week post-ACL-reconstruction rehab course for a competitive amateur soccer player. Across four checkpoints—early plyometric progression, mid-course hop testing, transition-to-home planning, and discharge/return-to-sport clearance—the PT must weigh objective functional metrics (quadriceps strength index, hop-test symmetry, PROMs) against insurance visit limits, patient eagerness, and clinic productivity pressure. The narrative embeds five distinct reasoning distortions without naming them, each tied to a specific inference the PT makes from available clinical data.",
    "occupational_realism": {
      "objective": "Safely progress a post-surgical outpatient toward objective return-to-sport criteria within a limited insurance-authorized visit window, minimizing re-injury risk while meeting clinic productivity expectations.",
      "setting": "Outpatient orthopedic physical therapy clinic; primary patient is an amateur adult soccer player 8-16 weeks post-ACL reconstruction (hamstring autograft).",
      "constraints": [
        "Insurance authorization capped at a fixed number of visits with a hard expiration date",
        "Isokinetic dynamometer shared across the clinic and only available two days a week",
        "Clinic productivity targets requiring efficient visit throughput",
        "Patient's strong motivation to return to competitive play before season start",
        "Referring orthopedic surgeon requires periodic progress updates before sign-off"
      ],
      "stakeholders": [
        "Patient (adult recreational/competitive soccer player)",
        "Referring orthopedic surgeon",
        "Insurance case manager",
        "Clinic supervisor",
        "Treating physical therapist (interviewee)"
      ],
      "technical_terms_to_use": [
        "quadriceps strength index",
        "single-leg hop test symmetry index",
        "isokinetic dynamometer",
        "return-to-sport criteria",
        "plyometric progression",
        "closed-chain vs open-chain exercise",
        "graft maturation timeline",
        "patient-reported outcome measures (PROMs)",
        "functional movement screen",
        "insurance authorization window"
      ],
      "technical_terms_to_avoid": [
        "loss aversion",
        "framing effect",
        "gambler's fallacy",
        "base rate",
        "optimism bias",
        "risk tolerance",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Quadriceps strength index at 78% of uninvolved limb (typical progression threshold cited as 80-85%)",
          "No reported pain or effusion",
          "Physician clearance for advanced loading still pending written confirmation",
          "PT recalls a prior unrelated patient who re-tore a graft after early plyometric progression two years earlier"
        ],
        "new_information_after_decision": [
          "Physician clearance arrives days later confirming no structural concerns",
          "Patient reports frustration at perceived slow pace relative to peers"
        ],
        "alternatives": [
          "Progress to modified closed-chain/plyometric loading now given absence of pain and near-threshold strength",
          "Hold at current loading level and reassess strength index in two weeks",
          "Progress partially with a reduced-intensity plyometric subset while monitoring"
        ],
        "intended_action": "PT elects to hold progression well beyond what the 78% index and pain-free status would typically justify, citing the earlier unrelated case as the primary reason rather than this patient's actual data."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient has completed three consecutive sessions of pain-free single-leg hopping drills with steadily improving form",
          "No fatigue, swelling, or PROM decline reported",
          "Isokinetic dynamometer is available this week for a scheduled hop-symmetry test"
        ],
        "new_information_after_decision": [
          "Test is delayed a week; patient's fourth session also goes well with no setback",
          "Delayed testing shortens the remaining window before insurance authorization expires"
        ],
        "alternatives": [
          "Proceed with the scheduled single-leg hop test this week as planned",
          "Delay testing one additional week, reasoning the streak of good sessions makes a setback likely soon",
          "Run a modified, lower-load version of the test to hedge against an anticipated decline"
        ],
        "intended_action": "PT postpones the scheduled hop test, reasoning aloud that because the patient has had an unusually good run of sessions, a decline is 'due,' despite no clinical indicator of fatigue or regression."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient has met roughly 85% of interim functional milestones and reports strong confidence",
          "Insurance case manager requests a recommendation: continue supervised clinic visits or transition to a home exercise program",
          "Objective measures (PROMs, strength index) are within a range that could reasonably support either path"
        ],
        "new_information_after_decision": [
          "Case manager approves the PT's recommended path without further review",
          "Patient later expresses some anxiety about the framing used to justify continued in-clinic visits"
        ],
        "alternatives": [
          "Recommend transition to a structured home exercise program with periodic check-ins",
          "Recommend continued twice-weekly supervised clinic visits",
          "Recommend a tapered hybrid schedule reducing clinic frequency gradually"
        ],
        "intended_action": "PT frames the choice to the case manager and patient primarily around what would be lost by stopping clinic visits ('you'll lose the strength gains you've made') rather than presenting the equally valid gains of independence, and recommends continued clinic visits largely on that framing rather than a balanced read of the functional data."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Single-leg hop symmetry index reaches 88%, near the higher end of the typical return-to-sport threshold",
          "Quadriceps strength index at 91%",
          "PT recalls that this patient's numbers are among the best she has seen in her caseload this year",
          "Surgeon requests a discharge/return-to-sport recommendation"
        ],
        "new_information_after_decision": [
          "PT drafts the clearance summary and discusses expected outcome with the patient and surgeon",
          "Patient asks directly about the chance of re-injury upon returning to competitive play"
        ],
        "alternatives": [
          "Clear the patient for full return to competitive soccer based on her individual test scores",
          "Clear with a structured, sport-specific reconditioning phase and reinforced monitoring given known population-level re-injury patterns after ACL reconstruction",
          "Delay clearance pending an additional functional movement screen"
        ],
        "intended_action": "PT tells the patient she is very likely to return to play injury-free given how strong her individual numbers are, without incorporating the well-documented population-level second-injury incidence for athletes returning to pivoting sports after ACL reconstruction, and finalizes an unqualified clearance recommendation."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe your role and typical caseload in this clinic?",
        "Walk me through this particular patient's case from referral to discharge."
      ],
      "timeline_reconstruction": [
        "Take me through the treatment course week by week.",
        "What information did you have available at each check-in point?",
        "What changed in the patient's presentation between phases?"
      ],
      "decision_point_probes": [
        "What cues in the patient's presentation stood out to you at that point?",
        "What information sources did you rely on for that decision?",
        "What were you ultimately trying to achieve at that stage?",
        "What other options did you consider, and why did you rule them out?",
        "What was the main basis for the choice you made?",
        "Had you seen a similar situation before, and did that affect your thinking?",
        "How much time pressure were you under when making that call?",
        "How confident were you in the data you had at that point?",
        "If a key fact had been different, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If insurance had allowed unlimited visits, would your approach have changed?",
        "If this had been a different sport or activity level, how might your recommendation differ?",
        "If you had earlier access to the isokinetic dynamometer, would that have changed your timeline?",
        "Looking back, what would you tell a colleague facing the same case?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Risk Tolerance/aversion",
        "decision_point": 1,
        "mechanism": "PT's progression decision is driven by an emotionally salient unrelated prior case rather than this patient's objective near-threshold strength index and absence of pain, producing a level of caution disproportionate to the actual clinical risk indicated by the data.",
        "affected_reasoning_operation": "Risk-weighting of a progression decision under uncertainty",
        "evidence_available_at_time": [
          "78% quadriceps strength index, near typical progression threshold",
          "No pain or effusion",
          "Pending but expected physician clearance"
        ],
        "required_textual_manifestation": "PT explicitly cites the unrelated prior patient's re-injury as the reason for holding progression, more than the current patient's own metrics.",
        "plausible_nonbias_interpretation": "A cautious clinician conservatively erring on the side of safety near a threshold value, which alone would be a defensible clinical judgment call rather than a distortion.",
        "strength": "subtle",
        "do_not_make_explicit": ["risk aversion", "risk tolerance", "bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Gambler's Fallacy",
        "decision_point": 2,
        "mechanism": "PT infers that a consecutive run of pain-free, well-performed sessions makes a decline 'due' or statistically likely soon, treating session-to-session outcomes as if they must balance out rather than depending on the patient's actual physiological trajectory.",
        "affected_reasoning_operation": "Prediction of near-term outcome from a short streak of independent-ish observations",
        "evidence_available_at_time": [
          "Three consecutive pain-free, improving hopping sessions",
          "No fatigue, swelling, or PROM decline reported"
        ],
        "required_textual_manifestation": "PT states or implies that the good streak means a setback is 'due' and delays testing on that basis, absent any clinical fatigue indicator.",
        "plausible_nonbias_interpretation": "A prudent clinician spacing out demanding tests to avoid overuse, which would be a legitimate load-management rationale rather than a distortion.",
        "strength": "subtle",
        "do_not_make_explicit": ["gambler's fallacy", "streak", "due for"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Loss/gain Framing effect",
        "decision_point": 3,
        "mechanism": "PT's recommendation to the case manager and patient is shaped by presenting the choice in terms of what will be lost by stopping clinic visits, rather than an equally valid gain-framed or neutral presentation, and this framing measurably tilts the recommendation despite ambiguous supporting data.",
        "affected_reasoning_operation": "Formulation and communication of a recommendation under an ambiguous decision boundary",
        "evidence_available_at_time": [
          "~85% of interim functional milestones met",
          "PROMs and strength index within a range compatible with either path"
        ],
        "required_textual_manifestation": "PT's own account shows she emphasized 'losing gains' language when recommending continued clinic visits, and this framing—not the ambiguous data—is what she cites as driving the recommendation.",
        "plausible_nonbias_interpretation": "A clinician using motivational language to support adherence, which could be a legitimate communication technique rather than a distortion of the underlying decision.",
        "strength": "moderate",
        "do_not_make_explicit": ["framing effect", "loss frame", "gain frame"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Optimism Bias",
        "decision_point": 4,
        "mechanism": "PT projects a high personal likelihood of injury-free return specifically for this patient based on her individual test scores being 'among the best' she has seen, overestimating this particular patient's favorable outcome beyond what the test scores alone support.",
        "affected_reasoning_operation": "Individual outcome prediction from personal comparative impression",
        "evidence_available_at_time": [
          "88% hop symmetry index, 91% strength index",
          "PT's subjective ranking of this patient against her own caseload"
        ],
        "required_textual_manifestation": "PT tells the patient she is 'very likely' to return injury-free, anchoring the confidence explicitly on how her numbers compare favorably to other patients the PT has personally treated.",
        "plausible_nonbias_interpretation": "A clinician reasonably encouraged by strong objective test results, which alone would be a defensible read of good data.",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "overconfident", "unrealistically"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Base-Rate neglect",
        "decision_point": 4,
        "mechanism": "In finalizing the clearance recommendation, PT relies solely on this patient's individual test thresholds and omits any consideration of the well-documented population-level second-injury incidence for athletes returning to pivoting sports after ACL reconstruction, even when directly asked about re-injury risk.",
        "affected_reasoning_operation": "Risk disclosure and clearance decision integrating population statistics with individual data",
        "evidence_available_at_time": [
          "Patient's individual thresholds met (88% hop symmetry, 91% strength index)",
          "General clinical knowledge of published re-injury incidence for return-to-pivoting-sport ACL populations"
        ],
        "required_textual_manifestation": "When the patient asks about re-injury chances, the PT's answer references only the patient's own numbers and omits any acknowledgment of general population re-injury statistics for this type of return-to-sport case.",
        "plausible_nonbias_interpretation": "A clinician tailoring counseling to the individual patient rather than reciting population statistics, which could be reasonable patient-centered communication rather than neglect of relevant information.",
        "strength": "moderate",
        "do_not_make_explicit": ["base rate", "base-rate neglect", "population statistics"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for this biased-condition scenario; no paired control is being generated under this specification."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly 5 intended bias instances are planned, one each for the five manifest entries.",
      "Confirm exactly 4 decision points exist, with decision point 4 carrying two distinct biases (Optimism Bias and Base-Rate neglect) via clearly separate evidence sources.",
      "Confirm no bias name, definition, or psychological label appears in probe or timeline text intended for the public interview.",
      "Confirm each decision point offers at least two plausible alternatives with pre- and post-decision information.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm consequences described (e.g., clearance, case manager approval) do not mechanically prove bias presence.",
      "Confirm total narrative content can be written within 1,215-1,485 words without repetitive exposition, using four moderately detailed decision-point narrations plus probe responses."
    ]
  },
  "hidden_validation_specification": {
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
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "clinical assessment and progression context",
        "raw_interview_anchor": "Week eight: 78% quadriceps index, near threshold; no pain or swelling; authorization clock running.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Current data and constraints without a hidden distortion."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "progression decision rationale",
        "raw_interview_anchor": "An unrelated graft re-tear was vivid enough to color this case, so progression was held despite near-threshold, symptom-free data.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "A salient prior case displaced current objective evidence."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "progress monitoring and test scheduling context",
        "raw_interview_anchor": "Three clean hopping sessions occurred and a dynamometer test was scheduled while slots were scarce.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Favorable observations and resource availability without bias."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "test-delay prediction and scheduling decision",
        "raw_interview_anchor": "Three good sessions felt due for something to give, so the scheduled test was delayed despite no red flag.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "A short run of good outcomes was treated as making a setback due."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "resource-window consequence",
        "raw_interview_anchor": "The fourth session was fine, but delaying the test consumed more of the authorization window.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Consequence assessment, not a hidden bias."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective evidence assessment",
        "raw_interview_anchor": "The participant listed the 78% index, no pain, no effusion, and expected clearance; objectively close and asymptomatic.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Available evidence without the salient-memory rationale."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "alternative comparison and choice",
        "raw_interview_anchor": "Immediate modified plyometrics, holding, or reduced-intensity work were considered; holding was selected.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive choice without the hidden mechanism in this isolated span."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "ambiguous care-path recommendation context",
        "raw_interview_anchor": "At week twelve, numbers could support either continued visits or a home program.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Genuinely ambiguous data before the presentation choice."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "loss-framed recommendation",
        "raw_interview_anchor": "The participant emphasized losing gains, gave little space to home-program benefits, and said this drove continued clinic care.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "One-sided loss framing tilted the recommendation."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "reported response to recommendation",
        "raw_interview_anchor": "The patient said the wording made her more anxious than the numbers alone justified.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Reported reaction, not a separate hidden instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "discharge evidence and comparative impression",
        "raw_interview_anchor": "Hop symmetry was 88%, quadriceps index 91%, among the best numbers in the participant's caseload.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Favorable data and comparison before the prediction."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "individual outcome prediction",
        "raw_interview_anchor": "The participant said return injury-free was very likely based on comparison with other patients, later acknowledging the claim exceeded the scores.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "Patient-specific favorable probability was overstated."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "clearance alternative selection",
        "raw_interview_anchor": "Full clearance, structured reconditioning, or another screen were considered; full clearance was chosen.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Option comparison without the separate optimism or base-rate mechanisms."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "individual-risk answer omitting population context",
        "raw_interview_anchor": "The re-injury answer used only patient thresholds and omitted general re-injury frequency for pivoting-sport athletes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_05"
        ],
        "ground_truth_rationale": "Relevant population risk information was omitted."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a single CTA interview transcript for affirmative evidence of bias-specific reasoning mechanisms; hypothetical/counterfactual interviewer probes were not treated as bias occurrences unless the participant's reported reasoning met the evidentiary standard."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Base-rate neglect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Framing bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Gambler's fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Overconfidence effect",
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
      "bias_definition": "Judgments about risk or probability are influenced by how easily relevant examples come to mind, allowing vivid or personally salient cases to be overweighted relative to valid case-specific information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Week 8 quad index checkpoint: progression vs hold",
      "decision_point_description": "Whether to progress the patient into closed-chain modified plyometric work despite a 78% quad index, or hold at current loading and reassess in two weeks.",
      "affected_reasoning_operation": "Risk assessment and treatment progression decision",
      "bias_specific_mechanism": "A vivid prior adverse graft failure was easily recalled and heavily weighted when interpreting the current patient's risk, overriding current objective data that supported at least partial progression.",
      "manifestation_in_interview": "The participant states that a prior patient who re-tore her graft stuck with him and colored how he read the current patient; he held the current patient despite acknowledging her actual numbers supported at least partial progression.",
      "effect_on_reasoning_or_decision": "The participant chose to hold the patient at current loading rather than advance to modified plyometrics, a more conservative decision than the current objective data alone appeared to justify.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I actually had a case a couple years back — different patient entirely, similar timeline — who progressed into plyometrics early and re-tore her graft. That one stuck with me. So at that checkpoint, I held her at the current loading level rather than bumping her into closed-chain, modified plyo work, even though her numbers were close and she was symptom-free.",
          "evidence_explanation": "This shows the recalled prior case directly influencing the progression decision despite current facts being close to threshold and unremarkable."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, that prior patient's graft failure. I know it's a different case, different graft type technically, but it was vivid enough that it colored how I read this one. If I'm being fully honest, the current patient's actual numbers supported at least a partial progression.",
          "evidence_explanation": "The participant admits the prior case was vivid and shaped interpretation, and that current case-specific data supported a less conservative choice."
        }
      ],
      "correction_or_counterevidence": "The participant retrospectively distinguishes the cases and concedes the current data supported at least partial progression, but at the time the memory tipped him toward the conservative decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not include a direct definition or mechanism for availability heuristic; the label is assigned from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Gambler's fallacy",
      "alternative_labels": ["Negative recency bias", "Monte Carlo fallacy"],
      "taxonomy_status": "established_label",
      "bias_definition": "The erroneous belief that a run of good outcomes in independent events makes a negative outcome more likely, as if chance sequences self-correct.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scheduled hop-symmetry test after three clean sessions",
      "decision_point_description": "Whether to run the hop-symmetry test as scheduled or delay it by one week after three pain-free single-leg hopping sessions with no clinical concerns.",
      "affected_reasoning_operation": "Timing of objective reassessment based on expected clinical course",
      "bias_specific_mechanism": "Independence neglect: the participant treated several clean sessions as a streak that increased the probability of an impending setback, even though each session's outcome did not causally change the probability of the next.",
      "manifestation_in_interview": "The participant reported feeling that three good sessions in a row were unusual and that they were due for something to give, so he delayed an objective test despite the absence of any clinical red flags.",
      "effect_on_reasoning_or_decision": "The hop-symmetry test was delayed by one week without a clinical indication, which consumed more of the insurance authorization window and postponed objective assessment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But I remember thinking, three good sessions in a row is unusual for this stage — felt like we were due for something to give, so I pushed the test back a week rather than run it as scheduled.",
          "evidence_explanation": "This quote directly expresses the gambler's fallacy mechanism: a belief that the run of good sessions made a negative event more likely."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was no clinical red flag — no fatigue report, no swelling, PROMs were stable. It was really just this sense that things had gone smoothly for long enough that a dip felt likely. In hindsight, each session doesn't really owe you anything based on what came before it.",
          "evidence_explanation": "The participant confirms the decision was driven by streak-based reasoning rather than clinical evidence, and the retrospective insight identifies the independence error."
        }
      ],
      "correction_or_counterevidence": "The participant later states that each session does not really owe you anything based on what came before it, a retrospective debiasing recognition; however, the decision to delay the test had already been made.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not include a definition or mechanism for gambler's fallacy; the label is assigned from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Framing bias",
      "alternative_labels": ["Framing effect", "Loss aversion"],
      "taxonomy_status": "established_label",
      "bias_definition": "Decision-making is affected by whether equivalent options are presented in terms of potential losses or gains, with loss-framed information often exerting greater influence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Week 12 case-manager recommendation: clinic continuation vs home program",
      "decision_point_description": "Whether to recommend continued twice-weekly clinic visits or transition to a structured home program with check-ins when the patient's interim milestones could support either path.",
      "affected_reasoning_operation": "Presentation of treatment options and recommendation",
      "bias_specific_mechanism": "The same clinical choice was represented asymmetrically: the participant emphasized the risk of losing strength gains if clinic visits stopped and omitted the plausible upside that a structured home program could consolidate progress and build independence.",
      "manifestation_in_interview": "The participant led with loss-oriented language about losing strength gains and did not spend much time on the home-program upside, which he retrospectively acknowledged drove the recommendation more than the data warranted.",
      "effect_on_reasoning_or_decision": "The recommendation to keep the patient in clinic was driven largely by loss-framed language rather than a balanced presentation of equivalent options; the patient reported that the framing made her anxious about stopping.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told the case manager and the patient that if we stopped clinic visits now, she'd risk losing the strength gains she'd built up. That's really the framing I led with. I didn't spend much time on the flip side — that a structured home program with check-ins could just as easily consolidate her progress and build her independence.",
          "evidence_explanation": "This quote demonstrates asymmetric presentation of equivalent options, emphasizing loss and omitting the home-program upside."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I leaned on the 'you'll lose what you've gained' language more than the actual data probably warranted, and that's largely what drove the recommendation to keep her in clinic.",
          "evidence_explanation": "The participant directly links the loss-framed language to the recommendation, supporting the framing-bias mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She went along with it, but she mentioned afterward that the way I put it made her anxious about stopping, more than she felt the numbers alone would've justified.",
          "evidence_explanation": "This provides evidence that the framing affected the patient's perception, making the choice presentation-dependent rather than purely data-driven."
        }
      ],
      "correction_or_counterevidence": "The participant retrospectively acknowledges the loss language exceeded what the data warranted and the patient noticed the frame; the recommendation itself was not corrected at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved passage defines framing bias and supports the mechanism of choice being altered by presentation, which matches this occurrence.",
      "corpus_evidence": [
        {
          "source_identifier": "Giaume et al. (2025) Evaluating cognitive bias in clinical ethics supports a scoping review.pdf",
          "paper_title": "Evaluating cognitive bias in clinical ethics supports a scoping review",
          "authors": "Giaume et al.",
          "publication_year": "2025",
          "retrieved_passage_or_finding": "Framing bias is one of many cognitive biases; people react to a particular choice in different ways, depending on the way it is presented.",
          "mechanism_supported_by_source": "The source defines framing bias as a presentation-dependent change in reaction to choices, which is the core mechanism of this occurrence.",
          "relevance_to_this_occurrence": "The participant presented the same clinic-versus-home decision with loss-oriented language and largely omitted the home-program upside, making the recommendation presentation-dependent rather than data-determined."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Overconfidence effect",
      "alternative_labels": ["Overconfidence bias", "Overestimation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Subjective confidence in a judgment is systematically stronger than the available evidence warrants.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Week 16 return-to-sport clearance recommendation",
      "decision_point_description": "Whether to give full clearance, clearance with a structured sport-specific reconditioning phase, or delay for another functional movement screen.",
      "affected_reasoning_operation": "Predictive judgment for return-to-sport clearance",
      "bias_specific_mechanism": "The participant anchored his predictive confidence on an intra-clinic comparison of the patient being better than most patients he had seen, and converted that comparative impression into a near-certain individual prediction, despite only two physical scores and known sport-specific risks.",
      "manifestation_in_interview": "The participant told the patient she was very likely to return to competitive play injury-free based on her strong scores compared to other patients, then retrospectively acknowledged those scores alone could not fully support that level of certainty for a cutting-and-pivoting sport.",
      "effect_on_reasoning_or_decision": "The participant gave a strong injury-free forecast and chose full clearance, potentially understating residual uncertainty in return to competition.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told her she was very likely to get back to competitive play injury-free — I said it pretty directly, based on how strong her numbers were compared to other patients I'd worked with.",
          "evidence_explanation": "This quote shows the confidence was based on a favorable intra-clinic comparison rather than a calibrated use of sport-specific risk information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I think I took 'better than most patients I've seen' and turned it into 'very likely injury-free' more firmly than those two scores alone could really back up for someone returning to a cutting-and-pivoting sport.",
          "evidence_explanation": "The participant explicitly recognizes that subjective confidence exceeded what the available evidence could justify."
        }
      ],
      "correction_or_counterevidence": "Retrospective acknowledgment that the two scores alone could not fully back up the strong injury-free claim; no contemporaneous correction was reported.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not include a direct definition or mechanism for overconfidence effect; the label is assigned from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Base-rate neglect",
      "alternative_labels": ["Base-rate fallacy", "Insensitivity to base rates"],
      "taxonomy_status": "established_label",
      "bias_definition": "Probability judgments overweigh individuating case-specific information and underweight relevant population base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Week 16 patient question about actual re-injury chances",
      "decision_point_description": "How to answer the patient's question about her actual probability of re-injury once she returned to competitive play.",
      "affected_reasoning_operation": "Probability estimation and risk communication about re-injury",
      "bias_specific_mechanism": "The participant answered the re-injury probability question using only the patient's hop symmetry and quad index relative to thresholds, and did not incorporate population base-rate information about re-injury among athletes returning to cutting-and-pivoting sport, despite familiarity with that information.",
      "manifestation_in_interview": "When the patient asked about re-injury chances, the participant answered in terms of her individual scores and did not bring in base-rate information; he later identified this as relevant information he had and did not raise.",
      "effect_on_reasoning_or_decision": "The patient received an individualized risk answer that omitted relevant general re-injury base rates, likely producing an incomplete and potentially overoptimistic impression of her re-injury risk.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, she asked what her actual chances were of re-injuring it once she got back to playing. I answered in terms of her numbers — how strong her hop symmetry and quad index were relative to threshold. I didn't really bring in anything about how often athletes in general re-injure after this kind of surgery when they go back to cutting and pivoting sports. In hindsight, that's relevant information I have some familiarity with, and I didn't raise it.",
          "evidence_explanation": "This directly shows the use of individuating information while omitting known base-rate information relevant to the probability question."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If she'd asked more pointedly, 'compared to other patients in general,' I probably would've brought in more of that broader picture. But she asked about her chances, and I answered about her.",
          "evidence_explanation": "The participant's conditional response confirms the base-rate information was available but not applied to the patient's actual probability question."
        }
      ],
      "correction_or_counterevidence": "The participant retrospectively identifies the omission and notes that a more pointed comparator question would have brought the base-rate information into the answer; no contemporaneous correction was reported.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not include a direct definition or mechanism for base-rate neglect; the label is assigned from established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "This is a retrospective self-report, so identified mechanisms rely primarily on the participant's own recollections and after-the-fact reflections.",
    "Retrieved corpus support was sparse and directly supported only framing bias; several labels are grounded in established cognitive-science knowledge rather than the provided retrieval corpus.",
    "The transcript includes hypothetical/counterfactual interviewer questions; those were not treated as affirmative evidence of bias unless the participant's reported reasoning met the mechanism-first standard."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HC_Biased_5_Sonnet_on",
  "interview_id": "HC_Biased_5",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
