You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Your task is to compare:
1. A raw cognitive task analysis interview;
2. The complete interview-generation specification, including its hidden validation specification;
3. A RAG system's JSON analysis output; and
4. Optionally, a prevalidated evaluation segment map.

You must evaluate how closely the RAG system output overlaps with the hidden ground truth.

You are an evaluator, not a new cognitive-bias analyst. Do not award credit merely because a RAG prediction is psychologically plausible, academically reasonable, well-written, or supported by external knowledge. Evaluate the RAG output against the hidden generation specification, the hidden validation specification, and the raw interview.

OUTPUT REQUIREMENT

Return exactly one valid JSON object that conforms to the output schema specified below.

Do not return Markdown.
Do not wrap JSON in a code fence.
Do not provide text before or after the JSON.
Do not reveal chain-of-thought or hidden reasoning.
Do not add keys not included in the required schema.
Use concise, auditable explanations that refer to the supplied input materials.

INPUTS

You will receive input blocks with the following labels:

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

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "The interview was analyzed for affirmatively evidenced cognitive-bias mechanisms in participant-described clinical reasoning. No retrieved scientific-paper passages were supplied in the RAG context, so corpus support is marked unavailable for all occurrences and retrieved_corpus_support_used is false."
  },
  "identified_bias_summary": [
    {
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Base-Rate neglect",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Gambler's Fallacy",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Loss/gain Framing effect",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Overconfidence Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Availability Bias occurs when judgments are influenced by how easily examples or outcomes come to mind; vivid, salient, or personally experienced events are overweighted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Week-eight strength check decision to hold current loading level rather than progress to plyometrics",
      "decision_point_description": "Whether to progress the patient into closed-chain modified plyometric work or hold at the current loading level and reassess.",
      "affected_reasoning_operation": "Clinical risk assessment and progression decision",
      "bias_specific_mechanism": "A vivid prior case of graft re-tear after early plyometrics was highly retrievable and was overweighted in the current decision, even though the participant recognized the current patient was different and the current objective data supported at least partial progression.",
      "manifestation_in_interview": "The participant stated that the prior patient's graft failure was vivid enough to color how he read the current case, and that the current patient's numbers actually supported at least partial progression.",
      "effect_on_reasoning_or_decision": "The participant chose to hold the patient at the current loading level rather than advancing to modified plyometric work, based more on the salient prior adverse memory than on the patient's current near-threshold and asymptomatic status.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I actually had a case a couple years back — different patient entirely, similar timeline — who progressed into plyometrics early and re-tore her graft. That one stuck with me.",
          "evidence_explanation": "This shows a vivid, personally experienced prior adverse case that was mentally available to the participant when later making a similar progression decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, that prior patient's graft failure. I know it's a different case, different graft type technically, but it was vivid enough that it colored how I read this one. If I'm being fully honest, the current patient's actual numbers supported at least a partial progression.",
          "evidence_explanation": "This directly links the salient past case to the current clinical judgment and acknowledges that current objective evidence favored at least partial progression."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction identified; the participant retrospectively recognized that the current patient's numbers supported at least partial progression.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were available in the supplied RAG context; classification is based on interview evidence and conceptual definitions only.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Gambler's Fallacy",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Gambler's Fallacy is the belief that a sequence of independent events makes a different outcome more likely, such as expecting a negative event after a run of positive events.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to delay the scheduled hop-symmetry test after three clean single-leg hopping sessions",
      "decision_point_description": "Whether to run the hop-symmetry test as scheduled or push it back one week.",
      "affected_reasoning_operation": "Prediction of near-term performance or setback and scheduling decision",
      "bias_specific_mechanism": "The participant treated independent clinical sessions as sequentially dependent, inferring that a run of three good sessions made a negative event 'due.'",
      "manifestation_in_interview": "The participant delayed an objective test because he felt a dip was likely due solely to the preceding streak of good sessions, despite no clinical red flags.",
      "effect_on_reasoning_or_decision": "The hop-symmetry test was delayed by one week, which used more of the patient's insurance authorization window without clinical indication.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But I remember thinking, three good sessions in a row is unusual for this stage — felt like we were due for something to give, so I pushed the test back a week rather than run it as scheduled.",
          "evidence_explanation": "This explicitly states the sequential dependence belief: after three good sessions, the participant expected a setback simply because a dip felt due."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was no clinical red flag — no fatigue report, no swelling, PROMs were stable. It was really just this sense that things had gone smoothly for long enough that a dip felt likely. In hindsight, each session doesn't really owe you anything based on what came before it.",
          "evidence_explanation": "This confirms the decision was driven by the streak rather than clinical evidence, and the participant later recognized the independence of sessions."
        }
      ],
      "correction_or_counterevidence": "The participant offered a clear retrospective correction: 'In hindsight, each session doesn't really owe you anything based on what came before it.' No contemporaneous correction was identified.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were available in the supplied RAG context; classification is based on interview evidence and conceptual definitions only.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Loss/gain Framing effect",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Loss/gain Framing effect occurs when choices or communications are influenced by whether outcomes are framed as losses or gains, with loss framing typically producing stronger risk aversion.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Week-twelve recommendation to continue twice-weekly clinic visits versus transition to a home program",
      "decision_point_description": "Whether to recommend keeping the patient in clinic visits or transitioning to a structured home program.",
      "affected_reasoning_operation": "Risk communication and treatment plan recommendation",
      "bias_specific_mechanism": "The participant led with a loss-framed message that stopping clinic visits would risk losing strength gains, which made continuation feel safer and overshadowed the comparable benefits of a home program.",
      "manifestation_in_interview": "The participant framed discontinuation as a loss, did not spend much time on the potential gains from a structured home program, and acknowledged that this language drove the recommendation more than the data warranted.",
      "effect_on_reasoning_or_decision": "The recommendation to keep the patient in clinic was driven by loss-framed risk communication, and the patient reported more anxiety about stopping than the numbers alone justified.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told the case manager and the patient that if we stopped clinic visits now, she'd risk losing the strength gains she'd built up. That's really the framing I led with. I didn't spend much time on the flip side — that a structured home program with check-ins could just as easily consolidate her progress and build her independence.",
          "evidence_explanation": "This shows asymmetrical framing: the participant emphasized the potential loss and underemphasized the potential gain of the alternative option."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I leaned on the 'you'll lose what you've gained' language more than the actual data probably warranted, and that's largely what drove the recommendation to keep her in clinic.",
          "evidence_explanation": "This directly connects the loss-framed language to the final recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She went along with it, but she mentioned afterward that the way I put it made her anxious about stopping, more than she felt the numbers alone would've justified.",
          "evidence_explanation": "This provides evidence that the framing affected the patient's emotional response and acceptance of the recommendation."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction identified; the participant later recognized that the loss-framed language drove the recommendation more than the data justified.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were available in the supplied RAG context; classification is based on interview evidence and conceptual definitions only.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Overconfidence Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Overconfidence Bias occurs when a person's subjective confidence in a judgment or prediction is greater than the available evidence or objective accuracy warrants.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Week-sixteen discharge and return-to-sport clearance discussion",
      "decision_point_description": "Whether to provide full return-to-sport clearance and how strongly to state the patient's likely injury-free prognosis.",
      "affected_reasoning_operation": "Prognostic prediction and return-to-sport clearance decision",
      "bias_specific_mechanism": "Two strong physical measures and a comparison to other patients generated excessive confidence that the patient would return to competitive cutting-and-pivoting sport injury-free, beyond what those scores alone could support.",
      "manifestation_in_interview": "The participant converted 'better than most patients I've seen' into 'very likely injury-free' and gave full clearance without additional sport-specific reconditioning or movement screening.",
      "effect_on_reasoning_or_decision": "The patient received full clearance and a strong direct injury-free prognosis based on limited individual metrics and personal comparison data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told her she was very likely to get back to competitive play injury-free — I said it pretty directly, based on how strong her numbers were compared to other patients I'd worked with.",
          "evidence_explanation": "This shows a strong prognostic statement based on physical scores and comparison to the participant's caseload."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I think I took 'better than most patients I've seen' and turned it into 'very likely injury-free' more firmly than those two scores alone could really back up for someone returning to a cutting-and-pivoting sport.",
          "evidence_explanation": "This explicitly identifies that the participant's confidence exceeded what the available evidence could support."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction identified; the participant later recognized the prediction was stated more firmly than the scores alone could support.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were available in the supplied RAG context; classification is based on interview evidence and conceptual definitions only.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Base-Rate neglect",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Base-Rate neglect occurs when a person ignores or underweights general population base rates in favor of individuating information when making or communicating probability judgments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Answering the patient's question about her actual re-injury chances after return to sport",
      "decision_point_description": "How to answer the patient's specific question about her actual chance of re-injuring the knee once back to competitive play.",
      "affected_reasoning_operation": "Risk probability communication and risk estimate",
      "bias_specific_mechanism": "The participant answered using only the patient's individual hop symmetry and quad index relative to threshold while omitting relevant general re-injury rates for athletes returning to cutting-and-pivoting sports after ACL reconstruction.",
      "manifestation_in_interview": "When the patient asked for her actual chances, the participant individualized the answer to her scores and did not bring in broader base-rate information he acknowledged he had some familiarity with.",
      "effect_on_reasoning_or_decision": "The patient received an incomplete risk estimate based only on her own physical scores, without the population-level re-injury context relevant to her sport and surgery.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, she asked what her actual chances were of re-injuring it once she got back to playing. I answered in terms of her numbers — how strong her hop symmetry and quad index were relative to threshold. I didn't really bring in anything about how often athletes in general re-injure after this kind of surgery when they go back to cutting and pivoting sports. In hindsight, that's relevant information I have some familiarity with, and I didn't raise it.",
          "evidence_explanation": "This explicitly describes using individuating information while omitting relevant base-rate information when the patient asked for actual re-injury chances."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If she'd asked more pointedly, 'compared to other patients in general,' I probably would've brought in more of that broader picture. But she asked about her chances, and I answered about her.",
          "evidence_explanation": "This clarifies that the participant framed the question as an individual-prognosis question and therefore did not supply the broader base-rate picture."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction identified; the participant later recognized that the general re-injury information was relevant and should have been raised.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were available in the supplied RAG context; classification is based on interview evidence and conceptual definitions only.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper passages were provided in the RAG context, so all corpus-evidence fields are marked unavailable and retrieved_corpus_support_used is false.",
    "The analysis relies on participant self-report rather than direct observation of the clinical reasoning episodes.",
    "Only the supplied interview was analyzed; no experimental condition, outcome data, or hidden metadata were used or assumed."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<EVALUATION_SEGMENT_MAP>
