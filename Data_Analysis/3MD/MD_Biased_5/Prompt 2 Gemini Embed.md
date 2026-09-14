You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. As a reminder, this session is for the after-action cognitive review, not for attribution of blame—I just want to understand how decisions actually got made. That okay with you?

Participant: Yeah, that's fine. I've done these before.

Interviewer: Good. Can you start by giving me your role and what the mission was?

Participant: I'm the battalion S3 for the task force. Our mission was to secure and hold the Route BLUE crossing so brigade could push their main effort across within a 48-hour window. We had one Mobile Gap-Crossing Bridge, limited float capacity, and weather was closing in on our aerial ISR window. It mattered because if we didn't hold that crossing on schedule, brigade's whole synchronization plan slid.

Interviewer: Walk me through how the incident actually unfolded, start to finish.

Participant: Sure. About 48 hours out, S2 flagged enemy scout vehicles in a spot that didn't quite match what we'd been seeing—three months of pattern-of-life had them screening consistently off ridge NAI 12, and this sighting was lower, closer to the river. The vehicle types and rough timing matched what we'd tracked before, so it read to me like the same defensive template, and I didn't put much weight on the location itself. S2 actually noted that the river-side position wasn't really consistent with how that unit normally screened, but I still treated it as a variant of the pattern we knew rather than something that needed a second look. So we didn't request additional ISR retasking, we just kept the reconnaissance-in-force plan as built.

About six hours after that, brigade S3 called and directed us to continue on Axis BLUE per the original order, citing the synchronization requirement. At that point our engineer had already flagged a preliminary concern about the bridge's load capacity, but it wasn't a hard number yet—no full classification. I mentioned it to brigade informally but didn't push hard. If I'm honest, I thought the concern was enough to justify at least asking for a short pause to get the classification confirmed, but once brigade framed continuation as a synchronization requirement, raising that again felt like second-guessing a decision that had already been made.

Then closer to execution, the engineer came back with an actual classification report suggesting overweight risk for our heaviest vehicles. We had a planning session that same day. The plan was already rehearsed, already briefed up to brigade. The report got raised, a couple people nodded at it, but the discussion moved straight to what the plan already had going for it rather than to whether the risk itself changed anything, and nobody proposed rerouting. The session wrapped with everyone agreeing to keep the existing crossing plan.

Execution day, we had a partial bridge failure under one of the heavier platforms, and almost simultaneously took contact from dismounts near the crossing site. We ran the branch plan, secured the site, and finished the crossing over the alternate ford instead.

Interviewer: Let's slow down and rebuild that timeline with the information you had at each point, not what you know now.

Participant: Fair. At H-48, all I had was the scout sighting and the historical pattern. No confirmation either way on intent. At H-30 or so, I had brigade's directive plus an informal, unconfirmed engineer concern. At H-24, I had a real classification number and a rehearsed plan already in brigade's hands. At H-hour, I had the failure and the contact simultaneously.

Interviewer: Take me back to that first sighting. What made you read it as consistent with the known template rather than as something new?

Participant: The vehicle types matched, the timing matched roughly what we'd seen before, and three months of consistent behavior is a strong baseline. Even with S2 pointing out the location was a little off for that unit's normal screening, it still looked and moved like the same picture we'd been tracking, so I didn't treat the position as something that changed the category. If I chased every deviation with an ISR request, given how constrained our collection was, we'd never finalize anything.

Interviewer: Did you consider requesting retasking anyway, just to confirm?

Participant: S2 raised it as an option. I didn't prioritize it because the weather window for aerial support was closing and I didn't think the deviation was significant enough to justify pulling that asset off other priorities.

Interviewer: When the ground patrol later reported dismounts moving toward the crossing itself rather than the ridge, how did that land?

Participant: That's when S2 flagged it as worth another look. But we were already committed to the recon plan by then, so it didn't change what we'd built.

Interviewer: Move to brigade's call directing continuation on Axis BLUE. What alternatives did you weigh?

Participant: I could have pushed back and asked for a short delay to firm up the bridge picture or scout the alternate ford. Or I could comply and keep the timeline. I went with compliance.

Interviewer: What drove that choice specifically?

Participant: Brigade had already made the call, and it came with the synchronization argument attached. Honestly, the informal concern was probably enough on its own to justify asking for a short hold pending classification, but by the time brigade framed it as a fixed requirement, pushing that same point again felt like challenging a decision that was already settled above me. It felt like brigade owned that risk calculus at that point more than I did.

Interviewer: Did you get any pushback or written response from brigade on the bridge issue?

Participant: No, not before we committed.

Interviewer: Let's go to the planning session where the classification report came in. How did that discussion actually go?

