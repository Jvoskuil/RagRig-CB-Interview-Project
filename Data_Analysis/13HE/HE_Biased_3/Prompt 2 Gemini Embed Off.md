You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a research review of design decision-making, nothing you say will be tied to your name in any report, and you can skip anything you're not comfortable discussing. Sound okay?

Participant: Yeah, that's fine. I've done these before for our internal lessons-learned process, so I'm used to it.

Interviewer: Great. Can you start by telling me what your role was on this project and what the assignment involved?

Participant: Sure. I'm the lead design engineer on a sprinkler retrofit for a distribution warehouse, about 140,000 square feet, tilt-up concrete. The building owner was bringing in a new third-party logistics tenant who needed part of the floor converted to high-piled rack storage, double-row selective rack up to 32 feet. My job was to take the existing system, which was designed for a much lighter occupancy, and redesign it to handle the new storage configuration, get it through plan review, and get it installed before the tenant's lease start.

Interviewer: What made this one more complicated than a typical retrofit?

Participant: Mainly the schedule. We had about three weeks from kickoff to permit submission because the tenant's stocking schedule was locked in and the owner didn't want to renegotiate the lease start. On top of that, the existing water supply and riser sizing were set up for the old, lower-hazard use, so I was working within infrastructure that wasn't originally built for this.

Interviewer: Walk me through the incident from the beginning, in your own words.

Participant: We got the go-ahead and I needed to nail down the commodity classification pretty fast, because that drives everything else, the density, the rack sprinkler requirements, all of it. I hadn't gotten a finalized SKU or packaging list from the tenant yet, they were still finalizing their own inventory plans, but the owner wanted the classification locked so he could set the retrofit budget. I'd done two other jobs for similar 3PL operators in the past couple of years, so I had a sense of what that kind of tenant typically stores. Based on that, I classified it as Class III commodity and moved forward with design. From there I pulled the NFPA design density and area curves for that classification at 32 feet of rack height, picked a density/area point that cleared the code minimum, and built out the hydraulic calculations. That went to the owner for a value engineering pass, since the number came in over his budget, and we had a conversation about trimming the in-rack sprinkler allowance to bring the cost down. After the system was installed, we got to commissioning, and even with the schedule tight, I made sure we did the full witnessed flow test before sign-off, which the AHJ requires.

Interviewer: Let's reconstruct that chronologically. What came first?

Participant: Classification first, in the first few days. Then the hydraulic calc and density selection, maybe a week and a half in, right before permit submission. The value-engineering conversation with the owner happened after plan review comments came back, so maybe two and a half weeks in. Commissioning was right at the end, days before the tenant's move-in date.

Interviewer: What did you learn after the classification that you didn't know at the time you made it?

Participant: A partial inventory list came through a bit later, and it showed a decent chunk of exposed unexpanded plastics mixed in with the cartoned goods, more than I'd assumed. That pushed the actual profile closer to a plastics classification than straight Class III.

Interviewer: Let's go back to that classification decision specifically. What information did you actually have in hand at that point?

Participant: I had the tenant's general business type, third-party logistics handling retail goods, and I had my own history with two comparable clients. I didn't have their SKU list yet.

Interviewer: What other approaches did you consider before settling on Class III?

Participant: I could have asked for a preliminary packaging sample list before finalizing anything, or gone conservative and designed to a worst-case plastics assumption until the data came in.

Interviewer: Why didn't you go with either of those?

Participant: Honestly, this type of tenant, in my experience, usually runs cartoned retail goods, maybe some mixed packaging, but nothing that changes the classification much. The two prior jobs I'd done for similar operators both landed at Class III, so I went with that pattern rather than waiting on the tenant's list, especially with the owner pushing to lock the budget.

Interviewer: What would have made you wait for the SKU data instead?

Participant: If something about this particular tenant's business model had stood out as different, like if they'd mentioned handling electronics or aerosols specifically. Nothing in the early conversations flagged that, so I didn't press for the list before moving forward.

Interviewer: Let's move to the density selection. What alternatives were actually on the table?

Participant: There were several density/area points that would satisfy the code minimum for Class III at that rack height, some requiring more in-rack sprinklers, some less. I could have compared those against the specific rack configuration and aisle widths, or checked the manufacturer's design guide for something tailored to that layout.

Interviewer: What did you actually do?

Participant: I took the first density/area point that cleared the minimum for the assumed classification and built the calc package around it. We were up against the submission deadline, and that point technically satisfied the requirement, so I ran with it rather than working through the other combinations.

