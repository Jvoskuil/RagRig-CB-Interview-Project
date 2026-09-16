You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. This is part of a research review on design decision-making, it's recorded, nothing gets tied to your name, and you can pass on anything you'd rather not get into. Okay?

Participant: Sure, no problem.

Interviewer: Tell me about your role on this project and what it involved.

Participant: I was lead design engineer on a sprinkler retrofit for a distribution warehouse, 140,000 square feet, tilt-up concrete. The owner was bringing in a new third-party logistics tenant who needed part of the floor converted to high-piled rack storage, double-row selective rack up to 32 feet. I had to redesign the existing system, which was sized for a lighter occupancy, get it through plan review, and get it installed before the tenant's lease started.

Interviewer: How did the schedule on this one compare to a typical retrofit?

Participant: Actually pretty comfortable, for once. We had six weeks from kickoff to permit submission, which is more breathing room than I usually get. The existing water supply and riser sizing were still set up for the old, lower-hazard use, so that part of the challenge was still there, but I wasn't fighting the calendar the way I sometimes am.

Interviewer: Walk me through the incident from the start.

Participant: Early on I needed to settle the commodity classification, since that drives the density, the rack sprinkler requirements, everything downstream. I didn't have a finalized SKU or packaging list from the tenant yet, they were still working that out on their end, and the owner wanted the classification locked so he could fix the retrofit budget. There wasn't really a schedule reason it had to happen that week, I could have waited and asked for a sample of their packaging list, but I'd done two other jobs for similar 3PL operators and had a good sense of what that kind of tenant typically stores. I went with Class III based on that pattern and moved on. Then I pulled the NFPA density and area curves for that classification at 32 feet, picked a point that cleared the code minimum, and built the hydraulic calculations. There was still plenty of runway before submission, so I could have run a few more combinations against the actual rack layout, but I didn't loop back to compare. That package went to the owner, who wanted a value-engineering pass since it came in over budget, and we talked about trimming the in-rack sprinkler allowance. Once the system was installed, we got to commissioning, and with the schedule no longer tight, we did the full witnessed flow test without any rush.

Interviewer: Let's reconstruct that in order. What happened first?

Participant: Classification, in the first week or so. Density and area selection maybe two and a half weeks in. Value engineering came after plan review comments, around week four. Commissioning was near the end, but we still had days to spare before move-in.

Interviewer: What did you learn after the classification that you didn't know when you made it?

Participant: A partial inventory list came in later and showed more exposed unexpanded plastics mixed with the cartoned goods than I'd assumed, closer to a plastics classification than straight Class III.

Interviewer: Going back to that first call, what did you actually have in hand, and how much time did you have to get more?

Participant: I had the tenant's general business type and my history with two comparable clients. I didn't have their SKU list, but with six weeks on the clock, I probably had time to ask for a preliminary sample and wait a bit.

Interviewer: Did you consider requesting that data before finalizing?

Participant: I thought about it briefly. But in my experience, this type of tenant runs cartoned retail goods, maybe some mixed packaging, and both of the prior jobs landed at Class III. I went with that pattern instead of waiting on their list.

Interviewer: If you'd had the SKU list before classifying, would you have done anything differently?

Participant: Probably, yeah, if the plastics share had been visible upfront I'd have leaned more conservative from the start.

Interviewer: What would have made you press for that data given you had the time?

Participant: Something specific standing out, like if they'd mentioned electronics or aerosols. Nothing in the early conversations flagged that, so it didn't feel urgent to chase down.

Interviewer: Moving to the density selection. What alternatives were actually available to you?

Participant: Several density and area points would have satisfied code minimum for Class III at that height, some needing more in-rack sprinklers. I could have compared those against the specific rack configuration and aisle widths, or checked the manufacturer's guide for something tailored to the layout.

Interviewer: With several weeks still on the calendar, what determined which one you picked?

Participant: I took the first point that cleared the minimum for the assumed classification and built the calc package around it. I had the time to run more comparisons, honestly, I just didn't loop back once I had something that worked.

Interviewer: Did the plan reviewer comment on that later?

Participant: Yeah, flagged that the point I'd chosen was close to the edge of the applicable curve for the actual rack configuration. Not a rejection, just a note to be aware of.

Interviewer: What went through your mind when the owner asked for value engineering?

