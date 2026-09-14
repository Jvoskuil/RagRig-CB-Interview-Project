You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time. This is a debrief for our analytic process review — walk me through a specific incident, how you reasoned through it, and what information you had at each point. No scoring, and you can decline anything you're not comfortable with.

Participant: Sure. Which case did you want to go through?

Interviewer: The marathon threat stream from earlier this year — the walk-in tip that came in about 72 hours before the event. Can you set the scene? What was going on at the fusion center?

Participant: That week we were stretched thin. Most analysts were pulled onto the gang-violence surge, which had been running about three weeks and eating our bandwidth. So when the walk-in report came in, I had two people, including myself, available in real time. The source was brand new, no reporting history, no reliability rating yet. He came into the regional office and said there was a device hidden near the finish-line corridor of the marathon route. That was the whole tip — no timeline, no actor description, just that location and the claim.

Interviewer: What was your first reaction?

Participant: My first thought was, this is the most concrete thing we've got, so let's build around it. We had no SIGINT yet, and nothing in the JTTF threat matrix pointed at this event. The corridor mention was the one piece of actionable intelligence in front of me.

Interviewer: Walk me through what happened next, in sequence.

Participant: First day, we get the tip and I task collection. Second day, I call our senior JTTF liaison for his read. That afternoon we pulled the team together to decide what to tell the Director and how to size the resource ask. Third day morning is the bulletin deadline — I drafted it and briefed it before the event.

Interviewer: Let's take those in turn. Starting with the tip — what did you decide about collection tasking?

Participant: I directed our SIGINT request and HUMINT follow-up specifically at the finish-line corridor. That's where he said the device was, so that's where I wanted eyes.

Interviewer: What alternatives did you consider?

Participant: We talked about spreading collection across the whole event footprint instead of narrowing in, since the source had zero track record. But with only two of us, spreading thin felt like it would get us nothing anywhere. Narrowing to the corridor at least gave us a shot at confirming or knocking down something specific.

Interviewer: Did anything come in afterward that touched on that decision?

Participant: Yeah. Later that first day a partial SIGINT hit came back from a channel we normally trust, and it referenced route security for the marathon generally, but the location was a different sector, about two miles up from the corridor he named. I logged it but didn't reassign the team to it. It didn't fit the tip, so I treated it as probably a separate, unrelated signal and kept the corridor as the priority.

Interviewer: What made you treat it as unrelated rather than a second piece of the same picture?

Participant: The channel's usually solid and it did touch on the event, so it wasn't nothing. But by then the corridor was already what we were working toward, and I didn't reopen the location question — I filed it as a separate thread and stayed on the one we already had detail on.

Interviewer: Moving to the liaison call — what did that add?

Participant: He's got over twenty years in this, worked several of the region's thwarted plots directly. He heard the tip summary, said it resembled the pattern from a plot broken up about two years back, and recommended elevating the threat level.

Interviewer: Did your team independently compare that earlier case to this tip before acting on his recommendation?

Participant: Not really — we hadn't pulled the case file yet. But he's the one who worked that case directly, so when he says it resembles the pattern, that carries weight. I took his read and recommended to the Director that we elevate.

Interviewer: What led you to recommend elevation without the case comparison first?

Participant: Time, mostly. If someone with his background tells you it looks familiar, you don't sit on that while digging through old files. I trusted the call.

Interviewer: Was that comparison checked afterward?

Participant: It was, later. The earlier case was a vehicle-borne device against a different target type — tactic and target didn't line up with this tip at all. The resemblance turned out to be surface-level rather than substantive.

Interviewer: Tell me about the team meeting where you decided how to characterize the threat.

Participant: Tense. We had maybe forty minutes before the Director needed something. A junior analyst raised the corroboration gap — the SIGINT mismatch and the unverified case comparison — and asked for another 24 hours before escalating further.

Interviewer: What happened with that request?

Participant: We discussed it for a few minutes, but the room was mostly already leaning toward moving forward — people nodding, the liaison's read still fresh, no 24 hours to spare with the deadline coming. We reached agreement quickly and moved to the resource ask. I didn't write her concern into the formal notes — not because she was wrong, but because a documented disagreement in front of the Director would have muddied a recommendation we needed unified. We just moved on once the room was aligned.

Interviewer: How did you decide how to present the resource request?

Participant: I framed it as roughly a ten percent chance of an incident, rather than a ninety percent chance everything goes fine. Same numbers, different emphasis. I went with the version that made the risk concrete because the Director responds to clear, decisive figures rather than reassurance-sounding ones.

Interviewer: Did that framing affect what got approved?

Participant: It did — we got a fairly large surge in patrol and screening approved off that ask. When I read the number out as roughly one-in-ten, the Director cut in and said that was exactly the figure he needed to justify pulling resources on short notice, and asked me to keep the sheet in those terms going forward. If I'd led with the ninety-percent-safe version, I don't think it would've carried the same urgency — the numbers were identical, just how I said them.