Interviewer: Did the plan reviewer have any comments on that later?

Participant: Yeah, the AHJ reviewer flagged that the point I'd chosen was pretty close to the edge of the applicable curve for the actual rack configuration. Not a rejection, just a note.

Interviewer: What was going through your mind when the owner asked for value engineering?

Participant: He wanted the number under budget, and the in-rack sprinkler allowance was the biggest line item I could trim. Retaining it would've kept more margin against the classification uncertainty, since I knew the plastics content wasn't fully confirmed yet. But we've got two more retrofit jobs pending with this same owner, and I didn't want that relationship to get strained over this one line item, so I recommended pulling the in-rack allowance to hit his number.

Interviewer: Did you lay out the classification uncertainty as part of that recommendation?

Participant: Not in as much detail as I probably could have. I mentioned it in passing but framed the removal as a reasonable trade-off rather than walking him through how much margin we'd be giving up.

Interviewer: Last decision point, commissioning. What determined how much testing you pursued?

Participant: The AHJ requires a witnessed flow test regardless, so that wasn't really optional. With the move-in date bearing down, I could have leaned on the contractor's certification paperwork and expedited sign-off, or done a partial test on just the modified risers. I decided to do the full witnessed test anyway.

Interviewer: How did that turn out?

Participant: It passed, but the value came in close to the required minimum, close enough that I flagged it for monitoring going forward.

Interviewer: If you'd had the tenant's full SKU list before classifying the commodity, would you have done anything differently?

Participant: Probably, yeah. If I'd seen the plastics percentage upfront, I'd have leaned toward a more conservative classification from the start rather than defaulting to what I'd seen on similar jobs.

Interviewer: If there'd been no ongoing relationship with the building owner, do you think the value-engineering conversation would have gone differently?

Participant: Maybe. I'd like to think I'd have pushed harder on keeping the in-rack allowance, but I can't say for certain the outcome would've changed.

Interviewer: Looking back, is there a point where you'd make a different call given the same information you had at the time?

