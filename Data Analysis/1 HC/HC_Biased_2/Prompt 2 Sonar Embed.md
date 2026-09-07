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

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis is limited to the supplied interview transcript. No retrieved scientific-paper corpus was provided in the input, so bias definitions and mechanisms rely on the reference-ontology labels and the interview evidence rather than on supplied paper support."
  },
  "identified_bias_summary": [
    {
      "canonical_bias_name": "Affect Heurisitic",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Information bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Omission bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 2
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Omission bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Preference for inaction or withholding an intervention because harmful commissions are judged as worse or more blameworthy than harmful omissions, even when omission carries comparable or greater risk.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial anticoagulation decision after atrial fibrillation diagnosis and fall history",
      "decision_point_description": "Day 1 choice to start a DOAC immediately, start a lower empirical dose, or withhold anticoagulation pending formal fall-risk assessment.",
      "affected_reasoning_operation": "Treatment initiation decision for stroke prevention",
      "bias_specific_mechanism": "The participant framed starting anticoagulation as being the direct cause of a possible bleed and treated that as more aversive than omitting anticoagulation despite the resident noting the stroke-risk reduction was larger.",
      "manifestation_in_interview": "The participant explicitly reported not wanting to be the direct cause of a bad outcome and described withholding as the more conservative option, even while acknowledging the stroke-risk reduction favored treatment.",
      "effect_on_reasoning_or_decision": "Immediate anticoagulation was withheld in favor of waiting for a formal fall-risk assessment, delaying evidence-based stroke prevention.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't want to be the one who started a blood thinner and then she fell again and bled into her head.",
          "evidence_explanation": "This directly expresses a preference to avoid being the causal agent of a harmful commission, a core omission-bias mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I suppose not wanting to be the direct cause of a bad outcome. Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number.",
          "evidence_explanation": "The participant contrasts withholding with starting the drug and chooses withholding despite acknowledging the quantitative risk-benefit case for stroke prevention."
        }
      ],
      "correction_or_counterevidence": "The recent fall was clinically relevant and a formal fall-risk assessment was still pending; the resident had pointed out that stroke-risk reduction was the larger effect.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the task context, so this occurrence could not be corroborated with retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Judgments of probability, risk, or salience are influenced by how easily examples, especially recent or vivid ones, come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final anticoagulation deferral after recent ward bleed story",
      "decision_point_description": "Decision to start anticoagulation before discharge, start at a lower dose with close follow-up, or defer entirely to outpatient management after CT and PT clearance.",
      "affected_reasoning_operation": "Risk perception and treatment decision about anticoagulation",
      "bias_specific_mechanism": "A recent, vivid nearby patient death from anticoagulant-related GI bleeding remained easy to recall and made bleeding harm disproportionately salient, even after objective bleeding-risk workup was reassuring.",
      "manifestation_in_interview": "The participant stated that the ward story about the other patient's bleed was fresh in everyone's mind and linked that story to the decision context, despite clean clinical data.",
      "effect_on_reasoning_or_decision": "The readily available bleeding example contributed to deferring anticoagulation rather than revising the plan after normal CT and low fall-risk clearance.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation.",
          "evidence_explanation": "This establishes that a highly vivid and recent bleeding complication was available in the unit's collective memory."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly with this patient, but the ward story about the other patient's bleed was fresh in everyone's mind that week.",
          "evidence_explanation": "The participant explicitly reports that the recent story was cognitively salient and shaped the case context."
        }
      ],
      "correction_or_counterevidence": "The head CT was normal, physical therapy cleared low fall risk, and the participant acknowledged the numbers clearly favored starting treatment.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the task context, so this occurrence could not be corroborated with retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Information bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Seeking additional information or testing even when it is not needed to inform the decision, often because it provides reassurance or reduces discomfort.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day 2 response to family anxiety about anticoagulation",
      "decision_point_description": "Decision whether to order a head CT, despite no clinical indication, to provide concrete reassurance and facilitate the family conversation.",
      "affected_reasoning_operation": "Diagnostic imaging decision",
      "bias_specific_mechanism": "The participant ordered a non-indicated head CT to have a concrete normal result to reduce family anxiety, rather than because the test was needed to guide diagnosis or management.",
      "manifestation_in_interview": "The participant stated that the CT was not really indicated but was ordered partly to reassure the daughter and make the conversation easier.",
      "effect_on_reasoning_or_decision": "The admission was extended by a day for imaging that was not clinically required, changing the discharge timeline.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated.",
          "evidence_explanation": "This shows the imaging was ordered for reassurance rather than clinical necessity, consistent with information bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But it felt like having a normal scan in hand would make the conversation easier.",
          "evidence_explanation": "This further confirms that the expected informational value of the test was emotional and conversational rather than diagnostic."
        }
      ],
      "correction_or_counterevidence": "The participant reflected that walking through the patient's individual numbers might have replaced the non-indicated imaging.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the task context, so this occurrence could not be corroborated with retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Affect Heurisitic",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Mental shortcut in which an emotionally charged image or feeling about an outcome guides judgment and decision-making, overriding more analytic probability-based reasoning.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final anticoagulation decision at the nurses' station",
      "decision_point_description": "Decision to start anticoagulation before discharge, start at a lower dose with close follow-up, or defer entirely to the outpatient team after normal CT and low fall-risk clearance.",
      "affected_reasoning_operation": "Risk-benefit judgment and anticoagulation treatment choice",
      "bias_specific_mechanism": "The participant's vivid mental image of a major bleed, the family conversation, and lasting team distress produced a negative affective response that outweighed the objective risk-benefit data favoring anticoagulation.",
      "manifestation_in_interview": "The participant described picturing the bleed scenario and stated that the feeling seemed heavier to carry than just not starting the drug, and that it was no longer really about probability.",
      "effect_on_reasoning_or_decision": "Anticoagulation was deferred to the outpatient team despite low fall risk, normal CT, and scores favoring treatment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember standing at the nurses' station with the resident and just picturing what it would be like if we started her on this drug and then she had a major bleed — the conversation with the daughter, explaining that decision, how that would sit with all of us.",
          "evidence_explanation": "This shows an emotionally vivid imagined scenario becoming central to the decision process."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That feeling seemed heavier to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge.",
          "evidence_explanation": "This directly links the affective weight of the imagined bleed to the choice to defer treatment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It wasn't really about the probability anymore.",
          "evidence_explanation": "This explicitly states that affective evaluation displaced probabilistic risk-benefit reasoning."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that the data were pretty clean, with low fall risk, normal imaging, and scores favoring treatment, but the affective scenario still guided the decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the task context, so this occurrence could not be corroborated with retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Omission bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Preference for inaction or deferral because harmful commissions are judged as worse or more culpable than harmful omissions, even when omission creates comparable risk.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final anticoagulation decision after normal CT and PT clearance",
      "decision_point_description": "Decision to start anticoagulation before discharge, start at a lower dose with close follow-up, or defer entirely to outpatient management.",
      "affected_reasoning_operation": "Anticoagulation treatment choice",
      "bias_specific_mechanism": "The participant treated the possibility of causing bleeding by acting as more aversive than the risk of stroke from deferring, and therefore preferred the omission pathway of letting the outpatient team start treatment later.",
      "manifestation_in_interview": "The participant described the feeling of causing a bleed as heavier to carry than just not starting the drug and chose to defer, even though objective data favored starting anticoagulation.",
      "effect_on_reasoning_or_decision": "The patient was discharged without a firm inpatient anticoagulation start plan, despite low fall risk, normal CT, and scores favoring treatment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That feeling seemed heavier to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge.",
          "evidence_explanation": "This directly contrasts the feared commission of starting the drug with the preferred omission of not starting it, even after risk-benefit data shifted toward treatment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The data at that point was pretty clean — low fall risk, normal imaging, scores favoring treatment. But I remember describing to the resident, almost involuntarily, this scenario of her bleeding on a drug I'd started.",
          "evidence_explanation": "This shows the decision favored omission despite acknowledging the objective data favored action."
        }
      ],
      "correction_or_counterevidence": "The resident had earlier pointed out that stroke-risk reduction was the bigger number; PT cleared low fall risk and CT was normal, yet the participant deferred.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the task context, so this occurrence could not be corroborated with retrieved corpus support.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_name": "Impact Bias",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final anticoagulation deferral after normal CT and PT clearance",
      "supporting_interview_quote": "it felt like the kind of thing I'd still be replaying weeks later, something that would sit over the whole team and not really lift for a long time.",
      "plausible_mechanism": "The participant may have overestimated the duration and intensity of future negative affect following a possible bleed, making the feared outcome feel especially heavy.",
      "why_not_identified": "The interview does not provide evidence that this affective forecast was inaccurate or that a distinct overestimation mechanism, separate from the affect heuristic and omission preference, drove the decision."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_name": "Conservatism Bias",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final anticoagulation decision after fall-risk clearance and normal CT",
      "supporting_interview_quote": "The data at that point was pretty clean — low fall risk, normal imaging, scores favoring treatment. But I remember describing to the resident, almost involuntarily, this scenario of her bleeding on a drug I'd started.",
      "plausible_mechanism": "The participant may have insufficiently revised the initial withholding plan despite new evidence that favored starting anticoagulation.",
      "why_not_identified": "The participant's own explanation emphasizes affective and omission-based mechanisms rather than underweighting of new evidence, so conservatism is not affirmatively established as a separate mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper corpus was supplied in the user input, so retrieved_corpus_support_used is false and all corpus_evidence arrays are empty. Bias labels and definitions rely on the reference-ontology names and interview evidence rather than supplied paper support.",
    "The analysis is based on one participant's retrospective account, so it cannot independently verify recalled reasoning or exclude self-justification and social-desirability effects.",
    "The final anticoagulation deferral episode contains overlapping evidence for availability, affect, and omission mechanisms; they are reported separately only because distinct bias-specific mechanisms are described."
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