Interviewer: Now the bulletin. What did the final draft say, and how did you land on that language?

Participant: We were against the deadline, no new corroboration had come in, the location mismatch was still unresolved, and her dissent hadn't been revisited. I still drafted the bulletin naming the corridor specifically as the likely target, with fairly strong, high-confidence language.

Interviewer: How sure did you feel about that assessment when you briefed it?

Participant: Honestly, pretty sure. I stated it with real confidence. When you're the one who has to say something in front of the Director and the event organizers, hedging doesn't land well.

Interviewer: Looking at the open items — the mismatch, the unverified comparison, the unresolved dissent — how do those square with the confidence you briefed?

Participant: I'll be honest, those things were never fully closed out. We went into the bulletin with those loose ends still there. I stand by acting decisively given the clock, but the underlying picture wasn't as clean as the language I used suggested.

Interviewer: What happened at the event?

Participant: Nothing. No device, no incident, anywhere on the route, including the corridor we named. Whether the extra patrols deterred something or there was never anything there to begin with, I honestly can't say.

Interviewer: A few hypotheticals. If the source had been vaguer about location, how would your collection tasking have gone differently?

Participant: Probably would have stayed broader across the whole footprint instead of narrowing to one corridor. The specificity is what pulled us that direction.

Interviewer: If a more junior person had made that pattern comparison instead of the liaison, would your recommendation have changed?

Participant: Probably — I think I'd have asked for the case file comparison before elevating, rather than moving straight on the recommendation.

Interviewer: If the dissent had been formally logged and circulated before the resource discussion, would the meeting have gone differently?

Participant: Maybe. It's possible we'd have slowed down. Hard to say for sure.

Interviewer: Looking back, would you phrase the resource request the same way?

Participant: I'd think harder about it now. At the time it didn't feel like a meaningful choice — just how to say the same thing.

Interviewer: Last one — what would have made you issue a lower-confidence bulletin?

Participant: If the case comparison had checked out, or the SIGINT had actually matched the location, I'd have felt more solid going in strong. Without that, I probably should have flagged the gaps more than I did.

Interviewer: That's really helpful, thank you.

