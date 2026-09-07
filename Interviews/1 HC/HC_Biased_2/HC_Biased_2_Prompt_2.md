You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HC_Biased_2",
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
    }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
