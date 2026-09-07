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
Interviewer: Thanks for making time for this. Just to confirm, this conversation is for our internal review of discharge planning practices, it's confidential, and you can skip anything you're not comfortable discussing. Can you tell me your role and how long you've been doing discharge planning?

Participant: Sure. I'm a social worker on the internal medicine unit, I've been doing discharge planning for about six years now. I work with a pretty steady caseload, usually eight to twelve active patients at a time.

Interviewer: Great. I'd like to walk through a specific case — the one involving Mr. Hoffmann. Can you give me the general shape of what happened?

Participant: Yeah, this was a Thursday-into-Friday case, which already tells you something because bed management wants those rooms turned over by Friday noon if at all possible. Mr. Hoffmann is seventy-eight, came in after a fall at home, and he's got COPD on top of that. He lives alone. His daughter's about two hours away, so she's not a daily presence. My job was to figure out, does he go home with some outpatient support, or does he need a short-term rehab stay first. The tricky part was time — we had maybe a day and a half to sort it out before the bed pressure really kicked in.

Interviewer: What was the referral information you had going in?

Participant: The ED note said he ambulates independently with a cane and lives alone. That's a pretty common profile for us, so I had a sense of where this was probably headed. I went and talked to him myself before PT had even gotten to him — just a short bedside conversation, maybe ten minutes. He was alert, joking around a little, said he was "fine, just tripped on a rug." Honestly, within that conversation I felt like I had a good read on him. You develop an instinct for who's steady and who isn't, and my instinct said steady.

Interviewer: What happened after that first conversation?

Participant: PT saw him later that day. Their formal numbers showed slower gait speed and weaker grip strength than what the ED note suggested. And nursing flagged two near-falls overnight, unwitnessed, so we don't know exactly what happened, but he was found close to the bed rail both times. I noted that, but at that point I'd already sort of built my plan around the independent-living picture, so those things registered more as things to keep an eye on rather than something that should make me start over.

Interviewer: Let's slow down on that moment. What were you weighing when you formed that initial impression?

Participant: Mostly the ED documentation, since that's the first thing I see, and then my own impression from talking to him. He was sharp, engaged, using the cane fine getting to the bathroom with the nurse. I remember feeling pretty confident, actually — like, within a few minutes of talking to him I felt I had him pegged as someone who could probably manage independently.

Interviewer: And when the near-fall notes came in overnight, did that change your read?

Participant: Not dramatically, no. I read it more as an overnight fluke — new environment, maybe he got tangled in the call light cord, that kind of thing. The original picture, ambulates independently with a cane, that was still sort of my anchor point for how I was thinking about him. I did mention the near-falls in my note, but I framed the plan around the baseline description rather than treating the new information as something that should reset my assessment.

Interviewer: Moving to the next stage — figuring out the discharge destination itself. What information did you have about the daughter's ability to help?

Participant: Early on, I called her, and she said she wants to help however she can. That was basically it at that point — no specific days, no specifics on her schedule. But from that, plus the fact he'd gone home successfully after two previous admissions, I moved forward planning for home with outpatient services.

Interviewer: What did your follow-up conversations with her and with home care focus on?

Participant: Honestly, mostly logistics — when could services start, what days would work best for a home health aide, whether she could be there for the first visit. I was asking more "how do we make this work" than "can this actually work." In hindsight, I didn't really ask her directly whether she could commit to a regular schedule until later.

Interviewer: What made you interpret her comment that way initially?

Participant: I think it's just — in my experience, families usually do step up more than the first phone call suggests. That's usually how it goes. People say vague things on a first call because they're stressed, and then it works out once services are in place. So I took her willingness at face value as enough to build around.

Interviewer: Did that assumption hold up?

Participant: Not entirely. A follow-up call later revealed she can only visit twice a week and works full-time. And the home care agency flagged that weekend coverage wasn't guaranteed. Neither of those was shocking exactly, but it did mean the coverage picture was thinner than what I'd been planning around.

Interviewer: Let's go to the chart review and risk assessment. Walk me through that.

Participant: His chart showed two hospitalizations in the past year, both discharged home fine. No documented falls-at-home readmission for him specifically. But — and this is what really stuck with me — I'd personally handled a case last month, a patient with a pretty similar profile, who was readmitted after a fall at home. That case was still fresh, and honestly it's the first thing that came to mind when I was thinking through Hoffmann's risk, even before I'd looked closely at his own numbers.

Interviewer: Did you use the discharge risk-scoring tool at that point?

Participant: Not right away. It's available, but at that point I already had a working plan in my head, and it felt more like a box to check than something that would change the direction. I figured I'd get to it, but running it wasn't the thing that felt urgent — moving the plan forward did. If I'd run it right then and it had come back high, I'd have been the one who had to unwind everything and explain the delay to bed management and to him. Just not running it yet didn't feel like I was actually doing anything one way or the other — the plan was already moving on its own, so leaving the tool for later felt like the lower-stakes choice.

Interviewer: What did the fuller chart review and the tool eventually show?

