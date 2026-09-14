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
[ontology-free RAG JSON output]
</RAG_ANALYSIS_OUTPUT>