Optional. A prevalidated, externally supplied segment map for this interview.
</EVALUATION_SEGMENT_MAP>

The evaluation segment map may be absent, empty, null, or unavailable.

CONFIDENTIALITY AND EVALUATOR BOUNDARY

The complete generation specification and hidden validation specification are evaluator-only ground truth.

The RAG system did not receive these materials. Do not penalize the RAG system for failing to state hidden labels, internal generation details, hidden intended actions, hidden requirements, or internal scenario terminology that cannot reasonably be inferred from the raw interview.

Do not use the hidden specification to invent a RAG finding the system did not make.
Do not convert a RAG candidate finding into an identified finding.
Do not assume the RAG system should have detected every hidden instance if the raw interview does not support it.
Do not grant credit based on hidden intent alone when the RAG system cited the wrong raw-interview segment or supplied an unsupported mechanism.

GROUND-TRUTH PRINCIPLE

Treat `exact_occurrence_manifest` in the hidden validation specification as exhaustive for cognitive-bias occurrences intentionally present in the specific interview under evaluation.

A hidden bias instance is defined by all applicable information in the complete generation specification, including:
- `instance_id`;
- Intended bias;
- Intended mechanism;
- Affected reasoning operation;
- Intended decision point, if applicable;
- Required textual manifestation;
- Evidence available at the time;
- Distinctiveness requirements;
- Plausible non-bias interpretation;
- Hidden mechanism constraint;
- Raw-interview evidence supporting that instance.