Participant: When I did look closer, his actual readmission history was lower than what my gut had been telling me. And the tool rated him moderate, not high. So the numbers didn't fully back up how worried I'd been feeling based on that other case.

Interviewer: Let's talk about the final decision — finalizing the plan. What were the options at that point?

Participant: There was a short-term rehab bed available, but it needed one more day for insurance pre-authorization. The alternative was finalizing home discharge that same day. Bed management wanted an answer. And Mr. Hoffmann himself was pretty upset at the idea of any delay or of going anywhere other than home.

Interviewer: What did you think that extra day would actually do to him?

Participant: Honestly, I pictured him getting more worked up the longer it dragged on — maybe starting to feel like we'd gone back on our word, losing some trust in the plan altogether. When I mentioned it might just be the one night, for the safety check, he actually said he supposed he could manage if he really had to, even though he clearly didn't like the idea. But even hearing that, it still felt to me like it wouldn't just be one rough night for him — like the frustration and the sense of being stuck here would carry over past the delay itself. So finishing the extra checks felt like it would cost more than it was worth if it meant putting him through that.

Interviewer: What tipped it toward same-day discharge?

Participant: Honestly, a big piece of it was him. He was distressed even talking about waiting a day, and I didn't want to put him through that when we already had a workable home plan. The extra day would've let us finish the home safety evaluation and firm up the caregiver picture, but weighing that against how upset he clearly was about delay, I leaned toward getting him home that day.

Interviewer: What came out of the home safety evaluation once it was finally done?

Participant: After discharge, it turned up a loose stair rail and poor lighting in the bathroom. And the daughter later said she felt underprepared for how much support he actually needed.

Interviewer: Looking back, if the PT assessment had come in before your first conversation with him, do you think anything would have gone differently?

Participant: Maybe. I might have gone in with more questions instead of forming an opinion so quickly.

Interviewer: If you hadn't had that other readmission case fresh in mind, would your risk read have been different?

Participant: Possibly less urgent-feeling, yeah. It's hard to separate that out completely.

Interviewer: Any point where slowing down might have changed the outcome?

Participant: Probably the caregiver piece. If I'd pushed harder on specifics with the daughter earlier instead of assuming it would work out, we might have caught the coverage gap sooner.

Interviewer: What would you do differently with a similar case tomorrow?

Participant: Probably run the risk tool earlier, and ask more direct questions about caregiving capacity right from the first call, rather than filling in the gaps myself.

