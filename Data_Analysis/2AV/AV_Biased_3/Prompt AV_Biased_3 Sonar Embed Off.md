You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. Just to confirm, this is a cognitive task analysis interview—I'll ask about a specific turnaround you handled, and I'd like you to walk me through your reasoning as it happened, not just the outcome. Nothing here is evaluative of your performance. Can you tell me your role and roughly how long you've been doing it?

Participant: Sure. I'm a load controller, been doing it about nine years now, mostly narrow-body combi ops. On a normal day I'm building load sheets, issuing loading instructions to the ramp, checking weight and balance against structural limits, and making sure the NOTOC is accurate before the captain gets it. This particular one was a standard 45-minute turnaround, nothing scheduled to be unusual about it.

Interviewer: Walk me through what happened, from when you first got involved.

Participant: I got the initial cargo manifest about an hour before departure. Mixed load—regular baggage, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what we usually put through, not on a pallet. Our load-control software generates an automatic load instruction—the ALI—and it put that machinery item into hold 3. The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated so they could start loading, because we were already tight on time. About twenty minutes later, after the ramp had loaded per that instruction, they called up and said the aircraft was sitting slightly tail-heavy on the jacks reading—not out of limits, just noticeably aft of where we'd expect for that load.

Interviewer: What did you do at that point?

Participant: I logged it and kept moving, because we still had the last-minute change to deal with. About that time, an LMC came in—roughly 380 kilos of mail plus six late bags that hadn't made the original manifest. The mail got assigned to hold 5, which is our aft bulk hold, smaller one. I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route—we'd had three similar ones, same ballpark, and none of those needed any redistribution. So I cleared it on that basis and moved to finalize the trim sheet.

Interviewer: And the trim sheet—what informed that?

Participant: I pulled up the dispatch log because I wanted a sanity check before signing off, given the tail-heavy reading from the ramp. I saw that the two previous flights on this same rotation—different tail numbers, one had gone to a different destination—had both needed aft trim adjustments. That, plus what the ramp had just told me, made me think the rotation itself was running tail-heavy that day, so I shifted some of the cargo distribution forward before finalizing, beyond what my own computed index actually called for.

Interviewer: Let's slow down and go through each of these moments individually. Starting with the ALI and the machinery item—what specifically told you it was fine to issue as generated?

Participant: Mainly just experience with the system. It's been accurate for months on this fleet, and we don't have time in a 45-minute turn to hand-check every ALI. I did register that the item was irregular, non-palletized, heavier than usual—that did cross my mind—but the system's had a good run, so I went with it.

Interviewer: Was there a manual limits chart you could have checked against for that item specifically?

Participant: There is one, for exactly this kind of non-standard cargo. I know it exists. I just didn't pull it that time.

Interviewer: What would have made you stop and check it?

Participant: If the system itself had flagged it somehow—like if it had kicked back a warning saying "verify manually," I'd have stopped. Since it didn't, I treated it the same as any other ALI.

Interviewer: Moving to the LMC decision—what exactly did you compare when the mail and bags came in?

Participant: Total weight against the week's pattern. That's the number I had readily in my head from the previous LMCs.

Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs had gone?

Participant: Not specifically, no. The earlier ones went into a forward hold, I believe—hold 2 typically. This one went aft into 5. I didn't run the index shift for that specific placement; I just used the weight comparison as my check.

Interviewer: What would it have taken to run that index calculation directly instead?

Participant: A couple of extra minutes with the trim computer, honestly. It wasn't unavailable—I just didn't feel it was necessary given how the weight lined up.

Interviewer: Let's talk about the trim sheet redistribution. What was your reasoning connecting the two previous flights to this one?

Participant: They were on the same rotation, back to back, both needed aft correction. Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift as a margin before I signed off.

Interviewer: At the time, what did your own calculated index for this flight actually show?