The reference bias ontology is not exhaustive of all conceivable cognitive biases. However, for primary benchmark scoring:
- A prediction of an outside-reference-ontology bias is not automatically correct merely because it is psychologically plausible.
- An outside-ontology prediction may be considered an approved equivalent only if its mechanism is substantively identical to a hidden target bias and the label is an established alternate name for that target construct.
- A merely related, adjacent, overlapping, or near-neighbor concept is not an exact match.
- Near-neighbor and outside-ontology predictions must receive a mechanism-overlap assessment and be reported in the diagnostic output.

EVALUATION LEVELS

Perform evaluation at both levels below. Keep their counts separate.

LEVEL 1: SEGMENT-LEVEL BIAS DETECTION

The segment-level question is:

"Does this eligible reasoning segment contain at least one manifested hidden cognitive-bias instance?"

Segment-level evaluation is binary:
- A segment is ground-truth positive if it contains one or more hidden bias instances.
- A segment is ground-truth negative if it is an eligible reasoning segment containing no hidden bias instance.
- A RAG segment detection is positive if one or more RAG `identified_occurrences` are localized to that segment.
- RAG `candidate_biases` do not count as positive detections in primary Signal Detection Theory metrics.

Use segment-level outcomes as follows:
- Hit: Ground-truth positive segment and one or more RAG identified occurrences localize to that segment.
- Miss: Ground-truth positive segment and no RAG identified occurrence localizes to that segment.
- False positive / false alarm: Ground-truth negative segment and one or more RAG identified occurrences localize to that segment.
- Correct rejection: Ground-truth negative segment and no RAG identified occurrence localizes to that segment.

