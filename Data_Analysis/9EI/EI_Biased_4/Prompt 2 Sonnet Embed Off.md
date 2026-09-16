You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm before we start — this is being recorded for a research study on how administrators handle nonroutine incidents, your name won't be attached to the write-up, and you can skip any question you'd rather not answer. That okay?

Participant: Yes, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role and how long you've been in it?

Participant: I'm the principal here, going on my sixth year. Before that I was an assistant principal for four years at a different building, so I've handled my share of discipline cases, but this one turned into more than a discipline case by the end of the day.

Interviewer: Let's start broad. Can you describe the incident from the beginning?

Participant: It started at lunch, around 11:40. Two of my lunch monitors came to get me because there'd been a shoving incident near the cafeteria exit — two students, pretty visible, in front of maybe thirty other kids. By the time I got down there the crowd had scattered, so I didn't see it myself. Within ten minutes, a twelve-second clip of it was already circulating on phones. My first priority was getting the two students separated somewhere safe and figuring out what actually happened. The two monitors gave me quick verbal accounts, but they didn't fully agree on who moved first. I didn't have time to track down every kid who'd been standing there, so I went with what I had — the clip and the two staff accounts — and started questioning the students individually. Honestly, by the time I sat the two of them down, I already had a rough read on who'd started it from that clip and the monitors' accounts, and I figured chasing down another bystander or two wasn't going to change that picture much, so I didn't send anyone looking. That felt like the right move with lunch ending and both kids needing to be away from an audience.

Interviewer: What were you weighing in that moment?

Participant: Safety first, then figuring out enough of the facts to make a fair call. I remember thinking a full investigation — tracking down every witness — wasn't realistic with the day running the way it does. I had maybe five hours before dismissal and this was already spreading online, so I needed to move.

Interviewer: What happened after you separated them?

Participant: About an hour later a second, longer video surfaced — different angle, showed more of the lead-up. A teacher also came forward saying she'd overheard one of the boys say something provocative right before the shove. What was interesting is that in that same longer clip, right before the provocative comment, you can actually see the other student — the one with the clean record — step in close and gesture at him first, which on its face reads like he escalated things too. One student already had two minor conduct referrals this year; the other had a clean record. My assistant principal had looked at the same materials and leaned toward the referral kid being primarily at fault. Meanwhile the family of the student with the clean record was already en route, upset.

Interviewer: How did you fold that new information in?

Participant: I looked at that stepping-in moment for a while, but I didn't weight it that heavily — it's the kind of thing you see in any hallway confrontation without it meaning much. What stood out more was the pattern: he's had two run-ins this year, both times some confrontational language before things escalated, so the provocative comment fit something I'd already seen from him. I finalized in-school suspension for him. There was a third potential witness mentioned, but locating and interviewing her would've taken more time than I had, and the picture I had felt coherent enough to act on.

Interviewer: Was there a point where you considered pausing that decision, or applying something more provisional first?

Participant: I thought about a short cooling-off removal for both of them instead of a suspension for one, just to buy time. But once the story clicked into place for me — the pattern, the video, the provocation — it felt more honest to act on what I believed happened rather than sit on it.

Interviewer: Let's move to the communications piece. What came next?

Participant: By early afternoon, rumors were going around that discipline had been applied unevenly — that we'd come down harder on one kid because of the group he's part of. District communications wanted a statement out the same day, and a local reporter had already called twice. At that point I felt I understood the full sequence — I had both videos, the referral history, the AP's account. So I put out a statement laying out what happened and why the discipline decision was made the way it was.

Interviewer: When you say you had the full sequence — had you spoken with the school counselor by then, or heard from the third witness?

Participant: No, not yet. I hadn't gotten to either. But between the two videos and the referral pattern, I felt confident I had enough of the real story to speak to it publicly. I didn't want to put out something that just said "we're looking into it" — parents and reporters read that as us hiding something.

Interviewer: What did the counselor tell you afterward?

Participant: She mentioned there'd been tension between these two kids for weeks — some social media back-and-forth I hadn't known about. That reframed things a little. It wasn't just a one-off shove; there was history I hadn't accounted for when I made the statement.

Interviewer: Let's talk about the walkout. What happened there?