Participant: No problem.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Biased_5",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Counterterrorism Analyst (Team Lead, Fusion Center)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The 72-Hour Marathon Threat Stream",
    "scenario_summary_internal": "A regional fusion center's counterterrorism team lead receives an uncorroborated walk-in tip warning of a possible attack tied to a major public marathon occurring in 72 hours. Under staffing pressure from a concurrent gang-violence surge and a hard event deadline, the team lead triages the tip, consults a senior JTTF liaison, runs a rushed team meeting to characterize the threat and request resources, and finally drafts the pre-event threat bulletin. The interview reconstructs this chronology and probes the analyst's reasoning at each juncture without ever naming or explaining the biases embedded in the narrative.",
    "occupational_realism": {
      "objective": "Determine whether an uncorroborated tip about a possible attack on a public marathon within 72 hours warrants escalation, resource reallocation, and a formal threat bulletin, while managing a competing open investigation and limited staff.",
      "setting": "Regional multi-agency fusion center supporting a metropolitan police department, FBI Joint Terrorism Task Force (JTTF) liaison office, and city event-security coordination, three days before a large public marathon.",
      "constraints": [
        "72-hour window before the marathon with no ability to postpone the event",
        "Analyst team is short-staffed because most personnel are pulled into an ongoing gang-violence surge investigation",
        "Only one new, previously unused walk-in source with no track record",
        "Partial and ambiguous SIGINT corroboration that does not cleanly match the tip's specifics",
        "Political pressure from city officials wanting either reassurance or decisive action, not ambiguity",
        "Hard deadline for issuing a pre-event situational awareness bulletin"
      ],
      "stakeholders": [
        "Fusion Center Director",
        "Senior JTTF Liaison",
        "Junior Intelligence Analyst (dissenting voice)",
        "City Police Counterterrorism Unit Commander",
        "Marathon event organizers and city officials",
        "Patrol and event-security field commanders"
      ],
      "technical_terms_to_use": [
        "walk-in source",
        "HUMINT",
        "SIGINT",
        "corroboration",
        "threat stream",
        "indicators and warnings (I&W)",
        "threat matrix",
        "JTTF",
        "situational awareness bulletin",
        "confidence level",
        "actionable intelligence",
        "tearline",
        "source reliability rating"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "anchoring",
        "framing",
        "groupthink",
        "overconfidence",
        "authority bias",
        "cognitive",
        "psychology",
        "confirmation"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "New walk-in source with no prior reporting history claims a device is 'hidden near the finish-line corridor' of the marathon route",
          "Source reliability rating is unassigned pending vetting",
          "No SIGINT or other corroboration yet reviewed"
        ],
        "new_information_after_decision": [
          "A later SIGINT partial hit surfaces in a different sector of the route, roughly two miles from the named finish-line corridor",
          "The SIGINT hit is logged but not re-tasked as a primary collection priority"
        ],
        "alternatives": [
          "Treat the tip as low-confidence pending corroboration and direct broad collection across the entire event footprint",
          "Lock collection scope immediately to the specific corridor named by the source"
        ],
        "intended_action": "Analyst directs all follow-up SIGINT and HUMINT tasking to the named finish-line corridor based on the source's specific wording, and downweights the later hit in a different sector as likely unrelated."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Senior JTTF liaison, with 20 years of counterterrorism experience, reviews the tip and states it 'resembles the pattern' of a plot thwarted two years earlier",
          "Liaison recommends elevating the internal threat level based on this resemblance",
          "No independent comparison of tactic, target type, or actor profile has been completed by the analyst's own team"
        ],
        "new_information_after_decision": [
          "A subsequent case-file review shows the earlier thwarted plot involved a different tactic (vehicle-borne device vs. this tip's claimed placed device) and a different target type",
          "The resemblance is later assessed as superficial rather than substantive"
        ],
        "alternatives": [
          "Independently re-verify the source's reliability and the substance of the pattern match before recommending escalation to the Director",
          "Elevate the threat level on the liaison's recommendation without independent re-verification, given his seniority and track record"
        ],
        "intended_action": "Analyst recommends elevating the threat level to the Fusion Center Director primarily on the strength of the liaison's seniority and stated resemblance, without independently re-checking the pattern match."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Team meets under time pressure to decide how to characterize the threat and what resources to request",
          "A junior analyst raises the corroboration gap (mismatched location, superficial pattern match) and requests 24 more hours before escalating",
          "Team lead must phrase the resource request to the Director and city officials"
        ],
        "new_information_after_decision": [
          "The Director approves a large surge in patrol and screening resources based on the phrasing used",
          "A retrospective review later notes that an equivalent request phrased around the probability of a safe event, rather than the probability of an attack, might have received a smaller or delayed resource allocation"
        ],
        "alternatives": [
          "Formally log the junior analyst's dissent and request the additional 24 hours for corroboration before finalizing a resource ask",
          "Reach quick unanimous agreement to escalate immediately, closing discussion once the majority view emerges",
          "Present the resource request framed around the probability of an attack occurring",
          "Present the same underlying evidence framed around the probability of the event proceeding safely"
        ],
        "intended_action": "The team quickly converges on immediate escalation without formally recording the dissent, and the team lead frames the request to leadership in terms of attack probability, which noticeably increases the resources approved."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Deadline for the pre-event situational awareness bulletin has arrived",
          "Unresolved contradictions remain: location mismatch, superficial pattern match, unlogged dissent",
          "No new corroborating source has emerged in the final hours"
        ],
        "new_information_after_decision": [
          "The marathon proceeds without any incident at the named corridor or elsewhere on the route",
          "It remains unresolved whether the protective posture deterred an actual plot or whether no credible plot existed at all"
        ],
        "alternatives": [
          "Issue the bulletin with calibrated, moderate-confidence language that explicitly flags the unresolved corroboration gaps",
          "Issue the bulletin with high-confidence language stating an attack at the named corridor is highly likely, to maximize protective posture"
        ],
        "intended_action": "Analyst issues a high-confidence bulletin naming the specific corridor as the likely target, despite the unresolved gaps, stating strong personal confidence in the assessment during the pre-event briefing."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this tip first came to your attention.",
        "What was your initial read on the situation, before you did anything else?"
      ],
      "timeline_reconstruction": [
        "What happened right after you received the walk-in report?",
        "What did the liaison call add to your understanding, and when did it happen relative to the team meeting?",
        "What was decided in the team meeting, and how did that lead to the final bulletin?"
      ],
      "decision_point_probes": [
        "What specific cues in the source's statement drove where you focused collection? (Phase 1)",
        "What other information sources did you consider consulting before locking the collection scope? (Phase 1)",
        "What was your goal in accepting or questioning the liaison's pattern comparison? (Phase 2)",
        "What alternatives did you weigh before recommending escalation to the Director? (Phase 2)",
        "What was the basis for closing discussion so quickly in the team meeting? (Phase 3)",
        "How did you decide how to phrase the resource request to leadership? (Phase 3)",
        "How much time pressure did you feel finalizing the bulletin, and how did that affect the confidence language you chose? (Phase 4)",
        "What uncertainty remained at the time you issued the bulletin, and how did you communicate it? (Phase 4)"
      ],
      "closing_hypotheticals": [
        "If the walk-in source's statement had been vaguer about location, how do you think your collection tasking would have differed?",
        "If a less senior person had made the pattern comparison, would your recommendation have changed?",
        "If the junior analyst's dissent had been formally logged and circulated, do you think the outcome of the meeting would have changed?",
        "Looking back, would you phrase the resource request the same way if you had to do it again?",
        "What would have made you issue a lower-confidence bulletin?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Analyst's downstream collection scope and interpretation remain fixed on the source's initial specific claim (the named corridor), causing later, non-confirming SIGINT information from a different sector to be discounted rather than triggering a scope re-evaluation.",
        "affected_reasoning_operation": "Evidence weighting and collection prioritization following initial exposure to a specific numeric/locational claim",
        "evidence_available_at_time": [
          "Uncorroborated walk-in claim naming a specific corridor",
          "No source reliability rating yet assigned",
          "Later partial SIGINT hit in a different route sector, received after scope was already locked"
        ],
        "required_textual_manifestation": "Analyst explicitly explains locking tasking to the named corridor because of the source's specific wording, and explains downweighting the later SIGINT hit as 'probably unrelated' without giving an independent evidentiary reason for the dismissal.",
        "plausible_nonbias_interpretation": "Focusing scarce collection resources on the most specific, actionable detail available is a defensible triage heuristic under time pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "first number", "initial estimate"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Authority Bias or Authority Obedience",
        "decision_point": 2,
        "mechanism": "Analyst adopts and forwards the senior liaison's pattern-match conclusion and escalation recommendation primarily because of the liaison's seniority and reputation, rather than because of independently verified evidentiary similarity.",
        "affected_reasoning_operation": "Acceptance and forwarding of a threat assessment without independent verification of its evidentiary basis",
        "evidence_available_at_time": [
          "Liaison's verbal assertion of pattern resemblance to a past thwarted plot",
          "No independent case-file comparison completed at the time of the recommendation",
          "Liaison's stated seniority and prior track record"
        ],
        "required_textual_manifestation": "Analyst states that the recommendation was adopted because the liaison 'has seen this before' and has 20 years of experience, without describing any independent check of the tactic or target-type match before escalating.",
        "plausible_nonbias_interpretation": "Deferring to a demonstrably experienced colleague under time pressure is a reasonable use of expertise and division of labor.",
        "strength": "subtle",
        "do_not_make_explicit": ["authority", "deference", "seniority bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "The team reaches rapid unanimous agreement to escalate immediately, and the dissenting junior analyst's corroboration concerns are not formally logged, discussed, or resolved before the group moves to consensus.",
        "affected_reasoning_operation": "Group decision convergence and handling of dissenting input under time pressure",
        "evidence_available_at_time": [
          "Junior analyst's stated concern about location mismatch and superficial pattern match",
          "Explicit request for 24 more hours of corroboration",
          "Time pressure from the approaching bulletin deadline"
        ],
        "required_textual_manifestation": "Analyst describes the meeting moving quickly to agreement once 'most people were on the same page,' and confirms the junior analyst's dissent was not written into the record or revisited before the group finalized its position.",
        "plausible_nonbias_interpretation": "Reaching quick alignment under a hard deadline is a practical necessity when the team must act before the event begins.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "consensus pressure", "suppressed dissent"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Framing effects",
        "decision_point": 3,
        "mechanism": "The identical underlying evidence produces a larger resource request when the team lead phrases it in terms of probability of an attack occurring rather than probability of the event proceeding safely, and the analyst chooses the attack-probability phrasing without treating the choice of framing as consequential.",
        "affected_reasoning_operation": "Communication and packaging of a probability estimate to decision-makers, distinct from the group-consensus process itself",
        "evidence_available_at_time": [
          "Same underlying threat-matrix data available under either phrasing",
          "Director's known preference for clear, decisive language",
          "Awareness that phrasing affects how much resource leadership tends to approve"
        ],
        "required_textual_manifestation": "Analyst recalls choosing to present the request as '10% chance of an incident' rather than '90% chance the event proceeds safely' and notes, in hindsight, that the size of the approved resource surge might have differed under the alternate phrasing, without treating this as evidentiarily meaningful.",
        "plausible_nonbias_interpretation": "Choosing vivid, decision-actionable language for leadership is a normal communication practice in briefings.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "loss framing", "gain framing"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Analyst issues a high-confidence bulletin and expresses strong personal certainty about the specific corridor being the target, despite openly acknowledged unresolved contradictions in the evidence base at the time of drafting.",
        "affected_reasoning_operation": "Calibration of stated confidence level relative to the actual strength and completeness of supporting evidence",
        "evidence_available_at_time": [
          "Unresolved location mismatch between the tip and the SIGINT hit",
          "Superficial, unverified pattern match from Phase 2",
          "Unlogged dissent from Phase 3",
          "No new corroboration in the final hours before the deadline"
        ],
        "required_textual_manifestation": "Analyst describes drafting the bulletin with high-confidence language naming the specific corridor and recalls feeling 'very sure' of the assessment during the briefing, despite acknowledging, when asked, that the underlying contradictions were never resolved.",
        "plausible_nonbias_interpretation": "Under a hard deadline with no time for further corroboration, decisive language can be operationally necessary to drive protective action.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence", "miscalibration", "confidence bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control variant."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable",
      "original_state": "Not applicable",
      "counterfactual_state": "Not applicable",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "Not applicable",
      "causal_test_question": "Not applicable"
    },
    "generation_checks": [
      "Interview must contain exactly four decision points corresponding to Phases 1-4.",
      "No bias name, definition, or psychological term may appear in the public interview text.",
      "Each of the five planned instances (cb_01 through cb_05) must be independently identifiable from distinct textual evidence tied to its assigned decision point.",
      "Decision Point 3 must contain two distinct, separately identifiable manifestations (cb_03 Groupthink, cb_04 Framing effects) tied to different reasoning operations (group consensus vs. message framing), not a single blended passage.",
      "Consequences (safe event outcome) must be presented as inconclusive regarding whether any decision was biased.",
      "Total interview length must fall between 1,215 and 1,485 words, with target 1,350 words.",
      "Probes must cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes across the four decision points.",
      "No additional, unrequested instance of any of the five named biases may be introduced in probes, hypotheticals, or the outcome narration."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Authority Bias or Authority Obedience",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as adoption of the senior liaison's conclusion due to seniority/reputation rather than independent verification, at Decision Point 2."
      },
      {
        "bias": "Framing effects",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as differential resource-request outcome tied to attack-probability vs. safety-probability phrasing, at Decision Point 3, distinct from the consensus-formation process."
      },
      {
        "bias": "Groupthink",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as rapid unanimous convergence with unlogged/unresolved dissent, at Decision Point 3, distinct from the framing choice."
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as stated high personal confidence in the bulletin despite acknowledged unresolved evidentiary contradictions, at Decision Point 4."
      },
      {
        "bias": "Anchoring Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as fixation on the initial source's specific locational claim causing discounting of later non-confirming SIGINT, at Decision Point 1."
      }
    ],
    "target_bias_names": [
      "Authority Bias or Authority Obedience",
      "Framing effects",
      "Groupthink",
      "Overconfidence Bias",
      "Anchoring Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Authority Bias or Authority Obedience", "requested_occurrences": 1 },
      { "bias": "Framing effects", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Anchoring Bias" },
      { "instance_id": "cb_02", "bias": "Authority Bias or Authority Obedience" },
      { "instance_id": "cb_03", "bias": "Groupthink" },
      { "instance_id": "cb_04", "bias": "Framing effects" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Authority Bias or Authority Obedience", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Groupthink", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Framing effects", "decision_point": 3 },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Anchoring Bias",
        "mechanism": "Fixation on the initial source's specific corridor claim causes discounting of a later non-confirming SIGINT hit rather than a scope re-evaluation.",
        "affected_reasoning_operation": "Evidence weighting and collection prioritization",
        "evidence_source": "Walk-in source's initial specific claim vs. later SIGINT hit in a different sector",
        "distinctiveness_requirement": "Only instance involving the initial tip's specific claim and its effect on collection scope; must not overlap with the liaison's pattern-match assessment (cb_02)."
      },
      {
        "instance_id": "cb_02",
        "bias": "Authority Bias or Authority Obedience",
        "mechanism": "Analyst forwards the senior liaison's escalation recommendation based on seniority/reputation rather than independent verification of the pattern match.",
        "affected_reasoning_operation": "Acceptance and forwarding of an assessment without independent verification",
        "evidence_source": "Senior liaison's verbal pattern-match assertion and stated experience",
        "distinctiveness_requirement": "Only instance tied to deference toward the liaison specifically; must not overlap with team-meeting consensus dynamics (cb_03)."
      },
      {
        "instance_id": "cb_03",
        "bias": "Groupthink",
        "mechanism": "Rapid unanimous convergence in the team meeting with the junior analyst's dissent left unlogged and unresolved.",
        "affected_reasoning_operation": "Group decision convergence and handling of dissenting input",
        "evidence_source": "Junior analyst's dissent and request for 24 more hours, and how the group closed discussion",
        "distinctiveness_requirement": "Only instance tied to the process of reaching group consensus; must be textually separable from the framing/phrasing choice (cb_04) even though both occur in Phase 3."
      },
      {
        "instance_id": "cb_04",
        "bias": "Framing effects",
        "mechanism": "Identical underlying evidence yields a different resource-approval outcome depending on attack-probability vs. safety-probability phrasing choice by the team lead.",
        "affected_reasoning_operation": "Packaging and communication of a probability estimate to decision-makers",
        "evidence_source": "Team lead's choice of phrasing in the resource request and the Director's resulting approval",
        "distinctiveness_requirement": "Only instance tied to the wording/presentation choice, not to the act of reaching group agreement (cb_03); must reference the specific phrasing comparison as its own evidence trace."
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "mechanism": "Analyst states strong personal confidence in the final bulletin's specific-corridor claim despite acknowledged unresolved contradictions.",
        "affected_reasoning_operation": "Calibration of stated confidence relative to actual evidentiary completeness",
        "evidence_source": "Final bulletin drafting and pre-event briefing statements",
        "distinctiveness_requirement": "Only instance tied to the terminal confidence-calibration act at bulletin issuance; must not restate or merely summarize the earlier decision points' uncertainties."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Authority Bias or Authority Obedience", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Framing effects", "strength": "subtle" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_5",
    "domain_id": "IA",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences were spread across all four decision points where mechanism fit allowed one-per-decision-point allocation (Phases 1, 2, and 4). Phase 3 (team meeting) received two distinct biases (Groupthink and Framing effects) because both plausibly co-occur in a single group deliberation but were required to involve different reasoning operations (consensus formation vs. message framing) and different evidence traces (dissent handling vs. phrasing choice), satisfying the no-more-than-two-per-bias and distinct-evidence-source rules. No bias received more than one instance, so intra-bias separation rules did not need to be invoked beyond the cross-bias separation at Phase 3.",
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
          "segment_id": "seg_1",
          "speaker": "Participant",
          "segment_type": "eligible_reasoning_segment",
          "raw_interview_anchor": "P1: corridor tip, corridor tasking, mismatched SIGINT",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "Positive hidden reasoning segment for cb_01."
        },
        {
          "segment_id": "seg_2",
          "speaker": "Participant",
          "segment_type": "eligible_reasoning_segment",
          "raw_interview_anchor": "P2: liaison pattern comparison and escalation",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_02"
          ],
          "ground_truth_rationale": "Positive hidden reasoning segment for cb_02."
        },
        {
          "segment_id": "seg_3",
          "speaker": "Participant",
          "segment_type": "eligible_reasoning_segment",
          "raw_interview_anchor": "P3: dissent handling and attack/safety phrasing",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_03",
            "cb_04"
          ],
          "ground_truth_rationale": "Positive hidden reasoning segment for cb_03 and cb_04."
        },
        {
          "segment_id": "seg_4",
          "speaker": "Participant",
          "segment_type": "eligible_reasoning_segment",
          "raw_interview_anchor": "P4: strong corridor-specific bulletin",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_05"
          ],
          "ground_truth_rationale": "Positive hidden reasoning segment for cb_05."
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
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis of participant-reported decision-making for affirmatively demonstrated cognitive-bias mechanisms. Hypothetical, pedagogical, and purely retrospective outcome knowledge were not used as primary evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Groupthink",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Overconfidence effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Anchoring effect",
      "alternative_labels": [
        "Anchoring bias",
        "Focalism",
        "Anchoring and adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient adjustment from an initial focal cue during subsequent inference or evidence search.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial collection tasking after walk-in tip",
      "decision_point_description": "Whether to focus collection narrowly on the finish-line corridor named by the untested source or spread it across the whole event footprint.",
      "affected_reasoning_operation": "Evidence search and collection prioritization",
      "bias_specific_mechanism": "The finish-line corridor named in the initial tip became the focal hypothesis; subsequent collection was built around it with limited adjustment for source unreliability or later differing signals.",
      "manifestation_in_interview": "The participant directed SIGINT and HUMINT follow-up specifically at the named corridor because the source identified it, even though the source was new and had no reliability rating.",
      "effect_on_reasoning_or_decision": "Narrowed collection and analytical focus to the named corridor, reducing search across the broader event footprint.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That's where he said the device was, so that's where I wanted eyes.",
          "evidence_explanation": "This shows the initial focal location directly determining collection tasking before corroboration."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Narrowing to the corridor at least gave us a shot at confirming or knocking down something specific.",
          "evidence_explanation": "The participant framed the narrowed search as the only acceptable option, consistent with an anchoring effect on the initial location."
        }
      ],
      "correction_or_counterevidence": "The participant considered a broader search alternative but rejected it because of limited staffing. This resource constraint is a plausible bounded-rational factor, but the later failure to update the location focus when a differing SIGINT arrived keeps anchoring as a contributory mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific corpus support was available in the RAG context. This classification relies on established cognitive-science knowledge of anchoring and focalism.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory bias",
        "Selective evidence weighting",
        "Congruence bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Selective weighting, interpretation, or search for information consistent with an existing hypothesis while discounting incongruent information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Handling of first partial SIGINT return",
      "decision_point_description": "Whether to treat the route-security SIGINT from a different sector as relevant to the marathon threat and re-evaluate the corridor focus.",
      "affected_reasoning_operation": "Evidence interpretation and hypothesis updating",
      "bias_specific_mechanism": "The existing corridor hypothesis functioned as a filter: the SIGINT was judged likely unrelated because it did not fit the tip, rather than being used to update the location hypothesis.",
      "manifestation_in_interview": "The participant logged a partial SIGINT hit that referenced route security for the marathon but did not reassign resources to it, explicitly avoiding reopening the location question.",
      "effect_on_reasoning_or_decision": "A potentially event-relevant signal from a usually trusted channel was not integrated; the corridor remained the unchallenged priority.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It didn't fit the tip, so I treated it as probably a separate, unrelated signal and kept the corridor as the priority.",
          "evidence_explanation": "The participant used congruence with the tip as the test for relevance, which is a hallmark of confirmatory reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "By then the corridor was already what we were working toward, and I didn't reopen the location question — I filed it as a separate thread and stayed on the one we already had detail on.",
          "evidence_explanation": "This shows the existing hypothesis was preserved despite new route-security information that could have called the location into question."
        }
      ],
      "correction_or_counterevidence": "The SIGINT mismatch could genuinely have been a separate signal; however, the stated reason for not reopening the location question was the existing focus rather than positive evidence that the SIGINT was unrelated.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific corpus support was available in the RAG context. This classification relies on established cognitive-science knowledge of confirmation bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Authority bias",
      "alternative_labels": [
        "Authority heuristic",
        "Expert authority bias",
        "Source credibility bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Over-reliance on the judgment or perceived expertise of an authority or experienced source, substituting that assertion for independent evidential comparison.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Senior JTTF liaison call and elevation recommendation",
      "decision_point_description": "Whether to adopt the liaison's pattern comparison and recommend elevation, or to pull and compare the prior case file first.",
      "affected_reasoning_operation": "Source-weighted analogical inference",
      "bias_specific_mechanism": "The participant accepted a pattern resemblance and acted on it because of the liaison's extensive experience and direct case involvement, without independently comparing the prior case to the current tip.",
      "manifestation_in_interview": "The participant recommended elevation based on the liaison's familiarity with an earlier plot, even though the team had not yet pulled the case file.",
      "effect_on_reasoning_or_decision": "Elevation recommendation was made on the basis of a surface-level resemblance that later did not align with the earlier case.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But he's the one who worked that case directly, so when he says it resembles the pattern, that carries weight. I took his read and recommended to the Director that we elevate.",
          "evidence_explanation": "The participant explicitly attributes the decision weight to the liaison's authority and experience rather than to an independent evidential comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If someone with his background tells you it looks familiar, you don't sit on that while digging through old files. I trusted the call.",
          "evidence_explanation": "The participant reports accepting the comparison because of the source's background, directly demonstrating authority-based deference."
        }
      ],
      "correction_or_counterevidence": "After the decision, the earlier case was compared and found to differ in tactic and target; this retrospective check was not performed at the time of reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific corpus support was available in the RAG context. This classification relies on established cognitive-science knowledge of authority and source-credibility biases.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Groupthink",
      "alternative_labels": [
        "Concurrence seeking",
        "Dissent suppression",
        "Groupthink syndrome"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A group decision process characterized by premature consensus, suppression of dissent, and failure to adequately evaluate alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Team meeting on threat characterization and resource ask",
      "decision_point_description": "Whether to grant a junior analyst's request for 24 hours and whether to document her corroboration-gap concern before the Director.",
      "affected_reasoning_operation": "Group deliberation and dissent documentation",
      "bias_specific_mechanism": "Consensus pressure, the freshness of the liaison's read, and deadline pressure led to rapid alignment. The participant intentionally omitted the junior analyst's concern from formal notes to preserve a unified recommendation.",
      "manifestation_in_interview": "The junior analyst raised the corroboration gap and asked for more time, but the room moved forward quickly and the concern was not documented for the Director.",
      "effect_on_reasoning_or_decision": "Dissenting information did not reach the Director, and the resource discussion proceeded without documented challenge to the emerging threat characterization.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The room was mostly already leaning toward moving forward — people nodding, the liaison's read still fresh, no 24 hours to spare with the deadline coming. We reached agreement quickly and moved to the resource ask.",
          "evidence_explanation": "The participant describes a premature consensus process in which the dissenting request was quickly overridden."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't write her concern into the formal notes — not because she was wrong, but because a documented disagreement in front of the Director would have muddied a recommendation we needed unified. We just moved on once the room was aligned.",
          "evidence_explanation": "This is explicit suppression of dissent and a preference for unity over surfacing a live evidential gap."
        }
      ],
      "correction_or_counterevidence": "None documented in the transcript at the time of decision; the junior analyst's concern was not revisited before the bulletin.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific corpus support was available in the RAG context. This classification relies on established cognitive-science knowledge of groupthink and dissent suppression.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Framing effect",
      "alternative_labels": [
        "Attribute framing",
        "Equivalence framing",
        "Risky-choice framing",
        "Framing bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Differential evaluation or choice based on whether equivalent outcomes are framed in positive or negative terms.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Presentation of resource request to Director",
      "decision_point_description": "Whether to present the same risk as a 10% chance of an incident or a 90% chance that everything goes fine.",
      "affected_reasoning_operation": "Risk communication and resource allocation",
      "bias_specific_mechanism": "The participant selected a risk-emphasizing frame because it sounded more decisive and concrete; numerically equivalent information produced different urgency and resource approval.",
      "manifestation_in_interview": "The participant described using the 10-percent-incident framing rather than the 90-percent-safe framing and reported that the Director responded to the risk-emphasizing version.",
      "effect_on_reasoning_or_decision": "The resource request was approved as a fairly large patrol and screening surge; the participant judged that the 90-percent-safe framing would not have carried the same urgency.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I framed it as roughly a ten percent chance of an incident, rather than a ninety percent chance everything goes fine. Same numbers, different emphasis. I went with the version that made the risk concrete because the Director responds to clear, decisive figures rather than reassurance-sounding ones.",
          "evidence_explanation": "The participant explicitly identifies that the numbers were identical but that the framing was chosen to create a different impression."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd led with the ninety-percent-safe version, I don't think it would've carried the same urgency — the numbers were identical, just how I said them.",
          "evidence_explanation": "This demonstrates that the equivalent representation affected the decision-maker's response, not the underlying probability."
        }
      ],
      "correction_or_counterevidence": "Retrospectively the participant said he would think harder about it now, but no time-of-decision correction or neutral reframing occurred.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific corpus support was available in the RAG context. This classification relies on established cognitive-science knowledge of framing effects.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Overconfidence bias",
        "Overprecision",
        "Miscalibration"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Subjective confidence in a judgment or forecast that exceeds the evidentiary support or calibration.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Drafting and briefing the bulletin",
      "decision_point_description": "How confidently to characterize the corridor as the likely target in external bulletin language.",
      "affected_reasoning_operation": "Confidence calibration and threat communication",
      "bias_specific_mechanism": "Despite unresolved gaps including the SIGINT mismatch, unverified case comparison, and unrecorded dissent, the participant stated high confidence and used strong language, partly because hedging was seen as undesirable before the Director and organizers.",
      "manifestation_in_interview": "The final bulletin named the corridor specifically as the likely target in fairly strong, high-confidence language even though corroboration had not come in and open items remained.",
      "effect_on_reasoning_or_decision": "External communication conveyed higher certainty than the underlying evidence justified.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, pretty sure. I stated it with real confidence. When you're the one who has to say something in front of the Director and the event organizers, hedging doesn't land well.",
          "evidence_explanation": "The participant reports high subjective confidence in the bulletin while also tying that confidence to audience expectations rather than evidentiary closure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'll be honest, those things were never fully closed out. We went into the bulletin with those loose ends still there. I stand by acting decisively given the clock, but the underlying picture wasn't as clean as the language I used suggested.",
          "evidence_explanation": "This retrospective admission confirms that the expressed confidence exceeded the state of the evidence at the time."
        }
      ],
      "correction_or_counterevidence": "No correction at the time of briefing; the participant later acknowledged the unresolved gaps and the mismatch between the internal picture and the external language.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific corpus support was available in the RAG context. This classification relies on established cognitive-science knowledge of overconfidence and miscalibration.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Escalation of commitment",
      "alternative_labels": [
        "Sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Retention of corridor focus after initial collection investment",
      "supporting_interview_quote": "By then the corridor was already what we were working toward, and I didn't reopen the location question.",
      "plausible_mechanism": "Continued commitment to the initial corridor because time and collection effort had been invested, despite a differing SIGINT signal.",
      "why_not_identified": "The transcript also cites resource constraints and a desire for a specific focus, so a distinct sunk-cost or escalation mechanism is not cleanly separable from the already identified anchoring and confirmation biases."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Base-rate neglect",
      "alternative_labels": [
        "Source reliability neglect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial interpretation of new walk-in source with no reliability history",
      "supporting_interview_quote": "The source was brand new, no reporting history, no reliability rating yet.",
      "plausible_mechanism": "Treating a low-reliability single-source tip as highly actionable despite missing base rates for source reliability and threat reporting.",
      "why_not_identified": "The participant explicitly acknowledged the source's lack of reliability and considered a broader search alternative, so the transcript does not show categorical neglect of base-rate information."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "Availability heuristic",
      "alternative_labels": [
        "Availability bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Senior JTTF liaison",
      "possible_decision_episode_label": "Pattern comparison to prior plot",
      "supporting_interview_quote": "He heard the tip summary, said it resembled the pattern from a plot broken up about two years back, and recommended elevating the threat level.",
      "plausible_mechanism": "A mentally available prior plot shaped the liaison's pattern comparison without structured case-file review.",
      "why_not_identified": "The transcript offers no direct evidence about the liaison's internal retrieval process; the participant's acceptance of the comparison is better captured as authority bias."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific corpus passages were supplied in the RAG context; classifications rely on established cognitive-science knowledge rather than task-specific retrieved literature.",
    "The interview is a single retrospective self-report, so memory reconstruction and self-presentation may affect the record.",
    "The analysis is conservative and does not equate bad outcomes, resource-constrained heuristics, or ordinary decision-making under uncertainty with bias."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Biased_5_Gemini_off",
  "interview_id": "IA_Biased_5",
  "system_prompt_id": "Gemini",
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