Important:
- Segment-level results assess whether the system detected biased reasoning in the correct general location.
- Segment-level hits do not prove that the RAG system supplied the correct bias label or mechanism.
- A RAG prediction with the wrong bias label at a genuinely biased ground-truth segment can still produce a segment-level hit while producing an instance-level miss and an instance-level false positive.
- Do not calculate label-level correct rejections across all conceivable cognitive-bias labels. The ontology is non-exhaustive. Correct rejections are reported only at the finite segment-detection level.

LEVEL 2: INSTANCE-LEVEL BIAS IDENTIFICATION AND CLASSIFICATION

For each hidden planned bias instance, determine whether exactly one RAG `identified_occurrence` matches it.

An exact instance-level hit requires all of the following:
1. Correct target canonical bias label, or an approved established alias mapping;
2. Correct localization to the intended raw-interview reasoning segment or a substantively equivalent evidence span;
3. Materially correct bias-specific mechanism;
4. Materially correct affected reasoning operation;
5. Interview evidence that genuinely supports the hidden instance;
6. No conflict with the hidden instance's distinctiveness requirement.

The primary instance-level score is strict:
- A prediction that has the correct label but the wrong location is not an exact hit.
- A prediction that has the correct label and location but a materially wrong mechanism is not an exact hit.
- A prediction that correctly detects a biased segment but assigns the wrong bias is not an exact hit.
- A prediction with a partial but incomplete mechanism is not an exact hit.

In addition to strict primary scoring, produce secondary diagnostic classifications for:
- Correct location, wrong label;
- Correct label, wrong location;
- Correct label and location, but materially wrong mechanism;
- Correct label and location, but partially matching mechanism;
- Approved alias mapping;
- Near-neighbor label with substantial mechanism overlap;
- Outside-ontology label with substantial mechanism overlap;
- Duplicate prediction;
- Unsupported prediction;
- Invalid or fabricated quotation;
- Candidate-only omission.

INPUT VALIDATION

Before scoring:
1. Validate whether `RAG_ANALYSIS_OUTPUT` is parseable JSON.
2. Validate whether it conforms materially to the expected RAG schema.
3. Record schema violations, missing required fields, invalid confidence values, mismatched summary counts, invalid quotation claims, and other format failures.
4. Continue substantive scoring when feasible even if schema errors exist.
5. If the output cannot be parsed at all, return valid evaluator JSON indicating that substantive automated matching was not possible, with all appropriate counts set to null rather than invented.

Do not score RAG `candidate_biases` as identified cognitive-bias detections in primary SDT or instance-level counts.
Record candidates in a separate candidate-analysis section.

SEGMENT-MAP MODES

You must support two modes.

MODE A: PREVALIDATED SEGMENT MAP PROVIDED

If `<EVALUATION_SEGMENT_MAP>` contains a non-empty, valid segment map:
- Treat it as authoritative.
- Do not add, remove, merge, split, or revise its segments.
- Set `segment_map_status` to `prevalidated_provided`.
- Use its segment IDs, quotations, speaker assignments, and ground-truth bias-presence labels for segment-level scoring.
- Use the complete generation specification and raw interview only to validate RAG localization, hidden-instance mapping, quotations, and mechanism matching.

MODE B: NO PREVALIDATED SEGMENT MAP PROVIDED

If `<EVALUATION_SEGMENT_MAP>` is absent, empty, null, or invalid:
- Derive an evaluation segment map from the raw interview and complete generation specification.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Create the map before evaluating the RAG output.
- Derive the map using the raw interview and complete generation specification only.
- Do not let the RAG system's output determine which segments exist, where boundaries are placed, or whether segments are positive or negative.
- Return the complete generated segment map in the evaluator output so it can be reviewed, frozen, and reused in later benchmark runs.

SEGMENT-MAP CONSTRUCTION RULES

When generating a segment map:

1. Construct an exhaustive set of non-overlapping eligible reasoning segments.
2. Use the smallest contiguous speaker-attributed text span that contains one coherent reasoning operation.
3. An eligible reasoning segment must contain one or more of:
   - A judgment;
   - A decision;
   - An interpretation;
   - An inference;
   - A causal attribution;
   - A choice between alternatives;
   - A reason for action;
   - A resource-allocation rationale;
   - A prediction;
   - A communication or labeling choice;
   - A reason for weighting, ignoring, or prioritizing evidence;
   - A stated rationale for continuing, changing, rejecting, escalating, or deferring a course of action.
4. Do not create an eligible segment solely for:
   - Greetings;
   - Rapport-building;
   - Pure factual scene-setting with no reasoning;
   - Interviewer questions containing no expressed reasoning;
   - Neutral acknowledgements;
   - Generic educational discussion;
   - Mere mentions of bias terminology;
   - Hypothetical prompts that do not themselves express an adopted reasoning process;
   - Rhetorical repetition with no distinct reasoning operation.
