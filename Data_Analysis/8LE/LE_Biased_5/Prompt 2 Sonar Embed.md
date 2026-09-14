You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time. Just to confirm before we start—this is a voluntary cognitive task analysis session, recorded for internal research on how IA investigations get worked, not a disciplinary review. You can decline any question. That work for you?

Participant: Yeah, that's fine. I've sat through enough of these on the other side of the table.

Interviewer: Can you tell me your role and how long you've handled complaint reviews?

Participant: I've been in the Internal Affairs Bureau about five years, investigator rank. I handle use-of-force complaints, some policy violations, occasional off-duty stuff.

Interviewer: Let's start with the case itself. Can you walk me through what came in?

Participant: Sure. Complaint came in the morning after a traffic stop on Cedar Street—expired registration stop that turned into a takedown. Driver, a Mr. Alvarez, said Officer Marquez used excessive force, ended up with a wrist fracture. Marquez wrote it up as a compliant-turned-resistant subject, said the takedown was necessary once Alvarez pulled his arm away. His partner, Officer Chen, backed that account. I pulled the file—Marquez has nine years in, two prior complaints, both closed unfounded. Alvarez has a record, two priors including a resisting-arrest charge.

Interviewer: When you opened the file, what did you do first?

Participant: I wanted to know who I was dealing with on both sides, so I ran backgrounds. For Alvarez, I requested his full arrest history and looked for anything that might explain inconsistency in his statement—prior resisting charge stood out, so I flagged that for the interview. For Marquez, I already had the two priors in the system, both unfounded, so I treated his report as the operational starting point and built the review around confirming or contradicting it rather than opening a parallel background pull on him the same way.

Interviewer: Was there a reason you didn't request the same kind of independent verification for Marquez's account at that stage?

Participant: I mean, his report exists, it's the formal record, that's the baseline you work from. Alvarez's statement is what's being tested. I don't think I consciously decided to treat them differently—it's just how intake usually goes. Later, dispatch audio came back showing it was a routine expired-registration stop, not flagged high-risk, and the medical report showed the wrist fracture, which honestly could line up with either version.

Interviewer: Let's move to the footage. Take me through the BWC review.

Participant: Eighteen minutes total, minus a forty-second gap where his camera didn't reactivate right after the initial contact. The first part is pretty calm—verbal back and forth, Marquez asking for license and registration, nothing dramatic. Then the last ninety seconds, Alvarez pulls his arm back when Marquez tries to walk him to the cruiser, and Marquez takes him down. That's where the injury happens.

Interviewer: How did you weigh the earlier minutes against that final sequence when you were forming your assessment?

Participant: Honestly, the takedown is what matters for a force review—that's the moment the fracture occurred, so that's where I put most of my attention. I ended up running that last segment back three or four times to get the mechanics right, and by the time I moved on, it was just sitting closer to the front of my mind than anything from the first part of the stop. The earlier fifteen minutes felt like it had run its course without incident, so once I'd watched it through the first time, I didn't feel much pull to go back and sit with it again. My working read was built mainly around those last ninety seconds.

Interviewer: Did anything from earlier in the footage later become relevant?

Participant: Yeah, actually. A slowed-frame audio pass done later picked up Marquez raising his voice and stepping into Alvarez's space almost three minutes before the takedown—something neither report mentioned. A use-of-force consultant flagged that positioning as relevant to the reasonableness call. I hadn't weighted that part much the first time through.

Interviewer: What was your reaction to learning that?

Participant: A little uncomfortable, if I'm honest. It didn't fit cleanly into the picture I'd already been building around the final segment.

Interviewer: Let's talk about the case conference. Who was there and what happened?

Participant: Day six, me, the sergeant, and two peer investigators. The sergeant supervised Marquez for three years and opened by saying Marquez has "never been a problem," which set kind of a tone. One of the other investigators raised the forty-second BWC gap, said it was worth flagging before we went further.

Interviewer: How did the room respond to that?

Participant: We talked about it briefly, but the conversation moved pretty quickly toward the take that the force was likely justified given Chen's corroboration and the resisting motion on camera. We didn't formally table the gap as an open item. I drafted the preliminary summary along those lines within the forty-eight-hour window we had for the Deputy Chief.

Interviewer: Did the investigator who raised the gap seem satisfied with that?

Participant: Not entirely, as it turned out. She told me privately afterward she still had reservations but didn't push it once the room had settled on a direction. I didn't document that follow-up conversation in the file at the time.

Interviewer: What made you align with the room's direction rather than the concern she'd raised?

Participant: I think once the sergeant framed it that way and Chen's report backed it up, the momentum was already there. It felt like the sensible read given everyone's read of the tape. I didn't feel like there was a strong reason to hold it up.

Interviewer: Let's go to day ten. What happened with the eyewitness?