</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HC_Biased_7",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Social Worker (Hospital Discharge Planning)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Friday Discharge: Mr. Hoffmann's Fall and the Empty Apartment",
    "scenario_summary_internal": "A hospital social worker manages discharge planning for a 78-year-old man (Mr. Hoffmann) admitted after a fall at home, complicated by COPD and a recent history of ED visits. The social worker must decide, under time pressure before a Friday discharge deadline, whether the patient can safely return home with outpatient support or needs a short-term rehabilitation placement. The narrative follows four sequential decisions: initial mobility/risk assessment, discharge destination selection, review of readmission risk using chart history, and finalization of the discharge plan and follow-up scheduling. Interpersonal pressure from bed-management staff, an ambiguous family caregiving situation, and the worker's own prior caseload experience create fertile, realistic ground for subtle reasoning distortions without any need for dramatic negligence.",
    "occupational_realism": {
      "objective": "Determine a safe, timely discharge destination and follow-up plan for a fall-risk patient before a bed-management deadline.",
      "setting": "Mid-size regional hospital, internal medicine ward, Thursday afternoon into Friday morning before a weekend discharge push.",
      "constraints": [
        "Bed management is requesting the room be freed by Friday noon.",
        "Patient's daughter lives two hours away and can only visit twice a week.",
        "Home care agency has limited weekend staffing.",
        "Patient expresses strong preference to return home.",
        "Short-term rehab bed availability is uncertain and requires insurance pre-authorization."
      ],
      "stakeholders": [
        "Mr. Hoffmann (patient)",
        "Patient's daughter (long-distance caregiver)",
        "Attending physician",
        "Bed management coordinator",
        "Home care agency liaison",
        "Physical therapist"
      ],
      "technical_terms_to_use": [
        "discharge readiness",
        "fall risk assessment",
        "home safety evaluation",
        "readmission risk",
        "outpatient services referral",
        "caregiver capacity",
        "short-term rehabilitation placement",
        "chart review",
        "functional mobility score"
      ],
      "technical_terms_to_avoid": [
        "anchoring bias",
        "confirmation bias",
        "overconfidence",
        "availability heuristic",
        "expectation bias",
        "impact bias",
        "omission bias",
        "cognitive bias",
        "heuristic"
      ],
      "timeline": [],
      "probe_plan": {},
      "occurrence_embedding_plan_internal": [],
      "control_specification": {},
      "counterfactual_specification": {},
      "generation_checks": []
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Referral note from the ED states patient 'ambulates independently with cane, lives alone.'",
          "Physical therapist has not yet completed a formal functional mobility assessment.",
          "Patient reports feeling 'fine, just tripped on a rug.'",
          "Social worker has an initial 10-minute bedside conversation before the PT evaluation is scheduled."
        ],
        "new_information_after_decision": [
          "PT evaluation later shows reduced grip strength and slower gait speed than the ED note implied.",
          "Nursing notes mention two unwitnessed near-falls overnight."
        ],
        "alternatives": [
          "Treat the ED note's mobility description as the baseline and proceed with planning around independent living.",
          "Withhold judgment on mobility until the formal PT assessment is complete and gather additional observation."
        ],
        "intended_action": "Social worker forms an initial risk impression anchored to the ED referral note's mobility description and expresses confidence in her read of the patient's independence before PT data arrives."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Daughter said in an early phone call she 'wants to help however she can' but did not commit to specific days.",
          "Home care agency confirmed limited weekend visit slots.",
          "Patient insists he wants to go home and has done so successfully after two prior admissions.",
          "No documented home safety inspection has occurred this admission."
        ],
        "new_information_after_decision": [
          "A follow-up call reveals the daughter can only visit twice weekly and works full time.",
          "The home care agency liaison flags that weekend coverage cannot be guaranteed."
        ],
        "alternatives": [
          "Plan for home discharge with outpatient services, treating the daughter's general willingness as sufficient caregiver support.",
          "Pause the plan to explicitly verify caregiver availability and coverage gaps before committing to a destination."
        ],
        "intended_action": "Social worker selects home discharge as the working plan, interprets the daughter's vague willingness as confirming adequate caregiver coverage, and directs follow-up questions toward logistics of home discharge rather than toward whether it is appropriate."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chart shows two prior hospitalizations in the past year, both discharged home successfully.",
          "A different patient with a similar profile was readmitted last month after a fall at home, a case the social worker personally handled and remembers vividly.",
          "Current chart has no documented falls-at-home readmission for Mr. Hoffmann specifically.",
          "A discharge risk-scoring tool is available but not yet consulted."
        ],
        "new_information_after_decision": [
          "The full chart review later reveals Mr. Hoffmann's actual readmission history is low relative to his risk score.",
          "The risk-scoring tool, once used, rates him as moderate rather than high risk."
        ],
        "alternatives": [
          "Weight the recent, memorable readmission case heavily when judging Mr. Hoffmann's own readmission risk.",
          "Rely primarily on Mr. Hoffmann's documented chart history and the risk-scoring tool rather than a recalled similar case."
        ],
        "intended_action": "Social worker's risk judgment is swayed by the vividness of a recently handled, similar-seeming readmission case, and she also omits actively running the standard discharge risk-scoring tool because the home-plan default already 'feels' settled."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Short-term rehab bed is available pending one more day of insurance pre-authorization.",
          "Patient has expressed distress at the idea of any delay or rehab placement.",
          "Bed management is pressing for a same-day decision.",
          "A one-day delay would allow completion of the home safety evaluation and caregiver confirmation."
        ],
        "new_information_after_decision": [
          "The home safety evaluation, completed after discharge, identifies a loose stair rail and poor bathroom lighting.",
          "The daughter later reports she felt unprepared for the level of support needed."
        ],
        "alternatives": [
          "Finalize immediate home discharge to avoid the patient's anticipated distress from a one-day delay.",
          "Accept a one-day delay to complete verification steps despite the patient's expressed frustration."
        ],
        "intended_action": "Social worker finalizes the home discharge plan same-day, weighting the patient's anticipated emotional reaction to a delay more heavily than the incremental value of completing verification steps."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this case first came to your attention?",
        "What was your overall objective for Mr. Hoffmann's discharge?"
      ],
      "timeline_reconstruction": [
        "What happened right after you first read the referral note?",
        "Walk me through your conversations with the daughter, in order.",
        "When did the PT assessment and chart review happen relative to your planning decisions?",
        "What was the sequence of events on the final day before discharge?"
      ],
      "decision_point_probes": [
        "What specific information were you relying on when you formed your first impression of his mobility?",
        "What made you feel confident in that initial read before PT weighed in?",
        "What did the daughter's comment about wanting to help mean to you at the time?",
        "Did you look for any information that might have contradicted the home-discharge plan?",
        "What made the earlier readmission case come to mind here?",
        "Did you run the standard risk-scoring tool before or after settling on a plan?",
        "What weighed most heavily in your decision to finalize discharge that day rather than wait?",
        "How did you weigh the patient's reaction to a delay against the outstanding verification steps?"
      ],
      "closing_hypotheticals": [
        "If the PT assessment had come back before your first conversation with the patient, would anything have changed?",
        "If you hadn't recently handled that similar readmission case, do you think your risk read would have been different?",
        "Looking back, is there a point where slowing down might have changed the plan?",
        "What would you do differently if a similar case came in tomorrow?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ob_01",
        "bias": "Overconfidence Bias",
        "decision_point": 1,
        "mechanism": "Social worker expresses high certainty in her independent read of the patient's mobility/risk status based on a brief bedside chat, before any formal assessment data exists, and states this confidence explicitly when asked about her basis.",
        "affected_reasoning_operation": "Self-assessment of judgment accuracy under incomplete information",
        "evidence_available_at_time": [
          "ED referral note",
          "Brief bedside conversation",
          "No completed PT evaluation"
        ],
        "required_textual_manifestation": "A statement where she describes feeling sure of her read on his independence 'within a few minutes' of talking to him, ahead of any formal mobility testing.",
        "plausible_nonbias_interpretation": "Experienced clinicians often form rapid, generally accurate first impressions; confidence alone is not proof of bias.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence", "bias", "heuristic"]
      },
      {
        "instance_id": "an_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "The ED referral note's phrase 'ambulates independently with cane' becomes the fixed reference point for all subsequent mobility judgments, even as new observational cues (overnight near-falls) emerge.",
        "affected_reasoning_operation": "Initial estimate formation and insufficient adjustment from a starting value",
        "evidence_available_at_time": [
          "ED referral note wording",
          "Overnight nursing near-fall notes (available same phase but received after initial framing)"
        ],
        "required_textual_manifestation": "She references the original note's wording when explaining her mobility read, and treats later contradicting nursing notes as a minor addendum rather than reason to revise the initial estimate.",
        "plausible_nonbias_interpretation": "It is reasonable to weight an ED clinician's documented mobility assessment as a credible starting point.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchoring", "bias", "reference point"]
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 2,
        "mechanism": "After tentatively settling on home discharge, the social worker's follow-up questions to the daughter and agency focus on logistics that support the plan (visit scheduling, service setup) rather than on testing whether caregiver support is actually sufficient.",
        "affected_reasoning_operation": "Selective information-seeking after forming a working hypothesis",
        "evidence_available_at_time": [
          "Daughter's general statement of willingness to help",
          "Two prior successful home discharges"
        ],
        "required_textual_manifestation": "A description of the questions she asked the daughter and agency, showing they were framed around 'when' and 'how' home support would work, not 'whether' it was adequate.",
        "plausible_nonbias_interpretation": "Once a plan is provisionally chosen, operational questions are a normal next step in care coordination.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "selective search"]
      },
      {
        "instance_id": "eb_01",
        "bias": "Expectation Bias",
        "decision_point": 2,
        "mechanism": "Because most families in her caseload experience end up providing adequate informal care, she interprets the daughter's ambiguous, noncommittal statement as confirming sufficient caregiver capacity, coloring how she records and recalls that conversation.",
        "affected_reasoning_operation": "Interpretation of ambiguous verbal evidence based on a prior expectation about typical case outcomes",
        "evidence_available_at_time": [
          "Daughter's vague verbal commitment",
          "General pattern from prior similar cases she has handled"
        ],
        "required_textual_manifestation": "A statement linking her interpretation of the daughter's words to 'usually how it goes with families' rather than to specifics the daughter actually said.",
        "plausible_nonbias_interpretation": "Drawing on general caseload patterns to interpret ambiguous statements is a common, sometimes valid, professional shortcut.",
        "strength": "subtle",
        "do_not_make_explicit": ["expectation bias", "prior expectation"]
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 3,
        "mechanism": "A recent, personally-handled readmission case with superficial similarity comes to mind vividly and disproportionately shapes her estimate of Mr. Hoffmann's own readmission risk, ahead of consulting his actual chart history.",
        "affected_reasoning_operation": "Probability/risk estimation via ease of recall of a salient example",
        "evidence_available_at_time": [
          "Memory of last month's similar-seeming readmission case",
          "Mr. Hoffmann's own chart (not yet reviewed in depth)"
        ],
        "required_textual_manifestation": "A statement where she explains her heightened concern for Mr. Hoffmann by referencing 'that other patient last month' before mentioning any of his own documented history.",
        "plausible_nonbias_interpretation": "Pattern recognition from recent cases is a legitimate part of clinical judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability bias", "vividness", "recall"]
      },
      {
        "instance_id": "om_01",
        "bias": "Omission Bias",
        "decision_point": 3,
        "mechanism": "She skips actively running the standard discharge risk-scoring tool, treating the inaction of not using it as less consequential than the active step of ordering additional assessment, because the home-plan default already feels settled.",
        "affected_reasoning_operation": "Weighing an act of omission (not consulting an available tool) versus an act of commission (actively reassessing)",
        "evidence_available_at_time": [
          "Availability of the standard risk-scoring tool",
          "Working assumption that the home plan is already appropriate"
        ],
        "required_textual_manifestation": "A moment where she acknowledges the tool exists but explains she didn't feel it was necessary to run it at that point, treating the decision not to check as lower-stakes than actively second-guessing the plan.",
        "plausible_nonbias_interpretation": "Time pressure can reasonably lead to deprioritizing a supplementary tool when a plan already seems supported by other evidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["omission bias", "act versus omission"]
      },
      {
        "instance_id": "ib_01",
        "bias": "Impact Bias",
        "decision_point": 4,
        "mechanism": "She overestimates how distressing a one-day delay would be for the patient's emotional state, using this overestimate to justify finalizing discharge immediately rather than completing outstanding verification steps.",
        "affected_reasoning_operation": "Affective forecasting about the intensity/duration of a stakeholder's emotional reaction to a hypothetical delay",
        "evidence_available_at_time": [
          "Patient's expressed frustration at the idea of delay",
          "Availability of a one-day delay option to complete verification"
        ],
        "required_textual_manifestation": "A statement where she explains prioritizing same-day discharge specifically because she anticipated the delay would be very upsetting for him, more than the incremental safety value of the extra day.",
        "plausible_nonbias_interpretation": "Patient-centered care legitimately weighs psychological wellbeing alongside logistics.",
        "strength": "subtle",
        "do_not_make_explicit": ["impact bias", "affective forecasting"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition, not a control."
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
      "Verify exactly 4 decision points are present, each with at least two alternatives.",
      "Verify exactly 7 total bias instances are embedded, one per manifest entry.",
      "Verify no bias terminology or explicit psychological labels appear in the interview text.",
      "Verify each instance has independent, distinguishable evidentiary support (no duplicate reasoning across instances of same or different biases).",
      "Verify decision point 1 contains exactly two distinct instances (Overconfidence, Anchoring) tied to different evidence sources (self-assessment confidence vs. referral-note wording).",
      "Verify decision point 2 contains exactly two distinct instances (Confirmation, Expectation) tied to different reasoning operations (selective search vs. ambiguous interpretation).",
      "Verify decision point 3 contains exactly two distinct instances (Availability, Omission) tied to different reasoning operations (recall-based estimation vs. act/omission weighting).",
      "Verify decision point 4 contains exactly one instance (Impact Bias).",
      "Verify total word count target of 1,350 (range 1,215-1,485) is achievable given probe density and timeline detail.",
      "Verify consequences described (near-falls, low actual readmission history, home safety findings) do not conclusively prove bias, preserving plausible non-bias interpretations."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Overconfidence Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Expectation Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Impact Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Omission Bias", "occurrences": 1, "mechanism_constraint": null}
    ],
    "target_bias_names": [
      "Overconfidence Bias",
      "Availability Bias",
      "Anchoring Bias",
      "Confirmation Bias",
      "Expectation Bias",
      "Impact Bias",
      "Omission Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Overconfidence Bias", "requested_occurrences": 1},
      {"bias": "Availability Bias", "requested_occurrences": 1},
      {"bias": "Anchoring Bias", "requested_occurrences": 1},
      {"bias": "Confirmation Bias", "requested_occurrences": 1},
      {"bias": "Expectation Bias", "requested_occurrences": 1},
      {"bias": "Impact Bias", "requested_occurrences": 1},
      {"bias": "Omission Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "ob_01", "bias": "Overconfidence Bias"},
      {"instance_id": "an_01", "bias": "Anchoring Bias"},
      {"instance_id": "cb_01", "bias": "Confirmation Bias"},
      {"instance_id": "eb_01", "bias": "Expectation Bias"},
      {"instance_id": "av_01", "bias": "Availability Bias"},
      {"instance_id": "om_01", "bias": "Omission Bias"},
      {"instance_id": "ib_01", "bias": "Impact Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "ob_01", "bias": "Overconfidence Bias", "decision_point": 1},
      {"instance_id": "an_01", "bias": "Anchoring Bias", "decision_point": 1},
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 2},
      {"instance_id": "eb_01", "bias": "Expectation Bias", "decision_point": 2},
      {"instance_id": "av_01", "bias": "Availability Bias", "decision_point": 3},
      {"instance_id": "om_01", "bias": "Omission Bias", "decision_point": 3},
      {"instance_id": "ib_01", "bias": "Impact Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ob_01",
        "bias": "Overconfidence Bias",
        "mechanism": "Expressing high certainty in a rapid, informal read of patient mobility/risk before formal PT data is available.",
        "affected_reasoning_operation": "Self-assessment of judgment accuracy under incomplete information",
        "evidence_source": "Bedside conversation and ED note, absent PT assessment",
        "distinctiveness_requirement": "Must be distinct from an_01 by focusing on her stated confidence level rather than the content anchor she used."
      },
      {
        "instance_id": "an_01",
        "bias": "Anchoring Bias",
        "mechanism": "Fixating on the ED referral note's mobility phrase as the reference point, under-adjusting despite later contradicting nursing observations.",
        "affected_reasoning_operation": "Initial estimate formation and insufficient adjustment",
        "evidence_source": "ED referral note wording vs. overnight nursing near-fall notes",
        "distinctiveness_requirement": "Must be distinct from ob_01 by focusing on the specific reference value (note wording) and failure to revise, not on confidence level."
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Directing follow-up questions toward confirming the already-favored home-discharge plan rather than testing its adequacy.",
        "affected_reasoning_operation": "Selective information-seeking after forming a working hypothesis",
        "evidence_source": "Content/framing of questions posed to daughter and home care agency",
        "distinctiveness_requirement": "Must be distinct from eb_01 by involving active question-framing/search behavior, not passive interpretation of an ambiguous statement."
      },
      {
        "instance_id": "eb_01",
        "bias": "Expectation Bias",
        "mechanism": "Interpreting the daughter's ambiguous, noncommittal statement as adequate caregiver support because most similar past cases worked out that way.",
        "affected_reasoning_operation": "Interpretation of ambiguous evidence colored by prior expectation of typical outcomes",
        "evidence_source": "Daughter's vague verbal statement plus recalled general caseload pattern",
        "distinctiveness_requirement": "Must be distinct from cb_01 by centering on interpretation of existing ambiguous input, not on which new information was sought."
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Overweighting a vivid, recently-handled similar readmission case when estimating Mr. Hoffmann's own readmission risk, ahead of his documented chart history.",
        "affected_reasoning_operation": "Probability/risk estimation via ease of recall of a salient example",
        "evidence_source": "Personal memory of a recent similar case vs. Mr. Hoffmann's own chart",
        "distinctiveness_requirement": "Must be distinct from om_01 by involving recall-driven estimation, not the act/omission decision about using a formal tool."
      },
      {
        "instance_id": "om_01",
        "bias": "Omission Bias",
        "mechanism": "Treating the omission of running the standard risk-scoring tool as less consequential than an active reassessment, given the plan already feels settled.",
        "affected_reasoning_operation": "Differential weighting of omission versus commission in risk-assessment behavior",
        "evidence_source": "Availability and non-use of the discharge risk-scoring tool",
        "distinctiveness_requirement": "Must be distinct from av_01 by centering on the decision not to act (skip tool use), not on which memory drove her risk belief."
      },
      {
        "instance_id": "ib_01",
        "bias": "Impact Bias",
        "mechanism": "Overestimating the intensity of the patient's distress from a one-day discharge delay, using this forecast to justify same-day finalization over completing verification.",
        "affected_reasoning_operation": "Affective forecasting about intensity/duration of a stakeholder's emotional reaction",
        "evidence_source": "Patient's expressed frustration and availability of a one-day delay option",
        "distinctiveness_requirement": "Sole instance at decision point 4; distinct from all others by being an affective-forecasting operation rather than a probability, recall, or evidence-search operation."
      }
    ],
    "intended_strength": [
      {"instance_id": "ob_01", "bias": "Overconfidence Bias", "strength": "subtle"},
      {"instance_id": "an_01", "bias": "Anchoring Bias", "strength": "subtle"},
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle"},
      {"instance_id": "eb_01", "bias": "Expectation Bias", "strength": "subtle"},
      {"instance_id": "av_01", "bias": "Availability Bias", "strength": "subtle"},
      {"instance_id": "om_01", "bias": "Omission Bias", "strength": "subtle"},
      {"instance_id": "ib_01", "bias": "Impact Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Biased_7",
    "domain_id": "HC",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across 4 decision points by mechanism fit and narrative realism: DP1 (Overconfidence, Anchoring - both tied to initial mobility impression but distinct reasoning operations), DP2 (Confirmation, Expectation - both tied to caregiver adequacy judgment but distinct operations of search vs. interpretation), DP3 (Availability, Omission - both tied to readmission risk judgment but distinct operations of recall vs. act/omission weighting), DP4 (Impact - sole instance, tied to finalization timing). No decision point exceeds two instances of any single bias; all co-located instances use different evidence sources or reasoning operations as required.",
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
    "analysis_scope_note": "The interview was analyzed without supplied RAG corpus passages; all classifications rely on interview evidence and the reference ontology, and every identified occurrence records the absence of retrieved corpus support."
  },
  "identified_bias_summary": [
    {
      "canonical_bias_name": "Affect Heurisitic",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Anchoring Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Confirmation Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Impact Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Ostrich Effect",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Anchoring Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": "anchor point",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information when making subsequent judgments or decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Updating Mr. Hoffmann's mobility and fall-risk assessment after PT and overnight near-fall findings",
      "decision_point_description": "Whether to revise the initial home-discharge plan in light of new PT and nursing findings",
      "affected_reasoning_operation": "Interpretation and weighting of new clinical evidence; adjustment of the initial discharge-readiness assessment",
      "bias_specific_mechanism": "The early baseline depiction of Mr. Hoffmann as independent with a cane, reinforced by a brief bedside impression, became the reference point; later contradictory evidence of slower gait, weaker grip, and near-falls was treated as a watch item rather than sufficient reason to reset the assessment.",
      "manifestation_in_interview": "The participant explicitly calls the original independent-living picture her anchor point and says she framed the plan around the baseline description.",
      "effect_on_reasoning_or_decision": "The contradictory mobility and safety information was underweighted, allowing the home-discharge plan to remain largely intact.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The original picture, ambulates independently with a cane, that was still sort of my anchor point for how I was thinking about him.",
          "evidence_explanation": "This is an explicit statement that the initial baseline was functioning as an anchor in her ongoing assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did mention the near-falls in my note, but I framed the plan around the baseline description rather than treating the new information as something that should reset my assessment.",
          "evidence_explanation": "This demonstrates the effect of the anchor: new safety-relevant information was documented but not allowed to reset the initial plan."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The ED note said he ambulates independently with a cane and lives alone. That's a pretty common profile for us, so I had a sense of where this was probably headed.",
          "evidence_explanation": "This shows the early formation of the initial baseline that later served as the anchor."
        }
      ],
      "correction_or_counterevidence": "The participant did note the near-falls and eventually reviewed the discharge risk-scoring tool, but neither was treated as requiring a reset of the anchored baseline at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context; support is based on the interview and reference-ontology definition.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Confirmation Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or strengthen one's existing beliefs or plans.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluating caregiver capacity and feasibility of home support",
      "decision_point_description": "Whether to continue planning home discharge based on the daughter's vague offer of help or to test whether caregiver coverage was actually adequate",
      "affected_reasoning_operation": "Information gathering and questioning of the daughter and home care agency",
      "bias_specific_mechanism": "After forming a home-discharge plan, the participant focused on logistics to implement the plan rather than testing whether the plan was viable; she accepted the daughter's nonspecific willingness as sufficient without asking directly about schedule commitment until later.",
      "manifestation_in_interview": "The participant states that she asked 'how do we make this work' rather than 'can this actually work' and did not directly ask about regular caregiver schedule until later.",
      "effect_on_reasoning_or_decision": "The caregiver coverage gap was not identified until later, and the home-support plan was thinner than assumed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, mostly logistics — when could services start, what days would work best for a home health aide, whether she could be there for the first visit. I was asking more 'how do we make this work' than 'can this actually work.'",
          "evidence_explanation": "This indicates a confirmatory information-search pattern: questions were directed at implementing the existing plan rather than testing its feasibility."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, I didn't really ask her directly whether she could commit to a regular schedule until later.",
          "evidence_explanation": "This confirms that inquiry about the key feasibility issue was postponed, consistent with confirmation-driven information gathering."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So I took her willingness at face value as enough to build around.",
          "evidence_explanation": "This shows ambiguous information was interpreted favorably to the existing home-discharge plan."
        }
      ],
      "correction_or_counterevidence": "A later follow-up call revealed the daughter could only visit twice a week and worked full-time, and the home care agency flagged that weekend coverage was not guaranteed.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context; support is based on the interview and reference-ontology definition.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "The tendency to judge frequency or risk by the ease with which examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Estimating readmission and fall risk during chart review before using the formal risk tool",
      "decision_point_description": "Whether to weigh a recent similar personal case more heavily than Mr. Hoffmann's own documented history",
      "affected_reasoning_operation": "Risk estimation and felt urgency about readmission/fall risk",
      "bias_specific_mechanism": "A recent, personally handled case of a similar patient readmitted after a fall was still fresh and became the first basis for risk worry, before the participant closely examined Mr. Hoffmann's own numbers.",
      "manifestation_in_interview": "The participant says the recent case was still fresh and was the first thing that came to mind, and later says the actual numbers did not fully back up how worried she had been feeling based on that other case.",
      "effect_on_reasoning_or_decision": "Her subjective risk concern was more urgent than Mr. Hoffmann's own chart history and formal risk score supported.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd personally handled a case last month, a patient with a pretty similar profile, who was readmitted after a fall at home. That case was still fresh, and honestly it's the first thing that came to mind when I was thinking through Hoffmann's risk, even before I'd looked closely at his own numbers.",
          "evidence_explanation": "This demonstrates the availability mechanism: a salient recent example came to mind easily and formed the initial risk impression."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So the numbers didn't fully back up how worried I'd been feeling based on that other case.",
          "evidence_explanation": "This shows the resulting risk estimate was driven more by the recalled case than by the patient's own data."
        }
      ],
      "correction_or_counterevidence": "She later looked more closely at the chart and ran the risk tool, which showed moderate risk and a lower actual readmission history than her gut concern suggested.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context; support is based on the interview and reference-ontology definition.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Ostrich Effect",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "The tendency to avoid information that may be unpleasant, threatening, or require unwanted action.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Use of the discharge risk-scoring tool",
      "decision_point_description": "Whether to run the risk-scoring tool immediately or defer it",
      "affected_reasoning_operation": "Decision to seek or avoid formal risk information",
      "bias_specific_mechanism": "The participant anticipated that a high score would force her to unwind the existing plan and explain delay to bed management and the patient, so she framed deferring the tool as the lower-stakes choice and did not run it immediately.",
      "manifestation_in_interview": "She describes the tool as more of a box to check at that point and says leaving it for later felt like the lower-stakes choice.",
      "effect_on_reasoning_or_decision": "Formal risk stratification was delayed, allowing the existing plan to continue without early confrontation with potentially adverse risk information.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Not right away. It's available, but at that point I already had a working plan in my head, and it felt more like a box to check than something that would change the direction.",
          "evidence_explanation": "This shows the participant avoided the risk tool because it did not fit with the plan already moving forward."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd run it right then and it had come back high, I'd have been the one who had to unwind everything and explain the delay to bed management and to him.",
          "evidence_explanation": "This reveals the anticipated negative consequence driving avoidance of the information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Just not running it yet didn't feel like I was actually doing anything one way or the other — the plan was already moving on its own, so leaving the tool for later felt like the lower-stakes choice.",
          "evidence_explanation": "This demonstrates the avoidance-based framing: not obtaining information felt less risky than potentially having to act on bad news."
        }
      ],
      "correction_or_counterevidence": "The participant eventually did run the tool, which rated Mr. Hoffmann moderate rather than high.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context; support is based on the interview and reference-ontology definition.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Affect Heurisitic",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "The influence of emotional reactions on judgments and decisions, where the feeling about an option replaces a broader risk-benefit evaluation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final same-day discharge versus short-term rehab delay decision",
      "decision_point_description": "Whether to finalize same-day home discharge or allow an extra day for insurance pre-authorization and safety evaluation",
      "affected_reasoning_operation": "Weighing of patient distress against the safety and care-planning benefits of a one-day delay",
      "bias_specific_mechanism": "The participant's strong negative affective response to Mr. Hoffmann's distress about delay led her to avoid the delay and select home discharge, rather than fully weighing the possible safety benefits of additional evaluation.",
      "manifestation_in_interview": "She says a big piece of the decision was the patient's distress, and she did not want to put him through that when they already had a workable home plan.",
      "effect_on_reasoning_or_decision": "Same-day discharge was chosen even though the extra day would have allowed completion of the home safety evaluation and firmer caregiver planning.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, a big piece of it was him. He was distressed even talking about waiting a day, and I didn't want to put him through that when we already had a workable home plan.",
          "evidence_explanation": "This explicitly describes affect-driven decision weighting: the patient's distress became a primary reason for choosing same-day discharge."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I pictured him getting more worked up the longer it dragged on — maybe starting to feel like we'd gone back on our word, losing some trust in the plan altogether.",
          "evidence_explanation": "This shows anticipated negative emotion shaping the decision, even though the safety checks were unfinished."
        }
      ],
      "correction_or_counterevidence": "Mr. Hoffmann did say he supposed he could manage one night if he really had to, but the participant still gave substantial weight to his distress.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context; support is based on the interview and reference-ontology definition.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "canonical_bias_name": "Impact Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "The tendency to overestimate the intensity or duration of future emotional reactions to events.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Predicting Mr. Hoffmann's emotional response to a one-day delay",
      "decision_point_description": "Whether the one-day rehab pre-authorization delay would produce a manageable or prolonged emotional cost",
      "affected_reasoning_operation": "Affective forecasting about the patient's reaction to delay",
      "bias_specific_mechanism": "The participant predicted that the patient's frustration and sense of being stuck would carry over beyond the delay itself, even after the patient said he could manage one night if he had to.",
      "manifestation_in_interview": "She says it felt to her like it would not just be one rough night, and that the frustration would carry over past the delay.",
      "effect_on_reasoning_or_decision": "This prediction reinforced the choice of same-day discharge to avoid what was forecast as extended negative affect.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I mentioned it might just be the one night, for the safety check, he actually said he supposed he could manage if he really had to, even though he clearly didn't like the idea. But even hearing that, it still felt to me like it wouldn't just be one rough night for him — like the frustration and the sense of being stuck here would carry over past the delay itself.",
          "evidence_explanation": "This demonstrates an affective forecast of enduring negative emotional impact that goes beyond the one-night delay, despite the patient's statement that he could manage."
        }
      ],
      "correction_or_counterevidence": "The patient said he could manage one night if he really had to, which cuts against the prediction that the frustration would necessarily carry over.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context; support is based on the interview and reference-ontology definition.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_name": "Overconfidence Bias",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial independent-living assessment after a 10-minute bedside conversation",
      "supporting_interview_quote": "I remember feeling pretty confident, actually — like, within a few minutes of talking to him I felt I had him pegged as someone who could probably manage independently.",
      "plausible_mechanism": "The participant's subjective confidence in the initial 'steady' read may have exceeded what the brief pre-PT encounter and available information could support.",
      "why_not_identified": "The evidence is suggestive, but the reasoning effect is difficult to separate from the already identified Anchoring Bias, and there is no sufficiently independent decision point or bias-specific outcome to justify a separate occurrence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper passages were supplied in the RAG context; therefore retrieved_corpus_support_used is false and all corpus_evidence arrays are empty.",
    "Several potential biases such as overconfidence, premature closure, and plan continuation overlap with the identified anchoring and confirmation mechanisms and were not separated to avoid over-detection.",
    "Impact Bias is classified at moderate confidence because the interview does not provide an independent outcome measure of the patient's actual emotional response to a delay."
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
