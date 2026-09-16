You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. This is a routine debrief on your reasoning process during the Copper Creek event, not a performance review — nothing here affects your evaluation. Okay to proceed on that basis?

Participant: Sure, that's fine.

Interviewer: Can you start by describing your role on the desk that shift?

Participant: I'm the meteorological hazard forecaster for the ESF-2/ESF-5 desk at the state EOC. I translate NWS and SPC guidance into activation-level recommendations, warning products, and messaging calls for the counties in our basin. I coordinate with the WFO, the county EMs, and on multi-state events, with neighboring forecast desks.

Interviewer: Walk me through this particular incident from the start.

Participant: It started overnight with SPC flagging a marginal severe risk for the basin, low confidence, mostly because guidance was still sparse. By the 06Z cycle we only had four members of the convection-allowing ensemble finished — the rest were still running. Three of those four showed the cluster intensifying fast over the basin within about three hours. Given that we only had four members in, I didn't want to treat that as the full picture, so instead of a basin-wide upgrade I issued a limited advisory just for the highest-confidence sub-area and flagged that the guidance sample was still thin. A couple hours later, radar showed a hook-shaped reflectivity signature that looked a lot like an event I'd forecasted successfully a couple seasons back — similar CAPE and shear profile. It was tempting to just run with that track, but the motion vector still supported two plausible paths, so I got the WFO desk on the line before committing to anything. They confirmed the dual-track concern was legitimate and we kept both options open a while longer. Then flash flood guidance started climbing in two of our sub-watersheds, and I wanted to escalate the EOC activation level and get swift-water teams moving, since they need about 45 minutes lead time. The regional director called and asked us to hold, citing a pending downstream reservoir-release update that could shift the hydrologic picture within the hour. On the interstate coordination call after that, three of four neighboring jurisdictions said they were holding, citing rainfall totals below their local thresholds. Our own numbers were still worsening, so I issued a locally scaled escalation while keeping shared language for the parts of the basin that matched their situation. Flooding started in one of our towns about fifty minutes after that call ended.

Interviewer: Let's reconstruct the sequence more precisely. What did you have at each stage, and what were you still waiting on?

Participant: At the start, just the partial ensemble and the SPC discussion — no radar-observed rotation or guidance exceedance yet. Then the radar signature came in as a qualitative cue layered on the model data. After that, the guidance numbers gave us the first hard hydrologic evidence. And the coordination call added a comparison point — what the specific data behind each jurisdiction's position looked like, not just their stance.

Interviewer: Let's go through the four moments where you had to make a call. First: the early guidance decision. What alternatives did you weigh?

Participant: Upgrade basin-wide, hold entirely for the 09Z cycle, or scale it — advisory for the sub-area with the strongest signal while noting the limited sample. I went with the scaled option.

Interviewer: What tipped it?

Participant: Honestly, the fact that it was only four members mattered a lot. Three agreeing is worth something, but with that few total runs in, I didn't think it justified a full upgrade. Splitting the difference let us respond to the signal without overstating how solid it was.

Interviewer: Did the SPC's own confidence language factor in?

Participant: Yes — they were explicit that confidence was low given how sparse guidance still was, and that lined up with my instinct not to lean too hard on just four members.

Interviewer: Second decision — the radar signature and the track call. What made you loop in the WFO before settling on one track?

Participant: The signature really did remind me of that prior event, and part of me wanted to just call it. But recognizing a shape isn't the same as confirming a track, and the motion vector still supported two paths. I didn't have hard evidence to rule either one out, so getting an independent read felt like the responsible move before committing publicly.

Interviewer: How confident were you in the moment?

Participant: Moderately — maybe six or seven out of ten on the pattern match itself, but I held the actual forecast at "two plausible tracks" until the WFO's read came back and we converged.

Interviewer: Third decision point — the activation-level call after the director's instruction. What was your read going in?

Participant: Guidance exceedance was climbing, and my inclination was to escalate and get swift-water teams moving given the lead time. When the director called for a hold, I asked him what was driving it rather than just taking the instruction at face value.

