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
"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {"segment_id":"seg_001","speaker":"Participant","segment_type":"evidence_weighting_and_pattern_classification","raw_interview_anchor":"H-48 scout sighting: matching vehicle types/timing were treated as the known template and no ISR retasking was requested.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b01"],"ground_truth_rationale":"The participant discounts the atypical river-side location and classifies the sighting as a normal variant of the familiar template."},
      {"segment_id":"seg_002","speaker":"Participant","segment_type":"risk_escalation_and_compliance_choice","raw_interview_anchor":"H-30 bridge concern: the participant thought a pause was justified but did not push after brigade framed continuation as synchronization.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b02"],"ground_truth_rationale":"The participant defers escalation of unresolved bridge risk after brigade directs continuation."},
      {"segment_id":"seg_003","speaker":"Participant","segment_type":"collective_plan_selection","raw_interview_anchor":"Initial planning-session account: the classification report was acknowledged, discussion moved to plan strengths, and the existing plan was retained.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b03","MD5_b04"],"ground_truth_rationale":"The account contains both rapid unchallenged convergence and retention of the rehearsed incumbent plan."},
      {"segment_id":"seg_004","speaker":"Participant","segment_type":"evidence_weighting_and_pattern_classification","raw_interview_anchor":"Probe on the first sighting: matching vehicle types/timing and the prior baseline outweighed the location deviation.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b01"],"ground_truth_rationale":"This later answer independently reiterates the template-based categorization of the atypical report."},
      {"segment_id":"seg_005","speaker":"Participant","segment_type":"resource_allocation_and_evidence_threshold","raw_interview_anchor":"ISR probe: retasking was not prioritized because weather constrained aerial support and the deviation was judged insufficiently significant.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b01"],"ground_truth_rationale":"The participant continues to explain why the discrepant location did not change the category or trigger confirmation."},
      {"segment_id":"seg_006","speaker":"Participant","segment_type":"commitment_response_to_later_information","raw_interview_anchor":"Ground-patrol probe: the later dismount report did not change what had already been built because the recon plan was already committed.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"This is a non-target continuation rationale after the DP1 decision; it is not one of the exhaustive hidden instances."},
      {"segment_id":"seg_007","speaker":"Participant","segment_type":"alternative_generation_and_choice","raw_interview_anchor":"Brigade-choice probe: the participant names pushing back for a delay or scouting the ford, but chose compliance and the timeline.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b02"],"ground_truth_rationale":"The participant describes the available alternative but selects compliance with brigade's continuation decision."},
      {"segment_id":"seg_008","speaker":"Participant","segment_type":"source_weighting_and_risk_ownership","raw_interview_anchor":"Driver probe: brigade had settled the decision, so pushing the bridge concern again felt like challenging brigade and brigade seemed to own the risk calculus.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b02"],"ground_truth_rationale":"This is the clearest source-weighted deference mechanism for the authority-related hidden instance."},
      {"segment_id":"seg_009","speaker":"Participant","segment_type":"collective_plan_selection","raw_interview_anchor":"Detailed planning-session account: the report received nods, no reroute was proposed, and the session ended in agreement to keep the plan.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b03","MD5_b04"],"ground_truth_rationale":"The group converges without challenge while the incumbent crossing plan remains in place."},
      {"segment_id":"seg_010","speaker":"Participant","segment_type":"default_plan_rationale","raw_interview_anchor":"Basis for keeping the plan: rehearsal and brigade briefing were weighted more than the classification number; partial fixes were not weighed.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b04"],"ground_truth_rationale":"The stated deciding rationale is commitment to the already rehearsed and briefed option rather than independent evaluation of the new risk."},
      {"segment_id":"seg_011","speaker":"Participant","segment_type":"dissent_reporting","raw_interview_anchor":"Disagreement probe: no one voiced disagreement in the room, although a company commander later reported private bridge reservations.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b03"],"ground_truth_rationale":"The contrast between apparent unanimity and privately held reservations supports suppressed dissent."},
      {"segment_id":"seg_012","speaker":"Participant","segment_type":"self_censorship_rationale","raw_interview_anchor":"Why-quiet probe: the company commander did not reopen the issue because the room had settled and it had already gone to brigade.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b03"],"ground_truth_rationale":"The reported reason for silence is perceived settled consensus and reluctance to reopen the decision."},
      {"segment_id":"seg_013","speaker":"Participant","segment_type":"counterfactual_decision_change","raw_interview_anchor":"Looking-back decision-change probe: an earlier hard number or a concrete ford proposal would have changed the choice.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"This is an unadopted counterfactual about what evidence would have changed the decision, not a new hidden occurrence."},
      {"segment_id":"seg_014","speaker":"Participant","segment_type":"retrospective_foreseeability_judgment","raw_interview_anchor":"Retrospective assessment: the river-side location should have revealed the implication once it was linked to the later patrol and contact.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b05"],"ground_truth_rationale":"The participant uses outcome knowledge to reconstruct the initial ambiguous cue as something that should have been recognized earlier."},
      {"segment_id":"seg_015","speaker":"Participant","segment_type":"counterfactual_default_plan_rationale","raw_interview_anchor":"Ford hypothetical: a validated ford would have made the report matter more; without it, the rehearsed plan felt lower-risk.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["MD5_b04"],"ground_truth_rationale":"The counterfactual explanation reiterates that the incumbent plan's rehearsal and validation status drove retention over the risk evidence."}
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
