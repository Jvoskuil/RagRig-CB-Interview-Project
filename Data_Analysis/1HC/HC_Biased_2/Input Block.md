<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a internal case review on decision-making during admissions, and that I can ask follow-up questions as we go.

Participant: Sure, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role on the team during this admission?

Participant: I was the attending on the general medicine service. I had a resident covering with me, and we picked up this patient on hospital day one after she came in for something unrelated and ended up with a new finding on her monitor.

Interviewer: And what was your overall goal for her care during the stay?

Participant: Mainly to get her diagnosis sorted out and make sure we sent her home with a safe, appropriate plan. She was 78, otherwise fairly independent, living with her daughter nearby.

Interviewer: Can you walk me through what happened, from the diagnosis to discharge?

Participant: She came in and the admission ECG showed she was in atrial fibrillation, which nobody had picked up before — persistent, not paroxysmal. That obviously changes the calculus for stroke prevention. Her CHA2DS2-VASc came out to 4, so her annual stroke risk if left untreated is meaningful. Her HAS-BLED was 2, which is moderate, not a red flag. Pharmacy checked and there were no interactions with the DOAC we'd typically use. But she'd had a fall about three weeks before admission — mechanical, tripped on a rug at home, no head strike, no fracture, fully worked up at the time. Still, when I saw "fall" in the history, that gave me pause about starting a blood thinner right away. I told the team we'd hold off and get a formal fall-risk assessment first before committing to anything.

Then on day two, one of the nurses mentioned, sort of in passing, that a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation. Understandably, that got around the unit, and my patient's daughter had heard a version of it too. She was in the room a lot and got increasingly anxious every time anticoagulation came up. Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated. That pushed our timeline back a day.

By day three the CT was normal, and physical therapy had cleared her fall risk as low with a walker. So on paper the numbers were now clearly in favor of starting treatment. I remember standing at the nurses' station with the resident and just picturing what it would be like if we started her on this drug and then she had a major bleed — the conversation with the daughter, explaining that decision, how that would sit with all of us. It wasn't just that it would be bad; it felt like the kind of thing I'd still be replaying weeks later, something that would sit over the whole team and not really lift for a long time. That feeling seemed heavier to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge.

Then on day four, right before discharge, she got a small bruise at her IV site — unrelated, since she wasn't even on anticoagulation yet. It didn't change anything about the plan; we finalized the discharge summary without a firm start plan, just a note to follow up as an outpatient.

Interviewer: Let's slow down and go through each of those moments. At the first point, right after diagnosis — what stood out to you most?

Participant: Honestly, the fall. Clinically I knew the scores favored treatment, but a recent fall in an older patient just registers as a flag. I didn't want to be the one who started a blood thinner and then she fell again and bled into her head.

Interviewer: What alternatives did you consider there?

Participant: We could have started the DOAC immediately since the scores supported it, or started a lower empirical dose. I chose to wait for a formal PT evaluation instead, even though the fall itself had already been worked up and looked mechanical.

Interviewer: What was the main basis for waiting rather than starting treatment that day?

Participant: I suppose not wanting to be the direct cause of a bad outcome. Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number.

Interviewer: At the second point, with the daughter's anxiety and the CT — what were you trying to accomplish?

Participant: Mostly to de-escalate the family's fear so we could have a productive conversation. In hindsight, I could have just walked through her individual numbers with the daughter instead of ordering imaging that wasn't clinically indicated. But it felt like having a normal scan in hand would make the conversation easier.

Interviewer: How much time pressure did you feel making that call?

Participant: Some — we were already tight on discharge planning, and adding a CT meant another day. But I felt like skipping that step would leave the family conversation unresolved.

Interviewer: Move to the third point — after the CT came back normal and fall risk was cleared. What was going through your mind there?

Participant: That's the one I keep coming back to. The data at that point was pretty clean — low fall risk, normal imaging, scores favoring treatment. But I remember describing to the resident, almost involuntarily, this scenario of her bleeding on a drug I'd started, and picturing it as something that wouldn't really fade — like it would color how the family saw us and how I thought about the case for a long stretch afterward. It wasn't really about the probability anymore. I decided to leave it for the outpatient team.