Participant: He wanted the number under budget, and the in-rack allowance was the biggest thing I could trim. Keeping it would've given more margin against the classification uncertainty I already knew about. But we've got two more retrofit jobs pending with him, and I didn't want friction over one line item, so I recommended pulling the allowance to hit his number.

Interviewer: Did you walk him through the classification uncertainty as part of that?

Participant: Not in much depth. I mentioned it, but I framed the removal as a reasonable trade rather than spelling out how much margin we'd be giving up.

Interviewer: If there'd been no ongoing relationship with the owner, would that conversation have gone differently?

Participant: Possibly. I'd like to think I'd have pushed harder to keep the allowance, but I can't say for sure.

Interviewer: Last decision point, commissioning. What determined the testing you pursued?

Participant: The AHJ requires the witnessed flow test regardless, and with days to spare before move-in, there wasn't a reason to cut corners. I did the full test.

Interviewer: How did it turn out?

Participant: Passed comfortably, well above the required minimum. No concerns there.

Interviewer: Looking back, given that schedule wasn't really the constraint here, is there a decision you'd make differently?

Participant: The classification, still. Everything downstream followed from that first call, and I had the time to ask for more data before locking it in. I just didn't use it that way.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HE_Counterfactual_3",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Fire Protection System Designer (Sprinkler/Suppression Design Engineer)",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Rack Storage Retrofit: Same Trade-offs Under an Extended Schedule",
    "scenario_summary_internal": "This is the causal counterfactual of HE_Biased_3. The same fire protection design engineer is retained for the same sprinkler retrofit on the same warehouse, for the same 3PL tenant conversion, with the same budget, water-supply constraints, and ongoing multi-project relationship with the building owner. The single material change is that the design window is extended from three weeks to six weeks before the permit submission deadline, removing the severe schedule compression present in the base scenario. All other facts, decision structure, and stakes are held constant. The purpose is to test whether the classification shortcut, the density selection shortcut, and the relationship-driven value-engineering recommendation are attributable to schedule pressure alone, or whether they persist even when the engineer has materially more time available to gather tenant-specific data, compare design alternatives, and present a fuller risk picture to the owner.",
    "occupational_realism": {
      "objective": "Design a code-compliant automatic sprinkler system for a new high-piled combustible storage racking layout inside an existing distribution warehouse, now with a six-week design window rather than three weeks before the permit submission deadline.",
      "setting": "Existing 140,000 sq ft tilt-up concrete distribution warehouse being subdivided for a new 3PL tenant storing palletized retail goods on double-row selective rack up to 32 feet; retrofit must be designed, permitted, and installed before the tenant's lease start date, with a six-week runway to permit submission.",
      "constraints": [
        "Six-week design window before permit submission deadline (extended from the three-week baseline)",
        "Fixed retrofit budget set by the building owner before final commodity classification was confirmed",
        "Limited access to the tenant's actual SKU list before design must be finalized, despite the additional time available",
        "Ongoing multi-project relationship between the engineer's firm and the building owner",
        "Existing water supply and riser infrastructure sized for a prior, lower-hazard occupancy",
        "Local AHJ requires hydraulic calculations and a witnessed flow test before occupancy"
      ],
      "stakeholders": [
        "Fire Protection Design Engineer (interviewee)",
        "Building owner / developer",
        "Incoming 3PL tenant operations manager",
        "Sprinkler installation contractor",
        "Local Authority Having Jurisdiction (AHJ) plan reviewer",
        "Engineer's firm principal"
      ],
      "technical_terms_to_use": [
        "commodity classification",
        "high-piled storage",
        "design density/area curve",
        "in-rack sprinklers (IRAS)",
        "ESFR (early suppression fast response)",
        "hydraulic calculation",
        "K-factor",
        "value engineering",
        "witnessed flow test",
        "AHJ plan review"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation bias",
        "stereotype",
        "incentive bias",
        "satisficing"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tenant is a 3PL company similar in profile to two prior clients the engineer has designed for",
          "No finalized SKU or packaging list from the incoming tenant yet, though the six-week window would allow time to request and wait for one",
          "Building owner still wants classification finalized early to lock the budget, but there is no hard schedule reason it could not wait a week or two"
        ],
        "new_information_after_decision": [
          "Partial tenant inventory list later shows a meaningful share of exposed unexpanded plastics mixed with cartoned goods, closer to Class IV/plastics than assumed"
        ],
        "alternatives": [
          "Classify commodity based on general similarity to prior 3PL tenants' storage profile",
          "Request a preliminary SKU/packaging sample list from the tenant, which the extended schedule could accommodate",
          "Classify conservatively as worst-case plastics until tenant data is confirmed"
        ],
        "intended_action": "Engineer classifies the commodity as Class III based on its resemblance to two previous 3PL clients he has designed for, without requesting tenant-specific packaging data, even though the six-week window left time to obtain it."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "NFPA design density/area curves for the assumed Class III classification and 32-ft rack height",
          "Multiple density/area combinations satisfy code minimums, some requiring additional in-rack sprinklers",
          "Permit submission is still several weeks out, leaving time to compare alternatives against the specific rack configuration"
        ],
        "new_information_after_decision": [
          "AHJ plan reviewer later flags that the chosen density/area point is at the marginal edge of the applicable curve given the actual rack configuration"
        ],
        "alternatives": [
          "Select the first density/area point on the curve that meets the minimum code requirement for the assumed classification",
          "Evaluate multiple density/area combinations against the specific rack configuration and aisle widths before selecting, which the remaining schedule allowed",
          "Consult the sprinkler manufacturer's design guide for a configuration-specific recommendation"
        ],
        "intended_action": "Engineer selects the first tabulated density/area combination that technically satisfies the code minimum for the assumed classification, without comparing it against alternate points better suited to the specific rack geometry, despite having calendar time remaining before the deadline."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Building owner requests a value-engineering pass to bring the design under the fixed retrofit budget",
          "In-rack sprinkler upgrade would add cost but reduce sensitivity to commodity classification uncertainty",
          "Engineer's firm has two additional retrofit projects pending with this same building owner"
        ],
        "new_information_after_decision": [
          "Removing the in-rack sprinkler allowance leaves the design with less margin against the commodity classification uncertainty identified in Phase 1"
        ],
        "alternatives": [
          "Recommend retaining the in-rack sprinkler allowance despite the added cost, citing classification uncertainty",
          "Recommend removing the in-rack sprinkler allowance to meet the owner's budget target",
          "Present both options with risk trade-offs and let the owner decide with full information"
        ],
        "intended_action": "Engineer recommends removing the in-rack sprinkler allowance to meet the owner's budget target, favoring the option likely to keep the ongoing multi-project relationship with the owner smooth, without fully surfacing the classification uncertainty risk in the recommendation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Contractor's certification paperwork shows the system installed per approved drawings",
          "AHJ requires a witnessed flow test before final sign-off",
          "With the extended schedule, there is adequate time remaining to complete testing before the tenant move-in date"
        ],
        "new_information_after_decision": [
          "Flow test performed with adequate time available passes comfortably above the required minimum"
        ],
        "alternatives": [
          "Proceed with a full witnessed flow test as required before sign-off",
          "Accept contractor certification alone and expedite paperwork to save time",
          "Schedule a partial test covering only the modified risers"
        ],
        "intended_action": "Engineer proceeds with the full witnessed flow test as required, with no meaningful time pressure at this stage, and documents the result before sign-off."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this retrofit project was for and what your role was?",
        "How did the six-week design window compare to how you'd normally schedule a project like this?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "Walk me through how the commodity classification decision came about.",
        "What happened after the density/area selection was submitted for plan review?",
        "How did the value-engineering conversation with the building owner unfold?",
        "What happened during commissioning and sign-off?"
      ],
      "decision_point_probes": [
        "At the point you classified the commodity, what specific information did you have about this tenant's actual inventory, and how much time did you have to get more?",
        "What other classification approaches did you consider, and why did you rule them out given the time you had?",
        "When you selected the density/area combination, what alternatives were on the table and how did you compare them?",
        "With several weeks still on the calendar, what was your basis for choosing that particular design point over the others available?",
        "When the owner asked for value engineering, what options did you consider and how did you weigh them?",
        "How did your relationship with the building owner factor into how you presented the options?",
        "At commissioning, what made you decide on the level of testing you pursued?"
      ],
      "cues": [
        "What specific cues told you the commodity classification was appropriate?",
        "What cues, if any, suggested you should get more tenant-specific data before finalizing the design, and did the extra time change how you weighed those cues?"
      ],
      "information_sources": [
        "What sources of information did you rely on most heavily at each stage?",
        "Was there information you didn't seek out that, given the schedule you had, would have been feasible to obtain?"
      ],
      "goals": [
        "What were you personally trying to achieve or protect at each of these points?",
        "With more schedule slack than usual, were there still competing goals between the budget and code compliance?"
      ],
      "alternatives": [
        "What other courses of action did you seriously consider at each decision point?",
        "Why didn't you pursue those alternatives, given that time wasn't the limiting factor here?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision one way over another?",
        "How confident were you in that decision at the time you made it?"
      ],
      "prior_experience": [
        "How did your experience with similar past projects or clients shape your approach here?"
      ],
      "time_pressure": [
        "Given the longer runway on this project, how did you decide how much time to spend on each decision?"
      ],
      "uncertainty": [
        "What were you most uncertain about at each stage, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If you had had the tenant's full SKU list before classifying the commodity, would you have done anything differently?",
        "If there had been no ongoing relationship with the building owner, would the value-engineering conversation have gone differently?",
        "Looking back, given that schedule wasn't the constraint here, is there a point where you'd make a different call?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "st_01",
        "bias": "Stereotyping",
        "decision_point": 1,
        "mechanism": "Engineer categorizes the incoming tenant's storage hazard based on surface similarity to a category of past clients rather than verifying tenant-specific inventory characteristics, even though the extended schedule left ample time to request that data.",
        "affected_reasoning_operation": "Category-based inference substituting for case-specific evidence gathering during commodity classification",
        "evidence_available_at_time": [
          "No finalized SKU/packaging list from the tenant",
          "General resemblance of tenant type to two prior 3PL clients",
          "Six-week window leaving practical time to request and wait for tenant data"
        ],
        "required_textual_manifestation": "Interviewee attributes the classification choice to the tenant fitting the general pattern of prior 3PL clients rather than to tenant-specific data, and explicitly acknowledges that time was not the reason data wasn't requested.",
        "plausible_nonbias_interpretation": "Using base rates from experience with similar occupancies is a legitimate engineering heuristic; the account must show the classification was treated as settled by category resemblance despite feasible opportunity to verify, distinguishing it from a time-constrained judgment call.",
        "strength": "subtle",
        "do_not_make_explicit": ["stereotyping", "generalization", "category bias", "assumption based on client type"]
      },
      {
        "instance_id": "sf_01",
        "bias": "Satisficing",
        "decision_point": 2,
        "mechanism": "Engineer accepts the first density/area combination that clears the minimum code threshold for the assumed classification instead of evaluating configuration-specific alternatives, despite calendar time remaining before the deadline.",
        "affected_reasoning_operation": "Premature termination of the alternative-generation and comparison process during hydraulic design selection",
        "evidence_available_at_time": [
          "Multiple density/area curve points available for the assumed classification",
          "Rack height and aisle configuration data on hand",
          "Several weeks remaining before the permit submission deadline"
        ],
        "required_textual_manifestation": "Interviewee describes stopping at the first design point that 'met the minimum' without comparing it against other viable points or manufacturer guidance, and frames the stopping point as adequate rather than attributing it to lack of available time.",
        "plausible_nonbias_interpretation": "Selecting a code-compliant minimum is a valid engineering practice; the account must show the stopping point was driven by adequacy-seeking rather than genuine time scarcity, since the schedule was no longer the binding constraint.",
        "strength": "moderate",
        "do_not_make_explicit": ["satisficing", "settling", "good enough", "minimum viable"]
      },
      {
        "instance_id": "ib_01",
        "bias": "Incentive bias",
        "decision_point": 3,
        "mechanism": "Engineer's recommendation on removing the in-rack sprinkler allowance is shaped by the desire to preserve a smooth, ongoing multi-project relationship with the building owner, rather than by a neutral weighing of the classification-uncertainty risk this removal introduces.",
        "affected_reasoning_operation": "Selective emphasis and information-presentation during a risk-tradeoff recommendation to a client on whom future business depends",
        "evidence_available_at_time": [
          "Owner's budget constraint and request for value engineering",
          "Known classification uncertainty from Phase 1 not yet resolved",
          "Two additional pending projects with the same building owner"
        ],
        "required_textual_manifestation": "Interviewee acknowledges factoring in the ongoing relationship with the owner when deciding how to present the in-rack sprinkler trade-off, and describes downplaying or not fully surfacing the classification-uncertainty risk in the recommendation given to the owner.",
        "plausible_nonbias_interpretation": "Cost-conscious value engineering is a routine and legitimate part of design practice; the account must show the recommendation was tilted by the engineer's stake in the client relationship rather than purely by a neutral risk assessment. This instance is held constant from the base scenario since the causal variable being tested is schedule duration, not the client relationship.",
        "strength": "moderate",
        "do_not_make_explicit": ["incentive bias", "conflict of interest", "self-interest", "relationship preservation"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "HE_Biased_3",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a counterfactual scenario, not a vocabulary or ambiguous control."
    },
    "counterfactual_specification": {
      "causal_variable": "Length of the design schedule before permit submission deadline",
      "original_state": "Three-week compressed design window (HE_Biased_3), creating tight schedule pressure at every decision point",
      "counterfactual_state": "Six-week design window before permit submission deadline, removing severe schedule compression while holding budget, relationship, and infrastructure constraints constant",
      "variables_to_hold_constant": [
        "Building, tenant type, and rack configuration",
        "Fixed retrofit budget set before classification confirmation",
        "Ongoing multi-project relationship between the engineer's firm and the building owner",
        "Existing water supply and riser infrastructure limitations",
        "AHJ requirement for hydraulic calculations and witnessed flow test",
        "The four decision points, their alternatives, and their sequencing",
        "The three targeted bias instances and their assigned decision points and mechanisms"
      ],
      "expected_causal_difference": "If the classification shortcut and density-selection shortcut in the base scenario were purely artifacts of schedule compression, the extended six-week window should be accompanied by fuller information-gathering and alternative comparison at Decision Points 1 and 2. If those patterns persist despite the additional time, this indicates the shortcuts are not solely schedule-driven. The relationship-driven value-engineering recommendation at Decision Point 3 is expected to persist unchanged, since the causal variable manipulated here is schedule length, not the client relationship.",
      "causal_test_question": "Does relaxing the design schedule from three weeks to six weeks change how the engineer gathers tenant data and compares design alternatives, or do the same reasoning shortcuts appear even with materially more time available?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points appear in the timeline, with Decision Point 4 free of intentionally embedded named-bias instances.",
      "Confirm exactly one Stereotyping instance is embedded at Decision Point 1 only, and that the account explicitly shows time was not the limiting factor.",
      "Confirm exactly one Satisficing instance is embedded at Decision Point 2 only, and that the account explicitly shows calendar time remained available.",
      "Confirm exactly one Incentive bias instance is embedded at Decision Point 3 only, held materially unchanged from the base scenario.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the public interview text.",
      "Confirm each decision point includes at least two plausible alternatives and both pre- and post-decision information.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals, including at least one probe on what information would have changed the decision and one on what would happen if a key feature were different.",
      "Confirm only the schedule-length variable is changed relative to HE_Biased_3, and all other material facts, wording patterns, and decision structure are preserved as far as possible.",
      "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given the four decision points and probe density without repetitive exposition.",
      "Confirm consequences described (comfortable flow test margin, plan reviewer flag, unresolved classification uncertainty) do not mechanically prove any decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Incentive bias",
        "occurrences": 1,
        "mechanism_constraint": "Must be held constant relative to HE_Biased_3, unaffected by the schedule-length manipulation"
      },
      {
        "bias": "Satisficing",
        "occurrences": 1,
        "mechanism_constraint": "Must be shown to occur despite calendar time remaining, not attributable to schedule scarcity"
      },
      {
        "bias": "Stereotyping",
        "occurrences": 1,
        "mechanism_constraint": "Must be shown to occur despite feasible opportunity to obtain tenant-specific data within the extended window"
      }
    ],
    "target_bias_names": ["Incentive bias", "Satisficing", "Stereotyping"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Incentive bias", "requested_occurrences": 1},
      {"bias": "Satisficing", "requested_occurrences": 1},
      {"bias": "Stereotyping", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "st_01", "bias": "Stereotyping"},
      {"instance_id": "sf_01", "bias": "Satisficing"},
      {"instance_id": "ib_01", "bias": "Incentive bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "st_01", "bias": "Stereotyping", "decision_point": 1},
      {"instance_id": "sf_01", "bias": "Satisficing", "decision_point": 2},
      {"instance_id": "ib_01", "bias": "Incentive bias", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "st_01",
        "bias": "Stereotyping",
        "mechanism": "Category-based inference about tenant storage hazard substituted for case-specific inventory verification, persisting despite feasible time to verify",
        "affected_reasoning_operation": "Evidence-selection/classification during commodity classification",
        "evidence_source": "Similarity to two prior 3PL clients vs. absent tenant-specific SKU/packaging data, with six-week schedule allowing time to request it",
        "distinctiveness_requirement": "Only stereotyping instance in the scenario; occurs solely at Decision Point 1 tied to classification; distinguished from the paired base scenario by the explicit absence of schedule pressure as an available justification."
      },
      {
        "instance_id": "sf_01",
        "bias": "Satisficing",
        "mechanism": "Premature stopping at the first code-minimum-satisfying design option instead of comparing configuration-specific alternatives, despite remaining calendar time",
        "affected_reasoning_operation": "Alternative-generation and comparison during hydraulic density/area selection",
        "evidence_source": "Multiple available density/area curve points and manufacturer guidance vs. several weeks of schedule slack remaining",
        "distinctiveness_requirement": "Only satisficing instance in the scenario; occurs solely at Decision Point 2 tied to density/area selection; distinguished from the paired base scenario by removing the time-scarcity justification available in HE_Biased_3."
      },
      {
        "instance_id": "ib_01",
        "bias": "Incentive bias",
        "mechanism": "Recommendation shaped by desire to preserve an ongoing multi-project client relationship rather than neutral risk weighing; unaffected by the schedule-length manipulation",
        "affected_reasoning_operation": "Selective emphasis in risk-tradeoff communication during value-engineering recommendation",
        "evidence_source": "Owner's budget request and pending future projects vs. unresolved classification-uncertainty risk from Decision Point 1",
        "distinctiveness_requirement": "Only incentive-bias instance in the scenario; occurs solely at Decision Point 3 tied to the value-engineering recommendation; held constant across base and counterfactual scenarios since the manipulated causal variable is schedule length, not the client relationship."
      }
    ],
    "intended_strength": [
      {"instance_id": "st_01", "bias": "Stereotyping", "strength": "subtle"},
      {"instance_id": "sf_01", "bias": "Satisficing", "strength": "moderate"},
      {"instance_id": "ib_01", "bias": "Incentive bias", "strength": "moderate"}
    ],
    "paired_scenario_id": "HE_Biased_3",
    "counterfactual_variable": {
      "name": "Length of the design schedule before permit submission deadline",
      "original_state": "Three-week compressed design window",
      "changed_state": "Six-week design window before permit submission deadline",
      "variables_to_hold_constant": [
        "Building, tenant type, and rack configuration",
        "Fixed retrofit budget set before classification confirmation",
        "Ongoing multi-project relationship between the engineer's firm and the building owner",
        "Existing water supply and riser infrastructure limitations",
        "AHJ requirement for hydraulic calculations and witnessed flow test",
        "The four decision points, their alternatives, and their sequencing",
        "The three targeted bias instances and their assigned decision points and mechanisms"
      ]
    },
    "scenario_id": "HE_Counterfactual_3",
    "domain_id": "HE",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Occurrences spread one-per-bias across three distinct, mechanism-fitting decision points, mirroring the base scenario's allocation (Stereotyping at Decision Point 1, Satisficing at Decision Point 2, Incentive bias at Decision Point 3), with Decision Point 4 left free of intentional bias instances. The schedule-length causal variable is manipulated to strip away the time-pressure justification available at Decision Points 1 and 2 in the base scenario, while the relationship-driven mechanism at Decision Point 3 is deliberately held constant as it is orthogonal to the manipulated variable.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Building, tenant type, and rack configuration",
      "Fixed retrofit budget set before classification confirmation",
      "Ongoing multi-project relationship between the engineer's firm and the building owner",
      "Existing water supply and riser infrastructure limitations",
      "AHJ requirement for hydraulic calculations and witnessed flow test",
      "The four decision points, their alternatives, and their sequencing",
      "The three targeted bias instances and their assigned decision points and mechanisms"
    ],
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
          "segment_type": "schedule_assessment",
          "raw_interview_anchor": "Actually pretty comfortable, for once. We had six weeks from kickoff to permit submission... I wasn't fighting the calendar the way I sometimes am.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant explicitly characterizes the schedule as comfortable and non-constraining; this is contextual reasoning and contains no hidden bias instance."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "commodity_classification_and_information_search",
          "raw_interview_anchor": "There wasn't really a schedule reason it had to happen that week... I'd done two other jobs for similar 3PL operators... I went with Class III based on that pattern and moved on... I went with that pattern instead of waiting on their list.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["st_01"],
          "ground_truth_rationale": "The classification was inferred from a tenant-type category and two prior exemplars instead of tenant-specific packaging data, despite feasible time to obtain it."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "hydraulic_density_area_selection",
          "raw_interview_anchor": "Several density and area points would have satisfied code minimum... I took the first point that cleared the minimum... I had the time to run more comparisons, honestly, I just didn't loop back once I had something that worked.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["sf_01"],
          "ground_truth_rationale": "The participant stopped at the first technically acceptable design point without comparing configuration-specific alternatives, although several weeks remained."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "value_engineering_risk_communication",
          "raw_interview_anchor": "Keeping it would've given more margin against the classification uncertainty I already knew about. But we've got two more retrofit jobs pending with him... so I recommended pulling the allowance to hit his number... I framed the removal as a reasonable trade rather than spelling out how much margin we'd be giving up.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["ib_01"],
          "ground_truth_rationale": "The recommendation and selective framing were shaped by preserving an ongoing owner relationship while reducing a known safety margin."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "commissioning_testing_decision",
          "raw_interview_anchor": "The AHJ requires the witnessed flow test regardless, and with days to spare before move-in, there wasn't a reason to cut corners. I did the full test.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant followed the required full testing process with adequate schedule slack; the generation specification embeds no bias at Decision Point 4."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first review of a single retrospective interview about design decision-making. Only occurrences with affirmative evidence of a bias-specific reasoning mechanism are identified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "satisficing",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory bias", "confirmation bias in information search"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, favor, or avoid information in ways that confirm or protect an existing belief, while underweighting or failing to seek disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Commodity classification selection for warehouse retrofit",
      "decision_point_description": "Finalizing the storage commodity classification as Class III without waiting for SKU/packaging data",
      "affected_reasoning_operation": "classification judgment and information search under uncertainty",
      "bias_specific_mechanism": "The participant formed an initial Class III classification from tenant type and two prior similar projects, then avoided requesting project-specific SKU/packaging data that could have disconfirmed that classification, despite having time to obtain it.",
      "manifestation_in_interview": "He reports having enough time to request a preliminary SKU sample but instead relied on the pattern from two prior Class III jobs and stated that nothing specific in early conversations made him feel it was urgent to chase down the data.",
      "effect_on_reasoning_or_decision": "Locked in a Class III classification that later appeared too low; a later partial inventory list showed more exposed unexpanded plastics than assumed, closer to a plastics classification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have a finalized SKU or packaging list from the tenant yet, they were still working that out on their end, and the owner wanted the classification locked so he could fix the retrofit budget. There wasn't really a schedule reason it had to happen that week, I could have waited and asked for a sample of their packaging list, but I'd done two other jobs for similar 3PL operators and had a good sense of what that kind of tenant typically stores. I went with Class III based on that pattern and moved on.",
          "evidence_explanation": "Shows an initial belief based on prior jobs and a decision not to seek project-specific disconfirming information even though time allowed."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it briefly. But in my experience, this type of tenant runs cartoned retail goods, maybe some mixed packaging, and both of the prior jobs landed at Class III. I went with that pattern instead of waiting on their list.",
          "evidence_explanation": "Explicitly describes preferring the available precedent pattern over the potentially disconfirming current-project data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Something specific standing out, like if they'd mentioned electronics or aerosols. Nothing in the early conversations flagged that, so it didn't feel urgent to chase down.",
          "evidence_explanation": "Indicates that the absence of conspicuous disconfirming cues was treated as sufficient, rather than actively seeking the project-specific list."
        }
      ],
      "correction_or_counterevidence": "The participant did briefly consider requesting the data, and he said a specific early flag would have prompted him to wait. He also acknowledged in hindsight that seeing the SKU list upfront would likely have led to a more conservative classification.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved design-cognition passage supports confirmation bias in design, including ignoring or misinterpreting contradictory information and design fixation.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "When designers hold beliefs that can be contradicted by factual evidence, it is reasonable to assume they will fail to demonstrate a confirmatory bias. However, we observed numerous instances of belief pe of contradicting evidence, which resulted in participants misinterpreting or ignoring relevant information. ... Confirma tion bias could contribute to design fixation or an unwillingness to compromise on design ideas; if designers",
          "mechanism_supported_by_source": "The source connects confirmation bias to designers ignoring or misinterpreting contradictory information and to design fixation.",
          "relevance_to_this_occurrence": "The participant locked onto a Class III belief from prior experience and did not seek project-specific data that could contradict it, consistent with confirmation-biased information search and design fixation."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "satisficing",
      "alternative_labels": ["satisficing heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "A decision strategy of selecting the first option that meets a minimum threshold of acceptability, rather than optimizing across available alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hydraulic density/area selection for Class III at 32 feet",
      "decision_point_description": "Selecting the density and area point for the rack sprinkler hydraulic calculation",
      "affected_reasoning_operation": "alternative generation/comparison and option selection",
      "bias_specific_mechanism": "The participant accepted the first density/area point that cleared the code minimum and did not loop back to compare other code-compliant points or manufacturer guidance, even though he had time and acknowledged he could have done so.",
      "manifestation_in_interview": "He states he took the first point that cleared the minimum and built the calc package around it, and that he did not loop back once he had something that worked; the plan reviewer later noted the point was near the edge of the applicable curve.",
      "effect_on_reasoning_or_decision": "Selected a density/area point that was code-compliant but close to the edge of the applicable curve for the actual rack configuration, reducing design margin and prompting a plan reviewer note.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Several density and area points would have satisfied code minimum for Class III at that height, some needing more in-rack sprinklers. I could have compared those against the specific rack configuration and aisle widths, or checked the manufacturer's guide for something tailored to the layout.",
          "evidence_explanation": "Identifies feasible alternatives and information sources that were available but not used."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I took the first point that cleared the minimum for the assumed classification and built the calc package around it. I had the time to run more comparisons, honestly, I just didn't loop back once I had something that worked.",
          "evidence_explanation": "Directly expresses the satisficing mechanism: accepting the first minimally acceptable solution rather than comparing available alternatives."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, flagged that the point I'd chosen was close to the edge of the applicable curve for the actual rack configuration. Not a rejection, just a note to be aware of.",
          "evidence_explanation": "Shows a downstream consequence of the minimally compliant choice."
        }
      ],
      "correction_or_counterevidence": "The chosen point was code-compliant, plan review did not reject it, and the final witnessed flow test passed comfortably; the bias affected conservatism rather than causing failure.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved corpus passage treats satisficing in a cognitive-bias/search context and supports the mechanism of settling for a sufficient option rather than optimizing.",
      "corpus_evidence": [
        {
          "source_identifier": "Azzopardi (2021). Cognitive Biases in Search.pdf",
          "paper_title": "Cognitive Biases in Search",
          "authors": "Azzopardi",
          "publication_year": "2021",
          "retrieved_passage_or_finding": "rather than trying to minimise effort, satisficing may be due to searchers trying to optimise the rate at which they en- counter relevant information (as assumed in Information Foraging Theory [ 60 ] and other related models of search based on Expected",
          "mechanism_supported_by_source": "The source discusses satisficing as a decision/search mechanism, supporting the label and the general concept of accepting a sufficient option rather than fully optimizing.",
          "relevance_to_this_occurrence": "The participant accepted a sufficient density/area point instead of further comparing alternatives, consistent with satisficing."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "motivated reasoning",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Value-engineering recommendation to remove in-rack sprinkler allowance",
      "supporting_interview_quote": "He wanted the number under budget, and the in-rack allowance was the biggest thing I could trim. Keeping it would've given more margin against the classification uncertainty I already knew about. But we've got two more retrofit jobs pending with him, and I didn't want friction over one line item, so I recommended pulling the allowance to hit his number.",
      "plausible_mechanism": "The desire to preserve the owner relationship may have motivated the participant to frame the removal as a reasonable trade and under-communicate the classification uncertainty, a pattern consistent with motivated reasoning.",
      "why_not_identified": "The transcript presents this as an explicit tradeoff driven by budget and relationship incentives rather than a distorted belief or judgment. There is no affirmative evidence that the participant's own risk assessment was biased; the communication choice may reflect legitimate client-management behavior."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a single retrospective self-report and may not capture online cognitive processes at the time of each decision.",
    "The retrieved confirmation-bias passage contains OCR-like fragmentation, so its support is used with caution.",
    "Satisficing can be a defensible bounded-rationality strategy, so its classification as a bias depends on evidence that superior alternatives were available at acceptable cost.",
    "The analysis does not infer bias merely from the later partial inventory or from the plan reviewer's comment; it relies on the participant's description of his reasoning."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Counterfactual_3_Sonar_on",
  "interview_id": "HE_Counterfactual_3",
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
