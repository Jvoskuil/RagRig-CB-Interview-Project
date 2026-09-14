You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analyzed the interview transcript only for affirmative evidence of bias-specific mechanisms. No retrieved corpus passages were supplied, so labels and definitions rely on general cognitive-science knowledge rather than retrieval. No experimental condition or intended bias count was assumed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Omission bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Omission bias",
      "alternative_labels": ["Action-omission bias", "Anticipated regret", "Regret aversion"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge harmful outcomes caused by action as worse or more blameworthy than equally harmful outcomes caused by inaction, leading to a preference for omission even when active intervention is probabilistically net beneficial.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to withhold/defer anticoagulation despite stroke-risk data favoring treatment",
      "decision_point_description": "The participant initially withheld anticoagulation on day 1 pending fall-risk assessment and then, after day 3 clearance, decided to defer anticoagulation to the outpatient team rather than start it before discharge.",
      "affected_reasoning_operation": "Risk-benefit evaluation and selection of stroke-prevention treatment",
      "bias_specific_mechanism": "The participant weighed the harm of an action-caused bleed more heavily than the harm of an omission-caused stroke. Anticipated regret and blame for a bleeding event from a medication he started made withholding feel safer and more acceptable, even after objective data favored treatment.",
      "manifestation_in_interview": "The participant said he did not want to be the direct cause of a bleed, described withholding as the more conservative option despite knowing the stroke-risk reduction was larger, and reported that the anticipated emotional weight of a possible bleed was heavier than simply not starting the drug, leading to deferral.",
      "effect_on_reasoning_or_decision": "Anticoagulation was delayed and ultimately deferred to outpatient follow-up, although the participant acknowledged that CHA2DS2-VASc, HAS-BLED, normal CT, and low fall-risk clearance favored starting treatment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But she'd had a fall about three weeks before admission — mechanical, tripped on a rug at home, no head strike, no fracture, fully worked up at the time. Still, when I saw 'fall' in the history, that gave me pause about starting a blood thinner right away. I told the team we'd hold off and get a formal fall-risk assessment first before committing to anything.",
          "evidence_explanation": "Shows the initial choice to withhold an active intervention and defer to later assessment, with the feared bleed from action framing the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't want to be the one who started a blood thinner and then she fell again and bled into her head.",
          "evidence_explanation": "Directly expresses the action-related harm and blame concern central to omission bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number.",
          "evidence_explanation": "Shows the participant favored inaction despite acknowledging that the numerical benefit of active treatment was larger."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That feeling seemed heavier to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge.",
          "evidence_explanation": "Demonstrates that anticipated emotional/regret weight of an action-caused bleed drove the final decision to withhold."
        }
      ],
      "correction_or_counterevidence": "The resident noted that the stroke-risk reduction was the larger number, and the participant acknowledged that the day-3 data were clean: normal CT, low fall risk, and scores favoring treatment. These did not shift the final omission decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the named label and mechanism rest on general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias", "Salience bias", "Affect heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the probability or importance of an event by the ease with which examples or vivid mental images come to mind, rather than by objective base rates or clinical risk scores.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Influence of a recent ward bleeding death and vivid bleeding imagery on anticoagulation risk judgment",
      "decision_point_description": "After hearing a salient recent story about another patient's fatal GI bleed on anticoagulation, and after picturing a major bleed in this patient, the participant maintained the decision to defer anticoagulation despite objective clearance.",
      "affected_reasoning_operation": "Probability and risk judgment about bleeding versus stroke prevention",
      "bias_specific_mechanism": "A recent, emotionally charged bleeding-death example was easily available in memory and was reinforced by vivid mental simulation of this patient having a major bleed. The ease and vividness of that imagined bleed made anticoagulation risk feel more salient than the objective risk numbers, leading the participant away from probability-based reasoning.",
      "manifestation_in_interview": "The participant said the ward story was fresh in everyone's mind, described vividly picturing the bleed, and then stated that the decision was no longer about probability although the objective data favored treatment.",
      "effect_on_reasoning_or_decision": "The available bleeding example and vivid simulation contributed to the final decision to withhold anticoagulation, even after normal imaging and low fall-risk clearance.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Then on day two, one of the nurses mentioned, sort of in passing, that a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation. Understandably, that got around the unit, and my patient's daughter had heard a version of it too.",
          "evidence_explanation": "Establishes the recent, salient bleeding-death example that became cognitively available to the participant."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly with this patient, but the ward story about the other patient's bleed was fresh in everyone's mind that week.",
          "evidence_explanation": "Directly links the recent ward example to the decision context, supporting availability-based influence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember standing at the nurses' station with the resident and just picturing what it would be like if we started her on this drug and then she had a major bleed — the conversation with the daughter, explaining that decision, how that would sit with all of us.",
          "evidence_explanation": "Shows the participant generating a vivid, easily imagined negative outcome rather than comparing objective risk magnitudes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It wasn't really about the probability anymore.",
          "evidence_explanation": "Demonstrates that the salient imagined bleed displaced probabilistic clinical reasoning as the basis for the decision."
        }
      ],
      "correction_or_counterevidence": "The participant recognized in hindsight that the data had shifted and that one should separate the family's emotional reaction from the actual numbers. During the admission, however, this recognition did not change the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the named label and mechanism rest on general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Affect heuristic",
      "alternative_labels": ["Emotional reasoning"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision to order a non-indicated head CT to reassure the anxious daughter",
      "supporting_interview_quote": "Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated.",
      "plausible_mechanism": "The daughter's increasing anxiety about anticoagulation may have led the participant to use emotional distress as a proxy for the need for imaging, producing a non-indicated test to reduce affect rather than to change clinical risk assessment.",
      "why_not_identified": "The transcript describes a deliberate, partly non-clinical accommodation to family emotion rather than a clear alteration in the participant's own probability or risk judgment about the CT's value. Without evidence that the participant misjudged the clinical need, this remains plausible but not affirmatively identified as a bias-specific mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided, so labels and definitions are based on general knowledge rather than retrieved scientific support.",
    "The analysis relies on the participant's retrospective self-report; however, the reported reasoning was explicit enough to support the identified mechanisms."
  ]
}

</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HC_Biased_2_Sonnet_off",
  "interview_id": "HC_Biased_2",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
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
