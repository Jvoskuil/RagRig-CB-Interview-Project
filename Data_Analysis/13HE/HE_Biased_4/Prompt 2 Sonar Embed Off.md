You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
**Interviewer:** Thanks for making time this week. Just to confirm, this is a voluntary conversation about your recent work verifying the fire engineering package on the tower project—I'll be asking about a specific sequence of decisions, and there's no need to reference anything confidential like commercial terms. That work for you?

**Participant:** Sure, that's fine. I led the performance-based design verification on the 42-story mixed-use tower—office floors, residential above, and an assembly space at podium level. My job was to close out the fire strategy sign-off before the developer's occupancy certificate deadline.

**Interviewer:** Can you give me a general account of what happened in that final stretch?

**Participant:** It was a compressed week. We had four things converging: a late glazing substitution from the contractor, a smoke-control model that came back borderline, a punch list that wasn't fully closed, and a final egress run we needed clean before submission. Normally these would be spaced out, but the contract had liquidated damages tied to the occupancy date, so everything landed at once. The contractor proposed swapping the specified glazing for a cheaper product from another supplier—call them Vendor B—because the original product had a lead-time problem. Around the same time, our CFD smoke model for the atrium showed a visibility result at the escape stair door that was right at the edge of the tenability threshold. Then, with about two inspection days left, our QA reviewer flagged some open punch-list items across cladding fire-stopping, stair pressurization, and signage. And finally, we had to finalize the egress modeling parameters before submitting to building control.

**Interviewer:** Let's reconstruct that in order. What came first?

**Participant:** The glazing issue surfaced first, maybe ten days out. Vendor B sent their technical bulletin, and their rep followed up by email restating the same fire resistance figure, and then I found the same number again in their product brochure. The CFD result came in a few days later, right when we were prepping for fan commissioning. The punch-list conversation happened after that, once the QA reviewer did a walk-through. The egress modeling was the last piece, done in the final two days before submission.

**Interviewer:** Let's take the glazing decision first. What did you have in front of you?

**Participant:** The original spec had a UL-tested 90-minute integrity rating, properly documented. Vendor B's material said their product also achieved "90 minutes, independently verified." I saw that phrase in their bulletin, then again in the cover email, then again in their brochure.

**Interviewer:** What made you comfortable with that?

**Participant:** Honestly, seeing it stated the same way three times across three different documents gave me a level of confidence I probably wouldn't have had from just one. It felt corroborated—like it wasn't just marketing spin, because the same number kept showing up consistently.

**Interviewer:** Did you look at whether those three statements were drawing on the same underlying test?

**Participant:** Not at that stage, no. It didn't occur to me to check whether the bulletin, the email, and the brochure were all citing the same lab report versus separate testing. Building control asked for the raw report later, and that's when we found the mounting configuration in the original test didn't match our as-installed detail, which meant we needed a compatibility assessment. At the time, though, I provisionally accepted the substitution on the basis that it was consistently documented.

**Interviewer:** Moving to the CFD result—what were the options there?

**Participant:** The model showed visibility at the stair door getting close to the threshold around the six-minute mark. Our QA reviewer recommended re-running it with a revised HVAC shutdown sequence, which would've added about five working days. We had four days to the deadline. Fan commissioning was next on the critical path.

**Interviewer:** What did you decide, and why?

**Participant:** I authorized the commissioning to proceed. We were losing days, and holding the whole phase for a re-run felt like it would stall the entire program right when we needed to keep moving. I treated the re-run as something that could happen in parallel rather than as a gate before the next milestone.

**Interviewer:** Was there a technical basis for treating it as non-blocking, or was it mainly about the schedule?

**Participant:** If I'm honest, it was mostly about not wanting the project to stand still. The commissioning itself wasn't destructive, so proceeding felt like the safer, more productive choice compared to just waiting around for numbers we already suspected might come back tight. The re-run did eventually show the margin was narrower under a slightly different shutdown assumption, but by then commissioning had already passed its initial functional tests.

**Interviewer:** Let's talk about the punch-list reprioritization. What was on the list at that point?

**Participant:** Cladding fire-stopping, a pressurization deficiency on one of the lift-shaft fan doors, and some egress signage items. Two inspection days left.

**Interviewer:** How did you decide where to spend those two days?

**Participant:** There'd been that apartment-tower fire overseas about two weeks earlier—cladding-related, and the footage was everywhere. It stuck with me. Even though our cladding and compartmentation system is different and already well-documented, I put the remaining time into re-inspecting the cladding fire-stopping.

