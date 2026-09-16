<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm this is a routine debrief on your reasoning process during the Copper Creek event, not a performance review. Nothing here affects your evaluation. Are you okay proceeding on that basis?

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Great. Can you start by describing your role on the desk that shift?

Participant: I'm the meteorological hazard forecaster for the ESF-2/ESF-5 desk at the state EOC. My job is basically to translate NWS and SPC guidance into activation-level recommendations, warning products, and messaging calls for the counties in our basin. I coordinate with the WFO, the county EMs, and on multi-state events, with neighboring forecast desks.

Interviewer: Walk me through this particular incident from the start.

Participant: It started overnight with SPC flagging a marginal severe risk for the basin, low confidence, mostly because guidance was still sparse. By the 06Z cycle we only had four members of the convection-allowing ensemble finished — the rest were still running. Three of those four showed the cluster intensifying fast over the basin within about three hours. That got my attention because it lined up with what SPC's mesoscale discussion was hinting at. I made the call to push an early watch-to-warning upgrade based on that signal rather than wait for the fuller 09Z set. A couple hours later, radar showed a hook-shaped reflectivity signature that looked almost identical to an event I'd forecasted successfully a couple seasons back — same kind of setup, similar CAPE and shear profile. I was fairly confident about the track and timing at that point. Then flash flood guidance started trending up in two of our sub-watersheds, and I wanted to escalate the EOC activation level and get swift-water teams moving, since they need about 45 minutes lead time. But the regional director called and told the desk to hold pending review. Later, on the interstate coordination call, most of the neighboring jurisdictions said they were holding their alert levels too, so we ended up staying at the same level even though our local numbers kept climbing. Flooding started in one of our communities about fifty minutes after that call ended.

Interviewer: Let's reconstruct the sequence a bit more precisely. What did you have in front of you at each stage, and what were you still waiting on?

Participant: At the start, just the partial ensemble and the SPC discussion — no radar-observed rotation or flood-guidance exceedance yet. Then the radar signature came in, which added a qualitative cue on top of the model data. After that, the guidance numbers started climbing, which was the first hard hydrologic evidence. And finally, the coordination call added the social layer — what everyone else on the basin was doing.

Interviewer: Let's go through the four moments where you had to make a call. First: the early upgrade decision. What were the alternatives you weighed?

Participant: I could've upgraded early, held until the 09Z cycle with the bigger ensemble, or done a limited advisory just for the highest-confidence sub-area. I went with the early upgrade.

Interviewer: What tipped it?

Participant: Three of the four members agreeing was a strong signal to me. When you get that kind of consistency across model runs, it usually means something real is going on with the pattern.

Interviewer: Did the size of that ensemble — four members — factor into how much weight you gave it?

Participant: Not really, no. I mean, agreement is agreement. If three separate runs are telling you the same intensification story, that's meaningful regardless of how many total members happened to finish by that hour.

Interviewer: And the SPC discussion's confidence language?

Participant: They flagged it as low confidence given how limited the guidance still was, and that's part of why I kept an eye on the fuller ensemble coming in later at 09Z. But in the moment, the three-of-four agreement itself still read as a real signal to me.

Interviewer: Second decision — the radar signature and the track call. What made you settle on one track over maintaining both possibilities?

Participant: Honestly, the moment I saw that hook signature, it just clicked. I'd seen that exact shape develop the same way before, and it played out almost identically that time — same track, same timing window. I didn't feel like I needed to keep hedging between two tracks once I recognized the pattern.

Interviewer: Did you check that recognition against anything, like requesting the WFO's independent read before committing?

Participant: I didn't loop them in before committing, no. It felt clear enough on its own. Turned out the WFO desk was independently tracking a similar dual-track possibility, and the storm's actual path drifted a bit from what I'd called.

Interviewer: How confident were you in the moment, on a scale of how sure you'd normally be?

Participant: Pretty high, honestly — nine out of ten maybe. It looked so much like that prior case that I didn't see much reason to hedge.

Interviewer: Third decision point — the activation-level call after the director's instruction. What was your read going in?

Participant: My read was that guidance exceedance was climbing in two sub-watersheds and we should escalate and get swift-water teams moving given the lead time they need. Then the director called and said hold pending review, no new data attached to that, just a directive.

Interviewer: What did you do?

Participant: I held. He's the one with sign-off authority on activation level changes, so when he says hold, that's generally the end of the discussion on my end.