Participant: It was within the normal range on its own, forward of the aft limit with margin. The redistribution wasn't because my numbers were bad—it was more that I didn't fully trust that after seeing two prior aft trims.

Interviewer: Did you look into why those two prior flights ran tail-heavy?

Participant: Not at the time. I found out afterward one was a fuel imbalance and the other had extra catering loaded late. Different tails, different causes, nothing tying them to each other.

Interviewer: Last one—the final sign-off. What was the situation there?

Participant: Closeout figures were within limits, looked clean. But the ramp tally was one bag short of what the NOTOC and manifest showed. Small discrepancy, and we were right up against the slot.

Interviewer: What did you decide, and what were you weighing?

Participant: I signed and released with the figures as they stood. I weighed the delay risk—losing the slot—against a one-bag discrepancy that's usually a clerical miscount, not a safety issue on its own. It resolved itself afterward as a manifest correction; the weight and balance conclusion didn't change. I could see someone making the other call too, holding a few minutes to chase it down. It wasn't an easy one either way.

Interviewer: Looking back across the whole sequence, how confident were you in each of those calls at the time versus now?

Participant: The ALI and the LMC I was fairly confident on in the moment—maybe more than I'd be now, knowing how it played out. The trim redistribution I was less sure about even then; it felt more like caution than certainty. The final sign-off, I'm still not fully sure I made the "right" call, but I don't think it was wrong given what I had.

Interviewer: If the software had required a manual check for irregular cargo shapes before finalizing the ALI, do you think that changes how this played out?

Participant: Probably, yes. If it forced me to open the manual chart, I would have caught the hold 3 placement issue before the ramp ever loaded it.

Interviewer: And if the mail had gone into the usual forward hold instead of hold 5?

Participant: Then the weight comparison I used would have actually been a fair proxy, because placement wouldn't have mattered much. It was really the aft location that made the comparison misleading, not the comparison itself.

Interviewer: If you'd known upfront that the two prior tail-heavy events had unrelated causes, would you have redistributed the cargo the same way?

Participant: No, I don't think I would have. I'd have trusted my own numbers for this flight instead of layering in a correction based on what happened to two other tails.

Interviewer: Anything you'd do differently if this exact sequence happened again?