Participant: The classification, probably. Everything downstream followed from that first call, and I had the means to ask for more data before locking it in.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HE_Biased_3",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Fire Protection System Designer (Sprinkler/Suppression Design Engineer)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Rack Storage Retrofit: Commodity Classification and Density Trade-offs Under Deadline",
    "scenario_summary_internal": "A fire protection design engineer is retained to design an automatic sprinkler retrofit for a third-party logistics (3PL) distribution warehouse that is converting part of its floor plan to high-piled rack storage for a new client tenant. The engineer must classify the stored commodity, select a hydraulic design density/K-factor combination, respond to the building owner's cost-reduction pressure during value engineering, and decide how rigorously to verify installation compliance before sign-off. The project is compressed into a three-week design window because the tenant's lease and stocking schedule are fixed. The engineer has worked with similar 3PL operators before and has an ongoing multi-project relationship with this building owner.",
    "occupational_realism": {
      "objective": "Design a code-compliant automatic sprinkler system for a new high-piled combustible storage racking layout inside an existing distribution warehouse, within a compressed schedule and a fixed retrofit budget.",
      "setting": "Existing 140,000 sq ft tilt-up concrete distribution warehouse being subdivided for a new 3PL tenant storing palletized retail goods on double-row selective rack up to 32 feet; retrofit must be designed, permitted, and installed before the tenant's lease start date.",
      "constraints": [
        "Three-week design turnaround before permit submission deadline",
        "Fixed retrofit budget set by the building owner before final commodity classification was confirmed",
        "Limited access to the tenant's actual SKU list before design must be finalized",
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
          "No finalized SKU or packaging list from the incoming tenant yet",
          "Building owner wants classification finalized quickly to lock the budget"
        ],
        "new_information_after_decision": [
          "Partial tenant inventory list later shows a meaningful share of exposed unexpanded plastics mixed with cartoned goods, closer to Class IV/plastics than assumed"
        ],
        "alternatives": [
          "Classify commodity based on general similarity to prior 3PL tenants' storage profile",
          "Require a preliminary SKU/packaging sample list from the tenant before finalizing classification",
          "Classify conservatively as worst-case plastics until tenant data is confirmed"
        ],
        "intended_action": "Engineer classifies the commodity as Class III based on its resemblance to two previous 3PL clients he has designed for, without requesting tenant-specific packaging data."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "NFPA design density/area curves for the assumed Class III classification and 32-ft rack height",
          "Multiple density/area combinations satisfy code minimums, some requiring additional in-rack sprinklers",
          "Schedule pressure to finalize hydraulic calculations for permit submission"
        ],
        "new_information_after_decision": [
          "AHJ plan reviewer later flags that the chosen density/area point is at the marginal edge of the applicable curve given the actual rack configuration"
        ],
        "alternatives": [
          "Select the first density/area point on the curve that meets the minimum code requirement for the assumed classification",
          "Evaluate multiple density/area combinations against the specific rack configuration and aisle widths before selecting",
          "Consult the sprinkler manufacturer's design guide for a configuration-specific recommendation"
        ],
        "intended_action": "Engineer selects the first tabulated density/area combination that technically satisfies the code minimum for the assumed classification, without comparing it against alternate points better suited to the specific rack geometry, in order to keep the calculation package on schedule."
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
          "Schedule pressure remains high as tenant move-in date approaches"
        ],
        "new_information_after_decision": [
          "Flow test performed under time pressure passes but at a value close to the required minimum, prompting a note for future monitoring"
        ],
        "alternatives": [
          "Proceed with a full witnessed flow test as required before sign-off",
          "Accept contractor certification alone and expedite paperwork to save time",
          "Schedule a partial test covering only the modified risers"
        ],
        "intended_action": "Engineer proceeds with the full witnessed flow test as required, despite time pressure, and documents the result before sign-off."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this retrofit project was for and what your role was?",
        "What made this particular design assignment more difficult than a routine sprinkler retrofit?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "Walk me through how the commodity classification decision came about.",
        "What happened after the density/area selection was submitted for plan review?",
        "How did the value-engineering conversation with the building owner unfold?",
        "What happened during commissioning and sign-off?"
      ],
      "decision_point_probes": [
        "At the point you classified the commodity, what specific information did you have about this tenant's actual inventory?",
        "What other classification approaches did you consider, and why did you rule them out?",
        "When you selected the density/area combination, what alternatives were on the table and how did you compare them?",
        "What was your basis for choosing that particular design point over the others available?",
        "When the owner asked for value engineering, what options did you consider and how did you weigh them?",
        "How did your relationship with the building owner factor into how you presented the options?",
        "At commissioning, what made you decide on the level of testing you pursued?"
      ],
      "cues": [
        "What specific cues told you the commodity classification was appropriate?",
        "What cues, if any, suggested you should get more tenant-specific data before finalizing the design?"
      ],
      "information_sources": [
        "What sources of information did you rely on most heavily at each stage?",
        "Was there information you didn't seek out that, in hindsight, might have been available?"
      ],
      "goals": [
        "What were you personally trying to achieve or protect at each of these points?",
        "Were there competing goals between the schedule, the budget, and code compliance?"
      ],
      "alternatives": [
        "What other courses of action did you seriously consider at each decision point?",
        "Why didn't you pursue those alternatives?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision one way over another?",
        "How confident were you in that decision at the time you made it?"
      ],
      "prior_experience": [
        "How did your experience with similar past projects or clients shape your approach here?"
      ],
      "time_pressure": [
        "How did the compressed schedule affect how much time you spent on each decision?"
      ],
      "uncertainty": [
        "What were you most uncertain about at each stage, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If you had had the tenant's full SKU list before classifying the commodity, would you have done anything differently?",
        "If there had been no ongoing relationship with the building owner, would the value-engineering conversation have gone differently?",
        "Looking back, is there a point where you'd make a different call given the same information you had at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "st_01",
        "bias": "Stereotyping",
        "decision_point": 1,
        "mechanism": "Engineer categorizes the incoming tenant's storage hazard based on surface similarity to a category of past clients (\"3PL operators like this always store cartoned goods\") rather than verifying tenant-specific inventory characteristics.",
        "affected_reasoning_operation": "Category-based inference substituting for case-specific evidence gathering during commodity classification",
        "evidence_available_at_time": [
          "No finalized SKU/packaging list from the tenant",
          "General resemblance of tenant type to two prior 3PL clients",
          "Owner pressure to finalize classification quickly"
        ],
        "required_textual_manifestation": "Interviewee explicitly attributes the classification choice to the tenant fitting the general pattern of prior 3PL clients ('this type of tenant is usually...') rather than to tenant-specific data, and does not request or wait for confirming inventory data before finalizing.",
        "plausible_nonbias_interpretation": "Using base rates from experience with similar occupancies is a legitimate engineering heuristic when time-constrained; the account must show the classification was treated as settled rather than provisional despite available means to verify it.",
        "strength": "subtle",
        "do_not_make_explicit": ["stereotyping", "generalization", "category bias", "assumption based on client type"]
      },
      {
        "instance_id": "sf_01",
        "bias": "Satisficing",
        "decision_point": 2,
        "mechanism": "Engineer accepts the first density/area combination that clears the minimum code threshold for the assumed classification instead of evaluating configuration-specific alternatives that could better match the actual rack geometry.",
        "affected_reasoning_operation": "Premature termination of the alternative-generation and comparison process during hydraulic design selection",
        "evidence_available_at_time": [
          "Multiple density/area curve points available for the assumed classification",
          "Rack height and aisle configuration data on hand",
          "Schedule pressure to submit hydraulic calculations for permit"
        ],
        "required_textual_manifestation": "Interviewee describes stopping at the first design point that 'met the minimum' without describing a comparison against other viable points or manufacturer guidance, framing the choice as sufficient rather than optimal, given the deadline.",
        "plausible_nonbias_interpretation": "Selecting a code-compliant minimum is a valid, common engineering practice under time constraints; the account must show the stopping point was driven by adequacy-seeking rather than a reasoned comparison against configuration-specific alternatives that were accessible.",
        "strength": "subtle",
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
        "plausible_nonbias_interpretation": "Cost-conscious value engineering is a routine and legitimate part of design practice; the account must show the recommendation was tilted by the engineer's stake in the client relationship rather than purely by a neutral risk assessment.",
        "strength": "moderate",
        "do_not_make_explicit": ["incentive bias", "conflict of interest", "self-interest", "relationship preservation"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition scenario with no paired control specified in this request."
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
      "Confirm exactly 4 decision points appear in the timeline, with Decision Point 4 free of intentionally embedded named-bias instances.",
      "Confirm exactly one Stereotyping instance is embedded at Decision Point 1 only.",
      "Confirm exactly one Satisficing instance is embedded at Decision Point 2 only.",
      "Confirm exactly one Incentive bias instance is embedded at Decision Point 3 only.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the public interview text.",
      "Confirm each decision point includes at least two plausible alternatives and both pre- and post-decision information.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given the four decision points and probe density without repetitive exposition.",
      "Confirm consequences described (marginal flow test result, plan reviewer flag, unresolved classification uncertainty) do not mechanically prove any decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Incentive bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Satisficing",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Stereotyping",
        "occurrences": 1,
        "mechanism_constraint": null
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
        "mechanism": "Category-based inference about tenant storage hazard substituted for case-specific inventory verification",
        "affected_reasoning_operation": "Evidence-selection/classification during commodity classification",
        "evidence_source": "Similarity to two prior 3PL clients vs. absent tenant-specific SKU/packaging data",
        "distinctiveness_requirement": "Only stereotyping instance in the scenario; occurs solely at Decision Point 1 tied to classification, distinct from the Decision Point 2 satisficing instance which concerns density selection, not categorization."
      },
      {
        "instance_id": "sf_01",
        "bias": "Satisficing",
        "mechanism": "Premature stopping at the first code-minimum-satisfying design option instead of comparing configuration-specific alternatives",
        "affected_reasoning_operation": "Alternative-generation and comparison during hydraulic density/area selection",
        "evidence_source": "Multiple available density/area curve points and manufacturer guidance vs. schedule pressure",
        "distinctiveness_requirement": "Only satisficing instance in the scenario; occurs solely at Decision Point 2 tied to density/area selection, distinct from the Decision Point 1 classification act and the Decision Point 3 recommendation act."
      },
      {
        "instance_id": "ib_01",
        "bias": "Incentive bias",
        "mechanism": "Recommendation shaped by desire to preserve an ongoing multi-project client relationship rather than neutral risk weighing",
        "affected_reasoning_operation": "Selective emphasis in risk-tradeoff communication during value-engineering recommendation",
        "evidence_source": "Owner's budget request and pending future projects vs. unresolved classification-uncertainty risk from Decision Point 1",
        "distinctiveness_requirement": "Only incentive-bias instance in the scenario; occurs solely at Decision Point 3 tied to the value-engineering recommendation, distinct from the classification and density-selection acts at earlier decision points."
      }
    ],
    "intended_strength": [
      {"instance_id": "st_01", "bias": "Stereotyping", "strength": "subtle"},
      {"instance_id": "sf_01", "bias": "Satisficing", "strength": "subtle"},
      {"instance_id": "ib_01", "bias": "Incentive bias", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HE_Biased_3",
    "domain_id": "HE",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Occurrences spread one-per-bias across three distinct, mechanism-fitting decision points (Stereotyping at Decision Point 1 - classification; Satisficing at Decision Point 2 - density/area selection; Incentive bias at Decision Point 3 - value-engineering recommendation); Decision Point 4 (commissioning/sign-off) deliberately left free of intentional bias instances to serve as a non-biased comparison point and to avoid exceeding the two-instances-per-decision-point limit unnecessarily.",
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
      "segment_id": "dp_01_classification",
      "speaker": "Participant",
      "segment_type": "decision_reasoning",
      "raw_interview_anchor": "I had the tenant's general business type... I didn't have their SKU list yet. ... The two prior jobs I'd done for similar operators both landed at Class III, so I went with that pattern rather than waiting on the tenant's list.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["st_01"],
      "ground_truth_rationale": "The participant classified the tenant using category similarity to two prior 3PL clients instead of obtaining tenant-specific packaging data."
    },
    {
      "segment_id": "dp_02_density_selection",
      "speaker": "Participant",
      "segment_type": "decision_reasoning",
      "raw_interview_anchor": "I took the first density/area point that cleared the minimum... and ran with it rather than working through the other combinations.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["sf_01"],
      "ground_truth_rationale": "The participant stopped at the first code-minimum-satisfying design point without comparing the available configuration-specific alternatives."
    },
    {
      "segment_id": "dp_03_value_engineering",
      "speaker": "Participant",
      "segment_type": "decision_reasoning",
      "raw_interview_anchor": "We've got two more retrofit jobs pending with this same owner... I recommended pulling the in-rack allowance to hit his number. ... I mentioned [the uncertainty] in passing but framed the removal as a reasonable trade-off.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["ib_01"],
      "ground_truth_rationale": "The recommendation was influenced by preserving an ongoing owner relationship, while the classification-uncertainty risk was not fully surfaced."
    },
    {
      "segment_id": "dp_04_commissioning",
      "speaker": "Participant",
      "segment_type": "decision_reasoning",
      "raw_interview_anchor": "I decided to do the full witnessed test anyway.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "The generation specification deliberately leaves commissioning free of intentional bias; the participant followed the required full witnessed flow-test process."
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
    "analysis_scope_note": "Evaluated the interview transcript for affirmative, mechanism-grounded cognitive bias occurrences in the participant's decision-making episodes: commodity classification, density/area selection, value engineering, and commissioning. No experimental condition or benchmark was inferred."
  },
  "identified_bias_summary": [
    {
      "bias_label": "motivated reasoning",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness heuristic",
      "alternative_labels": ["availability heuristic", "prototype heuristic", "insensitivity to sample size"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the probability or category membership of an entity by how similar it is to a prototypical case or prior category members, while underweighting base rates and individuating information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Commodity classification under uncertainty",
      "decision_point_description": "Selecting the commodity classification for the retrofit before tenant SKU/packaging data was available.",
      "affected_reasoning_operation": "Categorization/classification under uncertainty",
      "bias_specific_mechanism": "The participant categorized the new tenant's commodity by matching it to a prototype formed from two prior similar 3PL projects, rather than waiting for tenant-specific SKU/packaging data. This pattern-matching overgeneralized to Class III and underweighted the possibility that the current tenant's inventory might contain a meaningful plastics content.",
      "manifestation_in_interview": "The participant stated that two similar past jobs had landed at Class III and that this type of tenant in his experience usually runs cartoned retail goods; on that basis he locked the commodity classification before receiving a finalized SKU or packaging list.",
      "effect_on_reasoning_or_decision": "The design was locked to a Class III basis prematurely; downstream hydraulic calculations and budget were developed from that assumption. The later partial inventory list showed exposed unexpanded plastics, suggesting the actual profile was closer to a plastics classification than straight Class III.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd done two other jobs for similar 3PL operators in the past couple of years, so I had a sense of what that kind of tenant typically stores. Based on that, I classified it as Class III commodity and moved forward with design.",
          "evidence_explanation": "This shows the participant derived the classification from prior similar jobs before any tenant-specific inventory data was available, which is the representativeness heuristic operation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, this type of tenant, in my experience, usually runs cartoned retail goods, maybe some mixed packaging, but nothing that changes the classification much. The two prior jobs I'd done for similar operators both landed at Class III, so I went with that pattern rather than waiting on the tenant's list, especially with the owner pushing to lock the budget.",
          "evidence_explanation": "This explicitly describes the pattern-matching rationale and the choice not to wait for the SKU list, demonstrating that the category prototype overrode the available individuating uncertainty."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction occurred; the partial inventory list later showed exposed unexpanded plastics and suggested the actual profile was closer to a plastics classification. Schedule and owner budget pressure were present, but the transcript indicates the participant had alternative options such as requesting a preliminary packaging list or designing to a worst-case plastics assumption.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific corpus passages were supplied with this interview; the classification relies on established cognitive-science knowledge rather than retrieved corpus evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "motivated reasoning",
      "alternative_labels": ["motivated cognition", "directional motivated reasoning"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to process information and evaluate risks in ways that support a directional goal or desired conclusion, such as maintaining a valued relationship, leading to selective evaluation and communication of risk-relevant information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Value engineering recommendation on in-rack sprinkler allowance",
      "decision_point_description": "Deciding whether to retain the in-rack sprinkler allowance or remove it to meet the owner's budget target.",
      "affected_reasoning_operation": "Risk assessment, recommendation, and risk communication",
      "bias_specific_mechanism": "The participant had a directional goal to preserve his relationship with the building owner because two additional retrofit jobs were pending. That relationship goal led him to recommend removing the in-rack sprinkler allowance and to downplay the classification uncertainty, rather than giving the owner a full account of the margin being sacrificed.",
      "manifestation_in_interview": "The participant stated that retaining the in-rack allowance would have kept more margin against classification uncertainty, but he recommended pulling it to hit the owner's number because he did not want the relationship strained. He also said he did not lay out the classification uncertainty in as much detail as he could have and framed the removal as a reasonable trade-off.",
      "effect_on_reasoning_or_decision": "The owner received a recommendation to remove margin under uncertainty and did not receive a full explanation of how much design margin was being given up, biasing the value-engineering trade-off toward the participant's relationship goal.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Retaining it would've kept more margin against the classification uncertainty, since I knew the plastics content wasn't fully confirmed yet. But we've got two more retrofit jobs pending with this same owner, and I didn't want that relationship to get strained over this one line item, so I recommended pulling the in-rack allowance to hit his number.",
          "evidence_explanation": "This shows that the decision to remove the in-rack allowance was motivated by preserving the owner relationship and future work, not solely by a technical risk assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not in as much detail as I probably could have. I mentioned it in passing but framed the removal as a reasonable trade-off rather than walking him through how much margin we'd be giving up.",
          "evidence_explanation": "This demonstrates selective communication of risk information: the participant knew the uncertainty was material but framed the recommendation in a way that supported the relationship goal."
        }
      ],
      "correction_or_counterevidence": "No direct correction is described. The later full flow test at commissioning passed, though the value came in close to the required minimum. The participant acknowledged he could have presented the classification uncertainty in more detail. There is a plausible professional judgment element in budget trade-offs, but the transcript indicates relationship motivation specifically shaped the recommendation and information sharing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific corpus passages were supplied with this interview; the classification relies on established cognitive-science knowledge rather than retrieved corpus evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring bias",
      "alternative_labels": ["insufficient adjustment"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Density/area selection for hydraulic design",
      "supporting_interview_quote": "I took the first density/area point that cleared the minimum for the assumed classification and built the calc package around it. We were up against the submission deadline, and that point technically satisfied the requirement, so I ran with it rather than working through the other combinations.",
      "plausible_mechanism": "The first code-compliant density/area point may have served as an anchor, or the participant may have narrowed the evaluation of alternatives prematurely; the plan reviewer's later note that the point was close to the edge of the applicable curve could indicate a biased restriction of alternatives.",
      "why_not_identified": "The transcript describes a deadline-driven selection of the first acceptable code-compliant option, which is more consistent with satisficing/bounded rationality than with a distinct cognitive bias. It does not affirmatively show that an irrelevant anchor distorted evaluation of the other density/area points, so it does not meet the occurrence threshold."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific corpus was supplied with this interview; bias labels and definitions are drawn from established cognitive-science knowledge rather than validated against retrieved source passages.",
    "The analysis is based solely on the participant's self-report, so internal reasoning processes are inferred from verbal behavior.",
    "The interview is a single account and may not capture all decision-relevant information or organizational context."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Biased_3_Gemini_off",
  "interview_id": "HE_Biased_3",
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