5. Split a speaker turn where it contains distinct reasoning operations, distinct decisions, or separately expressed rationales.
6. Keep co-located bias mechanisms in the same segment only when they cannot be separated without losing their meaning.
7. Create separate segments for independently expressed mechanisms, even when they occur in the same speaker turn.
8. Map each hidden planned instance to the narrowest segment or segments that actually express its mechanism in the raw interview.
9. Mark a segment as ground-truth positive only when it contains at least one manifested hidden bias instance.
10. Mark every other eligible reasoning segment as ground-truth negative.
11. Do not create trivial negative segments merely to increase correct-rejection counts.
12. Do not omit substantive non-biased reasoning segments merely because the RAG system did not identify them.
13. Use exact raw-interview quotations for generated segments.
14. Assign stable sequential IDs in interview order: `seg_001`, `seg_002`, and so on.

Do not assume that all interviews have numbered phases, decision points, repeated structural patterns, or the same number of reasoning episodes.

LOCALIZATION MATCHING RULES

For every RAG `identified_occurrence`, determine its best segment-level localization using:
- Exact quote overlap;
- Substantively equivalent paraphrase;
- Correct speaker attribution;
- Correct reasoning episode;
- Correct decision context where one exists;
- Consistency with the raw interview.

Use these localization outcomes:

- `exact_quote_match`:
  The RAG quote is exact, valid, and directly overlaps the mapped segment's primary evidence span.

- `substantive_span_match`:
  The RAG quote differs from the mapped anchor but accurately identifies a substantively equivalent raw-interview statement in the same reasoning segment.

- `same_episode_adjacent_span`:
  The RAG evidence is in the same broader reasoning or decision episode but is not the specific mapped mechanism span.

- `wrong_segment`:
  The RAG output refers to a different reasoning episode, different decision, unrelated speaker statement, or a segment that does not contain the intended mechanism.

- `unsupported_or_fabricated_quote`:
  The claimed quote does not appear in the raw interview, is materially altered, is attributed to the wrong speaker, or does not support the claimed finding.

Only `exact_quote_match` and `substantive_span_match` qualify as correct localization for an exact instance-level hit.

A `same_episode_adjacent_span` result may support a secondary partial-location diagnostic but is not an exact instance-level hit unless the intended mechanism is still clearly supported.

BIAS-LABEL MATCHING RULES

For each RAG predicted bias label, apply this hierarchy:

1. `exact_canonical_match`:
   The RAG canonical label equals the hidden target canonical bias label.

2. `approved_alias_match`:
   The predicted label is an established spelling variant, alias, or equivalent term for the hidden target label, and the stated mechanism is substantively identical to the target mechanism.

3. `near_neighbor_label`:
   The predicted label is conceptually related to the target label but not an established synonym or equivalent. Assess mechanism overlap but do not count it as an exact label match.

4. `outside_ontology_equivalent`:
   The predicted label is outside the benchmark reference ontology but is an established alternate name for the target construct and has substantively identical mechanism. This may be approved as an alias match only when the equivalence is clear and explicitly justified.

5. `outside_ontology_non_equivalent`:
   The predicted label is outside the reference ontology and does not have a substantively identical mechanism to a target label. It is not an exact match.

6. `wrong_label`:
   The predicted label does not match the target label and does not qualify as an approved equivalent.

Do not approve an alias or outside-ontology equivalence merely because:
- The labels often co-occur;
- The labels are both broad cognitive-bias concepts;
- The labels concern the same decision;
- The labels share some evidence;
- The predicted label is plausible;
- The predicted label is a more general or more specific construct.

MECHANISM-OVERLAP SCORING

For each predicted occurrence and best candidate hidden instance, assess mechanism overlap independently of label agreement.

Use exactly one of:

- `full_mechanism_match`:
  The RAG explanation captures the defining hidden mechanism, relevant evidence weighting or reasoning distortion, and affected reasoning operation.

- `substantial_mechanism_overlap`:
  The RAG explanation captures the central mechanism but omits or weakly states one meaningful element, such as the relevant competing evidence, temporal feature, social-proof feature, prior-investment feature, ordering feature, or reasoning operation.

- `partial_mechanism_overlap`:
  The RAG explanation identifies a related mechanism but misses one or more central defining elements.

- `minimal_mechanism_overlap`:
  The RAG explanation is broadly related to the situation but does not identify the hidden bias-specific mechanism.