Participant: A civilian witness who'd called in initially but was hard to reach finally gave a statement. She said Marquez was "aggressive from the start," which conflicts with how I'd characterized the early footage as calm. That came five days after I'd already briefed the Deputy Chief that this was trending toward exonerated.

Interviewer: How did that statement affect your thinking?

Participant: It shifted things somewhat. It was the freshest account I had at that point, closer in my mind than the footage I'd reviewed back on day three, so it carried a lot of weight in the conversations we had finalizing language.

Interviewer: You mentioned a supplemental review. What did that find?

Participant: A second investigator confirmed she had an unobstructed view but was about thirty-five feet away. Command also asked whether the preliminary briefing still stood.

Interviewer: How did you resolve the tension between her account and what you'd already told the Deputy Chief?

Participant: I leaned toward treating her statement as less determinative—distance, lighting, that kind of thing—and kept the briefing largely as it was. I'll admit part of that was probably about not wanting to walk back something I'd already told command with some confidence. Revising it at that point would've meant explaining why my read had changed, and I didn't feel the new statement was strong enough on its own to justify that.

Interviewer: What's the part of this case you're least confident about, even now?

Participant: Probably whether the early three-minute positioning detail should have carried more weight from the start. I don't know that it changes the final call, but I didn't give it a fair look the first time around.

Interviewer: If the eyewitness statement had come in on day two instead of day ten, do you think your review would have gone differently?

Participant: Probably. I'd have folded it into the footage review directly instead of layering it on top of an opinion I'd already formed and reported up.

Interviewer: If you'd been the only reviewer, without the case conference, do you think you'd have reached the same finding?

Participant: Hard to say. Maybe I'd have sat with the BWC gap longer on my own. Group discussions move faster than solo review, for better or worse.

Interviewer: Anything you'd handle differently in sequencing next time?

Participant: I'd probably push harder to get the eyewitness statement early, and I'd formally log dissenting concerns from the conference instead of letting them stay verbal. That's on me.