Participant: Pull the manual chart for anything irregular regardless of the system's history, and separate what the current flight's numbers say from what the last couple of flights did, unless I actually know there's a shared cause. The last-minute change is the one I'd still have to think about—weight alone clearly wasn't the full picture that day.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Biased_3",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Load Controller / Loadmaster (Commercial)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Late Reload and Trim Discrepancy on a Narrow-Body Turnaround",
    "scenario_summary_internal": "A commercial load controller finalizing a weight-and-balance load sheet during a tight 45-minute turnaround must reconcile an automatically generated load instruction for an atypical heavy/irregular cargo item, absorb a last-minute cargo change (LMC) into the trim calculation, interpret a short recent history of tail-heavy trim events on the same aircraft rotation, and finally decide whether to hold departure briefly to re-verify a minor bag-count discrepancy before signing off. The scenario is designed to surface one instance each of automation bias (over-reliance on the load-control software's automatically generated instruction for an atypical cargo type), substitution bias (answering an easier proxy question about aggregate LMC weight similarity instead of the harder question of placement-specific index impact), and apophenia/correlation bias (inferring a causal recurring 'tail-heavy rotation' pattern from two unrelated, temporally adjacent trim events). The final decision point is left genuinely ambiguous and bias-free to avoid mechanically signaling outcome-based bias attribution.",
    "occupational_realism": {
      "objective": "Produce and sign off a compliant final load sheet (weight, balance, and CG within structural and CG envelope limits) in time to meet the departure slot, while correctly incorporating a non-standard cargo item and a late cargo addition.",
      "setting": "Regional hub airport ramp and load control office during a scheduled 45-minute narrow-body turnaround; combi passenger/cargo configuration with belly holds 1-5.",
      "constraints": [
        "Fixed departure slot with limited buffer before ATC slot loss",
        "Atypical, irregularly shaped machinery cargo requiring non-standard hold placement",
        "Late cargo/baggage change (LMC) received after initial load instruction was generated",
        "Dangerous goods segregation and NOTOC accuracy requirements",
        "Structural per-hold and cumulative weight limits",
        "Reliance on a load-control software system (ALI generator) validated for standard palletized loads",
        "Ramp crew and dispatcher time pressure competing with verification thoroughness"
      ],
      "stakeholders": [
        "Load controller (interviewee)",
        "Ramp supervisor",
        "Ground handling agents",
        "Dispatcher / operations control",
        "Captain (recipient of NOTOC and final load sheet)"
      ],
      "technical_terms_to_use": [
        "load sheet", "weight and balance (W&B)", "center of gravity (CG)", "unit load device (ULD)",
        "automatic load instruction (ALI)", "last-minute change (LMC)", "NOTOC", "zero fuel weight (ZFW)",
        "trim sheet", "index units", "mean aerodynamic chord (MAC)", "bulk hold", "closeout figures"
      ],
      "technical_terms_to_avoid": [
        "automation bias", "substitution bias", "apophenia", "correlation bias", "heuristic",
        "cognitive bias", "anchoring", "pattern recognition error"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Load-control software has generated a correct ALI for this fleet type over many months",
          "An irregularly shaped machinery cargo item (heavier and non-palletized) has been assigned to hold 3 by the ALI",
          "Turnaround time is tight; ramp crew is waiting on final hold assignment to begin loading"
        ],
        "new_information_after_decision": [
          "Ramp later reports the aircraft trimming slightly tail-heavy after loading per the ALI-assigned placement"
        ],
        "alternatives": [
          "Accept the automatically generated ALI as-is and issue loading instructions immediately",
          "Independently cross-check the ALI's hold assignment for the irregular machinery item against the manual structural limits chart before issuing instructions"
        ],
        "intended_action": "Loadmaster accepts the ALI output without the independent manual cross-check specifically indicated for non-standard/irregular cargo, citing the system's long track record of accuracy."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "An LMC of approximately 380kg of mail plus 6 late bags arrives after the initial load sheet was drafted",
          "The mail is assigned to aft hold 5, a smaller hold not typically used for this route's routine LMCs",
          "The past three flights this week had LMCs of comparable total weight that did not require redistribution"
        ],
        "new_information_after_decision": [
          "The specific aft placement in hold 5 produces a larger index/moment shift than prior weeks' LMCs, which were placed forward"
        ],
        "alternatives": [
          "Run a full recalculation of the index/moment shift specific to placing this LMC in hold 5",
          "Judge the LMC acceptable based on its total weight being similar to this week's routine LMCs, without checking placement-specific index impact"
        ],
        "intended_action": "Loadmaster judges the LMC acceptable primarily because its aggregate weight resembles this week's typical LMCs, without independently verifying the placement-specific index effect of the aft hold assignment."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch log shows the previous two flights on this aircraft rotation (different tail numbers, one to a different destination) required aft trim adjustments",
          "This flight's own computed index, based on its actual load configuration, falls within the normal forward range",
          "Time is limited before the trim sheet must be finalized"
        ],
        "new_information_after_decision": [
          "The two prior tail-heavy events are later attributed to unrelated causes: one to a fuel imbalance, the other to additional catering load, not a rotation-wide pattern"
        ],
        "alternatives": [
          "Base the trim sheet strictly on this flight's own computed index and load configuration",
          "Pre-emptively shift cargo distribution forward because the same rotation trended tail-heavy on the two preceding flights"
        ],
        "intended_action": "Loadmaster pre-emptively redistributes cargo forward based on an inferred recurring 'tail-heavy rotation' pattern drawn from two unrelated preceding events, rather than relying on this flight's own within-limits computed index."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Closeout figures appear balanced and within limits under the current load sheet",
          "A minor discrepancy of one bag count is noted between the ramp tally and the NOTOC/baggage manifest",
          "The departure slot window is closing, and holding for re-verification risks a delay"
        ],
        "new_information_after_decision": [
          "The bag-count discrepancy is resolved shortly after release, either matching a clerical miscount or requiring a minor manifest correction, without changing the overall weight and balance conclusion"
        ],
        "alternatives": [
          "Sign and release the final load sheet with the current closeout figures",
          "Request a short hold to re-verify the closeout figures and bag count against the NOTOC before final sign-off"
        ],
        "intended_action": "Loadmaster weighs the operational cost of a short hold against the apparent minor nature of the discrepancy and makes a judgment call; no intended bias is embedded here, and either choice remains professionally defensible."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe your role and what a typical turnaround like this one involves?",
        "Walk me through what this particular flight's load planning looked like from the start."
      ],
      "timeline_reconstruction": [
        "What was the first piece of information you received about the cargo mix for this flight?",
        "When did the last-minute change come in, and how did that change your plan?",
        "What did the trim history for this rotation look like leading up to this flight?",
        "What happened right before you finalized and signed the load sheet?"
      ],
      "decision_point_probes": [
        "What specific cues told you the automated load instruction was ready to use as generated?",
        "What information sources did you consult when the mail and late bags came in, and what did you rely on most?",
        "What was your goal when you decided to adjust the cargo distribution forward before finalizing the trim sheet?",
        "What alternatives did you consider at each of these points, and why did you choose the path you did?",
        "How much time pressure were you under at each of these moments, and how did that affect your approach?",
        "How confident were you in each of these judgments at the time, versus after the fact?",
        "Had you seen similar situations before in your experience, and how did that shape your response this time?"
      ],
      "closing_hypotheticals": [
        "If the load-control software had flagged the irregular machinery cargo as requiring mandatory manual verification, do you think your process would have changed?",
        "If the LMC mail had been placed in the usual forward hold instead of hold 5, would your assessment have differed?",
        "Looking back, if you had known the two prior tail-heavy events had unrelated causes, would you have redistributed the cargo the same way?",
        "What would you do differently if you faced this exact sequence of events again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "au_01",
        "bias": "Automaticity or Automation Bias",
        "decision_point": 1,
        "mechanism": "Over-reliance on the automatically generated ALI for an atypical, irregularly shaped machinery cargo item, treating the system's general track record on standard palletized loads as sufficient justification to skip the manual cross-check specifically indicated for non-standard cargo.",
        "affected_reasoning_operation": "Verification/checking of a system-generated output before acting on it",
        "evidence_available_at_time": [
          "System's consistent accuracy over months on standard loads",
          "Awareness that this cargo item is irregular and non-standard",
          "Time pressure from tight turnaround"
        ],
        "required_textual_manifestation": "Loadmaster explicitly cites the system's past reliability as the reason for not independently checking the hold assignment for the atypical item, despite acknowledging its non-standard nature.",
        "plausible_nonbias_interpretation": "Reasonable trust in a validated tool under time constraints, consistent with normal operational reliance on certified systems.",
        "strength": "subtle",
        "do_not_make_explicit": ["automation bias", "over-reliance", "system trust heuristic"]
      },
      {
        "instance_id": "sub_01",
        "bias": "Substitution bias",
        "decision_point": 2,
        "mechanism": "Replacing the harder question ('what precise index/moment shift does this specific LMC placement in hold 5 produce') with an easier proxy question ('does this LMC's total weight resemble this week's routine LMCs'), and treating the proxy answer as resolving the original question.",
        "affected_reasoning_operation": "Evaluation of whether a new piece of evidence (the LMC) requires a full recalculation",
        "evidence_available_at_time": [
          "Total weight of the new LMC (~380kg plus 6 bags)",
          "Historical pattern of similar-weight LMCs this week",
          "Fact that this LMC's hold placement (aft, hold 5) differs from prior LMCs (forward holds)"
        ],
        "required_textual_manifestation": "Loadmaster states or implies that the LMC was judged acceptable mainly by comparing its total weight to past LMCs, without describing a placement-specific index check for hold 5.",
        "plausible_nonbias_interpretation": "A reasonable use of pattern-based experience to triage low-risk changes under time pressure, when weight similarity is genuinely informative in most cases.",
        "strength": "subtle",
        "do_not_make_explicit": ["substitution bias", "proxy question", "attribute substitution"]
      },
      {
        "instance_id": "ap_01",
        "bias": "Apophenia or Correlation Bias",
        "decision_point": 3,
        "mechanism": "Inferring a causal, recurring 'tail-heavy rotation' pattern from two temporally adjacent but causally unrelated trim events on different tail numbers, and using that inferred pattern to override this flight's own within-limits computed index.",
        "affected_reasoning_operation": "Causal attribution and generalization from a small, coincidental sample to guide a current decision",
        "evidence_available_at_time": [
          "Two prior flights on the same rotation logged aft trim adjustments",
          "Those two flights differed in tail number and one differed in destination",
          "This flight's own index, computed from its actual load, was within normal forward range"
        ],
        "required_textual_manifestation": "Loadmaster explains the pre-emptive forward redistribution by referencing the rotation's recent trim history as if it were a causal or recurring property of the rotation, rather than treating the two events as potentially coincidental.",
        "plausible_nonbias_interpretation": "A cautious, experience-based safety margin applied given recent operational history, which is a defensible judgment call absent further information.",
        "strength": "subtle",
        "do_not_make_explicit": ["apophenia", "correlation bias", "illusory pattern", "small sample"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario was requested for this generation (paired_scenario_id = NONE)."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence of a mandatory manual cross-check flag in the load-control software for irregular/non-standard cargo shapes",
      "original_state": "The software does not flag irregular or non-palletized cargo for mandatory independent manual verification before the ALI is issued",
      "counterfactual_state": "The software flags irregular/non-palletized cargo and requires an independent manual cross-check before the ALI can be finalized",
      "variables_to_hold_constant": [
        "Turnaround time window", "Cargo mix and weights", "LMC content and timing", "Rotation trim history", "Crew and stakeholder roles"
      ],
      "expected_causal_difference": "Under the counterfactual state, the automation-bias instance at decision point 1 would be structurally prevented or substantially weakened, since the mandatory flag would force the manual check that was otherwise skipped.",
      "causal_test_question": "Would the loadmaster still bypass independent verification of the atypical cargo placement if the software itself required a manual cross-check flag to be cleared first?"
    },
    "generation_checks": [
      "Exactly 3 total intended bias instances planned, matching the manifest sum (1+1+1)",
      "Exactly 4 decision points defined, each with at least two alternatives",
      "Each bias instance assigned to a distinct decision point (DP1, DP2, DP3); DP4 left intentionally neutral/ambiguous",
      "No bias terminology or psychological labels appear in probe plan or timeline text",
      "Each instance has a plausible non-bias interpretation distinct from its intended mechanism",
      "Decision point 4 contains no intended bias instance and has a genuinely ambiguous, non-mechanical outcome",
      "Target word count (1,215-1,485 words) is achievable given four decision points with probes, without repetitive exposition"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Substitution bias", "occurrences": 1, "mechanism_constraint": "Must manifest as answering an easier proxy question (aggregate weight similarity) in place of the harder question (placement-specific index/moment impact) at decision point 2." },
      { "bias": "Apophenia or Correlation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as inferring a causal recurring pattern from two temporally adjacent but causally unrelated trim events at decision point 3." },
      { "bias": "Automaticity or Automation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as bypassing an independent manual check on an automated system output specifically for an atypical/non-standard case at decision point 1." }
    ],
    "target_bias_names": [
      "Substitution bias",
      "Apophenia or Correlation Bias",
      "Automaticity or Automation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Substitution bias", "requested_occurrences": 1 },
      { "bias": "Apophenia or Correlation Bias", "requested_occurrences": 1 },
      { "bias": "Automaticity or Automation Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias" },
      { "instance_id": "sub_01", "bias": "Substitution bias" },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias", "decision_point": 1 },
      { "instance_id": "sub_01", "bias": "Substitution bias", "decision_point": 2 },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "au_01",
        "bias": "Automaticity or Automation Bias",
        "mechanism": "Skipping manual cross-check for irregular cargo based on general system reliability",
        "affected_reasoning_operation": "Verification of system-generated output before action",
        "evidence_source": "ALI output plus known irregularity of the machinery cargo item",
        "distinctiveness_requirement": "Must be the only instance in the interview where a system output is accepted without a check specifically warranted by an atypical case; not repeated elsewhere."
      },
      {
        "instance_id": "sub_01",
        "bias": "Substitution bias",
        "mechanism": "Substituting an easier proxy question (weight similarity) for the harder question (placement-specific index impact)",
        "affected_reasoning_operation": "Evaluation of whether new evidence (LMC) requires full recalculation",
        "evidence_source": "LMC weight and placement data compared against historical LMC pattern",
        "distinctiveness_requirement": "Must be the only instance where a harder quantitative question is answered via an easier proxy comparison; distinct from the automation-bias instance in that no automated system output is involved, only the loadmaster's own reasoning shortcut."
      },
      {
        "instance_id": "ap_01",
        "bias": "Apophenia or Correlation Bias",
        "mechanism": "Inferring a causal recurring pattern from two coincidental, causally unrelated prior events",
        "affected_reasoning_operation": "Causal attribution/generalization applied to override a current, independently valid computed value",
        "evidence_source": "Trim log history of two preceding flights on the same rotation",
        "distinctiveness_requirement": "Must be the only instance involving inference of a causal pattern from a small historical sample; distinct from sub_01, which involves comparing current data to past data without asserting causality."
      }
    ],
    "intended_strength": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias", "strength": "subtle" },
      { "instance_id": "sub_01", "bias": "Substitution bias", "strength": "subtle" },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence of a mandatory manual cross-check flag in the load-control software for irregular/non-standard cargo shapes",
      "original_state": "No mandatory flag; irregular cargo processed like standard cargo by the ALI generator",
      "changed_state": "Mandatory flag requires independent manual verification before ALI finalization for irregular cargo",
      "variables_to_hold_constant": [
        "Turnaround time window", "Cargo mix and weights", "LMC content and timing", "Rotation trim history", "Crew and stakeholder roles"
      ]
    },
    "scenario_id": "AV_Biased_3",
    "domain_id": "AV",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Each of the three requested biases was assigned to exactly one distinct decision point (DP1, DP2, DP3) chosen for mechanism fit and narrative realism: automation bias to the automated-system-reliance moment (DP1), substitution bias to the quantitative-verification-shortcut moment (DP2), and apophenia/correlation bias to the causal-pattern-inference moment (DP3). Decision point 4 was deliberately left free of intended bias instances to preserve an ambiguous, non-mechanical outcome as required by CTA design rules.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Turnaround time window", "Cargo mix and weights", "LMC content and timing", "Rotation trim history", "Crew and stakeholder roles", "Aircraft type and route"
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
        "segment_type": "decision_episode",
        "raw_interview_anchor": "The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "au_01"
        ],
        "ground_truth_rationale": "The participant accepted an automated instruction for atypical cargo without the available manual cross-check, relying on the system's general reliability."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "I logged it and kept moving, because we still had the last-minute change to deal with.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a continuation decision under time pressure, without a hidden bias instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route... So I cleared it on that basis.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sub_01"
        ],
        "ground_truth_rationale": "The participant used aggregate weight similarity instead of evaluating the placement-specific index impact of the aft hold assignment."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ap_01"
        ],
        "ground_truth_rationale": "The participant inferred a recurring causal rotation pattern from two unrelated prior events and overrode the current flight's own computed index."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification leaves this operational tradeoff neutral and professionally defensible."
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
    "analysis_scope_note": "Analysis focused on the participant's real-time reasoning statements. Retrospective statements were used only where they clarify an earlier reasoning mechanism; no identified occurrence depends solely on later outcome information."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "illusory correlation",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation bias",
      "alternative_labels": ["automation-induced complacency", "overreliance on automation"],
      "taxonomy_status": "established_label",
      "bias_definition": "Overreliance on an automated decision-support system, such that the system's output is accepted without sufficient independent verification, especially when the decision maker notices potentially relevant discrepancies or unusual features.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "ALI issuance for irregular machinery item",
      "decision_point_description": "Whether to manually verify the automated load instruction for an irregular, non-palletized, heavier-than-usual cargo item before issuing the ALI to the ramp.",
      "affected_reasoning_operation": "Acceptance and issuance of the automated load instruction without manual verification",
      "bias_specific_mechanism": "The participant's trust in the load-control software's historical accuracy substituted for manual checking, even though he explicitly registered that the cargo item was irregular, non-palletized, and heavier than usual. The absence of an automated warning was treated as sufficient evidence that no manual chart check was needed.",
      "manifestation_in_interview": "The participant stated the system had been reliable, issued the ALI essentially as generated, acknowledged that the irregular cargo crossed his mind, and admitted he did not pull the manual limits chart even though it existed for exactly this kind of non-standard cargo.",
      "effect_on_reasoning_or_decision": "He issued the ALI to the ramp without manually checking hold 3 placement for the irregular cargo, allowing loading to proceed before the problem was identified.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated so they could start loading, because we were already tight on time.",
          "evidence_explanation": "This explicitly connects reliance on the system's historical reliability to the decision to issue the automated instruction without manual verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did register that the item was irregular, non-palletized, heavier than usual—that did cross my mind—but the system's had a good run, so I went with it.",
          "evidence_explanation": "Shows a noticed anomaly was overridden by generalized trust in automation, the core automation-bias mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There is one, for exactly this kind of non-standard cargo. I know it exists. I just didn't pull it that time.",
          "evidence_explanation": "Confirms an available independent check existed and was not used, strengthening the attribution to automation reliance rather than lack of information."
        }
      ],
      "correction_or_counterevidence": "The participant was under real time pressure in a 45-minute turnaround, and the automated system had a long error-free history on the fleet, so using it as the default may have been a reasonable operational heuristic. However, the participant himself identifies that the irregular cargo should have triggered a manual chart check.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available for this analysis; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "representativeness heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging whether a present case requires action by the ease with which similar recent instances come to mind, rather than by analyzing the decision-relevant features of the current case.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "LMC clearance for late mail and bags",
      "decision_point_description": "Whether to clear the 380 kg mail plus six late bags assigned to aft hold 5 without running an index-shift calculation for the specific placement.",
      "affected_reasoning_operation": "Risk assessment and clearance of the last-minute change",
      "bias_specific_mechanism": "The participant compared the current LMC's total weight to three recent LMCs that were readily available in memory and concluded no redistribution was needed. This ease-of-recall comparison substituted for examining the current LMC's placement—hold 5 aft versus the earlier forward hold 2—which was decision-relevant for weight and balance.",
      "manifestation_in_interview": "The participant said the previous LMC weights were readily in his head, used that comparison as his check, and did not check placement or run an index shift.",
      "effect_on_reasoning_or_decision": "He cleared the LMC and moved to finalize without correcting for the aft placement, which he later says made the weight comparison misleading.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route—we'd had three similar ones, same ballpark, and none of those needed any redistribution. So I cleared it on that basis and moved to finalize the trim sheet.",
          "evidence_explanation": "This shows the participant used a comparison to recent similar LMCs rather than a calculation based on the current load's placement."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Total weight against the week's pattern. That's the number I had readily in my head from the previous LMCs.",
          "evidence_explanation": "This directly indicates availability from memory guided the comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not specifically, no. The earlier ones went into a forward hold, I believe—hold 2 typically. This one went aft into 5. I didn't run the index shift for that specific placement; I just used the weight comparison as my check.",
          "evidence_explanation": "This confirms the participant omitted the decision-relevant placement information that would have distinguished the current LMC from the recalled instances."
        }
      ],
      "correction_or_counterevidence": "Time pressure and recent comparable LMCs provided a plausible heuristic basis; if the placement had matched previous LMCs, the weight comparison might have been a fair proxy. The participant's later statement does not by itself prove bias, but the affirmative failure to check placement indicates the heuristic substituted for the relevant analysis.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available for this analysis; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "illusory correlation",
      "alternative_labels": ["clustering illusion", "insensitivity to sample size", "belief in the law of small numbers"],
      "taxonomy_status": "established_label",
      "bias_definition": "Perceiving a systematic relationship or trend when none exists, particularly by overinferring from a small number of co-occurring or salient events.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Trim sheet forward redistribution after observed prior aft trims",
      "decision_point_description": "Whether to redistribute cargo forward beyond the participant's own computed index for this flight based on the two previous flights plus a current ramp tail-heavy reading.",
      "affected_reasoning_operation": "Trim sheet cargo distribution decision",
      "bias_specific_mechanism": "The participant took two consecutive aft-trim events on the same rotation as evidence that the rotation itself was running tail-heavy that day, despite the events involving different tail numbers and no known common cause. He then layered a forward correction onto his own within-limits computed index.",
      "manifestation_in_interview": "He said 'Two in a row felt like enough to say something was going on with how this rotation was trending that day.' He did not investigate causes at the time; afterward the causes were unrelated.",
      "effect_on_reasoning_or_decision": "He shifted cargo forward beyond what his own current-flight index required, distrusting his own calculation because of a perceived rotation-level trend.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I saw that the two previous flights on this same rotation—different tail numbers, one had gone to a different destination—had both needed aft trim adjustments. That, plus what the ramp had just told me, made me think the rotation itself was running tail-heavy that day, so I shifted some of the cargo distribution forward before finalizing, beyond what my own computed index actually called for.",
          "evidence_explanation": "This shows the participant inferred a rotation-level trend from two previous aft-trim events and acted beyond his own flight-specific calculation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "They were on the same rotation, back to back, both needed aft correction. Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift as a margin before I signed off.",
          "evidence_explanation": "The phrase 'two in a row felt like enough' explicitly indicates overinference from a small sample."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at the time. I found out afterward one was a fuel imbalance and the other had extra catering loaded late. Different tails, different causes, nothing tying them to each other.",
          "evidence_explanation": "This supports the illusory nature of the perceived rotation-level correlation: the two events had unrelated causes."
        }
      ],
      "correction_or_counterevidence": "The ramp's current tail-heavy reading provided some independent local evidence, and adding a forward margin could be viewed as a conservative load-control decision under uncertainty. However, the participant's own calculated index was within limits and he declined to investigate causes before treating the two prior events as a trend.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available for this analysis; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific corpus passages were available in the RAG context, so the labels and mechanisms are assigned from general cognitive-science knowledge and should not be treated as corpus-supported.",
    "The interview is retrospective self-report, so the present account may be shaped by later knowledge or self-presentation.",
    "Some decisions occurred under real operational time pressure, which may reduce the diagnostic specificity of heuristic use as a cognitive bias.",
    "The analysis does not presume that any decision outcome was unsafe or incorrect; it focuses only on the reasoning mechanisms evidenced in the transcript."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Biased_3_Sonar_off",
  "interview_id": "AV_Biased_3",
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