Participant: Word had spread that students were planning to walk out around 2:45 to protest what they saw as unfair treatment. It happened — a good chunk of the junior and senior classes went out to the front lawn. It lasted about twenty minutes and ended peacefully, no injuries, nobody left the property. There was also a fire drill scheduled at a neighboring building around the same time, and the noise actually helped pull a lot of kids back inside faster than we expected.

Interviewer: How did you communicate that outcome to the superintendent?

Participant: I sent a same-day summary. I walked through the decisions I'd made — separating the students quickly, finalizing discipline before it could drag on, getting ahead of the narrative with a statement — and how that combination kept things from escalating further. The AP and our resource officer were both out there during the walkout doing good work talking kids down, and I mentioned that, but the summary was really about how the decisions I'd made through the day set the conditions for it to stay peaceful.

Interviewer: Did the fire drill timing factor into how you described it?

Participant: I noted it in passing, but I don't think it was the deciding factor. I think the kids came back in largely because we'd handled the day the way we did — quick action, clear discipline, a statement that got ahead of the rumors. If I'd sat on my hands all afternoon I don't think it ends as cleanly.

Interviewer: Looking back, if you'd had that third witness statement — the one suggesting the provocation came from the other student — before you finalized discipline, would anything have changed?

Participant: That's fair. I go back and forth. Two days later, once we fully weighed her statement, we revised part of the discipline decision. So it clearly mattered. At the time, though, what I had felt solid enough to act on, and I stand by needing to make a call rather than let it drag into the next day.

Interviewer: What about the walkout — if it had turned confrontational instead of ending peacefully, would you describe today differently?

Participant: Probably. If it had gone badly I imagine my summary to the district would've focused more on the resource officer's response and less on the earlier discipline call. It's easier to see the whole day as one thread when it ends well.

Interviewer: Last one — anything you'd do differently if a similar incident happened again tomorrow?

Participant: I'd try to get the counselor and any additional witnesses into the loop earlier, even under time pressure. But I don't think the core approach — act fast, use what you've got, communicate clearly — was wrong. Some of it is just the nature of the job. You rarely get the full picture before you have to decide.

Interviewer: That's really helpful. Thanks for walking through all of that in such detail.