Interviewer: Appreciate you walking through this in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Biased_5",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Internal Affairs Investigator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Cedar Street Stop: Use-of-Force Complaint Review",
    "scenario_summary_internal": "An Internal Affairs (IA) investigator is assigned to review a citizen complaint alleging excessive force by Officer R. Marquez during a late-night traffic stop that ended in a takedown and a minor injury to the driver. The investigator must triage the complaint, review body-worn camera (BWC) footage and written reports, consult with peer investigators and a sergeant at a case conference, and reach a final sustained/unsustained determination after a delayed witness statement surfaces. The case is nonroutine because the complainant has a prior record (creating scrutiny asymmetry), the officer is well-regarded and previously cleared in two prior complaints (creating in-group trust), and new evidence arrives late in the process, after the investigator has already reported a preliminary impression to command.",
    "occupational_realism": {
      "objective": "Determine whether Officer Marquez's use of force during the Cedar Street stop was objectively reasonable and consistent with department use-of-force policy, and issue a sustained/unsustained/exonerated finding supported by the case file.",
      "setting": "Municipal police department Internal Affairs Bureau, over a 12-day review period following a citizen complaint filed the morning after the incident.",
      "constraints": [
        "14-day departmental deadline to issue a preliminary finding",
        "BWC footage has a 40-second gap due to a camera reactivation delay",
        "Complainant has two prior arrests, one for resisting arrest, which is known to the investigator before the interview",
        "Officer Marquez has 9 years of service, two prior complaints both closed as unfounded",
        "Sergeant on the review panel supervised Marquez for 3 years and voices strong support early in the case conference",
        "A civilian eyewitness statement is not collected until day 10 due to delayed callback"
      ],
      "stakeholders": [
        "Internal Affairs Investigator (interviewee)",
        "Officer R. Marquez (subject officer)",
        "Officer T. Chen (witness officer, Marquez's partner)",
        "Complainant D. Alvarez",
        "Civilian eyewitness (late-disclosed)",
        "IA Sergeant (case conference lead)",
        "Deputy Chief (command, receives preliminary briefing)"
      ],
      "technical_terms_to_use": [
        "use-of-force continuum",
        "objectively reasonable standard",
        "sustained/unsustained/exonerated finding",
        "body-worn camera (BWC) review",
        "totality of circumstances",
        "preliminary briefing",
        "case conference",
        "administrative investigation timeline"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "asymmetrical skepticism",
        "recency effect",
        "groupthink",
        "cognitive dissonance",
        "any explicit bias-naming or psychological labeling"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Complainant's written statement alleging excessive force",
          "Complainant's prior record includes a resisting-arrest arrest",
          "Officer Marquez's incident report describing a compliant-turned-resistant subject",
          "Two prior unfounded complaints against Marquez on file"
        ],
        "new_information_after_decision": [
          "Dispatch audio confirms a routine stop for expired registration, not a high-risk call",
          "Medical report shows a wrist fracture consistent with either resistance or excessive force"
        ],
        "alternatives": [
          "Open a full parallel review of both accounts with equal initial scrutiny and independent evidence requests",
          "Prioritize verifying the complainant's account for inconsistencies before scheduling the officer interview",
          "Request an expedited command briefing before any evidence review"
        ],
        "intended_action": "Investigator opens the file by requesting corroborating detail for the complainant's account (criminal history, prior conduct) while accepting the officer's report as a working baseline pending contrary evidence."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Full BWC footage (18 minutes) covering the stop from approach to handcuffing",
          "Early footage shows a calm verbal exchange and Marquez's initial de-escalation attempts",
          "Final 90 seconds show a rapid takedown after the subject pulls his arm away",
          "Written report from Officer Chen corroborating the takedown as necessary"
        ],
        "new_information_after_decision": [
          "Slowed-frame audio analysis reveals Marquez raised his voice and stepped into the subject's space nearly 3 minutes before the takedown, a detail not emphasized in either report",
          "Use-of-force expert consultant notes the earlier positioning as relevant to reasonableness"
        ],
        "alternatives": [
          "Score proportionality based on the full 18-minute sequence, weighting early de-escalation and late escalation equally",
          "Focus the proportionality assessment primarily on the final takedown sequence since that is what generated the injury",
          "Request a third-party use-of-force expert review before forming any working assessment"
        ],
        "intended_action": "Investigator's working assessment of proportionality is anchored heavily on the final takedown sequence, treating the earlier de-escalation minutes as largely settled and less relevant to the reasonableness judgment."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Case conference with IA Sergeant and two peer investigators scheduled on day 6",
          "Sergeant supervised Marquez for 3 years and states early in the meeting that Marquez has 'never been a problem'",
          "One peer investigator raises the unaddressed 40-second BWC gap as worth flagging",
          "Preliminary written summary due to the Deputy Chief within 48 hours of the conference"
        ],
        "new_information_after_decision": [
          "The peer investigator who raised the BWC gap later privately tells the investigator she still had reservations but did not press the point in the room",
          "The Deputy Chief's briefing note reflects the majority view reached in the meeting, not the flagged concern"
        ],
        "alternatives": [
          "Formally table the BWC gap as an open item requiring follow-up before any preliminary characterization is finalized",
          "Adopt the room's quickly-formed consensus that the force was likely justified and move to drafting the preliminary summary",
          "Request a recorded dissent or minority note be attached to the case file"
        ],
        "intended_action": "Investigator aligns with the sergeant-led consensus that the force was likely justified, and the unresolved BWC gap is set aside without documented follow-up, matching the group's converging view rather than the individual reservation raised in the room."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary briefing already delivered to the Deputy Chief on day 8 indicating a likely exonerated finding",
          "On day 10, a civilian eyewitness statement is finally obtained, describing Marquez as 'aggressive from the start' and disputing the calm-exchange characterization",
          "The eyewitness account partially conflicts with the early BWC minutes previously reviewed",
          "Deadline for final determination is day 14"
        ],
        "new_information_after_decision": [
          "A supplemental review by a second investigator confirms the eyewitness had an unobstructed view but was 35 feet away",
          "Command asks for confirmation that the preliminary briefing still stands"
        ],
        "alternatives": [
          "Treat the new eyewitness statement as one data point to be weighed alongside the full BWC record and re-open the proportionality analysis",
          "Give the most recently obtained eyewitness statement primary weight in finalizing the determination since it is the newest account",
          "Formally revise the preliminary briefing to reflect uncertainty and request additional time before finalizing"
        ],
        "intended_action": "Investigator both over-weights the newly obtained eyewitness statement relative to the earlier BWC record when finalizing language, and separately reconciles the tension between the earlier command briefing (already committed to an exonerated leaning) and the new conflicting evidence by minimizing the eyewitness account's relevance rather than revising the briefing, preserving consistency with the position already reported upward."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how you first received and triaged this complaint.",
        "What was your initial read on the credibility of each party before reviewing any footage?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of the BWC review, minute by minute if you can.",
        "When did the case conference happen relative to your evidence review, and who was present?",
        "When exactly did the eyewitness statement come in, and how did that fit into your existing timeline?"
      ],
      "decision_point_probes": [
        "What specifically made you request more detail on the complainant's background before the officer's account?",
        "How did you weigh the first 15 minutes of footage against the final 90 seconds when forming your proportionality judgment?",
        "What was said in the case conference that shaped the room's direction, and did anyone disagree?",
        "How did the eyewitness statement change your written determination, if at all?"
      ],
      "cues_information_sources": [
        "What cues told you the dispatch call type mattered or didn't matter?",
        "Which document or footage segment carried the most weight in your mind, and why?"
      ],
      "goals_alternatives": [
        "What were you trying to protect or establish at each stage—department credibility, officer fairness, complainant fairness?",
        "What alternative approach to the case conference did you consider, if any?"
      ],
      "decision_basis": [
        "What specific evidence, in your own words, most drove your preliminary finding?",
        "If you had to defend your final determination to an outside auditor, what would you point to first?"
      ],
      "prior_experience": [
        "Had you worked with Officer Marquez's file before? Did that history inform your expectations?",
        "Has a case conference ever changed your individual view before? What was different this time?"
      ],
      "time_pressure": [
        "How did the 14-day deadline affect your review pace, especially once the eyewitness statement came in late?"
      ],
      "uncertainty": [
        "What part of this case are you least confident about, even now?",
        "Was there a point where you felt the evidence was genuinely ambiguous?"
      ],
      "closing_hypotheticals": [
        "If the eyewitness statement had arrived on day 2 instead of day 10, would your review have unfolded differently?",
        "If you had been the only reviewer, without a case conference, do you think your finding would have been the same?",
        "Looking back, is there a point where you'd handle the sequencing of evidence review differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cbas_01",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "decision_point": 1,
        "mechanism": "Investigator applies differential scrutiny: actively seeking disconfirming background detail (prior arrests) on the complainant while accepting the officer's incident report as a default baseline without an equivalent verification request.",
        "affected_reasoning_operation": "Initial evidence-selection and credibility weighting at case intake",
        "evidence_available_at_time": [
          "Complainant's written statement",
          "Complainant's prior arrest record",
          "Officer's incident report",
          "Two prior unfounded complaints against the officer"
        ],
        "required_textual_manifestation": "Investigator explicitly describes requesting corroboration/background checks for the complainant but not initiating equivalent independent verification of the officer's narrative at the same stage.",
        "plausible_nonbias_interpretation": "Standard intake procedure may reasonably prioritize checking complainant credibility first since a formal report already exists from the officer's side.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "asymmetrical skepticism", "double standard of proof"]
      },
      {
        "instance_id": "re_01",
        "bias": "Recency Effects",
        "decision_point": 2,
        "mechanism": "In weighing an 18-minute BWC sequence, the investigator's proportionality judgment is anchored on the final 90-second takedown segment, treating earlier de-escalation minutes as settled and discounting their relevance to the overall reasonableness assessment.",
        "affected_reasoning_operation": "Integration and weighting of sequential evidence when forming an overall judgment",
        "evidence_available_at_time": [
          "Full 18-minute BWC footage",
          "Early calm exchange and de-escalation attempt",
          "Final takedown sequence",
          "Officer Chen's corroborating report"
        ],
        "required_textual_manifestation": "Investigator, when asked how proportionality was assessed, describes the takedown moment as the primary basis for judgment and treats the earlier minutes as background rather than integral evidence.",
        "plausible_nonbias_interpretation": "The takedown is the moment force was actually applied, so focusing there could be a legitimate scoping choice tied to the injury being reviewed.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "primacy vs recency", "anchoring on final segment"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "In the case conference, the sergeant's strong early framing produces rapid convergence toward a shared 'likely justified' view; a peer investigator's dissenting concern about the BWC gap is raised but not pursued once the group direction is set, and the investigator adopts the consensus without documenting the unresolved concern.",
        "affected_reasoning_operation": "Group deliberation and consensus formation prior to a preliminary determination",
        "evidence_available_at_time": [
          "Sergeant's supervisory history and framing statement",
          "Peer investigator's flagged concern about the 40-second BWC gap",
          "Draft preliminary summary due to command"
        ],
        "required_textual_manifestation": "Investigator recounts the case conference discussion, notes the sergeant's early framing, mentions the dissenting concern being raised, and describes the group settling on a shared view without a documented follow-up on the dissent.",
        "plausible_nonbias_interpretation": "Team consensus could reflect genuinely convergent, independently-reasoned judgments rather than social pressure to conform.",
        "strength": "moderate",
        "do_not_make_explicit": ["groupthink", "social conformity pressure", "suppressed dissent"]
      },
      {
        "instance_id": "re_02",
        "bias": "Recency Effects",
        "decision_point": 4,
        "mechanism": "When finalizing the determination, the investigator gives the newly obtained (day 10) eyewitness statement disproportionate weight relative to the earlier, more extensive BWC record, because it was the most recently acquired piece of evidence.",
        "affected_reasoning_operation": "Final evidence-integration and re-weighting near decision closure",
        "evidence_available_at_time": [
          "Late-arriving civilian eyewitness statement (day 10)",
          "Full BWC footage reviewed on day 3",
          "Supplemental review noting eyewitness distance (35 feet)"
        ],
        "required_textual_manifestation": "Investigator describes the eyewitness statement as significantly shifting the picture in the final determination discussion, disproportionate to its evidentiary weight relative to the earlier, fuller BWC record.",
        "plausible_nonbias_interpretation": "New eyewitness testimony can legitimately warrant serious consideration, especially if it directly contradicts a prior characterization.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "most-recent-evidence weighting", "primacy vs recency"]
      },
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "decision_point": 4,
        "mechanism": "Having already delivered a preliminary briefing to the Deputy Chief indicating a likely exonerated finding, the investigator resolves the discomfort of new conflicting eyewitness evidence by minimizing its relevance rather than revising the previously communicated position, preserving consistency with the earlier commitment.",
        "affected_reasoning_operation": "Post-commitment evidence reconciliation and self-justification",
        "evidence_available_at_time": [
          "Preliminary briefing already delivered to command (day 8)",
          "New conflicting eyewitness statement (day 10)",
          "Command's request to confirm the preliminary briefing still stands"
        ],
        "required_textual_manifestation": "Investigator explains the decision to downplay the eyewitness account's relevance in a way that is tied to having already told command a different conclusion, rather than to an independent evidentiary reassessment.",
        "plausible_nonbias_interpretation": "A reasonable investigator might legitimately conclude the eyewitness account carries less weight due to distance and viewing conditions, independent of any prior commitment.",
        "strength": "moderate",
        "do_not_make_explicit": ["cognitive dissonance", "commitment consistency", "post-hoc rationalization"]
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
      "Confirm exactly 4 decision points, each with at least 2 stated alternatives.",
      "Confirm exactly 5 total bias instances embedded: 1 confirmation-bias/asymmetrical-skepticism, 2 recency-effect, 1 groupthink, 1 cognitive-dissonance.",
      "Confirm no bias name, definition, or psychological label appears in the public interview text.",
      "Confirm re_01 and re_02 use distinct evidence sources (BWC sequence weighting vs. late eyewitness statement weighting) and occur at different decision points.",
      "Confirm cd_01 and re_02 at decision point 4 are textually distinguishable: re_02 concerns evidentiary weighting, cd_01 concerns reconciliation with a prior committed position.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm final word count target of 1,350 words falls within 1,215-1,485 words.",
      "Confirm no unrequested bias (e.g., anchoring, hindsight bias) is intentionally embedded as a labeled instance."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Cognitive dissonance", "occurrences": 1, "mechanism_constraint": "Must manifest as reconciliation between a previously communicated preliminary position and new conflicting evidence, not merely discomfort acknowledgment." },
      { "bias": "Recency Effects", "occurrences": 2, "mechanism_constraint": "Each instance must involve a distinct evidence stream (sequential footage weighting vs. most-recently-obtained testimony weighting) at different decision points." },
      { "bias": "Groupthink", "occurrences": 1, "mechanism_constraint": "Must show rapid consensus formation with a dissenting view raised then not pursued." },
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "occurrences": 1, "mechanism_constraint": "Must show unequal verification effort applied to the two competing accounts at intake." }
    ],
    "target_bias_names": [
      "Cognitive dissonance",
      "Recency Effects",
      "Groupthink",
      "Confirmation Bias and Asymmetrical skepticism"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Cognitive dissonance", "requested_occurrences": 1 },
      { "bias": "Recency Effects", "requested_occurrences": 2 },
      { "bias": "Groupthink", "requested_occurrences": 1 },
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cbas_01", "bias": "Confirmation Bias and Asymmetrical skepticism" },
      { "instance_id": "re_01", "bias": "Recency Effects" },
      { "instance_id": "gt_01", "bias": "Groupthink" },
      { "instance_id": "re_02", "bias": "Recency Effects" },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance" }
    ],
    "intended_decision_points": [
      { "instance_id": "cbas_01", "bias": "Confirmation Bias and Asymmetrical skepticism", "decision_point": 1 },
      { "instance_id": "re_01", "bias": "Recency Effects", "decision_point": 2 },
      { "instance_id": "gt_01", "bias": "Groupthink", "decision_point": 3 },
      { "instance_id": "re_02", "bias": "Recency Effects", "decision_point": 4 },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cbas_01",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "mechanism": "Differential verification effort applied to complainant vs. officer accounts at intake",
        "affected_reasoning_operation": "Initial evidence-selection and credibility weighting",
        "evidence_source": "Complainant prior record vs. officer incident report",
        "distinctiveness_requirement": "Only instance of this bias; distinguished from recency/groupthink by occurring at intake before any footage or group deliberation."
      },
      {
        "instance_id": "re_01",
        "bias": "Recency Effects",
        "mechanism": "Anchoring proportionality judgment on the final segment of a sequential footage review",
        "affected_reasoning_operation": "Integration/weighting of sequential BWC evidence",
        "evidence_source": "18-minute BWC footage, final 90-second segment vs. earlier de-escalation minutes",
        "distinctiveness_requirement": "Must be distinguished from re_02 by evidence type (footage sequence) and decision point (2, not 4)."
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Rapid group consensus formation under supervisory framing, with dissent raised then unpursued",
        "affected_reasoning_operation": "Group deliberation and consensus formation",
        "evidence_source": "Case conference dialogue: sergeant's framing, peer investigator's flagged BWC-gap concern",
        "distinctiveness_requirement": "Only instance of this bias; distinguished from cd_01 by occurring in the shared group setting rather than an individual post-commitment reconciliation."
      },
      {
        "instance_id": "re_02",
        "bias": "Recency Effects",
        "mechanism": "Disproportionate weighting of the most recently obtained eyewitness statement relative to the earlier, fuller BWC record",
        "affected_reasoning_operation": "Final evidence-integration near decision closure",
        "evidence_source": "Day-10 eyewitness statement vs. day-3 BWC review",
        "distinctiveness_requirement": "Must be distinguished from re_01 by evidence type (testimony vs. footage) and decision point (4, not 2)."
      },
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "mechanism": "Minimizing new conflicting evidence to preserve consistency with an already-communicated preliminary position to command",
        "affected_reasoning_operation": "Post-commitment evidence reconciliation and self-justification",
        "evidence_source": "Prior preliminary briefing to Deputy Chief vs. new eyewitness statement",
        "distinctiveness_requirement": "Must be distinguished from re_02 by reasoning operation: re_02 is a weighting error, cd_01 is a consistency-preserving reconciliation tied to a prior stated commitment."
      }
    ],
    "intended_strength": [
      { "instance_id": "cbas_01", "bias": "Confirmation Bias and Asymmetrical skepticism", "strength": "subtle" },
      { "instance_id": "re_01", "bias": "Recency Effects", "strength": "subtle" },
      { "instance_id": "gt_01", "bias": "Groupthink", "strength": "moderate" },
      { "instance_id": "re_02", "bias": "Recency Effects", "strength": "subtle" },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Biased_5",
    "domain_id": "LE",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across distinct decision points wherever mechanism fit allowed one instance per point (DP1: confirmation/asymmetrical skepticism; DP2: recency #1; DP3: groupthink); the two remaining occurrences (recency #2, cognitive dissonance) were co-located at DP4 because that is the narratively natural point of final determination, but were required to use distinct evidence sources and reasoning operations (evidentiary re-weighting vs. commitment-consistency reconciliation) per the shared-decision-point rule.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": [
      "Decision point 4 hosts two distinct bias instances (re_02 and cd_01) because the final determination phase is the only narratively defensible point for both a late-arriving-evidence weighting error and a post-commitment reconciliation; they are documented as using different evidence sources and reasoning operations to satisfy the instance-independence rule, but validators should pay close attention to their separability in the generated text."
    ]
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "seg_dp1_intake_asymmetric_scrutiny",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "I requested his full arrest history and looked for anything that might explain inconsistency in his statement... For Marquez, I ... treated his report as the operational starting point",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cbas_01"
          ],
          "ground_truth_rationale": "The investigator sought adverse background detail on Alvarez while accepting Marquez's report as the baseline without equivalent independent verification, matching the hidden differential-scrutiny mechanism."
        },
        {
          "segment_id": "seg_dp2_bwc_final_sequence",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "The takedown is what matters for a force review... My working read was built mainly around those last ninety seconds.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "re_01"
          ],
          "ground_truth_rationale": "The investigator gave the final 90-second takedown disproportionate weight relative to the earlier sequential footage, matching the first recency instance."
        },
        {
          "segment_id": "seg_dp3_case_conference_consensus",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "The conversation moved pretty quickly toward the take that the force was likely justified... We didn't formally table the gap as an open item.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "gt_01"
          ],
          "ground_truth_rationale": "The investigator adopted the sergeant-led consensus, left the BWC gap and peer reservation undocumented, and allowed group momentum to determine the preliminary direction."
        },
        {
          "segment_id": "seg_dp4_late_witness_reconciliation",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "It was the freshest account I had at that point, closer in my mind than the footage... so it carried a lot of weight",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "re_02",
            "cd_01"
          ],
          "ground_truth_rationale": "The late eyewitness was weighted because of its freshness, while the investigator separately minimized the conflict to preserve the exonerated-leaning briefing already sent to command."
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
    "analysis_scope_note": "Analysis of the participant's self-reported reasoning and decision-making during an Internal Affairs use-of-force complaint review."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Conformity bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Escalation of commitment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Recency effect",
      "identified_occurrence_count": 2
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory hypothesis testing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and structure evidence in ways that confirm an existing hypothesis or starting account.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial intake and background review",
      "decision_point_description": "Choosing which account to treat as the primary hypothesis and how to structure background verification.",
      "affected_reasoning_operation": "Evidence search and hypothesis framing during case intake",
      "bias_specific_mechanism": "The participant treated the officer's formal report as the primary account to be confirmed or contradicted, creating asymmetric evidence gathering that focused more on testing the complainant than on independently testing the officer's account.",
      "manifestation_in_interview": "The participant reported using Officer Marquez's report as the operational starting point and building the review around confirming or contradicting it, rather than opening a parallel background pull on the officer.",
      "effect_on_reasoning_or_decision": "The review was structured around the officer's account as the baseline, reducing early independent scrutiny of Marquez's version.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "For Marquez, I already had the two priors in the system, both unfounded, so I treated his report as the operational starting point and built the review around confirming or contradicting it rather than opening a parallel background pull on him the same way.",
          "evidence_explanation": "This explicitly describes an asymmetric hypothesis-testing structure in which the officer's report is the account to be confirmed or contradicted, a core manifestation of confirmation bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mean, his report exists, it's the formal record, that's the baseline you work from. Alvarez's statement is what's being tested. I don't think I consciously decided to treat them differently—it's just how intake usually goes.",
          "evidence_explanation": "The participant frames the complainant's account as the object of testing while treating the officer's report as the baseline, showing asymmetrical evidence treatment even if not consciously chosen."
        }
      ],
      "correction_or_counterevidence": "The participant said he did not consciously decide to treat the two accounts differently and described the approach as typical intake practice. This suggests institutional routine may contribute, but does not eliminate the confirmatory structure of the reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages mention confirmation bias but do not provide an adequate mechanism definition; the label and definition therefore derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Recency effect",
      "alternative_labels": [
        "Recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for recent events or information to be remembered more clearly and weighted more heavily than earlier information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "BWC footage review and initial assessment formation",
      "decision_point_description": "Weighting the early stop interaction versus the final takedown segment when forming the force-review assessment.",
      "affected_reasoning_operation": "Attention allocation and evidence weighting during video review",
      "bias_specific_mechanism": "The final 90-second takedown sequence was watched last and replayed repeatedly, making it more cognitively accessible than earlier footage and leading the participant to overweight it in his working read.",
      "manifestation_in_interview": "The participant replayed only the final segment multiple times and said it was closer to the front of his mind than the earlier footage, so his working read was built mainly around those last 90 seconds.",
      "effect_on_reasoning_or_decision": "Earlier interaction footage was underweighted, including the pre-takedown positioning later flagged as relevant to the reasonableness call.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the takedown is what matters for a force review—that's the moment the fracture occurred, so that's where I put most of my attention. I ended up running that last segment back three or four times to get the mechanics right, and by the time I moved on, it was just sitting closer to the front of my mind than anything from the first part of the stop.",
          "evidence_explanation": "The participant explicitly states that recent, repeatedly reviewed footage was more mentally accessible than earlier footage, which is the mechanism of the recency effect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My working read was built mainly around those last ninety seconds.",
          "evidence_explanation": "This directly links the recency-driven mental availability of the final segment to the participant's overall assessment."
        }
      ],
      "correction_or_counterevidence": "Later slowed-frame audio showed earlier escalation by the officer, including raised voice and encroachment into the subject's space, which the participant had not weighted during the initial footage review.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": null,
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Recent events are remembered more clearly and therefore can disproportionately influence judgment.",
          "relevance_to_this_occurrence": "The participant reports that the final 90 seconds of footage were closer to the front of his mind and drove his working read, consistent with the recency effect mechanism described in the retrieved passage."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Conformity bias",
      "alternative_labels": [
        "Bandwagon effect",
        "Social proof"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to align one's judgment with perceived group consensus or the framing of a senior colleague, reducing independent critical evaluation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Case conference discussion of BWC gap and preliminary direction",
      "decision_point_description": "Deciding whether to formally flag the BWC gap and whether to adopt the room's likely-justified direction.",
      "affected_reasoning_operation": "Group judgment and direction-setting during case conference",
      "bias_specific_mechanism": "The sergeant's authority-tinged framing and perceived group momentum made the likely-justified direction feel sensible, reducing the participant's willingness to hold up the decision over the BWC gap.",
      "manifestation_in_interview": "The participant reported that the sergeant's framing set the tone, the conversation moved quickly toward likely justified force, and the participant did not feel a strong reason to hold the decision up.",
      "effect_on_reasoning_or_decision": "The BWC gap was not formally tabled as an open item, and the preliminary summary was drafted along the room's likely-justified direction within the required 48-hour window.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The sergeant supervised Marquez for three years and opened by saying Marquez has 'never been a problem,' which set kind of a tone.",
          "evidence_explanation": "This shows a senior colleague with a prior relationship framed the officer favorably at the outset, a social influence cue that shaped the room's starting point."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We talked about it briefly, but the conversation moved pretty quickly toward the take that the force was likely justified given Chen's corroboration and the resisting motion on camera. We didn't formally table the gap as an open item.",
          "evidence_explanation": "The group moved quickly toward consensus and did not preserve the dissenting concern as an open item, indicating movement toward group direction rather than holding independent scrutiny."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think once the sergeant framed it that way and Chen's report backed it up, the momentum was already there. It felt like the sensible read given everyone's read of the tape. I didn't feel like there was a strong reason to hold it up.",
          "evidence_explanation": "The participant explicitly attributes his alignment to the sergeant's framing and group momentum, the core mechanism of conformity bias."
        }
      ],
      "correction_or_counterevidence": "A peer investigator raised the BWC gap and later privately expressed continued reservations, showing that not everyone in the room fully agreed; however, the participant did not document that follow-up and still aligned with the group direction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No suitable retrieved passage directly addressed conformity or group momentum; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Recency effect",
      "alternative_labels": [
        "Recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for recent events or information to be remembered more clearly and weighted more heavily than earlier information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Integration of late-arriving eyewitness statement",
      "decision_point_description": "Determining how much weight to give the eyewitness statement when finalizing review language.",
      "affected_reasoning_operation": "Evidence weighting during finalization of review language",
      "bias_specific_mechanism": "The newly received eyewitness statement was the freshest account and therefore more cognitively accessible than the footage reviewed earlier in the week, causing it to carry disproportionate weight in finalization conversations.",
      "manifestation_in_interview": "The participant stated that the new statement was the freshest account, closer in his mind than the day-three footage, and that it carried a lot of weight in the conversations finalizing language.",
      "effect_on_reasoning_or_decision": "The late eyewitness statement became highly influential in finalization discussions despite being received after the participant had already formed and reported a preliminary conclusion.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It shifted things somewhat. It was the freshest account I had at that point, closer in my mind than the footage I'd reviewed back on day three, so it carried a lot of weight in the conversations we had finalizing language.",
          "evidence_explanation": "The participant explicitly explains that the recency of the account made it more mentally accessible and influential, matching the recency effect mechanism."
        }
      ],
      "correction_or_counterevidence": "The same eyewitness account was later discounted in part due to commitment to the prior briefing, which is a separate escalation-of-commitment mechanism rather than a correction of the recency effect.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": null,
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Recent events are remembered more clearly and therefore can disproportionately influence judgment.",
          "relevance_to_this_occurrence": "The participant states that the freshest account was closer in mind than earlier footage and therefore carried disproportionate weight, matching the recency mechanism described in the retrieved passage."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Escalation of commitment",
      "alternative_labels": [
        "Commitment bias",
        "Consistency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to maintain or defend a prior decision or publicly stated conclusion despite new conflicting evidence, often to avoid admitting error or reversing a prior commitment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-eyewitness decision to retain preliminary briefing",
      "decision_point_description": "Whether to revise the preliminary briefing given the new eyewitness statement and supplemental review.",
      "affected_reasoning_operation": "Evaluation of contradictory evidence and decision to revise or retain the prior conclusion",
      "bias_specific_mechanism": "The participant had already briefed the Deputy Chief with confidence and framed that as a commitment; to avoid walking back the prior statement, he evaluated the new evidence as less determinative and kept the briefing largely unchanged.",
      "manifestation_in_interview": "The participant discounted the eyewitness statement using distance and lighting and kept the briefing largely as it was, while explicitly admitting part of that was probably not wanting to walk back something already told to command.",
      "effect_on_reasoning_or_decision": "Contradictory eyewitness evidence was not fully integrated, and the preliminary briefing remained essentially unchanged.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned toward treating her statement as less determinative—distance, lighting, that kind of thing—and kept the briefing largely as it was. I'll admit part of that was probably about not wanting to walk back something I'd already told command with some confidence. Revising it at that point would've meant explaining why my read had changed, and I didn't feel the new statement was strong enough on its own to justify that.",
          "evidence_explanation": "The participant explicitly links the decision to maintain the prior briefing to the desire to avoid walking back a statement already made with confidence, which is the central escalation-of-commitment mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant also stated that the new statement did not feel strong enough on its own to justify revision, a plausible non-bias factor. However, he explicitly identified his own reluctance to walk back the prior briefing as part of the reason.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages mention plan continuation in aviation but do not provide an adequate mechanistic definition for escalation of commitment; the label and mechanism therefore derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Only one participant interview was analyzed; there was no independent verification of case records or outcomes.",
    "The retrieved corpus support was limited, and several bias labels rely on general cognitive-science knowledge because corpus-based definitions were unavailable.",
    "The analysis is based on self-report, which may be incomplete, post hoc, or shaped by the participant's later reflections.",
    "Some mechanisms co-occur in overlapping reasoning episodes, so the boundaries between identified biases are interpretive."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Biased_5_Sonar_on",
  "interview_id": "LE_Biased_5",
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
