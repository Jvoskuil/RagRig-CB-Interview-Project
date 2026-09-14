<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just so you know, I'll ask you to walk through a specific turnaround and explain your thinking as it unfolded, not just what ended up happening. Can you tell me your role and a bit about your background?

Participant: Sure. I've been a load controller about nine years, mostly narrow-body combi work. Normally I build the load sheet, issue the loading instruction to the ramp, check weight and balance against structural limits, and finalize the NOTOC for the captain. This one wasn't a normal turn, though—the inbound aircraft came in late, so instead of our usual 45 minutes on the ground, we were looking at more like 30 before the slot.

Interviewer: How did that change things going in?

Participant: Right away I knew I'd be compressing steps I'd normally spread out a bit more. Nothing about the flight itself was unusual—same route, same aircraft type—it was just less time to work with.

Interviewer: Walk me through what happened.

Participant: I got the cargo manifest with about 30 minutes left. Mixed load—regular bags, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what typically goes through, not palletized. Our load-control software generates an automatic load instruction, and it put that machinery item into hold 3. That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately. About fifteen minutes later, the ramp called and said the aircraft was sitting slightly tail-heavy—not out of limits, just aft of where you'd expect.

Interviewer: What did you do with that?

Participant: Logged it and kept going, because right then an LMC came in—about 380 kilos of mail plus six late bags that missed the original manifest. That mail got assigned to hold 5, our aft bulk hold. With the time we had left, I looked at the total weight, saw it was in line with the LMCs we'd been getting all week on this route—three similar ones, same range, none of those needed redistribution—and cleared it on that basis so I could move to the trim sheet.

Interviewer: And the trim sheet itself?

Participant: I pulled the dispatch log for a quick check, given the tail-heavy call from the ramp. Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required.

Interviewer: Let's go through each of those moments in more detail. Starting with the ALI and the machinery item—what specifically told you it was fine to run with as generated?

Participant: Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me.

Interviewer: Was there a manual chart you could have checked against for that kind of cargo?

Participant: There is, for exactly that situation. I know where it is. I just didn't reach for it that day.

Interviewer: What would have made you stop and pull it?

Participant: If we'd had the full 45, probably. Or if the system itself had thrown some kind of flag saying this needs manual sign-off. Neither of those happened, so I treated it like any other ALI.

Interviewer: On the LMC—what exactly did you compare when the mail and bags came in?

Participant: Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest.

Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs went?

Participant: No, not specifically. The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it.

Interviewer: What would it have taken to run that calculation directly?

Participant: A few extra minutes at the trim computer. It wasn't unavailable to me. I just didn't think it was worth the time against the schedule we were on.

Interviewer: On the trim sheet redistribution—how did you connect the two previous flights to this one?

Participant: They were on the same rotation, back to back, and both needed aft correction. Two in a row felt like it meant something about how the rotation was running that day, so I built in a forward shift before signing off, and honestly, with the time we had left, I didn't feel like there was room to dig into it further.

Interviewer: What did your own calculated index for this flight show on its own?

Participant: It was fine—within the normal forward range with margin. The redistribution wasn't because my numbers were bad. It was more that seeing two prior aft trims made me not fully trust it, and I didn't have the minutes to sit with that discomfort.

Interviewer: Did you find out afterward why those two flights ran tail-heavy?

Participant: Yeah—one was a fuel imbalance, the other had extra catering loaded late. Different tails, unrelated causes. Nothing tying them to each other or to this flight.

Interviewer: Last one—the final sign-off. What was the situation?

Participant: Closeout figures looked clean, within limits. But the ramp tally was one bag short of the NOTOC and manifest. Small discrepancy, and the slot was closing faster than a normal turn would allow.

Interviewer: What did you decide, and what were you weighing?

Participant: I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself. It turned out to be a manifest correction afterward—the weight and balance conclusion didn't change. I can see someone holding a couple minutes to chase it down instead. Neither call feels obviously wrong to me.

Interviewer: How confident were you in each of these at the time, versus now?

