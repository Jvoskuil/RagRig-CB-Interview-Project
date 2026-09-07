You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EM_Vocab_Control_4",
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