Participant: No problem. It was a long day, but not one I'm likely to forget.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EI_Biased_4",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "School Principal / Building Administrator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Cafeteria Video Incident: Discipline, Rumor, and a Threatened Walkout",
    "scenario_summary_internal": "A mid-size public high school principal must respond within a single school day to a filmed physical altercation between two students that circulates on social media, triggers conflicting eyewitness accounts, provokes accusations of unequal disciplinary treatment along racial/social-group lines, and escalates into a planned student walkout by mid-afternoon. The principal must decide how to open the investigation, how to assign discipline under incomplete information, how to communicate with parents/media, and how to manage the walkout threat while maintaining safety and legal defensibility — all inside roughly five hours with no time for a full formal investigation.",
    "occupational_realism": {
      "objective": "Contain a fast-moving disciplinary and reputational crisis while protecting student safety, ensuring fair and defensible discipline, and maintaining trust with families and staff, all before the end of the school day.",
      "setting": "A public high school of approximately 1,100 students; incident begins at 11:40 AM during lunch period and must be substantially resolved by the 3:15 PM dismissal bell.",
      "constraints": [
        "No more than 5 hours before dismissal and a planned walkout",
        "Only partial video footage and conflicting witness statements available",
        "District policy requires discipline decisions to be defensible under due-process review",
        "Assistant principal and school resource officer have competing priorities and limited availability",
        "Parents and a local news reporter are already calling the front office",
        "Superintendent's office expects a same-day incident summary"
      ],
      "stakeholders": [
        "Principal (protagonist)",
        "Assistant Principal",
        "School Resource Officer",
        "Two students involved in the altercation and their families",
        "Classroom teachers and lunch monitors",
        "District communications office",
        "Student body / informal leaders organizing the walkout"
      ],
      "technical_terms_to_use": [
        "progressive discipline matrix",
        "due process notice",
        "restorative conference",
        "incident report",
        "chain of custody (for video evidence)",
        "de-escalation protocol"
      ],
      "technical_terms_to_avoid": [
        "bounded rationality",
        "satisficing",
        "confirmation bias",
        "rationalization",
        "self-serving attribution",
        "illusion of understanding",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "A 12-second video clip showing one student shoving another near the cafeteria exit",
          "Two lunch monitors' brief verbal reports, partially contradictory",
          "A crowd of roughly 30 students dispersing before staff arrived",
          "No footage of what happened immediately before the shove"
        ],
        "new_information_after_decision": [
          "A second, longer video surfaces an hour later showing the sequence differently",
          "A teacher reports overhearing a verbal provocation not visible in the first clip"
        ],
        "alternatives": [
          "Open a full multi-witness investigation before separating students, delaying lunch dismissal",
          "Act immediately on the first video and monitor statements to separate and question the two students, deferring further evidence-gathering",
          "Call the resource officer to hold both students until every available witness is interviewed"
        ],
        "intended_action": "Principal separates the two students and begins questioning based only on the first clip and monitor reports, treating this as sufficient to proceed."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The second video and the overheard provocation, which complicate who instigated the conflict",
          "One student has two prior minor conduct referrals; the other has none",
          "Assistant principal's preliminary notes lean toward the student with prior referrals being primarily at fault",
          "Parents of the student with no prior record are already on their way to the school"
        ],
        "new_information_after_decision": [
          "A third witness later states the provocation came from the student with no prior referrals",
          "Discipline decision is issued before this third statement is logged"
        ],
        "alternatives": [
          "Pause the discipline decision until the third witness can be located and interviewed",
          "Finalize a discipline decision consistent with the emerging narrative that fits the prior-referral history",
          "Apply an interim, reversible consequence (e.g., short cooling-off removal) pending full review"
        ],
        "intended_action": "Principal finalizes an in-school suspension for the student with prior referrals, integrating the new video and prior history into a single confident account of what happened, explaining away the parts that don't fit."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Rumors are circulating that discipline was applied unevenly based on the students' social groups",
          "District communications office requests a same-day public statement",
          "Principal has not yet reviewed the third witness statement or consulted the school counselor about group dynamics",
          "Principal feels confident the situation is now fully explained based on the video and referral history"
        ],
        "new_information_after_decision": [
          "The counselor later notes an unresolved peer conflict dating back weeks that neither video nor referral history captured",
          "Several students state the walkout is about fairness perceptions, not just this single incident"
        ],
        "alternatives": [
          "Issue a statement acknowledging the incident is still under review and details may change",
          "Issue a confident, finalized public statement asserting the sequence of events and rationale for discipline as fully understood",
          "Delay any public statement until the counselor's input and all witness statements are collected"
        ],
        "intended_action": "Principal issues a confident public statement describing the incident and discipline rationale as fully resolved and understood, without flagging remaining uncertainty."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Walkout occurs briefly at 2:45 PM but ends peacefully within 20 minutes with no injuries",
          "Assistant principal and resource officer contributed significantly to on-the-ground de-escalation during the walkout",
          "District superintendent asks the principal for an end-of-day summary of how the crisis was handled",
          "Some staff privately note the walkout was defused partly by lucky timing (a scheduled fire drill nearby drew students back inside)"
        ],
        "new_information_after_decision": [
          "Follow-up review two days later finds the discipline decision needs partial revision once the third witness statement is fully weighed",
          "Staff feedback survey shows mixed views on whether the crisis was handled well"
        ],
        "alternatives": [
          "Attribute the peaceful outcome broadly to the full team's efforts and acknowledge the role of chance factors",
          "Frame the peaceful resolution primarily as a result of the principal's own quick judgment and leadership decisions",
          "Withhold judgment on the outcome's causes until a fuller after-action review is completed"
        ],
        "intended_action": "Principal frames the end-of-day summary to the superintendent as evidence of the principal's own effective, decisive leadership, downplaying the resource officer's, assistant principal's, and circumstantial contributions."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were told when this incident first came to your attention.",
        "What was your overall goal in the first few minutes after hearing about the altercation?"
      ],
      "timeline_reconstruction": [
        "What information did you have at each stage, and what changed as the day went on?",
        "When did the second video and the additional witness statements reach you, and how did that affect your thinking?"
      ],
      "decision_point_probes": [
        "At the point you separated the students, what alternatives did you consider besides acting on the first clip?",
        "When you finalized the discipline decision, how did you weigh the new video against the prior referral history?",
        "What made you confident enough to issue a public statement when you did?",
        "In your summary to the superintendent, how did you decide which factors to highlight as reasons the walkout ended peacefully?"
      ],
      "information_sources": [
        "Which sources did you trust most at each stage — video, staff reports, student accounts — and why?",
        "Was there information you didn't have time to seek out? How did you handle that gap?"
      ],
      "goals_and_alternatives": [
        "What competing goals were you balancing at each decision point?",
        "Looking back, what other options were realistically available to you at the time?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision at each of these four points?"
      ],
      "prior_experience": [
        "Did past incidents like this one shape how you read this situation?"
      ],
      "time_pressure_and_uncertainty": [
        "How much uncertainty did you feel you were operating under, and how did that affect your confidence in your conclusions?",
        "Where did the time constraint most affect the quality of information you could gather?"
      ],
      "closing_hypotheticals": [
        "If you'd had the third witness statement before finalizing discipline, would anything have changed?",
        "If the walkout had turned confrontational instead of peaceful, how would you describe today differently?",
        "What would you do differently if a similar incident happened again tomorrow?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 1,
        "mechanism": "Under severe time pressure and incomplete evidence, the principal treats the first available video clip and two brief monitor reports as an adequate basis for immediate action rather than seeking a fuller (but slower) investigation, satisficing on a workable-but-incomplete information set.",
        "affected_reasoning_operation": "Evidence sufficiency judgment / stopping rule for information search",
        "evidence_available_at_time": [
          "12-second video clip",
          "two partially contradictory monitor reports",
          "dispersed crowd with no other immediate witnesses"
        ],
        "required_textual_manifestation": "Principal explicitly states that pursuing a fuller investigation before acting was 'not realistic' given lunch-period logistics and proceeds to question and separate students using only the two available accounts.",
        "plausible_nonbias_interpretation": "A reasonable administrator might argue that immediate separation is a safety-first best practice regardless of evidentiary completeness.",
        "strength": "subtle",
        "do_not_make_explicit": ["bounded rationality", "satisficing", "limited information processing capacity"]
      },
      {
        "instance_id": "cr_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 2,
        "mechanism": "When the second video and overheard provocation complicate the emerging story, the principal integrates the new, partially conflicting information into a single tidy narrative consistent with the prior-referral student being at fault, rather than treating the inconsistency as genuinely unresolved.",
        "affected_reasoning_operation": "Integration of new evidence into an existing causal narrative",
        "evidence_available_at_time": [
          "second video complicating who instigated",
          "overheard provocation not visible in first clip",
          "one student's prior referral history",
          "assistant principal's preliminary lean"
        ],
        "required_textual_manifestation": "Principal describes explaining away the provocation detail as 'consistent with' the student's known pattern, producing a single coherent account rather than acknowledging the account is still contested.",
        "plausible_nonbias_interpretation": "Weighing prior conduct history as a legitimate risk factor in a progressive discipline matrix is a defensible policy practice.",
        "strength": "moderate",
        "do_not_make_explicit": ["rationalization", "coherence-based reasoning", "motivated reasoning"]
      },
      {
        "instance_id": "iu_01",
        "bias": "Illusion of understanding",
        "decision_point": 3,
        "mechanism": "Before issuing a public statement, the principal expresses confident, complete understanding of the incident's causes and dynamics, despite not having reviewed the third witness statement or consulted the counselor about the underlying weeks-long peer conflict.",
        "affected_reasoning_operation": "Confidence calibration about causal knowledge prior to public commitment",
        "evidence_available_at_time": [
          "video and referral-history-based narrative from decision point 2",
          "unreviewed third witness statement",
          "uncontacted counselor with relevant background information",
          "rumors of unequal treatment perception"
        ],
        "required_textual_manifestation": "Principal states the situation is 'fully understood' or equivalent and issues a finalized public account without flagging that key sources (counselor, third witness) were not yet consulted.",
        "plausible_nonbias_interpretation": "A principal might reasonably feel a public statement needs to project confidence to reassure parents, independent of actual epistemic certainty.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of understanding", "overconfidence", "epistemic miscalibration"]
      },
      {
        "instance_id": "se_01",
        "bias": "Self-Enhancement or Self-serving Bias",
        "decision_point": 4,
        "mechanism": "In summarizing the peaceful resolution of the walkout to the superintendent, the principal attributes the favorable outcome primarily to their own decisive leadership while downplaying the assistant principal's and resource officer's on-the-ground contributions and the fortuitous, unrelated fire drill that helped disperse students.",
        "affected_reasoning_operation": "Causal attribution of a favorable outcome to self versus external/team/chance factors",
        "evidence_available_at_time": [
          "assistant principal and resource officer's active de-escalation role during the walkout",
          "the incidental fire drill that helped draw students back inside",
          "mixed staff feedback on the day's handling"
        ],
        "required_textual_manifestation": "Principal's account of the end-of-day summary foregrounds their own judgment and decisions as the reason things ended well, mentioning colleagues and the fire drill only briefly or not as causal factors.",
        "plausible_nonbias_interpretation": "A principal reporting to a superintendent may reasonably emphasize their own decision-making because that is the information the superintendent specifically requested.",
        "strength": "subtle",
        "do_not_make_explicit": ["self-serving bias", "self-enhancement", "attribution bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control specified in this request."
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
      "Confirm exactly four decision points are present, each with at least two plausible alternatives.",
      "Confirm each of the four bias instances is embedded at its assigned decision point and nowhere else.",
      "Confirm no bias label, definition, or psychological terminology appears in the interview text.",
      "Confirm total word count falls between 1,215 and 1,485 words.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm consequences (peaceful walkout end, later partial revision of discipline) do not mechanically prove or disprove bias presence.",
      "Confirm each instance has a distinguishable evidence trace separate from the other three instances."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as premature closure of information search under time pressure, not as a stated policy rule."
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as explaining away conflicting new evidence to preserve a single tidy causal narrative."
      },
      {
        "bias": "Illusion of understanding",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as expressed confidence of complete causal understanding prior to a public commitment, despite unconsulted sources."
      },
      {
        "bias": "Self-Enhancement or Self-serving Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as attributing a favorable team/chance-influenced outcome primarily to the principal's own agency."
      }
    ],
    "target_bias_names": [
      "Bounded Rationality",
      "Coherence-based reasoning or Rationalisation",
      "Illusion of understanding",
      "Self-Enhancement or Self-serving Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Bounded Rationality",
        "requested_occurrences": 1
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "requested_occurrences": 1
      },
      {
        "bias": "Illusion of understanding",
        "requested_occurrences": 1
      },
      {
        "bias": "Self-Enhancement or Self-serving Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality"
      },
      {
        "instance_id": "cr_01",
        "bias": "Coherence-based reasoning or Rationalisation"
      },
      {
        "instance_id": "iu_01",
        "bias": "Illusion of understanding"
      },
      {
        "instance_id": "se_01",
        "bias": "Self-Enhancement or Self-serving Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 1
      },
      {
        "instance_id": "cr_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 2
      },
      {
        "instance_id": "iu_01",
        "bias": "Illusion of understanding",
        "decision_point": 3
      },
      {
        "instance_id": "se_01",
        "bias": "Self-Enhancement or Self-serving Bias",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Premature closure of information search under time pressure; treats first available, incomplete evidence set as sufficient to act.",
        "affected_reasoning_operation": "Evidence sufficiency judgment / stopping rule for information search",
        "evidence_source": "12-second video clip plus two partially contradictory monitor reports",
        "distinctiveness_requirement": "Occurs at decision point 1 only, tied to the initial separation/questioning decision, distinct from later narrative-integration and confidence issues."
      },
      {
        "instance_id": "cr_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "mechanism": "Integrates conflicting new evidence (second video, overheard provocation) into a single narrative consistent with the prior-referral student's fault, explaining away the misfit.",
        "affected_reasoning_operation": "Integration of new evidence into an existing causal narrative",
        "evidence_source": "second video and overheard provocation weighed against prior referral history",
        "distinctiveness_requirement": "Occurs at decision point 2 only, tied to finalizing discipline; involves reconciling new conflicting evidence, distinct from br_01's information-search cutoff and iu_01's confidence expression."
      },
      {
        "instance_id": "iu_01",
        "bias": "Illusion of understanding",
        "mechanism": "Expresses confident, complete comprehension of the incident's causes before a public statement, despite unreviewed third witness statement and uncontacted counselor.",
        "affected_reasoning_operation": "Confidence calibration about causal knowledge prior to public commitment",
        "evidence_source": "unreviewed third witness statement and uncontacted school counselor's background knowledge",
        "distinctiveness_requirement": "Occurs at decision point 3 only, tied to the public statement decision; concerns epistemic confidence rather than narrative construction (cr_01) or search cutoff (br_01)."
      },
      {
        "instance_id": "se_01",
        "bias": "Self-Enhancement or Self-serving Bias",
        "mechanism": "Attributes the peaceful walkout resolution primarily to own leadership decisions, downplaying colleagues' de-escalation efforts and an unrelated fortuitous fire drill.",
        "affected_reasoning_operation": "Causal attribution of a favorable outcome to self versus external/team/chance factors",
        "evidence_source": "assistant principal and resource officer's de-escalation actions; incidental fire drill timing",
        "distinctiveness_requirement": "Occurs at decision point 4 only, tied to the end-of-day summary; concerns outcome attribution, distinct from the three preceding evidence-processing biases."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "strength": "subtle"
      },
      {
        "instance_id": "cr_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "strength": "moderate"
      },
      {
        "instance_id": "iu_01",
        "bias": "Illusion of understanding",
        "strength": "moderate"
      },
      {
        "instance_id": "se_01",
        "bias": "Self-Enhancement or Self-serving Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Biased_4",
    "domain_id": "EI",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (1 through 4) chosen for mechanism fit and narrative realism: bounded rationality to the earliest time-pressured triage decision, rationalization to the evidence-integration/discipline-finalization decision, illusion of understanding to the pre-public-statement confidence decision, and self-enhancement to the post-outcome attribution decision. No decision point received more than one instance, satisfying the no-more-than-two-per-point rule trivially and ensuring full spread across the timeline.",
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
          "segment_id": "EI_Biased_4_dp1",
          "speaker": "Participant",
          "segment_type": "decision_point_1_initial_evidence_gathering",
          "raw_interview_anchor": "I already had a rough read on who'd started it ... chasing down another bystander or two wasn't going to change that picture much, so I didn't send anyone looking.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "br_01"
          ],
          "ground_truth_rationale": "The principal closes the information search on the first incomplete evidence set under time pressure."
        },
        {
          "segment_id": "EI_Biased_4_dp2",
          "speaker": "Participant",
          "segment_type": "decision_point_2_discipline_finalization",
          "raw_interview_anchor": "I didn't weight [the stepping-in moment] that heavily ... the pattern ... fit something I'd already seen from him ... the picture I had felt coherent enough to act on.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cr_01"
          ],
          "ground_truth_rationale": "Conflicting new evidence is explained away and selectively integrated into a tidy narrative consistent with prior referrals."
        },
        {
          "segment_id": "EI_Biased_4_dp3",
          "speaker": "Participant",
          "segment_type": "decision_point_3_public_statement",
          "raw_interview_anchor": "I felt I understood the full sequence ... I felt confident I had enough of the real story to speak to it publicly. I hadn't gotten to [the counselor or third witness].",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "iu_01"
          ],
          "ground_truth_rationale": "The principal expresses complete causal confidence before a public commitment despite two material sources remaining unconsulted."
        },
        {
          "segment_id": "EI_Biased_4_dp4",
          "speaker": "Participant",
          "segment_type": "decision_point_4_outcome_summary",
          "raw_interview_anchor": "The kids came back in largely because we'd handled the day the way we did ... I noted [the fire drill] in passing ... the AP and resource officer ... were both out there doing good work.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "se_01"
          ],
          "ground_truth_rationale": "A favorable, team- and chance-influenced outcome is attributed primarily to the principal's own decisions while other causes are downplayed."
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
    "analysis_scope_note": "Transcript-only analysis; no retrieved corpus passages were supplied as RAG context, so identified bias labels rely on general cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "fundamental attribution error",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "self-serving bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["biased assimilation", "selective exposure"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and weight evidence in ways that confirm an existing belief or expectation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial and final discipline decision for the lunch shoving incident",
      "decision_point_description": "Finalizing in-school suspension for the student with prior conduct referrals.",
      "affected_reasoning_operation": "Information search and evidence weighting",
      "bias_specific_mechanism": "The principal formed an early rough read from the initial clip and staff accounts, then selectively sought and weighted information consistent with that view while underweighting or not obtaining disconfirming evidence.",
      "manifestation_in_interview": "The participant reports declining to seek additional bystanders because the initial picture seemed sufficient, discounting the second video's stepping-in moment that suggested the other student escalated too, and deferring a third witness because the existing picture felt coherent.",
      "effect_on_reasoning_or_decision": "Led to finalizing a one-sided suspension without fully resolving contradictory evidence; later evidence from the third witness and counselor required a partial revision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, by the time I sat the two of them down, I already had a rough read on who'd started it from that clip and the monitors' accounts, and I figured chasing down another bystander or two wasn't going to change that picture much, so I didn't send anyone looking.",
          "evidence_explanation": "Shows an early formed hypothesis and a decision not to seek potentially disconfirming witness evidence because it was predicted not to change the existing picture."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at that stepping-in moment for a while, but I didn't weight it that heavily — it's the kind of thing you see in any hallway confrontation without it meaning much. What stood out more was the pattern: he's had two run-ins this year, both times some confrontational language before things escalated, so the provocative comment fit something I'd already seen from him.",
          "evidence_explanation": "Demonstrates selective weighting: ambiguous evidence that could challenge the initial attribution is minimized, while prior-record information consistent with the initial view is treated as more meaningful."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a third potential witness mentioned, but locating and interviewing her would've taken more time than I had, and the picture I had felt coherent enough to act on.",
          "evidence_explanation": "Shows that the sense of a coherent picture was used to justify not obtaining additional potentially disconfirming evidence."
        }
      ],
      "correction_or_counterevidence": "Later in the interview the participant acknowledges that a third witness statement and counselor information were eventually weighed and part of the discipline decision was revised, indicating the initial decision was not robust to disconfirming information.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label 'confirmation bias' is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "fundamental attribution error",
      "alternative_labels": ["correspondence bias", "attribution bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overattribute another person's behavior to dispositional or internal causes while underweighting situational constraints or influences.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of the second video and competing accounts",
      "decision_point_description": "Determining which student was primarily responsible for the physical escalation.",
      "affected_reasoning_operation": "Causal attribution of student behavior",
      "bias_specific_mechanism": "The principal interpreted the referral student's behavior in terms of a stable internal pattern from prior conduct referrals, while discounting the visible situational provocation in which the other student stepped in close and gestured first.",
      "manifestation_in_interview": "The participant notes that the clean-record student's stepping-in gesture 'on its face reads like he escalated things too,' but then minimizes that action and instead emphasizes the referral student's prior conduct pattern as the meaningful explanation.",
      "effect_on_reasoning_or_decision": "Supported the conclusion that the student with prior referrals was primarily at fault, contributing to the final suspension decision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "What was interesting is that in that same longer clip, right before the provocative comment, you can actually see the other student — the one with the clean record — step in close and gesture at him first, which on its face reads like he escalated things too. One student already had two minor conduct referrals this year; the other had a clean record.",
          "evidence_explanation": "This quote shows the participant had access to situational evidence that the other student also escalated, but immediately contrasts it with the students' disciplinary records, framing the event partly in dispositional terms."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at that stepping-in moment for a while, but I didn't weight it that heavily — it's the kind of thing you see in any hallway confrontation without it meaning much. What stood out more was the pattern: he's had two run-ins this year, both times some confrontational language before things escalated, so the provocative comment fit something I'd already seen from him.",
          "evidence_explanation": "Demonstrates underweighting of the situational action by the other student and overweighting of the referral student's dispositional pattern."
        }
      ],
      "correction_or_counterevidence": "A plausible non-bias consideration is that prior conduct history can be legitimate evidence in discipline decisions. In addition, the participant did initially notice the situational stepping-in gesture before discounting it.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label 'fundamental attribution error' is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence bias",
      "alternative_labels": ["overconfidence effect", "miscalibration"],
      "taxonomy_status": "established_label",
      "bias_definition": "A metacognitive bias in which an individual's subjective confidence in their judgment, knowledge, or information completeness exceeds objective accuracy.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Issuing the same-day public statement before counselor or third witness input",
      "decision_point_description": "Decision to release a definitive public statement describing the full sequence and rationale.",
      "affected_reasoning_operation": "Assessment of information sufficiency and public communication decision",
      "bias_specific_mechanism": "The principal felt he understood the full sequence and had enough of the real story despite explicitly knowing he had not spoken to the counselor or the third witness.",
      "manifestation_in_interview": "The participant states he felt he understood the full sequence from two videos, referral history, and the AP's account, and that he was confident enough to speak publicly rather than issuing a provisional statement.",
      "effect_on_reasoning_or_decision": "Led to a definitive public statement before known outstanding information was collected; later input from the counselor and third witness added materially important context.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point I felt I understood the full sequence — I had both videos, the referral history, the AP's account. So I put out a statement laying out what happened and why the discipline decision was made the way it was.",
          "evidence_explanation": "Shows high subjective confidence in completeness of understanding based on limited sources, motivating a definitive public statement."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not yet. I hadn't gotten to either. But between the two videos and the referral pattern, I felt confident I had enough of the real story to speak to it publicly. I didn't want to put out something that just said 'we're looking into it' — parents and reporters read that as us hiding something.",
          "evidence_explanation": "Explicitly acknowledges missing counselor and third witness information while still expressing strong confidence in having enough of the real story."
        }
      ],
      "correction_or_counterevidence": "Time pressure and district/media communication demands may have constrained the decision; the participant also frames the public statement partly as a communication strategy to avoid appearing evasive.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label 'overconfidence bias' is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "self-serving bias",
      "alternative_labels": ["self-serving attribution bias", "self-serving attribution"],
      "taxonomy_status": "established_label",
      "bias_definition": "A motivational bias in which people attribute positive outcomes to their own actions and negative outcomes to external or situational factors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Same-day summary to superintendent describing the walkout outcome",
      "decision_point_description": "Constructing the district-facing account of why the walkout remained peaceful.",
      "affected_reasoning_operation": "Causal explanation of the walkout outcome and outcome reporting",
      "bias_specific_mechanism": "The principal attributed the peaceful walkout primarily to his own earlier decisions while downplaying the external fire drill noise and, in a counterfactual, indicating that a negative outcome would have been attributed more to the resource officer's response than to his own discipline decisions.",
      "manifestation_in_interview": "The participant states that his summary emphasized how his quick action, clear discipline, and public statement set conditions for the walkout to stay peaceful, while noting the fire drill only in passing and describing the resource officer's role as secondary.",
      "effect_on_reasoning_or_decision": "Produced a success narrative that credited the principal's own decisions and may have distorted the district's operational understanding of the walkout outcome.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The AP and our resource officer were both out there during the walkout doing good work talking kids down, and I mentioned that, but the summary was really about how the decisions I'd made through the day set the conditions for it to stay peaceful.",
          "evidence_explanation": "Credits his own decisions as the primary cause of the peaceful outcome while acknowledging but backgrounding others' contributions."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I noted it in passing, but I don't think it was the deciding factor. I think the kids came back in largely because we'd handled the day the way we did — quick action, clear discipline, a statement that got ahead of the rumors. If I'd sat on my hands all afternoon I don't think it ends as cleanly.",
          "evidence_explanation": "Downplays the fire drill's contributory role and emphasizes his own decisions as the decisive cause of the peaceful outcome."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If it had gone badly I imagine my summary to the district would've focused more on the resource officer's response and less on the earlier discipline call. It's easier to see the whole day as one thread when it ends well.",
          "evidence_explanation": "Explicitly indicates outcome-contingent attribution: success would be tied to his own actions, while a negative outcome would have been tied to others' response."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledges the fire drill timing and the AP/resource officer's work, but he discounts them. A competing non-bias explanation is that his earlier decisions genuinely contributed to keeping the walkout peaceful.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label 'self-serving bias' is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied as RAG context, so corpus_evidence fields are empty and bias labels rely on general cognitive-science knowledge.",
    "Some structural constraints such as time pressure and district communication needs appear in the transcript; these were not classified as biases unless a distinct bias-specific mechanism was separately evidenced.",
    "Several of the identified occurrences share overlapping interview material, but they were separated based on distinct reasoning operations: evidence weighting, causal attribution, confidence calibration, and outcome attribution."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Biased_4_Sonnet_off",
  "interview_id": "EI_Biased_4",
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