Participant: The ALI and the LMC, fairly confident in the moment, more than I'd be now looking back. The trim redistribution, less sure even then—it felt like caution more than certainty. The sign-off, I'm still not positive I made the better call, but I don't think it was unreasonable given the time.

Interviewer: If you'd had the full 45 minutes instead of 30, would you have handled the machinery cargo differently?

Participant: Probably, yes. I think I'd have pulled the manual chart. The shorter window is what pushed me to just trust the system's history instead.

Interviewer: If the mail had gone to the usual forward hold instead of hold 5?

Participant: Then the weight comparison would've actually held up fine, since placement wouldn't have mattered as much. It was the aft location that made that comparison misleading, not the comparison itself.

Interviewer: If you'd known upfront the two prior tail-heavy events were unrelated, would you have redistributed the same way?

Participant: No. I'd have trusted my own numbers for this flight instead of layering in a correction based on two other tails.

Interviewer: Anything you'd do differently facing this same sequence again, under the same shortened window?

Participant: Pull the manual chart for anything irregular no matter how tight the clock is, and keep this flight's numbers separate from what happened on previous ones unless I actually know there's a shared cause. The LMC piece I'd still have to think through—weight alone wasn't the full story that day, and less time made that easier to miss, not harder.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Counterfactual_3",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Load Controller / Loadmaster (Commercial)",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Late Reload and Trim Discrepancy on a Compressed Narrow-Body Turnaround",
    "scenario_summary_internal": "This is the causal-variable counterfactual pairing of AV_Biased_3. The incident, cargo mix, LMC, rotation trim history, and final bag-count discrepancy are held materially constant. The single causal variable changed is the length of the turnaround window: instead of a routine 45-minute turnaround, an inbound delay compresses the ground time to approximately 30 minutes before the fixed departure slot. All other facts, actors, and the sequence of four decision points are preserved so that any difference in the load controller's reasoning can be attributed to the tighter time window rather than to a different incident. The same three intended bias instances are implemented at the same decision points as in the base scenario: automation bias at decision point 1 (accepting the automatically generated load instruction for atypical cargo without an independent manual cross-check), substitution bias at decision point 2 (using aggregate LMC weight similarity as a proxy for placement-specific index verification), and apophenia/correlation bias at decision point 3 (inferring a causal recurring trim pattern from two unrelated preceding events). Decision point 4 remains neutral and genuinely ambiguous.",
    "occupational_realism": {
      "objective": "Produce and sign off a compliant final load sheet (weight, balance, and CG within structural and CG envelope limits) before a fixed departure slot that now allows less buffer than usual, while correctly incorporating a non-standard cargo item and a late cargo addition.",
      "setting": "Regional hub airport ramp and load control office; ground time compressed to roughly 30 minutes because the inbound aircraft arrived late, on a narrow-body combi aircraft with belly holds 1-5.",
      "constraints": [
        "Compressed ~30-minute turnaround due to a delayed inbound aircraft, with the same fixed departure slot as originally scheduled",
        "Atypical, irregularly shaped machinery cargo requiring non-standard hold placement",
        "Late cargo/baggage change (LMC) received after the initial load instruction was generated",
        "Dangerous goods segregation and NOTOC accuracy requirements",
        "Structural per-hold and cumulative weight limits",
        "Reliance on a load-control software system (ALI generator) validated for standard palletized loads",
        "Heightened ramp crew and dispatcher time pressure relative to the base scenario, competing with verification thoroughness"
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
          "Inbound delay has compressed ground time to about 30 minutes, less than the usual 45",
          "Load-control software has generated a correct ALI for this fleet type over many months",
          "An irregularly shaped machinery cargo item (heavier and non-palletized) has been assigned to hold 3 by the ALI",
          "Ramp crew is waiting, now with less buffer than usual, for the final hold assignment"
        ],
        "new_information_after_decision": [
          "Ramp later reports the aircraft trimming slightly tail-heavy after loading per the ALI-assigned placement"
        ],
        "alternatives": [
          "Accept the automatically generated ALI as-is and issue loading instructions immediately given the shorter window",
          "Independently cross-check the ALI's hold assignment for the irregular machinery item against the manual structural limits chart before issuing instructions"
        ],
        "intended_action": "Loadmaster accepts the ALI output without the independent manual cross-check specifically indicated for non-standard/irregular cargo, citing the system's long track record of accuracy and the now-tighter schedule."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "An LMC of approximately 380kg of mail plus 6 late bags arrives after the initial load sheet was drafted, with even less time remaining than in a normal turn",
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
        "intended_action": "Loadmaster judges the LMC acceptable primarily because its aggregate weight resembles this week's typical LMCs, without independently verifying the placement-specific index effect of the aft hold assignment, under greater time constraint than the base scenario."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch log shows the previous two flights on this aircraft rotation (different tail numbers, one to a different destination) required aft trim adjustments",
          "This flight's own computed index, based on its actual load configuration, falls within the normal forward range",
          "Very little time remains before the trim sheet must be finalized given the compressed window"
        ],
        "new_information_after_decision": [
          "The two prior tail-heavy events are later attributed to unrelated causes: one to a fuel imbalance, the other to additional catering load, not a rotation-wide pattern"
        ],
        "alternatives": [
          "Base the trim sheet strictly on this flight's own computed index and load configuration",
          "Pre-emptively shift cargo distribution forward because the same rotation trended tail-heavy on the two preceding flights"
        ],
        "intended_action": "Loadmaster pre-emptively redistributes cargo forward based on an inferred recurring 'tail-heavy rotation' pattern drawn from two unrelated preceding events, rather than relying on this flight's own within-limits computed index, reasoning that there is no time left to investigate further."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Closeout figures appear balanced and within limits under the current load sheet",
          "A minor discrepancy of one bag count is noted between the ramp tally and the NOTOC/baggage manifest",
          "The compressed departure slot window is closing faster than usual, and holding for re-verification risks a delay"
        ],
        "new_information_after_decision": [
          "The bag-count discrepancy is resolved shortly after release, either matching a clerical miscount or requiring a minor manifest correction, without changing the overall weight and balance conclusion"
        ],
        "alternatives": [
          "Sign and release the final load sheet with the current closeout figures",
          "Request a short hold to re-verify the closeout figures and bag count against the NOTOC before final sign-off"
        ],
        "intended_action": "Loadmaster weighs the operational cost of a short hold, now more costly given the compressed schedule, against the apparent minor nature of the discrepancy, and makes a judgment call; no intended bias is embedded here, and either choice remains professionally defensible."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe your role and what this particular turnaround looked like compared to a typical one?",
        "Walk me through what changed when you learned the ground time would be shorter than planned."
      ],
      "timeline_reconstruction": [
        "What was the first piece of information you received about the cargo mix for this flight?",
        "When did the last-minute change come in, and how did the shorter window affect how you handled it?",
        "What did the trim history for this rotation look like leading up to this flight?",
        "What happened right before you finalized and signed the load sheet, given how little time was left?"
      ],
      "decision_point_probes": [
        "What specific cues told you the automated load instruction was ready to use as generated, especially with less time available?",
        "What information sources did you consult when the mail and late bags came in, and what did you rely on most under that time constraint?",
        "What was your goal when you decided to adjust the cargo distribution forward before finalizing the trim sheet?",
        "What alternatives did you consider at each of these points, and did the shorter window change which alternative felt realistic?",
        "How much time pressure were you under at each of these moments compared to a normal turn, and how did that affect your approach?",
        "How confident were you in each of these judgments at the time, versus after the fact?",
        "Had you seen similar situations before in your experience, and how did that shape your response this time?"
      ],
      "closing_hypotheticals": [
        "If you had had the full 45 minutes instead of 30, do you think you would have handled the machinery cargo differently?",
        "If the LMC mail had been placed in the usual forward hold instead of hold 5, would your assessment have differed?",
        "Looking back, if you had known the two prior tail-heavy events had unrelated causes, would you have redistributed the cargo the same way?",
        "What would you do differently if you faced this exact sequence of events again, with the same shortened window?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "au_01",
        "bias": "Automaticity or Automation Bias",
        "decision_point": 1,
        "mechanism": "Over-reliance on the automatically generated ALI for an atypical, irregularly shaped machinery cargo item, treating the system's general track record on standard palletized loads as sufficient justification to skip the manual cross-check specifically indicated for non-standard cargo, now reinforced by the compressed schedule.",
        "affected_reasoning_operation": "Verification/checking of a system-generated output before acting on it",
        "evidence_available_at_time": [
          "System's consistent accuracy over months on standard loads",
          "Awareness that this cargo item is irregular and non-standard",
          "Heightened time pressure from the compressed ~30-minute turnaround"
        ],
        "required_textual_manifestation": "Loadmaster explicitly cites the system's past reliability and the shorter window as reasons for not independently checking the hold assignment for the atypical item, despite acknowledging its non-standard nature.",
        "plausible_nonbias_interpretation": "Reasonable trust in a validated tool under an unusually tight schedule, consistent with normal operational triage when time is scarce.",
        "strength": "subtle",
        "do_not_make_explicit": ["automation bias", "over-reliance", "system trust heuristic"]
      },
      {
        "instance_id": "sub_01",
        "bias": "Substitution bias",
        "decision_point": 2,
        "mechanism": "Replacing the harder question ('what precise index/moment shift does this specific LMC placement in hold 5 produce') with an easier proxy question ('does this LMC's total weight resemble this week's routine LMCs'), and treating the proxy answer as resolving the original question, under greater time scarcity than the base scenario.",
        "affected_reasoning_operation": "Evaluation of whether a new piece of evidence (the LMC) requires a full recalculation",
        "evidence_available_at_time": [
          "Total weight of the new LMC (~380kg plus 6 bags)",
          "Historical pattern of similar-weight LMCs this week",
          "Fact that this LMC's hold placement (aft, hold 5) differs from prior LMCs (forward holds)"
        ],
        "required_textual_manifestation": "Loadmaster states or implies that the LMC was judged acceptable mainly by comparing its total weight to past LMCs, without describing a placement-specific index check for hold 5, and references the shorter window as part of the justification.",
        "plausible_nonbias_interpretation": "A reasonable use of pattern-based experience to triage low-risk changes under unusually tight time pressure, when weight similarity is genuinely informative in most cases.",
        "strength": "subtle",
        "do_not_make_explicit": ["substitution bias", "proxy question", "attribute substitution"]
      },
      {
        "instance_id": "ap_01",
        "bias": "Apophenia or Correlation Bias",
        "decision_point": 3,
        "mechanism": "Inferring a causal, recurring 'tail-heavy rotation' pattern from two temporally adjacent but causally unrelated trim events on different tail numbers, and using that inferred pattern to override this flight's own within-limits computed index, with the compressed schedule cited as the reason further investigation was skipped.",
        "affected_reasoning_operation": "Causal attribution and generalization from a small, coincidental sample to guide a current decision",
        "evidence_available_at_time": [
          "Two prior flights on the same rotation logged aft trim adjustments",
          "Those two flights differed in tail number and one differed in destination",
          "This flight's own index, computed from its actual load, was within normal forward range"
        ],
        "required_textual_manifestation": "Loadmaster explains the pre-emptive forward redistribution by referencing the rotation's recent trim history as if it were a causal or recurring property of the rotation, rather than treating the two events as potentially coincidental, and notes there was no time left to check further.",
        "plausible_nonbias_interpretation": "A cautious, experience-based safety margin applied given recent operational history and limited time, which is a defensible judgment call absent further information.",
        "strength": "subtle",
        "do_not_make_explicit": ["apophenia", "correlation bias", "illusory pattern", "small sample"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "AV_Biased_3",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is a counterfactual pairing, not a vocabulary or ambiguous control."
    },
    "counterfactual_specification": {
      "causal_variable": "Length of the turnaround window before the fixed departure slot",
      "original_state": "A routine 45-minute turnaround with no additional schedule compression (as in AV_Biased_3)",
      "counterfactual_state": "A compressed ~30-minute turnaround caused by a delayed inbound aircraft, with the same fixed departure slot",
      "variables_to_hold_constant": [
        "Cargo mix and weights, including the irregular machinery item",
        "LMC content, weight, and hold placement",
        "Rotation trim history and its two prior unrelated causes",
        "Aircraft type and route",
        "Actors and stakeholder roles",
        "ALI system behavior and its lack of a mandatory manual-check flag",
        "The final bag-count discrepancy and its resolution"
      ],
      "expected_causal_difference": "The same three reasoning patterns (automation reliance, weight-based proxy judgment, and unrelated-event pattern inference) are expected to persist, but should be framed more explicitly around time scarcity as the stated justification, testing whether the same bias mechanisms are attributed mainly to the shorter window rather than disappearing under greater pressure.",
      "causal_test_question": "Does compressing the turnaround from 45 to 30 minutes change how strongly the load controller invokes time pressure as the reason for the same three reasoning shortcuts, without changing whether those shortcuts occur?"
    },
    "generation_checks": [
      "Exactly 3 total intended bias instances planned, matching the manifest sum (1+1+1)",
      "Exactly 4 decision points defined, each with at least two alternatives",
      "Each bias instance assigned to a distinct decision point (DP1, DP2, DP3), matching the base scenario's assignment; DP4 left intentionally neutral/ambiguous",
      "Only the turnaround-window variable and its direct time-pressure framing differ from AV_Biased_3; all other material facts are held constant",
      "No bias terminology or psychological labels appear in probe plan or timeline text",
      "Each instance has a plausible non-bias interpretation distinct from its intended mechanism",
      "Decision point 4 contains no intended bias instance and has a genuinely ambiguous, non-mechanical outcome",
      "Target word count (1,215-1,485 words) is achievable given four decision points with probes, without repetitive exposition"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Substitution bias", "occurrences": 1, "mechanism_constraint": "Must manifest as answering an easier proxy question (aggregate weight similarity) in place of the harder question (placement-specific index/moment impact) at decision point 2, with time scarcity cited as contributing justification." },
      { "bias": "Apophenia or Correlation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as inferring a causal recurring pattern from two temporally adjacent but causally unrelated trim events at decision point 3, with time scarcity cited as the reason further checking was skipped." },
      { "bias": "Automaticity or Automation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as bypassing an independent manual check on an automated system output specifically for an atypical/non-standard case at decision point 1, with the compressed schedule cited as reinforcing justification." }
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
        "mechanism": "Skipping manual cross-check for irregular cargo based on general system reliability, reinforced by compressed schedule framing",
        "affected_reasoning_operation": "Verification of system-generated output before action",
        "evidence_source": "ALI output plus known irregularity of the machinery cargo item plus stated 30-minute window",
        "distinctiveness_requirement": "Must be the only instance in the interview where a system output is accepted without a check specifically warranted by an atypical case; not repeated elsewhere."
      },
      {
        "instance_id": "sub_01",
        "bias": "Substitution bias",
        "mechanism": "Substituting an easier proxy question (weight similarity) for the harder question (placement-specific index impact), reinforced by compressed schedule framing",
        "affected_reasoning_operation": "Evaluation of whether new evidence (LMC) requires full recalculation",
        "evidence_source": "LMC weight and placement data compared against historical LMC pattern, under stated time scarcity",
        "distinctiveness_requirement": "Must be the only instance where a harder quantitative question is answered via an easier proxy comparison; distinct from au_01 in that no automated system output is involved."
      },
      {
        "instance_id": "ap_01",
        "bias": "Apophenia or Correlation Bias",
        "mechanism": "Inferring a causal recurring pattern from two coincidental, causally unrelated prior events, reinforced by compressed schedule framing",
        "affected_reasoning_operation": "Causal attribution/generalization applied to override a current, independently valid computed value",
        "evidence_source": "Trim log history of two preceding flights on the same rotation, under stated time scarcity",
        "distinctiveness_requirement": "Must be the only instance involving inference of a causal pattern from a small historical sample; distinct from sub_01, which involves comparing current data to past data without asserting causality."
      }
    ],
    "intended_strength": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias", "strength": "subtle" },
      { "instance_id": "sub_01", "bias": "Substitution bias", "strength": "subtle" },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": "AV_Biased_3",
    "counterfactual_variable": {
      "name": "Length of the turnaround window before the fixed departure slot",
      "original_state": "Routine 45-minute turnaround with no additional schedule compression",
      "changed_state": "Compressed ~30-minute turnaround due to a delayed inbound aircraft, same fixed departure slot",
      "variables_to_hold_constant": [
        "Cargo mix and weights, including the irregular machinery item",
        "LMC content, weight, and hold placement",
        "Rotation trim history and its two prior unrelated causes",
        "Aircraft type and route",
        "Actors and stakeholder roles",
        "ALI system behavior and its lack of a mandatory manual-check flag",
        "The final bag-count discrepancy and its resolution"
      ]
    },
    "scenario_id": "AV_Counterfactual_3",
    "domain_id": "AV",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Each of the three requested biases was assigned to exactly one distinct decision point (DP1, DP2, DP3), mirroring the allocation used in the paired base scenario AV_Biased_3, so that only the turnaround-window causal variable differs between the pair. Decision point 4 was deliberately left free of intended bias instances to preserve an ambiguous, non-mechanical outcome, consistent with the base scenario.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Cargo mix and weights, including the irregular machinery item",
      "LMC content, weight, and hold placement",
      "Rotation trim history and its two prior unrelated causes",
      "Aircraft type and route",
      "Actors and stakeholder roles",
      "ALI system behavior and its lack of a mandatory manual-check flag",
      "The final bag-count discrepancy and its resolution"
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
        "segment_type": "context_reasoning",
        "raw_interview_anchor": "Right away I knew I'd be compressing steps I'd normally spread out a bit more. Nothing about the flight itself was unusual—it was just less time to work with.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This explains operational compression caused by the shortened turnaround but does not itself contain a hidden bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The irregular machinery item was assigned to hold 3 by the automatic load instruction, and the participant issued the ALI as generated because the system had been reliable and time was short; follow-up confirms the available manual chart was not used.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "au_01"
        ],
        "ground_truth_rationale": "Decision point 1 contains the intended automation-bias mechanism: an automated output for atypical cargo was accepted without the situation-specific manual cross-check, with system reliability and schedule compression cited as reasons."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The participant cleared the 380-kilogram mail and six late bags in aft hold 5 after comparing total weight with three recent LMCs, without calculating the placement-specific index shift.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sub_01"
        ],
        "ground_truth_rationale": "Decision point 2 contains the intended substitution mechanism: aggregate weight similarity was used as an easier proxy for the harder placement-specific index calculation under time scarcity."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The participant inferred that the rotation was running tail-heavy from the ramp report and two prior aft-trim events, then shifted cargo forward beyond what the current flight's own index required.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ap_01"
        ],
        "ground_truth_rationale": "Decision point 3 contains the intended apophenia/correlation mechanism: a recurring causal pattern was inferred from two temporally adjacent events and used to override valid current-flight data."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The participant signed and released with a one-bag discrepancy after weighing delay risk against the possibility of a routine miscount; the discrepancy was later corrected without changing the W&B conclusion.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Decision point 4 is deliberately neutral and genuinely ambiguous. The participant made an explicit operational risk tradeoff, and either sign-off or a short hold was professionally defensible."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective_recommendation",
        "raw_interview_anchor": "The participant recommended pulling the manual chart for irregular cargo and keeping the current flight's numbers separate from prior flights unless a shared cause is known, while remaining uncertain about the LMC issue.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective recommendation and uncertainty statement, not an additional hidden occurrence."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[ontology-free RAG JSON output]
</RAG_ANALYSIS_OUTPUT>