Participant: It was quick. The engineer laid out the overweight risk, a couple of people acknowledged it, and then the conversation moved on to why the current plan was already solid rather than to what the new number actually meant for it. Nobody put a reroute on the table. We closed with agreement to keep the plan.

Interviewer: What was the reasoning for keeping the plan rather than shifting to the alternate ford?

Participant: Once the classification came in, the room still leaned on the fact that the plan was rehearsed and already briefed to brigade more than it leaned on the number itself. Rerouting would have meant reconning an unfamiliar ford in current water conditions, in daylight, with no rehearsal, and we didn't really stop to weigh a partial fix, like resequencing the heavier vehicles, against just keeping what we had.

Interviewer: Did anyone in the room actually voice disagreement with keeping the plan?

Participant: Not in the room, no. I found out afterward that one of the company commanders had reservations about the bridge but didn't say anything during the session.

Interviewer: Did he ever say why he stayed quiet?

Participant: He told me later that by the time the report came up, the room had already settled on keeping the plan, and he didn't want to be the one to reopen something that had already gone up to brigade.

Interviewer: Now the crossing itself. What would have changed your decision to keep the original plan, looking back at what you knew before execution?

Participant: A hard confirmed number earlier, or if someone had actually put the alternate ford proposal on the table instead of just the report sitting there. If we'd had even a day more, I think we'd have reconned the ford as a real branch option instead of a theoretical one.

Interviewer: How do you assess the scout sighting now, knowing what happened at the crossing?

Participant: Looking back, I think we should have caught more from that first report than we did. The river-side location was there in the original reporting, and given how it lines up with the patrol and the contact, we probably should have recognized the implication right then instead of waiting for later confirmation.

Interviewer: Last one—if the alternate ford had been reconned earlier, do you think the planning session goes differently?

