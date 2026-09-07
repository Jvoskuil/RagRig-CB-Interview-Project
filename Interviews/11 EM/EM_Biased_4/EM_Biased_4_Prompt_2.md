You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EM_Biased_4",
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
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