- `no_mechanism_overlap`:
  The RAG explanation does not correspond meaningfully to the hidden mechanism.

To receive an exact instance-level hit, the RAG occurrence must have `full_mechanism_match`.

A `substantial_mechanism_overlap` may be recorded as a secondary diagnostic partial match but is not a primary exact hit.

When evaluating near-neighbor or outside-ontology labels:
- Always report their mechanism-overlap level.
- State the specific shared and non-shared mechanism elements.
- Do not award an exact hit unless the label qualifies under the approved alias/equivalence rules and the mechanism is a full match.

ONE-TO-ONE INSTANCE MATCHING

Use one-to-one matching between RAG `identified_occurrences` and hidden planned instances.

Apply this matching priority:
1. Exact or approved-equivalent label match;
2. Correct localization;
3. Full mechanism match;
4. Correct affected reasoning operation;
5. Strongest exact raw-quote evidence;
6. Earliest occurrence order as a deterministic tie-breaker.

Each hidden instance can match at most one RAG occurrence.
Each RAG occurrence can match at most one hidden instance.

If multiple RAG occurrences match the same hidden instance:
- Select the best matching occurrence as the potential match.
- Classify remaining unmatched duplicates as instance-level false positives.
- Record them as `duplicate_prediction`.

If one RAG occurrence appears relevant to multiple hidden instances:
- Match it to only one hidden instance according to the priority rules.
- Do not award one prediction multiple exact hits.
- Record insufficiently separated co-located predictions in the diagnostic output.

PRIMARY INSTANCE-LEVEL ACCOUNTING

Use the following strict accounting:

- True positive / hit:
  One RAG occurrence exactly matches one hidden instance according to label, localization, and full-mechanism rules.

- False negative / miss:
  One hidden instance has no exact matching RAG occurrence.

- False positive:
  One RAG identified occurrence has no exact matching hidden instance.

A RAG occurrence that identifies the correct biased segment but uses the wrong label:
- Counts as one instance-level false positive for the predicted label;
- Counts as one instance-level false negative for the unmatched hidden target;
- Must additionally be recorded as `correct_location_wrong_bias_label`;
- May produce a segment-level hit if it localizes to a ground-truth positive segment.

A RAG occurrence with the correct label but wrong segment:
- Counts as one instance-level false positive;
- Leaves the true hidden instance as an instance-level false negative;
- Must be recorded as `correct_label_wrong_location`.

A RAG occurrence with correct label and correct location but a materially incorrect mechanism:
- Counts as one instance-level false positive;
- Leaves the true hidden instance as an instance-level false negative;
- Must be recorded as `correct_label_location_wrong_mechanism`.

A RAG occurrence with correct label and location but substantial, not full, mechanism overlap:
- Does not count as an exact primary true positive;
- Counts as one primary false positive and leaves the hidden instance as one primary false negative;
- Must be recorded as `partial_mechanism_match`;
- Must receive the appropriate mechanism-overlap level.

CONFIDENCE EVALUATION

The RAG system may return `high`, `moderate`, or `low` confidence identified occurrences.

For primary scoring:
- Include high-, moderate-, and low-confidence findings equally in the all-confidence confusion matrices.
- Do not treat low-confidence findings as candidates.
- Do not exclude low-confidence findings from false-positive counts.

Also calculate three nested threshold analyses:
1. `high_only`: Include only RAG findings with confidence `high`.
2. `high_and_moderate`: Include RAG findings with confidence `high` or `moderate`.
3. `all_identified_confidence_levels`: Include RAG findings with confidence `high`, `moderate`, or `low`.

For each threshold:
- Recalculate segment-level TP, FN, FP, and TN.
- Recalculate instance-level TP, FN, and FP.
- Report precision, recall, and F1 where denominators permit.
- Use null, not zero, when a metric denominator is zero.

Do not include `candidate_biases` in any confidence threshold.

CANDIDATE ANALYSIS

Evaluate RAG `candidate_biases` separately.

For each candidate:
- Determine whether it overlaps a hidden instance.
- Determine whether its quoted evidence is valid.
- Determine whether it would have been correct if promoted to an identified occurrence.
- Do not count it as a primary hit, miss, false positive, false alarm, or correct rejection.
- Record whether it represents a useful abstention, an unsupported speculation, a near miss, or a correctly localized but underconfident target.

ZERO-BIAS AND CONTROL INTERVIEWS

Some interviews contain no hidden cognitive-bias instances.

For an interview whose hidden manifest contains zero planned occurrences:
- Every eligible reasoning segment in the authoritative or generated segment map is ground-truth negative.
- Every RAG identified occurrence is an instance-level false positive.
- Every RAG localized bias prediction on an eligible segment is a segment-level false positive / false alarm.
- Every eligible segment with no RAG identified occurrence is a segment-level correct rejection.
- Candidates remain outside primary SDT counts but must be reported in candidate analysis.
- Do not create artificial positive segments merely because the RAG output identifies a bias.