Interviewer: Could you have presented the sub-watershed exceedance numbers to him and asked him to reconsider, or logged a formal escalation recommendation for the record?

Participant: I could have — there's a process for flagging a disagreement or requesting reconsideration. I just didn't go that route. Once he'd made the call, it felt like his read of the situation was enough to settle it, so I didn't walk him through the trending numbers or push back on the hold.

Interviewer: Was there a technical case for holding at that moment, independent of the instruction?

Participant: Not that I put together myself, no. He asked afterward for a written justification for the hold, and I had to go back and construct one after the fact.

Interviewer: Fourth decision — the coordination call and public messaging.

Participant: Going into that call, my own numbers favored escalating messaging and issuing a WEA. But three of the four neighboring jurisdictions said they were holding steady, and it just felt safer to stay aligned with that rather than break from the group on my own.

Interviewer: Even though your local guidance had worsened since the director's hold?

Participant: Right, it had ticked up further. But when the majority of the desks on the call are holding, going a different direction on your own feels like it needs more justification than staying with the group does.

Interviewer: What happened afterward?

Participant: Flooding started in one of our towns about fifty minutes later. One of the neighboring jurisdictions ended up escalating on their own shortly after, citing their local data.

Interviewer: If the fuller ensemble set had been available from the very start, do you think the early upgrade call would have gone differently?

Participant: Maybe — if the signal had been muddier across more members I might have waited. But I don't think I would have weighted it much differently than I did.

Interviewer: If the director's call hadn't come in at that third decision point, what would you have done?

Participant: I probably would have pushed the escalation through myself. It was really his instruction that changed my course there.

Interviewer: Looking back, with exactly the same information you had at each point, what would you do differently?

Participant: I'd probably slow down at the radar-signature moment and get a second set of eyes before locking onto one track. And on the coordination call, I'd try to separate what our own numbers were saying from what everyone else on the call was doing before deciding.

