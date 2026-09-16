You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "The transcript contains four discrete decision episodes: early watch-to-warning upgrade, radar-signature track commitment, activation-level response to a director hold, and public-messaging alignment on a coordination call. Four bias occurrences were identified based on the participant's stated reasoning."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Conformity bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Insensitivity to sample size",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Insensitivity to sample size",
      "alternative_labels": [
        "Sample size neglect",
        "Belief in the law of small numbers",
        "Law of small numbers"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge a small sample as highly informative based on internal consistency while neglecting the statistical instability introduced by small sample size.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Early watch-to-warning upgrade decision",
      "decision_point_description": "Whether to upgrade watch-to-warning based on the partial 06Z convection-allowing ensemble or wait for the fuller 09Z cycle.",
      "affected_reasoning_operation": "Probabilistic inference from ensemble model agreement",
      "bias_specific_mechanism": "The participant treated agreement among three of four completed model runs as strong evidence of a true atmospheric pattern, thereby dismissing the small sample size that made that agreement unreliable.",
      "manifestation_in_interview": "The participant explicitly stated that the number of ensemble members did not matter and that agreement alone was meaningful.",
      "effect_on_reasoning_or_decision": "Led to an early watch-to-warning upgrade before the fuller ensemble became available.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Three of the four members agreeing was a strong signal to me. When you get that kind of consistency across model runs, it usually means something real is going on with the pattern.",
          "evidence_explanation": "This identifies the active choice: the participant made the early upgrade based on a three-of-four partial-ensemble signal."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. I mean, agreement is agreement. If three separate runs are telling you the same intensification story, that's meaningful regardless of how many total members happened to finish by that hour.",
          "evidence_explanation": "This directly shows insensitivity to sample size: the participant denies that having only four members affects how much weight the agreement should carry."
        }
      ],
      "correction_or_counterevidence": "SPC explicitly flagged low confidence and limited guidance, and the participant noted he was still monitoring the later 09Z cycle; however, these cautions did not prevent overinterpretation of the partial sample.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a canonical definition of insensitivity to sample size; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": [
        "Representativeness bias",
        "Similarity heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the probability of an event by the degree to which it resembles a previously encountered case or category, while ignoring base rates and reliability cues.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Radar-signature track commitment",
      "decision_point_description": "Whether to commit to one track for the radar signature or maintain a dual-track hedging approach.",
      "affected_reasoning_operation": "Pattern recognition and probabilistic track judgment",
      "bias_specific_mechanism": "The participant judged the current storm's likely track by its similarity to a single memorable prior event, generating high subjective confidence and dismissing a dual-track alternative without independent verification.",
      "manifestation_in_interview": "The participant reported that the hook signature 'just clicked' because it resembled a prior successful forecast, and he did not seek WFO review before committing.",
      "effect_on_reasoning_or_decision": "Locked the participant onto one track and reduced hedging; WFO independent read was not requested before commitment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the moment I saw that hook signature, it just clicked. I'd seen that exact shape develop the same way before, and it played out almost identically that time — same track, same timing window. I didn't feel like I needed to keep hedging between two tracks once I recognized the pattern.",
          "evidence_explanation": "This shows the participant used similarity to a memorable prior event, rather than current verification evidence, to collapse a dual-track possibility into one track."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Pretty high, honestly — nine out of ten maybe. It looked so much like that prior case that I didn't see much reason to hedge.",
          "evidence_explanation": "This links the similarity-based judgment to high subjective confidence and reduced hedging."
        }
      ],
      "correction_or_counterevidence": "The WFO was independently tracking a dual-track possibility, and the participant later stated he would slow down and get a second set of eyes; however, this retrospective view does not negate the bias at the time of the track call.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a canonical definition of the representativeness heuristic; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Authority bias",
      "alternative_labels": [
        "Obedience to authority",
        "Deference to authority"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to grant undue epistemic weight or sufficiency to the statements or directives of an authority figure, beyond what the evidence or formal constraint requires.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Activation-level response to director hold",
      "decision_point_description": "Whether to accept the director's hold directive without presenting sub-watershed exceedance data or logging a formal escalation recommendation.",
      "affected_reasoning_operation": "Evidence communication and dissent escalation under authority instruction",
      "bias_specific_mechanism": "Instead of treating the director's hold as solely a formal sign-off constraint, the participant treated the director's review as substantively settling the hazard analysis, thereby suppressing available contradicting evidence and dissent.",
      "manifestation_in_interview": "The participant reported that once the director made the call, the director's read of the situation felt like enough to settle it, so he did not present the trending numbers or push back.",
      "effect_on_reasoning_or_decision": "The participant held the escalation and did not present contradictory hydrologic data or log a formal disagreement.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I could have — there's a process for flagging a disagreement or requesting reconsideration. I just didn't go that route. Once he'd made the call, it felt like his read of the situation was enough to settle it, so I didn't walk him through the trending numbers or push back on the hold.",
          "evidence_explanation": "This demonstrates that the participant treated the director's authority as substantive evidence sufficient to settle the issue, rather than merely complying because he lacked sign-off authority."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He asked afterward for a written justification for the hold, and I had to go back and construct one after the fact.",
          "evidence_explanation": "This indicates that the participant did not reach the hold decision through an independent technical rationale, supporting the inference that authority deference shaped acceptance."
        }
      ],
      "correction_or_counterevidence": "The director had formal sign-off authority, so the participant was not free to escalate unilaterally; however, a formal disagreement or reconsideration process was available and not used, which is why this occurrence is rated low-confidence rather than non-bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a canonical definition of authority bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Conformity bias",
      "alternative_labels": [
        "Social proof bias",
        "Herd behavior",
        "Bandwagon effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to align one's judgments or actions with a majority group even in the face of contrary local evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Coordination call public-messaging decision",
      "decision_point_description": "Whether to escalate public messaging and issue a WEA based on local guidance or align with neighboring jurisdictions holding steady.",
      "affected_reasoning_operation": "Risk communication and decision to act amid social comparison",
      "bias_specific_mechanism": "The participant used the majority of neighboring desks as a reference for appropriate action, causing him to override his own worsening local hydrologic evidence.",
      "manifestation_in_interview": "The participant stated that when the majority of desks were holding, going a different direction felt like it needed more justification than staying with the group.",
      "effect_on_reasoning_or_decision": "The participant stayed aligned with the group and did not issue a WEA or escalate messaging despite his own worsening local guidance.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Going into that call, my own numbers favored escalating messaging and issuing a WEA. But three of the four neighboring jurisdictions said they were holding steady, and it just felt safer to stay aligned with that rather than break from the group on my own.",
          "evidence_explanation": "This demonstrates that the participant changed course from his own evidence-based judgment in response to the majority position."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Right, it had ticked up further. But when the majority of the desks on the call are holding, going a different direction on your own feels like it needs more justification than staying with the group does.",
          "evidence_explanation": "This shows continued conformity pressure dominating even after local guidance worsened."
        }
      ],
      "correction_or_counterevidence": "Regional coordination may legitimately favor aligned messaging; however, the neighboring jurisdictions merely stated they were holding, and no binding consensus required suppressing the participant's local WEA decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a canonical definition of conformity bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory bias",
        "Selective exposure"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Radar-signature track call",
      "supporting_interview_quote": "I didn't loop them in before committing, no. It felt clear enough on its own.",
      "plausible_mechanism": "After recognizing the hook signature, the participant may have avoided obtaining an independent WFO read that could disconfirm the single-track interpretation.",
      "why_not_identified": "The transcript does not show active gathering or weighting of confirming evidence or explicit rejection of contradictory evidence; the pattern is more parsimoniously explained by representativeness-driven overconfidence."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring and adjustment",
        "Anchoring"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Early watch-to-warning upgrade decision",
      "supporting_interview_quote": "Three of the four members agreeing was a strong signal to me. When you get that kind of consistency across model runs, it usually means something real is going on with the pattern.",
      "plausible_mechanism": "The initial partial-ensemble signal may have anchored the participant's interpretation, with insufficient adjustment for SPC's low-confidence caveat.",
      "why_not_identified": "The transcript shows an explicit dismissal of sample size rather than a numeric anchor-and-adjustment sequence; insensitivity to sample size is the more precise mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific passages directly supported the specific labels in this analysis, so the classifications rely on established general cognitive-science knowledge rather than corpus-anchored support.",
    "The transcript is retrospective self-report, which may involve memory reconstruction or post-hoc rationalization.",
    "The authority and coordination decisions occurred within hierarchical and interagency constraints, so those findings are assigned low-to-moderate confidence.",
    "The analysis does not use outcome information to classify biases; all biases are assessed using the participant's stated reasoning available at the time of each decision."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Biased_4_Gemini_on",
  "interview_id": "EM_Biased_4",
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