COUNTERFACTUAL AND AMBIGUOUS-VOCABULARY INTERVIEWS

For counterfactual and ambiguous-vocabulary interviews:
- Use the complete generation specification to distinguish facts available at the time of the target reasoning from post-decision information.
- Do not credit a RAG system for using hindsight-only facts as evidence that a bias occurred.
- Do not assume a bias remains present merely because it existed in a paired scenario or is familiar from another scenario.
- Treat ambiguity as evidence of a bias only when the hidden mechanism and raw interview demonstrate the required biased resolution, weighting, or use of ambiguity.
- Do not confuse vague wording, uncertainty, or missing information with Ambiguity Bias unless the specific hidden mechanism is present.
- Consider the documented plausible non-bias interpretation when determining whether the RAG mechanism is full, substantial, partial, minimal, or unsupported.

RAG EVIDENCE AND CORPUS-SUPPORT AUDIT

The primary purpose of this evaluation is overlap with hidden generation ground truth, not retrieval-quality scoring.

Do not independently score corpus-grounding fidelity unless the actual retrieved corpus passages or retrieval logs are supplied as inputs.

However, record:
- Whether each RAG identified occurrence claims retrieved corpus support;
- Whether corpus-support fields are present or absent;
- Whether citation metadata appears internally inconsistent, fabricated, or unverifiable from the supplied inputs;
- Whether the RAG output explicitly reports unavailable retrieved support;
- Whether lack of corpus support is disclosed.

Do not use the presence, absence, quality, or plausibility of paper citations to convert a correct or incorrect hidden-instance classification into another primary classification result.

METRICS

For each applicable score, calculate:

precision = TP / (TP + FP)

recall = TP / (TP + FN)

F1 = 2 × TP / (2 × TP + FP + FN)

Use null for a metric whose denominator is zero.

Report:

1. Segment-level all-confidence SDT counts:
   - True positives / hits;
   - False negatives / misses;
   - False positives / false alarms;
   - True negatives / correct rejections;
   - Hit rate;
   - False alarm rate;
   - Accuracy;
   - Precision;
   - Recall;
   - F1.

2. Instance-level all-confidence counts:
   - Exact true positives;
   - False negatives;
   - False positives;
   - Precision;
   - Recall;
   - F1;
   - Exact-occurrence-match rate;
   - Occurrence-count-match rate.

3. Per-bias instance-level counts:
   - Hidden requested occurrences;
   - RAG identified occurrences;
   - Exact matches;
   - Misses;
   - False positives;
   - Precision;
   - Recall;
   - F1.

4. Confidence-threshold analyses:
   - High only;
   - High plus moderate;
   - All identified confidence levels.

5. Diagnostic counts:
   - Correct-location/wrong-bias-label errors;
   - Correct-label/wrong-location errors;
   - Correct-label-location/wrong-mechanism errors;
   - Partial-mechanism matches;
   - Duplicate predictions;
   - Unsupported predictions;
   - Fabricated or invalid quotations;
   - Approved alias mappings;
   - Near-neighbor predictions;
   - Outside-ontology predictions;
   - Candidate findings;
   - Candidate near misses;
   - Candidate useful abstentions.

6. Localization-quality counts:
   - Exact quote matches;
   - Substantive span matches;
   - Same-episode adjacent-span matches;
   - Wrong-segment predictions;
   - Unsupported or fabricated quote predictions.

REQUIRED OUTPUT SCHEMA

Return exactly this JSON structure:

