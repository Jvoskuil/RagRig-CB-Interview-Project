You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HC_Ambigious_2",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Attending Physician, Hospital Internal Medicine Service",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "The Anticoagulation Judgment Call: Conflicting Signals, No Clear Answer",
    "scenario_summary_internal": "A hospital internal medicine attending manages a 78-year-old inpatient newly diagnosed with persistent atrial fibrillation who has a recent fall history that a formal assessment leaves only partially resolved. Over a four-day admission, the attending must decide whether and when to start stroke-prevention anticoagulation while genuinely conflicting pieces of evidence accumulate: an indeterminate fall-risk score, a clinically relevant question raised by a nearby patient's bleeding complication, and a new finding at discharge that could plausibly bear on bleeding risk. The case mirrors the structure, vocabulary, actors, and emotional tone of a paired anticoagulation-decision scenario, but every decision point is built so that the available evidence and reasonable clinical judgment remain genuinely underdetermined, with no decision point instantiating a specific named cognitive bias.",
    "occupational_realism": {
      "objective": "Decide, across a single hospital admission, whether and when to initiate stroke-prevention anticoagulation for a patient with new persistent atrial fibrillation, balancing stroke risk reduction against bleeding and fall risk under discharge time pressure and genuinely incomplete information.",
      "setting": "General medicine inpatient ward of a mid-sized teaching hospital, four-day admission, with a discharge-planning deadline and periodic input from a covering resident, a pharmacist, and the patient's daughter.",
      "constraints": [
        "CHA2DS2-VASc score indicates high annual stroke risk if untreated",
        "HAS-BLED score indicates moderate bleeding risk, not a formal contraindication",
        "Patient had one fall three weeks prior to admission with a cause that remains only partly explained",
        "Formal fall-risk assessment returns an indeterminate/borderline result rather than a clear low or high classification",
        "Limited outpatient follow-up availability within two weeks of discharge",
        "A different patient on the same ward had a bleeding complication on anticoagulation the previous month, with clinically relevant differences (renal function, concurrent antiplatelet use) that are only partially known",
        "Discharge planning timeline compresses the decision window to under 48 hours",
        "Daughter present and asking pointed, reasonable questions about risk trade-offs"
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
        "discharge summary",
        "renal clearance",
        "platelet count"
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
          "Fall three weeks earlier with an incomplete explanation: patient recalls tripping but also reports brief lightheadedness beforehand that was never worked up",
          "No history of prior bleeding events",
          "Pharmacist confirms no drug interactions with candidate DOAC, but flags that renal function is at the lower end of normal and warrants monitoring"
        ],
        "new_information_after_decision": [
          "Formal fall-risk assessment returns a borderline/moderate score rather than clearly low or high",
          "Cardiology curbside opinion notes that guidance on timing anticoagulation after an unexplained pre-fall symptom is not settled in this population"
        ],
        "alternatives": [
          "Start a DOAC promptly given the stroke-risk score",
          "Defer briefly pending outpatient evaluation of the lightheadedness episode",
          "Start a reduced empirical dose while further workup proceeds"
        ],
        "intended_action": "The attending orders further evaluation of the unexplained pre-fall symptom before committing to a start date, a choice that reasonable clinicians could evaluate differently given the genuinely incomplete history and borderline risk assessment."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Nursing staff mention a nearby patient had a bleeding complication while on anticoagulation the prior month",
          "That patient's renal function and concurrent antiplatelet use are known to differ from this patient's, but the full details are not readily available on the ward",
          "Daughter asks specific, reasonable questions about how this patient's situation compares",
          "Pharmacist notes that without confirming the other patient's exact regimen, a direct comparison is not clinically meaningful"
        ],
        "new_information_after_decision": [
          "Chart review clarifies the other patient had significantly reduced renal clearance and was on a differing dose",
          "Daughter's questions are answered with patient-specific numbers, though she remains understandably cautious"
        ],
        "alternatives": [
          "Look up the comparator patient's chart details before responding to the family's questions",
          "Answer using only this patient's individualized risk data without referencing the other case",
          "Defer the conversation until the multidisciplinary team can address it together"
        ],
        "intended_action": "The attending requests the comparator patient's relevant chart details before finalizing the family conversation, a reasonable step given real informational gaps, though it also adds a day to the timeline."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Comparator patient's differing renal function and antiplatelet use are now documented",
          "This patient's fall-risk assessment remains borderline rather than clearly resolved",
          "CHA2DS2-VASc and HAS-BLED scores are unchanged and still numerically favor treatment",
          "Discharge is now scheduled for the next morning"
        ],
        "new_information_after_decision": [
          "Resident documents that the team considered starting therapy but wanted one more renal function check first",
          "Discharge planner flags that outpatient follow-up may occur three weeks out rather than the intended two"
        ],
        "alternatives": [
          "Start the DOAC before discharge given the unchanged favorable risk scores",
          "Obtain one additional renal function check before finalizing the dose and timing",
          "Defer the entire decision to the outpatient primary care physician"
        ],
        "intended_action": "The attending opts to obtain one more renal function check before finalizing dosing, a decision that could reflect appropriate dose-safety diligence or, alternatively, an avoidable extra step, without the interview resolving which interpretation is correct."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient develops a small bruise at a site where a blood draw was recently performed",
          "The patient is not yet on anticoagulation",
          "The renal function check from decision point 3 has not yet resulted",
          "Discharge is proceeding within hours"
        ],
        "new_information_after_decision": [
          "Renal function ultimately resolves as adequate for standard dosing, though this returns after discharge",
          "Discharge summary is finalized with a plan to start treatment at the outpatient follow-up in three weeks"
        ],
        "alternatives": [
          "Proceed with discharge as planned and note the bruise for outpatient awareness",
          "Delay discharge to obtain the pending renal result before finalizing any plan",
          "Start a reduced dose immediately with explicit safety-netting instructions"
        ],
        "intended_action": "The attending finalizes discharge without starting treatment, citing the still-pending renal result as the reason, a decision that is consistent with either careful diligence or an avoidable delay depending on how one weighs the already-available risk data."
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
        "If the fall-risk assessment had come back clearly low instead of borderline, what would you have done differently?",
        "If the comparator patient's chart details had been available immediately, do you think the outcome here would have changed?",
        "Looking back, what would you tell a colleague facing a similar case?"
      ]}}

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