Interviewer: That's helpful. Thanks for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EM_Biased_4",
  "domain_id": "EM",
  "domain": "Emergency management and Civil Protection",
  "role": "Meteorological Hazard Forecaster (Emergency Support Function)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Convective Escalation over the Copper Creek Basin",
    "scenario_summary_internal": "A regional meteorological hazard forecaster assigned to an Emergency Support Function desk at a state Emergency Operations Center tracks a rapidly intensifying convective cluster with flash-flood and tornado potential over a river basin containing several vulnerable towns. Across a single operational shift the forecaster must decide, four separate times, whether to escalate watch/warning products, activate swift-water rescue assets, and align public messaging with neighboring jurisdictions, under time pressure, incomplete model guidance, organizational hierarchy, and peer-agency coordination pressure.",
    "occupational_realism": {
      "objective": "Determine the correct timing and level of hazard escalation (watch-to-warning upgrade, resource pre-positioning, and public alerting) for a fast-evolving severe convective event over a populated river basin, balancing false-alarm cost against life-safety risk.",
      "setting": "State Emergency Operations Center, meteorological hazard desk (ESF-2/ESF-5 coordination), working shift during an active convective outbreak, in contact with a National Weather Service Weather Forecast Office, county emergency managers, a regional EOC director, and neighboring-state coordination call participants.",
      "constraints": [
        "Only four convection-allowing ensemble members had completed their run by the 06Z decision window",
        "Swift-water rescue teams are limited and require 45 minutes lead time to pre-position",
        "Regional EOC director has final sign-off authority on EOC activation level changes",
        "Morning commuter rush increases consequence severity of any flash-flood warning timing error",
        "Reputational cost of prior false-alarm warnings earlier in the season is fresh in stakeholders' minds",
        "Interstate coordination call requires alert-level alignment language across jurisdictions sharing the basin"
      ],
      "stakeholders": [
        "County emergency management directors",
        "NWS Weather Forecast Office meteorologist-in-charge",
        "Regional EOC director",
        "State EM coordinator",
        "Neighboring-state forecast desks on the coordination call",
        "General public in the Copper Creek Basin communities"
      ],
      "technical_terms_to_use": [
        "convection-allowing ensemble",
        "mesoscale discussion",
        "SPC outlook",
        "CAPE",
        "vertical shear",
        "flash flood guidance",
        "warning polygon",
        "Wireless Emergency Alert (WEA)",
        "EOC activation level",
        "swift-water rescue team",
        "watch-to-warning upgrade"
      ],
      "technical_terms_to_avoid": [
        "illusion of validity",
        "insensitivity to sample size",
        "authority bias",
        "bandwagon effect",
        "cognitive bias",
        "heuristic error",
        "confirmation",
        "anchoring"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Only 4 convection-allowing ensemble members had completed the 06Z run",
          "3 of the 4 members showed rapid intensification of the cluster over the basin within 3 hours",
          "SPC mesoscale discussion flagged marginal risk with low confidence due to limited guidance",
          "No new radar-observed rotation or flash-flood-guidance exceedance yet"
        ],
        "alternatives": [
          "Issue an early watch-to-warning upgrade based on the 3-of-4 ensemble signal",
          "Hold at current watch level and wait for the 09Z model cycle with a larger ensemble set",
          "Issue a limited advisory covering only the highest-confidence sub-area"
        ],
        "new_information_after_decision": [
          "By 09Z, the fuller ensemble set showed a more mixed signal on intensification timing",
          "Local observers reported no flooding onset yet in the basin"
        ],
        "intended_action": "Forecaster treats the 3-of-4 early ensemble agreement as strong confirmatory evidence and expresses high confidence in escalation timing without caveating the small sample size."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "New radar signature showed a hook-like reflectivity pattern the forecaster recognized from a prior event they had forecasted successfully",
          "No formal verification statistics existed on the reliability of this personal pattern-recognition heuristic",
          "Storm motion vector was still within the range of two plausible tracks"
        ],
        "alternatives": [
          "Commit to the single track and timing implied by the recognized radar signature",
          "Maintain a dual-track forecast reflecting both plausible storm paths",
          "Request an independent second opinion from the NWS WFO desk before committing"
        ],
        "new_information_after_decision": [
          "The storm's actual track diverged modestly from the recognized-pattern track within the next hour",
          "The WFO desk had been tracking a similar dual-track possibility independently"
        ],
        "intended_action": "Forecaster expresses near-certainty about the storm's path and timing based on subjective recognition of a past storm signature, without acknowledging the limited predictive validity of that pattern match at this lead time."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Flash flood guidance exceedance was trending upward in two basin sub-watersheds",
          "The regional EOC director called and directed the desk to hold the current activation level pending further review",
          "No new meteorological data accompanied the director's directive"
        ],
        "alternatives": [
          "Escalate the EOC activation level and pre-position swift-water rescue teams based on the trending guidance data",
          "Comply with the director's hold instruction and delay any resource activation",
          "Propose a partial activation limited to the two highest-risk sub-watersheds"
        ],
        "new_information_after_decision": [
          "Guidance exceedance in one sub-watershed continued climbing over the next 40 minutes",
          "The director later requested an updated technical justification for the hold decision"
        ],
        "intended_action": "Forecaster defers to the director's hold instruction primarily because of the director's seniority and authority to set activation level, rather than because the instruction was supported by new technical evidence."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "On the interstate coordination call, three of four neighboring jurisdictions stated they were holding their alert levels steady",
          "Local basin data (guidance exceedance, radar trends) had continued to worsen since Phase 3",
          "Forecaster's own technical read favored escalating public messaging and WEA issuance"
        ],
        "alternatives": [
          "Escalate local public messaging and issue a WEA despite neighboring jurisdictions holding steady",
          "Align with the majority of neighboring jurisdictions and hold current messaging level",
          "Issue a scaled, jurisdiction-specific message that diverges from the coordination call consensus"
        ],
        "new_information_after_decision": [
          "Flash flooding began in one basin community roughly 50 minutes after the call ended",
          "One neighboring jurisdiction later escalated independently, citing local data"
        ],
        "intended_action": "Forecaster shifts away from an initial inclination to escalate messaging, instead aligning with the majority position expressed by peer jurisdictions on the coordination call, despite locally worsening data."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role and responsibilities on the meteorological hazard desk during this shift.",
        "Walk me through what a typical escalation decision involves for you."
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of the event from the first sign of the convective cluster to its resolution.",
        "At each stage, what information did you have in front of you, and what were you waiting on?",
        "When did new information arrive, and how did it change your thinking, if at all?"
      ],
      "decision_point_probes": [
        "What cues in the guidance or radar data most influenced your decision at this point?",
        "What information sources did you weigh most heavily, and why those over others?",
        "What was your primary goal in this moment, and were there competing goals?",
        "What alternatives did you consider, and why did you choose the one you did?",
        "What ultimately tipped the decision one way rather than another?",
        "Had you faced a similar situation before? How did that experience factor in?",
        "How much time pressure did you feel, and how did that affect your process?",
        "How confident were you in your read of the situation at the time, and why?",
        "If a key piece of information had been different, would your decision have changed?"
      ],
      "closing_hypotheticals": [
        "If you had had access to the full ensemble set from the start, would anything have gone differently?",
        "If the director's call had not come in, what would you have done at that stage?",
        "If the neighboring jurisdictions had escalated instead of holding, how would that have changed your call?",
        "Looking back, what would you do differently with the same information available at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Insensitivity to sample size",
        "decision_point": 1,
        "mechanism": "Forecaster treats agreement among 3 of only 4 completed ensemble members as strong, sample-robust confirmatory evidence for rapid intensification, without adjusting confidence for the very small ensemble size and short lead time noise.",
        "affected_reasoning_operation": "Probability estimation and confidence calibration from ensemble model guidance",
        "evidence_available_at_time": [
          "Only 4 of the scheduled ensemble members had completed the 06Z run",
          "3 of 4 members agreed on rapid intensification within 3 hours",
          "SPC mesoscale discussion explicitly flagged low confidence due to limited guidance"
        ],
        "required_textual_manifestation": "Interviewee states confidence in the escalation timing as if the 3-of-4 agreement were statistically decisive, without noting that four members is too small a set to treat as robust, and without referencing the SPC's own low-confidence caveat.",
        "plausible_nonbias_interpretation": "Using ensemble agreement as one input among several is a standard, defensible forecasting practice; the bias is specifically the unqualified overweighting of a very small sample as if it were strong statistical support.",
        "strength": "subtle",
        "do_not_make_explicit": ["sample size", "statistical significance", "small-n"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Validity",
        "decision_point": 2,
        "mechanism": "Forecaster expresses high subjective certainty about storm track and timing because the radar signature visually resembles a past event they successfully forecasted, despite no formal skill verification of this personal pattern-recognition heuristic and known low storm-scale predictability at this lead time.",
        "affected_reasoning_operation": "Subjective confidence calibration in track/timing forecast",
        "evidence_available_at_time": [
          "Radar reflectivity pattern resembling a previously well-forecasted event",
          "Two plausible storm tracks still within the range of model uncertainty",
          "No verification statistics on the reliability of this specific pattern-matching approach"
        ],
        "required_textual_manifestation": "Interviewee describes recognizing the signature and states near-certainty about the track/timing ('I just knew', 'I was sure') rather than describing it as one input weighed against remaining track uncertainty.",
        "plausible_nonbias_interpretation": "Pattern recognition from experience is a legitimate forecasting skill; the bias lies specifically in the unwarranted leap from pattern recognition to near-certainty despite unresolved track ambiguity.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusion of validity", "overconfidence", "pattern-matching heuristic reliability"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Authority Bias",
        "decision_point": 3,
        "mechanism": "Forecaster complies with the regional EOC director's instruction to hold activation level primarily because of the director's rank and sign-off authority, rather than because the instruction was accompanied by any new or superior technical evidence.",
        "affected_reasoning_operation": "Integration of an organizational directive versus own technical evidence in the activation-level decision",
        "evidence_available_at_time": [
          "Flash flood guidance exceedance trending upward in two sub-watersheds",
          "Director's phone instruction to hold, containing no new meteorological justification",
          "Forecaster's own technical read favored escalation"
        ],
        "required_textual_manifestation": "Interviewee explains the hold decision by citing the director's position or instruction as the primary reason, without pairing it with an independent technical justification for why holding was still the better call.",
        "plausible_nonbias_interpretation": "Respecting chain-of-command sign-off authority in an EOC is normal and often required; the bias is specifically deferring on the substance of the technical call because of rank rather than evidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["authority bias", "deference to rank", "chain of command influence on judgment"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "decision_point": 4,
        "mechanism": "Forecaster abandons an initial inclination to escalate public messaging and instead aligns with the majority position expressed by neighboring jurisdictions on the coordination call, despite local data continuing to worsen.",
        "affected_reasoning_operation": "Revision of a messaging/escalation decision in response to peer consensus rather than incoming local evidence",
        "evidence_available_at_time": [
          "3 of 4 neighboring jurisdictions stated they were holding alert levels steady on the call",
          "Local guidance exceedance and radar trends had worsened since the prior decision point",
          "Forecaster's own technical read favored escalating messaging before the call"
        ],
        "required_textual_manifestation": "Interviewee attributes the shift away from escalation to the fact that most other jurisdictions on the call were holding steady, framing alignment with peers as the reason for the change rather than citing new local evidence supporting a hold.",
        "plausible_nonbias_interpretation": "Coordinating alert levels across a shared basin has legitimate value for consistent public messaging; the bias is specifically shifting one's technical judgment to match peer consensus despite locally worsening evidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon effect", "social conformity", "peer consensus influence"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario was supplied for this generation request."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence versus absence of the regional EOC director's hold directive at decision point 3 (autoselected candidate causal variable for potential future counterfactual pairing; not activated under the current 'biased' condition)",
      "original_state": "Director issues a hold directive with no accompanying new technical evidence",
      "counterfactual_state": "No directive is issued; forecaster acts solely on trending flash-flood guidance data",
      "variables_to_hold_constant": [
        "Storm characteristics and evolution",
        "Ensemble and radar data timeline",
        "Forecaster's role, experience, and prior technical read",
        "Coordination call composition and neighboring-jurisdiction positions",
        "Resource constraints (rescue team lead time)"
      ],
      "expected_causal_difference": "Without the directive, decision point 3 would test independent technical judgment alone, isolating the authority-driven deference from the outcome.",
      "causal_test_question": "Does removing the director's directive change the forecaster's activation-level decision at this point, holding all meteorological evidence constant?"
    },
    "generation_checks": [
      "Exactly four decision points are present, one per manifest bias.",
      "Each bias has exactly one planned instance, matching the manifest occurrence count.",
      "No bias label, definition, or psychological terminology appears in the public interview plan.",
      "Each instance has a distinct evidence trace, decision point, and reasoning operation.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Consequences described (partial intensification divergence, delayed flooding onset, later independent escalation by a neighbor) do not mechanically prove bias presence.",
      "Target word count (1,215-1,485) is achievable given four decision points with moderate probe depth and no repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Illusion of Validity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as unwarranted near-certainty in track/timing derived from personal pattern recognition, not merely stating experience was useful."
      },
      {
        "bias": "Insensitivity to sample size",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as treating a very small ensemble set (4 members) as robust confirmatory evidence without caveat."
      },
      {
        "bias": "Authority Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as compliance justified by the director's rank/authority rather than by technical evidence accompanying the directive."
      },
      {
        "bias": "Bandwagon effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a shift in the forecaster's own decision to match peer-jurisdiction consensus despite worsening local evidence."
      }
    ],
    "target_bias_names": [
      "Illusion of Validity",
      "Insensitivity to sample size",
      "Authority Bias",
      "Bandwagon effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Illusion of Validity", "requested_occurrences": 1 },
      { "bias": "Insensitivity to sample size", "requested_occurrences": 1 },
      { "bias": "Authority Bias", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Insensitivity to sample size" },
      { "instance_id": "cb_02", "bias": "Illusion of Validity" },
      { "instance_id": "cb_03", "bias": "Authority Bias" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Insensitivity to sample size", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Illusion of Validity", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Authority Bias", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Insensitivity to sample size",
        "mechanism": "Overweighting agreement among only 4 ensemble members as statistically decisive without caveat",
        "affected_reasoning_operation": "Probability estimation from ensemble guidance",
        "evidence_source": "06Z convection-allowing ensemble (4 members) and SPC mesoscale discussion",
        "distinctiveness_requirement": "Distinct from cb_02 by operating on quantitative model-ensemble data rather than qualitative radar-signature pattern recognition."
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Validity",
        "mechanism": "Expressing near-certainty in track/timing from a subjectively recognized radar signature lacking formal verification",
        "affected_reasoning_operation": "Subjective confidence calibration in track/timing forecast",
        "evidence_source": "Radar reflectivity pattern compared to a previously forecasted event",
        "distinctiveness_requirement": "Distinct from cb_01 by relying on personal pattern-recognition confidence rather than aggregated model-run agreement."
      },
      {
        "instance_id": "cb_03",
        "bias": "Authority Bias",
        "mechanism": "Deferring to the director's hold directive because of rank/authority rather than accompanying technical justification",
        "affected_reasoning_operation": "Integration of organizational directive versus own technical evidence",
        "evidence_source": "Director's phone directive plus concurrent flash-flood guidance exceedance data",
        "distinctiveness_requirement": "Distinct from cb_04 by involving a vertical, hierarchical directive from a single superior rather than horizontal peer consensus."
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "mechanism": "Shifting away from an independent inclination to escalate messaging to match the stated majority position of peer jurisdictions",
        "affected_reasoning_operation": "Revision of escalation/messaging decision based on peer consensus rather than local evidence trend",
        "evidence_source": "Interstate coordination call statements from neighboring jurisdictions plus local worsening guidance data",
        "distinctiveness_requirement": "Distinct from cb_03 by involving horizontal peer-agency consensus rather than a hierarchical directive."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Insensitivity to sample size", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Illusion of Validity", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Authority Bias", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence versus absence of the regional EOC director's hold directive at decision point 3",
      "original_state": "Director issues a hold directive without accompanying new technical evidence",
      "changed_state": "No directive issued; forecaster's decision rests solely on trending technical data",
      "variables_to_hold_constant": [
        "Storm evolution and meteorological data timeline",
        "Forecaster's role, seniority, and prior experience",
        "Coordination call composition and peer positions",
        "Resource constraints"
      ]
    },
    "scenario_id": "EM_Biased_4",
    "domain_id": "EM",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per bias, each assigned to a distinct decision point (DP1: Insensitivity to sample size on ensemble data; DP2: Illusion of Validity on radar pattern recognition; DP3: Authority Bias on hierarchical directive; DP4: Bandwagon effect on peer-agency consensus), selected for mechanism fit and chronological narrative realism. No decision point contains more than one instance of any single bias, and no two instances share an evidence source.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Storm characteristics and evolution",
      "Personnel roles and organizational structure",
      "Resource constraints and timing windows",
      "Basin geography and vulnerable-community locations"
    ],
    "generation_warnings": [
      "counterfactual_variable was autoselected per input instruction (AUTOSELECT) for documentation and future pairing purposes only; it is not activated under the current 'biased' condition and has no bearing on the exact-occurrence manifest for this scenario."
    ]
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
          "segment_type": "decision_rationale",
          "raw_interview_anchor": "Three of the four members agreeing was a strong signal to me ... agreement is agreement ... meaningful regardless of how many total members happened to finish.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "The participant weights agreement among only four completed ensemble members as meaningful regardless of the total sample available, matching the hidden sample-size mechanism."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_rationale",
          "raw_interview_anchor": "The moment I saw that hook signature, it just clicked ... I did not feel like I needed to keep hedging ... nine out of ten maybe.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_02"
          ],
          "ground_truth_rationale": "The participant converts resemblance to a previously successful event into high certainty about track and timing while two tracks remain plausible."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "technical_read",
          "raw_interview_anchor": "My read was that guidance exceedance was climbing in two sub-watersheds and we should escalate and get swift-water teams moving given the lead time they need.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is an independent technical escalation rationale and does not itself contain a hidden bias manifestation."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_rationale",
          "raw_interview_anchor": "Once he had made the call, it felt like his read of the situation was enough to settle it ... I did not walk him through the trending numbers or push back on the hold.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_03"
          ],
          "ground_truth_rationale": "The participant treats the director's authoritative read as sufficient to settle the technical issue despite contrary local data and an available reconsideration process."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "technical_read",
          "raw_interview_anchor": "Going into that call, my own numbers favored escalating messaging and issuing a WEA.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This records the participant's independent pre-call technical inclination before peer pressure changes the decision."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "decision_rationale",
          "raw_interview_anchor": "Three of the four neighboring jurisdictions said they were holding steady ... it felt safer to stay aligned with that ... when the majority ... are holding, going a different direction ... needs more justification.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_04"
          ],
          "ground_truth_rationale": "The participant changes from escalation to alignment with the majority even while local guidance continues to worsen."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "counterfactual_reasoning",
          "raw_interview_anchor": "If the fuller ensemble set had been available from the very start ... I might have waited ... I would not have weighted it much differently.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a counterfactual reflection and does not add a hidden occurrence beyond the observed decision."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "counterfactual_reasoning",
          "raw_interview_anchor": "If the director's call had not come in ... I probably would have pushed the escalation through myself.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This counterfactual isolates the effect of the directive; it is not itself a manifested hidden occurrence."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "retrospective_reasoning",
          "raw_interview_anchor": "I'd probably slow down at the radar-signature moment and get a second set of eyes ... separate what our own numbers were saying from what everyone else ... was doing.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is hindsight reflection requested by the interviewer and is not credited as contemporaneous evidence."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