**Interviewer:** What about the pressurization fan-door deficiency?

**Participant:** It got pushed down the list. It had already been logged, so it felt like something we understood and could revisit later. The cladding felt like the one I needed to be extra sure about after watching that. In hindsight, a follow-up visit found the fan-door issue was more significant than we'd initially logged, and the cladding re-inspection didn't turn up anything new.

**Interviewer:** Did you use the standard risk matrix to rank those items?

**Participant:** Not formally at that point. It was more of a judgment call based on what felt most urgent to check again.

**Interviewer:** Last decision point—the egress modeling parameters.

**Participant:** Right, this was in the final two days. The software's default library has pre-movement times and flow rates calibrated for generic office occupancy. Our building's mixed-use—office, residential, assembly—so the population isn't quite the same. A colleague flagged that we actually had project-specific pre-movement survey data, plus some comparable mixed-use studies, that could refine those numbers.

**Interviewer:** Did you use that data?

**Participant:** We didn't, in the end. Recalibrating with the survey data would've meant extra runs and QA time we didn't have. The defaults are the standard starting point in that software, so I kept them for the final compliance run. I flagged in my notes that the calibration population wasn't a perfect match, but the run passed the required threshold, so we submitted it as is.

**Interviewer:** If recalibrating had taken less effort, would you have used the survey data instead?

**Participant:** Probably, yes. It wasn't that I thought the defaults were more accurate—it was more that changing them under that timeline felt like an unnecessary complication.

**Interviewer:** Looking back across all four decisions, what would have changed your approach on the glazing, if anything?

**Participant:** If the 90-minute claim had come from one document instead of three, I think I'd have pushed harder for the raw report before accepting it. Something about seeing it repeated made it feel more settled than it actually was.

**Interviewer:** And if there'd been no deadline pressure at all that week?

**Participant:** The CFD re-run probably would've been a hard hold point rather than something running in parallel. Without the schedule squeeze, I don't think I'd have authorized commissioning ahead of it.

**Interviewer:** Last one—if that overseas fire hadn't been in the news right before your punch-list decision, do you think the priority would have looked different?

**Participant:** Possibly. I'd like to think I'd have gone with the risk matrix from the start. But I can't fully separate how much of that reallocation was the news versus genuine caution.

**Interviewer:** That's a helpful place to stop. Thanks for walking through it in this much detail.