Participant: Probably. If it had been a real, validated option sitting next to the bridge option, I think the report would have gotten more than a nod. As it stood, it was theoretical, so keeping the rehearsed plan felt like the lower-risk path in the room that day.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MD_Biased_5",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Battalion Operations Officer (S3)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Route BLUE Crossing: Delayed Bridge Reclassification Incident",
    "scenario_summary_internal": "A mechanized infantry battalion S3 must secure a river crossing (Route BLUE) within a compressed timeline to enable brigade's follow-on attack. Ambiguous enemy reconnaissance activity, a brigade-directed continuation of the original axis, and a staff planning session that converges too quickly on the existing crossing plan (despite a new engineer bridge-classification report) precede a crossing attempt that encounters partial bridge failure and enemy contact. The post-incident CTA interview captures the S3's chronological account and reflections.",
    "occupational_realism": {
      "objective": "Secure and hold Route BLUE river crossing to enable brigade's main-effort attack within a 48-hour window.",
      "setting": "Contested border corridor, mechanized infantry battalion task force, deteriorating weather, degraded FM/digital comms reliability.",
      "constraints": [
        "Single bridging asset (MGB) with limited engineer float capacity",
        "48-hour brigade timeline tied to a synchronized main-effort attack",
        "Intermittent SATCOM/FM comms degrading real-time intel updates",
        "Only one alternate ford, unrehearsed and unreconned in daylight",
        "Limited ISR assets already tasked to brigade's main effort"
      ],
      "stakeholders": [
        "Battalion Commander",
        "S3 (interviewee)",
        "S2 (Intelligence Officer)",
        "Battalion Engineer Officer",
        "Brigade S3",
        "Company Commanders (Route BLUE lead element)"
      ],
      "technical_terms_to_use": [
        "axis of advance",
        "movement to contact",
        "bridge classification",
        "reconnaissance-in-force",
        "main effort",
        "branch plan",
        "MGB (Mobile Gap-Crossing Bridge)",
        "named area of interest (NAI)",
        "template",
        "commander's critical information requirement (CCIR)"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "groupthink",
        "hindsight",
        "authority bias",
        "status quo bias",
        "representativeness"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "S2 reports enemy scout vehicles observed at an atypical location relative to the templated company defensive belt",
          "Prior three months of pattern-of-life data show enemy reconnaissance consistently screening from ridge NAI 12",
          "Weather forecast shows a closing window for aerial ISR support"
        ],
        "new_information_after_decision": [
          "A follow-up ground patrol later reports enemy dismounts moving toward the river crossing itself, not the ridge",
          "S2 flags the deviation as worth re-tasking ISR, but battalion has already committed to the original recon plan"
        ],
        "alternatives": [
          "Request additional ISR retasking to confirm whether the scout sighting represents a deviation from the known enemy template before finalizing the reconnaissance-in-force plan",
          "Proceed with the existing reconnaissance-in-force plan on the assumption the sighting is a normal variant of the known company defense template"
        ],
        "intended_action": "S3 treats the atypical sighting as consistent with the familiar enemy template and proceeds with the unmodified reconnaissance plan."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Brigade S3 directs continuation on Axis BLUE per the original brigade order, citing the synchronized attack timeline",
          "Battalion engineer has flagged a preliminary concern about bridge load capacity pending a full classification survey",
          "Battalion S3 has raised the bridge concern informally but has not yet received a written response from brigade"
        ],
        "new_information_after_decision": [
          "Engineer officer completes a fuller bridge classification later than planned, after the crossing plan is already locked in with brigade",
          "Brigade acknowledges the concern only after the battalion has already committed forces to the axis"
        ],
        "alternatives": [
          "Push back to brigade requesting a short delay to complete bridge reinforcement or reconnoiter the alternate ford before committing heavy vehicles",
          "Comply with brigade's direction to continue on Axis BLUE without altering the crossing timeline, given the synchronized attack requirement"
        ],
        "intended_action": "S3 defers to brigade's directive to continue on the original axis largely because brigade has prioritized timeline over the unresolved bridge concern."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Engineer officer presents a bridge classification report suggesting overweight risk for the battalion's heaviest vehicles",
          "The crossing plan has already been briefed to brigade and rehearsed by lead companies",
          "Staff members raise the report but no one proposes rerouting before the commander's planning session ends",
          "The alternate ford exists but has not been reconned in current water conditions"
        ],
        "new_information_after_decision": [
          "Post-session, one company commander privately notes he had reservations about the bridge but did not voice them in the session",
          "The alternate ford is later found passable, but only after the crossing attempt has already begun"
        ],
        "alternatives": [
          "Reroute the battalion's heavy vehicles to the alternate ford despite the added reconnaissance and rehearsal burden",
          "Retain the original bridge crossing plan on the grounds that it is already rehearsed, briefed to brigade, and requires no further coordination"
        ],
        "intended_action": "The staff converges quickly on retaining the existing bridge crossing plan; the session ends with unanimous, largely unchallenged agreement despite the unresolved load-capacity concern."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The crossing attempt results in a partial bridge failure under a heavy vehicle and near-simultaneous enemy contact from dismounts near the crossing site",
          "The battalion executes a hasty branch plan to secure the site and complete the crossing via the alternate ford",
          "The interview occurs after the operation, during a formal after-action review"
        ],
        "new_information_after_decision": [
          "Casualty and equipment loss reports are finalized",
          "S2 compiles a consolidated timeline showing the scout sighting, the bridge report, and the contact, for the after-action review"
        ],
        "alternatives": [
          "Describe the sequence of events and decisions as they appeared at each point in time, acknowledging what was and was not knowable",
          "Characterize the enemy activity and bridge risk as having been clearly foreseeable indicators of the eventual outcome"
        ],
        "intended_action": "During the interview, the S3 characterizes the earlier scout sighting as an obvious warning sign of the ambush, asserting the outcome was foreseeable given what 'was clearly there all along.'"
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through the overall mission and your role as S3 during this operation?",
        "What was the operational objective for Route BLUE, and why did it matter to brigade's plan?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "Walk me through the sequence of reports you received from S2 and the engineer officer.",
        "When did brigade's directive on Axis BLUE come in, and what did you know before that call?"
      ],
      "decision_point_probes": [
        "What cues made you interpret the scout sighting the way you did?",
        "What sources of information did you weigh most heavily when deciding whether to continue the recon plan?",
        "When brigade directed continuation on Axis BLUE, what alternatives did you consider, and why did you choose the one you did?",
        "During the planning session, how did the staff resolve the disagreement or concern about the bridge report?",
        "What was your basis for keeping the original crossing plan rather than rerouting?"
      ],
      "cues_and_information_sources": [
        "What specific data or reports drove each of your calls?",
        "How reliable did you consider the engineer's preliminary bridge assessment versus the fuller classification?"
      ],
      "goals_and_alternatives": [
        "What competing goals were you balancing at each decision point?",
        "What other courses of action did you or the staff consider but set aside?"
      ],
      "prior_experience": [
        "Had you encountered a similar enemy templated defense before, and how did that shape your read of the situation?",
        "Has your battalion faced a similar bridge or crossing constraint on past operations?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure were you under at each of these points?",
        "What were you most uncertain about, and how did that uncertainty affect your decision?"
      ],
      "closing_hypotheticals": [
        "If you had more time before the crossing, what would you have done differently?",
        "Looking back, what do you think the early indicators tell you about how predictable the outcome was?",
        "If the alternate ford had been reconned earlier, how might the planning session have gone differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "MD5_b01",
        "bias": "Representativeness Heuristic",
        "decision_point": 1,
        "mechanism": "S3 classifies the atypical scout sighting as belonging to the familiar enemy company-defense template based on surface similarity to past patterns, rather than weighing the specific locational deviation.",
        "affected_reasoning_operation": "Categorization of new evidence against a prior mental template",
        "evidence_available_at_time": [
          "Atypical scout vehicle location relative to templated defensive belt",
          "Three months of consistent pattern-of-life data showing screening from NAI 12"
        ],
        "required_textual_manifestation": "S3 explicitly states the sighting was treated as a normal variant of the known template and that this is why no plan modification or ISR retasking was requested.",
        "plausible_nonbias_interpretation": "Given limited ISR availability and a tight timeline, relying on a well-validated template could be framed as a reasonable economy-of-effort judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["representativeness", "heuristic", "template bias"]
      },
      {
        "instance_id": "MD5_b02",
        "bias": "Authority Bias or Higher-level prioritization Bias",
        "decision_point": 2,
        "mechanism": "S3 defers to brigade's directive to continue on Axis BLUE primarily because it originates from a higher headquarters, muting his own unresolved concern about bridge capacity rather than escalating it formally.",
        "affected_reasoning_operation": "Weighting of directive source over unresolved technical risk in a go/no-go judgment",
        "evidence_available_at_time": [
          "Brigade S3's verbal directive citing the synchronized attack timeline",
          "Battalion engineer's informal, unresolved concern about bridge load capacity"
        ],
        "required_textual_manifestation": "S3 states that he complied with brigade's directive largely because it came from brigade and the timeline was fixed, without describing an independent risk-weighing process.",
        "plausible_nonbias_interpretation": "Time-sensitive synchronization with a brigade main effort is a legitimate reason to prioritize compliance with a higher headquarters' timeline.",
        "strength": "moderate",
        "do_not_make_explicit": ["authority bias", "deference", "higher-level prioritization"]
      },
      {
        "instance_id": "MD5_b03",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "The staff planning session converges rapidly on retaining the existing plan with no one voicing dissent aloud, even though at least one company commander privately held reservations, indicating suppressed disagreement rather than genuine consensus.",
        "affected_reasoning_operation": "Group decision convergence and dissent suppression during collective evaluation of the bridge report",
        "evidence_available_at_time": [
          "Engineer's bridge classification report indicating overweight risk",
          "Staff members' brief mention of the report followed by no further challenge"
        ],
        "required_textual_manifestation": "S3 describes the session as reaching quick, unanimous agreement to keep the plan, and separately notes (or a probe reveals) that a company commander had unspoken reservations he did not raise.",
        "plausible_nonbias_interpretation": "A team with strong rapport and shared understanding may genuinely and legitimately agree quickly without any suppressed dissent.",
        "strength": "moderate",
        "do_not_make_explicit": ["groupthink", "consensus pressure", "suppressed dissent"]
      },
      {
        "instance_id": "MD5_b04",
        "bias": "Status Quo Bias",
        "decision_point": 3,
        "mechanism": "The staff retains the original bridge crossing plan primarily because it is already rehearsed and briefed to brigade, treating the effort already invested in the existing plan as a reason to avoid the alternate ford rather than independently evaluating the new load-capacity evidence.",
        "affected_reasoning_operation": "Selection between two crossing options, anchored on the default (already-committed) plan",
        "evidence_available_at_time": [
          "The alternate ford as an unreconned but available option",
          "The fact that the existing plan was already rehearsed and briefed to brigade"
        ],
        "required_textual_manifestation": "S3 explains the choice to keep the original plan by referencing the rehearsal and brigade briefing already completed, rather than the risk data itself, as the deciding factor.",
        "plausible_nonbias_interpretation": "Avoiding an unreconned ford under time pressure could be a legitimate risk-mitigation choice independent of any default preference.",
        "strength": "moderate",
        "do_not_make_explicit": ["status quo bias", "default option", "sunk cost of rehearsal"]
      },
      {
        "instance_id": "MD5_b05",
        "bias": "Hindsight Bias",
        "decision_point": 4,
        "mechanism": "During the after-action interview, S3 characterizes the earlier scout sighting as an obvious, foreseeable warning of the ambush, overstating how predictable the outcome was given what was actually known at the time.",
        "affected_reasoning_operation": "Retrospective reconstruction of prior uncertainty into perceived foreseeability",
        "evidence_available_at_time": [
          "Consolidated after-action timeline showing the scout sighting, bridge report, and eventual contact",
          "S3's own prior account (decision point 1) describing the sighting as ambiguous at the time"
        ],
        "required_textual_manifestation": "S3 states in the interview that the sighting 'was clearly there all along' or equivalent, implying the outcome was obvious in advance, contrasting with his earlier real-time uncertainty.",
        "plausible_nonbias_interpretation": "With full knowledge of the eventual contact, it is reasonable to note the sighting was relevant in retrospect without claiming it was obviously predictive at the time.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "foreseeability", "retrospective distortion"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no paired control scenario specified for this generation (condition = biased)."
    },
    "counterfactual_specification": {
      "causal_variable": "not_applicable",
      "original_state": "not_applicable",
      "counterfactual_state": "not_applicable",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "not_applicable",
      "causal_test_question": "not_applicable"
    },
    "generation_checks": [
      "Exactly 4 decision points are present in the timeline.",
      "Exactly 5 total bias instances are planned, matching the manifest sum (1 each for 5 biases).",
      "No decision point contains more than one instance of the same bias.",
      "Decision point 3 contains two distinct biases (Groupthink, Status Quo Bias) with separated evidence sources (dissent suppression vs. rehearsal/briefing investment).",
      "No bias labels, definitions, or psychological terminology appear in the technical_terms_to_use list or planned interview text.",
      "Each occurrence has a distinct evidence trace and a plausible non-bias explanation.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given 4 decision points and probe density without repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Authority Bias or Higher-level prioritization Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Hindsight Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Representativeness Heuristic",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Status Quo Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Groupthink",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Authority Bias or Higher-level prioritization Bias",
      "Hindsight Bias",
      "Representativeness Heuristic",
      "Status Quo Bias",
      "Groupthink"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Authority Bias or Higher-level prioritization Bias", "requested_occurrences": 1 },
      { "bias": "Hindsight Bias", "requested_occurrences": 1 },
      { "bias": "Representativeness Heuristic", "requested_occurrences": 1 },
      { "bias": "Status Quo Bias", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "MD5_b01", "bias": "Representativeness Heuristic" },
      { "instance_id": "MD5_b02", "bias": "Authority Bias or Higher-level prioritization Bias" },
      { "instance_id": "MD5_b03", "bias": "Groupthink" },
      { "instance_id": "MD5_b04", "bias": "Status Quo Bias" },
      { "instance_id": "MD5_b05", "bias": "Hindsight Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "MD5_b01", "bias": "Representativeness Heuristic", "decision_point": 1 },
      { "instance_id": "MD5_b02", "bias": "Authority Bias or Higher-level prioritization Bias", "decision_point": 2 },
      { "instance_id": "MD5_b03", "bias": "Groupthink", "decision_point": 3 },
      { "instance_id": "MD5_b04", "bias": "Status Quo Bias", "decision_point": 3 },
      { "instance_id": "MD5_b05", "bias": "Hindsight Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MD5_b01",
        "bias": "Representativeness Heuristic",
        "mechanism": "Classifying an atypical scout sighting as a normal variant of a familiar enemy template rather than weighing the specific deviation.",
        "affected_reasoning_operation": "Categorization of new evidence against prior template",
        "evidence_source": "S2 scout-sighting report vs. historical pattern-of-life data",
        "distinctiveness_requirement": "Occurs at DP1, involves categorical pattern-matching, distinct from all other instances by evidence type (intel pattern data) and reasoning operation (categorization, not deference or default preference)."
      },
      {
        "instance_id": "MD5_b02",
        "bias": "Authority Bias or Higher-level prioritization Bias",
        "mechanism": "Deferring to brigade's directive to continue the axis primarily because of its source (higher headquarters) rather than independent risk-weighing.",
        "affected_reasoning_operation": "Source-weighted compliance judgment overriding unresolved technical risk",
        "evidence_source": "Brigade S3 verbal directive vs. battalion engineer's informal risk flag",
        "distinctiveness_requirement": "Occurs at DP2, involves deference to hierarchical authority, distinct from DP1 (no external directive involved) and DP3 (no group consensus dynamic)."
      },
      {
        "instance_id": "MD5_b03",
        "bias": "Groupthink",
        "mechanism": "Rapid, unchallenged staff convergence on retaining the plan despite a company commander's private, unvoiced reservations.",
        "affected_reasoning_operation": "Suppressed dissent during collective evaluation",
        "evidence_source": "Staff session dynamics and company commander's private post-session comment",
        "distinctiveness_requirement": "Shares DP3 with MD5_b04 but is distinguished by focusing on group dissent suppression (social/interpersonal evidence: unvoiced commander reservation) rather than the plan-retention rationale itself."
      },
      {
        "instance_id": "MD5_b04",
        "bias": "Status Quo Bias",
        "mechanism": "Choosing to retain the original bridge crossing plan because it was already rehearsed and briefed, rather than because the risk evidence favored it.",
        "affected_reasoning_operation": "Default-anchored selection between two crossing options",
        "evidence_source": "Engineer bridge classification report vs. sunk investment in the rehearsed/briefed plan",
        "distinctiveness_requirement": "Shares DP3 with MD5_b03 but is distinguished by evidence source (rehearsal/briefing investment and risk-data comparison) rather than group dynamics; reflects individual/staff preference for the incumbent option, not suppressed dissent."
      },
      {
        "instance_id": "MD5_b05",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospectively describing the earlier scout sighting as an obvious, foreseeable warning of the ambush, overstating predictability relative to the real-time uncertainty documented earlier.",
        "affected_reasoning_operation": "Retrospective reconstruction of foreseeability",
        "evidence_source": "After-action consolidated timeline vs. S3's own earlier (DP1) account of ambiguity",
        "distinctiveness_requirement": "Occurs at DP4 during post-outcome reflection only; distinct from MD5_b01 because it concerns retrospective judgment of foreseeability, not real-time categorization."
      }
    ],
    "intended_strength": [
      { "instance_id": "MD5_b01", "bias": "Representativeness Heuristic", "strength": "subtle" },
      { "instance_id": "MD5_b02", "bias": "Authority Bias or Higher-level prioritization Bias", "strength": "moderate" },
      { "instance_id": "MD5_b03", "bias": "Groupthink", "strength": "moderate" },
      { "instance_id": "MD5_b04", "bias": "Status Quo Bias", "strength": "moderate" },
      { "instance_id": "MD5_b05", "bias": "Hindsight Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Biased_5",
    "domain_id": "MD",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Instances distributed across 4 decision points per mechanism fit and narrative realism: DP1 (Representativeness Heuristic - intel categorization), DP2 (Authority Bias - directive compliance), DP3 (Groupthink and Status Quo Bias - two distinct biases co-located with separated evidence sources: dissent suppression vs. rehearsal-anchored plan retention), DP4 (Hindsight Bias - post-outcome reflection). No single bias exceeds one occurrence per decision point; co-located DP3 instances differ in evidence source and reasoning operation per Instance Independence Rule.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
null
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
    "analysis_scope_note": "Conservative, mechanism-first evaluation of the interview transcript. Retrieved corpus passages were used to anchor confirmation bias and plan continuation bias terminology; groupthink and hindsight bias classifications rely on established cognitive-science knowledge because no RAG passage directly supported them."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "groupthink",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "hindsight bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 2
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "expectation bias",
        "selective interpretation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial scout sighting assessment at H-48",
      "decision_point_description": "Whether to treat the river-side scout vehicle sighting as a significant deviation warranting additional ISR retasking or as a variant of the known defensive pattern.",
      "affected_reasoning_operation": "Evidence weighting and pattern classification",
      "bias_specific_mechanism": "The participant's pre-existing mental model of the enemy's three-month pattern-of-life caused him to overweight matching vehicle types and timing while underweighting the contradictory river-side location cue that S2 explicitly flagged as inconsistent.",
      "manifestation_in_interview": "The participant stated that he did not put much weight on the location because vehicle types and timing matched; he treated the discrepant position as a variant of the known pattern rather than as a new signal requiring a second look, despite S2 noting the inconsistency.",
      "effect_on_reasoning_or_decision": "No additional ISR retasking was requested, and the reconnaissance-in-force plan remained unchanged; the potential indicator of enemy adaptation near the crossing was not escalated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "S2 actually noted that the river-side position wasn't really consistent with how that unit normally screened, but I still treated it as a variant of the pattern we knew rather than something that needed a second look.",
          "evidence_explanation": "This explicitly shows the participant acknowledging contradictory location information while discounting it in favor of the prior pattern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The vehicle types matched, the timing matched roughly what we'd seen before, and three months of consistent behavior is a strong baseline. Even with S2 pointing out the location was a little off for that unit's normal screening, it still looked and moved like the same picture we'd been tracking, so I didn't treat the position as something that changed the category.",
          "evidence_explanation": "Demonstrates selective weighting of confirmatory features over an inconsistent location cue, leading to confirmation of the existing template."
        }
      ],
      "correction_or_counterevidence": "A bounded-rationality alternative exists: ISR assets were constrained and weather was closing, so not retasking on every deviation may have been a legitimate prioritization. However, the participant's explicit statement that the location did not change the category, despite acknowledging its inconsistency, supports a confirmation mechanism rather than purely resource-based deferral.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Cook and Smallman passage describes a strong and pervasive confirmation bias in intelligence analysis for selecting and prioritizing evidence; the cockpit review also lists confirmation bias and expectation bias as common operational biases.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at as- sessment but a strong and pervasive conﬁrmation for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias in intelligence analysis; evidence selection and prioritization favoring a pre-existing hypothesis.",
          "relevance_to_this_occurrence": "The participant prioritized pattern-consistent cues and lowered weight on contradictory location information, analogous to confirmation bias in evidence selection."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation",
        "continuation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A bias toward continuing an original plan of action even when changing circumstances require a new plan.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Brigade directive to continue on Axis BLUE at H-30",
      "decision_point_description": "Whether to comply silently with brigade's continuation directive or to push back and request a short delay to firm up the bridge picture.",
      "affected_reasoning_operation": "Risk escalation and response to changing circumstances",
      "bias_specific_mechanism": "The participant had an informal but potentially sufficient concern about bridge load capacity; however, the existing plan had already been decided and directed by brigade, and the synchronization rationale made the plan seem settled. This commitment to the original plan suppressed further escalation of the concern.",
      "manifestation_in_interview": "The participant explicitly stated that the concern justified asking for a short pause, but once brigade framed continuation as a synchronization requirement, pushing again felt like second-guessing a settled decision.",
      "effect_on_reasoning_or_decision": "The participant complied with the original plan and did not request a delay for classification; the bridge risk remained unconfirmed and unmitigated before execution.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, I thought the concern was enough to justify at least asking for a short pause to get the classification confirmed, but once brigade framed continuation as a synchronization requirement, raising that again felt like second-guessing a decision that had already been made.",
          "evidence_explanation": "This explicitly shows the participant weighing a changed circumstance but continuing the original plan due to perceived settledness rather than the risk's merits."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I could have pushed back and asked for a short delay to firm up the bridge picture or scout the alternate ford. Or I could comply and keep the timeline. I went with compliance.",
          "evidence_explanation": "Indicates the decision was not forced; the continuation bias influenced the choice to comply."
        }
      ],
      "correction_or_counterevidence": "The brigade directive was a legitimate order with a stated synchronization requirement, so compliance may be partly explained by formal authority and mission constraints. The participant did informally mention the engineer concern, showing some escalation behavior. This is why confidence is moderate rather than high.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved O'Connor cockpit review defines plan continuation bias and identifies it as a common operational bias.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "Plan continuation bias is described as \"a deep original plan of action even when changing circumstances require a new plan\" (Dismukes and Berman, 2006, p. 28).",
          "mechanism_supported_by_source": "Continuing an original plan even when changing circumstances require a new plan.",
          "relevance_to_this_occurrence": "The participant continued the original plan after learning of a bridge-capacity concern because the plan was already decided and framed as a synchronization requirement."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation",
        "commitment to prior plan"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A bias toward continuing an original plan of action even when changing circumstances require a new plan.",
      "attributed_to_speaker": "Planning session group including Participant and company commanders",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Planning session after engineer's bridge classification report at H-24",
      "decision_point_description": "Whether to keep the rehearsed and brigade-briefed bridge crossing plan or to evaluate alternatives and partial fixes after receiving a hard bridge overweight classification.",
      "affected_reasoning_operation": "Group decision evaluation and risk reassessment",
      "bias_specific_mechanism": "Once the classification report arrived, the group's prior rehearsal and brigade briefing made the existing plan seem dominant. The conversation shifted to the plan's strengths rather than to whether the new risk changed the plan, and alternatives were not formally weighed.",
      "manifestation_in_interview": "The participant reported that the report was acknowledged, a couple people nodded, but the discussion moved to what the plan had going for it; nobody proposed a reroute, and the session closed with agreement to keep the plan.",
      "effect_on_reasoning_or_decision": "The existing crossing plan was retained without re-evaluating alternatives such as rerouting or resequencing heavy vehicles; the bridge later partially failed under a heavy platform.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The report got raised, a couple people nodded at it, but the discussion moved straight to what the plan already had going for it rather than to whether the risk itself changed anything, and nobody proposed rerouting.",
          "evidence_explanation": "Shows group attention shifted away from the contradictory risk toward confirmation of the existing plan, consistent with plan continuation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once the classification came in, the room still leaned on the fact that the plan was rehearsed and already briefed to brigade more than it leaned on the number itself.",
          "evidence_explanation": "Explicitly indicates prior commitment to the plan outweighed new risk information."
        }
      ],
      "correction_or_counterevidence": "The group had some legitimate operational reasons to prefer the existing bridge plan: rerouting to an unfamiliar ford in current water conditions with no rehearsal carried its own risk. However, the transcript indicates those alternatives were not actually weighed as partial fixes, which supports a plan continuation mechanism.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The same retrieved O'Connor passage defines plan continuation bias and supports this group-level continuation behavior.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "Plan continuation bias is described as \"a deep original plan of action even when changing circumstances require a new plan\" (Dismukes and Berman, 2006, p. 28).",
          "mechanism_supported_by_source": "Continuing an original plan even when changing circumstances require a new plan.",
          "relevance_to_this_occurrence": "The group retained the rehearsed, already briefed plan despite a new bridge-risk classification, fitting the corpus definition of plan continuation bias."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "groupthink",
      "alternative_labels": [
        "self-censorship",
        "conformity bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mode of thinking in highly cohesive groups where the desire for unanimity overrides realistic appraisal of alternatives and suppresses dissent.",
      "attributed_to_speaker": "Company Commander as reported by Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Planning session after engineer's bridge classification report at H-24",
      "decision_point_description": "Whether the company commander should voice his reservations about the bridge during the planning session.",
      "affected_reasoning_operation": "Expression of dissent and group consensus monitoring",
      "bias_specific_mechanism": "The commander perceived that the room had already settled on keeping the plan and did not want to reopen a decision already briefed to brigade. This self-censorship suppressed contradictory information and reinforced the appearance of consensus.",
      "manifestation_in_interview": "Afterward, the commander told the participant that he had reservations but stayed quiet because the room had settled and he did not want to reopen the issue.",
      "effect_on_reasoning_or_decision": "No one voiced disagreement in the session, which confirmed the appearance of agreement to keep the original plan without dissent; the bridge risk was not fully debated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He told me later that by the time the report came up, the room had already settled on keeping the plan, and he didn't want to be the one to reopen something that had already gone up to brigade.",
          "evidence_explanation": "This is an explicit report of self-censorship driven by perceived group consensus, a core groupthink symptom."
        }
      ],
      "correction_or_counterevidence": "The evidence is secondhand and reported after the fact; the commander may have had other reasons not to speak. No direct group pressure is documented. Therefore confidence is low.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the RAG context directly addresses groupthink or self-censorship; classification relies on established cognitive-science knowledge of group decision-making, including Janis's groupthink.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to perceive past events as having been more predictable after the outcome is known than they actually were before.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "After-action retrospective assessment of the scout sighting",
      "decision_point_description": null,
      "affected_reasoning_operation": "Retrospective judgment and hindsight evaluation",
      "bias_specific_mechanism": "After knowing the later dismount contact and crossing-site attack, the participant reconstructed the initial river-side sighting as a clear implication that should have been recognized immediately, instead of evaluating its predictiveness from the H-48 information alone.",
      "manifestation_in_interview": "The participant stated that, looking back, the river-side location was in the original reporting and, given how it lines up with later contact, they probably should have recognized the implication right then.",
      "effect_on_reasoning_or_decision": "The after-action review may overattribute foreseeability to the initial report, potentially distorting lessons learned and overestimating the signal value of the H-48 sighting.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I think we should have caught more from that first report than we did. The river-side location was there in the original reporting, and given how it lines up with the patrol and the contact, we probably should have recognized the implication right then instead of waiting for later confirmation.",
          "evidence_explanation": "This explicitly uses outcome information about the patrol and contact to inflate the expected foresight of the original report, which is the hallmark of hindsight bias."
        }
      ],
      "correction_or_counterevidence": "Some of this language may reflect ordinary after-action self-criticism rather than a measurable probability estimate. However, the explicit outcome-linked judgment of what should have been recognized is sufficiently indicative of hindsight bias to support low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the RAG context directly addresses hindsight bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "authority bias",
      "alternative_labels": [
        "deference to authority",
        "obedience to authority"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Brigade directive to continue on Axis BLUE at H-30",
      "supporting_interview_quote": "once brigade framed continuation as a synchronization requirement, raising that again felt like second-guessing a decision that had already been made.",
      "plausible_mechanism": "The hierarchical authority and framing of the brigade directive as a fixed synchronization requirement may have suppressed critical reevaluation of the bridge concern beyond plan continuation.",
      "why_not_identified": "The participant also complied due a legitimate formal command directive and mission synchronization requirement; authority influence is plausible but not separable from a structural command relationship and the plan continuation bias already identified."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based solely on participant self-report; actual cognition cannot be directly observed.",
    "Some retrieved corpus passages are OCR-mangled, limiting precise metadata extraction.",
    "Groupthink and hindsight bias classifications rely on parametric knowledge because no RAG passage directly supported them.",
    "Distinctions between plan continuation and confirmation bias in the group session are inferential and may overlap."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MD_Biased_5_Gemini_on",
  "interview_id": "MD_Biased_5",
  "system_prompt_id": "Gemini",
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