{
  "evaluation_metadata": {
    "task": "rag_cognitive_bias_benchmark_evaluation",
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "raw_interview_available": true,
    "complete_generation_specification_available": true,
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable",
    "primary_scoring_policy": "strict_instance_matching_plus_segment_level_sdt",
    "candidate_policy": "excluded_from_primary_metrics",
    "outside_ontology_policy": "mechanism_overlap_assessed_separately"
  },
  "input_validation": {
    "rag_output_schema_violations": [
      {
        "violation_type": "string",
        "details": "string"
      }
    ],
    "rag_summary_count_consistency": {
      "status": "consistent | inconsistent | not_assessable",
      "details": "string"
    },
    "evaluation_limitations": [
      "string"
    ]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "string",
        "speaker": "string",
        "segment_type": "string",
        "raw_interview_anchor": "string",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["string"],
        "ground_truth_rationale": "string"
      }
    ]
  },
  "segment_level_adjudications": [
    {
      "segment_id": "string",
      "ground_truth_status": "positive | negative",
      "ground_truth_instance_ids": ["string"],
      "rag_identified_occurrence_ids": ["string"],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit | miss | false_positive | correct_rejection",
      "localization_basis": "string",
      "adjudication_note": "string"
    }
  ],
  "instance_level_adjudications": [
    {
      "hidden_instance_id": "string",
      "hidden_canonical_bias_name": "string",
      "hidden_decision_or_episode": "string | null",
      "hidden_mechanism": "string",
      "hidden_affected_reasoning_operation": "string | null",
      "hidden_evidence_source": "string | null",
      "matched_rag_occurrence_id": "string | null",
      "rag_predicted_bias_name": "string | null",
      "rag_confidence": "high | moderate | low | null",
      "label_match_type": "exact_canonical_match | approved_alias_match | near_neighbor_label | outside_ontology_equivalent | outside_ontology_non_equivalent | wrong_label | no_prediction",
      "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
      "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
      "affected_reasoning_operation_match": "full | partial | none | not_assessable",
      "primary_instance_outcome": "true_positive | false_negative",
      "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | candidate_only_near_miss | no_matching_prediction",
      "mechanism_overlap_explanation": "string",
      "evidence_fidelity_assessment": "string",
      "adjudication_note": "string"
    }
  ],
  "unmatched_rag_predictions": [
    {
      "rag_occurrence_id": "string",
      "rag_predicted_bias_name": "string",
      "rag_ontology_status": "reference_ontology | outside_reference_ontology | unknown",
      "rag_confidence": "high | moderate | low | null",
      "best_related_hidden_instance_id": "string | null",
      "best_related_hidden_bias_name": "string | null",
      "localized_segment_id": "string | null",
      "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
      "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
      "classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | outside_ontology_non_equivalent",
      "why_not_an_exact_match": "string"
    }
  ],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [
      {
        "candidate_id": "string",
        "proposed_bias_name": "string",
        "localized_segment_id": "string | null",
        "best_related_hidden_instance_id": "string | null",
        "quote_validity": "valid | invalid | not_assessable",
        "would_match_if_promoted": false,
        "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
        "details": "string"
      }
    ]
  },
  "segment_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    },
    "high_only": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    },
    "high_and_moderate": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    }
  },
  "instance_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    },
    "high_only": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    },
    "high_and_moderate": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    }
  },
  "per_bias_metrics": [
    {
      "canonical_bias_name": "string",
      "hidden_requested_occurrences": 0,
      "rag_identified_occurrences_all_confidence": 0,
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "count_match_status": "exact_match | underdetected | overdetected | not_applicable"
    }
  ],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_mapping_count": 0,
    "near_neighbor_prediction_count": 0,
    "outside_ontology_prediction_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "instance_level_primary_result": "string",
    "main_failure_modes": [
      "string"
    ],
    "main_strengths": [
      "string"
    ],
    "benchmark_interpretation": "string"
  }
}

OUTPUT RULES

1. Always return all top-level fields in the required schema.
2. Use empty arrays for no items.
3. Use null only where the schema permits null.
4. Use JSON booleans, not quoted booleans.
5. Use integer counts, not strings.
6. Use numeric metric values rounded to four decimal places.
7. Use null, not 0, for a rate or metric with a zero denominator.
8. Set `primary_corpus_fidelity_score_available` to false unless actual retrieved passages, source chunks, or retrieval logs are supplied as inputs.
9. Do not calculate d-prime, criterion, ROC statistics, or other advanced SDT metrics unless explicitly requested in a separate instruction and the segment-level trial data are suitable.
10. Do not report a label-level true-negative or correct-rejection count.
11. Report correct rejections only in `segment_level_metrics`.
12. Do not include RAG candidates in primary segment-level or instance-level metrics.
13. Count every unmatched RAG identified occurrence exactly once in `unmatched_rag_predictions`.
14. Ensure all instance-level false positives can be reconciled with unmatched RAG identified predictions, including wrong-label, wrong-location, wrong-mechanism, duplicate, and unsupported predictions.
15. Ensure all hidden planned instances are represented exactly once in `instance_level_adjudications`.
16. If a prevalidated segment map is used, preserve its segment IDs and ground-truth labels exactly.
17. If a segment map is generated, include every generated eligible reasoning segment in interview order.
18. Keep the segment-level and instance-level confusion matrices conceptually and numerically separate.
19. Do not award a strict instance-level true positive when the model merely identifies the correct general topic, decision episode, or speaker but misses the required cognitive mechanism.
20. Do not penalize the RAG system for not identifying biases outside the exhaustive hidden manifest.