**Participant:** No problem. It's useful to go back over it, honestly.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HE_Biased_4",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Structural Fire Engineer (Performance-Based Design)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Atrium Tower Occupancy Signoff Under Schedule Pressure",
    "scenario_summary_internal": "A structural fire engineer leading performance-based design (PBD) verification for a 42-story mixed-use tower must close out four remaining compliance items before the developer's occupancy certificate deadline: a late substitute-glazing test report, a borderline smoke-control CFD result requiring re-modeling, a QA punch-list reprioritization occurring two weeks after a widely publicized high-rise fire elsewhere, and a final egress-modeling run using software default occupant parameters. Each decision is made under time and commercial pressure, with plausible technical justifications available at every step.",
    "occupational_realism": {
      "objective": "Complete and sign off the fire engineering verification package (glazing fire resistance, smoke control performance, compartmentation QA, egress modeling) so the developer can obtain the occupancy certificate on schedule.",
      "setting": "Fire engineering consultancy office and construction site of a 42-story mixed-use (office/residential/assembly) tower in final commissioning phase, four days before a contractual occupancy deadline.",
      "constraints": [
        "Hard occupancy certificate deadline set by developer contract with liquidated-damages exposure",
        "Independent QA reviewer flags open items requiring further verification",
        "Limited remaining site-access days for punch-list inspections",
        "Substitute glazing product proposed late by contractor for cost/lead-time reasons",
        "Modeling software licensed with generic default occupant-behavior libraries not calibrated to this occupancy mix"
      ],
      "stakeholders": [
        "Lead structural fire engineer (interviewee)",
        "Independent QA/peer reviewer",
        "Developer's project director",
        "General contractor",
        "Glazing subcontractor and Vendor B (substitute glazing supplier)",
        "Building control/approving authority"
      ],
      "technical_terms_to_use": [
        "performance-based design (PBD)",
        "fire resistance rating",
        "integrity and insulation criteria",
        "CFD smoke modeling",
        "tenability criteria / visibility threshold",
        "compartmentation",
        "cladding fire-stopping",
        "stair pressurization",
        "pre-movement time",
        "egress/evacuation modeling",
        "punch list",
        "commissioning"
      ],
      "technical_terms_to_avoid": [
        "illusion of truth",
        "action bias",
        "affect bias",
        "default bias",
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Original glazing spec was approved with a UL/EN test report showing 90-minute integrity rating",
          "Contractor proposes a substitute product from Vendor B for cost and lead-time reasons",
          "Vendor B's technical bulletin, cover email, and marketing brochure each state '90 minutes, independently verified' fire resistance",
          "The underlying test referenced in all three documents used a different mounting/frame configuration than the project's installation detail"
        ],
        "new_information_after_decision": [
          "Building control later requests the raw test report and mounting schedule for the substitute product",
          "The raw report shows the mounting configuration differs from the as-installed detail, requiring a compatibility assessment"
        ],
        "alternatives": [
          "Request the raw underlying test report and mounting schedule before accepting the substitution",
          "Commission an independent verification test or engineering judgment memo for the as-installed configuration",
          "Provisionally accept the substitution based on the consistency of the vendor's repeated claims"
        ],
        "intended_action": "Engineer provisionally accepts the substitute glazing, citing that the 90-minute rating appears 'consistently documented across multiple vendor sources.'"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary smoke-control CFD model shows borderline visibility at the escape-stair door at approximately six minutes",
          "Independent QA review recommends re-running the model with a revised HVAC shutdown sequence, adding five working days",
          "Occupancy certificate deadline is four days away",
          "Fan commissioning is the next scheduled construction milestone and is on the critical path"
        ],
        "new_information_after_decision": [
          "Fan commissioning proceeds and passes initial functional tests",
          "The revised CFD re-run, completed later than planned, shows the visibility margin was narrower than assumed under a different plausible shutdown sequence"
        ],
        "alternatives": [
          "Pause the commissioning phase and wait for the revised CFD re-run before proceeding",
          "Authorize fan commissioning to proceed now while treating the re-run as a parallel, non-blocking check",
          "Implement an interim mechanical mitigation and hold the next milestone pending re-run results"
        ],
        "intended_action": "Engineer authorizes fan commissioning to proceed immediately 'to keep the program moving,' without making the re-run result a hold point for the next milestone."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A widely reported apartment-tower fire in another country, involving dramatic cladding-fire footage, occurred two weeks earlier",
          "This building uses a different cladding and compartmentation system with adequate prior documentation",
          "Remaining QA punch list includes open items across cladding fire-stopping, lift-shaft pressurization (unresolved fan-door deficiency), and egress signage",
          "Only two inspection days remain before signoff"
        ],
        "new_information_after_decision": [
          "The pressurization fan-door deficiency is later found during a follow-up visit to be more significant than initially logged",
          "The cladding re-inspection finds no new deficiencies beyond what was already documented"
        ],
        "alternatives": [
          "Rank the remaining punch-list items using the project's standard risk/probability matrix",
          "Reallocate the final two inspection days toward cladding-related items ahead of the pressurization deficiency",
          "Split the remaining time evenly across all three open item categories"
        ],
        "intended_action": "Engineer reallocates the final two inspection days to re-inspect cladding fire-stopping, deprioritizing the pressurization fan-door deficiency."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Egress-modeling software ships with default pre-movement time and flow-rate parameters calibrated for a generic office occupancy",
          "This building has a mixed-use occupancy (office, residential, assembly) with a different demographic and behavioral profile",
          "A colleague flags that project-specific pre-movement survey data and comparable mixed-use building studies are available",
          "Substituting project-specific values requires additional recalibration effort before the deadline"
        ],
        "new_information_after_decision": [
          "The compliance run using default parameters passes the required egress time threshold with limited margin",
          "A later audit note observes the default library's behavioral assumptions were developed for a different occupancy type"
        ],
        "alternatives": [
          "Substitute the project-specific survey-based pre-movement values into the model",
          "Blend the default values with a partial adjustment based on the available survey data",
          "Retain the software's default parameters for the final compliance run with a documented justification"
        ],
        "intended_action": "Engineer retains the software's default pre-movement and flow parameters for the final compliance run rather than substituting the available project-specific data."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role in signing off this tower's fire engineering package?",
        "What was the overall objective in the final week before the occupancy deadline?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what triggered the glazing substitution request?",
        "Walk me through the sequence of events between the CFD result and the fan commissioning decision.",
        "How did the punch-list reprioritization unfold over those final two days?",
        "When did the egress-modeling parameter question come up relative to the other decisions?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you when you decided to accept the substitute glazing?",
        "What made the vendor's documentation convincing at that point?",
        "What alternatives did you consider before authorizing fan commissioning to proceed?",
        "How did you weigh the five-day delay against the borderline CFD result?",
        "What led you to prioritize the cladding re-inspection over the pressurization deficiency?",
        "How did the recent tower fire in the news factor into that prioritization, if at all?",
        "Why did you keep the software's default pre-movement parameters for the final run?",
        "Was the project-specific survey data considered, and if so, how?"
      ],
      "closing_hypotheticals": [
        "If the vendor documentation had come from a single source instead of three, would you have handled it differently?",
        "If there had been no deadline pressure, would the CFD re-run have been a hold point?",
        "If the fire in the news had not occurred, would the punch-list priority have been different?",
        "If recalibrating the egress model had taken less effort, would you have used the survey data?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "he4_iot_01",
        "bias": "Illusion of Truth effect",
        "decision_point": 1,
        "mechanism": "Repeated exposure to the same '90-minute, independently verified' claim across three separate vendor documents (spec sheet, email, brochure) increases the engineer's subjective sense of its credibility, even though all three repetitions trace back to a single underlying test with a differing mounting configuration.",
        "affected_reasoning_operation": "Evaluation of source credibility / evidence weighting for a technical claim",
        "evidence_available_at_time": [
          "Three vendor documents repeating an identical fire-resistance claim",
          "No independent second test or raw report yet obtained",
          "A mounting-configuration discrepancy that is discoverable but not yet checked"
        ],
        "required_textual_manifestation": "The interviewee should explicitly attribute their increased confidence to the claim being 'documented consistently' or 'repeated across multiple sources,' rather than to independent verification, and should not mention checking whether the sources shared a common underlying test.",
        "plausible_nonbias_interpretation": "A reasonable engineer might treat multiple corroborating vendor documents as a legitimate (if incomplete) form of triangulation under time pressure, without this reflecting a truth-illusion effect.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "illusion of truth",
          "repetition effect",
          "familiarity breeds belief"
        ]
      },
      {
        "instance_id": "he4_ab_01",
        "bias": "Action bias",
        "decision_point": 2,
        "mechanism": "Faced with a borderline, uncertain CFD result and a recommended pause, the engineer favors authorizing an active step (proceeding with fan commissioning) over the passive/waiting alternative, framing forward motion itself as risk-reducing regardless of the analytic case for waiting.",
        "affected_reasoning_operation": "Choice between action and inaction under time pressure and uncertainty",
        "evidence_available_at_time": [
          "Borderline visibility margin in preliminary CFD results",
          "A specific QA recommendation to re-run the model before the next milestone",
          "A four-day deadline creating pressure to keep the schedule moving"
        ],
        "required_textual_manifestation": "The interviewee should justify authorizing commissioning primarily in terms of 'needing to do something' or 'keeping momentum,' rather than through a risk-based justification for why proceeding without the re-run was analytically sound.",
        "plausible_nonbias_interpretation": "Proceeding with a non-destructive commissioning step in parallel with a re-run could be a legitimate schedule-risk management strategy, not necessarily a bias.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "action bias",
          "bias toward action",
          "omission versus commission"
        ]
      },
      {
        "instance_id": "he4_afb_01",
        "bias": "Affect Bias",
        "decision_point": 3,
        "mechanism": "The emotionally vivid recent cladding-fire disaster elsewhere increases the perceived risk salience of cladding fire-stopping on this project, causing the engineer to reallocate scarce inspection time toward the emotionally resonant system rather than toward the item with an already-documented, arguably more severe technical deficiency (the pressurization fan-door issue).",
        "affected_reasoning_operation": "Risk prioritization / resource allocation across competing open QA items",
        "evidence_available_at_time": [
          "News coverage of an unrelated but emotionally striking high-rise fire two weeks prior",
          "An already-logged, unresolved pressurization fan-door deficiency",
          "No updated technical data suggesting this building's cladding risk had actually increased"
        ],
        "required_textual_manifestation": "The interviewee's explanation for reprioritizing toward cladding should reference the emotional impact or vividness of the recent fire (e.g., feeling it was 'too close for comfort' or wanting to be 'extra sure' after seeing it), rather than new technical evidence about this building's cladding.",
        "plausible_nonbias_interpretation": "Increased public and regulatory scrutiny of cladding after a major incident could be a legitimate, defensible reason to revisit cladding documentation, independent of any emotional reaction.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "affect bias",
          "emotional salience",
          "availability from vivid recent event"
        ]
      },
      {
        "instance_id": "he4_db_01",
        "bias": "Default bias",
        "decision_point": 4,
        "mechanism": "The engineer retains the modeling software's pre-set occupant-behavior parameters for the final compliance run rather than substituting available project-specific data, favoring the path requiring no active change over an equally or more available alternative.",
        "affected_reasoning_operation": "Selection of model input parameters / choice between status-quo default and available alternative data",
        "evidence_available_at_time": [
          "Software default pre-movement and flow-rate parameters calibrated for generic office occupancy",
          "Availability of project-specific survey data and comparable mixed-use building studies, flagged by a colleague",
          "Awareness that this building's occupancy mix differs from the office-calibrated default"
        ],
        "required_textual_manifestation": "The interviewee should explain keeping the default values in terms of it being the standard/pre-set path or requiring less effort to change, while acknowledging the mismatch between the default's calibration population and the actual occupancy mix, without providing a substantive technical justification for why the default was actually more appropriate.",
        "plausible_nonbias_interpretation": "If the software vendor's default had been independently validated for mixed-use buildings, retaining it could be a legitimate, evidence-based choice rather than a default bias.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "default bias",
          "status quo",
          "path of least resistance"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition and no paired control scenario ID was supplied."
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
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Exactly one intended bias instance is embedded per decision point, matching the manifest total of four.",
      "No bias name, definition, or psychological label appears in the planned public interview text.",
      "Each occurrence has a distinct evidence trace, decision point, and plausible non-bias interpretation.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Planned content supports a 1,215-1,485 word interview without repetitive exposition.",
      "Consequences described do not mechanically prove or disprove bias presence."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Illusion of Truth effect",
        "occurrences": 1,
        "mechanism_constraint": "Repetition of an identical unverified claim across multiple documents from a single underlying source, mistaken for independent corroboration."
      },
      {
        "bias": "Action bias",
        "occurrences": 1,
        "mechanism_constraint": "Preference for proceeding with an active step over pausing/waiting, justified primarily by the value of acting rather than by risk analysis."
      },
      {
        "bias": "Affect Bias",
        "occurrences": 1,
        "mechanism_constraint": "Risk prioritization driven by emotional reaction to a vivid, unrelated recent event rather than new technical evidence."
      },
      {
        "bias": "Default bias",
        "occurrences": 1,
        "mechanism_constraint": "Retention of pre-set software parameters over an available, more representative alternative, justified by effort/status-quo rather than technical superiority."
      }
    ],
    "target_bias_names": [
      "Illusion of Truth effect",
      "Action bias",
      "Affect Bias",
      "Default bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Illusion of Truth effect", "requested_occurrences": 1 },
      { "bias": "Action bias", "requested_occurrences": 1 },
      { "bias": "Affect Bias", "requested_occurrences": 1 },
      { "bias": "Default bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "he4_iot_01", "bias": "Illusion of Truth effect" },
      { "instance_id": "he4_ab_01", "bias": "Action bias" },
      { "instance_id": "he4_afb_01", "bias": "Affect Bias" },
      { "instance_id": "he4_db_01", "bias": "Default bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "he4_iot_01", "bias": "Illusion of Truth effect", "decision_point": 1 },
      { "instance_id": "he4_ab_01", "bias": "Action bias", "decision_point": 2 },
      { "instance_id": "he4_afb_01", "bias": "Affect Bias", "decision_point": 3 },
      { "instance_id": "he4_db_01", "bias": "Default bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "he4_iot_01",
        "bias": "Illusion of Truth effect",
        "mechanism": "Repeated exposure to the same claim across three vendor documents traced to one underlying test increases perceived credibility without independent verification.",
        "affected_reasoning_operation": "Evaluation of source credibility / evidence weighting",
        "evidence_source": "Vendor B's spec sheet, cover email, and marketing brochure, all citing the same '90-minute, independently verified' claim",
        "distinctiveness_requirement": "Must be tied to decision point 1's glazing substitution evaluation only; not restated in later decision points."
      },
      {
        "instance_id": "he4_ab_01",
        "bias": "Action bias",
        "mechanism": "Preference for authorizing an active commissioning step over waiting for a recommended re-run, justified by the value of maintaining momentum rather than analysis of the borderline CFD result.",
        "affected_reasoning_operation": "Action-versus-inaction choice under schedule pressure and uncertainty",
        "evidence_source": "Preliminary CFD visibility result and QA's re-run recommendation at decision point 2",
        "distinctiveness_requirement": "Must be tied to the fan-commissioning authorization only; not conflated with the cladding-reprioritization decision in point 3."
      },
      {
        "instance_id": "he4_afb_01",
        "bias": "Affect Bias",
        "mechanism": "Emotional salience of a vivid, unrelated recent high-rise fire shifts inspection-time allocation toward the emotionally resonant cladding system over the technically more urgent pressurization deficiency.",
        "affected_reasoning_operation": "Risk-based prioritization of remaining QA punch-list items",
        "evidence_source": "News coverage of the unrelated fire and the pre-existing pressurization fan-door deficiency log at decision point 3",
        "distinctiveness_requirement": "Must be tied to punch-list reallocation only; must not be justified by new technical cladding evidence."
      },
      {
        "instance_id": "he4_db_01",
        "bias": "Default bias",
        "mechanism": "Retention of software's generic-office default occupant parameters over available project-specific survey data, justified by effort/status-quo rather than technical fit.",
        "affected_reasoning_operation": "Selection of model input parameters for the final egress compliance run",
        "evidence_source": "Software default library and colleague's flagged project-specific survey/comparable-building data at decision point 4",
        "distinctiveness_requirement": "Must be tied to the final egress-modeling run only; must not reuse action-bias or illusion-of-truth reasoning."
      }
    ],
    "intended_strength": [
      { "instance_id": "he4_iot_01", "bias": "Illusion of Truth effect", "strength": "moderate" },
      { "instance_id": "he4_ab_01", "bias": "Action bias", "strength": "moderate" },
      { "instance_id": "he4_afb_01", "bias": "Affect Bias", "strength": "moderate" },
      { "instance_id": "he4_db_01", "bias": "Default bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HE_Biased_4",
    "domain_id": "HE",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias assigned to a distinct decision point (1:1 mapping across the four decision points), selected for mechanism fit and narrative realism: illusion of truth at the documentary-evidence evaluation (point 1), action bias at the schedule-pressure go/no-go choice (point 2), affect bias at the risk-prioritization choice following a vivid external event (point 3), and default bias at the modeling-parameter selection (point 4). No bias shares a decision point, so no additional evidence-source separation was required.",
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
          "segment_id": "seg_001",
          "speaker": "Participant",
          "segment_type": "schedule_context_reasoning",
          "raw_interview_anchor": "It was a compressed week. We had four things converging... the contract had liquidated damages tied to the occupancy date, so everything landed at once.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Substantive explanation of schedule convergence and commercial pressure, but no hidden bias mechanism is manifested in this span."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "evidence_weighting_decision",
          "raw_interview_anchor": "Honestly, seeing it stated the same way three times across three different documents gave me a level of confidence... It felt corroborated...",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["he4_iot_01"],
          "ground_truth_rationale": "The participant attributes increased credibility to repeated identical claims and does not check whether the documents share one underlying test."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "action_inaction_decision",
          "raw_interview_anchor": "I authorized the commissioning to proceed... holding the whole phase for a re-run felt like it would stall the entire program... I treated the re-run as something that could happen in parallel rather than as a gate.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["he4_ab_01"],
          "ground_truth_rationale": "The active commissioning step is preferred over waiting for a recommended safety re-run primarily to maintain momentum under uncertainty and deadline pressure."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "risk_prioritization_decision",
          "raw_interview_anchor": "There'd been that apartment-tower fire overseas about two weeks earlier... It stuck with me... I put the remaining time into re-inspecting the cladding fire-stopping.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["he4_afb_01"],
          "ground_truth_rationale": "A vivid unrelated recent fire drives the cladding priority despite a different, documented system and an unresolved pressurization deficiency."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "default_parameter_selection",
          "raw_interview_anchor": "We didn't, in the end... The defaults are the standard starting point in that software, so I kept them for the final compliance run.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["he4_db_01"],
          "ground_truth_rationale": "The participant retains generic defaults over available project-specific data, acknowledging the mismatch and citing effort and complication rather than technical superiority."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "counterfactual_prediction",
          "raw_interview_anchor": "If the 90-minute claim had come from one document instead of three, I think I'd have pushed harder for the raw report before accepting it.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A retrospective counterfactual about the glazing decision supports the earlier occurrence but is not a separate hidden occurrence."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "counterfactual_prediction",
          "raw_interview_anchor": "The CFD re-run probably would've been a hard hold point rather than something running in parallel. Without the schedule squeeze, I don't think I'd have authorized commissioning ahead of it.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A counterfactual prediction about schedule pressure is evidence about the prior decision, not a separate manifested bias instance."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "counterfactual_prediction",
          "raw_interview_anchor": "If that overseas fire hadn't been in the news right before my punch-list decision, do you think the priority would have looked different? Possibly...",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A qualified counterfactual about the news event is supporting reflection on the punch-list decision, not a new hidden occurrence."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "counterfactual_prediction",
          "raw_interview_anchor": "If recalibrating the egress model had taken less effort, would you have used the survey data? Probably, yes...",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A counterfactual about effort and the egress parameters supports the prior decision but does not add another hidden occurrence."
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
    "analysis_scope_note": "The analysis covers four reasoning episodes described by the participant: glazing substitution acceptance, smoke-model commissioning decision, punch-list reprioritization, and egress model parameter selection. No retrieved corpus passages were supplied, so bias labels and mechanisms are drawn from general cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "illusory truth effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "illusory truth effect",
      "alternative_labels": ["repetition-induced truth effect", "truth effect", "frequency validity effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for repeated exposure to a statement to increase its perceived truth or credibility, independent of whether the repetition provides independent corroboration.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Provisional acceptance of Vendor B glazing substitution",
      "decision_point_description": "Whether to accept Vendor B's 90-minute fire-resistance claim for glazing substitution based on supplier documentation before obtaining the raw test report.",
      "affected_reasoning_operation": "Evaluation of technical documentation credibility and decision to provisionally accept the substitution",
      "bias_specific_mechanism": "Repeated exposure to the same claim across three documents (bulletin, email, brochure) produced a sense of corroboration and increased confidence, without checking whether the sources were truly independent or drew on the same underlying test.",
      "manifestation_in_interview": "The participant states that seeing '90 minutes, independently verified' repeated three times gave confidence that it was not marketing spin, and that one source would not have produced the same confidence. He did not check whether the documents cited the same underlying lab report.",
      "effect_on_reasoning_or_decision": "He provisionally accepted the substitution as consistently documented; later, building control requested the raw report and found the mounting configuration in the original test did not match the as-installed detail, requiring a compatibility assessment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Vendor B's material said their product also achieved '90 minutes, independently verified.' I saw that phrase in their bulletin, then again in the cover email, then again in their brochure.",
          "evidence_explanation": "Identifies the repeated identical claim across three documents."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, seeing it stated the same way three times across three different documents gave me a level of confidence I probably wouldn't have had from just one. It felt corroborated—like it wasn't just marketing spin, because the same number kept showing up consistently.",
          "evidence_explanation": "Directly links repetition to increased credibility and perceived corroboration, the core mechanism of illusory truth."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that stage, no. It didn't occur to me to check whether the bulletin, the email, and the brochure were all citing the same lab report versus separate testing.",
          "evidence_explanation": "Demonstrates that confidence was based on repetition rather than independent source verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At the time, though, I provisionally accepted the substitution on the basis that it was consistently documented.",
          "evidence_explanation": "Shows the reasoning outcome influenced by repeated documentation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the 90-minute claim had come from one document instead of three, I think I'd have pushed harder for the raw report before accepting it.",
          "evidence_explanation": "Confirms that repetition across documents was the differentiating factor in accepting the claim."
        }
      ],
      "correction_or_counterevidence": "Later, building control requested the raw report and a compatibility assessment was needed; this correction occurred after the initial decision and does not negate the repetition-based reasoning at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and mechanism derive from general cognitive-science knowledge about repetition-induced truth.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge risk, urgency, or probability based on how easily examples come to mind; recent, vivid, or emotionally salient events can dominate these judgments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Punch-list reprioritization during final two inspection days",
      "decision_point_description": "How to allocate limited inspection time among cladding fire-stopping, a pressurization fan-door deficiency, and egress signage.",
      "affected_reasoning_operation": "Risk prioritization and allocation of inspection attention",
      "bias_specific_mechanism": "The recent, emotionally salient overseas cladding fire made cladding-related risk disproportionately easy to recall, so the participant treated cladding fire-stopping as the most urgent item despite noting that the building's cladding and compartmentation system was different and already well-documented.",
      "manifestation_in_interview": "He explicitly attributes the prioritization to the fire sticking with him and the footage being everywhere, and he did not use the formal risk matrix.",
      "effect_on_reasoning_or_decision": "He allocated remaining inspection time to cladding fire-stopping, which found nothing new; the pressurization fan-door issue was deprioritized and later found to be more significant than initially logged.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There'd been that apartment-tower fire overseas about two weeks earlier—cladding-related, and the footage was everywhere. It stuck with me. Even though our cladding and compartmentation system is different and already well-documented, I put the remaining time into re-inspecting the cladding fire-stopping.",
          "evidence_explanation": "Shows a salient recent event directly influenced allocation of inspection attention despite known technical differences and existing documentation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The cladding felt like the one I needed to be extra sure about after watching that.",
          "evidence_explanation": "Indicates that the news footage created a strong sense of urgency about cladding specifically."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not formally at that point. It was more of a judgment call based on what felt most urgent to check again.",
          "evidence_explanation": "Suggests mental accessibility and intuitive salience rather than formal risk-ranking drove the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, a follow-up visit found the fan-door issue was more significant than we'd initially logged, and the cladding re-inspection didn't turn up anything new.",
          "evidence_explanation": "Provides outcome context that the salience-driven priority may not have matched actual technical risk, though the bias identification is based on the explicit mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant notes his cladding and compartmentation system was different and already well-documented; this awareness was present but did not override the salience-driven reprioritization. The outcome alone is not used to diagnose the bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and mechanism derive from general cognitive-science knowledge about the availability heuristic.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "status quo bias",
      "alternative_labels": ["default effect", "default bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The preference for the existing or default option, often because changing it seems costly or effortful, even when the default may not be the best fit.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of egress modeling parameters for final compliance run",
      "decision_point_description": "Whether to use project-specific pre-movement survey data and comparable mixed-use studies or retain the software's default values for the final egress modeling run.",
      "affected_reasoning_operation": "Model parameter selection under deadline",
      "bias_specific_mechanism": "The software defaults were treated as the standard starting point; although the participant acknowledged they were not a perfect match and did not think they were more accurate, changing them under the timeline felt like an unnecessary complication, leading to retention of the default option.",
      "manifestation_in_interview": "He declined to recalibrate with available project-specific data, kept the generic defaults, and wrote a note that the population calibration was not perfect.",
      "effect_on_reasoning_or_decision": "The final compliance run used generic office defaults rather than project-specific mixed-use data; it still passed the required threshold, but the submitted model was not calibrated to the project population.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "A colleague flagged that we actually had project-specific pre-movement survey data, plus some comparable mixed-use studies, that could refine those numbers.",
          "evidence_explanation": "Shows that a clearly available alternative to the default existed and was recognized."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We didn't, in the end. Recalibrating with the survey data would've meant extra runs and QA time we didn't have. The defaults are the standard starting point in that software, so I kept them for the final compliance run.",
          "evidence_explanation": "Demonstrates that the default was retained primarily on the basis of it being the standard and less effortful to keep."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It wasn't that I thought the defaults were more accurate—it was more that changing them under that timeline felt like an unnecessary complication.",
          "evidence_explanation": "Directly indicates that the default was preferred despite not being judged more accurate, which is consistent with status quo bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yes. It wasn't that I thought the defaults were more accurate—it was more that changing them under that timeline felt like an unnecessary complication.",
          "evidence_explanation": "Confirms that effort, not technical superiority, drove the choice."
        }
      ],
      "correction_or_counterevidence": "There were genuine time and resource constraints, and the participant flagged the calibration mismatch in his notes. The run also passed the required threshold. These factors are consistent with a practical decision under pressure, but the explicit statement that the default was not more accurate and that lower effort would have changed the choice supports status quo bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and mechanism derive from general cognitive-science knowledge about status quo bias and default effects.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "action bias",
      "alternative_labels": ["bias for action", "commission bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision to authorize fan commissioning before smoke-model re-run",
      "supporting_interview_quote": "If I'm honest, it was mostly about not wanting the project to stand still. The commissioning itself wasn't destructive, so proceeding felt like the safer, more productive choice compared to just waiting around for numbers we already suspected might come back tight.",
      "plausible_mechanism": "A preference for taking action over waiting under unresolved uncertainty and schedule pressure, with the action being treated as safer and more productive primarily because waiting felt like an unacceptable stall.",
      "why_not_identified": "The interview also supports a strong non-bias explanation: the commissioning was non-destructive, the re-run could plausibly proceed in parallel, and the decision occurred under a genuine hard deadline. It is not clear that inaction or delay was technically preferable at the time, so the evidence is treated as insufficient for an identified occurrence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific corpus was supplied, so corpus-based support could not be used; labels and mechanisms rely on general cognitive-science knowledge.",
    "The analysis relies on the participant's retrospective self-report, which may include memory or self-presentation effects.",
    "Several decisions occurred under genuine deadline and resource constraints, which are plausible non-bias contributors and were treated as competing explanations.",
    "Action bias is included as a candidate rather than an identified occurrence because the schedule-driven choice also had a legitimate non-bias explanation."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Biased_4_Sonar_off",
  "interview_id": "HE_Biased_4",
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
