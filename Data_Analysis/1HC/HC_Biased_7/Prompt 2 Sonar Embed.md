You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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

<EVALUATION_SEGMENT_MAP>
"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_baseline_inference",
        "raw_interview_anchor": "The ED note said he ambulates independently with a cane and lives alone. That's a pretty common profile for us, so I had a sense of where this was probably headed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "An initial baseline is expressed, but this span alone does not establish failure to update."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "confidence_in_initial_judgment",
        "raw_interview_anchor": "Within that conversation I felt like I had a good read on him... my instinct said steady.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ob_01"
        ],
        "ground_truth_rationale": "The participant expresses high confidence in a rapid mobility read before formal PT data."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "under_updating_from_contradictory_data",
        "raw_interview_anchor": "I had already sort of built my plan around the independent-living picture, so those things registered more as things to keep an eye on rather than something that should make me start over.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "an_01"
        ],
        "ground_truth_rationale": "The original independent-living description remains the reference point despite contradictory PT and nursing data."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "provisional_disposition_choice",
        "raw_interview_anchor": "From that, plus the fact he'd gone home successfully after two previous admissions, I moved forward planning for home with outpatient services.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A provisional plan is expressed without the explicit expectation-based interpretation required for eb_01."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "selective_follow_up_search",
        "raw_interview_anchor": "I was asking more 'how do we make this work' than 'can this actually work.'",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "Follow-up questions favored implementing the home plan rather than testing caregiver adequacy."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "expectation_based_interpretation",
        "raw_interview_anchor": "Families usually do step up... So I took her willingness at face value as enough to build around.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "eb_01"
        ],
        "ground_truth_rationale": "A vague caregiver statement is interpreted as sufficient because similar families usually work out."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "evidence_update",
        "raw_interview_anchor": "It did mean the coverage picture was thinner than what I'd been planning around.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a non-biased acknowledgment of newly discovered coverage limits."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "salient_case_based_risk_estimate",
        "raw_interview_anchor": "That case was still fresh, and honestly it's the first thing that came to mind when I was thinking through Hoffmann's risk.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "av_01"
        ],
        "ground_truth_rationale": "A vivid recent case shapes risk estimation before review of the patient's own data."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "risk_tool_omission_rationale",
        "raw_interview_anchor": "Leaving the tool for later felt like the lower-stakes choice.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "om_01"
        ],
        "ground_truth_rationale": "Omission of the available risk tool is treated as less consequential than active reassessment."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "objective_risk_update",
        "raw_interview_anchor": "The numbers didn't fully back up how worried I'd been feeling based on that other case.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is retrospective recognition of an objective-data mismatch, not a separate instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "option_and_constraint_comparison",
        "raw_interview_anchor": "There was a short-term rehab bed available... The alternative was finalizing home discharge that same day.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Options and constraints are described without the hidden affective-forecasting mechanism."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "anticipated_distress_weighting",
        "raw_interview_anchor": "The frustration and the sense of being stuck here would carry over past the delay itself. So finishing the extra checks felt like it would cost more than it was worth.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ib_01"
        ],
        "ground_truth_rationale": "The participant forecasts an extended distress reaction and uses it to reject completing verification."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "patient_preference_rationale",
        "raw_interview_anchor": "He was distressed even talking about waiting a day, and I didn't want to put him through that.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Patient distress is a legitimate consideration here; overestimation is not independently established in this span."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "retrospective_process_reflection",
        "raw_interview_anchor": "If I'd pushed harder on specifics with the daughter earlier instead of assuming it would work out, we might have caught the coverage gap sooner.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective process reflection, not a new occurrence."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "future_corrective_action",
        "raw_interview_anchor": "Run the risk tool earlier, and ask more direct questions about caregiving capacity.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Corrective intentions are not separately scored as bias occurrences."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Mechanism-first analysis of the Participant social worker's self-reported reasoning about discharge planning for Mr. Hoffmann. Interviewer questions are used only for context and are not themselves treated as evidence of bias."
  },
  "identified_bias_summary": [
    {
      "bias_label": "affect heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "search satisficing",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information when making subsequent judgments, with insufficient adjustment from later evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Forming an initial functional baseline and interpreting later physical therapy and nursing data",
      "decision_point_description": "Whether to revise the independent-living picture after slower gait speed, weaker grip strength, and two overnight near-falls.",
      "affected_reasoning_operation": "Assessment of the patient's functional safety and discharge needs",
      "bias_specific_mechanism": "The initial ED note and brief bedside impression formed an early anchor of the patient as independent with a cane. Subsequent disconfirming data from PT and nursing were acknowledged but interpreted as minor rather than resetting the assessment.",
      "manifestation_in_interview": "The participant explicitly described the original picture as his 'anchor point' and said the new data registered as things to monitor rather than reasons to start over.",
      "effect_on_reasoning_or_decision": "Reduced updating of the functional risk assessment and kept the home-with-outpatient-support plan as the default.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, within that conversation I felt like I had a good read on him. You develop an instinct for who's steady and who isn't, and my instinct said steady.",
          "evidence_explanation": "Shows early high-confidence impression from limited initial information, creating the anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I noted that, but at that point I'd already sort of built my plan around the independent-living picture, so those things registered more as things to keep an eye on rather than something that should make me start over.",
          "evidence_explanation": "Demonstrates that later disconfirming mobility/near-fall data did not meaningfully adjust the initial independent-living assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The original picture, ambulates independently with a cane, that was still sort of my anchor point for how I was thinking about him.",
          "evidence_explanation": "Explicitly identifies the original picture as the anchor point for subsequent reasoning."
        }
      ],
      "correction_or_counterevidence": "The participant did document the near-falls, and he later reflected that if the PT assessment had come before his first conversation, he might have formed his impression more slowly.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved case report explicitly describes anchoring onto an initially identified injury as a cognitive failure in clinical decision making.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The cognitive failures identified here are “anchoring” and “search satisficing.” The resident and attending staff both anchored onto the chest wound as the most significant injury. When they satisfied themselves that the chest wound was stable, the resident failed to conduct a sufficient search to rule out other significant injuries.",
          "mechanism_supported_by_source": "Anchoring on an initially identified problem and then failing to adjust sufficiently when further information should prompt reconsideration.",
          "relevance_to_this_occurrence": "The participant similarly anchored on the ED note and brief bedside impression of independent mobility, treating later PT and nursing data as minor rather than resetting risk."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "search satisficing",
      "alternative_labels": [
        "premature closure",
        "insufficient search"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to stop searching for information once a minimally acceptable or initially plausible answer has been reached, rather than conducting a sufficient search for more complete or disconfirming data.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluating caregiver support for home discharge",
      "decision_point_description": "Whether the daughter's vague offer of help was sufficient to support a safe home-discharge plan.",
      "affected_reasoning_operation": "Information gathering about caregiver capacity",
      "bias_specific_mechanism": "The participant accepted an early, ambiguous caregiver statement as adequate confirmation and oriented follow-up questions toward implementation logistics rather than testing whether the caregiver arrangement could actually work.",
      "manifestation_in_interview": "The participant said he was asking 'how do we make this work' rather than 'can this actually work' and did not ask directly about regular caregiver availability until later.",
      "effect_on_reasoning_or_decision": "The home-with-outpatient-services plan proceeded on an under-specified caregiver coverage assumption; later follow-up revealed thinner coverage than planned.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Early on, I called her, and she said she wants to help however she can. That was basically it at that point — no specific days, no specifics on her schedule. But from that, plus the fact he'd gone home successfully after two previous admissions, I moved forward planning for home with outpatient services.",
          "evidence_explanation": "Shows that a vague statement and prior discharge history were treated as sufficient to build the plan."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, mostly logistics — when could services start, what days would work best for a home health aide, whether she could be there for the first visit. I was asking more 'how do we make this work' than 'can this actually work.' In hindsight, I didn't really ask her directly whether she could commit to a regular schedule until later.",
          "evidence_explanation": "Demonstrates the search was narrowed to implementation after an initial plausible answer, rather than testing feasibility."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So I took her willingness at face value as enough to build around.",
          "evidence_explanation": "Indicates premature acceptance of ambiguous information as adequate for planning."
        }
      ],
      "correction_or_counterevidence": "Later follow-up with the daughter and home care agency identified the coverage gap, and the participant acknowledged he should have asked more direct questions about caregiving capacity earlier.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved case report describes search satisficing as calling off the search after an initial plausible finding, which matches the participant's premature acceptance of caregiver willingness.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Search satisficing” is again a problem, in that the resident called off the search for a cause for the patient’s dyspnea after ruling out pneumonia.",
          "mechanism_supported_by_source": "Stopping the information search after one plausible answer was reached, rather than continuing to search for alternative explanations or detailed feasibility.",
          "relevance_to_this_occurrence": "The participant stopped the caregiver search at the daughter's vague willingness and prior successful admissions, then moved to logistics rather than testing detailed availability."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging probability or risk by the ease with which relevant examples come to mind, rather than by objective base rates or individual data.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Estimating Mr. Hoffmann's readmission and fall risk",
      "decision_point_description": "How much weight to give the recent similar case versus the patient's own chart and risk score.",
      "affected_reasoning_operation": "Risk perception and assessment",
      "bias_specific_mechanism": "A recent, salient case of a similar patient readmitted after a fall was highly available in memory and came to mind before the participant examined the patient's own history, inflating subjective risk initially.",
      "manifestation_in_interview": "The participant said the recent case 'was still fresh' and was 'the first thing that came to mind'; later the chart and risk tool showed lower risk than his gut feeling.",
      "effect_on_reasoning_or_decision": "Initial risk concern was driven more by the available recent example than by Mr. Hoffmann's own moderate risk profile.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That case was still fresh, and honestly it's the first thing that came to mind when I was thinking through Hoffmann's risk, even before I'd looked closely at his own numbers.",
          "evidence_explanation": "Direct evidence that a recent salient case influenced risk judgment before objective chart review."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I did look closer, his actual readmission history was lower than what my gut had been telling me. And the tool rated him moderate, not high. So the numbers didn't fully back up how worried I'd been feeling based on that other case.",
          "evidence_explanation": "Shows the initial subjective risk was not supported by the patient's own data, consistent with availability-driven risk perception."
        }
      ],
      "correction_or_counterevidence": "The participant recognized that the chart and scoring tool did not support the high subjective risk and said the risk read might have felt less urgent without the fresh case.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus passage supports availability as a dominant heuristic in clinical decision-making under uncertainty; the detailed mechanism is supplemented by established cognitive-science knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "availability and anchoring are two dominant heuristics among emergency triage nurses.",
          "mechanism_supported_by_source": "The source identifies availability as a recognized clinician heuristic in risk/uncertainty settings, consistent with judgment by easily recalled examples.",
          "relevance_to_this_occurrence": "The participant's risk estimate was strongly influenced by a recently recalled similar case, matching the availability pattern rather than reliance on the patient's own base-rate information."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an existing plan or course of action when a decision point or newly available information could warrant reconsideration.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Deciding whether to run the discharge risk-scoring tool after forming a working plan",
      "decision_point_description": "Whether to use the risk tool at that point or defer it while continuing the existing discharge plan.",
      "affected_reasoning_operation": "Information search and risk evaluation within an active plan",
      "bias_specific_mechanism": "Because a working plan was already in motion, the participant treated the risk tool as a formal check rather than decision-relevant information and deferred it to avoid having to unwind the plan.",
      "manifestation_in_interview": "He described the plan as 'already moving on its own' and framed leaving the tool for later as 'the lower-stakes choice.'",
      "effect_on_reasoning_or_decision": "The risk tool was not run early, reducing the chance that a high score would interrupt the home-discharge plan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It's available, but at that point I already had a working plan in my head, and it felt more like a box to check than something that would change the direction.",
          "evidence_explanation": "Shows the existing plan reduced the perceived informational value of the tool."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Just not running it yet didn't feel like I was actually doing anything one way or the other — the plan was already moving on its own, so leaving the tool for later felt like the lower-stakes choice.",
          "evidence_explanation": "Explicitly describes continuing the existing plan and avoiding an action that could force reconsideration."
        }
      ],
      "correction_or_counterevidence": "The participant eventually ran the tool, which showed moderate risk, and he later said he would run the risk tool earlier in a similar future case.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the label was not available; the available cockpit-safety passage mentions plan continuation only by name, without definition or mechanism. The label is applied from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "affect heuristic",
      "alternative_labels": [
        "impact bias",
        "affective forecasting bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judgments and decisions are guided by current affective reactions, including evaluating risks and benefits based on immediate emotional responses rather than broader evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Choosing same-day discharge versus one-day delay for home safety evaluation",
      "decision_point_description": "Whether to proceed with same-day home discharge or wait one day to complete safety and caregiver verification.",
      "affected_reasoning_operation": "Risk-benefit tradeoff and prediction of patient emotional response",
      "bias_specific_mechanism": "The participant's immediate discomfort with the patient's visible distress, plus a prediction that distress would persist beyond the one-day delay, led him to heavily discount the value of completing safety checks despite the patient saying he could manage one night.",
      "manifestation_in_interview": "He interpreted the patient's dislike of delay as likely to produce lasting frustration and trust loss, and weighed that above completing safety and caregiver verification.",
      "effect_on_reasoning_or_decision": "Finalized same-day discharge; the home safety evaluation and caregiver picture remained incomplete.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I pictured him getting more worked up the longer it dragged on — maybe starting to feel like we'd gone back on our word, losing some trust in the plan altogether.",
          "evidence_explanation": "Shows a prediction of persistent negative affect from a one-day delay."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But even hearing that, it still felt to me like it wouldn't just be one rough night for him — like the frustration and the sense of being stuck here would carry over past the delay itself.",
          "evidence_explanation": "Demonstrates the emotional forecast persisted even after the patient said he could tolerate one night."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He was distressed even talking about waiting a day, and I didn't want to put him through that when we already had a workable home plan.",
          "evidence_explanation": "Indicates the immediate emotional response to patient distress weighed heavily in the final discharge decision."
        }
      ],
      "correction_or_counterevidence": "The patient said he could manage one night if he really had to, and the extra day would have allowed completion of the home safety evaluation and caregiver confirmation. Concern for patient distress is a legitimate clinical factor, so this occurrence is low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage provided an adequate definition or mechanism for affect heuristic or impact bias; the label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Analysis is based on a single retrospective self-report and cannot establish actual cognitive processing at the time of decisions.",
    "Some retrieved corpus passages mention bias labels without detailed definitions, so parts of the analysis rely on established cognitive-science labels.",
    "Time pressure, bed-management demands, and legitimate patient-autonomy considerations provide non-bias explanations that reduce confidence for some occurrences.",
    "The interview was conducted for internal review, which may encourage retrospective justification or selective reporting."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HC_Biased_7_Sonar_on",
  "interview_id": "HC_Biased_7",
  "system_prompt_id": "Sonar",
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