Interviewer: What alternatives were on the table then?

Participant: Starting it right there before discharge, starting a lower dose with a firm two-week follow-up, or deferring entirely, which is what I did.

Interviewer: Had you handled a similar case before that shaped this decision?

Participant: Not directly with this patient, but the ward story about the other patient's bleed was fresh in everyone's mind that week.

Interviewer: At the fourth point, the bruise at discharge — how did that factor in?

Participant: It didn't really change the clinical picture, since she wasn't even on the medication yet. We noted it and moved on. We sent her out with a follow-up appointment that ended up being three weeks out, later than the two-week window we'd wanted.

Interviewer: If the fall-risk assessment had come back before your first decision instead of after, would you have decided differently?

Participant: Probably, yes. If I'd had that clearance up front, I likely would have started treatment on day one instead of waiting.

Interviewer: If the other patient's bleeding event had never come up on the ward, do you think this admission would have gone differently?

Participant: It's hard to say for certain, but I think the family conversation would have been calmer.

Interviewer: Looking back, what would you tell a colleague facing a similar case?

Participant: I'd say make sure the fall workup happens early, not as an afterthought, and try to separate the family's emotional reaction from the actual numbers in front of you. It's easy to let the picture of a bad outcome sit with you well past the moment, even when the data has already shifted.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HC_Biased_2",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Attending Physician, Hospital Internal Medicine Service",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Deferred Anticoagulant: A Fall, A Rumor, and a Discharge Deadline",
    "scenario_summary_internal": "A hospital internal medicine attending manages a 78-year-old inpatient newly diagnosed with persistent atrial fibrillation who has a recent minor fall history. Over a four-day admission, the attending must decide whether and when to start stroke-prevention anticoagulation, while a ward rumor about another patient's fatal bleed and an anxious family member's fears complicate the decision landscape. The case is designed so that the physician's early reluctance to actively prescribe (favoring the status quo) and a later moment of vivid imagined-regret about a hypothetical bleeding event both shape decisions in ways that are not fully justified by the actual clinical risk-benefit numbers, without the interview ever naming these tendencies.",
    "occupational_realism": {
      "objective": "Decide, across a single hospital admission, whether and when to initiate stroke-prevention anticoagulation for a patient with new persistent atrial fibrillation, balancing stroke risk reduction against bleeding and fall risk under discharge time pressure.",
      "setting": "General medicine inpatient ward of a mid-sized teaching hospital, four-day admission, with a discharge-planning deadline and periodic input from a covering resident, a pharmacist, and the patient's daughter.",
      "constraints": [
        "CHA2DS2-VASc score indicates high annual stroke risk if untreated",
        "HAS-BLED score indicates only moderate bleeding risk, not a formal contraindication",
        "Patient had one mechanical, non-injurious fall three weeks prior to admission",
        "Limited outpatient follow-up availability within two weeks of discharge",
        "A different patient on the same ward experienced a fatal bleed on anticoagulation the previous month, which staff and family have heard about informally",
        "Discharge planning timeline compresses the decision window to under 48 hours",
        "Daughter present and vocal about wanting to avoid any bleeding risk"
      ],
      "stakeholders": [
        "Attending physician (interviewee)",
        "Covering internal medicine resident",
        "Clinical pharmacist",
        "Patient (78-year-old with new atrial fibrillation)",
        "Patient's daughter (primary family contact)",
        "Discharge planning nurse"
      ],
      "technical_terms_to_use": [
        "CHA2DS2-VASc score",
        "HAS-BLED score",
        "direct oral anticoagulant (DOAC)",
        "warfarin",
        "INR",
        "fall risk assessment",
        "shared decision-making",
        "number needed to treat/harm",
        "bridging therapy",
        "discharge summary"
      ],
      "technical_terms_to_avoid": [
        "impact bias",
        "omission bias",
        "affective forecasting",
        "action-inaction asymmetry",
        "cognitive bias",
        "anticipated regret",
        "durability bias",
        "status quo bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "New diagnosis of persistent atrial fibrillation on admission ECG",
          "CHA2DS2-VASc score of 4 (high annual stroke risk)",
          "HAS-BLED score of 2 (moderate bleeding risk, no active contraindication)",
          "One mechanical, non-injurious fall three weeks earlier, fully worked up as due to a loose rug",
          "No history of prior bleeding events",
          "Pharmacist confirms no drug interactions with candidate DOAC"
        ],
        "new_information_after_decision": [
          "Physical therapy consult later confirms patient's fall risk is low with a walker",
          "Resident notes stroke risk reduction from anticoagulation substantially outweighs bleeding risk in the calculated scores"
        ],
        "alternatives": [
          "Start a DOAC immediately per guideline-concordant risk scores",
          "Defer any anticoagulation decision until after a formal physical therapy fall-risk evaluation",
          "Start a reduced empirical dose pending further workup"
        ],
        "intended_action": "The attending defers starting anticoagulation, citing the recent fall as the deciding factor, and frames withholding treatment as the 'safer, do-no-harm' choice, even though the resident's summary shows the untreated stroke risk is higher than the treatment-associated bleeding risk."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Nursing staff mention that a patient on the same floor died last month from a major gastrointestinal bleed while on anticoagulation",
          "Daughter has heard this story secondhand and is visibly anxious",
          "Patient has no signs of active bleeding or new neurological symptoms",
          "Pharmacist reiterates that DOAC-associated major bleed rates are low and mostly manageable"
        ],
        "new_information_after_decision": [
          "Head CT ordered to reassure the family returns normal, adding a day to the admission",
          "Daughter remains anxious despite normal imaging"
        ],
        "alternatives": [
          "Address the family's fear directly with individualized numeric risk data and proceed with the original plan",
          "Order reassurance imaging/testing to manage anxiety without changing the treatment plan",
          "Postpone any further discussion until a scheduled multidisciplinary family meeting"
        ],
        "intended_action": "The attending orders a reassurance head CT primarily to manage family anxiety rather than because of a clinical indication, delaying the anticoagulation conversation by a day."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Normal head CT result",
          "Updated fall-risk assessment showing low risk with assistive device",
          "Quantitative risk data still favor anticoagulation over no treatment",
          "Discharge is now scheduled for the next morning"
        ],
        "new_information_after_decision": [
          "Resident documents the decision in the chart as 'deferred pending outpatient follow-up' without a firm restart date",
          "Discharge planner flags that outpatient follow-up may not occur for three weeks, beyond the two-week target"
        ],
        "alternatives": [
          "Start the DOAC before discharge now that fall risk has been clarified as low",
          "Defer the decision entirely to the outpatient primary care physician",
          "Start a lower dose with a firm two-week follow-up anticoagulation clinic referral"
        ],
        "intended_action": "While discussing the plan with the resident, the attending describes in vivid detail how devastating and lasting it would feel personally and for the family if the patient bled while on the drug they prescribed, and decides to defer the decision to the outpatient team, despite acknowledging the numbers now favor starting treatment."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient develops a small bruise at a routine IV site, unrelated to any anticoagulant since none has been started",
          "Nursing reports this to the team as a routine finding",
          "No anticoagulation has yet been given",
          "Discharge is proceeding within hours"
        ],
        "new_information_after_decision": [
          "Discharge summary is finalized without a firm anticoagulation start plan",
          "Outpatient appointment confirmed for three weeks out, beyond the original two-week target"
        ],
        "alternatives": [
          "Recognize the bruise as unrelated to anticoagulation and proceed with starting a DOAC before discharge",
          "Treat the bruise as a reason for additional caution and finalize the deferral to outpatient follow-up",
          "Start a reduced dose with explicit safety-netting instructions and an earlier follow-up date"
        ],
        "intended_action": "The attending finalizes discharge without starting anticoagulation, citing the bruise as reinforcing the wisdom of waiting, and hands off the decision to outpatient care with a vague follow-up plan."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role on the team during this admission?",
        "What was your overall goal for this patient's care during the hospitalization?"
      ],
      "timeline_reconstruction": [
        "Take me through what happened, in order, from the atrial fibrillation diagnosis to discharge.",
        "What did you know at each point, and when did new information arrive?"
      ],
      "decision_point_probes": [
        "What cues or findings stood out to you most at that moment?",
        "What information sources did you rely on to make that call?",
        "What were you trying to achieve or avoid with that decision?",
        "What other options did you consider, and why did you rule them out?",
        "What was the main basis for the choice you made?",
        "Had you handled a similar situation before, and did that experience shape this decision?",
        "How much time pressure did you feel at that point?",
        "How confident were you in the information you had?",
        "If one piece of information had been different, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If the fall risk assessment had come back before your first decision instead of after, what would you have done differently?",
        "If the other patient's bleeding event had never been mentioned on the ward, do you think the outcome here would have changed?",
        "Looking back, what would you tell a colleague facing a similar case?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "om_01",
        "bias": "Omission Bias",
        "decision_point": 1,
        "mechanism": "Preferring inaction (withholding anticoagulation) over action (prescribing) because harm resulting from the act of treating is judged more blameworthy than equivalent or greater harm resulting from withholding treatment, even when the quantitative risk data favor acting.",
        "affected_reasoning_operation": "Risk-benefit weighting and treatment-initiation choice at time of diagnosis",
        "evidence_available_at_time": [
          "CHA2DS2-VASc score of 4 indicating high stroke risk",
          "HAS-BLED score of 2 indicating only moderate bleeding risk",
          "Recent non-injurious mechanical fall with a clear alternative explanation",
          "Pharmacist confirmation of no interaction contraindications"
        ],
        "required_textual_manifestation": "The attending explicitly frames not starting the drug as the 'safe, do-no-harm' choice and justifies deferral mainly by the fall, despite acknowledging the resident's risk-score comparison favors treatment.",
        "plausible_nonbias_interpretation": "A cautious clinician reasonably wants a formal fall-risk workup before starting a bleeding-risk medication in an older patient.",
        "strength": "subtle",
        "do_not_make_explicit": ["omission bias", "status quo bias", "action-inaction asymmetry"]
      },
      {
        "instance_id": "im_01",
        "bias": "Impact Bias",
        "decision_point": 3,
        "mechanism": "Overestimating the intensity and durability of the emotional impact of a hypothetical future bleeding event (on self and family) relative to its actual expected impact, causing this imagined emotional consequence to outweigh the updated quantitative risk data.",
        "affected_reasoning_operation": "Final pre-discharge treatment decision and forecasting of future emotional consequences of a hypothetical adverse event",
        "evidence_available_at_time": [
          "Normal head CT and clarified low fall risk with assistive device",
          "Quantitative data now favoring anticoagulation over no treatment",
          "Awareness of a recent, salient bleeding death on the same ward",
          "Discharge timeline pressure"
        ],
        "required_textual_manifestation": "The attending vividly describes how devastating and long-lasting the emotional aftermath of a bleed would feel for themselves and the family, and this imagined future feeling, not the updated numbers, drives the deferral decision.",
        "plausible_nonbias_interpretation": "A physician reasonably wants to align a life-altering treatment decision with patient and family values and comfort before committing.",
        "strength": "subtle",
        "do_not_make_explicit": ["impact bias", "affective forecasting", "durability bias", "anticipated regret"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, no paired control scenario supplied."
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
      "Confirm exactly four decision points are present, each with at least two explicit alternatives.",
      "Confirm om_01 appears only at decision point 1 and im_01 only at decision point 3, with no repetition elsewhere.",
      "Confirm neither 'omission bias' nor 'impact bias' nor any synonym/psychological label appears anywhere in the interview text.",
      "Confirm decision points 2 and 4 contain no intentionally embedded instances of either named bias.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals for each decision point.",
      "Confirm final word count falls between 1,215 and 1,485 words.",
      "Confirm consequences described (normal CT, unrelated bruise, delayed follow-up) do not mechanically prove either decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Impact Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overestimation of the intensity/duration of imagined future emotional impact of a hypothetical bleeding event, not as a general fear statement."
      },
      {
        "bias": "Omission Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as explicit preference for inaction over action based on differential blame attribution, not as a generic caution statement."
      }
    ],
    "target_bias_names": ["Impact Bias", "Omission Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Impact Bias", "requested_occurrences": 1},
      {"bias": "Omission Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "om_01", "bias": "Omission Bias"},
      {"instance_id": "im_01", "bias": "Impact Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "om_01", "bias": "Omission Bias", "decision_point": 1},
      {"instance_id": "im_01", "bias": "Impact Bias", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "om_01",
        "bias": "Omission Bias",
        "mechanism": "Judging harm from action (prescribing anticoagulant) as more blameworthy than equivalent or greater harm from inaction (withholding), leading to deferral despite risk scores favoring treatment.",
        "affected_reasoning_operation": "Risk-benefit weighting and treatment-initiation choice at diagnosis",
        "evidence_source": "CHA2DS2-VASc/HAS-BLED scores and resident's risk comparison presented at decision point 1",
        "distinctiveness_requirement": "Must be tied to the initial diagnosis-stage decision and framed around act-vs-omission blame, distinct from im_01's forward-looking emotional forecasting at decision point 3."
      },
      {
        "instance_id": "im_01",
        "bias": "Impact Bias",
        "mechanism": "Overestimating the intensity and duration of imagined future emotional distress from a hypothetical bleeding event, causing this forecast to override updated quantitative risk data.",
        "affected_reasoning_operation": "Final pre-discharge treatment decision and prediction of future emotional consequences",
        "evidence_source": "Updated normal CT and fall-risk clarification plus recollection of the ward bleeding death, presented at decision point 3",
        "distinctiveness_requirement": "Must be tied to the discharge-stage decision and framed around vivid imagined future emotional impact, distinct from om_01's initial act-vs-omission blame framing."
      }
    ],
    "intended_strength": [
      {"instance_id": "om_01", "bias": "Omission Bias", "strength": "subtle"},
      {"instance_id": "im_01", "bias": "Impact Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Biased_2",
    "domain_id": "HC",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias assigned to a distinct decision point (Omission Bias at decision point 1, Impact Bias at decision point 3) selected for best mechanism fit and narrative realism; no decision point received more than one instance of any single bias; decision points 2 and 4 held neutral to avoid unintended bias concentration.",
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
        "segment_type": "care_goal",
        "raw_interview_anchor": "Mainly to get her diagnosis sorted out and make sure we sent her home with a safe, appropriate plan.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States the overall care objective without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_risk_assessment",
        "raw_interview_anchor": "Her CHA2DS2-VASc came out to 4... Her HAS-BLED was 2, which is moderate, not a red flag. Pharmacy checked and there were no interactions with the DOAC we'd typically use.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Accurately summarizes available quantitative risk and medication-interaction information."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "initial_treatment_deferral",
        "raw_interview_anchor": "Still, when I saw \"fall\" in the history, that gave me pause about starting a blood thinner right away... we'd hold off and get a formal fall-risk assessment first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Describes a clinically plausible precaution based on a recent fall but does not independently contain the required explicit act-versus-omission blame framing."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "family_reassurance_decision",
        "raw_interview_anchor": "Clinically nothing had changed... but I ended up ordering a head CT partly to have something concrete to reassure her with.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explains an anxiety-management and communication choice; no hidden target instance is assigned to this episode."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "updated_objective_assessment",
        "raw_interview_anchor": "By day three the CT was normal, and physical therapy had cleared her fall risk as low with a walker. So on paper the numbers were now clearly in favor of starting treatment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Records the updated evidence and its implication without the subsequent emotional forecast."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "final_emotional_forecast_and_deferral",
        "raw_interview_anchor": "I remember standing at the nurses' station... picturing what it would be like if we started her on this drug and then she had a major bleed... It felt like the kind of thing I'd still be replaying weeks later... That feeling seemed heavier to carry than just not starting it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "im_01"
        ],
        "ground_truth_rationale": "Contains the vivid forecast of intense and durable emotional consequences from a hypothetical bleed overriding the updated quantitative evidence."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "discharge_bruise_assessment",
        "raw_interview_anchor": "It didn't change anything about the plan; we finalized the discharge summary without a firm start plan.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly treats the bruise as unrelated and non-decisive."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "first_point_cue_assessment",
        "raw_interview_anchor": "Clinically I knew the scores favored treatment, but a recent fall in an older patient just registers as a flag.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Describes salience of the fall but does not by itself state differential blame for action versus inaction."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "first_point_alternatives",
        "raw_interview_anchor": "We could have started the DOAC immediately... or started a lower empirical dose. I chose to wait for a formal PT evaluation instead.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Lists alternatives and the selected precaution; the explicit blame-based rationale appears in the following segment."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "first_point_decision_basis",
        "raw_interview_anchor": "I suppose not wanting to be the direct cause of a bad outcome. Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "om_01"
        ],
        "ground_truth_rationale": "Explicitly prefers withholding because prescribing would make the physician the direct cause of harm, despite recognizing that treatment had the larger numerical benefit."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "family_conversation_goal",
        "raw_interview_anchor": "Mostly to de-escalate the family's fear so we could have a productive conversation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States a communication goal without a target bias manifestation."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "time_pressure_assessment",
        "raw_interview_anchor": "We were already tight on discharge planning, and adding a CT meant another day. But I felt like skipping that step would leave the family conversation unresolved.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explains perceived communication pressure and does not instantiate either hidden target mechanism."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "third_point_reflection",
        "raw_interview_anchor": "The data at that point was pretty clean... I remember describing... this scenario of her bleeding on a drug I'd started... something that wouldn't really fade... It wasn't really about the probability anymore.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Corroborates the already mapped day-three instance but is not treated as a separate hidden occurrence."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "third_point_alternatives",
        "raw_interview_anchor": "Starting it right there before discharge, starting a lower dose with a firm two-week follow-up, or deferring entirely, which is what I did.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Lists alternatives and the choice without independently adding a new hidden instance."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "prior_experience_context",
        "raw_interview_anchor": "The ward story about the other patient's bleed was fresh in everyone's mind that week.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Provides contextual salience that supports a candidate availability interpretation but does not explicitly establish that mechanism."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "bruise_decision_context",
        "raw_interview_anchor": "It didn't really change the clinical picture, since she wasn't even on the medication yet. We noted it and moved on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly rejects the bruise as causally relevant."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "follow_up_constraint",
        "raw_interview_anchor": "We sent her out with a follow-up appointment that ended up being three weeks out, later than the two-week window we'd wanted.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States an operational consequence and follow-up constraint."
      },
      {
        "segment_id": "seg_018",
        "speaker": "Participant",
        "segment_type": "counterfactual_first_decision",
        "raw_interview_anchor": "If I'd had that clearance up front, I likely would have started treatment on day one instead of waiting.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Counterfactual reflection about timing of information; it does not add a new hidden occurrence."
      },
      {
        "segment_id": "seg_019",
        "speaker": "Participant",
        "segment_type": "counterfactual_family_effect",
        "raw_interview_anchor": "If the other patient's bleeding event had never come up on the ward... I think the family conversation would have been calmer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Counterfactual communication reflection without a direct bias manifestation."
      },
      {
        "segment_id": "seg_020",
        "speaker": "Participant",
        "segment_type": "closing_debiasing_advice",
        "raw_interview_anchor": "Make sure the fall workup happens early... try to separate the family's emotional reaction from the actual numbers... It's easy to let the picture of a bad outcome sit with you well past the moment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective advice and debiasing reflection rather than a new decision-time instance."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