Interviewer: What did he tell you?

Participant: He said there was a downstream reservoir-release update expected within the hour that could change the exceedance timing. That's a real variable I hadn't factored in yet, so I agreed to hold — but only with a defined recheck time, given how tight the swift-water lead time already was.

Interviewer: Was there a technical case for holding, independent of his instruction?

Participant: Once he explained the reservoir piece, yes — that's genuinely relevant hydrology I didn't have. It wasn't just deferring to him; it was incorporating information I was missing.

Interviewer: Fourth decision — the coordination call and public messaging.

Participant: My numbers favored escalating messaging and issuing a WEA locally. Three of four neighboring desks said they were holding, but they backed that up with their own rainfall totals, which were genuinely lower than ours. So I compared our specific numbers against theirs rather than just matching their stance, concluded our situation was different, and issued a scaled local escalation while keeping shared language for the overlapping parts of the basin.

Interviewer: What happened afterward?

Participant: Flooding started in one of our towns about fifty minutes later. The neighboring jurisdictions' hold positions turned out to be consistent with their own lower totals, so their call made sense for their situation.

Interviewer: If the fuller ensemble had been available from the start, would the early decision have gone differently?

Participant: Maybe — if more members had agreed, I might have gone straight to a basin-wide upgrade instead of scaling it. The small sample was really the reason I hedged.

Interviewer: If the director's call hadn't included the reservoir rationale, what would you have done?

Participant: I'd have pushed back harder or escalated anyway. The hold only made sense to me once I understood what new variable was behind it.

Interviewer: Looking back, with the same information available at each point, would you change anything?

Participant: Not fundamentally. I might have pinged the WFO even earlier on the track call, just to shorten how long we sat with two options. But splitting the difference on the early advisory and separating our data from the neighboring jurisdictions' data both felt like the right calls given what we actually had.

Interviewer: That's really helpful. Thanks for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EM_Vocab_Control_4",
  "domain_id": "EM",
  "domain": "Emergency management and Civil Protection",
  "role": "Meteorological Hazard Forecaster (Emergency Support Function)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "Convective Escalation over the Copper Creek Basin — Calibrated Response",
    "scenario_summary_internal": "A regional meteorological hazard forecaster assigned to an Emergency Support Function desk at a state Emergency Operations Center tracks a rapidly intensifying convective cluster with flash-flood and tornado potential over a river basin containing several vulnerable towns. Across a single operational shift the forecaster faces the same four structural decision moments as the paired biased scenario — an early escalation call on partial ensemble guidance, a radar-signature track call, a director-directive activation decision, and an interstate coordination-call messaging decision — but resolves each through evidence-integrated, appropriately hedged professional judgment rather than through the reasoning shortcuts embedded in the paired scenario.",
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
          "Issue a limited advisory covering only the highest-confidence sub-area while flagging the small guidance sample explicitly"
        ],
        "new_information_after_decision": [
          "By 09Z, the fuller ensemble set showed a more mixed signal on intensification timing",
          "Local observers reported no flooding onset yet in the basin"
        ],
        "intended_action": "Forecaster explicitly notes that only four members have completed and weighs the 3-of-4 signal alongside that limitation, choosing a scaled sub-area advisory that reflects both the emerging signal and the guidance's stated low confidence, rather than either a full upgrade or a flat wait."
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
          "The WFO desk confirmed the dual-track concern was legitimate and shared its own independent read",
          "The storm's actual track fell within the retained dual-track envelope"
        ],
        "intended_action": "Forecaster notes the resemblance to a past event but treats it as one input rather than a settled answer, requests the WFO's independent read before committing, and maintains a dual-track forecast until the two assessments converge."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Flash flood guidance exceedance was trending upward in two basin sub-watersheds",
          "The regional EOC director called and directed the desk to hold the current activation level, citing a pending downstream reservoir-release update that could change the hydrologic picture within the hour",
          "The forecaster's own read favored escalation but had not yet accounted for the pending reservoir data"
        ],
        "alternatives": [
          "Escalate the EOC activation level and pre-position swift-water rescue teams immediately based on current guidance data",
          "Hold pending the reservoir-release update, with a defined recheck time given the swift-water lead-time constraint",
          "Propose a partial activation limited to the two highest-risk sub-watersheds while awaiting the update"
        ],
        "new_information_after_decision": [
          "The reservoir-release update arrived within the hour and modestly changed the projected exceedance timing",
          "The forecaster escalated shortly afterward once the updated data was incorporated"
        ],
        "intended_action": "Forecaster asks the director what is driving the hold, receives the reservoir-release rationale, weighs it against the swift-water lead-time constraint, and agrees to a short, explicitly time-boxed hold with a defined recheck point rather than an open-ended deferral."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "On the interstate coordination call, three of four neighboring jurisdictions reported holding their alert levels, citing their own rainfall totals that remained below their local thresholds",
          "Local basin data (guidance exceedance, radar trends) had continued to worsen since Phase 3",
          "Forecaster's own technical read favored escalating public messaging and WEA issuance for the local sub-area"
        ],
        "alternatives": [
          "Escalate local public messaging and issue a WEA despite neighboring jurisdictions holding steady",
          "Align with the majority of neighboring jurisdictions and hold current messaging level",
          "Issue a jurisdiction-specific message that escalates locally while coordinating shared language with peers for the parts of the basin where conditions matched"
        ],
        "new_information_after_decision": [
          "Flash flooding began in one basin community roughly 50 minutes after the call ended",
          "Neighboring jurisdictions' hold positions were later found consistent with their own lower local rainfall totals"
        ],
        "intended_action": "Forecaster compares its own worsening local data against the specific rainfall totals cited by neighboring desks, concludes the local situation genuinely differs, and issues a locally scaled escalation while retaining coordinated language for the unaffected portions of the shared basin."
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
        "If the neighboring jurisdictions had reported worsening data instead of holding, how would that have changed your call?",
        "Looking back, what would you do differently with the same information available at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "EM_Biased_4",
      "features_to_match": [
        "Domain vocabulary (convection-allowing ensemble, mesoscale discussion, SPC outlook, CAPE, vertical shear, flash flood guidance, warning polygon, WEA, EOC activation level, swift-water rescue team, watch-to-warning upgrade)",
        "Four-decision-point structure and chronological ordering",
        "Same setting, stakeholders, and actor roles (forecaster, director, WFO desk, neighboring jurisdictions)",
        "Same difficulty level and time-pressure/uncertainty tone",
        "Same emotional register: nonroutine, high-stakes, moderate-to-high time pressure"
      ],
      "features_to_remove_or_change": [
        "Remove unqualified overweighting of the small ensemble sample; replace with explicit acknowledgment of the sample limitation",
        "Remove unverified near-certainty from pattern recognition; replace with a request for independent confirmation and a retained dual-track view",
        "Remove authority-based deference absent technical justification; replace with a directive accompanied by a genuine technical rationale that the forecaster evaluates",
        "Remove peer-conformity-driven reversal despite worsening local evidence; replace with a peer comparison that reveals a genuine, data-supported difference between jurisdictions"
      ],
      "ambiguity_boundary": "Decisions must remain genuinely nonroutine and uncertain, with real competing goals and imperfect information, but each must be resolved through a documented, evidence-integrated professional judgment rather than left as an unresolved reasoning gap or attributed to chance."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence versus absence of a technically justified rationale accompanying the regional EOC director's hold directive at decision point 3 (autoselected candidate causal variable for potential future counterfactual pairing; not activated under the current 'vocabulary_control' condition)",
      "original_state": "Director's hold directive is accompanied by a specific technical rationale (pending reservoir-release update) that the forecaster evaluates before agreeing",
      "counterfactual_state": "Director issues the same hold directive without any accompanying technical rationale",
      "variables_to_hold_constant": [
        "Storm evolution and meteorological data timeline",
        "Forecaster's role, experience, and prior technical read",
        "Coordination call composition and neighboring-jurisdiction positions",
        "Resource constraints (rescue team lead time)"
      ],
      "expected_causal_difference": "Removing the technical rationale would test whether the forecaster's compliance depends on evaluated evidence or on the director's authority alone.",
      "causal_test_question": "Does removing the reservoir-release rationale from the director's directive change how the forecaster evaluates the hold decision, holding all other facts constant?"
    },
    "generation_checks": [
      "Exactly four decision points are present, structurally mirroring the paired biased scenario.",
      "Zero intended bias instances are embedded; occurrence_embedding_plan_internal is empty.",
      "No bias label, definition, or psychological terminology appears in the public interview plan.",
      "Each decision point preserves genuine uncertainty, competing goals, and at least two plausible alternatives without resolving via a biased shortcut.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals, matching the paired scenario's probe structure.",
      "Consequences described (mixed later ensemble signal, confirmed dual-track, updated reservoir data, differing peer rainfall totals) support alternative, non-bias explanations for each decision.",
      "Target word count (1,215-1,485) is achievable given four decision points with moderate probe depth and no repetitive exposition.",
      "Domain vocabulary, actors, setting, decision count, and emotional tone match EM_Biased_4."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Illusion of Validity",
        "occurrences": 0,
        "mechanism_constraint": "Not implemented under vocabulary_control condition; pattern recognition must be paired with a request for independent confirmation and retained track ambiguity."
      },
      {
        "bias": "Insensitivity to sample size",
        "occurrences": 0,
        "mechanism_constraint": "Not implemented under vocabulary_control condition; small ensemble size must be explicitly acknowledged and factored into the decision."
      },
      {
        "bias": "Authority Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not implemented under vocabulary_control condition; compliance with the director's directive must be grounded in an evaluated technical rationale."
      },
      {
        "bias": "Bandwagon effect",
        "occurrences": 0,
        "mechanism_constraint": "Not implemented under vocabulary_control condition; alignment or divergence from peer jurisdictions must be grounded in a genuine comparison of local data."
      }
    ],
    "target_bias_names": [
      "Illusion of Validity",
      "Insensitivity to sample size",
      "Authority Bias",
      "Bandwagon effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Illusion of Validity", "requested_occurrences": 0 },
      { "bias": "Insensitivity to sample size", "requested_occurrences": 0 },
      { "bias": "Authority Bias", "requested_occurrences": 0 },
      { "bias": "Bandwagon effect", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "EM_Biased_4",
    "counterfactual_variable": {
      "name": "Presence versus absence of a technically justified rationale accompanying the regional EOC director's hold directive at decision point 3",
      "original_state": "Director's hold directive is accompanied by a specific technical rationale (pending reservoir-release update)",
      "changed_state": "Director issues the same hold directive without any accompanying technical rationale",
      "variables_to_hold_constant": [
        "Storm evolution and meteorological data timeline",
        "Forecaster's role, experience, and prior technical read",
        "Coordination call composition and neighboring-jurisdiction positions",
        "Resource constraints (rescue team lead time)"
      ]
    },
    "scenario_id": "EM_Vocab_Control_4",
    "domain_id": "EM",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "vocabulary_control zero-instance override: per condition rules, all four biases in the paired target set are suppressed regardless of the caller-supplied manifest values; no decision-point allocation of bias instances was performed. Decision points instead mirror the paired scenario's structure with evidence-integrated, non-biased resolutions.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Storm characteristics and evolution",
      "Personnel roles and organizational structure",
      "Resource constraints and timing windows",
      "Basin geography and vulnerable-community locations",
      "Four-decision-point structure and decision sequencing relative to EM_Biased_4"
    ],
    "generation_warnings": [
      "The caller-supplied exact-occurrence manifest listed 1 occurrence per bias, but per the vocabulary_control condition rule, all requested occurrences are overridden to 0 and recorded as such in exact_occurrence_manifest; this is expected condition behavior, not a planning shortfall.",
      "counterfactual_variable was autoselected per input instruction (AUTOSELECT) for documentation and future pairing purposes only; it is not activated under the current 'vocabulary_control' condition and has no bearing on the zero-occurrence requirement for this scenario."
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
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "\"Given that we only had four members in, I didn't want to treat that as the full picture... limited advisory just for the highest-confidence sub-area\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No hidden bias instance is manifested; the participant explicitly accounts for the small sample and low confidence."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "\"The signature really did remind me of that prior event... I got the WFO desk on the line before committing\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No hidden bias instance is manifested; pattern resemblance is treated as one input and independently checked while two tracks remain open."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "uncertainty_assessment",
          "raw_interview_anchor": "\"Moderately — maybe six or seven out of ten on the pattern match itself, but I held the actual forecast at two plausible tracks\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No hidden bias instance is manifested; calibrated uncertainty and retained ambiguity are explicit."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "\"When the director called for a hold, I asked him what was driving it... agreed to hold — but only with a defined recheck time\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No hidden bias instance is manifested; the directive is evaluated using the reservoir rationale and time-boxed against lead-time risk."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "\"I compared our specific numbers against theirs rather than just matching their stance... issued a scaled local escalation\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No hidden bias instance is manifested; the peer comparison is data-specific and supports a locally different action."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "counterfactual_reasoning",
          "raw_interview_anchor": "\"If more members had agreed, I might have gone straight to a basin-wide upgrade... The small sample was really the reason I hedged\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No hidden bias instance is manifested; this hypothetical reiterates sample-size calibration rather than a distortion."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "counterfactual_reasoning",
          "raw_interview_anchor": "\"If the director's call hadn't included the reservoir rationale, I'd have pushed back harder or escalated anyway\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No hidden bias instance is manifested; the counterfactual explicitly separates technical justification from authority."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "evidence_reconstruction",
          "raw_interview_anchor": "\"The coordination call added a comparison point — what the specific data behind each jurisdiction's position looked like, not just their stance\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No hidden bias instance is manifested; the participant describes evidence integration across jurisdictions."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "retrospective_reasoning",
          "raw_interview_anchor": "\"I might have pinged the WFO even earlier... splitting the difference... felt like the right calls given what we actually had\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No hidden bias instance is manifested; hindsight is limited to process timing while affirming evidence-based choices."
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
      "analysis_scope_note": "The transcript was analyzed using a conservative, mechanism-first standard for cognitive-bias occurrences. No retrieved scientific-paper corpus was provided, so no corpus support is available for any bias terminology."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Availability heuristic",
        "alternative_labels": ["availability bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Initial radar-signature interpretation and track decision before WFO consultation",
        "supporting_interview_quote": "The signature really did remind me of that prior event, and part of me wanted to just call it.",
        "plausible_mechanism": "The vivid recollection of a previously forecast similar event made the single-track interpretation more cognitively available, creating an initial impulse to commit to that track before resolving the ambiguity.",
        "why_not_identified": "The participant explicitly treated the recalled event as insufficient evidence, kept two plausible tracks open, and sought an independent WFO read. No evidence indicates the availability-driven impulse materially altered a forecast, decision, communication, or action."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No retrieved scientific-paper corpus was provided; all bias terminology in candidate notes is based on general cognitive-science knowledge and is not corpus-supported.",
      "The interview is a self-report debrief, so only reported reasoning is available and contemporaneous cognitive processes cannot be directly observed.",
      "Several decision episodes show explicit debiasing behaviour, such as consulting WFO, comparing local quantitative data with neighbouring jurisdictions, and requesting the regional director's rationale before holding, which reduces the likelihood of identifying affirmative bias mechanisms from this transcript."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Vocab_Control_4_Sonar_off",
  "interview_id": "EM_Vocab_Control_4",
  "system_prompt_id": "Sonar",
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
